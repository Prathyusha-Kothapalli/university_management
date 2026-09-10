from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class AIConversationCreate(BaseModel):
    user_id: UUID
    title: str = "New Conversation"


class AIConversationUpdate(BaseModel):
    user_id: UUID | None = None
    title: str | None = None


class AIConversationResponse(BaseModel):
    id: UUID
    user_id: UUID
    title: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
