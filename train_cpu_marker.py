#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


def main() -> int:
    p = argparse.ArgumentParser(
        description=(
            "CPU-safe default train step: records challenge/eval metadata and "
            "writes a changing marker file into model dir so upload produces a new commit."
        )
    )
    p.add_argument("--uid", required=True)
    p.add_argument("--challenge-json", required=True)
    p.add_argument("--eval-json", required=True)
    p.add_argument("--prep-out-dir", required=True)
    p.add_argument("--model-dir", required=True)
    args = p.parse_args()

    challenge = json.loads(Path(args.challenge_json).read_text(encoding="utf-8"))
    eval_rec = json.loads(Path(args.eval_json).read_text(encoding="utf-8"))
    prep_dir = Path(args.prep_out_dir)
    model_dir = Path(args.model_dir)
    model_dir.mkdir(parents=True, exist_ok=True)

    manifest_path = prep_dir / "manifest.json"
    manifest = {}
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

    report = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "uid": int(args.uid),
        "challenge_epoch": challenge.get("current_epoch"),
        "challenge_block": challenge.get("current_block"),
        "validators": len(challenge.get("validators", [])),
        "union_samples": manifest.get("union_size"),
        "latest_eval": {
            "timestamp": eval_rec.get("timestamp"),
            "model_repo": eval_rec.get("model_repo"),
            "model_revision": eval_rec.get("model_revision"),
            "gate": eval_rec.get("gate"),
            "cur_kl": eval_rec.get("cur_kl"),
            "req_kl": eval_rec.get("req_kl"),
            "prev_kl": eval_rec.get("prev_kl"),
        },
        "note": "Default CPU marker training step (no weight optimization).",
    }

    # Marker file updated every run; ensures non-empty HF commit.
    marker = model_dir / "AUTO_TRAIN_MARKER.json"
    marker.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"Wrote marker: {marker}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

