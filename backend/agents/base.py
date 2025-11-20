from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict, Optional

from models.llm_base import LLM


class BaseAgent(ABC):
    """Lightweight interface implemented by all agents."""

    def __init__(self, name: str, llm: Optional[LLM]):
        self.name = name
        self.llm = llm

    @abstractmethod
    def run(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        raise NotImplementedError

