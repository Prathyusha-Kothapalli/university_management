from abc import ABC, abstractmethod
from typing import Dict, Any, List
from ai.app.schemas.schemas import AgentQueryRequest, AgentQueryResponse, ToolCallRequest, ToolCallResponse
from ai.app.safety.pii_sanitizer import PIISanitizer
from ai.app.safety.injection_detector import PromptInjectionDetector
from ai.app.safety.permission_validator import ToolPermissionValidator
from ai.app.tools.registry import ToolRegistry
from ai.app.rag.pipeline import RAGPipeline

class BaseAgent(ABC):
    """
    Abstract Base Class for all UniSphere AI Role-Specific Agents.
    Enforces PII redaction, prompt injection defense, tool permission scoping, and RAG context.
    """
    def __init__(self, role_name: str, system_prompt: str, tool_registry: ToolRegistry, rag_pipeline: RAGPipeline):
        self.role_name = role_name
        self.system_prompt = system_prompt
        self.tool_registry = tool_registry
        self.rag_pipeline = rag_pipeline
        self.pii_sanitizer = PIISanitizer()
        self.injection_detector = PromptInjectionDetector()
        self.permission_validator = ToolPermissionValidator()

    def process_query(self, request: AgentQueryRequest) -> AgentQueryResponse:
        # 1. Prompt Injection Defense
        is_injection, phrases = self.injection_detector.is_injection_attempt(request.query)
        if is_injection:
            return AgentQueryResponse(
                conversation_id=request.conversation_id or f"conv-{request.user_id}",
                user_role=request.user_role,
                query=request.query,
                answer=f"⚠️ Request blocked: Potential prompt security injection detected ({', '.join(phrases)}).",
                confidence_score=0.0
            )

        # 2. PII Sanitization
        clean_query, _ = self.pii_sanitizer.sanitize(request.query)

        # 3. RAG Retrieval
        rag_context = ""
        citations = []
        if request.enable_rag:
            rag_results = self.rag_pipeline.retrieve_context(clean_query)
            rag_context = self.rag_pipeline.build_prompt_context(clean_query)
            citations = [{"title": r.chunk.document_title, "category": r.chunk.document_category} for r in rag_results]

        # 4. Tool Execution if enabled
        executed_tools: List[ToolCallResponse] = []
        if request.enable_tools:
            tool_name = self.infer_tool(clean_query)
            if tool_name:
                if self.permission_validator.is_tool_authorized(request.user_role, tool_name):
                    tool = self.tool_registry.get_tool(tool_name)
                    if tool:
                        t_req = ToolCallRequest(
                            tool_name=tool_name,
                            arguments={"query": clean_query, "target": "auto"},
                            user_id=request.user_id,
                            user_role=request.user_role
                        )
                        t_res = tool.run(t_req)
                        executed_tools.append(t_res)
                else:
                    executed_tools.append(ToolCallResponse(
                        tool_name=tool_name,
                        success=False,
                        error=f"Permission Denied: Role '{request.user_role}' is not authorized to run tool '{tool_name}'.",
                        execution_time_ms=0.0
                    ))

        # 5. Generate Structured Response
        answer = self.generate_response(clean_query, rag_context, executed_tools)

        return AgentQueryResponse(
            conversation_id=request.conversation_id or f"conv-{request.user_id}",
            user_role=request.user_role,
            query=request.query,
            answer=answer,
            citations=citations,
            tools_executed=executed_tools,
            confidence_score=0.98
        )

    @abstractmethod
    def infer_tool(self, query: str) -> str:
        pass

    @abstractmethod
    def generate_response(self, query: str, rag_context: str, tools: List[ToolCallResponse]) -> str:
        pass
