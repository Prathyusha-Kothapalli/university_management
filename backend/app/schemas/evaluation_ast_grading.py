from datetime import datetime
from typing import Optional, List, Dict, Any
from uuid import UUID
from pydantic import BaseModel, Field


class CodeAstCreate(BaseModel):
    submission_id: UUID
    ast_json: Dict[str, Any]
    cyclomatic_complexity: int = 1
    linter_warnings: int = 0


class CodeAstResponse(CodeAstCreate):
    id: UUID

    class Config:
        from_attributes = True


class PlagiarismScanCreate(BaseModel):
    submission_a_id: UUID
    submission_b_id: UUID
    similarity_score: float
    matched_tokens: int = 0


class PlagiarismScanResponse(PlagiarismScanCreate):
    id: UUID
    is_flagged: bool
    scanned_at: datetime

    class Config:
        from_attributes = True
