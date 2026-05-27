#!/usr/bin/env bash
# Quick preflight for validator-matching KL eval with vLLM ref server.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AGENT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
ENV_FILE="${ENV_FILE:-$AGENT_DIR/.env}"

read_env() {
    local key="$1" default="${2:-}"
    if [ -f "$ENV_FILE" ]; then
        local line
        line="$(grep -E "^${key}=" "$ENV_FILE" 2>/dev/null | tail -1 || true)"
        if [ -n "$line" ]; then
            echo "${line#*=}"
            return 0
        fi
    fi
    echo "$default"
}

VLLM_BIN="$(read_env VLLM_EXECUTABLE "$AGENT_DIR/vllm_env/bin/vllm")"
HF_TOKEN_VAL="$(read_env HF_TOKEN "")"
HF_TOKEN_VAL="${HF_TOKEN_VAL:-$(read_env HUGGINGFACE_HUB_TOKEN "")}"
CUDA_HOME_ENV="$(read_env CUDA_HOME "")"
[ -n "$CUDA_HOME_ENV" ] && export CUDA_HOME="$CUDA_HOME_ENV"
ok=0
warn=0

pass() { echo "  OK   $*"; ok=$((ok + 1)); }
fail() { echo "  FAIL $*"; warn=$((warn + 1)); }
note() { echo "  --   $*"; }

echo "sn-47-agent vLLM / CUDA preflight"
echo ""

if command -v nvidia-smi &>/dev/null; then
    pass "GPU: $(nvidia-smi --query-gpu=name,memory.total --format=csv,noheader | head -1)"
else
    fail "nvidia-smi not found"
fi

if [ -x "$VLLM_BIN" ]; then
    pass "vLLM binary: $VLLM_BIN"
else
    fail "vLLM binary missing: $VLLM_BIN (run scripts/setup-vllm.sh)"
fi

discover_nvcc() {
    if [ -n "${CUDA_HOME:-}" ] && [ -x "${CUDA_HOME}/bin/nvcc" ]; then
        echo "${CUDA_HOME}/bin/nvcc"
        return 0
    fi
    if command -v nvcc &>/dev/null; then
        command -v nvcc
        return 0
    fi
    for d in /usr/local/cuda /usr/local/cuda-12.8 /usr/local/cuda-12.6 /usr/local/cuda-12.4 /opt/cuda; do
        if [ -x "$d/bin/nvcc" ]; then
            echo "$d/bin/nvcc"
            return 0
        fi
    done
    return 1
}

if command -v ninja &>/dev/null; then
    pass "ninja: $(command -v ninja) ($(ninja --version 2>/dev/null || echo '?'))"
else
    fail "ninja not found — flashinfer JIT needs: apt-get install -y ninja-build"
fi

if NVCC_PATH="$(discover_nvcc)"; then
    CUDA_HOME_FOUND="$(dirname "$(dirname "$NVCC_PATH")")"
    pass "nvcc: $NVCC_PATH (CUDA_HOME=$CUDA_HOME_FOUND)"
    note "Add to .env if vLLM still fails: CUDA_HOME=$CUDA_HOME_FOUND"
else
    fail "nvcc not found — vLLM 0.21 flashinfer will JIT-compile and crash without CUDA toolkit"
    note "RunPod: use PyTorch template with -devel (cuda12.8-devel), or:"
    note "  export CUDA_HOME=/usr/local/cuda-12.8"
    note "  export PATH=\$CUDA_HOME/bin:\$PATH"
    note "Or skip vLLM (in-process KL still matches validator scale ~2.x):"
    note "  KL_EVAL_REF_MODE=inprocess"
    note "  KL_EVAL_START_VLLM_REF=false"
fi

if [ -n "$HF_TOKEN_VAL" ]; then
    pass "HF token set"
else
    fail "HF_TOKEN not set (ref model download)"
fi

echo ""
if [ "$warn" -eq 0 ]; then
    echo "Ready for vLLM ref server (KL_EVAL_REF_MODE=vllm)."
    exit 0
fi
echo "$warn check(s) failed — use in-process KL or fix CUDA before vLLM."
exit 1
