import uuid
from datetime import datetime
from typing import List, Optional
from sqlalchemy import select, and_
from sqlalchemy.orm import Session

from app.models.exam_expansion import (
    QuestionBankItem,
    ExamPaper,
    ExamPaperQuestion,
    ProctorTelemetryLog,
)
from app.schemas.exam_expansion import (
    QuestionBankItemCreate,
    ExamPaperCreate,
    ProctorTelemetryCreate,
)


def create_question_item(
    db: Session,
    created_by_id: uuid.UUID,
    data: QuestionBankItemCreate
) -> QuestionBankItem:
    item = QuestionBankItem(
        course_id=data.course_id,
        question_type=data.question_type,
        difficulty_level=data.difficulty_level,
        question_text=data.question_text,
        options=data.options,
        correct_answer=data.correct_answer,
        points=data.points,
        created_by_id=created_by_id,
    )
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def generate_exam_paper(
    db: Session,
    created_by_id: uuid.UUID,
    data: ExamPaperCreate
) -> ExamPaper:
    paper = ExamPaper(
        course_offering_id=data.course_offering_id,
        title=data.title,
        total_marks=data.total_marks,
        duration_minutes=data.duration_minutes,
        is_published=True,
        created_by_id=created_by_id,
    )
    db.add(paper)
    db.flush()

    for idx, q_id in enumerate(data.question_ids, start=1):
        link = ExamPaperQuestion(
            exam_paper_id=paper.id,
            question_id=q_id,
            question_order=idx,
            assigned_marks=data.total_marks / max(len(data.question_ids), 1),
        )
        db.add(link)

    db.commit()
    db.refresh(paper)
    return paper


def log_proctor_telemetry(
    db: Session,
    data: ProctorTelemetryCreate
) -> ProctorTelemetryLog:
    log = ProctorTelemetryLog(
        student_id=data.student_id,
        exam_paper_id=data.exam_paper_id,
        anomaly_type=data.anomaly_type,
        confidence_score=data.confidence_score,
        snapshot_url=data.snapshot_url,
    )
    db.add(log)
    db.commit()
    db.refresh(log)
    return log
