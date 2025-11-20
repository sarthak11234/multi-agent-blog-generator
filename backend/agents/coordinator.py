from __future__ import annotations

import uuid
from typing import Any, Dict

from agents.base import BaseAgent
from memory.long_term_memory import LongTermMemory
from memory.session_memory import SessionMemory
from services.evaluator import ContentEvaluator
from services.logger import RunLogger


class CoordinatorAgent(BaseAgent):
    """Orchestrates the multi-agent workflow."""

    def __init__(
        self,
        researcher,
        writer,
        editor,
        session_memory: SessionMemory,
        long_term_memory: LongTermMemory,
        logger: RunLogger,
        evaluator: ContentEvaluator,
    ):
        super().__init__("coordinator", llm=None)
        self.researcher = researcher
        self.writer = writer
        self.editor = editor
        self.session_memory = session_memory
        self.long_term_memory = long_term_memory
        self.logger = logger
        self.evaluator = evaluator

    def _ensure_run_id(self, payload: Dict[str, Any]) -> str:
        run_id = payload.get("run_id")
        if run_id:
            return run_id
        run_id = str(uuid.uuid4())
        payload["run_id"] = run_id
        return run_id

    def run(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        topic: str = payload.get("topic", "")
        goal: str = payload.get("goal", "Inform and educate the reader.")
        run_id = self._ensure_run_id(payload)

        memory_context = self.long_term_memory.retrieve(topic)
        self.session_memory.start_session(run_id, topic, goal)

        try:
            researcher_output = self.researcher.run(
                {"topic": topic, "goal": goal, "memory": memory_context}
            )
            self.session_memory.append(run_id, "researcher", researcher_output["summary"])
            self.logger.log(
                agent="researcher",
                run_id=run_id,
                content=researcher_output["summary"],
            )
        except Exception as e:
            self.logger.log(agent="researcher", run_id=run_id, content=f"Error: {str(e)}")
            raise e


        try:
            writer_output = self.writer.run(
                {
                    "topic": topic,
                    "goal": goal,
                    "research_summary": researcher_output["summary"],
                }
            )
            self.session_memory.append(run_id, "writer", writer_output["draft"])
            self.logger.log(agent="writer", run_id=run_id, content=writer_output["draft"])
        except Exception as e:
            self.logger.log(agent="writer", run_id=run_id, content=f"Error: {str(e)}")
            raise e


        try:
            editor_output = self.editor.run(
                {"topic": topic, "goal": goal, "draft": writer_output["draft"]}
            )
            self.session_memory.append(
                run_id, "editor", editor_output["final_content"]
            )
            self.logger.log(
                agent="editor",
                run_id=run_id,
                content=editor_output["final_content"],
                extra=editor_output.get("seo_report"),
            )
        except Exception as e:
            self.logger.log(agent="editor", run_id=run_id, content=f"Error: {str(e)}")
            raise e

        evaluation = self.evaluator.evaluate(editor_output["final_content"])

        self.long_term_memory.add_memory(
            topic=topic,
            content=editor_output["final_content"],
            metadata={"goal": goal, "run_id": run_id},
        )

        return {
            "run_id": run_id,
            "topic": topic,
            "goal": goal,
            "steps": {
                "researcher": researcher_output,
                "writer": writer_output,
                "editor": editor_output,
            },
            "evaluation": evaluation,
            "memory_context": memory_context,
        }

