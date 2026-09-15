from typing import List
from .base_agent import BaseAgent
from ai.app.schemas.schemas import ToolCallResponse

class StudentAgent(BaseAgent):
    """
    Dedicated AI Copilot for Students. Helps with GPA calculation, course schedules, fee ledgers & study roadmaps.
    """
    def __init__(self, tool_registry, rag_pipeline):
        system_prompt = (
            "You are UniSphere AI Student Copilot. "
            "Help students check GPA, course attendance, assignment deadlines, fee ledgers, and placement eligibility."
        )
        super().__init__("student", system_prompt, tool_registry, rag_pipeline)

    def infer_tool(self, query: str) -> str:
        q_lower = query.lower()
        if "gpa" in q_lower or "cgpa" in q_lower or "calculate" in q_lower:
            return "calculate_gpa"
        elif "attendance" in q_lower or "absence" in q_lower:
            return "get_attendance_summary"
        elif "fee" in q_lower or "tuition" in q_lower or "due" in q_lower:
            return "get_student_fee_status"
        elif "placement" in q_lower or "drive" in q_lower:
            return "get_placement_drives"
        elif "book" in q_lower or "library" in q_lower:
            return "search_library_books"
        return "get_student_academics"

    def generate_response(self, query: str, rag_context: str, tools: List[ToolCallResponse]) -> str:
        tool_outputs = ""
        for t in tools:
            if t.success and t.result:
                tool_outputs += f"\n📊 Verified Student Data ({t.tool_name}): {t.result}"
            elif t.error:
                tool_outputs += f"\n⚠️ Tool Notice ({t.tool_name}): {t.error}"

        return (
            f"🎓 **UniSphere AI Student Copilot Assist**\n\n"
            f"Query: \"{query}\"\n\n"
            f"{tool_outputs if tool_outputs else ''}\n\n"
            f"📖 **University Policy Context:**\n{rag_context}\n\n"
            f"💡 **Recommendation:** Review your active coursework, maintain >=75% attendance in each course, and check placement eligibility thresholds."
        )
