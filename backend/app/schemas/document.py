from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class DocumentCreate(BaseModel):
    user_id: UUID
    title: str
    document_type: str = "OTHER"
    file_url: str
    file_size: int | None = None
    mime_type: str | None = None


class DocumentUpdate(BaseModel):
    user_id: UUID | None = None
    title: str | None = None
    document_type: str | None = None
    file_url: str | None = None
    file_size: int | None = None
    mime_type: str | None = None


class DocumentResponse(BaseModel):
    id: UUID
    user_id: UUID
    title: str
    document_type: str
    file_url: str
    file_size: int | None
    mime_type: str | None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
