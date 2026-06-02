#!/usr/bin/env bash
# ─────────────────────────────────────────────────────────────────────────────
# sn-47-agent — vLLM environment setup (validator-matching KL eval)
# ─────────────────────────────────────────────────────────────────────────────
#
# Creates an isolated vLLM virtualenv used only for the ref-model server
# (Qwen/Qwen3.5-9B) during local gate-check KL evaluation.
#
# Keep this separate from the EvolAI main env: vLLM pins fastapi/setuptools
# versions that conflict with bittensor.
#
# Usage:
#   bash /var/www/sn-47-agent/phoenix/scripts/setup-vllm.sh
#   VLLM_VENV=/var/www/evolai/vllm_env bash scripts/setup-vllm.sh
#   EVOLAI_PYTHON_VERSION=3.11 bash scripts/setup-vllm.sh
#
# After setup, .env is updated with VLLM_EXECUTABLE and KL eval vLLM settings.
# ─────────────────────────────────────────────────────────────────────────────

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AGENT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
ENV_FILE="${ENV_FILE:-$AGENT_DIR/.env}"
VLLM_VENV="${VLLM_VENV:-$AGENT_DIR/vllm_env}"
EVOLAI_PYTHON_VERSION="${EVOLAI_PYTHON_VERSION:-3.11}"

BOLD="\033[1m"
GREEN="\033[32m"
CYAN="\033[36m"
YELLOW="\033[33m"
RESET="\033[0m"

info()  { echo -e "${CYAN}▸${RESET} $*"; }
ok()    { echo -e "${GREEN}✓${RESET} $*"; }
warn()  { echo -e "${YELLOW}⚠${RESET} $*"; }
header(){ echo -e "\n${BOLD}$*${RESET}"; }

upsert_env() {
    local key="$1"
    local value="$2"
    local tmp
    tmp="$(mktemp)"
    if [ -f "$ENV_FILE" ]; then
        grep -v "^${key}=" "$ENV_FILE" > "$tmp" || true
    fi
    printf '%s=%s\n' "$key" "$value" >> "$tmp"
    mv "$tmp" "$ENV_FILE"
}

install_vllm_with_uv() {
    if [ ! -d "$VLLM_VENV" ]; then
        info "Creating virtualenv at $VLLM_VENV (Python $EVOLAI_PYTHON_VERSION)"
        uv venv "$VLLM_VENV" --python "$EVOLAI_PYTHON_VERSION"
    else
        info "Reusing existing virtualenv at $VLLM_VENV"
    fi
    info "Installing vllm (uv selects the matching CUDA wheel)..."
    uv pip install vllm --torch-backend auto \
        --python "$VLLM_VENV/bin/python" -q
}

install_vllm_with_pip() {
    if [ ! -d "$VLLM_VENV" ]; then
        info "Creating virtualenv at $VLLM_VENV"
        python3 -m venv "$VLLM_VENV"
    else
        info "Reusing existing virtualenv at $VLLM_VENV"
    fi
    info "Upgrading pip..."
    "$VLLM_VENV/bin/python" -m pip install --upgrade pip wheel -q
    info "Installing vllm (this may take several minutes)..."
    "$VLLM_VENV/bin/python" -m pip install vllm -q
}

header "sn-47-agent vLLM setup"

if ! command -v nvidia-smi &>/dev/null; then
    warn "nvidia-smi not found — vLLM install will proceed, but KL eval needs a CUDA GPU."
else
    ok "GPU detected: $(nvidia-smi --query-gpu=name,memory.total --format=csv,noheader | head -1)"
fi

header "Step 1/3 — Install vLLM virtualenv"
if command -v uv &>/dev/null; then
    ok "uv $(uv --version)"
    install_vllm_with_uv
else
    warn "uv not found — falling back to python -m venv + pip"
    warn "For faster installs, use: curl -LsSf https://astral.sh/uv/install.sh | sh"
    install_vllm_with_pip
fi

VLLM_BIN="$VLLM_VENV/bin/vllm"
if [ ! -x "$VLLM_BIN" ]; then
    echo "Expected vLLM binary not found at $VLLM_BIN" >&2
    exit 1
fi
ok "vLLM installed — $($VLLM_BIN --version 2>&1 || echo 'binary present')"

header "Step 2/3 — Write sn-47-agent .env"
if [ ! -f "$ENV_FILE" ]; then
    warn "$ENV_FILE missing — copying from .env.example"
    cp "$AGENT_DIR/.env.example" "$ENV_FILE"
fi

upsert_env "VLLM_EXECUTABLE" "$VLLM_BIN"
upsert_env "KL_EVAL_REF_MODE" "vllm"
upsert_env "KL_EVAL_START_VLLM_REF" "true"
upsert_env "VLLM_REF_URL" ""
upsert_env "VLLM_REF_PORT" "8002"
upsert_env "VLLM_REF_GPU_INDEX" "0"
upsert_env "VLLM_REF_GPU_MEMORY_UTILIZATION" "0.50"
upsert_env "VLLM_REF_MAX_MODEL_LEN" "4096"

ok "Updated $ENV_FILE"
ok "  VLLM_EXECUTABLE=$VLLM_BIN"
ok "  KL_EVAL_REF_MODE=vllm"
ok "  KL_EVAL_START_VLLM_REF=true"

header "Step 3/3 — Quick sanity check"
if "$VLLM_BIN" --help >/dev/null 2>&1; then
    ok "vLLM CLI responds"
else
    warn "vLLM CLI help failed — binary exists but may need CUDA drivers at runtime"
fi

if bash "$SCRIPT_DIR/check-vllm-ready.sh"; then
    ok "vLLM runtime preflight passed"
else
    warn "vLLM preflight failed — KL eval will use in-process ref (or fix CUDA: bash scripts/fix-cuda-path.sh)"
    upsert_env "KL_EVAL_REF_MODE" "inprocess"
    upsert_env "KL_EVAL_START_VLLM_REF" "false"
    ok "Set KL_EVAL_REF_MODE=inprocess until nvcc is available"
fi

header "Setup complete"
echo ""
echo -e "  ${BOLD}Layout:${RESET}"
echo -e "    Agent dir:  $AGENT_DIR"
echo -e "    vLLM venv:  $VLLM_VENV"
echo -e "    vLLM bin:   $VLLM_BIN"
echo -e "    Config:     $ENV_FILE"
echo ""
echo -e "  ${BOLD}Next:${RESET}"
echo -e "    1. Ensure HF_TOKEN is set in .env (ref model download)"
echo -e "    2. Run full_auto pipeline — KL eval starts ref vLLM on port 8002 automatically"
echo -e "    3. Optional manual test:"
echo -e "       ${CYAN}/var/www/evolai/.venv/bin/python $AGENT_DIR/validator_kl_eval.py \\${RESET}"
echo -e "       ${CYAN}  --model-dir \$AUTO_MODEL_DIR --prep-out-dir \$AUTO_PREPARE_OUT_DIR \\${RESET}"
echo -e "       ${CYAN}  --out-json $AGENT_DIR/kl_eval_test.json --device cuda --start-vllm-ref${RESET}"
echo ""
