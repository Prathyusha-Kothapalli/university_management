import pytest
from ai.app.rag.document_chunker import DocumentChunker
from ai.app.rag.hybrid_retriever import HybridRetriever


def test_document_chunker_markdown_and_overlap():
    chunker = DocumentChunker(chunk_size=20, overlap=5)
    sample_md = """# Academic Policy
Students must maintain at least 75% attendance to take end-semester exams.

## Financial Policy
Financial holds prevent course registration and degree transcript generation."""

    chunks = chunker.chunk_text(sample_md, document_id="doc_test_101")
    assert len(chunks) >= 2
    assert chunks[0]["document_id"] == "doc_test_101"
    assert "attendance" in chunks[0]["content"].lower()


def test_hybrid_retriever_dense_and_sparse():
    retriever = HybridRetriever()
    retriever.add_chunks([
        {"chunk_id": "ch1", "document_id": "d1", "section": "Attendance", "content": "75 percent attendance required for exams."},
        {"chunk_id": "ch2", "document_id": "d2", "section": "Hostel", "content": "Hostel room allocation opens every August."},
    ])

    resp = retriever.search(query="attendance requirement", top_k=2, alpha=0.7)
    assert resp.total_results == 2
    assert resp.results[0].chunk_id == "ch1"
    assert resp.results[0].score > 0.0
