from __future__ import annotations

from typing import Any, Dict, List

from agents.base import BaseAgent
from tools.search_tool import SearchTool


class ResearcherAgent(BaseAgent):
    """Queries the search tool and summarises the findings."""

    def __init__(self, llm, search_tool: SearchTool):
        super().__init__("researcher", llm)
        self.search_tool = search_tool

    def run(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        topic: str = payload.get("topic", "")
        goal: str = payload.get("goal", "")
        memory: str = payload.get("memory", "")

        results: List[Dict[str, str]] = self.search_tool.run(topic)

        prompt = (
            "You are a diligent research assistant.\n"
            f"Topic: {topic}\n"
            f"Goal: {goal}\n"
            f"Relevant memory: {memory}\n"
            "Use the following search snippets to produce a concise research summary "
            "with bullet points and cite the sources inline as [S#].\n\n"
        )

        for idx, result in enumerate(results, start=1):
            snippet = result.get("snippet") or result.get("content") or ""
            prompt += f"[S{idx}] {result.get('title','Untitled')}: {snippet}\n"

        summary = self.llm.generate(prompt, max_tokens=400)
        return {"summary": summary, "sources": results}
