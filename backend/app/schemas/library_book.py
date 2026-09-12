from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class LibraryBookCreate(BaseModel):
    university_id: UUID
    isbn: str | None = None
    title: str
    author: str
    publisher: str | None = None
    category: str | None = None
    total_copies: int = 1
    available_copies: int = 1


class LibraryBookUpdate(BaseModel):
    university_id: UUID | None = None
    isbn: str | None = None
    title: str | None = None
    author: str | None = None
    publisher: str | None = None
    category: str | None = None
    total_copies: int | None = None
    available_copies: int | None = None


class LibraryBookResponse(BaseModel):
    id: UUID
    university_id: UUID
    isbn: str | None
    title: str
    author: str
    publisher: str | None
    category: str | None
    total_copies: int
    available_copies: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
