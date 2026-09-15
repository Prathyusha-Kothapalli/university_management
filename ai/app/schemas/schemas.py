from typing import Dict, Any, List, Optional
from pydantic import BaseModel, Field
from datetime import datetime

class ToolCallRequest(BaseModel):
    tool_name: str = Field(..., description="Name of tool to execute")
    arguments: Dict[str, Any] = Field(default_factory=dict, description="Arguments for tool")
    user_id: str = Field(..., description="ID of user calling tool")
    user_role: str = Field(..., description="Role of user calling tool")

class ToolCallResponse(BaseModel):
    tool_name: str
    success: bool
    result: Optional[Dict[str, Any]] = None
    error: Optional[str] = None
    execution_time_ms: float

class AgentQueryRequest(BaseModel):
    user_id: str = Field(..., description="Authenticated user ID")
    user_role: str = Field(..., description="User role: student, faculty, hod, parent, librarian, finance, exam, placement, admin")
    query: str = Field(..., min_length=1, description="Natural language prompt")
    conversation_id: Optional[str] = Field(None, description="Optional active conversation ID")
    context_override: Optional[Dict[str, Any]] = Field(default_factory=dict)
    enable_rag: bool = Field(default=True)
    enable_tools: bool = Field(default=True)

class AgentQueryResponse(BaseModel):
    conversation_id: str
    user_role: str
    query: str
    answer: str
    citations: List[Dict[str, Any]] = Field(default_factory=list)
    tools_executed: List[ToolCallResponse] = Field(default_factory=list)
    confidence_score: float = Field(default=0.95)
    execution_timestamp: datetime = Field(default_factory=datetime.utcnow)
    tokens_used: int = Field(default=0)

class RAGDocumentChunk(BaseModel):
    chunk_id: str
    document_title: str
    document_category: str
    content: str
    embedding: List[float] = Field(default_factory=list)
    metadata: Dict[str, Any] = Field(default_factory=dict)

class RAGSearchResult(BaseModel):
    chunk: RAGDocumentChunk
    similarity_score: float
    rerank_score: Optional[float] = None

class SafetyAuditLog(BaseModel):
    log_id: str
    user_id: str
    user_role: str
    event_type: str  # pii_detected, prompt_injection_blocked, unauthorized_tool
    details: Dict[str, Any]
    timestamp: datetime = Field(default_factory=datetime.utcnow)
