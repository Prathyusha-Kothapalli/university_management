import re
import uuid
from typing import List, Dict, Any, Optional
from ai.app.schemas.schemas import RAGDocumentChunk
from ai.app.rag.pipeline import RAGPipeline


class DocumentIngestorService:
    """
    Ingests PDF/Text documents, extracts metadata, performs sliding-window chunking,
    and indexes document chunks into the vector store.
    """
    def __init__(self, rag_pipeline: Optional[RAGPipeline] = None):
        self.pipeline = rag_pipeline or RAGPipeline()

    def clean_text(self, text: str) -> str:
        # Normalize whitespace and strip special control characters
        cleaned = re.sub(r'\s+', ' ', text)
        cleaned = re.sub(r'[\x00-\x1F\x7F]', '', cleaned)
        return cleaned.strip()

    def chunk_text(self, text: str, chunk_size: int = 250, overlap: int = 40) -> List[str]:
        words = text.split()
        if len(words) <= chunk_size:
            return [text]

        chunks = []
        start = 0
        while start < len(words):
            end = start + chunk_size
            chunk_words = words[start:end]
            chunks.append(" ".join(chunk_words))
            start += (chunk_size - overlap)

        return chunks

    def ingest_document(
        self,
        document_title: str,
        category: str,
        raw_text: str,
        author: Optional[str] = "UniSphere Faculty"
    ) -> Dict[str, Any]:
        cleaned = self.clean_text(raw_text)
        text_chunks = self.chunk_text(cleaned)

        created_chunks = []
        doc_id = str(uuid.uuid4())

        for idx, content in enumerate(text_chunks, start=1):
            chunk_id = f"{doc_id}-chunk-{idx}"
            chunk = RAGDocumentChunk(
                chunk_id=chunk_id,
                document_title=document_title,
                document_category=category,
                content=content
            )
            self.pipeline.vector_store.add_chunk(chunk)
            created_chunks.append(chunk_id)

        return {
            "document_id": doc_id,
            "document_title": document_title,
            "category": category,
            "author": author,
            "total_words": len(cleaned.split()),
            "chunks_created": len(created_chunks),
            "chunk_ids": created_chunks
        }


document_ingestor = DocumentIngestorService()
