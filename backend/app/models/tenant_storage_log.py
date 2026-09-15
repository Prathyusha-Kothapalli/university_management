from datetime import datetime
from uuid import UUID, uuid4
from sqlalchemy import DateTime, ForeignKey, String, BigInteger, Float
from sqlalchemy.orm import Mapped, mapped_column
from app.database.base import Base


class TenantStorageLog(Base):
    __tablename__ = "tenant_storage_logs"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )

    university_id: Mapped[UUID] = mapped_column(
        ForeignKey("universities.id"),
        nullable=False,
        index=True
    )

    total_storage_bytes: Mapped[int] = mapped_column(
        BigInteger,
        default=0,
        nullable=False
    )

    storage_quota_bytes: Mapped[int] = mapped_column(
        BigInteger,
        default=107374182400, # 100 GB default
        nullable=False
    )

    document_count: Mapped[int] = mapped_column(
        BigInteger,
        default=0,
        nullable=False
    )

    usage_percentage: Mapped[float] = mapped_column(
        Float,
        default=0.0
    )

    recorded_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False
    )
