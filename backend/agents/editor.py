from __future__ import annotations

from typing import Any, Dict

from agents.base import BaseAgent
from tools.seo_tool import SEOTool


class EditorAgent(BaseAgent):
    """Polishes the draft, enforces style, and applies SEO recommendations."""

    def __init__(self, llm, seo_tool: SEOTool):
        super().__init__("editor", llm)
        self.seo_tool = seo_tool

    def run(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        draft: str = payload.get("draft", "")
        topic: str = payload.get("topic", "")
        intent: str = payload.get("goal", "")

        seo_report = self.seo_tool.run({"topic": topic, "content": draft})

        prompt = (
            "You are an experienced editor tasked with producing a publication-ready "
            "article. Improve clarity, flow, and voice while respecting SEO feedback. "
            "Incorporate a short meta description and key takeaways bullets.\n"
            f"Topic: {topic}\n"
            f"Intent: {intent}\n"
            f"SEO Suggestions:\n{seo_report['suggestions']}\n\n"
            "Draft to edit:\n"
            f"{draft}\n"
        )

        final_content = self.llm.generate(prompt, max_tokens=600)
        return {"final_content": final_content, "seo_report": seo_report}
