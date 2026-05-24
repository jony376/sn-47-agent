#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any

import torch
import torch.nn.functional as F
from transformers import AutoModelForCausalLM, AutoTokenizer


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    if not path.exists():
        return out
    for ln in path.read_text(encoding="utf-8").splitlines():
        ln = ln.strip()
        if not ln:
            continue
        out.append(json.loads(ln))
    return out


def _render_text(r: dict[str, Any]) -> str:
    ins = (r.get("instruction") or "").strip()
    resp = (r.get("response") or "").strip()
    if resp:
        return f"### Human: {ins}\n\n### Assistant: {resp}"
    return f"### Human: {ins}\n\n### Assistant:"


def _avg_kl_on_rows(
    model,
    ref_model,
    tokenizer,
    rows: list[dict[str, Any]],
    max_seq_len: int,
    limit: int,
) -> float:
    use = rows[: min(limit, len(rows))]
    if not use:
        return float("nan")
    model.eval()
    ref_model.eval()
    kls: list[float] = []
    with torch.inference_mode():
        for r in use:
            txt = _render_text(r)
            enc = tokenizer(
                txt,
                return_tensors="pt",
                truncation=True,
                max_length=max_seq_len,
            )
            ids = enc["input_ids"]
            attn = enc["attention_mask"]
            if ids.shape[1] < 2:
                continue
            out_m = model(input_ids=ids, attention_mask=attn, use_cache=False)
            out_r = ref_model(input_ids=ids, attention_mask=attn, use_cache=False)
            lm = out_m.logits[:, :-1, :]
            lr = out_r.logits[:, :-1, :]
            if lm.shape[-1] != lr.shape[-1]:
                raise RuntimeError(
                    f"Vocab mismatch: model={lm.shape[-1]} ref={lr.shape[-1]}"
                )
            p_ref = F.softmax(lr, dim=-1)
            log_p_ref = F.log_softmax(lr, dim=-1)
            log_p_m = F.log_softmax(lm, dim=-1)
            kl = (p_ref * (log_p_ref - log_p_m)).sum(dim=-1).mean()
            kls.append(float(kl.detach().cpu().item()))
    return float(sum(kls) / max(1, len(kls)))


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Validator-like KL eval on per-validator slices.")
    p.add_argument("--model-dir", required=True)
    p.add_argument("--prep-out-dir", required=True)
    p.add_argument("--out-json", required=True)
    p.add_argument(
        "--ref-model",
        default="Qwen/Qwen3.5-9B",
        help="Reference model id used for KL.",
    )
    p.add_argument("--max-seq-len", type=int, default=512)
    p.add_argument("--limit-per-validator", type=int, default=40)
    return p.parse_args()


def main() -> int:
    args = parse_args()
    model_dir = Path(args.model_dir).resolve()
    prep_dir = Path(args.prep_out_dir).resolve()
    out_path = Path(args.out_json).resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)

    files = sorted(prep_dir.glob("validator_*_next.jsonl"))
    if not files:
        raise SystemExit(f"No validator_*_next.jsonl files found in {prep_dir}")

    print(f"[KL] loading tokenizer/model from {model_dir}", flush=True)
    tokenizer = AutoTokenizer.from_pretrained(str(model_dir), local_files_only=True)
    model = AutoModelForCausalLM.from_pretrained(
        str(model_dir),
        torch_dtype=torch.float32,
        low_cpu_mem_usage=True,
        local_files_only=True,
    )
    print(f"[KL] loading reference model {args.ref_model}", flush=True)
    ref_model = AutoModelForCausalLM.from_pretrained(
        args.ref_model,
        torch_dtype=torch.float32,
        low_cpu_mem_usage=True,
    )
    # Use same tokenizer space as candidate model for comparable logits.
    # (Assumes same tokenizer/vocab family as validator track.)

    rows = []
    for f in files:
        vid = int(f.stem.replace("validator_", "").replace("_next", ""))
        data = _read_jsonl(f)
        kl = _avg_kl_on_rows(
            model=model,
            ref_model=ref_model,
            tokenizer=tokenizer,
            rows=data,
            max_seq_len=args.max_seq_len,
            limit=args.limit_per_validator,
        )
        rows.append(
            {
                "validator_uid": vid,
                "samples": min(len(data), args.limit_per_validator),
                "kl": kl,
                "file": str(f),
            }
        )
        print(f"[KL] validator={vid} kl={kl:.6f} samples={min(len(data), args.limit_per_validator)}", flush=True)

    out = {
        "model_dir": str(model_dir),
        "ref_model": args.ref_model,
        "max_seq_len": args.max_seq_len,
        "rows": rows,
    }
    out_path.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(f"[KL] wrote {out_path}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

