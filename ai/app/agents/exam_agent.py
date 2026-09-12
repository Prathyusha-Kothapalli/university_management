from typing import List
from .base_agent import BaseAgent
from ai.app.schemas.schemas import ToolCallResponse

class ExamAgent(BaseAgent):
    """
    Dedicated AI Copilot for Examination Officers.
    Generates exam hall tickets, seating plans, invigilator schedules, and grade validation.
    """
    def __init__(self, tool_registry, rag_pipeline):
        system_prompt = (
            "You are UniSphere AI Examination Cell Assistant. "
            "Assist exam officers with hall tickets, room seat allocations, attendance clearance, and result publishing."
        )
        super().__init__("exam", system_prompt, tool_registry, rag_pipeline)

    def infer_tool(self, query: str) -> str:
        return "generate_hall_ticket"

    def generate_response(self, query: str, rag_context: str, tools: List[ToolCallResponse]) -> str:
        tool_outputs = ""
        for t in tools:
            if t.success and t.result:
                tool_outputs += f"\n📝 Exam Cell Admittance Data ({t.tool_name}): {t.result}"

        return (
            f"📝 **UniSphere AI Examination Cell Assistant**\n\n"
            f"Query: \"{query}\"\n\n"
            f"{tool_outputs if tool_outputs else ''}\n\n"
            f"📖 **Exam Cell Regulations:**\n{rag_context}\n\n"
            f"💡 **Exam Cell Note:** Hall tickets require minimum 75% attendance clearance & zero fee dues."
        )
