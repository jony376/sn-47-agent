#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from dataclasses import asdict
from typing import Any


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description=(
            "Read validator seeds from chain and derive per-validator challenge "
            "indices for a target miner UID."
        )
    )
    p.add_argument("--uid", type=int, required=True, help="Target miner UID (0-255).")
    p.add_argument(
        "--network",
        type=str,
        default="finney",
        help="Bittensor network (default: finney).",
    )
    p.add_argument("--netuid", type=int, default=47, help="Subnet netuid (default: 47).")
    p.add_argument(
        "--max-epoch-lag",
        type=int,
        default=2,
        help="How many epochs back to read commitments (default: 2).",
    )
    p.add_argument(
        "--track",
        type=str,
        choices=("transformer", "mamba2"),
        default="transformer",
        help="Track used to choose sample count n (default: transformer).",
    )
    p.add_argument(
        "--json",
        action="store_true",
        help="Print full JSON output (machine-readable).",
    )
    return p.parse_args()


def _pick_latest_and_previous(seeds: list[Any]) -> tuple[Any | None, Any | None]:
    if not seeds:
        return None, None
    ordered = sorted(seeds, key=lambda s: s.epoch, reverse=True)
    latest = ordered[0]
    prev = ordered[1] if len(ordered) > 1 else None
    return latest, prev


def main() -> int:
    args = parse_args()

    if not (0 <= args.uid <= 255):
        raise SystemExit("uid must be between 0 and 255")

    import bittensor as bt
    from evolai.validator.config import ACTIVE_DATASETS, EPOCH_BLOCKS, N_EVAL, N_EVAL_TRANSFORMER
    from evolai.validator.challenge_client import get_dataset_size
    from evolai.validator.epoch_manager import (
        EVAL_SALT,
        current_epoch,
        derive_indices,
        read_all_validator_seeds,
    )

    subtensor = bt.Subtensor(network=args.network)
    try:
        metagraph = subtensor.metagraph(netuid=args.netuid)
        block = subtensor.block
        epoch_num = current_epoch(block, EPOCH_BLOCKS)

        n_eval = N_EVAL_TRANSFORMER if args.track == "transformer" else N_EVAL
        ds_sizes = {ds: get_dataset_size(ds) for ds in ACTIVE_DATASETS}

        all_seeds = read_all_validator_seeds(
            subtensor=subtensor,
            netuid=args.netuid,
            metagraph=metagraph,
            current_epoch_num=epoch_num,
            max_epoch_lag=args.max_epoch_lag,
        )

        per_validator: dict[int, list[Any]] = {}
        for s in all_seeds:
            per_validator.setdefault(s.validator_uid, []).append(s)

        rows: list[dict[str, Any]] = []
        for v_uid in sorted(per_validator.keys()):
            latest, prev = _pick_latest_and_previous(per_validator[v_uid])
            if latest is None:
                continue

            datasets_next = {
                ds: derive_indices(
                    seed=latest.seed,
                    uid=args.uid,
                    dataset_name=ds,
                    dataset_size=ds_sizes[ds],
                    n=n_eval,
                    salt=EVAL_SALT,
                )
                for ds in ACTIVE_DATASETS
            }

            datasets_prev = None
            if prev is not None:
                datasets_prev = {
                    ds: derive_indices(
                        seed=prev.seed,
                        uid=args.uid,
                        dataset_name=ds,
                        dataset_size=ds_sizes[ds],
                        n=n_eval,
                        salt=EVAL_SALT,
                    )
                    for ds in ACTIVE_DATASETS
                }

            rows.append(
                {
                    "validator_uid": latest.validator_uid,
                    "validator_hotkey": latest.validator_hotkey,
                    "latest_seed_epoch": latest.epoch,
                    "latest_seed": latest.seed,
                    "previous_seed_epoch": prev.epoch if prev else None,
                    "previous_seed": prev.seed if prev else None,
                    "next_challenge_indices_from_latest_seed": datasets_next,
                    "challenge_indices_from_previous_seed": datasets_prev,
                }
            )

        payload = {
            "network": args.network,
            "netuid": args.netuid,
            "target_uid": args.uid,
            "current_block": block,
            "current_epoch": epoch_num,
            "track": args.track,
            "n_eval": n_eval,
            "active_datasets": ACTIVE_DATASETS,
            "validators": rows,
        }

        if args.json:
            print(json.dumps(payload, indent=2))
            return 0

        print(
            f"network={args.network} netuid={args.netuid} block={block} "
            f"epoch={epoch_num} target_uid={args.uid} track={args.track} n_eval={n_eval}"
        )
        print(f"datasets={', '.join(ACTIVE_DATASETS)}")
        print(f"validators_with_seeds={len(rows)}")
        print()

        for row in rows:
            print(
                f"validator_uid={row['validator_uid']} hotkey={row['validator_hotkey'][:12]}... "
                f"latest(epoch={row['latest_seed_epoch']}, seed={row['latest_seed'][:8]}...) "
                f"previous(epoch={row['previous_seed_epoch']}, "
                f"seed={(row['previous_seed'][:8] + '...') if row['previous_seed'] else None})"
            )
            for ds in ACTIVE_DATASETS:
                nxt = row["next_challenge_indices_from_latest_seed"][ds]
                print(f"  next[{ds}] ({len(nxt)}): {nxt}")
            if row["challenge_indices_from_previous_seed"] is not None:
                for ds in ACTIVE_DATASETS:
                    prv = row["challenge_indices_from_previous_seed"][ds]
                    print(f"  prev[{ds}] ({len(prv)}): {prv}")
            print()
        return 0
    finally:
        try:
            subtensor.close()
        except Exception:
            pass


if __name__ == "__main__":
    raise SystemExit(main())

