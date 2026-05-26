#!/usr/bin/env python3
"""Validator-matching KL evaluation for miner gate prediction.

Uses evolai.validator.loss_evaluator.evaluate_with_side_quests with the same
protocol as on-chain validators:
  - Qwen chat template + enable_thinking=True KL prompts
  - MC KL on ref-generated continuation tokens (vLLM path), or exact full-vocab
    KL when an in-process ref model is used
  - skip_ce=True, skip_sq=True (KL only)
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Iterator

EVOLAI_ROOT = Path(os.environ.get("EVOLAI_ROOT", "/root/sn47/evolai")).resolve()
if str(EVOLAI_ROOT) not in sys.path:
    sys.path.insert(0, str(EVOLAI_ROOT))

from evolai.validator.config import (  # noqa: E402
    EVAL_FWD_CHUNK_SIZE_TRANSFORMER,
    EVAL_KL_CHUNK_SIZE_TRANSFORMER,
    EVAL_KL_MAX_NEW_TOKENS_TRANSFORMER,
    EVAL_PENALTY_LOSS,
    EVAL_REFERENCE_TOKENIZER,
    HF_LOSS_MAX_SEQ_LEN,
    LOCAL_API_KEY,
    N_EVAL_TRANSFORMER,
    SIDE_QUEST_MAX_CTX,
    VLLM_REF_GENERATE_TIMEOUT_S,
    VLLM_REF_GPU_INDEX,
    VLLM_REF_GPU_MEMORY_UTILIZATION,
    VLLM_REF_MAX_MODEL_LEN,
    VLLM_REF_PORT,
)
from evolai.validator.loss_evaluator import (  # noqa: E402
    ChatSample,
    evaluate_with_side_quests,
    pregenerate_kl_sequences,
    pregenerate_kl_via_vllm,
)


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


def _rows_to_samples(rows: list[dict[str, Any]], limit: int) -> list[ChatSample]:
    samples: list[ChatSample] = []
    for row in rows[:limit]:
        ins = (row.get("instruction") or "").strip()
        resp = (row.get("response") or "").strip()
        if ins:
            samples.append(ChatSample(instruction=ins, response=resp))
    return samples


@contextmanager
def _maybe_vllm_ref_server(
    ref_model: str,
    ref_mode: str,
    vllm_ref_url: str,
    start_vllm: bool,
) -> Iterator[tuple[str | None, Any]]:
    """Yield (vllm_base_url, vllm_client_or_none). Starts/stops server when requested."""
    client = None
    base_url = vllm_ref_url.strip() or None
    mode = ref_mode.lower()

    if mode == "inprocess":
        yield None, None
        return

    if base_url:
        yield base_url.rstrip("/"), None
        return

    if mode == "vllm" or (mode == "auto" and start_vllm):
        try:
            from evolai.validator.vllm_client import VLLMClient
        except Exception as exc:
            if mode == "vllm":
                raise SystemExit(f"vLLM client unavailable: {exc}") from exc
            print(f"[KL] vLLM unavailable ({exc}); falling back to in-process ref model", flush=True)
            yield None, None
            return

        print(
            f"[KL] starting ref vLLM server model={ref_model} port={VLLM_REF_PORT} "
            f"gpu={VLLM_REF_GPU_INDEX}",
            flush=True,
        )
        client = VLLMClient(
            port=VLLM_REF_PORT,
            max_model_len=VLLM_REF_MAX_MODEL_LEN,
            gpu_memory_utilization=VLLM_REF_GPU_MEMORY_UTILIZATION,
        )
        try:
            client.start_server(ref_model, gpu_index=VLLM_REF_GPU_INDEX)
            url = f"http://127.0.0.1:{VLLM_REF_PORT}/v1"
            print(f"[KL] ref vLLM ready at {url}", flush=True)
            yield url, client
        finally:
            try:
                client.stop_server()
            except Exception as exc:
                print(f"[KL] warn: vLLM stop failed: {exc}", flush=True)
        return

    yield None, None


def _resolve_device(device_arg: str) -> str:
    import torch

    if device_arg == "cuda":
        if not torch.cuda.is_available():
            raise SystemExit("KL_EVAL_DEVICE=cuda but CUDA is not available")
        return "cuda"
    if device_arg == "cpu":
        return "cpu"
    return "cuda" if torch.cuda.is_available() else "cpu"


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Validator-matching KL eval (evaluate_with_side_quests, KL only)."
    )
    p.add_argument("--model-dir", required=True)
    p.add_argument("--prep-out-dir", required=True)
    p.add_argument("--out-json", required=True)
    p.add_argument(
        "--data-suffix",
        default="_next",
        help="Per-validator jsonl suffix, e.g. _next or _current (default: _next).",
    )
    p.add_argument(
        "--ref-model",
        default=os.getenv("KL_EVAL_REF_MODEL", EVAL_REFERENCE_TOKENIZER),
        help="Reference model id (vLLM server model or HF weights).",
    )
    p.add_argument(
        "--ref-tokenizer",
        default=os.getenv("KL_EVAL_REF_TOKENIZER", EVAL_REFERENCE_TOKENIZER),
        help="Reference tokenizer repo (must match validator).",
    )
    p.add_argument(
        "--ref-mode",
        default=os.getenv("KL_EVAL_REF_MODE", "auto"),
        choices=["auto", "vllm", "inprocess"],
        help="Ref generation backend: vLLM MC-KL (validator default), in-process, or auto.",
    )
    p.add_argument(
        "--vllm-ref-url",
        default=os.getenv("VLLM_REF_URL", ""),
        help="Existing ref vLLM base URL (e.g. http://127.0.0.1:8002/v1).",
    )
    p.add_argument(
        "--start-vllm-ref",
        action="store_true",
        default=os.getenv("KL_EVAL_START_VLLM_REF", "").strip().lower()
        in {"1", "true", "yes", "on"},
        help="Start a local ref vLLM server when none is reachable.",
    )
    p.add_argument(
        "--max-length",
        type=int,
        default=int(os.getenv("KL_EVAL_MAX_LENGTH", str(min(HF_LOSS_MAX_SEQ_LEN, SIDE_QUEST_MAX_CTX)))),
        help="Max prompt context (validator uses min(HF_LOSS_MAX_SEQ_LEN, SIDE_QUEST_MAX_CTX)).",
    )
    p.add_argument(
        "--kl-max-new-tokens",
        type=int,
        default=int(
            os.getenv("KL_EVAL_KL_MAX_NEW_TOKENS", str(EVAL_KL_MAX_NEW_TOKENS_TRANSFORMER))
        ),
    )
    p.add_argument(
        "--limit-per-validator",
        type=int,
        default=int(os.getenv("KL_EVAL_LIMIT_PER_VALIDATOR", str(N_EVAL_TRANSFORMER))),
    )
    p.add_argument("--progress-every", type=int, default=5)
    p.add_argument(
        "--device",
        default=os.getenv("KL_EVAL_DEVICE", "auto"),
        choices=["auto", "cpu", "cuda"],
    )
    p.add_argument(
        "--block-hash",
        default=os.getenv("KL_EVAL_BLOCK_HASH", "local_gate_check"),
        help="Block hash passed to evaluate_with_side_quests (side quests skipped).",
    )
    return p.parse_args()


def main() -> int:
    args = parse_args()
    model_dir = Path(args.model_dir).resolve()
    prep_dir = Path(args.prep_out_dir).resolve()
    out_path = Path(args.out_json).resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)

    pattern = f"validator_*{args.data_suffix}.jsonl"
    files = sorted(prep_dir.glob(pattern))
    if not files:
        raise SystemExit(f"No {pattern} files found in {prep_dir}")

    device = _resolve_device(args.device)
    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer

    dtype = torch.bfloat16 if device.startswith("cuda") else torch.float32
    print(
        f"[KL] validator-matching eval device={device} dtype={str(dtype).replace('torch.', '')} "
        f"ref_mode={args.ref_mode} kl_max_new_tokens={args.kl_max_new_tokens} "
        f"max_length={args.max_length}",
        flush=True,
    )

    print(f"[KL] loading ref tokenizer {args.ref_tokenizer}", flush=True)
    ref_tokenizer = AutoTokenizer.from_pretrained(args.ref_tokenizer, trust_remote_code=False)

    print(f"[KL] loading candidate model from {model_dir}", flush=True)
    _ensure_local_model_metadata(model_dir)
    model = AutoModelForCausalLM.from_pretrained(
        str(model_dir),
        torch_dtype=dtype,
        low_cpu_mem_usage=True,
        local_files_only=True,
    )
    model = model.to(device)
    print("[KL] candidate model loaded", flush=True)

    rows_out: list[dict[str, Any]] = []
    ref_model_obj = None
    eval_meta: dict[str, Any] = {
        "evaluator": "evolai.validator.loss_evaluator.evaluate_with_side_quests",
        "skip_ce": True,
        "skip_sq": True,
        "ref_tokenizer": args.ref_tokenizer,
        "ref_model": args.ref_model,
        "ref_mode_requested": args.ref_mode,
        "kl_max_new_tokens": args.kl_max_new_tokens,
        "max_length": args.max_length,
        "data_suffix": args.data_suffix,
        "device": device,
    }

    with _maybe_vllm_ref_server(
        ref_model=args.ref_model,
        ref_mode=args.ref_mode,
        vllm_ref_url=args.vllm_ref_url,
        start_vllm=args.start_vllm_ref,
    ) as (vllm_url, _vllm_client):
        use_vllm = vllm_url is not None
        eval_meta["ref_mode_used"] = "vllm" if use_vllm else "inprocess"
        eval_meta["vllm_ref_url"] = vllm_url or ""

        if not use_vllm:
            print(f"[KL] loading in-process ref model {args.ref_model}", flush=True)
            ref_model_obj = AutoModelForCausalLM.from_pretrained(
                args.ref_model,
                torch_dtype=dtype,
                low_cpu_mem_usage=True,
            )
            ref_model_obj = ref_model_obj.to(device)
            print("[KL] in-process ref model loaded (full-vocab KL path)", flush=True)

        total_validators = len(files)
        for v_idx, f in enumerate(files, start=1):
            stem = f.stem
            vid = int(stem.replace("validator_", "").replace(args.data_suffix, ""))
            data = _read_jsonl(f)
            samples = _rows_to_samples(data, args.limit_per_validator)
            if not samples:
                print(f"[KL] validator uid={vid}: no samples, skipping", flush=True)
                continue

            print(
                f"[KL] validator {v_idx}/{total_validators} uid={vid} "
                f"samples={len(samples)} start",
                flush=True,
            )
            v_started = time.time()
            progress_state = {"last": 0}

            def _progress(done: int, total: int, _vid: int = vid) -> None:
                if done == total or (
                    args.progress_every > 0
                    and (done == 1 or done % args.progress_every == 0)
                    and done != progress_state["last"]
                ):
                    progress_state["last"] = done
                    elapsed = time.time() - v_started
                    msg = f"[KL] uid={_vid} progress {done}/{total} elapsed={elapsed:.1f}s"
                    if done > 0:
                        eta = (elapsed / done) * (total - done)
                        msg += f" eta={eta:.1f}s"
                    print(msg, flush=True)

            ref_supplier = None
            if use_vllm:
                from evolai.validator.loss_evaluator import build_kl_prompts_for_samples

                kl_prompts = build_kl_prompts_for_samples(samples, ref_tokenizer)

                def _ref_supplier(
                    _prompts: list[str] = kl_prompts,
                    _url: str = vllm_url,
                ) -> list:
                    return pregenerate_kl_via_vllm(
                        kl_prompts=_prompts,
                        vllm_base_url=_url,
                        ref_model_name=args.ref_model,
                        api_key=LOCAL_API_KEY,
                        kl_max_new_tokens=args.kl_max_new_tokens,
                        ref_tokenizer=ref_tokenizer,
                        device=device,
                        timeout_s=VLLM_REF_GENERATE_TIMEOUT_S,
                    )

                ref_supplier = _ref_supplier
            elif ref_model_obj is not None:
                from evolai.validator.loss_evaluator import build_kl_prompts_for_samples

                kl_prompts = build_kl_prompts_for_samples(samples, ref_tokenizer)
                ref_supplier = lambda _p=kl_prompts, _rm=ref_model_obj: pregenerate_kl_sequences(
                    kl_prompts=_p,
                    ref_model=_rm,
                    ref_tokenizer=ref_tokenizer,
                    kl_max_new_tokens=args.kl_max_new_tokens,
                    max_length=args.max_length,
                    device=device,
                )

            _think_ce, _base_ce, _sq_acc, kl_loss = evaluate_with_side_quests(
                model,
                ref_tokenizer,
                samples,
                block_hash=args.block_hash,
                kl_max_new_tokens=args.kl_max_new_tokens,
                max_length=args.max_length,
                device=device,
                progress_callback=lambda d, t: _progress(d, t),
                penalty_loss=EVAL_PENALTY_LOSS,
                ref_model=ref_model_obj,
                fwd_chunk_size=EVAL_FWD_CHUNK_SIZE_TRANSFORMER,
                kl_chunk_size=EVAL_KL_CHUNK_SIZE_TRANSFORMER,
                skip_ce=True,
                skip_sq=True,
                ref_gen_supplier=ref_supplier,
            )

            v_elapsed = time.time() - v_started
            rows_out.append(
                {
                    "validator_uid": vid,
                    "samples": len(samples),
                    "kl": float(kl_loss),
                    "file": str(f),
                }
            )
            print(
                f"[KL] validator={vid} done kl={kl_loss:.6f} samples={len(samples)} "
                f"elapsed={v_elapsed:.1f}s mode={eval_meta['ref_mode_used']}",
                flush=True,
            )

    out = {
        "model_dir": str(model_dir),
        "ref_model": args.ref_model,
        "ref_tokenizer": args.ref_tokenizer,
        "max_length": args.max_length,
        "kl_max_new_tokens": args.kl_max_new_tokens,
        "eval_meta": eval_meta,
        "rows": rows_out,
    }
    out_path.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(f"[KL] wrote {out_path}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
