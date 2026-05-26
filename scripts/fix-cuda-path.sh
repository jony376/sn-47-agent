#!/usr/bin/env bash
# Discover nvcc and write CUDA_HOME into sn-47-agent .env (RunPod / minimal CUDA images).
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AGENT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
ENV_FILE="${ENV_FILE:-$AGENT_DIR/.env}"

discover_cuda_home() {
    if [ -n "${CUDA_HOME:-}" ] && [ -x "${CUDA_HOME}/bin/nvcc" ]; then
        echo "$CUDA_HOME"
        return 0
    fi
    if command -v nvcc &>/dev/null; then
        dirname "$(dirname "$(command -v nvcc)")"
        return 0
    fi
    for d in /usr/local/cuda /usr/local/cuda-12.8 /usr/local/cuda-12.6 /usr/local/cuda-12.4 /opt/cuda; do
        if [ -x "$d/bin/nvcc" ]; then
            echo "$d"
            return 0
        fi
    done
    return 1
}

if ! HOME_FOUND="$(discover_cuda_home)"; then
    echo "Could not find nvcc. Install CUDA devel toolkit or use a -devel GPU image." >&2
    echo "Fallback: set KL_EVAL_REF_MODE=inprocess in $ENV_FILE" >&2
    exit 1
fi

echo "Found CUDA toolkit at: $HOME_FOUND"
export CUDA_HOME="$HOME_FOUND"
export PATH="$CUDA_HOME/bin:$PATH"
nvcc --version | head -3

upsert_env() {
    local key="$1" value="$2" tmp
    tmp="$(mktemp)"
    if [ -f "$ENV_FILE" ]; then
        grep -v "^${key}=" "$ENV_FILE" > "$tmp" || true
    fi
    printf '%s=%s\n' "$key" "$value" >> "$tmp"
    mv "$tmp" "$ENV_FILE"
}

if [ -f "$ENV_FILE" ]; then
    upsert_env "CUDA_HOME" "$HOME_FOUND"
    echo "Updated $ENV_FILE with CUDA_HOME=$HOME_FOUND"
else
    echo "No $ENV_FILE — export in your shell:"
    echo "  export CUDA_HOME=$HOME_FOUND"
    echo "  export PATH=\$CUDA_HOME/bin:\$PATH"
fi

if [ ! -e /usr/local/cuda ] && [ "$HOME_FOUND" != "/usr/local/cuda" ]; then
    echo "Optional symlink (requires root): ln -sf $HOME_FOUND /usr/local/cuda"
fi
