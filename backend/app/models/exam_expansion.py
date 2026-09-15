from datetime import datetime
from uuid import UUID, uuid4
from sqlalchemy import Boolean, DateTime, ForeignKey, String, Text, Float, Integer, JSON
from sqlalchemy.orm import Mapped, mapped_column
from app.database.base import Base


class QuestionBankItem(Base):
    __tablename__ = "question_bank_items"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    course_id: Mapped[UUID] = mapped_column(
        ForeignKey("courses.id"),
        nullable=False,
        index=True
    )

    question_type: Mapped[str] = mapped_column(
        String(30), # MCQ, SHORT_ANSWER, ESSAY, CODING, TRUE_FALSE
        nullable=False
    )

    difficulty_level: Mapped[str] = mapped_column(
        String(20), # EASY, MEDIUM, HARD, EXPERT
        default="MEDIUM"
    )

    question_text: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    options: Mapped[dict | None] = mapped_column(
        JSON,
        nullable=True
    )

    correct_answer: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    points: Mapped[float] = mapped_column(
        Float,
        default=1.0
    )

    created_by_id: Mapped[UUID] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False
    )


class ExamPaper(Base):
    __tablename__ = "exam_papers"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    course_offering_id: Mapped[UUID] = mapped_column(
        ForeignKey("course_offerings.id"),
        nullable=False,
        index=True
    )

    title: Mapped[str] = mapped_column(
        String(200),
        nullable=False
    )

    total_marks: Mapped[float] = mapped_column(
        Float,
        default=100.0
    )

    duration_minutes: Mapped[int] = mapped_column(
        Integer,
        default=120
    )

    is_published: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    created_by_id: Mapped[UUID] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False
    )


class ExamPaperQuestion(Base):
    __tablename__ = "exam_paper_questions"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    exam_paper_id: Mapped[UUID] = mapped_column(
        ForeignKey("exam_papers.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    question_id: Mapped[UUID] = mapped_column(
        ForeignKey("question_bank_items.id"),
        nullable=False
    )

    question_order: Mapped[int] = mapped_column(
        Integer,
        default=1
    )

    assigned_marks: Mapped[float] = mapped_column(
        Float,
        default=5.0
    )


class ProctorTelemetryLog(Base):
    __tablename__ = "proctor_telemetry_logs"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    student_id: Mapped[UUID] = mapped_column(
        ForeignKey("students.id"),
        nullable=False,
        index=True
    )

    exam_paper_id: Mapped[UUID] = mapped_column(
        ForeignKey("exam_papers.id"),
        nullable=False
    )

    anomaly_type: Mapped[str] = mapped_column(
        String(50), # FACE_NOT_DETECTED, MULTIPLE_FACES, NOISE_DETECTED, TAB_SWITCH
        nullable=False
    )

    confidence_score: Mapped[float] = mapped_column(
        Float,
        default=0.95
    )

    snapshot_url: Mapped[str | None] = mapped_column(
        String(300),
        nullable=True
    )

    logged_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False
    )
