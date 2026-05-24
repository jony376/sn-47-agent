#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import time
import traceback
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Optional
from urllib import parse, request

from huggingface_hub import HfApi


SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_ENV_PATH = SCRIPT_DIR / ".env"
EVOLAI_ROOT = Path("/root/sn47/evolai")
EVOLAI_PYTHON = EVOLAI_ROOT / ".venv/bin/python"
CHALLENGE_SCRIPT = SCRIPT_DIR / "get_prev_seed_and_next_indices.py"
PREPARE_SCRIPT = SCRIPT_DIR / "cpu_pass_all_pipeline.py"
POST_TRAIN_GATE_SCRIPT = SCRIPT_DIR / "post_train_gate_check.py"


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


def parse_latest_eval_for_uid(log_file: Path, uid: int) -> dict[str, Any]:
    lines = log_file.read_text(encoding="utf-8").splitlines()
    start_pat = re.compile(
        rf"^(\d{{4}}-\d{{2}}-\d{{2}} \d{{2}}:\d{{2}}:\d{{2}})\s+\[\d+/\d+\]\s+UID {uid}\s+\|\s+(.+?)\s+@$"
    )
    rev_pat = re.compile(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\s+([0-9a-f]{40})\s+\|")
    gate_pat = re.compile(
        r"Gate\s+(PASS|FAIL).+cur=([0-9.]+)\s+req<=([0-9.]+)\s+prev=([0-9.]+)"
    )
    kl_pat = re.compile(r"\|\s+KL\s+([0-9.]+)\s+\|\s+NextKL\s+([0-9.]+)")

    starts = [i for i, ln in enumerate(lines) if start_pat.search(ln)]
    if not starts:
        raise RuntimeError(f"No eval block found for UID {uid} in {log_file}")
    s_idx = starts[-1]
    e_idx = len(lines)
    for i in range(s_idx + 1, len(lines)):
        if re.search(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\s+\[\d+/\d+\]\s+UID \d+\s+\|", lines[i]):
            e_idx = i
            break
    block = lines[s_idx:e_idx]
    m = start_pat.search(block[0])
    assert m is not None
    out: dict[str, Any] = {
        "uid": uid,
        "timestamp": m.group(1),
        "model_repo": m.group(2).strip(),
        "model_revision": "",
        "challenge": None,
        "kl": None,
        "next_kl": None,
        "gate": None,
        "cur_kl": None,
        "req_kl": None,
        "prev_kl": None,
        "raw_block": block,
    }
    for ln in block:
        if not out["model_revision"]:
            rm = rev_pat.search(ln)
            if rm:
                out["model_revision"] = rm.group(1)
        if out["challenge"] is None and "Challenge:" in ln:
            out["challenge"] = ln.split("Challenge:", 1)[1].strip()
        if out["kl"] is None and "| KL " in ln:
            km = kl_pat.search(ln)
            if km:
                out["kl"] = float(km.group(1))
                out["next_kl"] = float(km.group(2))
        if out["gate"] is None and "Gate " in ln:
            gm = gate_pat.search(ln)
            if gm:
                out["gate"] = gm.group(1)
                out["cur_kl"] = float(gm.group(2))
                out["req_kl"] = float(gm.group(3))
                out["prev_kl"] = float(gm.group(4))
    return out


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


def run_training(train_cmd_template: str, env_extra: dict[str, str], cwd: Path) -> dict[str, Any]:
    if not train_cmd_template.strip():
        notify("[TRAIN] TRAIN_CMD is empty; skipping training.", telegram=False)
        return {"skipped": True}
    cmd = train_cmd_template.format(**env_extra)
    notify(f"[TRAIN] Running: {cmd}", telegram=False)
    code = run_streaming(
        cmd,
        cwd=cwd,
        env={**os.environ, **env_extra},
    )
    if code != 0:
        raise RuntimeError(f"Training command failed with exit code {code}")
    notify("[TRAIN] Training command completed.", telegram=False)
    return {
        "skipped": False,
        "command": cmd,
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


def upload_model(api: HfApi, source_dir: Path, repo_id: str, message: str) -> str:
    if not source_dir.exists():
        raise RuntimeError(f"UPLOAD_SOURCE_DIR not found: {source_dir}")
    notify(f"[UPLOAD] {source_dir} -> {repo_id}", telegram=False)
    api.upload_folder(
        repo_id=repo_id,
        repo_type="model",
        folder_path=str(source_dir),
        commit_message=message,
    )
    info = api.model_info(repo_id=repo_id)
    revision = getattr(info, "sha", None)
    if not revision:
        raise RuntimeError(f"Unable to read uploaded revision for {repo_id}")
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


def main() -> int:
    env_path = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else DEFAULT_ENV_PATH
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
        eval_rec = parse_latest_eval_for_uid(log_file, uid)
        eval_json.write_text(json.dumps(eval_rec, indent=2), encoding="utf-8")
        summary["latest_eval"] = eval_rec
        notify(f"[STEP {step}] done in {time.time()-t:.1f}s", telegram=False)

        t = step_log("Derive challenge indices from latest seeds")
        ch = derive_challenge_json(uid=uid, network=network, netuid=netuid, out_path=challenge_json)
        summary["challenge"] = {
            "validators": len(ch.get("validators", [])),
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
        }
        summary["training"] = {"enabled": train_enabled}
        summary["gate_check"] = {"enabled": gate_check_enabled and train_enabled}

        if train_enabled:
            if train_until_pass_enabled and gate_check_enabled:
                t = step_log(
                    f"Train-until-pass loop (max_rounds={train_until_pass_max_rounds}, "
                    f"required_improvement={gate_required_improvement})"
                )
                loop_rounds: list[dict[str, Any]] = []
                passed = False
                for ridx in range(1, max(1, train_until_pass_max_rounds) + 1):
                    notify(f"[LOOP] round {ridx}/{train_until_pass_max_rounds}: training", telegram=False)
                    train_result = run_training(train_cmd, env_extra=env_extra, cwd=work_dir)
                    report_json = Path(env_extra["TRAIN_REPORT_JSON"])
                    if not report_json.exists():
                        raise RuntimeError(
                            f"Training report not found after round {ridx}: {report_json}"
                        )
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
                        }
                    )
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
        register_revision = env_str("REGISTER_REVISION", "main")
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
            "track": track,
        }
        notify(f"[STEP {step}] done in {time.time()-t:.1f}s", telegram=False)

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


if __name__ == "__main__":
    raise SystemExit(main())
