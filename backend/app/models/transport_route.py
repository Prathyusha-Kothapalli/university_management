from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import DateTime, Float, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class TransportRoute(Base):
    __tablename__ = "transport_routes"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    campus_id: Mapped[UUID] = mapped_column(
        ForeignKey("campuses.id"),
        nullable=False,
        index=True
    )

    route_number: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    route_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    start_location: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    end_location: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    fee: Mapped[float] = mapped_column(
        Float,
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

    campus = relationship("Campus")

    vehicles = relationship(
        "TransportVehicle",
        back_populates="route",
        cascade="all, delete-orphan"
    )

    allocations = relationship(
        "TransportAllocation",
        back_populates="route",
        cascade="all, delete-orphan"
    )
