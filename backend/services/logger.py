from __future__ import annotations

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

from backend.models.llm_base import estimate_tokens


class RunLogger:
    """Simple JSONL logger to trace every agent output."""

    def __init__(self, log_dir: str = "backend/logs"):
        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(parents=True, exist_ok=True)
        self.aggregate_file = self.log_dir / "latest.log"

    def log(
        self,
        agent: str,
        run_id: str,
        content: str,
        extra: Optional[Dict] = None,
    ):
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "agent": agent,
            "run_id": run_id,
            "content_preview": content[:400],
            "estimated_tokens": estimate_tokens(content),
            "extra": extra or {},
        }
        per_run_file = self.log_dir / f"{run_id}.jsonl"
        with per_run_file.open("a", encoding="utf-8") as fp:
            fp.write(json.dumps(entry) + "\n")
        with self.aggregate_file.open("a", encoding="utf-8") as fp:
            fp.write(json.dumps(entry) + "\n")

    def recent(self, limit: int = 50) -> List[Dict]:
        if not self.aggregate_file.exists():
            return []
        with self.aggregate_file.open("r", encoding="utf-8") as fp:
            lines = fp.readlines()[-limit:]
        return [json.loads(line) for line in lines]

