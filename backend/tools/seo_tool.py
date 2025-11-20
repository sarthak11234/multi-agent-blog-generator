from __future__ import annotations

import math
import re
from collections import Counter
from typing import Dict


class Tool:
    def run(self, payload):
        raise NotImplementedError


class SEOTool(Tool):
    """Basic keyword density and readability helper."""

    def run(self, payload: Dict[str, str]) -> Dict[str, str | float | Dict]:
        topic = payload.get("topic", "")
        content = payload.get("content", "")
        tokens = re.findall(r"[a-zA-Z]+", content.lower())
        total_words = len(tokens) or 1

        topic_tokens = re.findall(r"[a-zA-Z]+", topic.lower())
        topic_counts = sum(tokens.count(tok) for tok in topic_tokens)
        density = round((topic_counts / total_words) * 100, 2)

        headings = len(re.findall(r"^#+\s", content, flags=re.MULTILINE))
        paragraphs = len([p for p in content.split("\n\n") if p.strip()])

        suggestions = []
        if density < 1.5:
            suggestions.append("Increase usage of the primary keyword naturally.")
        if headings < 3:
            suggestions.append("Add more descriptive headings (H2/H3) to break sections.")
        if paragraphs < 4:
            suggestions.append("Include more paragraphs for scannability.")
        if len(content) < 600:
            suggestions.append("Content is short; expand with detailed insights.")

        return {
            "keyword_density": density,
            "headings": headings,
            "paragraphs": paragraphs,
            "suggestions": "\n".join(f"- {s}" for s in suggestions) or "Looks good!",
        }

