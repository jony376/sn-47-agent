# sn-47-agent HF model bot

Downloads a Hugging Face model, uploads to an auto-incremented model name, then registers it through EvolAI CLI.

## 1) Configure

```bash
cd /root/sn47/sn-47-agent
cp .env.example .env
```

Fill `.env` values:
- `HF_TOKEN`
- `DOWNLOAD_USERNAME`, `DOWNLOAD_MODEL_NAME`
- `UPLOAD_USERNAME`, `UPLOAD_MODEL_NAME` (existing model repo)
- `REGISTER_WALLET_NAME`, `REGISTER_HOTKEY`, `REGISTER_NETUID`
- `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID`

Upload commits into your existing model repo:
- `<UPLOAD_USERNAME>/<UPLOAD_MODEL_NAME>`

## 2) Run

```bash
/root/sn47/evolai/.venv/bin/python /root/sn47/sn-47-agent/hf_model_ops_bot.py
```

Or pass custom env file path:

```bash
/root/sn47/evolai/.venv/bin/python /root/sn47/sn-47-agent/hf_model_ops_bot.py /path/to/custom.env
```

## Notes

- Script sends Telegram updates for start/finish/failure.
- Script gets uploaded model revision SHA automatically and uses it for:

```bash
python -m evolai.cli.main miner register <repo_id> --revision <sha> ...
```

- **Do not register `main`.** Validators lock revisions at the start of each
  loop (~300s). Register the immutable upload SHA so the next lock picks up
  your new model exactly once.

## Full auto UID pipeline

See `full_auto_uid_bot.py` for train → upload → register with lock-window checks.

### Real-time logs from W&B (no API key)

The W&B web UI is a React app — **HTML scraping does not work**. For public runs like
[open-evolai/evol-validator](https://wandb.ai/open-evolai/evol-validator/runs/ya596ynd/logs),
the bot uses W&B's **public GraphQL API** (same data as the Logs tab, no `WANDB_API_KEY`):

```bash
LOG_SOURCE=wandb
WANDB_FETCH_MODE=auto          # public_graphql when no API key
WANDB_RUN_URL=https://wandb.ai/open-evolai/evol-validator/runs/ya596ynd/logs
AUTO_WATCH_MODE=true
AUTO_WATCH_POLL_SECONDS=15
```

Optional: set `WANDB_API_KEY` only if you switch to a private run (`WANDB_FETCH_MODE=api`).

### GPU

Training and KL eval use CUDA (KL eval runs via EvolAI venv Python):

```bash
TRAIN_CMD=... --device cuda ...
KL_EVAL_DEVICE=cuda
KL_EVAL_REF_MODE=auto          # vLLM MC-KL when ref server available
KL_EVAL_MAX_LENGTH=8192        # match validator SIDE_QUEST_MAX_CTX
KL_EVAL_KL_MAX_NEW_TOKENS=512  # match EVAL_KL_MAX_NEW_TOKENS_TRANSFORMER
```

Gate prediction uses `validator_kl_eval.py`, which calls the same
`evaluate_with_side_quests` KL path as on-chain validators (Qwen chat template,
ref-generated tokens, not teacher-forced CE).

### vLLM (recommended — matches validator MC-KL exactly)

Install the isolated vLLM environment once:

```bash
bash /root/sn47/sn-47-agent/scripts/setup-vllm.sh
```

This creates `sn-47-agent/vllm_env`, installs vLLM, and writes these into `.env`:

```bash
VLLM_EXECUTABLE=/root/sn47/sn-47-agent/vllm_env/bin/vllm
KL_EVAL_REF_MODE=vllm
KL_EVAL_START_VLLM_REF=true
VLLM_REF_PORT=8002
VLLM_REF_GPU_INDEX=0
```

To reuse EvolAI's validator vLLM env instead:

```bash
VLLM_VENV=/root/sn47/evolai/vllm_env bash /root/sn47/sn-47-agent/scripts/setup-vllm.sh
```

If a ref server is already running, point at it and skip auto-start:

```bash
VLLM_REF_URL=http://127.0.0.1:8002/v1
KL_EVAL_START_VLLM_REF=false
```

Critical `.env` settings (see `.env.example` for full list):

```bash
REGISTER_REVISION=auto
AUTO_WATCH_MODE=true              # default: trigger on new completed eval only
AUTO_WATCH_POLL_SECONDS=15
VALIDATOR_EVAL_INTERVAL_S=300
LOCK_RISK_BUDGET_FRACTION=0.40    # finish pipeline within ~120s
AUTO_ABORT_ON_HIGH_LOCK_RISK=true
AUTO_ABORT_ON_MEDIUM_LOCK_RISK=true
AUTO_FAST_TRAIN_ON_LOCK_RISK=true
FAST_TRAIN_CMD=...                # shorter super_light run when time is tight
```

Lock-window flow (log-driven timing, `LOCK_TIMING_MODE=dynamic`):

1. Watch detects your UID eval finished (`Gate PASS`/`FAIL` in log).
2. Pipeline parses W&B logs for `Locked transformer revisions` and your `[slot/total] UID` position.
3. Estimates seconds until the **next lock** (typically ~11 min at slot 30/50, ~3 min at 48/50).
4. Budget and abort thresholds use that estimate — not a fixed 300s interval.
5. Pre-upload re-fetches logs and re-checks remaining time.
6. Registers uploaded SHA (never `main`).

Known failure modes the bot guards against:

| Failure | Cause | Mitigation |
|---------|-------|------------|
| `Improve same SHA` | Register `main` or upload after validator lock | `REGISTER_REVISION=auto` + watch mode |
| `Improve FAIL` | Same model re-evaluated twice | Budget + pre-upload abort |
| Stale manual run | Old eval log | Abort on medium/high lock risk |
| Duplicate pipeline | Same eval re-triggered | Watch trigger key + `AUTO_SKIP_DUPLICATE_EVAL` |

## Watch mode (auto detect source new commit)

Set in `.env`:

```bash
WATCH_MODE=true
WATCH_POLL_SECONDS=60
RUN_DOWNLOAD=true
RUN_UPLOAD=true
RUN_REGISTER=true
```

Behavior:
- Checks `DOWNLOAD_USERNAME/DOWNLOAD_MODEL_NAME` head commit SHA
- If SHA changed, automatically runs download -> upload -> register
- Stores last processed SHA in `STATE_FILE_PATH` to avoid duplicate runs

## PM2 example

```bash
pm2 start /root/sn47/evolai/.venv/bin/python --name hf-model-ops -- /root/sn47/sn-47-agent/hf_model_ops_bot.py
pm2 logs hf-model-ops
```
