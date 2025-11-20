from __future__ import annotations

from typing import Any, Dict

from agents.base import BaseAgent


class WriterAgent(BaseAgent):
    """Turns research notes into a long-form draft."""

    def __init__(self, llm):
        super().__init__("writer", llm)

    def run(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        topic: str = payload.get("topic", "")
        research_summary: str = payload.get("research_summary", "")
        goal: str = payload.get("goal", "")

        prompt = (
            "You are a senior content strategist.\n"
            "Write a structured blog article with introduction, 3-5 sections, and a "
            "clear conclusion. Embed data or citations from the research summary.\n\n"
            f"Topic: {topic}\n"
            f"Goal: {goal}\n"
            "Research Summary:\n"
            f"{research_summary}\n"
        )

        draft = self.llm.generate(prompt, max_tokens=700)
        return {"draft": draft}
