from typing import List, Dict, Any
from ai.app.schemas.schemas import RAGDocumentChunk, RAGSearchResult
from .embeddings import EmbeddingService
from .vector_store import VectorStore

class RAGPipeline:
    """
    Complete Retrieval-Augmented Generation Pipeline for University Regulations & Policies.
    """
    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.vector_store = VectorStore(self.embedding_service)
        self._seed_university_knowledge()

    def _seed_university_knowledge(self):
        docs = [
            {
                "id": "doc-1",
                "title": "Academic Regulations & Attendance Policy",
                "category": "Academic",
                "content": "UniSphere AI Academic Policy: Students must maintain minimum 75% attendance in each registered course to be eligible for End-Semester examinations. Attendance below 75% results in hall ticket detention unless medical condonation (up to 10%) is approved by Dean Academic Affairs."
            },
            {
                "id": "doc-2",
                "title": "Tuition Fee Installments & Payment Guidelines",
                "category": "Financial",
                "content": "Tuition Fee Policy: Tuition fees are due on the first day of each semester. Students may opt for 2-part, 3-part, or 4-part installment schedules with 0% interest penalty. Late fee of Rs. 100/day applies after 15 days grace period."
            },
            {
                "id": "doc-3",
                "title": "Central Library Borrowing Rules & Overdue Fines",
                "category": "Library",
                "content": "Library Policy: B.Tech students may borrow up to 4 books for a 14-day loan period. Overdue fine is Rs. 5 per book per day. Digital eBooks and online IEEE/ACM subscriptions are available 24/7."
            },
            {
                "id": "doc-4",
                "title": "Placement Drive Qualification & Dual Offer Policy",
                "category": "Placements",
                "content": "Placement Policy: Students with CGPA >= 8.0 and zero active backlogs are eligible for Tier-1 Super Dream corporate drives (CTC > Rs. 20 LPA). Once an offer is accepted, student is ineligible for lower CTC drives under the single-offer policy."
            }
        ]

        for doc in docs:
            chunk = RAGDocumentChunk(
                chunk_id=doc["id"],
                document_title=doc["title"],
                document_category=doc["category"],
                content=doc["content"]
            )
            self.vector_store.add_chunk(chunk)

    def retrieve_context(self, query: str, top_k: int = 2) -> List[RAGSearchResult]:
        return self.vector_store.search(query, top_k=top_k)

    def build_prompt_context(self, query: str) -> str:
        results = self.retrieve_context(query)
        if not results:
            return "No relevant university regulations found."

        context_blocks = []
        for r in results:
            context_blocks.append(f"[{r.chunk.document_title} - {r.chunk.document_category}]:\n{r.chunk.content}")

        return "\n\n".join(context_blocks)
