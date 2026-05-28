#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


def _extract_sample_from_row(row: dict[str, Any]) -> dict[str, str] | None:
    instruction_cols = ("instruction", "input", "question", "prompt", "human")
    response_cols = ("response", "output", "answer", "completion", "assistant", "gpt")
    plain_text_cols = ("text", "content")

    instr_col = next(
        (c for c in instruction_cols if c in row and isinstance(row[c], str) and row[c].strip()),
        None,
    )
    resp_col = next(
        (c for c in response_cols if c in row and isinstance(row[c], str) and row[c].strip()),
        None,
    )
    if instr_col and resp_col:
        return {
            "instruction": row[instr_col].strip(),
            "response": row[resp_col].strip(),
        }

    for col in plain_text_cols + instruction_cols:
        val = row.get(col)
        if isinstance(val, str) and val.strip():
            return {"instruction": val.strip(), "response": ""}

    for val in row.values():
        if isinstance(val, str) and val.strip():
            return {"instruction": val.strip(), "response": ""}
    return None


@dataclass
class PreparedExample:
    dataset: str
    index: int
    validator_uid: int
    epoch: int
    instruction: str
    response: str

    def to_json(self) -> dict[str, Any]:
        return {
            "dataset": self.dataset,
            "index": self.index,
            "validator_uid": self.validator_uid,
            "epoch": self.epoch,
            "instruction": self.instruction,
            "response": self.response,
        }


def _write_validator_split(
    *,
    validators: list[dict[str, Any]],
    out_dir: Path,
    ds_cache: dict[str, Any],
    indices_key: str,
    suffix: str,
    union_seen: set[tuple[str, int]] | None = None,
    fallback_indices_key: str | None = None,
) -> tuple[list[PreparedExample], list[str], list[int]]:
    """Build per-validator + union JSONL for one seed slice (_current / _next)."""
    union_examples: list[PreparedExample] = []
    per_validator_paths: list[str] = []
    fallback_validator_uids: list[int] = []
    track_union = union_seen is not None

    for v in validators:
        v_uid = int(v["validator_uid"])
        v_epoch = int(v.get("latest_seed_epoch") or 0)
        indices_map = v.get(indices_key)
        used_key = indices_key
        if not indices_map and fallback_indices_key:
            indices_map = v.get(fallback_indices_key)
            if indices_map:
                used_key = f"{fallback_indices_key} (fallback; {indices_key} missing)"
                fallback_validator_uids.append(v_uid)
        if not indices_map:
            continue

        per_val_examples: list[PreparedExample] = []
        from datasets import load_dataset

        for ds_name, indices in indices_map.items():
            if ds_name not in ds_cache:
                ds_cache[ds_name] = load_dataset(ds_name, split="train")
            ds = ds_cache[ds_name]
            ds_len = len(ds)
            for idx in indices:
                if idx < 0 or idx >= ds_len:
                    continue
                sample = _extract_sample_from_row(ds[int(idx)])
                if sample is None:
                    continue
                ex = PreparedExample(
                    dataset=ds_name,
                    index=int(idx),
                    validator_uid=v_uid,
                    epoch=v_epoch,
                    instruction=sample["instruction"],
                    response=sample["response"],
                )
                per_val_examples.append(ex)
                if track_union:
                    key = (ds_name, int(idx))
                    assert union_seen is not None
                    if key not in union_seen:
                        union_seen.add(key)
                        union_examples.append(ex)

        vf = out_dir / f"validator_{v_uid}{suffix}.jsonl"
        with vf.open("w", encoding="utf-8") as f:
            for ex in per_val_examples:
                f.write(json.dumps(ex.to_json(), ensure_ascii=True) + "\n")
        per_validator_paths.append(str(vf))
        print(f"Wrote {vf.name}: {len(per_val_examples)} samples ({used_key})")

    return union_examples, per_validator_paths, fallback_validator_uids


def cmd_prepare_data(args: argparse.Namespace) -> int:
    from datasets import load_dataset  # noqa: F401 — used by _write_validator_split

    challenge = json.loads(Path(args.challenge_json).read_text())
    validators = challenge.get("validators", [])
    if not validators:
        raise SystemExit("No validators found in challenge JSON.")

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    ds_cache: dict[str, Any] = {}

    # _current: previous_epoch_seed indices (matches validator log line "KL")
    union_current_seen: set[tuple[str, int]] = set()
    union_current, paths_current, current_fallback_uids = _write_validator_split(
        validators=validators,
        out_dir=out_dir,
        ds_cache=ds_cache,
        indices_key="challenge_indices_from_previous_seed",
        suffix="_current",
        union_seen=union_current_seen,
        fallback_indices_key="next_challenge_indices_from_latest_seed",
    )
    if current_fallback_uids:
        print(
            "Note: _current used latest-seed indices for validator UIDs "
            f"{current_fallback_uids} (no previous_seed on chain yet)."
        )
    uf_current = out_dir / "union_current.jsonl"
    with uf_current.open("w", encoding="utf-8") as f:
        for ex in union_current:
            f.write(json.dumps(ex.to_json(), ensure_ascii=True) + "\n")
    print(f"Wrote union dataset: {uf_current} ({len(union_current)} samples)")

    # _next: latest_seed indices (matches validator log line "NextKL")
    union_next_seen: set[tuple[str, int]] = set()
    union_next, paths_next, _ = _write_validator_split(
        validators=validators,
        out_dir=out_dir,
        ds_cache=ds_cache,
        indices_key="next_challenge_indices_from_latest_seed",
        suffix="_next",
        union_seen=union_next_seen,
    )
    uf_next = out_dir / "union_next.jsonl"
    with uf_next.open("w", encoding="utf-8") as f:
        for ex in union_next:
            f.write(json.dumps(ex.to_json(), ensure_ascii=True) + "\n")
    print(f"Wrote union dataset: {uf_next} ({len(union_next)} samples)")

    manifest = {
        "target_uid": challenge.get("target_uid"),
        "track": challenge.get("track"),
        "n_eval": challenge.get("n_eval"),
        "validators": [int(v["validator_uid"]) for v in validators],
        "current": {
            "indices_key": "challenge_indices_from_previous_seed",
            "fallback_indices_key": "next_challenge_indices_from_latest_seed",
            "fallback_validator_uids": current_fallback_uids,
            "union_size": len(union_current),
            "union_file": str(uf_current),
            "per_validator": paths_current,
        },
        "next": {
            "indices_key": "next_challenge_indices_from_latest_seed",
            "union_size": len(union_next),
            "union_file": str(uf_next),
            "per_validator": paths_next,
        },
    }
    (out_dir / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    print(f"Wrote per-validator datasets in: {out_dir}")
    print(
        "Tip: gate on validator_*_current.jsonl (KL); monitor validator_*_next.jsonl (NextKL)."
    )
    return 0


def cmd_gate_check(args: argparse.Namespace) -> int:
    """
    Input schema:
    {
      "validators": [
        {"validator_uid": 4, "prev_kl": 1.93, "cur_kl": 1.88},
        ...
      ]
    }
    """
    data = json.loads(Path(args.metrics_json).read_text())
    rows = data.get("validators", [])
    if not rows:
        raise SystemExit("No validators[] entries in metrics JSON.")

    delta = float(args.required_improvement)
    all_pass = True
    print(
        "validator_uid,prev_kl,req_kl,cur_kl,margin(req-cur),pass"
    )
    for r in rows:
        v_uid = int(r["validator_uid"])
        prev_kl = float(r["prev_kl"])
        cur_kl = float(r["cur_kl"])
        req_kl = prev_kl * (1.0 - delta)
        margin = req_kl - cur_kl
        passed = cur_kl <= req_kl
        if not passed:
            all_pass = False
        print(
            f"{v_uid},{prev_kl:.6f},{req_kl:.6f},{cur_kl:.6f},{margin:.6f},{'PASS' if passed else 'FAIL'}"
        )

    print()
    print(f"ALL_VALIDATORS_PASS={all_pass}")
    return 0 if all_pass else 2


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description=(
            "CPU-friendly pass-all pipeline utilities: "
            "prepare training data from challenge JSON, and gate-check per-validator KL."
        )
    )
    sub = p.add_subparsers(dest="cmd", required=True)

    p_prepare = sub.add_parser(
        "prepare-data",
        help="Build union and per-validator JSONL datasets from challenge JSON.",
    )
    p_prepare.add_argument(
        "--challenge-json",
        required=True,
        help="JSON output from scripts/get_prev_seed_and_next_indices.py --json",
    )
    p_prepare.add_argument(
        "--out-dir",
        default="cpu_pass_all_data",
        help="Output directory for JSONL files.",
    )
    p_prepare.set_defaults(func=cmd_prepare_data)

    p_gate = sub.add_parser(
        "gate-check",
        help="Check if candidate KL passes all validators with required relative improvement.",
    )
    p_gate.add_argument(
        "--metrics-json",
        required=True,
        help="JSON file with validators[] entries: validator_uid, prev_kl, cur_kl.",
    )
    p_gate.add_argument(
        "--required-improvement",
        type=float,
        default=0.02,
        help="Relative KL improvement required (default 0.02 = 2%%).",
    )
    p_gate.set_defaults(func=cmd_gate_check)

    return p


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())

