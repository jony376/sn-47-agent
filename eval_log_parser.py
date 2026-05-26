#!/usr/bin/env python3
"""Parse validator console eval blocks for a target miner UID."""
from __future__ import annotations

import re
from datetime import datetime, timezone
from typing import Any


def _uid_start_patterns(uid: int) -> list[re.Pattern[str]]:
    return [
        re.compile(
            rf"^(\d{{4}}-\d{{2}}-\d{{2}} \d{{2}}:\d{{2}}:\d{{2}})\s+\[\d+/\d+\]\s+UID {uid}\s+\|\s+(.+?)\s+@$"
        ),
        re.compile(rf"^\s*\[\d+/\d+\]\s+UID {uid}\s+\|\s+(.+?)\s+@$"),
    ]


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
        "model_revision": _extract_revision(block, 0, len(block)),
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
