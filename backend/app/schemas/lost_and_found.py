from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict


# --- Lost Item ---
class LostItemCreate(BaseModel):
    reporter_id: UUID
    item_title: str
    category: str
    description: str
    location_lost: str
    date_lost: datetime
    contact_number: Optional[str] = None


class LostItemUpdate(BaseModel):
    item_title: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    location_lost: Optional[str] = None
    status: Optional[str] = None


class LostItemResponse(BaseModel):
    id: UUID
    reporter_id: UUID
    item_title: str
    category: str
    description: str
    location_lost: str
    date_lost: datetime
    contact_number: Optional[str]
    status: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


# --- Item Claim ---
class ItemClaimCreate(BaseModel):
    item_id: UUID
    claimant_id: UUID
    proof_description: str


class ItemClaimUpdate(BaseModel):
    status: Optional[str] = None


class ItemClaimResponse(BaseModel):
    id: UUID
    item_id: UUID
    claimant_id: UUID
    proof_description: str
    status: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
