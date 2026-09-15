from typing import List
from .base_agent import BaseAgent
from ai.app.schemas.schemas import ToolCallResponse

class PlacementAgent(BaseAgent):
    """
    Dedicated AI Copilot for Placement Officers.
    Manages corporate recruitment drives, candidate eligibility scanners, shortlist publishing & offer letter verification.
    """
    def __init__(self, tool_registry, rag_pipeline):
        system_prompt = (
            "You are UniSphere AI Placement Officer Assistant. "
            "Assist TPO officers with corporate recruitment drives, candidate CGPA eligibility, interview shortlists, and offer letter verification."
        )
        super().__init__("placement", system_prompt, tool_registry, rag_pipeline)

    def infer_tool(self, query: str) -> str:
        q_lower = query.lower()
        if "offer" in q_lower or "verify" in q_lower:
            return "verify_offer_letter"
        return "get_placement_drives"

    def generate_response(self, query: str, rag_context: str, tools: List[ToolCallResponse]) -> str:
        tool_outputs = ""
        for t in tools:
            if t.success and t.result:
                tool_outputs += f"\n💼 Recruitment Drive Data ({t.tool_name}): {t.result}"

        return (
            f"💼 **UniSphere AI Training & Placement Officer Briefing**\n\n"
            f"Query: \"{query}\"\n\n"
            f"{tool_outputs if tool_outputs else ''}\n\n"
            f"📖 **Placement Policy:**\n{rag_context}\n\n"
            f"💡 **TPO Policy Note:** Single-offer policy strictly enforced for Tier-1 Super Dream drives."
        )
