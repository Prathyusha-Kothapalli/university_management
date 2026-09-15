from fastapi import APIRouter, HTTPException, status
from ai.app.schemas.rag_expansion import (
    HybridSearchQuery,
    HybridSearchResponse,
    DocumentChunkCreate,
)
from ai.app.rag.document_chunker import DocumentChunker
from ai.app.rag.hybrid_retriever import HybridRetriever

router = APIRouter(prefix="/rag", tags=["AI RAG Expansion"])

chunker = DocumentChunker(chunk_size=300, overlap=30)
retriever = HybridRetriever()

# Pre-populate sample institutional knowledge base chunks
sample_docs = [
    {
        "chunk_id": "doc_policy_01",
        "document_id": "doc_academic_regulations_2026",
        "section": "Grading & Attendance",
        "content": "Students must maintain a minimum of 75% attendance in all enrolled courses to be eligible for end-semester examinations. Exemptions require HOD approval.",
    },
    {
        "chunk_id": "doc_policy_02",
        "document_id": "doc_academic_regulations_2026",
        "section": "Academic Holds",
        "content": "Financial holds prevent course registration and transcript issuance. Holds are placed when tuition balances exceed $500.",
    },
    {
        "chunk_id": "doc_obe_01",
        "document_id": "doc_obe_accreditation_guide",
        "section": "Course Outcomes",
        "content": "Course Outcomes (COs) are mapped directly to Program Outcomes (POs) with weights 1 (Low), 2 (Medium), and 3 (High) under NBA/ABET standards.",
    },
]
retriever.add_chunks(sample_docs)


@router.post("/hybrid-search", response_model=HybridSearchResponse)
def hybrid_search_knowledge_base(query: HybridSearchQuery):
    """Execute hybrid dense/sparse search over the university knowledge base."""
    return retriever.search(
        query=query.query_text,
        top_k=query.top_k,
        alpha=query.alpha_dense_weight,
    )


@router.post("/chunk-document")
def chunk_document_endpoint(document_id: str, content: str):
    """Chunk raw document into hierarchical overlapping windows for vector ingestion."""
    chunks = chunker.chunk_text(content, document_id)
    retriever.add_chunks(chunks)
    return {
        "document_id": document_id,
        "total_chunks_created": len(chunks),
        "sample_chunk": chunks[0] if chunks else None,
    }
