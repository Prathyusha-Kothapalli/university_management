from typing import List, Dict, Any
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
try:
    from models.study_assistant import (
        StudyAssistantRequest,
        StudyAssistantResponse,
        FeedbackRequest
    )
    from services.study_assistant_service import StudyAssistantService
except ImportError:
    from app.models.study_assistant import (
        StudyAssistantRequest,
        StudyAssistantResponse,
        FeedbackRequest
    )
    from app.services.study_assistant_service import StudyAssistantService

app = FastAPI(
    title="UniSphere AI Service",
    version="0.1.0",
    description="Dedicated AI microservice for UniSphere AI Study Assistant & RAG pipelines"
)

# CORS middleware for seamless web integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(assistant_router)
app.include_router(rag_expanded_router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

conversation_service = ConversationService()

@app.get("/")
def read_root():
    return {
        "status": "healthy",
        "service": "UniSphere AI Microservice",
        "version": "0.1.0",
        "message": "AI Study Assistant & RAG Microservice Online"
    }

@app.get("/health")
def health_check():
    return {"status": "ok", "service": "ai"}

@app.post("/api/v1/query", response_model=AgentQueryResponse)
def process_agent_query(request: AgentQueryRequest):
    try:
        response = conversation_service.query(request)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/conversations/{conversation_id}/history")
def get_conversation_history(conversation_id: str):
    return {
        "status": "ok",
        "service": "ai",
        "features": ["study_assistant", "rag_retrieval", "multi_mode_explanation"]
    }

@app.get("/ai/courses", response_model=List[Dict[str, Any]])
def get_courses():
    """
    Retrieve indexed university curriculum courses available for AI study assistance.
    """
    return StudyAssistantService.get_available_courses()

@app.post("/ai/study-assistant", response_model=StudyAssistantResponse, status_code=status.HTTP_200_OK)
def handle_study_assistant_query(request: StudyAssistantRequest):
    """
    Process student academic query via RAG retrieval and multi-mode response synthesis.
    """
    return StudyAssistantService.generate_response(request)

@app.post("/ai/feedback", status_code=status.HTTP_200_OK)
def handle_feedback(feedback: FeedbackRequest):
    """
    Record student feedback (Helpful / Not Helpful) for continuous RAG quality evaluation.
    """
    return {
        "status": "success",
        "message": "Feedback recorded successfully",
        "conversation_id": feedback.conversation_id,
        "is_helpful": feedback.is_helpful
    }

@app.get("/api/v1/tools")
def list_available_tools():
    return conversation_service.tool_registry.list_tools()

@app.post("/api/v1/rag/search")
def search_rag_knowledge(query: str, top_k: int = 3):
    results = conversation_service.rag_pipeline.retrieve_context(query, top_k=top_k)
    return [
        {
            "title": r.chunk.document_title,
            "category": r.chunk.document_category,
            "content": r.chunk.content,
            "score": r.similarity_score
        }
        for r in results
    ]
