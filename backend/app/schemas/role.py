from uuid import UUID

from pydantic import BaseModel, ConfigDict


class RoleCreate(BaseModel):
    name: str
    description: str | None = None


class RoleUpdate(BaseModel):
    name: str | None = None
    description: str | None = None


class RoleResponse(BaseModel):
    id: UUID
    name: str
    description: str | None

    model_config = ConfigDict(from_attributes=True)