#!/usr/bin/env bash
# Start full_auto_uid_bot under PM2 with the EvolAI venv (required for KL + bittensor).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PY="${EVOLAI_PYTHON:-/root/sn47/evolai/.venv/bin/python}"
BOT="${ROOT}/full_auto_uid_bot.py"

pm2 delete sn47-miner 2>/dev/null || true
# ecosystem.config.cjs pins EvolAI venv; avoids bash -c python (system python, no transformers).
pm2 start "$ROOT/ecosystem.config.cjs"
pm2 save 2>/dev/null || true
echo "Started sn47-miner with $PY"
pm2 status sn47-miner
