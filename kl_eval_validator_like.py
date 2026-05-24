#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
import os
import time
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


def _ensure_local_model_metadata(model_dir: Path) -> None:
    needed = [
        "model.safetensors",
        "tokenizer.json",
        "config.json",
        "tokenizer_config.json",
        "generation_config.json",
        "chat_template.jinja",
    ]
    missing = [f for f in needed if not (model_dir / f).exists()]
    if not missing:
        return

    repo_id = os.getenv("MODEL_REPO", "").strip()
    revision = os.getenv("MODEL_REVISION", "").strip() or "main"
    token = os.getenv("HF_TOKEN", "").strip() or None
    if not repo_id:
        raise SystemExit(
            "Local model metadata missing "
            f"({', '.join(missing)}) and MODEL_REPO is not set."
        )

    print(
        f"[KL] local model missing files: {missing} | fetching from {repo_id}@{revision}",
        flush=True,
    )
    from huggingface_hub import hf_hub_download

    model_dir.mkdir(parents=True, exist_ok=True)
    fetched = 0
    for fn in missing:
        try:
            src = hf_hub_download(
                repo_id=repo_id,
                filename=fn,
                revision=revision,
                token=token,
            )
            dst = model_dir / fn
            Path(dst).write_bytes(Path(src).read_bytes())
            fetched += 1
        except Exception as exc:
            print(f"[KL] warn: could not fetch {fn}: {exc}", flush=True)

    if not (model_dir / "model.safetensors").exists() and not (model_dir / "pytorch_model.bin").exists():
        try:
            src = hf_hub_download(
                repo_id=repo_id,
                filename="pytorch_model.bin",
                revision=revision,
                token=token,
            )
            dst = model_dir / "pytorch_model.bin"
            Path(dst).write_bytes(Path(src).read_bytes())
            fetched += 1
            print("[KL] fetched fallback weight file: pytorch_model.bin", flush=True)
        except Exception:
            pass
    print(f"[KL] fetched {fetched}/{len(missing)} missing files", flush=True)

    if not (model_dir / "model.safetensors").exists() and not (model_dir / "pytorch_model.bin").exists():
        raise SystemExit(
            "No local model weights found after repair. "
            "Expected model.safetensors or pytorch_model.bin."
        )
    if not (model_dir / "tokenizer.json").exists():
        raise SystemExit("No local tokenizer.json found after repair.")


def _avg_kl_on_rows(
    model,
    ref_model,
    tokenizer,
    rows: list[dict[str, Any]],
    max_seq_len: int,
    limit: int,
    device: torch.device,
    progress_label: str = "",
    progress_every: int = 5,
) -> float:
    use = rows[: min(limit, len(rows))]
    if not use:
        return float("nan")
    model.eval()
    ref_model.eval()
    kls: list[float] = []
    started = time.time()
    total = len(use)
    with torch.inference_mode():
        for i, r in enumerate(use, start=1):
            txt = _render_text(r)
            enc = tokenizer(
                txt,
                return_tensors="pt",
                truncation=True,
                max_length=max_seq_len,
            )
            ids = enc["input_ids"].to(device)
            attn = enc["attention_mask"].to(device)
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
            if i == 1 or i == total or (progress_every > 0 and i % progress_every == 0):
                elapsed = time.time() - started
                msg = f"[KL] {progress_label} progress {i}/{total} elapsed={elapsed:.1f}s"
                if i > 0:
                    eta = (elapsed / i) * (total - i)
                    msg += f" eta={eta:.1f}s"
                print(msg, flush=True)
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
    p.add_argument("--progress-every", type=int, default=5)
    p.add_argument(
        "--device",
        default="auto",
        choices=["auto", "cpu", "cuda"],
        help="Device for KL eval. auto uses CUDA when available.",
    )
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

    if args.device == "cuda":
        device = torch.device("cuda")
    elif args.device == "cpu":
        device = torch.device("cpu")
    else:
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    dtype = torch.bfloat16 if device.type == "cuda" else torch.float32
    print(
        f"[KL] start device={device} dtype={str(dtype).replace('torch.', '')} "
        f"cuda_available={torch.cuda.is_available()}",
        flush=True,
    )

    print(f"[KL] loading tokenizer/model from {model_dir}", flush=True)
    _ensure_local_model_metadata(model_dir)
    tokenizer = AutoTokenizer.from_pretrained(str(model_dir), local_files_only=True)
    model = AutoModelForCausalLM.from_pretrained(
        str(model_dir),
        torch_dtype=dtype,
        low_cpu_mem_usage=True,
        local_files_only=True,
    )
    model = model.to(device)
    print("[KL] candidate model loaded", flush=True)
    print(f"[KL] loading reference model {args.ref_model}", flush=True)
    ref_model = AutoModelForCausalLM.from_pretrained(
        args.ref_model,
        torch_dtype=dtype,
        low_cpu_mem_usage=True,
    )
    ref_model = ref_model.to(device)
    print("[KL] reference model loaded", flush=True)
    # Use same tokenizer space as candidate model for comparable logits.
    # (Assumes same tokenizer/vocab family as validator track.)

    rows = []
    total_validators = len(files)
    for v_idx, f in enumerate(files, start=1):
        vid = int(f.stem.replace("validator_", "").replace("_next", ""))
        data = _read_jsonl(f)
        sample_n = min(len(data), args.limit_per_validator)
        print(
            f"[KL] validator {v_idx}/{total_validators} uid={vid} samples={sample_n} start",
            flush=True,
        )
        v_started = time.time()
        kl = _avg_kl_on_rows(
            model=model,
            ref_model=ref_model,
            tokenizer=tokenizer,
            rows=data,
            max_seq_len=args.max_seq_len,
            limit=args.limit_per_validator,
            device=device,
            progress_label=f"uid={vid}",
            progress_every=args.progress_every,
        )
        v_elapsed = time.time() - v_started
        rows.append(
            {
                "validator_uid": vid,
                "samples": sample_n,
                "kl": kl,
                "file": str(f),
            }
        )
        print(
            f"[KL] validator={vid} done kl={kl:.6f} samples={sample_n} elapsed={v_elapsed:.1f}s",
            flush=True,
        )

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
