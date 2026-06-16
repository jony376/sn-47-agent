#!/usr/bin/env python3
"""Validator-parity KL scoring helpers (size adjustment, gate rules)."""
from __future__ import annotations

import json
import math
import os
import sys
from pathlib import Path
from typing import Any

from agent_common import resolve_evolai_root

EVOLAI_ROOT = resolve_evolai_root()
if str(EVOLAI_ROOT) not in sys.path:
    sys.path.insert(0, str(EVOLAI_ROOT))

from evolai.validator.config import (  # noqa: E402
    EVAL_SIZE_BONUS_ALPHA,
    EVAL_SIZE_BONUS_REF_B,
    get_eval_config_for_model_size,
)


def estimate_num_params_b(model_dir: Path) -> float:
    """Estimate parameter count in billions (matches on-chain validator counting)."""
    cfg_path = model_dir / "config.json"
    if cfg_path.exists():
        try:
            cfg = json.loads(cfg_path.read_text(encoding="utf-8"))
            for key in ("num_parameters", "total_params", "n_params"):
                raw = cfg.get(key)
                if isinstance(raw, (int, float)) and raw > 0:
                    # Heuristic: large ints are raw counts, small floats are already B.
                    if raw > 1_000_000:
                        return float(raw) / 1e9
                    return float(raw)
        except Exception:
            pass

    weights = model_dir / "model.safetensors"
    if weights.exists():
        try:
            from safetensors import safe_open

            total = 0
            with safe_open(str(weights), framework="pt", device="cpu") as f:
                for key in f.keys():
                    total += f.get_tensor(key).numel()
            if total > 0:
                return total / 1e9
        except Exception:
            pass

    return 0.0


def size_adjustment_factor(num_params_b: float) -> float:
    """Same formula as evolai/cli/commands/validator.py (_size_adj)."""
    if num_params_b <= 0 or not math.isfinite(num_params_b):
        return 1.0
    ref_b = max(1e-9, float(EVAL_SIZE_BONUS_REF_B))
    alpha = float(EVAL_SIZE_BONUS_ALPHA)
    return (num_params_b / ref_b) ** alpha


def apply_validator_kl_adjustment(kl_raw: float, num_params_b: float) -> dict[str, float]:
    adj = size_adjustment_factor(num_params_b)
    kl_adj = float(kl_raw) * adj
    return {
        "kl_raw": float(kl_raw),
        "kl_adjusted": kl_adj,
        "kl": kl_adj,
        "size_adj": adj,
        "num_params_b": float(num_params_b),
    }


def resolve_eval_max_length(num_params_b: float, env_max: int = 0) -> int:
    """Match validator: min(model_table_seq, SIDE_QUEST_MAX_CTX, optional env cap)."""
    from evolai.validator.config import HF_LOSS_MAX_SEQ_LEN, SIDE_QUEST_MAX_CTX

    params_b = max(float(num_params_b), 0.01)
    _batch, seq_len = get_eval_config_for_model_size(params_b)
    cap = min(int(seq_len), int(SIDE_QUEST_MAX_CTX), int(HF_LOSS_MAX_SEQ_LEN))
    if env_max > 0:
        return min(int(env_max), cap)
    return cap


def kl_rows_from_payload(payload: dict[str, Any], *, use_adjusted: bool = True) -> dict[int, float]:
    out: dict[int, float] = {}
    for row in payload.get("rows", []):
        vid = int(row["validator_uid"])
        if use_adjusted:
            out[vid] = float(row.get("kl_adjusted", row.get("kl", 0.0)))
        else:
            out[vid] = float(row.get("kl_raw", row.get("kl", 0.0)))
    return out


def kl_gate_improvement_vs_baseline(
    baseline_kl: dict[int, float],
    current_kl: dict[int, float],
    required_improvement: float,
    *,
    target_validator_uids: list[int] | None = None,
) -> dict[str, Any]:
    """Relative improvement vs local baseline (train loop).

    Pass when current_kl <= baseline_kl * (1 - required_improvement) per validator.
    """
    vids = sorted(baseline_kl.keys())
    if target_validator_uids:
        vids = [v for v in vids if v in target_validator_uids]
    if not vids:
        return {
            "gate_mode": "baseline_improvement",
            "all_pass": False,
            "required_improvement": required_improvement,
            "rows": [],
            "worst_validator_uid": None,
            "worst_margin": None,
            "error": "no_baseline_kl",
        }

    rows = []
    all_pass = True
    worst_uid = None
    worst_margin = None
    for vid in vids:
        prev = float(baseline_kl[vid])
        cur = float(current_kl.get(vid, float("nan")))
        req = prev * (1.0 - required_improvement)
        margin = req - cur if math.isfinite(cur) else float("nan")
        passed = math.isfinite(cur) and cur <= req
        if not passed:
            all_pass = False
        rows.append(
            {
                "validator_uid": vid,
                "prev_kl": prev,
                "required_kl": req,
                "current_kl": cur,
                "margin": margin,
                "pass": passed,
            }
        )
        if worst_margin is None or (math.isfinite(margin) and margin < worst_margin):
            worst_margin = margin
            worst_uid = vid
    return {
        "gate_mode": "baseline_improvement",
        "all_pass": all_pass,
        "required_improvement": required_improvement,
        "rows": rows,
        "worst_validator_uid": worst_uid,
        "worst_margin": worst_margin,
    }


def kl_gate_combined(
    eval_rec: dict[str, Any],
    baseline_kl: dict[int, float],
    current_kl: dict[int, float],
    required_improvement: float,
    *,
    target_validator_uids: list[int] | None = None,
) -> dict[str, Any]:
    """Require both local baseline improvement and W&B validator-improve ceiling."""
    baseline_gate = kl_gate_improvement_vs_baseline(
        baseline_kl,
        current_kl,
        required_improvement,
        target_validator_uids=target_validator_uids,
    )
    validator_gate = kl_gate_validator_improve(
        eval_rec,
        current_kl,
        required_improvement=required_improvement,
        target_validator_uids=target_validator_uids,
    )
    all_pass = bool(baseline_gate["all_pass"] and validator_gate["all_pass"])
    worst_uid = None
    worst_margin = None
    for gate in (baseline_gate, validator_gate):
        m = gate.get("worst_margin")
        u = gate.get("worst_validator_uid")
        if m is not None and math.isfinite(float(m)):
            if worst_margin is None or float(m) < worst_margin:
                worst_margin = float(m)
                worst_uid = u
    return {
        "gate_mode": "both",
        "all_pass": all_pass,
        "required_improvement": required_improvement,
        "baseline_gate": baseline_gate,
        "validator_gate": validator_gate,
        "rows": baseline_gate.get("rows", []),
        "worst_validator_uid": worst_uid,
        "worst_margin": worst_margin,
    }


def kl_gate_validator_improve(
    eval_rec: dict[str, Any],
    current_kl_by_validator: dict[int, float],
    *,
    required_improvement: float,
    target_validator_uids: list[int] | None = None,
) -> dict[str, Any]:
    """Match on-chain Improve gate: cur_kl <= prev_next_kl * (1 - delta).

    Uses prev_kl/req_kl parsed from W&B when available (already size-adjusted).
    """
    prev_kl_global = float(eval_rec.get("prev_kl") or 0.0)
    req_kl_global = float(eval_rec.get("req_kl") or 0.0)
    if req_kl_global <= 0 and prev_kl_global > 0:
        req_kl_global = prev_kl_global * (1.0 - required_improvement)

    vids = sorted(current_kl_by_validator.keys())
    if target_validator_uids:
        vids = [v for v in vids if v in target_validator_uids]

    rows = []
    all_pass = True
    worst_uid = None
    worst_margin = None
    for vid in vids:
        cur = float(current_kl_by_validator.get(vid, float("nan")))
        req = req_kl_global if req_kl_global > 0 else float("nan")
        prev = prev_kl_global if prev_kl_global > 0 else float("nan")
        if req_kl_global <= 0 and prev_kl_global > 0:
            req = prev_kl_global * (1.0 - required_improvement)
        margin = req - cur if math.isfinite(req) and math.isfinite(cur) else float("nan")
        passed = math.isfinite(req) and math.isfinite(cur) and cur <= req
        if not passed:
            all_pass = False
        rows.append(
            {
                "validator_uid": vid,
                "prev_kl": prev,
                "required_kl": req,
                "current_kl": cur,
                "margin": margin,
                "pass": passed,
            }
        )
        if worst_margin is None or (math.isfinite(margin) and margin < worst_margin):
            worst_margin = margin
            worst_uid = vid

    return {
        "gate_mode": "validator_improve",
        "all_pass": all_pass,
        "required_improvement": required_improvement,
        "eval_rec_prev_kl": prev_kl_global,
        "eval_rec_req_kl": req_kl_global,
        "rows": rows,
        "worst_validator_uid": worst_uid,
        "worst_margin": worst_margin,
    }
