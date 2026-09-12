import uuid
from typing import List, Dict, Any, Optional
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from ai.app.services.document_ingestor import document_ingestor
from ai.app.rag.pipeline import RAGPipeline

router = APIRouter(
    prefix="/api/v1/assistant",
    tags=["AI Assistant & Study Engine"]
)

rag_pipeline = RAGPipeline()


class StudyQuizRequest(BaseModel):
    subject: str
    topic: str
    num_questions: int = 3
    difficulty: str = "Medium"


class DocumentIngestRequest(BaseModel):
    document_title: str
    category: str
    content: str
    author: Optional[str] = "Faculty Desk"


class RAGQueryRequest(BaseModel):
    query: str
    top_k: int = 3


@router.post("/generate-quiz")
def generate_study_quiz(req: StudyQuizRequest):
    quiz_id = str(uuid.uuid4())
    questions = []

    for i in range(1, req.num_questions + 1):
        questions.append({
            "question_id": f"q-{i}",
            "prompt": f"Regarding {req.subject} ({req.topic}), what is the primary function of component #{i}?",
            "options": [
                f"Option A: Standard {req.topic} allocation",
                f"Option B: Optimized {req.topic} execution",
                f"Option C: Multi-tenant {req.topic} isolation",
                f"Option D: None of the above"
            ],
            "correct_answer": "Option B: Optimized " + req.topic + " execution",
            "explanation": f"In {req.subject}, component #{i} governs optimized {req.topic} execution cycles."
        })

    return {
        "quiz_id": quiz_id,
        "subject": req.subject,
        "topic": req.topic,
        "num_questions": req.num_questions,
        "difficulty": req.difficulty,
        "questions": questions,
        "generated_at": "2026-09-11T12:30:00Z"
    }


@router.post("/ingest-document")
def ingest_rag_document(req: DocumentIngestRequest):
    res = document_ingestor.ingest_document(
        document_title=req.document_title,
        category=req.category,
        raw_text=req.content,
        author=req.author
    )
    return {
        "message": "Document ingested into AI RAG Vector Store successfully",
        "result": res
    }


@router.post("/rag-query")
def query_rag_knowledge(req: RAGQueryRequest):
    context = rag_pipeline.build_prompt_context(req.query)
    results = rag_pipeline.retrieve_context(req.query, top_k=req.top_k)

    return {
        "query": req.query,
        "retrieved_chunks_count": len(results),
        "context": context,
        "citations": [
            {
                "title": r.chunk.document_title,
                "category": r.chunk.document_category,
                "similarity_score": round(r.similarity_score, 4)
            }
            for r in results
        ]
    }
