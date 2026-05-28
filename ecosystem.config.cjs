/** PM2 config — do not use `bash -c python full_auto_uid_bot.py` (wrong interpreter). */
module.exports = {
  apps: [
    {
      name: "sn47-miner",
      cwd: "/root/sn47/sn-47-agent",
      script: "/root/sn47/evolai/.venv/bin/python",
      args: "/root/sn47/sn-47-agent/full_auto_uid_bot.py",
      interpreter: "none",
      autorestart: true,
      max_restarts: 10,
      min_uptime: "30s",
    },
  ],
};
