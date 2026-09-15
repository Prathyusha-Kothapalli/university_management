from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict


# --- Menu Item ---
class CanteenMenuItemCreate(BaseModel):
    name: str
    category: str
    price: float
    is_available: bool = True
    calories: Optional[int] = None
    allergens: Optional[str] = None


class CanteenMenuItemUpdate(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    price: Optional[float] = None
    is_available: Optional[bool] = None
    calories: Optional[int] = None
    allergens: Optional[str] = None


class CanteenMenuItemResponse(BaseModel):
    id: UUID
    name: str
    category: str
    price: float
    is_available: bool
    calories: Optional[int]
    allergens: Optional[str]
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


# --- Canteen Order ---
class CanteenOrderCreate(BaseModel):
    user_id: UUID
    total_amount: float


class CanteenOrderResponse(BaseModel):
    id: UUID
    user_id: UUID
    total_amount: float
    status: str
    payment_status: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


# --- Meal Plan ---
class CanteenMealPlanCreate(BaseModel):
    student_id: UUID
    plan_name: str
    remaining_credits: int
    start_date: datetime
    end_date: datetime


class CanteenMealPlanResponse(BaseModel):
    id: UUID
    student_id: UUID
    plan_name: str
    remaining_credits: int
    start_date: datetime
    end_date: datetime
    is_active: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
