import uuid
from typing import List, Optional
from sqlalchemy import select, and_
from sqlalchemy.orm import Session

from app.models.evaluation_ast_grading import (
    CodeSubmissionAst,
    PlagiarismScanReport,
)
from app.schemas.evaluation_ast_grading import (
    CodeAstCreate,
    PlagiarismScanCreate,
)


def save_code_ast(
    db: Session,
    data: CodeAstCreate
) -> CodeSubmissionAst:
    ast_obj = CodeSubmissionAst(
        submission_id=data.submission_id,
        ast_json=data.ast_json,
        cyclomatic_complexity=data.cyclomatic_complexity,
        linter_warnings=data.linter_warnings,
    )
    db.add(ast_obj)
    db.commit()
    db.refresh(ast_obj)
    return ast_obj


def record_plagiarism_report(
    db: Session,
    data: PlagiarismScanCreate
) -> PlagiarismScanReport:
    is_flagged = data.similarity_score >= 0.70
    report = PlagiarismScanReport(
        submission_a_id=data.submission_a_id,
        submission_b_id=data.submission_b_id,
        similarity_score=data.similarity_score,
        matched_tokens=data.matched_tokens,
        is_flagged=is_flagged,
    )
    db.add(report)
    db.commit()
    db.refresh(report)
    return report
