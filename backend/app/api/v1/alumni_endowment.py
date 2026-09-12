import uuid
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.api.v1.auth import get_current_user
from app.schemas.alumni_endowment import (
    AlumniProfileCreate,
    AlumniProfileResponse,
    EndowmentFundCreate,
    EndowmentFundResponse,
    DonationCreate,
    DonationResponse,
)
from app.services import alumni_endowment_service

router = APIRouter(prefix="/alumni-endowment", tags=["Alumni & Endowment Funds"])


@router.post("/profiles", response_model=AlumniProfileResponse, status_code=status.HTTP_201_CREATED)
def create_alumni_profile(
    data: AlumniProfileCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    """Register alumni career details and mentorship availability."""
    return alumni_endowment_service.create_alumni_profile(
        db=db,
        data=data,
    )


@router.post("/funds", response_model=EndowmentFundResponse, status_code=status.HTTP_201_CREATED)
def create_endowment_fund(
    data: EndowmentFundCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    """Establish institutional endowment or scholarship fund."""
    return alumni_endowment_service.create_endowment_fund(
        db=db,
        data=data,
    )


@router.post("/donations", response_model=DonationResponse, status_code=status.HTTP_201_CREATED)
def record_alumni_donation(
    data: DonationCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    """Record financial donation to endowment fund."""
    return alumni_endowment_service.record_donation(
        db=db,
        data=data,
    )
