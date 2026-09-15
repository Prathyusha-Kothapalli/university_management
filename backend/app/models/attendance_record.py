from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class AttendanceRecord(Base):
    __tablename__ = "attendance_records"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    attendance_session_id: Mapped[UUID] = mapped_column(
        ForeignKey("attendance_sessions.id"),
        nullable=False,
        index=True
    )

    student_id: Mapped[UUID] = mapped_column(
        ForeignKey("students.id"),
        nullable=False,
        index=True
    )

    status: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        default="PRESENT"
    )

    marked_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )

    remarks: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )

    attendance_session = relationship(
        "AttendanceSession",
        back_populates="attendance_records"
    )

    student = relationship(
        "Student",
        back_populates="attendance_records"
    )