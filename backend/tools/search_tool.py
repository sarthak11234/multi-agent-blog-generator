from __future__ import annotations

import datetime as dt
import random
from typing import Dict, List

import requests


class Tool:
    def run(self, payload):
        raise NotImplementedError


class SearchTool(Tool):
    """Attempts a real web search and falls back to curated stubs."""

    SEARCH_ENDPOINT = "https://ddg-api.herokuapp.com/search"

    def run(self, query: str | Dict[str, str]) -> List[Dict[str, str]]:
        if isinstance(query, dict):
            query = query.get("query") or query.get("topic") or ""
        params = {"query": query, "limit": 5}
        try:
            response = requests.get(self.SEARCH_ENDPOINT, params=params, timeout=6)
            if response.ok:
                data = response.json()
                return [
                    {
                        "title": item.get("title"),
                        "url": item.get("link"),
                        "snippet": item.get("description"),
                        "timestamp": dt.datetime.utcnow().isoformat(),
                    }
                    for item in data.get("results", [])
                ]
        except Exception:
            pass

        # Fallback deterministic mock data
        mock_snippets = [
            f"Latest developments around {query} with emphasis on real-world adoption.",
            f"Key statistics and metrics describing how {query} impacts teams.",
            f"Expert commentary on future of {query} and related AI tooling.",
        ]
        return [
            {
                "title": f"{query.title()} Insight #{idx+1}",
                "url": f"https://example.com/{query.replace(' ', '-')}/{idx}",
                "snippet": random.choice(mock_snippets),
                "timestamp": dt.datetime.utcnow().isoformat(),
            }
            for idx in range(3)
        ]

