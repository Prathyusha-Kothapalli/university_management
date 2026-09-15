from typing import List
from .base_agent import BaseAgent
from ai.app.schemas.schemas import ToolCallResponse

class FinanceAgent(BaseAgent):
    """
    Dedicated AI Copilot for Finance Officers & Accountants.
    Processes tuition payments, receipts, fee defaulter ledgers, installment plans & caution money refunds.
    """
    def __init__(self, tool_registry, rag_pipeline):
        system_prompt = (
            "You are UniSphere AI Finance & Accounting Assistant. "
            "Assist finance officers with student fee ledgers, payment receipts, fee defaulters, and installment calculators."
        )
        super().__init__("finance", system_prompt, tool_registry, rag_pipeline)

    def infer_tool(self, query: str) -> str:
        q_lower = query.lower()
        if "pay" in q_lower or "process" in q_lower:
            return "process_fee_payment"
        elif "defaulter" in q_lower or "outstanding" in q_lower:
            return "get_defaulters_ledger"
        elif "installment" in q_lower or "plan" in q_lower:
            return "calculate_installment_plan"
        return "get_student_fee_status"

    def generate_response(self, query: str, rag_context: str, tools: List[ToolCallResponse]) -> str:
        tool_outputs = ""
        for t in tools:
            if t.success and t.result:
                tool_outputs += f"\n💳 Financial Transaction Data ({t.tool_name}): {t.result}"

        return (
            f"💳 **UniSphere AI Finance Officer Assistant**\n\n"
            f"Query: \"{query}\"\n\n"
            f"{tool_outputs if tool_outputs else ''}\n\n"
            f"📖 **University Finance Policy:**\n{rag_context}\n\n"
            f"💡 **Ledger Summary:** 0% interest installment plans are active for Spring 2026 semester."
        )
