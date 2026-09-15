from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class AIMessageCreate(BaseModel):
    conversation_id: UUID
    sender: str
    content: str
    tokens_used: int | None = 0


class AIMessageUpdate(BaseModel):
    conversation_id: UUID | None = None
    sender: str | None = None
    content: str | None = None
    tokens_used: int | None = None


class AIMessageResponse(BaseModel):
    id: UUID
    conversation_id: UUID
    sender: str
    content: str
    tokens_used: int | None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
