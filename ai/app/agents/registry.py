from typing import Dict
from .base_agent import BaseAgent
from .student_agent import StudentAgent
from .faculty_agent import FacultyAgent
from .hod_agent import HODAgent
from .parent_agent import ParentAgent
from .librarian_agent import LibrarianAgent
from .finance_agent import FinanceAgent
from .exam_agent import ExamAgent
from .placement_agent import PlacementAgent
from .admin_agent import AdminAgent
from ai.app.tools.registry import ToolRegistry
from ai.app.rag.pipeline import RAGPipeline

class AgentRegistry:
    """
    Factory & Registry for instantiating role-specific UniSphere AI Agents.
    """
    def __init__(self, tool_registry: ToolRegistry, rag_pipeline: RAGPipeline):
        self.tool_registry = tool_registry
        self.rag_pipeline = rag_pipeline
        self._agents: Dict[str, BaseAgent] = {}
        self._initialize_agents()

    def _initialize_agents(self):
        self._agents["student"] = StudentAgent(self.tool_registry, self.rag_pipeline)
        self._agents["faculty"] = FacultyAgent(self.tool_registry, self.rag_pipeline)
        self._agents["hod"] = HODAgent(self.tool_registry, self.rag_pipeline)
        self._agents["parent"] = ParentAgent(self.tool_registry, self.rag_pipeline)
        self._agents["librarian"] = LibrarianAgent(self.tool_registry, self.rag_pipeline)
        self._agents["finance"] = FinanceAgent(self.tool_registry, self.rag_pipeline)
        self._agents["exam"] = ExamAgent(self.tool_registry, self.rag_pipeline)
        self._agents["placement"] = PlacementAgent(self.tool_registry, self.rag_pipeline)
        self._agents["admin"] = AdminAgent(self.tool_registry, self.rag_pipeline)
        self._agents["super_admin"] = AdminAgent(self.tool_registry, self.rag_pipeline)

    def get_agent(self, user_role: str) -> BaseAgent:
        role_lower = user_role.lower()
        return self._agents.get(role_lower, self._agents["student"])
