import math
from typing import List, Dict, Any
from ai.app.schemas.schemas import RAGDocumentChunk, RAGSearchResult
from .embeddings import EmbeddingService

class VectorStore:
    """
    In-Memory Vector Store for UniSphere AI Document Embeddings with Cosine Similarity Search.
    """
    def __init__(self, embedding_service: EmbeddingService):
        self.embedding_service = embedding_service
        self.chunks: List[RAGDocumentChunk] = []

    def add_chunk(self, chunk: RAGDocumentChunk):
        if not chunk.embedding:
            chunk.embedding = self.embedding_service.get_embedding(chunk.content)
        self.chunks.append(chunk)

    def cosine_similarity(self, vec1: List[float], vec2: List[float]) -> float:
        if not vec1 or not vec2:
            return 0.0
        dot = sum(a * b for a, b in zip(vec1, vec2))
        norm1 = math.sqrt(sum(a * a for a in vec1))
        norm2 = math.sqrt(sum(b * b for b in vec2))
        if norm1 == 0 or norm2 == 0:
            return 0.0
        return dot / (norm1 * norm2)

    def search(self, query_text: str, top_k: int = 3, category_filter: str = None) -> List[RAGSearchResult]:
        query_vec = self.embedding_service.get_embedding(query_text)
        results = []

        for chunk in self.chunks:
            if category_filter and chunk.document_category != category_filter:
                continue
            sim = self.cosine_similarity(query_vec, chunk.embedding)
            results.append(RAGSearchResult(chunk=chunk, similarity_score=sim))

        results.sort(key=lambda r: r.similarity_score, reverse=True)
        return results[:top_k]
