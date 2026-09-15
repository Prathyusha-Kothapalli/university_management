from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field


class DocumentChunkCreate(BaseModel):
    document_id: str
    content: str
    metadata: Dict[str, Any] = Field(default_factory=dict)
    chunk_index: int = 0


class HybridSearchQuery(BaseModel):
    query_text: str
    top_k: int = 5
    alpha_dense_weight: float = 0.7 # 0.7 dense + 0.3 sparse
    filter_metadata: Optional[Dict[str, Any]] = None


class SearchResultItem(BaseModel):
    chunk_id: str
    document_id: str
    content: str
    score: float
    dense_score: float
    sparse_score: float
    metadata: Dict[str, Any]


class HybridSearchResponse(BaseModel):
    query: str
    total_results: int
    results: List[SearchResultItem]
    execution_time_ms: float
