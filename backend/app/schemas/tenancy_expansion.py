from datetime import datetime
from typing import Optional, List
from uuid import UUID
from pydantic import BaseModel, EmailStr, Field


class TenantBrandingCreateUpdate(BaseModel):
    primary_color: str = "#1E40AF"
    secondary_color: str = "#3B82F6"
    accent_color: str = "#10B981"
    logo_url: Optional[str] = None
    favicon_url: Optional[str] = None
    custom_domain: Optional[str] = None
    custom_css: Optional[str] = None
    portal_title: str = "UniSphere Portal"
    support_email: Optional[EmailStr] = None


class TenantBrandingResponse(TenantBrandingCreateUpdate):
    id: UUID
    university_id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class TenantInvitationCreate(BaseModel):
    email: EmailStr
    role_name: str = "student"


class TenantInvitationResponse(BaseModel):
    id: UUID
    university_id: UUID
    email: str
    role_name: str
    invitation_token: str
    is_accepted: bool
    expires_at: datetime
    created_at: datetime

    class Config:
        from_attributes = True


class TenantFeatureFlagSchema(BaseModel):
    feature_key: str
    is_enabled: bool
    description: Optional[str] = None


class TenantStorageUsageResponse(BaseModel):
    university_id: UUID
    total_storage_bytes: int
    storage_quota_bytes: int
    document_count: int
    usage_percentage: float
    recorded_at: datetime


class BuildingRoomCreate(BaseModel):
    room_number: str
    room_type: str = "lecture_hall" # lecture_hall, lab, auditorium, office
    capacity: int = Field(30, ge=1)
    has_projector: bool = True
    has_air_conditioning: bool = True


class CampusBuildingCreate(BaseModel):
    campus_id: UUID
    building_name: str
    building_code: str
    number_of_floors: int = 1
