#!/usr/bin/env python3
"""Shared helpers for sn-47-agent bots (revision, timing, state)."""
from __future__ import annotations

import json
import re
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


SHA40_RE = re.compile(r"^[0-9a-f]{40}$")


def load_state(state_path: Path) -> dict[str, Any]:
    if not state_path.exists():
        return {}
    try:
        data = json.loads(state_path.read_text(encoding="utf-8"))
        if isinstance(data, dict):
            return data
    except Exception:
        pass
    return {}


def save_state(state_path: Path, state: dict[str, Any]) -> None:
    state_path.parent.mkdir(parents=True, exist_ok=True)
    state_path.write_text(json.dumps(state, indent=2), encoding="utf-8")


def is_valid_sha(value: str) -> bool:
    return bool(value and SHA40_RE.match(value.strip().lower()))


def resolve_register_revision(uploaded_revision: str, override: str = "") -> str:
    """Pick the on-chain revision to register.

    Default policy: always register the immutable upload SHA.
    Set override to a 40-char SHA for register-only mode, or leave blank/auto.
    """
    override = (override or "").strip()
    uploaded = (uploaded_revision or "").strip().lower()
    if not is_valid_sha(uploaded):
        raise ValueError(f"Invalid uploaded revision SHA: {uploaded_revision!r}")

    if not override or override.lower() in {"auto", "uploaded"}:
        return uploaded

    lowered = override.lower()
    if lowered == "main":
        raise ValueError(
            "REGISTER_REVISION=main is unsafe: validators may lock before main "
            "advances, causing Improve same SHA. Use auto (default) to register "
            "the uploaded commit SHA."
        )

    if not is_valid_sha(override):
        raise ValueError(
            f"REGISTER_REVISION must be auto/uploaded, a 40-char SHA, or empty; "
            f"got {override!r}"
        )
    return override.lower()


def verify_hf_revision(api, repo_id: str, revision: str) -> str:
    info = api.model_info(repo_id=repo_id, revision=revision, files_metadata=False)
    locked = (getattr(info, "sha", None) or revision or "").strip().lower()
    if not is_valid_sha(locked):
        raise RuntimeError(f"HF revision verify failed for {repo_id}@{revision}")
    if locked != revision.lower():
        raise RuntimeError(
            f"HF revision mismatch for {repo_id}: expected {revision}, got {locked}"
        )
    return locked


def parse_log_timestamp(ts: str) -> datetime | None:
    ts = (ts or "").strip()
    if not ts:
        return None
    try:
        return datetime.strptime(ts, "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)
    except ValueError:
        return None


def eval_age_seconds(eval_rec: dict[str, Any]) -> float | None:
    ts = parse_log_timestamp(str(eval_rec.get("timestamp") or ""))
    if ts is None:
        return None
    return max(0.0, (datetime.now(timezone.utc) - ts).total_seconds())


def pipeline_elapsed_seconds(eval_rec: dict[str, Any]) -> float | None:
    """Seconds since the pipeline was triggered (watch mode), if recorded."""
    raw = eval_rec.get("pipeline_trigger_unix")
    if raw is None:
        return None
    try:
        return max(0.0, time.time() - float(raw))
    except (TypeError, ValueError):
        return None


def effective_lock_age_seconds(eval_rec: dict[str, Any]) -> tuple[float | None, str]:
    """Age used for lock-window decisions (prefer trigger time over log timestamp)."""
    import time as _time

    trigger = eval_rec.get("pipeline_trigger_unix")
    if trigger is not None:
        try:
            age = max(0.0, _time.time() - float(trigger))
            return age, "pipeline_trigger"
        except (TypeError, ValueError):
            pass
    log_age = eval_age_seconds(eval_rec)
    if log_age is not None:
        return log_age, "eval_log_timestamp"
    return None, "unknown"


def eval_is_complete(eval_rec: dict[str, Any]) -> bool:
    """True when validator finished scoring (Gate line present)."""
    if eval_rec.get("gate") in ("PASS", "FAIL"):
        return True
    for ln in eval_rec.get("raw_block") or []:
        if "Gate PASS" in ln or "Gate FAIL" in ln:
            return True
    return False


def lock_budget_seconds(validator_eval_interval_s: float, budget_fraction: float) -> float:
    interval = max(60.0, float(validator_eval_interval_s))
    frac = min(0.95, max(0.10, float(budget_fraction)))
    return interval * frac


def assess_lock_risk(
    eval_rec: dict[str, Any],
    *,
    validator_eval_interval_s: float,
    budget_fraction: float = 0.40,
    blocks_remaining_in_epoch: int | None = None,
    block_time_s: float = 12.0,
    max_pipeline_seconds: float | None = None,
    lock_window: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Estimate whether the miner is likely to miss the next validator lock window."""
    age_s, age_source = effective_lock_age_seconds(eval_rec)
    log_age_s = eval_age_seconds(eval_rec)
    timing_mode = "fixed_interval"
    interval = max(60.0, float(validator_eval_interval_s))
    budget_s = lock_budget_seconds(interval, budget_fraction)
    remaining_s: float | None = None

    if lock_window and lock_window.get("timing_mode") == "dynamic_log":
        timing_mode = "dynamic_log"
        post_gate = float(lock_window.get("post_gate_window_s") or interval)
        remaining_s = lock_window.get("remaining_until_lock_s")
        if remaining_s is not None:
            remaining_s = float(remaining_s)
            interval = max(60.0, post_gate)
            budget_s = max(60.0, remaining_s * budget_fraction)
            if lock_window.get("lock_after_gate"):
                budget_s = min(budget_s, 30.0)
        else:
            interval = max(60.0, post_gate)
            budget_s = lock_budget_seconds(interval, budget_fraction)

    if max_pipeline_seconds is not None and max_pipeline_seconds > 0:
        budget_s = min(budget_s, float(max_pipeline_seconds))
    risk = "low"
    reasons: list[str] = []

    if lock_window and timing_mode == "dynamic_log":
        slot = lock_window.get("slot")
        total = lock_window.get("total_miners")
        round_d = lock_window.get("round_duration_s")
        if slot and total:
            reasons.append(
                f"log timing: slot {slot}/{total}, round ~{round_d:.0f}s, "
                f"post-gate window ~{interval:.0f}s"
            )
        if lock_window.get("lock_after_gate"):
            reasons.append(
                "validator locked revisions after this gate — register now or miss "
                "the next improvement window"
            )
            risk = "high"
        elif remaining_s is not None and remaining_s <= 0:
            reasons.append(
                f"estimated {remaining_s:.0f}s until next lock (window closed)"
            )
            risk = "high"

    if age_s is not None:
        label = "pipeline" if age_source == "pipeline_trigger" else "eval log"
        if timing_mode == "dynamic_log" and remaining_s is not None:
            if lock_window and lock_window.get("lock_after_gate"):
                pass  # already high
            elif remaining_s <= 0 or age_s >= max(0.0, remaining_s):
                risk = "high"
                reasons.append(
                    f"{label} age {age_s:.0f}s >= ~{remaining_s:.0f}s remaining until next lock"
                )
            elif age_s >= budget_s:
                if risk != "high":
                    risk = "medium"
                reasons.append(
                    f"{label} age {age_s:.0f}s >= budget {budget_s:.0f}s "
                    f"(~{max(0.0, remaining_s - age_s):.0f}s until next lock)"
                )
            elif age_s >= budget_s * 0.85:
                reasons.append(
                    f"{label} age {age_s:.0f}s; finish upload/register within "
                    f"{max(0.0, remaining_s - age_s):.0f}s (budget {budget_s:.0f}s)"
                )
        elif age_s >= interval:
            risk = "high"
            reasons.append(
                f"{label} age {age_s:.0f}s >= validator loop ~{interval:.0f}s; "
                "next lock likely already used the old SHA"
            )
        elif age_s >= budget_s:
            if risk != "high":
                risk = "medium"
            reasons.append(
                f"{label} age {age_s:.0f}s >= budget {budget_s:.0f}s "
                f"(~{interval - age_s:.0f}s until next lock)"
            )
        elif age_s >= budget_s * 0.85:
            reasons.append(
                f"{label} age {age_s:.0f}s; upload/register should finish within "
                f"{max(0.0, budget_s - age_s):.0f}s"
            )

    if (
        log_age_s is not None
        and age_source == "pipeline_trigger"
        and age_s is not None
        and age_s >= budget_s
    ):
        reasons.append(
            f"pipeline running {age_s:.0f}s (eval log {log_age_s:.0f}s ago); "
            "approaching next validator lock"
        )

    if blocks_remaining_in_epoch is not None and blocks_remaining_in_epoch <= 30:
        est_s = blocks_remaining_in_epoch * block_time_s
        if est_s <= interval:
            reasons.append(
                f"chain epoch ends in ~{est_s:.0f}s ({blocks_remaining_in_epoch} blocks); "
                "validators may lock/eval again soon"
            )
            if risk == "low":
                risk = "medium"

    gate = str(eval_rec.get("gate") or "")
    if "same SHA" in gate or "same sha" in gate.lower():
        reasons.append(
            "last eval failed with Improve same SHA — must upload+register a new SHA "
            "before the next validator lock"
        )
        risk = "high"

    return {
        "risk": risk,
        "age_seconds": age_s,
        "age_source": age_source,
        "eval_log_age_seconds": log_age_s,
        "timing_mode": timing_mode,
        "validator_eval_interval_s": interval,
        "remaining_until_lock_s": remaining_s,
        "budget_seconds": budget_s,
        "budget_fraction": budget_fraction,
        "reasons": reasons,
        "lock_window": lock_window,
    }


def lock_risk_requires_fast_train(lock_risk: dict[str, Any]) -> bool:
    return lock_risk.get("risk") in ("medium", "high")


def lock_risk_should_abort(
    lock_risk: dict[str, Any],
    *,
    abort_high: bool,
    abort_medium: bool,
) -> tuple[bool, str]:
    risk = lock_risk.get("risk", "low")
    if risk == "high" and abort_high:
        return True, "high lock-window risk"
    if risk == "medium" and abort_medium:
        return True, "medium lock-window risk"
    return False, ""


def watch_eval_trigger_key(uid: int) -> str:
    return f"last_watch_triggered_eval_revision:uid{uid}"


def get_subnet_timing(network: str, netuid: int) -> dict[str, Any]:
    import bittensor as bt
    from evolai.validator.config import EPOCH_BLOCKS
    from evolai.validator.epoch_manager import current_epoch

    subtensor = bt.Subtensor(network=network)
    try:
        block = subtensor.get_current_block()
        epoch_num = current_epoch(block, EPOCH_BLOCKS)
        blocks_in_epoch = block % EPOCH_BLOCKS
        blocks_remaining = EPOCH_BLOCKS - blocks_in_epoch
        return {
            "block": block,
            "epoch": epoch_num,
            "epoch_blocks": EPOCH_BLOCKS,
            "blocks_in_epoch": blocks_in_epoch,
            "blocks_remaining_in_epoch": blocks_remaining,
            "seconds_remaining_in_epoch_est": blocks_remaining * 12,
        }
    finally:
        try:
            subtensor.close()
        except Exception:
            pass


def should_skip_duplicate_eval(
    eval_rec: dict[str, Any],
    state: dict[str, Any],
    *,
    uid: int,
) -> tuple[bool, str]:
    """Skip if we already completed a pipeline run for this eval revision."""
    eval_rev = str(eval_rec.get("model_revision") or "").strip().lower()
    if not is_valid_sha(eval_rev):
        return False, "eval revision missing/invalid"

    last_processed = str(state.get(f"last_processed_eval_revision:uid{uid}") or "").lower()
    last_registered = str(state.get(f"last_registered_revision:uid{uid}") or "").lower()

    if last_processed and eval_rev == last_processed:
        if last_registered and last_registered != eval_rev:
            return False, (
                f"eval revision {eval_rev[:12]} already processed, but registered "
                f"{last_registered[:12]} since then — continuing"
            )
        return True, f"eval revision {eval_rev[:12]} already processed"

    return False, ""


def mark_pipeline_success(
    state: dict[str, Any],
    *,
    uid: int,
    eval_revision: str,
    registered_revision: str,
    block: int | None = None,
) -> None:
    state[f"last_processed_eval_revision:uid{uid}"] = eval_revision.lower()
    state[f"last_registered_revision:uid{uid}"] = registered_revision.lower()
    state[f"last_registered_at:uid{uid}"] = datetime.now(timezone.utc).isoformat()
    if block is not None:
        state[f"last_registered_block:uid{uid}"] = int(block)
