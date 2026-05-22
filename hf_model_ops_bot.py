#!/usr/bin/env python3
import json
import os
import subprocess
import sys
import time
import traceback
from pathlib import Path
from typing import Dict, Optional
from urllib import parse, request

from huggingface_hub import HfApi, snapshot_download


SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_ENV_PATH = SCRIPT_DIR / ".env"
EVOLAI_PYTHON = Path("/root/sn47/evolai/.venv/bin/python")
DEFAULT_STATE_PATH = SCRIPT_DIR / ".hf_model_ops_state.json"


def load_env_file(env_path: Path) -> None:
    if not env_path.exists():
        return
    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip("'").strip('"')
        if key and key not in os.environ:
            os.environ[key] = value


def env_str(name: str, default: str = "") -> str:
    return os.getenv(name, default).strip()


def env_bool(name: str, default: bool = False) -> bool:
    value = os.getenv(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "y", "on"}


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
        # Keep bot flow running even if telegram fails.
        pass


def notify(message: str, telegram: bool = True) -> None:
    print(message, flush=True)
    if telegram:
        send_telegram(message)


def require(name: str) -> str:
    value = env_str(name)
    if not value:
        raise ValueError(f"Missing required env: {name}")
    return value


def download_model(api: HfApi) -> Path:
    username = require("DOWNLOAD_USERNAME")
    model_name = require("DOWNLOAD_MODEL_NAME")
    target_dir = Path(env_str("DOWNLOAD_TARGET_DIR", str(SCRIPT_DIR / "models")))
    target_dir.mkdir(parents=True, exist_ok=True)
    repo_id = f"{username}/{model_name}"
    local_dir = target_dir / model_name

    notify(f"[START] Download model: {repo_id}", telegram=False)
    snapshot_download(
        repo_id=repo_id,
        local_dir=str(local_dir),
        token=env_str("HF_TOKEN"),
    )
    notify(f"[DONE] Download completed: {repo_id} -> {local_dir}", telegram=False)
    return local_dir


def upload_model(api: HfApi, source_dir: Optional[Path]) -> Dict[str, str]:
    username = require("UPLOAD_USERNAME")
    model_name = require("UPLOAD_MODEL_NAME")

    if source_dir is None:
        upload_source_env = env_str("UPLOAD_SOURCE_DIR")
        if upload_source_env:
            source_dir = Path(upload_source_env)

    if source_dir is None:
        raise ValueError(
            "UPLOAD_SOURCE_DIR is required when no downloaded directory is available."
        )
    if not source_dir.exists() or not source_dir.is_dir():
        raise ValueError(f"Upload source directory not found: {source_dir}")

    repo_id = f"{username}/{model_name}"

    notify(f"[START] Upload folder: {source_dir} -> {repo_id}", telegram=False)
    api.upload_folder(
        repo_id=repo_id,
        repo_type="model",
        folder_path=str(source_dir),
        commit_message="Upload model via sn-47-agent bot",
    )

    info = api.model_info(repo_id=repo_id)
    revision = getattr(info, "sha", None)
    if not revision:
        raise RuntimeError(f"Could not get revision sha for {repo_id}")

    notify(
        f"[DONE] Upload completed: {repo_id} (revision={revision})", telegram=False
    )
    return {"repo_id": repo_id, "revision": revision}


def register_model(repo_id: str, revision: str) -> None:
    if not EVOLAI_PYTHON.exists():
        raise FileNotFoundError(f"EvolAI python not found: {EVOLAI_PYTHON}")

    track = env_str("REGISTER_TRACK", "transformer")
    wallet_name = require("REGISTER_WALLET_NAME")
    hotkey = require("REGISTER_HOTKEY")
    netuid = env_str("REGISTER_NETUID", "47")

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
        "--hotkey",
        hotkey,
        "--netuid",
        netuid,
    ]

    notify(f"[START] Register model in EvolAI: {repo_id}", telegram=False)
    result = subprocess.run(
        cmd,
        cwd="/root/sn47/evolai",
        text=True,
        capture_output=True,
        check=False,
    )
    if result.stdout:
        print(result.stdout, flush=True)
    if result.returncode != 0:
        if result.stderr:
            print(result.stderr, file=sys.stderr, flush=True)
        raise RuntimeError(
            f"EvolAI register failed (exit={result.returncode}) for {repo_id}"
        )
    notify(f"[DONE] Register completed: {repo_id}", telegram=False)


def source_repo_id() -> str:
    username = require("DOWNLOAD_USERNAME")
    model_name = require("DOWNLOAD_MODEL_NAME")
    return f"{username}/{model_name}"


def source_head_revision(api: HfApi) -> str:
    repo_id = source_repo_id()
    info = api.model_info(repo_id=repo_id)
    revision = getattr(info, "sha", None)
    if not revision:
        raise RuntimeError(f"Could not read source revision for {repo_id}")
    return revision


def load_state(state_path: Path) -> Dict[str, str]:
    if not state_path.exists():
        return {}
    try:
        data = json.loads(state_path.read_text(encoding="utf-8"))
        if isinstance(data, dict):
            return {str(k): str(v) for k, v in data.items()}
    except Exception:
        pass
    return {}


def save_state(state_path: Path, state: Dict[str, str]) -> None:
    state_path.write_text(json.dumps(state, indent=2), encoding="utf-8")


def run_pipeline_once(api: HfApi) -> Dict[str, str]:
    started_at = time.monotonic()
    downloaded_dir: Optional[Path] = None
    upload_result: Optional[Dict[str, str]] = None

    run_download = env_bool("RUN_DOWNLOAD", True)
    run_upload = env_bool("RUN_UPLOAD", True)
    run_register = env_bool("RUN_REGISTER", True)

    if run_download:
        downloaded_dir = download_model(api)
    if run_upload:
        upload_result = upload_model(api, source_dir=downloaded_dir)
    if run_register:
        if not upload_result:
            repo_id = require("REGISTER_REPO_ID")
            revision = require("REGISTER_REVISION")
            register_model(repo_id, revision)
        else:
            register_model(upload_result["repo_id"], upload_result["revision"])

    elapsed_sec = time.monotonic() - started_at
    if upload_result:
        summary = (
            "[SUCCESS] Pipeline completed | "
            f"model={upload_result['repo_id']} | "
            f"revision={upload_result['revision']} | "
            f"elapsed={elapsed_sec:.1f}s"
        )
    else:
        summary = f"[SUCCESS] Pipeline completed | elapsed={elapsed_sec:.1f}s"
    notify(summary, telegram=True)
    return upload_result or {}


def main() -> int:
    env_path = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else DEFAULT_ENV_PATH
    load_env_file(env_path)

    hf_token = require("HF_TOKEN")
    api = HfApi(token=hf_token)
    watch_mode = env_bool("WATCH_MODE", False)

    notify("[BOOT] sn-47-agent HF model bot started", telegram=False)

    if not watch_mode:
        run_pipeline_once(api)
        return 0

    if not env_bool("RUN_DOWNLOAD", True):
        raise ValueError("WATCH_MODE requires RUN_DOWNLOAD=true")

    poll_seconds = int(env_str("WATCH_POLL_SECONDS", "60"))
    state_path = Path(env_str("STATE_FILE_PATH", str(DEFAULT_STATE_PATH)))
    state = load_state(state_path)
    src_repo = source_repo_id()
    last_seen_key = f"last_seen:{src_repo}"
    last_done_key = f"last_done:{src_repo}"

    notify(
        f"[WATCH] Watching {src_repo} for new commits every {poll_seconds}s "
        f"(state: {state_path})",
        telegram=False,
    )
    error_sleep_seconds = int(env_str("WATCH_ERROR_SLEEP_SECONDS", "30"))
    while True:
        try:
            current = source_head_revision(api)
            if state.get(last_seen_key) != current:
                state[last_seen_key] = current
                save_state(state_path, state)
                notify(f"[WATCH] New source commit detected: {current}", telegram=False)

            if state.get(last_done_key) != current:
                notify(
                    f"[WATCH] Triggering pipeline for source commit: {current}",
                    telegram=False,
                )
                run_pipeline_once(api)
                # Collapse multiple upstream commits: after one pipeline run, mark
                # the newest head as done so we do not replay intermediate commits.
                latest_after_run = source_head_revision(api)
                state[last_done_key] = latest_after_run
                save_state(state_path, state)
                notify(
                    "[WATCH] Completed pipeline. "
                    f"Marked latest source commit as done: {latest_after_run}",
                    telegram=False,
                )
            else:
                notify(f"[WATCH] No new source commit. Current: {current}", telegram=False)

            time.sleep(poll_seconds)
        except Exception as exc:
            message = f"[WATCH][ERROR] {exc}"
            print(message, file=sys.stderr, flush=True)
            traceback.print_exc()
            send_telegram(message)
            time.sleep(error_sleep_seconds)

    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        message = f"[FAILED] {exc}"
        print(message, file=sys.stderr, flush=True)
        traceback.print_exc()
        send_telegram(message)
        raise
