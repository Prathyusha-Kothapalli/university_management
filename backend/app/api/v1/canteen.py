from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.canteen import (
    CanteenMenuItem,
    CanteenOrder,
    CanteenMealPlan,
)
from app.schemas.canteen import (
    CanteenMenuItemCreate,
    CanteenMenuItemUpdate,
    CanteenMenuItemResponse,
    CanteenOrderCreate,
    CanteenOrderResponse,
    CanteenMealPlanCreate,
    CanteenMealPlanResponse,
)

router = APIRouter(
    prefix="/canteen",
    tags=["Smart Canteen & Meal Planner"]
)


# --- Menu Items ---
@router.post("/menu-items", response_model=CanteenMenuItemResponse, status_code=status.HTTP_201_CREATED)
def create_menu_item(
    item_in: CanteenMenuItemCreate,
    db: Session = Depends(get_db)
):
    item = CanteenMenuItem(**item_in.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


@router.get("/menu-items", response_model=List[CanteenMenuItemResponse])
def get_menu_items(
    category: str = None,
    db: Session = Depends(get_db)
):
    query = select(CanteenMenuItem)
    if category:
        query = query.where(CanteenMenuItem.category == category)
    result = db.execute(query)
    return result.scalars().all()


@router.patch("/menu-items/{item_id}", response_model=CanteenMenuItemResponse)
def update_menu_item(
    item_id: UUID,
    item_in: CanteenMenuItemUpdate,
    db: Session = Depends(get_db)
):
    item = db.get(CanteenMenuItem, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Menu item not found")
    
    update_data = item_in.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(item, field, value)
        
    db.commit()
    db.refresh(item)
    return item


# --- Canteen Orders ---
@router.post("/orders", response_model=CanteenOrderResponse, status_code=status.HTTP_201_CREATED)
def create_canteen_order(
    order_in: CanteenOrderCreate,
    db: Session = Depends(get_db)
):
    order = CanteenOrder(**order_in.model_dump())
    db.add(order)
    db.commit()
    db.refresh(order)
    return order


@router.get("/orders", response_model=List[CanteenOrderResponse])
def get_canteen_orders(
    user_id: UUID = None,
    db: Session = Depends(get_db)
):
    query = select(CanteenOrder)
    if user_id:
        query = query.where(CanteenOrder.user_id == user_id)
    result = db.execute(query)
    return result.scalars().all()


# --- Meal Plans ---
@router.post("/meal-plans", response_model=CanteenMealPlanResponse, status_code=status.HTTP_201_CREATED)
def create_meal_plan(
    plan_in: CanteenMealPlanCreate,
    db: Session = Depends(get_db)
):
    plan = CanteenMealPlan(**plan_in.model_dump())
    db.add(plan)
    db.commit()
    db.refresh(plan)
    return plan


@router.get("/meal-plans", response_model=List[CanteenMealPlanResponse])
def get_meal_plans(
    student_id: UUID = None,
    db: Session = Depends(get_db)
):
    query = select(CanteenMealPlan)
    if student_id:
        query = query.where(CanteenMealPlan.student_id == student_id)
    result = db.execute(query)
    return result.scalars().all()
