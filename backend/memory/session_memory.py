from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class SessionEntry:
    role: str
    content: str


@dataclass
class SessionRecord:
    topic: str
    goal: str
    messages: List[SessionEntry] = field(default_factory=list)


class SessionMemory:
    """Ephemeral per-run memory store."""

    def __init__(self):
        self.sessions: Dict[str, SessionRecord] = {}

    def start_session(self, run_id: str, topic: str, goal: str):
        self.sessions.setdefault(run_id, SessionRecord(topic=topic, goal=goal))

    def append(self, run_id: str, role: str, content: str):
        if run_id not in self.sessions:
            return
        self.sessions[run_id].messages.append(SessionEntry(role=role, content=content))

    def get_context(self, run_id: str) -> str:
        record = self.sessions.get(run_id)
        if not record:
            return ""
        formatted = [f"{entry.role.upper()}: {entry.content[:500]}" for entry in record.messages[-5:]]
        return "\n".join(formatted)

    def dump(self) -> Dict[str, Dict]:
        return {
            run_id: {
                "topic": record.topic,
                "goal": record.goal,
                "messages": [
                    {"role": entry.role, "content": entry.content}
                    for entry in record.messages
                ],
            }
            for run_id, record in self.sessions.items()
        }

