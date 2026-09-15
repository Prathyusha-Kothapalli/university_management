from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class PlacementApplication(Base):
    __tablename__ = "placement_applications"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    placement_drive_id: Mapped[UUID] = mapped_column(
        ForeignKey("placement_drives.id"),
        nullable=False,
        index=True
    )

    student_id: Mapped[UUID] = mapped_column(
        ForeignKey("students.id"),
        nullable=False,
        index=True
    )

    application_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="APPLIED",
        nullable=False
    )

    resume_url: Mapped[str | None] = mapped_column(
        String(500),
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

    placement_drive = relationship(
        "PlacementDrive",
        back_populates="applications"
    )

    student = relationship("Student")
