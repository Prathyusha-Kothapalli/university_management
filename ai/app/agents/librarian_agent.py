from typing import List
from .base_agent import BaseAgent
from ai.app.schemas.schemas import ToolCallResponse

class LibrarianAgent(BaseAgent):
    """
    Dedicated AI Copilot for Librarians. Manages catalog search, book issues, returns, overdue fines & circulation analytics.
    """
    def __init__(self, tool_registry, rag_pipeline):
        system_prompt = (
            "You are UniSphere AI Library Assistant. "
            "Assist librarians and borrowers with catalog search, book issues, returns, overdue fines, and e-book access."
        )
        super().__init__("librarian", system_prompt, tool_registry, rag_pipeline)

    def infer_tool(self, query: str) -> str:
        q_lower = query.lower()
        if "issue" in q_lower or "borrow" in q_lower:
            return "issue_book"
        elif "return" in q_lower:
            return "return_book"
        elif "fine" in q_lower or "overdue" in q_lower:
            return "calculate_overdue_fine"
        return "search_library_books"

    def generate_response(self, query: str, rag_context: str, tools: List[ToolCallResponse]) -> str:
        tool_outputs = ""
        for t in tools:
            if t.success and t.result:
                tool_outputs += f"\n📚 Circulation Data ({t.tool_name}): {t.result}"

        return (
            f"📚 **UniSphere AI Library Assistant**\n\n"
            f"Query: \"{query}\"\n\n"
            f"{tool_outputs if tool_outputs else ''}\n\n"
            f"📖 **Library Policy Reference:**\n{rag_context}\n\n"
            f"💡 **Circulation Note:** Maximum loan period is 14 days with Rs. 5/day overdue fine after due date."
        )
