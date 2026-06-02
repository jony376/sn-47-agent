/**
 * PM2 config for sn47-miner.
 * IMPORTANT: run with the EvolAI venv python directly (NOT `bash -c python3 ...`).
 * The system `python3` lacks deps like huggingface_hub and silently crash-loops.
 */
module.exports = {
  apps: [
    {
      name: "sn47-miner",
      cwd: "/root/sn47/sn47-agent",
      script: "/root/sn47/evolai/.venv/bin/python",
      args: "hf_model_ops_bot.py",
      interpreter: "none",
      autorestart: true,
      max_restarts: 10,
      min_uptime: "30s",
    },
  ],
};
