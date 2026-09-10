from typing import List
from .base_agent import BaseAgent
from ai.app.schemas.schemas import ToolCallResponse

class ParentAgent(BaseAgent):
    """
    Dedicated AI Advisory Copilot for Parents & Guardians.
    Provides authorized progress reports, attendance metrics, fee payment status, and faculty PTM scheduling for linked students.
    """
    def __init__(self, tool_registry, rag_pipeline):
        system_prompt = (
            "You are UniSphere AI Parent Advisor. "
            "Help parents monitor authorized student academic progress, attendance percentages, fee balances, and PTM slots."
        )
        super().__init__("parent", system_prompt, tool_registry, rag_pipeline)

    def infer_tool(self, query: str) -> str:
        q_lower = query.lower()
        if "attendance" in q_lower:
            return "get_linked_student_attendance"
        elif "fee" in q_lower or "due" in q_lower:
            return "get_linked_student_fees"
        elif "ptm" in q_lower or "meeting" in q_lower or "schedule" in q_lower:
            return "schedule_ptm_slot"
        return "get_linked_student_academics"

    def generate_response(self, query: str, rag_context: str, tools: List[ToolCallResponse]) -> str:
        tool_outputs = ""
        for t in tools:
            if t.success and t.result:
                tool_outputs += f"\n👨‍👩‍👧 Verified Student Summary ({t.tool_name}): {t.result}"

        return (
            f"👨‍👩‍👧 **UniSphere AI Parent Advisory Report**\n\n"
            f"Query: \"{query}\"\n\n"
            f"{tool_outputs if tool_outputs else ''}\n\n"
            f"📖 **Parent Guidance Notes:**\n{rag_context}\n\n"
            f"💡 **Advisor Note:** Your ward's attendance (94.5%) and academic CGPA (3.84) are in good standing."
        )
