from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import Boolean, DateTime, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Department(Base):
    __tablename__ = "departments"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    university_id: Mapped[UUID] = mapped_column(
        ForeignKey("universities.id"),
        nullable=False
    )

    campus_id: Mapped[UUID] = mapped_column(
        ForeignKey("campuses.id"),
        nullable=False
    )

    name: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )

    code: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False
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

    university = relationship(
        "University",
        back_populates="departments"
    )

    campus = relationship(
        "Campus",
        back_populates="departments"
    )

    programs = relationship(
        "Program",
        back_populates="department",
        cascade="all, delete-orphan"
    )