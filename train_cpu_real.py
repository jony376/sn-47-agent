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
from torch.optim import AdamW
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


def _build_text_and_labels(
    tokenizer,
    instruction: str,
    response: str,
    max_seq_len: int,
) -> tuple[torch.Tensor, torch.Tensor]:
    prompt = f"### Human: {instruction}\n\n### Assistant:"
    if response:
        full = f"{prompt} {response}"
        p = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=max_seq_len)
        f = tokenizer(full, return_tensors="pt", truncation=True, max_length=max_seq_len)
        input_ids = f["input_ids"][0]
        labels = input_ids.clone()
        prompt_len = min(p["input_ids"].shape[1], input_ids.shape[0])
        labels[:prompt_len] = -100
    else:
        f = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=max_seq_len)
        input_ids = f["input_ids"][0]
        labels = input_ids.clone()
    return input_ids, labels


def _avg_ce(
    model,
    tokenizer,
    rows: list[dict[str, Any]],
    max_seq_len: int,
    device: torch.device,
    limit: int = 64,
) -> float:
    if not rows:
        return float("nan")
    use = rows[: min(limit, len(rows))]
    model.eval()
    losses: list[float] = []
    with torch.inference_mode():
        for r in use:
            ins = (r.get("instruction") or "").strip()
            resp = (r.get("response") or "").strip()
            if not ins:
                continue
            input_ids, labels = _build_text_and_labels(tokenizer, ins, resp, max_seq_len)
            input_ids = input_ids.unsqueeze(0).to(device)
            labels = labels.unsqueeze(0).to(device)
            out = model(input_ids=input_ids, labels=labels, use_cache=False)
            losses.append(float(out.loss.detach().float().item()))
    return float(sum(losses) / max(1, len(losses)))


def _resolve_device(name: str) -> torch.device:
    choice = (name or "auto").strip().lower()
    if choice == "auto":
        return torch.device("cuda" if torch.cuda.is_available() else "cpu")
    if choice == "cuda" and not torch.cuda.is_available():
        raise SystemExit("CUDA requested but torch.cuda.is_available() is False")
    return torch.device(choice)


def _model_dtype(device: torch.device) -> torch.dtype:
    if device.type != "cuda":
        return torch.float32
    if torch.cuda.is_bf16_supported():
        return torch.bfloat16
    return torch.float16


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Fine-tune miner model on challenge data (CPU or GPU).")
    p.add_argument("--uid", required=True)
    p.add_argument("--challenge-json", required=True)
    p.add_argument("--eval-json", required=True)
    p.add_argument("--prep-out-dir", required=True)
    p.add_argument("--model-dir", required=True)
    p.add_argument("--report-json", required=True)
    p.add_argument("--max-steps", type=int, default=30)
    p.add_argument("--lr", type=float, default=5e-5)
    p.add_argument("--max-seq-len", type=int, default=512)
    p.add_argument("--warmup-steps", type=int, default=3)
    p.add_argument(
        "--focus-file",
        default="",
        help="Optional per-validator JSONL file to focus this training round.",
    )
    p.add_argument(
        "--train-mode",
        choices=("lm_head", "super_light"),
        default="super_light",
        help=(
            "lm_head: train full lm_head (heavy on CPU). "
            "super_light: train only bias/LayerNorm/lm_head bias tensors (much lighter)."
        ),
    )
    p.add_argument(
        "--device",
        default="auto",
        choices=("auto", "cpu", "cuda"),
        help="Training device. auto prefers CUDA when available.",
    )
    return p.parse_args()


def _ensure_local_model_metadata(model_dir: Path) -> None:
    """
    Ensure local model directory has minimum metadata files needed by
    AutoTokenizer/AutoModel. If missing, fetch small files from HF repo defined
    in env MODEL_REPO (+ optional MODEL_REVISION).
    """
    needed = [
        # core files required to actually load and train
        "model.safetensors",
        "tokenizer.json",
        # lightweight metadata
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
        f"[TRAIN] local model missing metadata: {missing} | fetching from {repo_id}@{revision}",
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
            print(f"[TRAIN] warn: could not fetch {fn} from {repo_id}: {exc}", flush=True)

    # Fallback for repos that store torch weights instead of safetensors.
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
            print("[TRAIN] fetched fallback weight file: pytorch_model.bin", flush=True)
        except Exception:
            pass
    print(f"[TRAIN] fetched {fetched}/{len(missing)} missing metadata files", flush=True)

    if not (model_dir / "model.safetensors").exists() and not (model_dir / "pytorch_model.bin").exists():
        raise SystemExit(
            "No local model weights found after repair. "
            "Expected model.safetensors or pytorch_model.bin."
        )
    if not (model_dir / "tokenizer.json").exists():
        raise SystemExit("No local tokenizer.json found after repair.")


def main() -> int:
    args = parse_args()
    prep_dir = Path(args.prep_out_dir).resolve()
    model_dir = Path(args.model_dir).resolve()
    report_path = Path(args.report_json).resolve()
    report_path.parent.mkdir(parents=True, exist_ok=True)

    union_path = prep_dir / "union_next.jsonl"
    if not union_path.exists():
        raise SystemExit(f"Missing union dataset: {union_path}")

    print(f"[TRAIN] loading union dataset: {union_path}", flush=True)
    union_rows = _read_jsonl(union_path)
    if not union_rows:
        raise SystemExit("Union dataset is empty.")
    print(f"[TRAIN] union samples: {len(union_rows)}", flush=True)

    focus_rows: list[dict[str, Any]] = []
    if args.focus_file:
        fp = Path(args.focus_file).resolve()
        focus_rows = _read_jsonl(fp)
        print(
            f"[TRAIN] focus-file={fp} samples={len(focus_rows)}",
            flush=True,
        )

    per_val_files = sorted(prep_dir.glob("validator_*_next.jsonl"))
    per_val_rows: dict[str, list[dict[str, Any]]] = {
        p.stem.replace("validator_", "").replace("_next", ""): _read_jsonl(p)
        for p in per_val_files
    }

    t0 = time.time()
    device = _resolve_device(args.device)
    dtype = _model_dtype(device)
    print(f"[TRAIN] device={device} dtype={dtype}", flush=True)
    print(f"[TRAIN] loading tokenizer/model from: {model_dir}", flush=True)
    _ensure_local_model_metadata(model_dir)
    tokenizer = AutoTokenizer.from_pretrained(str(model_dir), local_files_only=True)
    if tokenizer.pad_token is None and tokenizer.eos_token is not None:
        tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "right"

    model = AutoModelForCausalLM.from_pretrained(
        str(model_dir),
        torch_dtype=dtype if device.type == "cuda" else torch.float32,
        low_cpu_mem_usage=True,
        local_files_only=True,
    )
    model.to(device)
    model.train()
    print(f"[TRAIN] model loaded in {time.time()-t0:.1f}s", flush=True)

    # CPU-friendly train modes.
    for _, p in model.named_parameters():
        p.requires_grad = False
    trainable = 0
    if args.train_mode == "lm_head":
        if hasattr(model, "lm_head") and model.lm_head is not None:
            for p in model.lm_head.parameters():
                p.requires_grad = True
                trainable += p.numel()
        else:
            for n, p in model.named_parameters():
                if n.endswith("lm_head.weight") or n.endswith("lm_head.bias"):
                    p.requires_grad = True
                    trainable += p.numel()
    else:
        # super_light: only tiny subsets that still produce real updates.
        # This is much faster on CPU and suitable for quick iteration.
        for n, p in model.named_parameters():
            ln_name = n.lower()
            if (
                n.endswith(".bias")
                or "layernorm" in ln_name
                or ".ln_" in ln_name
                or n.endswith("norm.weight")
                or n.endswith("norm.bias")
                or n.endswith("lm_head.bias")
            ):
                p.requires_grad = True
                trainable += p.numel()
    if trainable == 0:
        raise SystemExit(f"No trainable parameters found for train_mode={args.train_mode}.")
    print(f"[TRAIN] train_mode={args.train_mode} trainable_parameters={trainable}", flush=True)

    before_union = _avg_ce(model, tokenizer, union_rows, args.max_seq_len, device)
    before_by_validator = {
        vid: _avg_ce(model, tokenizer, rows, args.max_seq_len, device)
        for vid, rows in per_val_rows.items()
    }

    optim = AdamW([p for p in model.parameters() if p.requires_grad], lr=args.lr)
    base_rows = focus_rows if focus_rows else union_rows
    rows = [r for r in base_rows if (r.get("instruction") or "").strip()]
    if not rows:
        raise SystemExit("No valid instruction rows in union dataset.")

    step = 0
    losses: list[float] = []
    t_train = time.time()
    print(
        f"[TRAIN] start steps={args.max_steps} lr={args.lr} max_seq_len={args.max_seq_len}",
        flush=True,
    )
    while step < args.max_steps:
        r = rows[step % len(rows)]
        ins = (r.get("instruction") or "").strip()
        resp = (r.get("response") or "").strip()
        input_ids, labels = _build_text_and_labels(tokenizer, ins, resp, args.max_seq_len)
        input_ids = input_ids.unsqueeze(0).to(device)
        labels = labels.unsqueeze(0).to(device)

        out = model(input_ids=input_ids, labels=labels, use_cache=False)
        loss = out.loss
        loss.backward()
        if step < args.warmup_steps:
            scale = float(step + 1) / max(1.0, float(args.warmup_steps))
            for g in optim.param_groups:
                g["lr"] = args.lr * scale
        else:
            for g in optim.param_groups:
                g["lr"] = args.lr
        optim.step()
        optim.zero_grad(set_to_none=True)

        step += 1
        losses.append(float(loss.detach().float().item()))
        elapsed = time.time() - t_train
        print(
            f"[TRAIN] step {step}/{args.max_steps} "
            f"loss={losses[-1]:.4f} avg={sum(losses)/len(losses):.4f} "
            f"elapsed={elapsed:.1f}s",
            flush=True,
        )

    print("[TRAIN] saving model/tokenizer...", flush=True)
    model.save_pretrained(str(model_dir), safe_serialization=True)
    tokenizer.save_pretrained(str(model_dir))
    print("[TRAIN] save complete", flush=True)

    after_union = _avg_ce(model, tokenizer, union_rows, args.max_seq_len, device)
    after_by_validator = {
        vid: _avg_ce(model, tokenizer, rows, args.max_seq_len, device)
        for vid, rows in per_val_rows.items()
    }

    report = {
        "uid": int(args.uid),
        "model_dir": str(model_dir),
        "device": str(device),
        "dtype": str(dtype),
        "train_mode": args.train_mode,
        "max_steps": int(args.max_steps),
        "lr": float(args.lr),
        "max_seq_len": int(args.max_seq_len),
        "trainable_params": int(trainable),
        "avg_train_loss": float(sum(losses) / max(1, len(losses))),
        "before_union_ce": before_union,
        "after_union_ce": after_union,
        "before_by_validator_ce": before_by_validator,
        "after_by_validator_ce": after_by_validator,
        "improvement_union_ratio": (
            (before_union - after_union) / before_union
            if before_union and math.isfinite(before_union) and before_union != 0
            else None
        ),
    }
    report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"Wrote train report: {report_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
