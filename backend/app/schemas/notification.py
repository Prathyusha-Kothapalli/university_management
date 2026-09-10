from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class NotificationCreate(BaseModel):
    user_id: UUID
    title: str
    message: str
    type: str = "ANNOUNCEMENT"
    is_read: bool = False


class NotificationUpdate(BaseModel):
    user_id: UUID | None = None
    title: str | None = None
    message: str | None = None
    type: str | None = None
    is_read: bool | None = None


class NotificationResponse(BaseModel):
    id: UUID
    user_id: UUID
    title: str
    message: str
    type: str
    is_read: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
