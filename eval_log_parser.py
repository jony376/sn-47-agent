#!/usr/bin/env python3
"""Parse validator console eval blocks for a target miner UID."""
from __future__ import annotations

import re
from datetime import datetime, timezone
from typing import Any


_ANSI_RE = re.compile(r"\x1b\[[0-9;?]*[A-Za-z]")
# Box-drawing (┃ │) and plain pipe characters used as leaderboard column separators.
_BAR_RE = re.compile(r"[│┃|]")
# Known per-track section headers inside a "Current Leaderboard:" block.
_TRACK_HEADERS = {"TRANSFORMER", "MAMBA2", "MAMBA", "GLM"}


def _strip_ansi(line: str) -> str:
    return _ANSI_RE.sub("", line)


def _leaderboard_top_row(lines: list[str], start: int, end: int, track: str) -> tuple[int, int, float] | None:
    """Return (rank, uid, score) for rank 1 of `track` within lines[start:end]."""
    section: int | None = None
    for i in range(start, end):
        if _strip_ansi(lines[i]).strip().upper() == track:
            section = i
            break
    if section is None:
        return None
    for i in range(section + 1, end):
        text = _strip_ansi(lines[i])
        if text.strip().upper() in _TRACK_HEADERS:
            return None  # reached the next track section without a data row
        parts = [p.strip() for p in _BAR_RE.split(text) if p.strip()]
        # Data rows look like: Rank | UID | Score | Loss | ... (rank + uid numeric).
        if len(parts) >= 3 and parts[0].isdigit() and parts[1].isdigit():
            try:
                score = float(parts[2])
            except ValueError:
                score = 0.0
            return int(parts[0]), int(parts[1]), score
    return None


def parse_top_uid_from_leaderboard(lines: list[str], track: str = "transformer") -> dict[str, Any]:
    """Find the current top miner for a track from validator "Current Leaderboard" tables.

    Validators print a leaderboard each eval cycle, ranked by Score (higher = better).
    At the start of a cycle every miner is reset to Score 0.0 / Loss 10.0, so the most
    recent block can be meaningless. We therefore scan blocks newest-first and return
    rank 1 from the most recent block whose top score is > 0, falling back to the latest
    block if none has a positive score.
    """
    track_u = track.strip().upper()
    starts = [i for i, ln in enumerate(lines) if "Current Leaderboard" in _strip_ansi(ln)]
    if not starts:
        raise RuntimeError("No 'Current Leaderboard' block found in log")

    fallback: dict[str, Any] | None = None
    for bi in range(len(starts) - 1, -1, -1):
        block_start = starts[bi]
        block_end = starts[bi + 1] if bi + 1 < len(starts) else len(lines)
        row = _leaderboard_top_row(lines, block_start, block_end, track_u)
        if row is None:
            continue
        rank, uid, score = row
        result = {"uid": uid, "rank": rank, "score": score, "track": track}
        if fallback is None:
            fallback = result
        if score > 0:
            return result
    if fallback is not None:
        return fallback
    raise RuntimeError(f"No leaderboard rows found for track {track!r}")


def _uid_start_patterns(uid: int) -> list[re.Pattern[str]]:
    return [
        re.compile(
            rf"^(\d{{4}}-\d{{2}}-\d{{2}} \d{{2}}:\d{{2}}:\d{{2}})\s+\[\d+/\d+\]\s+UID {uid}\s+\|\s+(.+?)\s+@(?:\s.*)?$"
        ),
        re.compile(rf"^\s*\[\d+/\d+\]\s+UID {uid}\s+\|\s+(.+?)\s+@(?:\s.*)?$"),
    ]


# Some validator runs print the revision inline on the header line:
#   [38/51] UID 102 | owner/repo @ <40-hex-sha> | hotkey 5DFZ...
# while others terminate the header with " @" and put the SHA on a later line.
_HEADER_INLINE_SHA = re.compile(r"\s@\s+([0-9a-f]{40})")


def _header_inline_sha(line: str) -> str:
    m = _HEADER_INLINE_SHA.search(line)
    return m.group(1) if m else ""


def _uid_block_start(line: str, uid: int) -> tuple[str, str] | None:
    m = _uid_start_patterns(uid)[0].search(line)
    if m:
        return m.group(1), m.group(2).strip()
    m = _uid_start_patterns(uid)[1].search(line)
    if m:
        return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S"), m.group(1).strip()
    return None


def _next_uid_block_index(lines: list[str], after: int) -> int | None:
    pat = re.compile(r"^\s*(?:\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\s+)?\[\d+/\d+\]\s+UID \d+\s+\|")
    for i in range(after + 1, len(lines)):
        if pat.search(lines[i]):
            return i
    return None


def _extract_revision(lines: list[str], start: int, end: int) -> str:
    rev_ts = re.compile(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\s+([0-9a-f]{40})\s+\|")
    rev_plain = re.compile(r"^\s*([0-9a-f]{40})\s+\|")
    for ln in lines[start:end]:
        for pat in (rev_ts, rev_plain):
            m = pat.search(ln)
            if m:
                return m.group(1)
    return ""


def parse_latest_eval_for_uid(lines: list[str], uid: int) -> dict[str, Any]:
    gate_pat = re.compile(
        r"Gate\s+(PASS|FAIL).+cur=([0-9.]+)\s+req<=([0-9.]+)\s+prev=([0-9.]+)"
    )
    kl_pat = re.compile(r"\|\s+KL\s+([0-9.]+)\s+\|\s+NextKL\s+([0-9.]+)")

    # Normalize away terminal color codes so parsing works regardless of which
    # validator run (colored or plain) produced the log.
    lines = [_strip_ansi(ln) for ln in lines]

    starts: list[int] = []
    for i, ln in enumerate(lines):
        if _uid_start_patterns(uid)[0].search(ln) or _uid_start_patterns(uid)[1].search(ln):
            starts.append(i)
    if not starts:
        raise RuntimeError(f"No eval block found for UID {uid}")

    s_idx = starts[-1]
    e_idx = _next_uid_block_index(lines, s_idx) or len(lines)
    block = lines[s_idx:e_idx]

    parsed = _uid_block_start(block[0], uid)
    assert parsed is not None
    timestamp, model_repo = parsed

    slot_m = re.search(r"\[(\d+)/(\d+)\]\s+UID", block[0])
    slot_index = int(slot_m.group(1)) if slot_m else None
    slot_total = int(slot_m.group(2)) if slot_m else None

    out: dict[str, Any] = {
        "uid": uid,
        "timestamp": timestamp,
        "slot": slot_index,
        "total": slot_total,
        "model_repo": model_repo,
        "model_revision": _header_inline_sha(block[0]) or _extract_revision(block, 0, len(block)),
        "challenge": None,
        "kl": None,
        "next_kl": None,
        "gate": None,
        "cur_kl": None,
        "req_kl": None,
        "prev_kl": None,
        "raw_block": block,
    }
    for ln in block:
        if out["challenge"] is None and "Challenge:" in ln:
            out["challenge"] = ln.split("Challenge:", 1)[1].strip()
        if out["kl"] is None and "| KL " in ln:
            km = kl_pat.search(ln)
            if km:
                out["kl"] = float(km.group(1))
                out["next_kl"] = float(km.group(2))
        if out["gate"] is None and "Gate " in ln:
            gm = gate_pat.search(ln)
            if gm:
                out["gate"] = gm.group(1)
                out["cur_kl"] = float(gm.group(2))
                out["req_kl"] = float(gm.group(3))
                out["prev_kl"] = float(gm.group(4))
                ts_m = re.match(r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})", ln)
                if ts_m:
                    out["gate_timestamp"] = ts_m.group(1)
    return out
