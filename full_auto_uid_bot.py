#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import re
import shlex
import subprocess
import sys
import time
import traceback
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Optional
from urllib import parse, request

from eval_log_parser import parse_latest_eval_for_uid as parse_eval_from_lines
from wandb_log_watcher import WandbLogTailer
from huggingface_hub import HfApi

from agent_common import (
    assess_lock_risk,
    effective_lock_age_seconds,
    eval_age_seconds,
    eval_is_complete,
    get_subnet_timing,
    is_valid_sha,
    load_state,
    lock_budget_seconds,
    lock_risk_requires_fast_train,
    lock_risk_should_abort,
    mark_pipeline_success,
    resolve_register_revision,
    save_state,
    should_skip_duplicate_eval,
    verify_hf_revision,
    watch_eval_trigger_key,
)
from validator_log_timing import (
    build_timing_model,
    enrich_eval_record,
    estimate_lock_window,
    load_timing_model_from_state,
    parse_lock_events,
    save_timing_model_to_state,
)
from validator_kl_scoring import (
    kl_gate_combined,
    kl_gate_improvement_vs_baseline,
    kl_gate_validator_improve,
    kl_rows_from_payload,
)
from fast_kl_eval import PersistentFastKLEvaluator, run_fast_kl_eval_subprocess


SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_ENV_PATH = SCRIPT_DIR / ".env"
EVOLAI_ROOT = Path("/var/www/evolai")
EVOLAI_PYTHON = EVOLAI_ROOT / ".venv/bin/python"
CHALLENGE_SCRIPT = SCRIPT_DIR / "get_prev_seed_and_next_indices.py"
PREPARE_SCRIPT = SCRIPT_DIR / "cpu_pass_all_pipeline.py"
POST_TRAIN_GATE_SCRIPT = SCRIPT_DIR / "post_train_gate_check.py"
KL_EVAL_SCRIPT = SCRIPT_DIR / "validator_kl_eval.py"


def load_env_file(env_path: Path, *, override: bool = True) -> None:
    """Load KEY=VALUE pairs from a dotenv file.

    By default overrides existing os.environ entries so project `.env` wins
    over stale PM2/shell exports (e.g. TRAIN_CMD truncated to ``python3``).
    """
    if not env_path.exists():
        return
    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip("'").strip('"')
        if not key:
            continue
        if override or key not in os.environ:
            os.environ[key] = value


def env_str(name: str, default: str = "") -> str:
    return os.getenv(name, default).strip()


def env_bool(name: str, default: bool = False) -> bool:
    value = os.getenv(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "y", "on"}


def require(name: str) -> str:
    value = env_str(name)
    if not value:
        raise ValueError(f"Missing required env: {name}")
    return value


def send_telegram(message: str) -> None:
    bot_token = env_str("TELEGRAM_BOT_TOKEN")
    chat_id = env_str("TELEGRAM_CHAT_ID")
    if not bot_token or not chat_id:
        return
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = parse.urlencode({"chat_id": chat_id, "text": message}).encode("utf-8")
    req = request.Request(url, data=payload, method="POST")
    try:
        with request.urlopen(req, timeout=20):
            pass
    except Exception:
        pass


def notify(message: str, telegram: bool = True) -> None:
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    print(f"[{ts}] {message}", flush=True)
    if telegram:
        send_telegram(message)


def run(cmd: list[str], cwd: Optional[Path] = None, env: Optional[dict] = None) -> subprocess.CompletedProcess:
    return subprocess.run(
        cmd,
        cwd=str(cwd) if cwd else None,
        env=env,
        text=True,
        capture_output=True,
        check=False,
    )


def run_streaming(
    cmd: str,
    cwd: Optional[Path] = None,
    env: Optional[dict] = None,
) -> int:
    proc = subprocess.Popen(
        cmd,
        cwd=str(cwd) if cwd else None,
        env=env,
        shell=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        bufsize=1,
    )
    assert proc.stdout is not None
    for line in proc.stdout:
        print(line.rstrip("\n"), flush=True)
    return proc.wait()


def run_streaming_argv(
    argv: list[str],
    cwd: Optional[Path] = None,
    env: Optional[dict] = None,
) -> int:
    proc = subprocess.Popen(
        argv,
        cwd=str(cwd) if cwd else None,
        env=env,
        shell=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        bufsize=1,
    )
    assert proc.stdout is not None
    for line in proc.stdout:
        print(line.rstrip("\n"), flush=True)
    return proc.wait()


def parse_latest_eval_for_uid(log_file: Path, uid: int) -> dict[str, Any]:
    lines = log_file.read_text(encoding="utf-8").splitlines()
    rec = parse_eval_from_lines(lines, uid)
    rec["log_source"] = "file"
    return rec


def _read_log_lines(
    *,
    log_source: str,
    log_file: Path,
    wandb_tailer: WandbLogTailer | None,
    refresh: bool = True,
) -> list[str]:
    source = (log_source or "wandb").strip().lower()
    if source == "wandb":
        if wandb_tailer is None:
            wandb_tailer = WandbLogTailer.from_env(cache_dir=SCRIPT_DIR / ".wandb_cache")
        if refresh:
            wandb_tailer.refresh()
            mirror = Path(env_str("AUTO_LOG_FILE", str(SCRIPT_DIR / "log.md"))).resolve()
            if env_bool("WANDB_MIRROR_TO_LOCAL_LOG", True):
                wandb_tailer.append_to_local_log(mirror)
        return list(wandb_tailer.lines)
    if source == "file":
        if not log_file.exists():
            return []
        return log_file.read_text(encoding="utf-8").splitlines()
    raise ValueError(f"Unknown LOG_SOURCE={log_source!r}; use wandb or file")


def fetch_latest_eval(uid: int, *, log_source: str, log_file: Path, wandb_tailer: WandbLogTailer | None) -> dict[str, Any]:
    source = (log_source or "wandb").strip().lower()
    lines = _read_log_lines(
        log_source=source,
        log_file=log_file,
        wandb_tailer=wandb_tailer,
        refresh=True,
    )
    if source == "wandb":
        if wandb_tailer is None:
            wandb_tailer = WandbLogTailer.from_env(cache_dir=SCRIPT_DIR / ".wandb_cache")
        rec = wandb_tailer.latest_eval_for_uid(uid)
    elif source == "file":
        rec = parse_latest_eval_for_uid(log_file, uid)
    else:
        raise ValueError(f"Unknown LOG_SOURCE={log_source!r}; use wandb or file")
    return enrich_eval_record(rec, lines, uid)


def compute_dynamic_lock_window(
    eval_rec: dict[str, Any],
    log_lines: list[str],
    *,
    uid: int,
    agent_state: dict[str, Any],
    track: str = "transformer",
) -> dict[str, Any]:
    cached = load_timing_model_from_state(agent_state, uid, track=track)
    model = build_timing_model(log_lines, uid=uid, track=track, cached=cached)
    save_timing_model_to_state(agent_state, uid, model, track=track)
    locks = parse_lock_events(log_lines, track=track)
    age_s, _ = effective_lock_age_seconds(eval_rec)
    return estimate_lock_window(
        eval_rec,
        model,
        locks=locks,
        pipeline_age_s=age_s,
    )


def derive_challenge_json(uid: int, network: str, netuid: int, out_path: Path) -> dict[str, Any]:
    cmd = [
        sys.executable,
        str(CHALLENGE_SCRIPT),
        "--uid",
        str(uid),
        "--network",
        network,
        "--netuid",
        str(netuid),
        "--json",
    ]
    res = run(cmd, cwd=CHALLENGE_SCRIPT.parent)
    if res.returncode != 0:
        raise RuntimeError(f"Challenge script failed:\n{res.stderr}\n{res.stdout}")
    if res.stdout:
        print(res.stdout[-1000:], flush=True)
    out_path.write_text(res.stdout, encoding="utf-8")
    return json.loads(res.stdout)


def prepare_union_dataset(challenge_json: Path, out_dir: Path) -> None:
    cmd = [
        sys.executable,
        str(PREPARE_SCRIPT),
        "prepare-data",
        "--challenge-json",
        str(challenge_json),
        "--out-dir",
        str(out_dir),
    ]
    res = run(cmd, cwd=PREPARE_SCRIPT.parent)
    if res.returncode != 0:
        raise RuntimeError(f"prepare-data failed:\n{res.stderr}\n{res.stdout}")
    if res.stdout:
        print(res.stdout[-2000:], flush=True)


def _train_argv(cmd: str) -> list[str]:
    """Build argv for train_cpu_real.py; always use EvolAI venv (PM2/shell python3 lacks deps)."""
    if not EVOLAI_PYTHON.exists():
        raise RuntimeError(f"EvolAI python not found: {EVOLAI_PYTHON}")
    argv = shlex.split(cmd)
    if not argv:
        raise ValueError("empty TRAIN_CMD")
    script_i = next(
        (i for i, tok in enumerate(argv) if tok.endswith("train_cpu_real.py")),
        None,
    )
    if script_i is None:
        raise ValueError(f"TRAIN_CMD must invoke train_cpu_real.py, got: {cmd!r}")
    py = str(EVOLAI_PYTHON)
    if script_i == 0:
        return [py, *argv]
    argv[0] = py
    return argv


def run_training(train_cmd_template: str, env_extra: dict[str, str], cwd: Path) -> dict[str, Any]:
    if not train_cmd_template.strip():
        notify("[TRAIN] TRAIN_CMD is empty; skipping training.", telegram=False)
        return {"skipped": True}
    cmd = train_cmd_template.format(**env_extra)
    argv = _train_argv(cmd)
    notify(f"[TRAIN] Running: {' '.join(argv)}", telegram=False)
    code = run_streaming_argv(
        argv,
        cwd=cwd,
        env={**os.environ, **env_extra},
    )
    if code != 0:
        raise RuntimeError(f"Training command failed with exit code {code}")
    notify("[TRAIN] Training command completed.", telegram=False)
    return {
        "skipped": False,
        "command": " ".join(argv),
        "report_json": env_extra.get("TRAIN_REPORT_JSON", ""),
    }


def run_post_train_gate_check(
    report_json: Path,
    required_improvement: float,
    summary_json: Path,
) -> dict[str, Any]:
    cmd = [
        sys.executable,
        str(POST_TRAIN_GATE_SCRIPT),
        "--report-json",
        str(report_json),
        "--required-improvement",
        str(required_improvement),
        "--out-json",
        str(summary_json),
    ]
    res = run(cmd, cwd=POST_TRAIN_GATE_SCRIPT.parent)
    if res.returncode not in (0, 2):
        raise RuntimeError(f"post-train gate-check failed:\n{res.stderr}\n{res.stdout}")
    all_pass = "ALL_VALIDATORS_PASS=True" in res.stdout
    return {
        "all_pass": all_pass,
        "returncode": res.returncode,
        "stdout_tail": res.stdout[-2000:],
        "summary_json": str(summary_json),
    }


def _finalize_kl_payload(payload: dict[str, Any], *, require_vllm_mc: bool) -> dict[str, Any]:
    eval_meta = payload.get("eval_meta") if isinstance(payload, dict) else None
    mode_used = str((eval_meta or {}).get("ref_mode_used") or "").strip()
    if mode_used:
        notify(f"[KL] ref_mode_used={mode_used}", telegram=False)
    if require_vllm_mc and mode_used != "vllm_mc":
        raise RuntimeError(
            "KL eval parity check failed: require ref_mode_used=vllm_mc "
            f"but got {mode_used or '<missing>'}. "
            "Ensure KL_EVAL_REF_MODE=vllm and disable in-process fallback."
        )
    return payload


def _run_kl_eval_subprocess_validator(
    *,
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
    model_repo: str,
    model_revision: str,
    vllm_ref_url: str,
    start_vllm_ref: bool,
    allow_inprocess_fallback: bool,
    validator_uids: str,
) -> None:
    python_bin = EVOLAI_PYTHON if EVOLAI_PYTHON.exists() else Path(sys.executable)
    cmd = [
        str(python_bin),
        str(KL_EVAL_SCRIPT),
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
    notify(f"[KL] Running: {' '.join(cmd)}", telegram=False)
    kl_env = os.environ.copy()
    load_env_file(DEFAULT_ENV_PATH)
    kl_env.update(os.environ)
    kl_env.setdefault("KL_EVAL_KEEP_VLLM_REF", "true")
    kl_env.setdefault("KL_EVAL_STOP_VLLM_REF", "false")
    if model_repo:
        kl_env["MODEL_REPO"] = model_repo
    if model_revision:
        kl_env["MODEL_REVISION"] = model_revision
    code = run_streaming(
        " ".join(cmd),
        cwd=KL_EVAL_SCRIPT.parent,
        env=kl_env,
    )
    if code != 0:
        raise RuntimeError(
            f"KL eval failed with exit code {code} "
            f"(see [KL] lines above; common: vLLM startup, OOM, or missing data files)"
        )


def run_kl_eval(
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
    data_suffix: str = "_next",
    model_repo: str = "",
    model_revision: str = "",
    vllm_ref_url: str = "",
    start_vllm_ref: bool = False,
    allow_inprocess_fallback: bool = True,
    validator_uids: str = "",
    require_vllm_mc: bool = False,
    persistent_evaluator: PersistentFastKLEvaluator | None = None,
    use_persistent_fast: bool = True,
) -> dict[str, Any]:
    """KL eval: persistent in-process ref (fast) or subprocess fallback."""
    kl_env = os.environ.copy()
    load_env_file(DEFAULT_ENV_PATH)
    kl_env.update(os.environ)
    kl_env.setdefault("KL_EVAL_KEEP_VLLM_REF", "true")
    kl_env.setdefault("KL_EVAL_STOP_VLLM_REF", "false")
    if model_repo:
        kl_env["MODEL_REPO"] = model_repo
    if model_revision:
        kl_env["MODEL_REVISION"] = model_revision

    if use_persistent_fast and persistent_evaluator is not None:
        try:
            notify("[KL] persistent fast eval (reuse ref)", telegram=False)
            payload = persistent_evaluator.fast_eval(
                candidate_model_dir=model_dir,
                prep_out_dir=prep_out_dir,
                data_suffix=data_suffix,
                limit_per_validator=limit_per_validator,
                validator_uids=validator_uids,
                progress_every=progress_every,
                out_json=out_json,
                model_repo=model_repo,
                model_revision=model_revision,
            )
            return _finalize_kl_payload(payload, require_vllm_mc=require_vllm_mc)
        except Exception as exc:
            notify(
                f"[PERSISTENT_EVAL_FALLBACK] persistent eval failed: {exc}",
                telegram=False,
            )

    python_bin = EVOLAI_PYTHON if EVOLAI_PYTHON.exists() else Path(sys.executable)
    if use_persistent_fast:
        notify("[KL] fallback: fast_kl_eval.py subprocess", telegram=False)
        code = run_fast_kl_eval_subprocess(
            python_bin=python_bin,
            model_dir=model_dir,
            prep_out_dir=prep_out_dir,
            out_json=out_json,
            ref_model=ref_model,
            ref_tokenizer=ref_tokenizer,
            ref_mode=ref_mode,
            max_length=max_length,
            kl_max_new_tokens=kl_max_new_tokens,
            limit_per_validator=limit_per_validator,
            device=device,
            progress_every=progress_every,
            data_suffix=data_suffix,
            validator_uids=validator_uids,
            vllm_ref_url=vllm_ref_url,
            start_vllm_ref=start_vllm_ref,
            allow_inprocess_fallback=allow_inprocess_fallback,
            env=kl_env,
        )
        if code == 0 and out_json.exists():
            payload = json.loads(out_json.read_text(encoding="utf-8"))
            return _finalize_kl_payload(payload, require_vllm_mc=require_vllm_mc)
        notify(
            f"[PERSISTENT_EVAL_FALLBACK] fast_kl_eval subprocess exit={code}; "
            "trying validator_kl_eval.py",
            telegram=False,
        )

    _run_kl_eval_subprocess_validator(
        model_dir=model_dir,
        prep_out_dir=prep_out_dir,
        out_json=out_json,
        ref_model=ref_model,
        ref_tokenizer=ref_tokenizer,
        ref_mode=ref_mode,
        max_length=max_length,
        kl_max_new_tokens=kl_max_new_tokens,
        limit_per_validator=limit_per_validator,
        device=device,
        progress_every=progress_every,
        data_suffix=data_suffix,
        model_repo=model_repo,
        model_revision=model_revision,
        vllm_ref_url=vllm_ref_url,
        start_vllm_ref=start_vllm_ref,
        allow_inprocess_fallback=allow_inprocess_fallback,
        validator_uids=validator_uids,
    )
    payload = json.loads(out_json.read_text(encoding="utf-8"))
    return _finalize_kl_payload(payload, require_vllm_mc=require_vllm_mc)


def _parse_validator_uid_list(raw: str) -> list[int]:
    if not raw.strip():
        return []
    return [int(p.strip()) for p in raw.split(",") if p.strip()]


def _validator_files_for_suffix(
    prep_out_dir: Path,
    suffix: str,
    validator_uids: list[int],
) -> list[Path]:
    files = sorted(prep_out_dir.glob(f"validator_*{suffix}.jsonl"))
    if not validator_uids:
        return [f for f in files if f.stat().st_size > 0]
    out: list[Path] = []
    for f in files:
        stem = f.stem.replace("validator_", "", 1)
        if stem.endswith(suffix):
            vid = int(stem[: -len(suffix)])
        else:
            vid = int(stem.split("_")[0])
        if vid in validator_uids and f.stat().st_size > 0:
            out.append(f)
    return out


def resolve_validator_focus_path(
    prep_out_dir: Path,
    validator_uid: int,
    suffix: str,
) -> Path:
    """Path to validator_{uid}{suffix}.jsonl (e.g. validator_6_next.jsonl)."""
    s = suffix if suffix.startswith("_") else f"_{suffix}"
    return prep_out_dir / f"validator_{validator_uid}{s}.jsonl"


def resolve_kl_data_suffix(
    prep_out_dir: Path,
    preferred_suffix: str,
    validator_uids: str = "",
) -> str:
    """Pick a data suffix that has non-empty per-validator JSONL files."""
    preferred = (preferred_suffix or "_current").strip()
    if not preferred.startswith("_"):
        preferred = f"_{preferred}"

    uids = _parse_validator_uid_list(validator_uids)
    if _validator_files_for_suffix(prep_out_dir, preferred, uids):
        return preferred

    if preferred == "_current":
        for alt in ("_next",):
            if _validator_files_for_suffix(prep_out_dir, alt, uids):
                notify(
                    f"[DATA] No non-empty validator_*{preferred}.jsonl for "
                    f"UID(s) {uids or 'all'}; falling back to {alt} for KL eval",
                    telegram=False,
                )
                return alt

    raise RuntimeError(
        f"No validator data files for suffix {preferred!r} under {prep_out_dir} "
        f"(validator_uids={validator_uids or 'all'}). Re-run prepare-data."
    )


def _log_kl_gate_rows(gate_result: dict[str, Any], *, round_idx: int | None = None) -> None:
    prefix = f"[GATE] round={round_idx} " if round_idx is not None else "[GATE] "
    for row in gate_result.get("rows", []):
        vid = row.get("validator_uid")
        prev = float(row.get("prev_kl", float("nan")))
        req = float(row.get("required_kl", float("nan")))
        cur = float(row.get("current_kl", float("nan")))
        margin = float(row.get("margin", float("nan")))
        passed = bool(row.get("pass"))
        notify(
            f"{prefix}uid={vid} prev={prev:.4f} req={req:.4f} "
            f"cur={cur:.4f} margin={margin:.4f} pass={passed}",
            telegram=False,
        )
    if gate_result.get("gate_mode") == "both":
        for sub_name, sub_key in (
            ("baseline", "baseline_gate"),
            ("validator", "validator_gate"),
        ):
            sub = gate_result.get(sub_key)
            if isinstance(sub, dict):
                notify(
                    f"{prefix}{sub_name}_all_pass={sub.get('all_pass')}",
                    telegram=False,
                )


def _resolve_kl_gate(
    *,
    gate_mode: str,
    eval_rec: dict[str, Any],
    baseline_kl: dict[int, float],
    current_kl: dict[int, float],
    required_improvement: float,
    target_validator_uids: list[int],
) -> dict[str, Any]:
    mode = (gate_mode or "baseline_improvement").strip().lower()
    uids = target_validator_uids or None
    if mode in ("both", "combined", "strict"):
        return kl_gate_combined(
            eval_rec,
            baseline_kl,
            current_kl,
            required_improvement,
            target_validator_uids=uids,
        )
    if mode == "baseline_improvement":
        return kl_gate_improvement_vs_baseline(
            baseline_kl,
            current_kl,
            required_improvement,
            target_validator_uids=uids,
        )
    return kl_gate_validator_improve(
        eval_rec,
        current_kl,
        required_improvement=required_improvement,
        target_validator_uids=uids,
    )


def upload_model(api: HfApi, source_dir: Path, repo_id: str, message: str) -> str:
    if not source_dir.exists():
        raise RuntimeError(f"UPLOAD_SOURCE_DIR not found: {source_dir}")
    notify(f"[UPLOAD] {source_dir} -> {repo_id}", telegram=False)
    commit_info = api.upload_folder(
        repo_id=repo_id,
        repo_type="model",
        folder_path=str(source_dir),
        commit_message=message,
    )
    revision = getattr(commit_info, "oid", None) or getattr(commit_info, "sha", None)
    if not revision:
        info = api.model_info(repo_id=repo_id)
        revision = getattr(info, "sha", None)
    if not is_valid_sha(str(revision or "")):
        raise RuntimeError(f"Unable to read uploaded revision for {repo_id}")
    revision = verify_hf_revision(api, repo_id, str(revision))
    notify(f"[UPLOAD] done revision={revision}", telegram=False)
    return revision


def register_model(repo_id: str, track: str, wallet_name: str, wallet_path: str, hotkey: str, netuid: int, revision: str) -> None:
    cmd = [
        str(EVOLAI_PYTHON),
        "-m",
        "evolai.cli.main",
        "miner",
        "register",
        repo_id,
        "--revision",
        revision,
        "--track",
        track,
        "--wallet-name",
        wallet_name,
        "--wallet-path",
        wallet_path,
        "--hotkey",
        hotkey,
        "--netuid",
        str(netuid),
    ]
    notify(f"[REGISTER] repo={repo_id} revision={revision}", telegram=False)
    res = run(cmd, cwd=EVOLAI_ROOT)
    if res.stdout:
        print(res.stdout, flush=True)
    if res.returncode != 0:
        raise RuntimeError(f"Register failed:\n{res.stderr}\n{res.stdout}")
    notify("[REGISTER] done", telegram=False)


def run_pipeline(env_path: Path) -> int:
    load_env_file(env_path)

    uid = int(env_str("AUTO_UID", "93"))
    network = env_str("AUTO_NETWORK", "finney")
    netuid = int(env_str("REGISTER_NETUID", env_str("AUTO_NETUID", "47")))
    track = env_str("REGISTER_TRACK", "transformer")
    wallet_name = require("REGISTER_WALLET_NAME")
    wallet_path = env_str("REGISTER_WALLET_PATH", "~/.bittensor/wallets")
    hotkey = require("REGISTER_HOTKEY")

    hf_token = require("HF_TOKEN")
    upload_username = require("UPLOAD_USERNAME")
    upload_model_name = require("UPLOAD_MODEL_NAME")
    upload_repo_id = f"{upload_username}/{upload_model_name}"

    log_file = Path(env_str("AUTO_LOG_FILE", str(SCRIPT_DIR / "log.md"))).resolve()
    work_dir = Path(env_str("AUTO_WORK_DIR", str(SCRIPT_DIR))).resolve()
    challenge_json = Path(env_str("AUTO_CHALLENGE_JSON", str(SCRIPT_DIR / "challenge_latest.json"))).resolve()
    prep_out_dir = Path(env_str("AUTO_PREPARE_OUT_DIR", str(SCRIPT_DIR / "cpu_pass_all_data"))).resolve()
    eval_json = Path(env_str("AUTO_EVAL_JSON", str(SCRIPT_DIR / "latest_eval_record.json"))).resolve()
    summary_json = Path(env_str("AUTO_SUMMARY_JSON", str(SCRIPT_DIR / "full_auto_summary.json"))).resolve()
    train_cmd = env_str("TRAIN_CMD", "")
    train_enabled = env_bool("TRAIN_ENABLED", True)
    gate_check_enabled = env_bool("GATE_CHECK_ENABLED", True)
    gate_required_improvement = float(env_str("GATE_REQUIRED_IMPROVEMENT", "0.0"))
    gate_fail_action = env_str("GATE_FAIL_ACTION", "abort").lower()
    train_until_pass_enabled = env_bool("TRAIN_UNTIL_PASS_ENABLED", False)
    train_until_pass_max_rounds = int(env_str("TRAIN_UNTIL_PASS_MAX_ROUNDS", "5"))
    target_validator_uid = int(env_str("TARGET_VALIDATOR_UID", "0"))
    kl_eval_validator_uids = env_str("KL_EVAL_VALIDATOR_UIDS", "").strip()
    if not kl_eval_validator_uids and target_validator_uid > 0:
        kl_eval_validator_uids = str(target_validator_uid)
    kl_eval_enabled = env_bool("KL_EVAL_ENABLED", True)
    kl_eval_ref_model = env_str("KL_EVAL_REF_MODEL", "Qwen/Qwen3.5-9B")
    kl_eval_ref_tokenizer = env_str("KL_EVAL_REF_TOKENIZER", kl_eval_ref_model)
    kl_eval_ref_mode = env_str("KL_EVAL_REF_MODE", "auto")
    kl_eval_max_length = int(
        env_str("KL_EVAL_MAX_LENGTH", env_str("KL_EVAL_MAX_SEQ_LEN", "8192"))
    )
    kl_eval_kl_max_new_tokens = int(env_str("KL_EVAL_KL_MAX_NEW_TOKENS", "512"))
    kl_eval_limit_per_validator = int(env_str("KL_EVAL_LIMIT_PER_VALIDATOR", "20"))
    kl_eval_device = env_str("KL_EVAL_DEVICE", "auto")
    kl_eval_progress_every = int(env_str("KL_EVAL_PROGRESS_EVERY", "5"))
    kl_eval_gate_suffix = env_str("KL_EVAL_GATE_SUFFIX", env_str("KL_EVAL_DATA_SUFFIX", "_next"))
    kl_eval_report_suffix = env_str("KL_EVAL_REPORT_SUFFIX", "_current")
    train_focus_suffix = env_str("TRAIN_FOCUS_SUFFIX", kl_eval_gate_suffix)
    kl_eval_gate_mode = env_str("KL_EVAL_GATE_MODE", "baseline_improvement")
    target_validator_uid_list = _parse_validator_uid_list(kl_eval_validator_uids)
    vllm_ref_url = env_str("VLLM_REF_URL", "")
    start_vllm_ref = env_bool("KL_EVAL_START_VLLM_REF", False)
    kl_eval_fallback_inprocess = env_bool("KL_EVAL_FALLBACK_INPROCESS", True)
    kl_eval_require_vllm_mc = env_bool("KL_EVAL_REQUIRE_VLLM_MC", False)
    kl_eval_persistent_fast = env_bool("KL_EVAL_PERSISTENT_FAST", True)
    lock_timing_mode = env_str("LOCK_TIMING_MODE", "dynamic").strip().lower()
    validator_eval_interval_s = float(env_str("VALIDATOR_EVAL_INTERVAL_S", "720"))
    lock_risk_budget_fraction = float(env_str("LOCK_RISK_BUDGET_FRACTION", "0.40"))
    max_pipeline_seconds = float(env_str("MAX_PIPELINE_SECONDS", "0"))
    auto_state_path = Path(
        env_str("AUTO_STATE_FILE", str(SCRIPT_DIR / ".full_auto_uid_state.json"))
    ).resolve()
    skip_duplicate_eval = env_bool("AUTO_SKIP_DUPLICATE_EVAL", True)
    abort_on_high_lock_risk = env_bool("AUTO_ABORT_ON_HIGH_LOCK_RISK", True)
    abort_on_medium_lock_risk = env_bool("AUTO_ABORT_ON_MEDIUM_LOCK_RISK", True)
    fast_train_on_lock_risk = env_bool("AUTO_FAST_TRAIN_ON_LOCK_RISK", True)
    fast_train_cmd = env_str("FAST_TRAIN_CMD", "").strip()
    register_override = env_str("REGISTER_REVISION", "auto")
    log_source = env_str("LOG_SOURCE", "wandb").strip().lower()
    wandb_cache_dir = Path(env_str("WANDB_CACHE_DIR", str(SCRIPT_DIR / ".wandb_cache"))).resolve()
    wandb_tailer: WandbLogTailer | None = None
    if log_source == "wandb":
        wandb_tailer = WandbLogTailer.from_env(cache_dir=wandb_cache_dir)

    upload_source_dir_env = env_str("UPLOAD_SOURCE_DIR")
    if upload_source_dir_env:
        upload_source_dir = Path(upload_source_dir_env).expanduser().resolve()
    else:
        # Safe fallback: clone/copy currently selected local model folder.
        default_model_dir = env_str("AUTO_MODEL_DIR", str(SCRIPT_DIR / "models" / "evolai_test_challenge"))
        upload_source_dir = Path(default_model_dir).expanduser().resolve()

    summary_json.parent.mkdir(parents=True, exist_ok=True)
    challenge_json.parent.mkdir(parents=True, exist_ok=True)
    prep_out_dir.mkdir(parents=True, exist_ok=True)

    summary: Dict[str, Any] = {
        "started_at": time.time(),
        "uid": uid,
        "status": "running",
    }
    step = 0

    def step_log(label: str) -> float:
        nonlocal step
        step += 1
        notify(f"[STEP {step}] {label}", telegram=False)
        return time.time()

    try:
        notify(f"[BOOT] full_auto_uid_bot start uid={uid} netuid={netuid}", telegram=False)
        t = step_log("Parse latest UID evaluation block")
        eval_rec = fetch_latest_eval(
            uid,
            log_source=log_source,
            log_file=log_file,
            wandb_tailer=wandb_tailer,
        )
        trigger_unix = env_str("PIPELINE_TRIGGER_UNIX", "").strip()
        if trigger_unix:
            try:
                eval_rec["pipeline_trigger_unix"] = float(trigger_unix)
            except ValueError:
                pass
        eval_json.write_text(json.dumps(eval_rec, indent=2), encoding="utf-8")
        summary["latest_eval"] = eval_rec
        notify(f"[STEP {step}] done in {time.time()-t:.1f}s", telegram=False)

        agent_state = load_state(auto_state_path)

        def _resolve_lock_window(refresh_log: bool = False) -> dict[str, Any] | None:
            if lock_timing_mode == "fixed":
                return None
            lines = _read_log_lines(
                log_source=log_source,
                log_file=log_file,
                wandb_tailer=wandb_tailer,
                refresh=refresh_log,
            )
            if not lines:
                return None
            return compute_dynamic_lock_window(
                eval_rec,
                lines,
                uid=uid,
                agent_state=agent_state,
                track=track,
            )

        if skip_duplicate_eval:
            skip, skip_reason = should_skip_duplicate_eval(
                eval_rec, agent_state, uid=uid
            )
            summary["duplicate_eval_skip"] = {"skip": skip, "reason": skip_reason}
            if skip:
                notify(f"[SKIP] {skip_reason}", telegram=True)
                summary["status"] = "skipped_duplicate_eval"
                summary["finished_at"] = time.time()
                summary_json.write_text(json.dumps(summary, indent=2), encoding="utf-8")
                return 0

        def _assess_lock(*, refresh_log: bool = False) -> dict[str, Any]:
            lock_window = _resolve_lock_window(refresh_log=refresh_log)
            if lock_window is not None:
                eval_rec["lock_window"] = lock_window
            timing_local = get_subnet_timing(network=network, netuid=netuid)
            interval_s = validator_eval_interval_s
            max_pipe = max_pipeline_seconds
            if lock_window and lock_timing_mode == "dynamic":
                remaining = lock_window.get("remaining_until_lock_s")
                if remaining is not None and float(remaining) > 0:
                    interval_s = float(lock_window.get("post_gate_window_s") or interval_s)
                    if max_pipe <= 0:
                        max_pipe = max(
                            60.0,
                            float(remaining) * lock_risk_budget_fraction,
                        )
            elif max_pipe <= 0:
                max_pipe = lock_budget_seconds(interval_s, lock_risk_budget_fraction)
            risk = assess_lock_risk(
                eval_rec,
                validator_eval_interval_s=interval_s,
                budget_fraction=lock_risk_budget_fraction,
                blocks_remaining_in_epoch=timing_local.get("blocks_remaining_in_epoch"),
                max_pipeline_seconds=max_pipe if max_pipe > 0 else None,
                lock_window=lock_window,
            )
            save_state(auto_state_path, agent_state)
            return {**timing_local, "lock_risk": risk, "lock_window": lock_window}

        def _enforce_lock_risk(phase: str, lock_risk: dict[str, Any]) -> None:
            should_abort, why = lock_risk_should_abort(
                lock_risk,
                abort_high=abort_on_high_lock_risk,
                abort_medium=abort_on_medium_lock_risk,
            )
            if should_abort:
                msg = (
                    f"Lock-window risk at {phase} ({why}): validator may lock the old "
                    f"SHA before upload/register. budget={lock_risk.get('budget_seconds', 0):.0f}s "
                    f"age={lock_risk.get('age_seconds')}s"
                )
                notify(f"[LOCK] {msg}", telegram=True)
                raise RuntimeError(msg)

        t = step_log("Assess validator lock-window risk (log-driven)")
        timing = _assess_lock(refresh_log=False)
        lock_risk = timing["lock_risk"]
        lock_window = timing.get("lock_window")
        summary["timing"] = timing
        age_s, age_src = effective_lock_age_seconds(eval_rec)
        timing_msg = (
            f"[TIMING] block={timing.get('block')} epoch={timing.get('epoch')} "
            f"age={age_s:.0f}s ({age_src}) budget={lock_risk.get('budget_seconds', 0):.0f}s "
            f"risk={lock_risk['risk']} mode={lock_risk.get('timing_mode', '?')}"
        )
        if lock_window:
            timing_msg += (
                f" slot={lock_window.get('slot')}/{lock_window.get('total_miners')} "
                f"remaining={lock_window.get('remaining_until_lock_s', 0):.0f}s "
                f"round~{lock_window.get('round_duration_s', 0):.0f}s"
            )
        notify(timing_msg if age_s is not None else timing_msg.replace(" age=?", ""), telegram=False)
        for reason in lock_risk.get("reasons", []):
            notify(f"[TIMING] {reason}", telegram=False)
        _enforce_lock_risk("pipeline_start", lock_risk)
        use_fast_train = fast_train_on_lock_risk and lock_risk_requires_fast_train(lock_risk)
        if use_fast_train and fast_train_cmd:
            notify(
                f"[LOCK] Using FAST_TRAIN_CMD (risk={lock_risk['risk']})",
                telegram=False,
            )
            train_cmd = fast_train_cmd
        elif use_fast_train and train_cmd:
            notify(
                f"[LOCK] Lock risk={lock_risk['risk']}; keep TRAIN_CMD but budget is tight",
                telegram=False,
            )
        notify(f"[STEP {step}] done in {time.time()-t:.1f}s", telegram=False)

        t = step_log("Derive challenge indices from latest seeds")
        ch = derive_challenge_json(uid=uid, network=network, netuid=netuid, out_path=challenge_json)
        challenge_validator_uids = [
            int(v.get("validator_uid"))
            for v in ch.get("validators", [])
            if v.get("validator_uid") is not None
        ]
        if target_validator_uid > 0:
            if target_validator_uid not in challenge_validator_uids:
                raise RuntimeError(
                    f"TARGET_VALIDATOR_UID={target_validator_uid} not found in current challenge validators: "
                    f"{challenge_validator_uids}"
                )
            notify(
                f"[CHALLENGE] single-validator mode enabled: uid={target_validator_uid}",
                telegram=False,
            )
        summary["challenge"] = {
            "validators": len(ch.get("validators", [])),
            "validator_uids": challenge_validator_uids,
            "target_validator_uid": (target_validator_uid if target_validator_uid > 0 else None),
            "epoch": ch.get("current_epoch"),
            "block": ch.get("current_block"),
        }
        notify(
            f"[STEP {step}] done in {time.time()-t:.1f}s | validators={summary['challenge']['validators']}",
            telegram=False,
        )

        t = step_log("Prepare union/per-validator datasets")
        prepare_union_dataset(challenge_json, prep_out_dir)
        summary["prepared_data_dir"] = str(prep_out_dir)
        kl_eval_gate_suffix = resolve_kl_data_suffix(
            prep_out_dir,
            kl_eval_gate_suffix,
            kl_eval_validator_uids,
        )
        train_focus_suffix = resolve_kl_data_suffix(
            prep_out_dir,
            train_focus_suffix,
            kl_eval_validator_uids,
        )
        if kl_eval_report_suffix:
            try:
                kl_eval_report_suffix = resolve_kl_data_suffix(
                    prep_out_dir,
                    kl_eval_report_suffix,
                    kl_eval_validator_uids,
                )
            except RuntimeError:
                kl_eval_report_suffix = ""
        notify(
            f"[DATA] KL gate suffix={kl_eval_gate_suffix} train_focus suffix={train_focus_suffix}"
            + (
                f" report suffix={kl_eval_report_suffix}"
                if kl_eval_report_suffix
                else ""
            )
            + (
                f" target_validator={target_validator_uid}"
                if target_validator_uid > 0
                else ""
            ),
            telegram=False,
        )
        notify(f"[STEP {step}] done in {time.time()-t:.1f}s", telegram=False)

        env_extra = {
            "UID": str(uid),
            "CHALLENGE_JSON": str(challenge_json),
            "EVAL_JSON": str(eval_json),
            "PREP_OUT_DIR": str(prep_out_dir),
            "MODEL_DIR": str(upload_source_dir),
            "MODEL_REPO": eval_rec.get("model_repo", ""),
            "MODEL_REVISION": eval_rec.get("model_revision", ""),
            "TRAIN_REPORT_JSON": str(SCRIPT_DIR / "train_report.json"),
            "FOCUS_FILE": "",
        }
        summary["training"] = {"enabled": train_enabled}
        summary["gate_check"] = {"enabled": gate_check_enabled and train_enabled}

        baseline_kl_by_validator: dict[int, float] = {}
        persistent_kl_eval: PersistentFastKLEvaluator | None = None
        if train_enabled and kl_eval_enabled and kl_eval_persistent_fast:
            try:
                notify(
                    "[KL] creating PersistentFastKLEvaluator (ref loaded once per cycle)",
                    telegram=False,
                )
                persistent_kl_eval = PersistentFastKLEvaluator(
                    ref_model=kl_eval_ref_model,
                    ref_tokenizer=kl_eval_ref_tokenizer,
                    ref_mode=kl_eval_ref_mode,
                    device=kl_eval_device,
                    max_length=kl_eval_max_length,
                    kl_max_new_tokens=kl_eval_kl_max_new_tokens,
                    vllm_ref_url=vllm_ref_url,
                    start_vllm_ref=start_vllm_ref,
                    allow_inprocess_fallback=kl_eval_fallback_inprocess,
                    keep_vllm_on_close=True,
                )
            except Exception as exc:
                notify(
                    f"[PERSISTENT_EVAL_FALLBACK] init failed: {exc}",
                    telegram=False,
                )
                persistent_kl_eval = None

        kl_subproc_start_vllm = start_vllm_ref and persistent_kl_eval is None

        try:
            if train_enabled and kl_eval_enabled:
                t = step_log(
                    f"Baseline KL eval (gate suffix={kl_eval_gate_suffix}, validator parity)"
                )
                baseline_json = SCRIPT_DIR / "kl_eval_baseline.json"
                baseline_payload = run_kl_eval(
                    model_dir=upload_source_dir,
                    prep_out_dir=prep_out_dir,
                    out_json=baseline_json,
                    ref_model=kl_eval_ref_model,
                    ref_tokenizer=kl_eval_ref_tokenizer,
                    ref_mode=kl_eval_ref_mode,
                    max_length=kl_eval_max_length,
                    kl_max_new_tokens=kl_eval_kl_max_new_tokens,
                    limit_per_validator=kl_eval_limit_per_validator,
                    device=kl_eval_device,
                    progress_every=kl_eval_progress_every,
                    data_suffix=kl_eval_gate_suffix,
                    model_repo=eval_rec.get("model_repo", ""),
                    model_revision=eval_rec.get("model_revision", ""),
                    vllm_ref_url=vllm_ref_url,
                    start_vllm_ref=kl_subproc_start_vllm,
                    allow_inprocess_fallback=kl_eval_fallback_inprocess,
                    validator_uids=kl_eval_validator_uids,
                    require_vllm_mc=kl_eval_require_vllm_mc,
                    persistent_evaluator=persistent_kl_eval,
                    use_persistent_fast=kl_eval_persistent_fast,
                )
                baseline_kl_by_validator = kl_rows_from_payload(
                    baseline_payload, use_adjusted=True
                )
                summary["kl_baseline"] = baseline_payload
                notify(
                    f"[KL] baseline gate suffix={kl_eval_gate_suffix} "
                    f"mode={kl_eval_gate_mode} required_improvement={gate_required_improvement}",
                    telegram=False,
                )
                for vid, bkl in sorted(baseline_kl_by_validator.items()):
                    req = bkl * (1.0 - gate_required_improvement)
                    notify(
                        f"[KL] baseline uid={vid} kl_adj={bkl:.4f} "
                        f"gate_req={req:.4f} (must beat after train)",
                        telegram=False,
                    )
                wandb_cur = eval_rec.get("cur_kl")
                if wandb_cur is not None and target_validator_uid_list:
                    vid = target_validator_uid_list[0]
                    local_b = baseline_kl_by_validator.get(vid)
                    if local_b is not None:
                        notify(
                            f"[KL] baseline uid={vid} local_adj={local_b:.4f} "
                            f"wandb_cur={float(wandb_cur):.4f} "
                            f"wandb_req={float(eval_rec.get('req_kl') or 0):.4f}",
                            telegram=False,
                        )
                notify(f"[STEP {step}] done in {time.time()-t:.1f}s", telegram=False)

            if train_enabled:
                if train_until_pass_enabled and gate_check_enabled:
                    t = step_log(
                        f"Train-until-pass loop (max_rounds={train_until_pass_max_rounds}, "
                        f"required_improvement={gate_required_improvement})"
                    )
                    loop_rounds: list[dict[str, Any]] = []
                    passed = False
                    last_gate_result: dict[str, Any] | None = None
                    for ridx in range(1, max(1, train_until_pass_max_rounds) + 1):
                        # single-validator mode: always focus configured validator file
                        if target_validator_uid > 0:
                            focus = resolve_validator_focus_path(
                                prep_out_dir,
                                target_validator_uid,
                                train_focus_suffix,
                            )
                            if focus.exists() and focus.stat().st_size > 0:
                                env_extra["FOCUS_FILE"] = str(focus)
                            else:
                                alt = resolve_validator_focus_path(
                                    prep_out_dir,
                                    target_validator_uid,
                                    kl_eval_gate_suffix,
                                )
                                if alt.exists() and alt.stat().st_size > 0:
                                    env_extra["FOCUS_FILE"] = str(alt)
                                else:
                                    union_focus = prep_out_dir / f"union{train_focus_suffix}.jsonl"
                                    env_extra["FOCUS_FILE"] = str(union_focus)
                                    notify(
                                        f"[LOOP] round {ridx}: validator_{target_validator_uid} "
                                        f"missing; fall back to {union_focus.name}",
                                        telegram=False,
                                    )
                            notify(
                                f"[LOOP] round {ridx}: focus validator {target_validator_uid} "
                                f"next-challenge file={env_extra['FOCUS_FILE']}",
                                telegram=False,
                            )
                        # worst-validator-focused schedule
                        elif last_gate_result and last_gate_result.get("worst_validator_uid") is not None:
                            wuid = int(last_gate_result["worst_validator_uid"])
                            focus = resolve_validator_focus_path(
                                prep_out_dir, wuid, train_focus_suffix
                            )
                            if focus.exists():
                                env_extra["FOCUS_FILE"] = str(focus)
                            else:
                                union_focus = prep_out_dir / f"union{train_focus_suffix}.jsonl"
                                env_extra["FOCUS_FILE"] = str(union_focus)
                                notify(
                                    f"[LOOP] round {ridx}: validator file missing for {wuid}; "
                                    f"falling back to {union_focus.name}",
                                    telegram=False,
                                )
                            notify(
                                f"[LOOP] round {ridx}: focusing validator {wuid} file={env_extra['FOCUS_FILE']}",
                                telegram=False,
                            )
                        else:
                            union_focus = prep_out_dir / f"union{train_focus_suffix}.jsonl"
                            env_extra["FOCUS_FILE"] = str(union_focus)
                            notify(
                                f"[LOOP] round {ridx}: no focus file, using union file={env_extra['FOCUS_FILE']}",
                                telegram=False,
                            )

                        notify(f"[LOOP] round {ridx}/{train_until_pass_max_rounds}: training", telegram=False)
                        train_result = run_training(train_cmd, env_extra=env_extra, cwd=work_dir)
                        report_json = Path(env_extra["TRAIN_REPORT_JSON"])
                        if not report_json.exists():
                            raise RuntimeError(
                                f"Training report not found after round {ridx}: {report_json}"
                            )
                        if kl_eval_enabled:
                            round_kl_json = SCRIPT_DIR / f"kl_eval_round{ridx}.json"
                            round_kl = run_kl_eval(
                                model_dir=upload_source_dir,
                                prep_out_dir=prep_out_dir,
                                out_json=round_kl_json,
                                ref_model=kl_eval_ref_model,
                                ref_tokenizer=kl_eval_ref_tokenizer,
                                ref_mode=kl_eval_ref_mode,
                                max_length=kl_eval_max_length,
                                kl_max_new_tokens=kl_eval_kl_max_new_tokens,
                                limit_per_validator=kl_eval_limit_per_validator,
                                device=kl_eval_device,
                                progress_every=kl_eval_progress_every,
                                data_suffix=kl_eval_gate_suffix,
                                model_repo=eval_rec.get("model_repo", ""),
                                model_revision=eval_rec.get("model_revision", ""),
                                vllm_ref_url=vllm_ref_url,
                                start_vllm_ref=False,
                                allow_inprocess_fallback=kl_eval_fallback_inprocess,
                                validator_uids=kl_eval_validator_uids,
                                require_vllm_mc=kl_eval_require_vllm_mc,
                                persistent_evaluator=persistent_kl_eval,
                                use_persistent_fast=kl_eval_persistent_fast,
                            )
                            cur_kl_by_validator = kl_rows_from_payload(round_kl, use_adjusted=True)
                            gate_result = _resolve_kl_gate(
                                gate_mode=kl_eval_gate_mode,
                                eval_rec=eval_rec,
                                baseline_kl=baseline_kl_by_validator,
                                current_kl=cur_kl_by_validator,
                                required_improvement=gate_required_improvement,
                                target_validator_uids=target_validator_uid_list,
                            )
                            gate_result["kl_eval_json"] = str(round_kl_json)
                            _log_kl_gate_rows(gate_result, round_idx=ridx)

                            if (
                                kl_eval_report_suffix
                                and kl_eval_report_suffix != kl_eval_gate_suffix
                            ):
                                next_kl_json = SCRIPT_DIR / f"kl_eval_round{ridx}_next.json"
                                next_kl = run_kl_eval(
                                    model_dir=upload_source_dir,
                                    prep_out_dir=prep_out_dir,
                                    out_json=next_kl_json,
                                    ref_model=kl_eval_ref_model,
                                    ref_tokenizer=kl_eval_ref_tokenizer,
                                    ref_mode=kl_eval_ref_mode,
                                    max_length=kl_eval_max_length,
                                    kl_max_new_tokens=kl_eval_kl_max_new_tokens,
                                    limit_per_validator=kl_eval_limit_per_validator,
                                    device=kl_eval_device,
                                    progress_every=kl_eval_progress_every,
                                    data_suffix=kl_eval_report_suffix,
                                    model_repo=eval_rec.get("model_repo", ""),
                                    model_revision=eval_rec.get("model_revision", ""),
                                    vllm_ref_url=vllm_ref_url,
                                    start_vllm_ref=False,
                                    allow_inprocess_fallback=kl_eval_fallback_inprocess,
                                    validator_uids=kl_eval_validator_uids,
                                    require_vllm_mc=kl_eval_require_vllm_mc,
                                    persistent_evaluator=persistent_kl_eval,
                                    use_persistent_fast=kl_eval_persistent_fast,
                                )
                                next_by_vid = kl_rows_from_payload(next_kl, use_adjusted=True)
                                gate_result["next_kl_by_validator"] = next_by_vid
                                gate_result["next_kl_eval_json"] = str(next_kl_json)
                                wandb_next = eval_rec.get("next_kl")
                                if wandb_next is not None and target_validator_uid_list:
                                    vid = target_validator_uid_list[0]
                                    local_n = next_by_vid.get(vid)
                                    if local_n is not None:
                                        notify(
                                            f"[KL] round {ridx} uid={vid} "
                                            f"local_next_adj={local_n:.4f} "
                                            f"wandb_next={float(wandb_next):.4f}",
                                            telegram=False,
                                        )

                            if target_validator_uid_list:
                                vid = target_validator_uid_list[0]
                                local_c = cur_kl_by_validator.get(vid)
                                if local_c is not None:
                                    notify(
                                        f"[KL] round {ridx} gate uid={vid} "
                                        f"local_cur_adj={local_c:.4f} "
                                        f"wandb_cur={float(eval_rec.get('cur_kl') or 0):.4f} "
                                        f"wandb_req={float(eval_rec.get('req_kl') or 0):.4f} "
                                        f"pass={gate_result['all_pass']}",
                                        telegram=False,
                                    )
                        else:
                            gate_summary_json = SCRIPT_DIR / f"post_train_gate_summary_round{ridx}.json"
                            gate_result = run_post_train_gate_check(
                                report_json=report_json,
                                required_improvement=gate_required_improvement,
                                summary_json=gate_summary_json,
                            )
                        loop_rounds.append(
                            {
                                "round": ridx,
                                "train": train_result,
                                "gate": gate_result,
                                "focus_file": env_extra.get("FOCUS_FILE", ""),
                            }
                        )
                        last_gate_result = gate_result
                        notify(
                            f"[LOOP] round {ridx}: gate all_pass={gate_result['all_pass']}",
                            telegram=False,
                        )
                        if gate_result["all_pass"]:
                            passed = True
                            break

                    summary["training"] = {
                        "enabled": True,
                        "train_until_pass": True,
                        "max_rounds": train_until_pass_max_rounds,
                        "rounds_executed": len(loop_rounds),
                        "passed": passed,
                        "rounds": loop_rounds,
                    }
                    summary["gate_check"] = {
                        "enabled": True,
                        "required_improvement": gate_required_improvement,
                        "all_pass": passed,
                        "last_round": loop_rounds[-1]["gate"] if loop_rounds else None,
                    }
                    notify(
                        f"[STEP {step}] done in {time.time()-t:.1f}s | pass={passed} rounds={len(loop_rounds)}",
                        telegram=False,
                    )
                    if not passed and gate_fail_action == "abort":
                        raise RuntimeError(
                            "Train-until-pass exhausted rounds without passing gate; "
                            "aborting upload/register due to GATE_FAIL_ACTION=abort."
                        )
                else:
                    t = step_log("Run training command")
                    train_result = run_training(train_cmd, env_extra=env_extra, cwd=work_dir)
                    summary["training"] = {"enabled": True, **train_result}
                    notify(f"[STEP {step}] done in {time.time()-t:.1f}s", telegram=False)

                    if gate_check_enabled:
                        t = step_log("Run post-train gate check")
                        report_json = Path(env_extra["TRAIN_REPORT_JSON"])
                        if not report_json.exists():
                            raise RuntimeError(
                                f"GATE_CHECK_ENABLED=true but training report not found: {report_json}"
                            )
                        gate_summary_json = SCRIPT_DIR / "post_train_gate_summary.json"
                        gate_result = run_post_train_gate_check(
                            report_json=report_json,
                            required_improvement=gate_required_improvement,
                            summary_json=gate_summary_json,
                        )
                        summary["gate_check"] = gate_result
                        notify(
                            f"[STEP {step}] done in {time.time()-t:.1f}s | all_pass={gate_result['all_pass']}",
                            telegram=False,
                        )
                        if not gate_result["all_pass"] and gate_fail_action == "abort":
                            raise RuntimeError(
                                "Post-train gate-check failed (not all validators pass); "
                                "aborting upload/register due to GATE_FAIL_ACTION=abort."
                            )
        finally:
            if persistent_kl_eval is not None:
                notify(
                    "[KL] closing PersistentFastKLEvaluator (end of cycle)",
                    telegram=False,
                )
                persistent_kl_eval.close()

        t = step_log("Pre-upload lock-window check")
        timing_pre = _assess_lock(refresh_log=True)
        lock_pre = timing_pre["lock_risk"]
        summary["timing_pre_upload"] = timing_pre
        _enforce_lock_risk("pre_upload", lock_pre)
        age_pre, _ = effective_lock_age_seconds(eval_rec)
        # MAX_PIPELINE_SECONDS=0 means no hard cap (see README / .env.example).
        if (
            max_pipeline_seconds > 0
            and age_pre is not None
            and age_pre > max_pipeline_seconds
        ):
            raise RuntimeError(
                f"Pipeline exceeded MAX_PIPELINE_SECONDS ({max_pipeline_seconds:.0f}s); "
                "upload/register would likely miss the next validator lock"
            )
        notify(f"[STEP {step}] done in {time.time()-t:.1f}s", telegram=False)

        t = step_log("Upload model to Hugging Face")
        api = HfApi(token=hf_token)
        commit_message = env_str("UPLOAD_COMMIT_MESSAGE", "Auto train+publish via full_auto_uid_bot")
        uploaded_revision = upload_model(api, upload_source_dir, upload_repo_id, commit_message)
        summary["upload"] = {
            "repo_id": upload_repo_id,
            "source_dir": str(upload_source_dir),
            "revision": uploaded_revision,
        }
        notify(f"[STEP {step}] done in {time.time()-t:.1f}s", telegram=False)

        t = step_log("Register model on subnet")
        register_revision = resolve_register_revision(
            uploaded_revision,
            register_override,
        )
        if register_revision == str(eval_rec.get("model_revision", "")).lower():
            notify(
                "[WARN] New registered revision matches the last evaluated revision. "
                "If the validator already locked this SHA, expect Improve same SHA.",
                telegram=True,
            )
        register_model(
            repo_id=upload_repo_id,
            track=track,
            wallet_name=wallet_name,
            wallet_path=wallet_path,
            hotkey=hotkey,
            netuid=netuid,
            revision=register_revision,
        )
        summary["register"] = {
            "repo_id": upload_repo_id,
            "revision": register_revision,
            "uploaded_revision": uploaded_revision,
            "track": track,
        }
        notify(f"[STEP {step}] done in {time.time()-t:.1f}s", telegram=False)

        mark_pipeline_success(
            agent_state,
            uid=uid,
            eval_revision=str(eval_rec.get("model_revision") or ""),
            registered_revision=register_revision,
            block=timing.get("block"),
        )
        save_state(auto_state_path, agent_state)
        summary["agent_state_file"] = str(auto_state_path)

        summary["status"] = "success"
        summary["finished_at"] = time.time()
        summary_json.write_text(json.dumps(summary, indent=2), encoding="utf-8")
        notify("[SUCCESS] full_auto_uid_bot completed", telegram=True)
        return 0
    except Exception as exc:
        summary["status"] = "failed"
        summary["error"] = str(exc)
        summary["finished_at"] = time.time()
        summary_json.write_text(json.dumps(summary, indent=2), encoding="utf-8")
        message = f"[FAILED] full_auto_uid_bot: {exc}"
        print(message, file=sys.stderr, flush=True)
        traceback.print_exc()
        send_telegram(message)
        return 1


def main() -> int:
    env_path = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else DEFAULT_ENV_PATH
    load_env_file(env_path)

    if env_bool("AUTO_WATCH_MODE", True):
        poll_s = int(env_str("AUTO_WATCH_POLL_SECONDS", "15"))
        error_sleep_s = int(env_str("AUTO_WATCH_ERROR_SLEEP_SECONDS", "30"))
        uid = int(env_str("AUTO_UID", "93"))
        log_file = Path(env_str("AUTO_LOG_FILE", str(SCRIPT_DIR / "log.md"))).resolve()
        log_source = env_str("LOG_SOURCE", "wandb").strip().lower()
        wandb_cache_dir = Path(env_str("WANDB_CACHE_DIR", str(SCRIPT_DIR / ".wandb_cache"))).resolve()
        wandb_tailer = WandbLogTailer.from_env(cache_dir=wandb_cache_dir) if log_source == "wandb" else None
        auto_state_path = Path(
            env_str("AUTO_STATE_FILE", str(SCRIPT_DIR / ".full_auto_uid_state.json"))
        ).resolve()
        notify(
            f"[WATCH] uid={uid} source={log_source} poll={poll_s}s "
            "(trigger only on new completed eval)",
            telegram=False,
        )
        if log_source == "wandb":
            notify(f"[WATCH] wandb run={wandb_tailer.run_path if wandb_tailer else '?'}", telegram=False)
        else:
            notify(f"[WATCH] log file={log_file}", telegram=False)
        while True:
            try:
                load_env_file(env_path)
                state = load_state(auto_state_path)
                try:
                    eval_rec = fetch_latest_eval(
                        uid,
                        log_source=log_source,
                        log_file=log_file,
                        wandb_tailer=wandb_tailer,
                    )
                except RuntimeError as exc:
                    notify(f"[WATCH] {exc}", telegram=False)
                    time.sleep(poll_s)
                    continue

                if not eval_is_complete(eval_rec):
                    time.sleep(poll_s)
                    continue

                eval_rev = str(eval_rec.get("model_revision") or "").lower()
                trigger_key = watch_eval_trigger_key(uid)
                if not is_valid_sha(eval_rev):
                    time.sleep(poll_s)
                    continue
                if state.get(trigger_key) == eval_rev:
                    time.sleep(poll_s)
                    continue

                state[trigger_key] = eval_rev
                save_state(auto_state_path, state)
                eval_rec["pipeline_trigger_unix"] = time.time()
                os.environ["PIPELINE_TRIGGER_UNIX"] = str(eval_rec["pipeline_trigger_unix"])

                notify(
                    f"[WATCH] New eval {eval_rev[:12]} gate={eval_rec.get('gate')} "
                    "— starting pipeline",
                    telegram=True,
                )
                code = run_pipeline(env_path)
                if code != 0:
                    state = load_state(auto_state_path)
                    if state.get(trigger_key) == eval_rev:
                        state.pop(trigger_key, None)
                        save_state(auto_state_path, state)
                        notify(
                            f"[WATCH] Pipeline failed; will retry eval {eval_rev[:12]}",
                            telegram=False,
                        )
                os.environ.pop("PIPELINE_TRIGGER_UNIX", None)
                sleep_s = error_sleep_s if code != 0 else poll_s
                time.sleep(sleep_s)
            except KeyboardInterrupt:
                notify("[WATCH] stopped by user", telegram=False)
                return 0

    return run_pipeline(env_path)


if __name__ == "__main__":
    raise SystemExit(main())
