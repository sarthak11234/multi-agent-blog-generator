from __future__ import annotations

import json
import os
from datetime import datetime
from typing import Dict, List


class LongTermMemory:
    """Writes memories to a JSON file for later retrieval."""

    def __init__(self, storage_path: str = "backend/memory/long_term_store.json"):
        self.storage_path = storage_path
        os.makedirs(os.path.dirname(storage_path), exist_ok=True)
        if not os.path.exists(storage_path):
            with open(storage_path, "w", encoding="utf-8") as fp:
                json.dump([], fp)

    def _load(self) -> List[Dict]:
        with open(self.storage_path, "r", encoding="utf-8") as fp:
            return json.load(fp)

    def _save(self, data: List[Dict]):
        with open(self.storage_path, "w", encoding="utf-8") as fp:
            json.dump(data, fp, indent=2)

    def add_memory(self, topic: str, content: str, metadata: Dict | None = None):
        data = self._load()
        data.append(
            {
                "topic": topic,
                "content": content,
                "metadata": metadata or {},
                "timestamp": datetime.utcnow().isoformat(),
            }
        )
        self._save(data[-200:])  # keep latest 200 entries

    def retrieve(self, topic: str) -> str:
        topic_lower = topic.lower()
        relevant = [
            item["content"]
            for item in self._load()
            if topic_lower in item["topic"].lower()
            or topic_lower in item["content"].lower()
        ]
        return "\n---\n".join(relevant[-3:]) if relevant else ""

    def dump(self) -> List[Dict]:
        return self._load()

