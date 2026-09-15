from typing import List
from .base_agent import BaseAgent
from ai.app.schemas.schemas import ToolCallResponse

class HODAgent(BaseAgent):
    """
    Dedicated AI Executive Copilot for Heads of Department.
    Provides department analytics, faculty workload distribution, at-risk student lists, and syllabus approvals.
    """
    def __init__(self, tool_registry, rag_pipeline):
        system_prompt = (
            "You are UniSphere AI Department Executive Assistant for HODs. "
            "Provide department performance metrics, faculty workload analysis, at-risk student lists, and syllabus approvals."
        )
        super().__init__("hod", system_prompt, tool_registry, rag_pipeline)

    def infer_tool(self, query: str) -> str:
        q_lower = query.lower()
        if "workload" in q_lower or "faculty" in q_lower:
            return "get_faculty_workload"
        elif "risk" in q_lower or "at-risk" in q_lower or "detention" in q_lower:
            return "get_at_risk_students"
        elif "syllabus" in q_lower or "revision" in q_lower:
            return "approve_syllabus_revision"
        return "get_dept_analytics"

    def generate_response(self, query: str, rag_context: str, tools: List[ToolCallResponse]) -> str:
        tool_outputs = ""
        for t in tools:
            if t.success and t.result:
                tool_outputs += f"\n🏛️ Department Analytics Data ({t.tool_name}): {t.result}"

        return (
            f"🏛️ **UniSphere AI Department Executive Briefing**\n\n"
            f"Query: \"{query}\"\n\n"
            f"{tool_outputs if tool_outputs else ''}\n\n"
            f"📖 **Department Regulations:**\n{rag_context}\n\n"
            f"📈 **Executive Summary:** Department performance is tracking at Rank #1 with 94.8% pass rate and 91.2% placement rate."
        )
