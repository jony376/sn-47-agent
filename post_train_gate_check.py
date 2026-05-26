#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


def _kl_map(payload: dict) -> dict[int, float]:
    out: dict[int, float] = {}
    for row in payload.get("rows", []):
        out[int(row["validator_uid"])] = float(row["kl"])
    return out


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Post-train per-validator gate check.")
    p.add_argument(
        "--report-json",
        default="",
        help="Train report from train_cpu_real.py (CE fallback when KL JSON not set).",
    )
    p.add_argument(
        "--baseline-kl-json",
        default="",
        help="Baseline validator-matching KL eval JSON (before training).",
    )
    p.add_argument(
        "--current-kl-json",
        default="",
        help="Current validator-matching KL eval JSON (after training).",
    )
    p.add_argument(
        "--required-improvement",
        type=float,
        default=0.0,
        help="Required relative improvement ratio (default 0.0).",
    )
    p.add_argument("--out-json", default="", help="Optional path to write gate summary JSON.")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    req = float(args.required_improvement)
    rows = []
    all_pass = True
    metric = "ce"

    if args.baseline_kl_json and args.current_kl_json:
        metric = "kl"
        before = _kl_map(json.loads(Path(args.baseline_kl_json).read_text(encoding="utf-8")))
        after = _kl_map(json.loads(Path(args.current_kl_json).read_text(encoding="utf-8")))
        if not before or not after:
            raise SystemExit("KL eval JSON missing per-validator rows.")
        print("validator_uid,before_kl,req_kl,after_kl,margin(req-after),pass")
        for vid in sorted(before.keys()):
            b = float(before[vid])
            a = float(after.get(vid, float("nan")))
            req_kl = b * (1.0 - req)
            margin = req_kl - a
            passed = a <= req_kl
            if not passed:
                all_pass = False
            rows.append(
                {
                    "validator_uid": int(vid),
                    "baseline_kl": b,
                    "required_kl": req_kl,
                    "current_kl": a,
                    "margin": margin,
                    "pass": passed,
                }
            )
            print(
                f"{vid},{b:.6f},{req_kl:.6f},{a:.6f},{margin:.6f},{'PASS' if passed else 'FAIL'}"
            )
    elif args.report_json:
        report = json.loads(Path(args.report_json).read_text(encoding="utf-8"))
        before = report.get("before_by_validator_ce", {})
        after = report.get("after_by_validator_ce", {})
        if not before or not after:
            raise SystemExit("Report missing per-validator CE sections.")
        print("validator_uid,before_ce,req_ce,after_ce,margin(req-after),pass")
        for vid in sorted(before.keys(), key=lambda x: int(x)):
            b = float(before[vid])
            a = float(after.get(vid, float("nan")))
            req_ce = b * (1.0 - req)
            margin = req_ce - a
            passed = a <= req_ce
            if not passed:
                all_pass = False
            rows.append(
                {
                    "validator_uid": int(vid),
                    "before_ce": b,
                    "required_ce": req_ce,
                    "after_ce": a,
                    "margin": margin,
                    "pass": passed,
                }
            )
            print(
                f"{vid},{b:.6f},{req_ce:.6f},{a:.6f},{margin:.6f},{'PASS' if passed else 'FAIL'}"
            )
    else:
        raise SystemExit(
            "Provide --baseline-kl-json + --current-kl-json, or --report-json for CE fallback."
        )

    summary = {
        "all_validators_pass": all_pass,
        "required_improvement": req,
        "metric": metric,
        "rows": rows,
    }
    if args.out_json:
        Path(args.out_json).write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print()
    print(f"ALL_VALIDATORS_PASS={all_pass}")
    return 0 if all_pass else 2


if __name__ == "__main__":
    raise SystemExit(main())

