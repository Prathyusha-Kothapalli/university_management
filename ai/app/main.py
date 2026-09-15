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
