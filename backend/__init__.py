"""Backend package for the AI Capstone Multi-Agent System.

This package contains:
- agents: Coordinator, Researcher, Writer, Editor agents
- models: LLM implementations (Transformers, GGUF, HuggingFace API)
- tools: Search and SEO analysis tools
- memory: Session and long-term memory management
- services: Logging and evaluation services
"""

__version__ = "1.0.0"
__author__ = "AI Capstone Project"

# Package-level imports for convenience
from backend.models.llm_base import LLM, LLMConfig, create_llm
from backend.agents.coordinator import CoordinatorAgent
from backend.agents.researcher import ResearcherAgent
from backend.agents.writer import WriterAgent
from backend.agents.editor import EditorAgent

__all__ = [
    "__version__",
    "LLM",
    "LLMConfig",
    "create_llm",
    "CoordinatorAgent",
    "ResearcherAgent",
    "WriterAgent",
    "EditorAgent",
]
