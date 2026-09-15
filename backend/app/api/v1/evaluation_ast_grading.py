import uuid
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.api.v1.auth import get_current_user
from app.schemas.evaluation_ast_grading import (
    CodeAstCreate,
    CodeAstResponse,
    PlagiarismScanCreate,
    PlagiarismScanResponse,
)
from app.services import evaluation_ast_grading_service

router = APIRouter(prefix="/ast-grading", tags=["AST Code Grading & Plagiarism Engine"])


@router.post("/ast-analysis", response_model=CodeAstResponse, status_code=status.HTTP_201_CREATED)
def save_code_ast(
    data: CodeAstCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    """Store AST structure, cyclomatic complexity, and linter metric analysis."""
    return evaluation_ast_grading_service.save_code_ast(
        db=db,
        data=data,
    )


@router.post("/plagiarism-reports", response_model=PlagiarismScanResponse, status_code=status.HTTP_201_CREATED)
def record_plagiarism_scan(
    data: PlagiarismScanCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    """Record pairwise code plagiarism similarity scan report."""
    return evaluation_ast_grading_service.record_plagiarism_report(
        db=db,
        data=data,
    )
