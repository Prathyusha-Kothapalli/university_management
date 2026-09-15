from typing import Dict, List, Optional, Any
from datetime import datetime
from ai.app.schemas.schemas import AgentQueryRequest, AgentQueryResponse
from ai.app.agents.registry import AgentRegistry
from ai.app.tools.registry import ToolRegistry
from ai.app.rag.pipeline import RAGPipeline

class ConversationService:
    """
    Manages active AI agent conversations, history buffers & role-specific query routing.
    """
    def __init__(self):
        self.tool_registry = ToolRegistry()
        self.rag_pipeline = RAGPipeline()
        self.agent_registry = AgentRegistry(self.tool_registry, self.rag_pipeline)
        self.conversations: Dict[str, List[Dict[str, Any]]] = {}

    def query(self, request: AgentQueryRequest) -> AgentQueryResponse:
        agent = self.agent_registry.get_agent(request.user_role)
        response = agent.process_query(request)

        # Store in conversation memory
        conv_id = response.conversation_id
        if conv_id not in self.conversations:
            self.conversations[conv_id] = []

        self.conversations[conv_id].append({
            "timestamp": datetime.utcnow().isoformat(),
            "query": request.query,
            "answer": response.answer,
            "role": request.user_role
        })

        return response

    def get_history(self, conversation_id: str) -> List[Dict[str, Any]]:
        return self.conversations.get(conversation_id, [])
