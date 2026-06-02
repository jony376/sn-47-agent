#!/usr/bin/env python3
"""Fast validator-matching KL eval with persistent reference model (or vLLM server).

Loads the reference tokenizer/model once per miner cycle; reloads only the candidate
checkpoint for each eval. CLI remains available for one-shot subprocess fallback.
"""
from __future__ import annotations

import argparse
import gc
import json
import os
import sys
import time
from pathlib import Path
from types import TracebackType
from typing import Any

EVOLAI_ROOT = Path(os.environ.get("EVOLAI_ROOT", "/var/www/evolai")).resolve()
if str(EVOLAI_ROOT) not in sys.path:
    sys.path.insert(0, str(EVOLAI_ROOT))

from evolai.validator.config import (  # noqa: E402
    EVAL_FWD_CHUNK_SIZE_TRANSFORMER,
    EVAL_KL_CHUNK_SIZE_TRANSFORMER,
    EVAL_PENALTY_LOSS,
    LOCAL_API_KEY,
    N_EVAL_TRANSFORMER,
)
from evolai.validator.loss_evaluator import evaluate_with_side_quests  # noqa: E402
from validator_kl_eval import (  # noqa: E402
    RefBackend,
    _ensure_local_model_metadata,
    _read_jsonl,
    _resolve_device,
    _resolve_ref_backend,
    _rows_to_samples,
    _validator_uid_from_stem,
)
from validator_kl_scoring import apply_validator_kl_adjustment, estimate_num_params_b, resolve_eval_max_length

FAST_KL_EVAL_SCRIPT = Path(__file__).resolve()


def _log_gpu_memory(label: str) -> None:
    try:
        import torch

        if not torch.cuda.is_available():
            print(f"[GPU_MEMORY] {label} cuda=unavailable", flush=True)
            return
        alloc = torch.cuda.memory_allocated() / (1024**3)
        reserved = torch.cuda.memory_reserved() / (1024**3)
        print(
            f"[GPU_MEMORY] {label} allocated={alloc:.2f}GiB reserved={reserved:.2f}GiB",
            flush=True,
        )
    except Exception as exc:
        print(f"[GPU_MEMORY] {label} error={exc}", flush=True)


def _unload_candidate(model: Any, device: str) -> None:
    del model
    gc.collect()
    if device.startswith("cuda"):
        import torch

        torch.cuda.empty_cache()


def _list_validator_files(
    prep_dir: Path,
    suffix: str,
    validator_uids: str,
) -> tuple[str, list[Path]]:
    if not suffix.startswith("_"):
        suffix = f"_{suffix}"
    pattern = f"validator_*{suffix}.jsonl"
    files = sorted(prep_dir.glob(pattern))
    if not files and suffix == "_current":
        alt = "_next"
        alt_files = sorted(prep_dir.glob(f"validator_*{alt}.jsonl"))
        if alt_files:
            print(
                f"[FAST_EVAL] no {pattern}; fallback validator_*{alt}.jsonl",
                flush=True,
            )
            suffix = alt
            files = alt_files
    if not files:
        raise FileNotFoundError(f"No {pattern} files found in {prep_dir}")

    uid_filter_raw = (validator_uids or "").strip()
    if uid_filter_raw:
        uid_filter = {
            int(part.strip())
            for part in uid_filter_raw.split(",")
            if part.strip()
        }
        files = [f for f in files if _validator_uid_from_stem(f.stem, suffix) in uid_filter]
        if not files:
            raise FileNotFoundError(
                f"No validator files matched --validator-uids={uid_filter_raw!r} "
                f"under {prep_dir}"
            )
    return suffix, files


class PersistentFastKLEvaluator:
    """Reuse ref tokenizer + ref backend (HF weights or vLLM) across checkpoint evals."""

    def __init__(
        self,
        *,
        ref_model: str,
        ref_tokenizer: str,
        ref_mode: str = "inprocess",
        device: str = "auto",
        max_length: int = 8192,
        kl_max_new_tokens: int = 512,
        vllm_ref_url: str = "",
        start_vllm_ref: bool = False,
        allow_inprocess_fallback: bool = True,
        block_hash: str = "local_gate_check",
        keep_vllm_on_close: bool = True,
    ) -> None:
        from transformers import AutoModelForCausalLM, AutoTokenizer

        self.ref_model_name = ref_model
        self.ref_tokenizer_name = ref_tokenizer
        self.ref_mode_requested = ref_mode
        self.device = _resolve_device(device)
        self.max_length = max_length
        self.kl_max_new_tokens = kl_max_new_tokens
        self.block_hash = block_hash
        self._keep_vllm_on_close = keep_vllm_on_close

        import torch

        self.dtype = torch.bfloat16 if self.device.startswith("cuda") else torch.float32

        print(f"[FAST_EVAL_START] persistent evaluator init ref_mode={ref_mode}", flush=True)
        _log_gpu_memory("before_ref_load")

        print(
            f"[REF_MODEL_LOAD_ONCE] loading ref tokenizer {ref_tokenizer}",
            flush=True,
        )
        self.ref_tokenizer = AutoTokenizer.from_pretrained(
            ref_tokenizer, trust_remote_code=False
        )

        self._backend_cm = _resolve_ref_backend(
            ref_model=ref_model,
            ref_mode=ref_mode,
            vllm_ref_url=vllm_ref_url,
            start_vllm=start_vllm_ref,
            allow_inprocess_fallback=allow_inprocess_fallback,
        )
        self.backend: RefBackend = self._backend_cm.__enter__()
        self.use_vllm = self.backend.mode == "vllm_mc"
        self.vllm_url = self.backend.vllm_url or ""

        self.ref_model_obj = None
        if self.use_vllm:
            print(
                f"[REF_MODEL_LOAD_ONCE] vLLM MC ref at {self.vllm_url} "
                "(HF ref weights not loaded)",
                flush=True,
            )
        else:
            print(
                f"[REF_MODEL_LOAD_ONCE] loading in-process ref model {ref_model}",
                flush=True,
            )
            self.ref_model_obj = AutoModelForCausalLM.from_pretrained(
                ref_model,
                torch_dtype=self.dtype,
                low_cpu_mem_usage=True,
            )
            self.ref_model_obj = self.ref_model_obj.to(self.device)
            self.ref_model_obj.eval()
            print("[REF_MODEL_LOAD_ONCE] in-process ref model ready", flush=True)

        _log_gpu_memory("after_ref_load")
        self._eval_count = 0

    def close(self) -> None:
        if getattr(self, "ref_model_obj", None) is not None:
            del self.ref_model_obj
            self.ref_model_obj = None
        if getattr(self, "_backend_cm", None) is not None:
            try:
                if self._keep_vllm_on_close and self.use_vllm:
                    os.environ.setdefault("KL_EVAL_KEEP_VLLM_REF", "true")
                    os.environ.setdefault("KL_EVAL_STOP_VLLM_REF", "false")
                self._backend_cm.__exit__(None, None, None)
            except Exception as exc:
                print(f"[FAST_EVAL] warn: backend close: {exc}", flush=True)
            self._backend_cm = None
        gc.collect()
        if self.device.startswith("cuda"):
            import torch

            torch.cuda.empty_cache()

    def __enter__(self) -> PersistentFastKLEvaluator:
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: TracebackType | None,
    ) -> None:
        self.close()

    def fast_eval(
        self,
        *,
        candidate_model_dir: Path,
        prep_out_dir: Path,
        data_suffix: str = "_current",
        limit_per_validator: int = 20,
        validator_uids: str = "",
        progress_every: int = 5,
        out_json: Path | None = None,
        model_repo: str = "",
        model_revision: str = "",
    ) -> dict[str, Any]:
        """Run KL eval for candidate; reuse loaded ref (log [REF_MODEL_REUSED])."""
        from transformers import AutoModelForCausalLM

        self._eval_count += 1
        model_dir = candidate_model_dir.resolve()
        prep_dir = prep_out_dir.resolve()

        if model_repo:
            os.environ.setdefault("MODEL_REPO", model_repo)
        if model_revision:
            os.environ.setdefault("MODEL_REVISION", model_revision)

        print(
            f"[REF_MODEL_REUSED] eval #{self._eval_count} candidate={model_dir}",
            flush=True,
        )
        print(f"[FAST_EVAL_START] candidate={model_dir} suffix={data_suffix}", flush=True)
        _log_gpu_memory("before_candidate_load")

        suffix, files = _list_validator_files(prep_dir, data_suffix, validator_uids)

        eval_meta: dict[str, Any] = {
            "evaluator": "fast_kl_eval.PersistentFastKLEvaluator",
            "skip_ce": True,
            "skip_sq": True,
            "ref_tokenizer": self.ref_tokenizer_name,
            "ref_model": self.ref_model_name,
            "ref_mode_requested": self.ref_mode_requested,
            "ref_mode_used": self.backend.mode,
            "vllm_ref_url": self.vllm_url,
            "fallback_reason": self.backend.fallback_reason,
            "backend_notes": self.backend.notes,
            "persistent": True,
            "persistent_eval_count": self._eval_count,
            "kl_max_new_tokens": self.kl_max_new_tokens,
            "max_length": self.max_length,
            "data_suffix": suffix,
            "device": self.device,
        }

        print(f"[CANDIDATE_MODEL_LOAD] {model_dir}", flush=True)
        _ensure_local_model_metadata(model_dir)
        num_params_b = estimate_num_params_b(model_dir)
        resolved_max_length = resolve_eval_max_length(num_params_b, env_max=self.max_length)
        if resolved_max_length != self.max_length:
            print(
                f"[FAST_EVAL] max_length={resolved_max_length} "
                f"(model {num_params_b:.2f}B)",
                flush=True,
            )
            self.max_length = resolved_max_length
        eval_meta["max_length_used"] = self.max_length

        model = AutoModelForCausalLM.from_pretrained(
            str(model_dir),
            torch_dtype=self.dtype,
            low_cpu_mem_usage=True,
            local_files_only=True,
        )
        model = model.to(self.device)
        model.eval()
        loaded_params_b = sum(p.numel() for p in model.parameters()) / 1e9
        if loaded_params_b > 0:
            num_params_b = loaded_params_b
        size_adj = apply_validator_kl_adjustment(1.0, num_params_b)["size_adj"]
        eval_meta["num_params_b"] = num_params_b
        eval_meta["size_adj"] = size_adj
        print(
            f"[CANDIDATE_MODEL_LOAD] params={num_params_b:.2f}B size_adj={size_adj:.4f}",
            flush=True,
        )
        _log_gpu_memory("after_candidate_load")

        rows_out: list[dict[str, Any]] = []
        total_validators = len(files)
        for v_idx, f in enumerate(files, start=1):
            vid = _validator_uid_from_stem(f.stem, suffix)
            data = _read_jsonl(f)
            samples = _rows_to_samples(data, limit_per_validator)
            if not samples:
                print(f"[FAST_EVAL] uid={vid}: no samples, skipping", flush=True)
                continue

            print(
                f"[FAST_EVAL] validator {v_idx}/{total_validators} uid={vid} "
                f"samples={len(samples)}",
                flush=True,
            )
            v_started = time.time()
            progress_state = {"last": 0}

            def _progress(done: int, total: int, _vid: int = vid) -> None:
                if done == total or (
                    progress_every > 0
                    and (done == 1 or done % progress_every == 0)
                    and done != progress_state["last"]
                ):
                    progress_state["last"] = done
                    elapsed = time.time() - v_started
                    msg = (
                        f"[FAST_EVAL] uid={_vid} progress {done}/{total} "
                        f"elapsed={elapsed:.1f}s"
                    )
                    if done > 0:
                        eta = (elapsed / done) * (total - done)
                        msg += f" eta={eta:.1f}s"
                    print(msg, flush=True)

            ref_supplier = None
            if self.use_vllm:
                from evolai.validator.loss_evaluator import (
                    build_kl_prompts_for_samples,
                    pregenerate_kl_via_vllm,
                )

                kl_prompts = build_kl_prompts_for_samples(samples, self.ref_tokenizer)

                def _ref_supplier(
                    _prompts: list[str] = kl_prompts,
                    _url: str = self.vllm_url,
                ) -> list:
                    return pregenerate_kl_via_vllm(
                        kl_prompts=_prompts,
                        vllm_base_url=_url,
                        ref_model_name=self.ref_model_name,
                        api_key=LOCAL_API_KEY,
                        kl_max_new_tokens=self.kl_max_new_tokens,
                        ref_tokenizer=self.ref_tokenizer,
                        device=self.device,
                        timeout_s=float(os.getenv("VLLM_REF_GENERATE_TIMEOUT_S", "600")),
                    )

                ref_supplier = _ref_supplier
            elif self.ref_model_obj is not None:
                from evolai.validator.loss_evaluator import (
                    build_kl_prompts_for_samples,
                    pregenerate_kl_sequences,
                )

                kl_prompts = build_kl_prompts_for_samples(samples, self.ref_tokenizer)
                ref_supplier = lambda _p=kl_prompts, _rm=self.ref_model_obj: pregenerate_kl_sequences(
                    kl_prompts=_p,
                    ref_model=_rm,
                    ref_tokenizer=self.ref_tokenizer,
                    kl_max_new_tokens=self.kl_max_new_tokens,
                    max_length=self.max_length,
                    device=self.device,
                )

            _think_ce, _base_ce, _sq_acc, kl_loss = evaluate_with_side_quests(
                model,
                self.ref_tokenizer,
                samples,
                block_hash=self.block_hash,
                kl_max_new_tokens=self.kl_max_new_tokens,
                max_length=self.max_length,
                device=self.device,
                progress_callback=lambda d, t: _progress(d, t),
                penalty_loss=EVAL_PENALTY_LOSS,
                ref_model=self.ref_model_obj,
                fwd_chunk_size=EVAL_FWD_CHUNK_SIZE_TRANSFORMER,
                kl_chunk_size=EVAL_KL_CHUNK_SIZE_TRANSFORMER,
                skip_ce=True,
                skip_sq=True,
                ref_gen_supplier=ref_supplier,
            )

            scored = apply_validator_kl_adjustment(float(kl_loss), num_params_b)
            rows_out.append(
                {
                    "validator_uid": vid,
                    "samples": len(samples),
                    "file": str(f),
                    **scored,
                }
            )
            v_elapsed = time.time() - v_started
            print(
                f"[FAST_EVAL] validator={vid} done "
                f"kl_raw={scored['kl_raw']:.6f} kl_adj={scored['kl_adjusted']:.6f} "
                f"elapsed={v_elapsed:.1f}s mode={eval_meta['ref_mode_used']}",
                flush=True,
            )

        print(f"[CANDIDATE_MODEL_UNLOAD] {model_dir}", flush=True)
        _unload_candidate(model, self.device)
        _log_gpu_memory("after_candidate_unload")

        payload = {
            "model_dir": str(model_dir),
            "ref_model": self.ref_model_name,
            "ref_tokenizer": self.ref_tokenizer_name,
            "max_length": self.max_length,
            "kl_max_new_tokens": self.kl_max_new_tokens,
            "eval_meta": eval_meta,
            "rows": rows_out,
        }
        if out_json is not None:
            out_path = out_json.resolve()
            out_path.parent.mkdir(parents=True, exist_ok=True)
            out_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
            print(f"[FAST_EVAL_DONE] wrote {out_path}", flush=True)
        else:
            print("[FAST_EVAL_DONE]", flush=True)
        return payload


def run_fast_kl_eval_subprocess(
    *,
    python_bin: Path,
    model_dir: Path,
    prep_out_dir: Path,
    out_json: Path,
    ref_model: str,
    ref_tokenizer: str,
    ref_mode: str,
    max_length: int,
    kl_max_new_tokens: int,
    limit_per_validator: int,
    device: str,
    progress_every: int,
    data_suffix: str,
    validator_uids: str = "",
    vllm_ref_url: str = "",
    start_vllm_ref: bool = False,
    allow_inprocess_fallback: bool = True,
    env: dict[str, str] | None = None,
) -> int:
    """One-shot CLI fallback (reloads ref each run)."""
    cmd = [
        str(python_bin),
        str(FAST_KL_EVAL_SCRIPT),
        "--model-dir",
        str(model_dir),
        "--prep-out-dir",
        str(prep_out_dir),
        "--out-json",
        str(out_json),
        "--ref-model",
        ref_model,
        "--ref-tokenizer",
        ref_tokenizer,
        "--ref-mode",
        ref_mode,
        "--max-length",
        str(max_length),
        "--kl-max-new-tokens",
        str(kl_max_new_tokens),
        "--limit-per-validator",
        str(limit_per_validator),
        "--device",
        device,
        "--progress-every",
        str(progress_every),
        "--data-suffix",
        data_suffix,
    ]
    if validator_uids.strip():
        cmd.extend(["--validator-uids", validator_uids.strip()])
    if vllm_ref_url:
        cmd.extend(["--vllm-ref-url", vllm_ref_url])
    if start_vllm_ref:
        cmd.append("--start-vllm-ref")
    if not allow_inprocess_fallback:
        cmd.append("--no-inprocess-fallback")

    import subprocess

    proc = subprocess.run(
        cmd,
        cwd=str(FAST_KL_EVAL_SCRIPT.parent),
        env=env,
        text=True,
    )
    return int(proc.returncode)


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="One-shot fast KL eval (CLI / fallback).")
    p.add_argument("--model-dir", required=True)
    p.add_argument("--prep-out-dir", required=True)
    p.add_argument("--out-json", required=True)
    p.add_argument("--data-suffix", default="_current")
    p.add_argument("--ref-model", default=os.getenv("KL_EVAL_REF_MODEL", "Qwen/Qwen3.5-9B"))
    p.add_argument(
        "--ref-tokenizer",
        default=os.getenv("KL_EVAL_REF_TOKENIZER", "Qwen/Qwen3.5-9B"),
    )
    p.add_argument("--ref-mode", default=os.getenv("KL_EVAL_REF_MODE", "inprocess"))
    p.add_argument("--max-length", type=int, default=int(os.getenv("KL_EVAL_MAX_LENGTH", "8192")))
    p.add_argument(
        "--kl-max-new-tokens",
        type=int,
        default=int(os.getenv("KL_EVAL_KL_MAX_NEW_TOKENS", "512")),
    )
    p.add_argument(
        "--limit-per-validator",
        type=int,
        default=int(os.getenv("KL_EVAL_LIMIT_PER_VALIDATOR", str(N_EVAL_TRANSFORMER))),
    )
    p.add_argument("--validator-uids", default=os.getenv("KL_EVAL_VALIDATOR_UIDS", ""))
    p.add_argument("--progress-every", type=int, default=5)
    p.add_argument("--device", default=os.getenv("KL_EVAL_DEVICE", "auto"))
    p.add_argument("--vllm-ref-url", default=os.getenv("VLLM_REF_URL", ""))
    p.add_argument(
        "--start-vllm-ref",
        action="store_true",
        default=os.getenv("KL_EVAL_START_VLLM_REF", "").strip().lower()
        in {"1", "true", "yes", "on"},
    )
    p.add_argument("--no-inprocess-fallback", action="store_true")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    allow_fallback = not args.no_inprocess_fallback
    with PersistentFastKLEvaluator(
        ref_model=args.ref_model,
        ref_tokenizer=args.ref_tokenizer,
        ref_mode=args.ref_mode,
        device=args.device,
        max_length=args.max_length,
        kl_max_new_tokens=args.kl_max_new_tokens,
        vllm_ref_url=args.vllm_ref_url,
        start_vllm_ref=args.start_vllm_ref,
        allow_inprocess_fallback=allow_fallback,
        keep_vllm_on_close=False,
    ) as evaluator:
        evaluator.fast_eval(
            candidate_model_dir=Path(args.model_dir),
            prep_out_dir=Path(args.prep_out_dir),
            data_suffix=args.data_suffix,
            limit_per_validator=args.limit_per_validator,
            validator_uids=args.validator_uids,
            progress_every=args.progress_every,
            out_json=Path(args.out_json),
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
