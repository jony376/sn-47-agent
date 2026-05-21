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
- `UPLOAD_USERNAME`
- `REGISTER_WALLET_NAME`, `REGISTER_HOTKEY`, `REGISTER_NETUID`
- `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID`

Upload target name is auto-generated as:
- `evolai-transformer-1`
- `evolai-transformer-2`
- ...

based on existing models under `UPLOAD_USERNAME`.

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
