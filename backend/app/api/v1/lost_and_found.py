from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.lost_and_found import LostItem, ItemClaim
from app.schemas.lost_and_found import (
    LostItemCreate,
    LostItemUpdate,
    LostItemResponse,
    ItemClaimCreate,
    ItemClaimUpdate,
    ItemClaimResponse,
)

router = APIRouter(
    prefix="/lost-and-found",
    tags=["Lost & Found Portal"]
)


# --- Lost Items ---
@router.post("/items", response_model=LostItemResponse, status_code=status.HTTP_201_CREATED)
def report_lost_item(
    item_in: LostItemCreate,
    db: Session = Depends(get_db)
):
    item = LostItem(**item_in.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


@router.get("/items", response_model=List[LostItemResponse])
def get_lost_items(
    category: str = None,
    status_filter: str = "OPEN",
    db: Session = Depends(get_db)
):
    query = select(LostItem)
    if status_filter:
        query = query.where(LostItem.status == status_filter)
    if category:
        query = query.where(LostItem.category == category)
    result = db.execute(query)
    return result.scalars().all()


@router.get("/items/{item_id}", response_model=LostItemResponse)
def get_lost_item(
    item_id: UUID,
    db: Session = Depends(get_db)
):
    item = db.get(LostItem, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Lost item record not found")
    return item


@router.patch("/items/{item_id}", response_model=LostItemResponse)
def update_lost_item(
    item_id: UUID,
    item_in: LostItemUpdate,
    db: Session = Depends(get_db)
):
    item = db.get(LostItem, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Lost item record not found")
    
    update_data = item_in.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(item, field, value)
        
    db.commit()
    db.refresh(item)
    return item


# --- Item Claims ---
@router.post("/claims", response_model=ItemClaimResponse, status_code=status.HTTP_201_CREATED)
def submit_item_claim(
    claim_in: ItemClaimCreate,
    db: Session = Depends(get_db)
):
    item = db.get(LostItem, claim_in.item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Target lost item not found")

    claim = ItemClaim(**claim_in.model_dump())
    db.add(claim)
    db.commit()
    db.refresh(claim)
    return claim


@router.get("/claims", response_model=List[ItemClaimResponse])
def get_item_claims(
    item_id: UUID = None,
    db: Session = Depends(get_db)
):
    query = select(ItemClaim)
    if item_id:
        query = query.where(ItemClaim.item_id == item_id)
    result = db.execute(query)
    return result.scalars().all()


@router.patch("/claims/{claim_id}", response_model=ItemClaimResponse)
def update_claim_status(
    claim_id: UUID,
    claim_in: ItemClaimUpdate,
    db: Session = Depends(get_db)
):
    claim = db.get(ItemClaim, claim_id)
    if not claim:
        raise HTTPException(status_code=404, detail="Claim record not found")
    
    update_data = claim_in.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(claim, field, value)
        
    db.commit()
    db.refresh(claim)
    return claim
