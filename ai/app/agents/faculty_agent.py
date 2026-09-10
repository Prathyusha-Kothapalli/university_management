from typing import List
from .base_agent import BaseAgent
from ai.app.schemas.schemas import ToolCallResponse

class FacultyAgent(BaseAgent):
    """
    Dedicated AI Copilot for Faculty. Assists with attendance sessions, assignment grading, section rosters, and exam marks.
    """
    def __init__(self, tool_registry, rag_pipeline):
        system_prompt = (
            "You are UniSphere AI Teaching Assistant for Professors and Instructors. "
            "Assist faculty with course attendance sessions, student grading rosters, office hours, and exam paper drafts."
        )
        super().__init__("faculty", system_prompt, tool_registry, rag_pipeline)

    def infer_tool(self, query: str) -> str:
        q_lower = query.lower()
        if "attendance" in q_lower or "mark" in q_lower:
            return "mark_attendance_session"
        elif "grade" in q_lower or "assignment" in q_lower:
            return "grade_assignment_submission"
        elif "marks" in q_lower or "exam" in q_lower:
            return "submit_exam_marks"
        return "get_faculty_courses"

    def generate_response(self, query: str, rag_context: str, tools: List[ToolCallResponse]) -> str:
        tool_outputs = ""
        for t in tools:
            if t.success and t.result:
                tool_outputs += f"\n📋 Verified Faculty Log ({t.tool_name}): {t.result}"

        return (
            f"👨‍🏫 **UniSphere AI Faculty Assistant**\n\n"
            f"Query: \"{query}\"\n\n"
            f"{tool_outputs if tool_outputs else ''}\n\n"
            f"📖 **Academic Guidelines:**\n{rag_context}\n\n"
            f"💡 **Instructor Action Item:** Ensure midterm grades & attendance logs are finalized before the exam cell deadline."
        )
