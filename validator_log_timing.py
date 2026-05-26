#!/usr/bin/env python3
"""Estimate validator lock-window timing from live W&B / console logs."""
from __future__ import annotations

import re
import statistics
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

from agent_common import parse_log_timestamp


# ── Log patterns ─────────────────────────────────────────────────────────────

_LOCK_TS = re.compile(
    r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+Locked (transformer|mamba2) revisions"
)
_UID_SLOT_TS = re.compile(
    r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+\[(\d+)/(\d+)\]\s+UID (\d+)\s+\|"
)
_GATE_TS = re.compile(
    r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+Gate\s+(PASS|FAIL)"
)


def extract_uid_slot(line: str, uid: int) -> tuple[int, int] | None:
    """Return (slot_index, slot_total) from a UID eval header line."""
    m = _UID_SLOT_TS.search(line)
    if not m or int(m.group(4)) != uid:
        return None
    return int(m.group(2)), int(m.group(3))


def parse_lock_events(
    lines: list[str],
    *,
    track: str = "transformer",
) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    track_l = track.lower()
    for ln in lines:
        m = _LOCK_TS.search(ln)
        if not m or m.group(2).lower() != track_l:
            continue
        ts = parse_log_timestamp(m.group(1))
        if ts is None:
            continue
        out.append({"timestamp": m.group(1), "unix": ts.timestamp(), "track": track_l})
    return out


_ANY_UID_TS = re.compile(
    r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\s+\[\d+/\d+\]\s+UID \d+\s+\|"
)


def parse_uid_eval_events(lines: list[str], uid: int) -> list[dict[str, Any]]:
    """One record per UID eval block: start, slot, gate."""
    events: list[dict[str, Any]] = []
    i = 0
    n = len(lines)
    while i < n:
        m = _UID_SLOT_TS.search(lines[i])
        if not m or int(m.group(4)) != uid:
            i += 1
            continue
        start_ts = m.group(1)
        slot = int(m.group(2))
        total = int(m.group(3))
        gate_ts = ""
        gate_result = ""
        j = i + 1
        while j < n:
            if _ANY_UID_TS.search(lines[j]):
                break
            gm = _GATE_TS.search(lines[j])
            if gm:
                gate_ts = gm.group(1)
                gate_result = gm.group(2)
                break
            j += 1
        start_dt = parse_log_timestamp(start_ts)
        gate_dt = parse_log_timestamp(gate_ts) if gate_ts else None
        events.append(
            {
                "start_timestamp": start_ts,
                "gate_timestamp": gate_ts,
                "start_unix": start_dt.timestamp() if start_dt else None,
                "gate_unix": gate_dt.timestamp() if gate_dt else None,
                "slot": slot,
                "total": total,
                "gate": gate_result,
                "eval_duration_s": (
                    (gate_dt - start_dt).total_seconds()
                    if start_dt and gate_dt
                    else None
                ),
            }
        )
        i = j + 1 if gate_ts else i + 1
    return events


def _median(values: list[float], default: float) -> float:
    if not values:
        return default
    return float(statistics.median(values))


def _clamp(v: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, v))


@dataclass
class ValidatorTimingModel:
    """Rolling stats inferred from validator console logs."""

    track: str = "transformer"
    round_duration_s: float = 1800.0
    seconds_per_slot_s: float = 36.0
    post_gate_window_s: float = 720.0
    sample_lock_intervals: int = 0
    sample_post_gate_windows: int = 0
    last_lock_unix: float | None = None
    last_lock_timestamp: str = ""
    source: str = "defaults"

    def to_dict(self) -> dict[str, Any]:
        return {
            "track": self.track,
            "round_duration_s": self.round_duration_s,
            "seconds_per_slot_s": self.seconds_per_slot_s,
            "post_gate_window_s": self.post_gate_window_s,
            "sample_lock_intervals": self.sample_lock_intervals,
            "sample_post_gate_windows": self.sample_post_gate_windows,
            "last_lock_unix": self.last_lock_unix,
            "last_lock_timestamp": self.last_lock_timestamp,
            "source": self.source,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any] | None) -> ValidatorTimingModel:
        if not data:
            return cls()
        return cls(
            track=str(data.get("track") or "transformer"),
            round_duration_s=float(data.get("round_duration_s") or 1800.0),
            seconds_per_slot_s=float(data.get("seconds_per_slot_s") or 36.0),
            post_gate_window_s=float(data.get("post_gate_window_s") or 720.0),
            sample_lock_intervals=int(data.get("sample_lock_intervals") or 0),
            sample_post_gate_windows=int(data.get("sample_post_gate_windows") or 0),
            last_lock_unix=data.get("last_lock_unix"),
            last_lock_timestamp=str(data.get("last_lock_timestamp") or ""),
            source=str(data.get("source") or "cached"),
        )


def build_timing_model(
    lines: list[str],
    *,
    uid: int,
    track: str = "transformer",
    cached: ValidatorTimingModel | None = None,
) -> ValidatorTimingModel:
    """Infer round duration and per-UID post-gate windows from log history."""
    locks = parse_lock_events(lines, track=track)
    uid_events = parse_uid_eval_events(lines, uid)

    model = cached or ValidatorTimingModel(track=track.lower())
    if locks:
        model.last_lock_unix = locks[-1]["unix"]
        model.last_lock_timestamp = locks[-1]["timestamp"]

    # Lock-to-lock round durations (10–45 min sane range).
    lock_intervals: list[float] = []
    for a, b in zip(locks, locks[1:]):
        dt = b["unix"] - a["unix"]
        if 600 <= dt <= 2700:
            lock_intervals.append(dt)
    if lock_intervals:
        model.round_duration_s = _median(lock_intervals, model.round_duration_s)
        model.sample_lock_intervals = len(lock_intervals)

    # Per-miner eval duration and slot pacing.
    eval_durs = [e["eval_duration_s"] for e in uid_events if e.get("eval_duration_s")]
    if eval_durs:
        model.seconds_per_slot_s = _median(eval_durs, model.seconds_per_slot_s)

    totals = [e["total"] for e in uid_events if e.get("total")]
    default_total = int(statistics.median(totals)) if totals else 50

    # Measured post-gate → next-lock windows for this UID.
    post_gate: list[float] = []
    for ev in uid_events:
        if ev.get("gate_unix") is None:
            continue
        gate_u = float(ev["gate_unix"])
        nxt = next((lk["unix"] for lk in locks if lk["unix"] > gate_u), None)
        if nxt is not None:
            w = nxt - gate_u
            if 60 <= w <= 2400:
                post_gate.append(w)

    if post_gate:
        model.post_gate_window_s = _median(post_gate, model.post_gate_window_s)
        model.sample_post_gate_windows = len(post_gate)
    elif lock_intervals and uid_events:
        # Estimate from slot position in the most recent completed eval.
        last = uid_events[-1]
        slot = int(last.get("slot") or default_total // 2)
        total = int(last.get("total") or default_total)
        frac_done = _clamp(slot / max(1, total), 0.05, 0.98)
        remaining_frac = 1.0 - frac_done
        model.post_gate_window_s = _clamp(
            model.round_duration_s * remaining_frac,
            120.0,
            model.round_duration_s,
        )

    if model.sample_lock_intervals or model.sample_post_gate_windows:
        model.source = "log_analysis"
    elif cached is not None:
        model.source = cached.source
    else:
        model.source = "defaults"

    return model


def estimate_lock_window(
    eval_rec: dict[str, Any],
    model: ValidatorTimingModel,
    *,
    locks: list[dict[str, Any]] | None = None,
    now_unix: float | None = None,
    pipeline_age_s: float | None = None,
    safety_margin_s: float = 90.0,
) -> dict[str, Any]:
    """Estimate seconds from gate (or now) until the next validator lock."""
    now = time.time() if now_unix is None else float(now_unix)
    gate_ts = str(eval_rec.get("gate_timestamp") or eval_rec.get("timestamp") or "")
    gate_dt = parse_log_timestamp(gate_ts)
    gate_unix = gate_dt.timestamp() if gate_dt else None

    slot = eval_rec.get("slot")
    total = eval_rec.get("total")
    if slot is None or total is None:
        raw = eval_rec.get("raw_block") or []
        if raw:
            parsed = extract_uid_slot(raw[0], int(eval_rec.get("uid") or 0))
            if parsed:
                slot, total = parsed
    slot_i = int(slot) if slot is not None else 0
    total_n = int(total) if total is not None else 50

    lock_list = locks or []
    lock_before: float | None = None
    lock_after: float | None = None
    if gate_unix is not None and lock_list:
        before = [lk["unix"] for lk in lock_list if lk["unix"] <= gate_unix]
        after = [lk["unix"] for lk in lock_list if lk["unix"] > gate_unix]
        if before:
            lock_before = max(before)
        if after:
            lock_after = min(after)
    elif model.last_lock_unix is not None and gate_unix is not None:
        if model.last_lock_unix <= gate_unix:
            lock_before = model.last_lock_unix
        else:
            lock_after = model.last_lock_unix

    post_gate_at_gate = float(model.post_gate_window_s)
    if gate_unix is not None and lock_before is not None and lock_before <= gate_unix:
        elapsed_in_round = gate_unix - lock_before
        post_gate_at_gate = max(
            60.0,
            model.round_duration_s - elapsed_in_round,
        )
    elif slot_i > 0 and total_n > 0:
        remaining_frac = 1.0 - _clamp(slot_i / total_n, 0.0, 0.99)
        post_gate_at_gate = max(60.0, model.round_duration_s * remaining_frac)

    if gate_unix is not None:
        next_lock_est = gate_unix + post_gate_at_gate
        remaining_s = next_lock_est - now
    else:
        remaining_s = post_gate_at_gate - (pipeline_age_s or 0.0)

    if pipeline_age_s is None and eval_rec.get("pipeline_trigger_unix") is not None:
        try:
            pipeline_age_s = max(0.0, now - float(eval_rec["pipeline_trigger_unix"]))
        except (TypeError, ValueError):
            pipeline_age_s = None

    lock_after_gate = lock_after is not None
    if lock_after_gate:
        remaining_s = min(remaining_s, -1.0)

    return {
        "timing_mode": "dynamic_log",
        "post_gate_window_s": post_gate_at_gate,
        "remaining_until_lock_s": remaining_s,
        "next_lock_est_unix": (gate_unix + post_gate_at_gate) if gate_unix else None,
        "gate_unix": gate_unix,
        "gate_timestamp": gate_ts,
        "slot": slot_i,
        "total_miners": total_n,
        "round_duration_s": model.round_duration_s,
        "seconds_per_slot_s": model.seconds_per_slot_s,
        "safety_margin_s": safety_margin_s,
        "lock_after_gate": lock_after_gate,
        "lock_before_unix": lock_before,
        "lock_after_unix": lock_after,
        "pipeline_age_s": pipeline_age_s,
        "model": model.to_dict(),
    }


def enrich_eval_record(eval_rec: dict[str, Any], lines: list[str], uid: int) -> dict[str, Any]:
    """Add slot, gate_timestamp, and timing fields to an eval record."""
    raw = eval_rec.get("raw_block") or []
    if raw:
        slot = extract_uid_slot(raw[0], uid)
        if slot:
            eval_rec["slot"] = slot[0]
            eval_rec["total"] = slot[1]
    for ln in raw:
        gm = _GATE_TS.search(ln)
        if gm:
            eval_rec["gate_timestamp"] = gm.group(1)
            break
    return eval_rec


def timing_state_key(uid: int, track: str = "transformer") -> str:
    return f"validator_timing:uid{uid}:{track.lower()}"


def load_timing_model_from_state(state: dict[str, Any], uid: int, track: str = "transformer") -> ValidatorTimingModel | None:
    raw = state.get(timing_state_key(uid, track))
    if isinstance(raw, dict):
        return ValidatorTimingModel.from_dict(raw)
    return None


def save_timing_model_to_state(
    state: dict[str, Any],
    uid: int,
    model: ValidatorTimingModel,
    track: str = "transformer",
) -> None:
    state[timing_state_key(uid, track)] = model.to_dict()
