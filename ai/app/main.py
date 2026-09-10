from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from ai.app.schemas.schemas import AgentQueryRequest, AgentQueryResponse
from ai.app.services.conversation_service import ConversationService

app = FastAPI(
    title="UniSphere AI Microservice",
    version="1.0.0",
    description="Dedicated Multi-Agent AI Subsystem with RAG & Tool Execution for UniSphere AI Platform"
)

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
        "version": "1.0.0",
        "registered_agents": 10,
        "registered_tools": 10
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
        "conversation_id": conversation_id,
        "history": conversation_service.get_history(conversation_id)
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
