import uuid
from datetime import datetime, timedelta
from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.digital_id_card import DigitalIdCard
from app.models.campus_access_log import CampusAccessLog
from app.services.identity_service import generate_live_digital_id_qr, verify_public_digital_id


class AccessScanRequest(BaseModel):
    card_number: str
    user_id: uuid.UUID
    gate_name: str = "Main Gate Turnstile 1"
    access_type: str = "ENTRY"


router = APIRouter(
    prefix="/digital-ids",
    tags=["Digital Identity"]
)


@router.get("/card/{user_id}")
def get_user_digital_id(user_id: uuid.UUID, db: Session = Depends(get_db)):
    card = db.execute(
        select(DigitalIdCard).where(DigitalIdCard.user_id == user_id)
    ).scalar_one_or_none()

    if not card:
        card_num = f"US-ID-2026-{str(user_id)[:6].upper()}"
        card = DigitalIdCard(
            user_id=user_id,
            card_number=card_num,
            role_name="STUDENT",
            status="ACTIVE",
            expiry_date=datetime.utcnow() + timedelta(days=730),
            qr_seed=str(uuid.uuid4())
        )
        db.add(card)
        db.commit()
        db.refresh(card)

    live_qr = generate_live_digital_id_qr(card.card_number, str(user_id))
    return {
        "card_id": str(card.id),
        "user_id": str(user_id),
        "card_number": card.card_number,
        "role_name": card.role_name,
        "status": card.status,
        "expiry_date": card.expiry_date.isoformat(),
        "live_qr": live_qr
    }


@router.post("/scan-access")
def record_campus_access_gate_scan(data: AccessScanRequest, db: Session = Depends(get_db)):
    access_entry = CampusAccessLog(
        card_number=data.card_number,
        user_id=data.user_id,
        gate_name=data.gate_name,
        access_type=data.access_type,
        status="GRANTED"
    )
    db.add(access_entry)
    db.commit()
    return {"message": "Access granted", "access_log_id": str(access_entry.id), "status": "GRANTED"}


@router.get("/verify/{card_number}")
def public_verify_id_card(card_number: str):
    res = verify_public_digital_id(card_number)
    return res
