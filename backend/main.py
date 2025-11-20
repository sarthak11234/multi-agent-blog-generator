from __future__ import annotations

import asyncio
import logging
import os
from pathlib import Path
from typing import Any, Dict

# Set up logging FIRST
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# CRITICAL: Set LLM_MODE before loading .env to prevent override
os.environ["LLM_MODE"] = "hf_api"

# Load .env file if it exists - must be done BEFORE importing other modules
try:
    from dotenv import load_dotenv
    # Try multiple paths for .env file
    env_paths = [
        Path(__file__).parent / ".env",  # backend/.env
        Path(__file__).parent.parent / "backend" / ".env",  # project_root/backend/.env
    ]
    loaded = False
    for env_path in env_paths:
        if env_path.exists():
            load_dotenv(env_path, override=True)
            logger.info(f"Loaded environment variables from {env_path}")
            loaded = True
            break
    if not loaded:
        logger.warning("No .env file found in expected locations")
    
    # Also check if token is set
    if os.getenv("HF_API_TOKEN"):
        token_preview = os.getenv("HF_API_TOKEN")[:10] + "..." if len(os.getenv("HF_API_TOKEN", "")) > 10 else "***"
        logger.info(f"HF_API_TOKEN found in environment: {token_preview}")
    else:
        logger.warning("HF_API_TOKEN not found in environment")
except ImportError:
    logger.warning("python-dotenv not installed, .env file won't be loaded")
except Exception as e:
    logger.error(f"Error loading .env file: {e}", exc_info=True)

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from agents.coordinator import CoordinatorAgent
from agents.editor import EditorAgent
from agents.researcher import ResearcherAgent
from agents.writer import WriterAgent
from memory.long_term_memory import LongTermMemory
from memory.session_memory import SessionMemory
from models.llm_base import LLMConfig, create_llm
from services.evaluator import ContentEvaluator
from services.logger import RunLogger
from tools.search_tool import SearchTool
from tools.seo_tool import SEOTool


class GenerateRequest(BaseModel):
    topic: str
    goal: str | None = None


class GenerateResponse(BaseModel):
    run_id: str
    topic: str
    goal: str
    steps: Dict[str, Any]
    evaluation: Dict[str, Any]
    memory_context: str


app = FastAPI(title="AI Capstone Multi-Agent System", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency graph
logger.info("Initializing LLM...")
# Use Mock LLM for demo (no API token required)
from backend.models.mock_llm import MockLLM
shared_llm = MockLLM()
logger.info(f"LLM initialized successfully using Mock LLM (demo mode)")

logger.info("Initializing tools and services...")
search_tool = SearchTool()
seo_tool = SEOTool()
session_memory = SessionMemory()
long_term_memory = LongTermMemory()
run_logger = RunLogger()
evaluator = ContentEvaluator()

logger.info("Initializing agents...")
researcher = ResearcherAgent(shared_llm, search_tool)
writer = WriterAgent(shared_llm)
editor = EditorAgent(shared_llm, seo_tool)
coordinator = CoordinatorAgent(
    researcher=researcher,
    writer=writer,
    editor=editor,
    session_memory=session_memory,
    long_term_memory=long_term_memory,
    logger=run_logger,
    evaluator=evaluator,
)
logger.info("All agents initialized. Server ready!")


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/generate", response_model=GenerateResponse)
async def generate(payload: GenerateRequest):
    if not payload.topic:
        raise HTTPException(status_code=400, detail="Topic is required.")

    def _run():
        return coordinator.run({"topic": payload.topic, "goal": payload.goal or ""})

    result = await asyncio.to_thread(_run)
    return result


@app.get("/logs")
async def get_logs(limit: int = 50):
    return {"logs": run_logger.recent(limit)}


@app.get("/memory")
async def get_memory():
    return {"memory": long_term_memory.dump()}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)

