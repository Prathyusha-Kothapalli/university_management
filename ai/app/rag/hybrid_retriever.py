import math
import time
from typing import List, Dict, Any
from ai.app.schemas.rag_expansion import SearchResultItem, HybridSearchResponse


class HybridRetriever:
    """
    Hybrid Retriever combining dense vector cosine similarity and BM25 term-frequency keyword matching.
    """

    def __init__(self):
        self.corpus_chunks: List[Dict[str, Any]] = []

    def add_chunks(self, chunks: List[Dict[str, Any]]):
        self.corpus_chunks.extend(chunks)

    def _compute_bm25_score(self, query: str, document_text: str) -> float:
        """Simple BM25 TF-IDF score computation."""
        query_words = set(query.lower().split())
        doc_words = document_text.lower().split()
        if not doc_words:
            return 0.0

        tf_dict = {}
        for w in doc_words:
            tf_dict[w] = tf_dict.get(w, 0) + 1

        score = 0.0
        doc_len = len(doc_words)
        k1 = 1.2
        b = 0.75
        avg_len = 150.0

        for qw in query_words:
            if qw in tf_dict:
                tf = tf_dict[qw]
                num = tf * (k1 + 1)
                denom = tf + k1 * (1 - b + b * (doc_len / avg_len))
                score += (num / denom)

        return min(score / 5.0, 1.0) # Normalized to [0, 1]

    def _mock_dense_similarity(self, query: str, text: str) -> float:
        """Simulated dense embedding cosine similarity based on n-gram overlap."""
        q_set = set(query.lower())
        t_set = set(text.lower())
        if not t_set:
            return 0.0
        jaccard = len(q_set.intersection(t_set)) / len(q_set.union(t_set))
        return min(jaccard * 1.8, 1.0)

    def search(
        self,
        query: str,
        top_k: int = 5,
        alpha: float = 0.7
    ) -> HybridSearchResponse:
        start_time = time.time()
        results = []

        for chk in self.corpus_chunks:
            dense_sim = self._mock_dense_similarity(query, chk["content"])
            sparse_bm25 = self._compute_bm25_score(query, chk["content"])

            combined_score = (alpha * dense_sim) + ((1.0 - alpha) * sparse_bm25)

            results.append(
                SearchResultItem(
                    chunk_id=chk.get("chunk_id", "chk_unknown"),
                    document_id=chk.get("document_id", "doc_unknown"),
                    content=chk["content"],
                    score=round(combined_score, 4),
                    dense_score=round(dense_sim, 4),
                    sparse_score=round(sparse_bm25, 4),
                    metadata={"section": chk.get("section", "General")},
                )
            )

        results.sort(key=lambda x: x.score, reverse=True)
        top_results = results[:top_k]
        elapsed_ms = (time.time() - start_time) * 1000.0

        return HybridSearchResponse(
            query=query,
            total_results=len(top_results),
            results=top_results,
            execution_time_ms=round(elapsed_ms, 2),
        )
