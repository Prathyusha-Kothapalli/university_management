import ast
import difflib
import uuid
from typing import List, Optional
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.assignment import Assignment
from app.schemas.assignment import (
    AssignmentCreate,
    AssignmentUpdate,
    AssignmentResponse,
)


router = APIRouter(
    prefix="/assignments",
    tags=["Assignments"]
)


class CodePlagiarismCheckRequest(BaseModel):
    source_code_a: str
    source_code_b: str
    language: str = "python"


class AutoRubricEvaluationRequest(BaseModel):
    submission_id: UUID
    test_cases_passed: int = 8
    total_test_cases: int = 10
    code_style_score: float = 9.0  # Out of 10
    time_complexity_rating: str = "O(N log N)"


@router.post(
    "/",
    response_model=AssignmentResponse
)
def create_assignment(
    assignment_data: AssignmentCreate,
    db: Session = Depends(get_db)
):
    try:
        assignment = Assignment(
            **assignment_data.model_dump()
        )

        db.add(assignment)
        db.commit()
        db.refresh(assignment)

        return assignment

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get(
    "/",
    response_model=list[AssignmentResponse]
)
def get_assignments(
    db: Session = Depends(get_db)
):
    result = db.execute(
        select(Assignment)
    )

    return result.scalars().all()


@router.post("/compare-code")
def compare_code_ast_plagiarism(req: CodePlagiarismCheckRequest):
    code_a = req.source_code_a.strip()
    code_b = req.source_code_b.strip()

    # Calculate token & structural sequence similarity ratio
    ratio = difflib.SequenceMatcher(None, code_a, code_b).ratio()
    similarity_percentage = round(ratio * 100, 2)

    # AST node count comparison for Python source code
    ast_nodes_a = 0
    ast_nodes_b = 0

    if req.language.lower() == "python":
        try:
            tree_a = ast.parse(code_a)
            ast_nodes_a = len(list(ast.walk(tree_a)))
        except Exception:
            ast_nodes_a = len(code_a.splitlines())

        try:
            tree_b = ast.parse(code_b)
            ast_nodes_b = len(list(ast.walk(tree_b)))
        except Exception:
            ast_nodes_b = len(code_b.splitlines())

    flagged_plagiarism = similarity_percentage > 70.0

    return {
        "language": req.language,
        "similarity_percentage": similarity_percentage,
        "ast_nodes_code_a": ast_nodes_a,
        "ast_nodes_code_b": ast_nodes_b,
        "flagged_plagiarism": flagged_plagiarism,
        "verdict": "PLAGIARISM_FLAGGED" if flagged_plagiarism else "PASS_CLEAN"
    }


@router.post("/evaluate-rubric")
def evaluate_auto_rubric(req: AutoRubricEvaluationRequest):
    pass_ratio = req.test_cases_passed / max(req.total_test_cases, 1)
    correctness_score = pass_ratio * 70.0  # 70% weight for test correctness
    style_weighted = (req.code_style_score / 10.0) * 20.0  # 20% weight for style
    efficiency_weighted = 10.0 if "O(N)" in req.time_complexity_rating or "O(1)" in req.time_complexity_rating else 7.5

    final_grade = round(correctness_score + style_weighted + efficiency_weighted, 2)

    letter_grade = "A" if final_grade >= 90 else "B" if final_grade >= 80 else "C" if final_grade >= 70 else "F"

    return {
        "submission_id": str(req.submission_id),
        "correctness_score": round(correctness_score, 2),
        "style_score": round(style_weighted, 2),
        "efficiency_score": round(efficiency_weighted, 2),
        "total_grade_percentage": final_grade,
        "letter_grade": letter_grade,
        "evaluated_at": "2026-09-11T11:55:00Z"
    }


@router.get(
    "/{assignment_id}",
    response_model=AssignmentResponse
)
def get_assignment(
    assignment_id: UUID,
    db: Session = Depends(get_db)
):
    assignment = db.get(
        Assignment,
        assignment_id
    )

    if not assignment:
        raise HTTPException(
            status_code=404,
            detail="Assignment not found"
        )

    return assignment


@router.put(
    "/{assignment_id}",
    response_model=AssignmentResponse
)
def update_assignment(
    assignment_id: UUID,
    assignment_data: AssignmentUpdate,
    db: Session = Depends(get_db)
):
    assignment = db.get(
        Assignment,
        assignment_id
    )

    if not assignment:
        raise HTTPException(
            status_code=404,
            detail="Assignment not found"
        )

    try:
        update_data = assignment_data.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            if hasattr(assignment, key):
                setattr(
                    assignment,
                    key,
                    value
                )

        db.commit()
        db.refresh(assignment)

        return assignment

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.delete("/{assignment_id}")
def delete_assignment(
    assignment_id: UUID,
    db: Session = Depends(get_db)
):
    assignment = db.get(
        Assignment,
        assignment_id
    )

    if not assignment:
        raise HTTPException(
            status_code=404,
            detail="Assignment not found"
        )

    db.delete(assignment)
    db.commit()

    return {
        "message": "Assignment deleted successfully"
    }

