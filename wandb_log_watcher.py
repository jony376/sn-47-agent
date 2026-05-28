#!/usr/bin/env python3
"""Fetch validator console logs from public W&B runs (no API key required)."""
from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any
from urllib import request
from urllib.parse import urlparse

from eval_log_parser import parse_latest_eval_for_uid

WANDB_GRAPHQL_URL = "https://api.wandb.ai/graphql"


def parse_wandb_run_url(url: str) -> tuple[str, str, str]:
    """Parse https://wandb.ai/{entity}/{project}/runs/{run_id}/..."""
    parsed = urlparse(url.strip())
    parts = [p for p in parsed.path.split("/") if p]
    if len(parts) < 4 or parts[2] != "runs":
        raise ValueError(f"Invalid W&B run URL: {url}")
    return parts[0], parts[1], parts[3]


def resolve_wandb_run_path(
    *,
    run_url: str = "",
    run_path: str = "",
    entity: str = "",
    project: str = "",
    run_id: str = "",
) -> tuple[str, str, str]:
    if run_url:
        return parse_wandb_run_url(run_url)
    if run_path:
        parts = run_path.strip().strip("/").split("/")
        if len(parts) != 3:
            raise ValueError(f"Invalid WANDB_RUN_PATH: {run_path}")
        return parts[0], parts[1], parts[2]
    if entity and project and run_id:
        return entity.strip(), project.strip(), run_id.strip()
    raise ValueError(
        "Set WANDB_RUN_URL or WANDB_RUN_PATH or (WANDB_ENTITY + WANDB_PROJECT + WANDB_RUN_ID)"
    )


def fetch_public_log_lines(
    entity: str,
    project: str,
    run_id: str,
    *,
    tail_lines: int = 8000,
    timeout_s: float = 60.0,
) -> tuple[list[str], int]:
    """Read console log lines from a public W&B run via the public GraphQL API."""
    query = """
    query FetchLogTail($entity: String!, $project: String!, $run: String!, $last: Int!) {
      project(name: $project, entityName: $entity) {
        run(name: $run) {
          logLineCount
          logLines(last: $last) {
            edges {
              node {
                line
              }
            }
          }
        }
      }
    }
    """
    payload = json.dumps(
        {
            "query": query,
            "variables": {
                "entity": entity,
                "project": project,
                "run": run_id,
                "last": int(tail_lines),
            },
        }
    ).encode("utf-8")
    req = request.Request(
        WANDB_GRAPHQL_URL,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with request.urlopen(req, timeout=timeout_s) as resp:
        body = json.loads(resp.read().decode("utf-8"))

    if body.get("errors"):
        raise RuntimeError(f"W&B GraphQL error: {body['errors']}")

    run = body["data"]["project"]["run"]
    total = int(run.get("logLineCount") or 0)
    edges = run["logLines"]["edges"]
    lines = [edge["node"]["line"] for edge in edges]
    return lines, total


class WandbLogTailer:
    """Poll public W&B validator logs and parse miner eval blocks."""

    def __init__(
        self,
        entity: str,
        project: str,
        run_id: str,
        *,
        tail_lines: int = 8000,
        cache_dir: Path | None = None,
        fetch_mode: str = "public_graphql",
        api_key: str = "",
    ) -> None:
        self.entity = entity
        self.project = project
        self.run_id = run_id
        self.run_path = f"{entity}/{project}/{run_id}"
        self.tail_lines = max(500, int(tail_lines))
        self.cache_dir = cache_dir or Path("/tmp/sn47_wandb_logs")
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.fetch_mode = (fetch_mode or "public_graphql").strip().lower()
        self.api_key = (api_key or "").strip()
        self._lines: list[str] = []
        self._total_line_count = 0

    @classmethod
    def from_env(cls, cache_dir: Path | None = None) -> "WandbLogTailer":
        entity, project, run_id = resolve_wandb_run_path(
            run_url=os.getenv("WANDB_RUN_URL", ""),
            run_path=os.getenv("WANDB_RUN_PATH", ""),
            entity=os.getenv("WANDB_ENTITY", "open-evolai"),
            project=os.getenv("WANDB_PROJECT", "evol-validator"),
            run_id=os.getenv("WANDB_RUN_ID", ""),
        )
        tail_lines = int(os.getenv("WANDB_LOG_TAIL_LINES", "8000"))
        fetch_mode = os.getenv("WANDB_FETCH_MODE", "auto").strip().lower()
        api_key = os.getenv("WANDB_API_KEY", "").strip()
        if fetch_mode == "auto":
            fetch_mode = "api" if api_key else "public_graphql"
        return cls(
            entity,
            project,
            run_id,
            tail_lines=tail_lines,
            cache_dir=cache_dir,
            fetch_mode=fetch_mode,
            api_key=api_key,
        )

    def refresh(self) -> int:
        if self.fetch_mode == "api":
            self._refresh_via_api()
        elif self.fetch_mode == "public_graphql":
            self._lines, self._total_line_count = fetch_public_log_lines(
                self.entity,
                self.project,
                self.run_id,
                tail_lines=self.tail_lines,
            )
        else:
            raise ValueError(
                f"Unknown WANDB_FETCH_MODE={self.fetch_mode!r}; use auto, public_graphql, or api"
            )
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        cache_file = self.cache_dir / f"{self.run_id}_tail.log"
        cache_file.write_text("\n".join(self._lines) + "\n", encoding="utf-8")
        return len(self._lines)

    def _refresh_via_api(self) -> None:
        import wandb

        api = wandb.Api(api_key=self.api_key) if self.api_key else wandb.Api()
        run = api.run(self.run_path)
        log_filename = os.getenv("WANDB_LOG_FILENAME", "output.log").strip() or "output.log"
        remote = run.file(log_filename)
        remote.download(replace=True, root=str(self.cache_dir))
        downloaded = self.cache_dir / log_filename
        if not downloaded.exists():
            raise RuntimeError(
                f"W&B log file {log_filename!r} not found after download for run {self.run_path}"
            )
        self._lines = downloaded.read_text(encoding="utf-8", errors="replace").splitlines()
        self._total_line_count = len(self._lines)

    @property
    def lines(self) -> list[str]:
        return self._lines

    @property
    def total_line_count(self) -> int:
        return self._total_line_count

    def latest_eval_for_uid(self, uid: int) -> dict[str, Any]:
        if not self._lines:
            self.refresh()
        rec = parse_latest_eval_for_uid(self._lines, uid)
        rec["log_source"] = "wandb_public" if self.fetch_mode == "public_graphql" else "wandb"
        rec["wandb_run_path"] = self.run_path
        rec["wandb_fetch_mode"] = self.fetch_mode
        rec["wandb_total_log_lines"] = self._total_line_count
        rec["wandb_tail_lines"] = len(self._lines)
        return rec

    def append_to_local_log(self, dest: Path) -> None:
        if not self._lines:
            return
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text("\n".join(self._lines) + "\n", encoding="utf-8")
