from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.hostel import Hostel
from app.schemas.hostel import (
    HostelCreate,
    HostelUpdate,
    HostelResponse,
)


router = APIRouter(
    prefix="/hostels",
    tags=["Hostels"]
)


@router.post(
    "/",
    response_model=HostelResponse
)
def create_hostel(
    hostel_data: HostelCreate,
    db: Session = Depends(get_db)
):
    try:
        hostel = Hostel(
            **hostel_data.model_dump()
        )

        db.add(hostel)
        db.commit()
        db.refresh(hostel)

        return hostel

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get(
    "/",
    response_model=list[HostelResponse]
)
def get_hostels(
    db: Session = Depends(get_db)
):
    result = db.execute(
        select(Hostel)
    )

    return result.scalars().all()


@router.get(
    "/{hostel_id}",
    response_model=HostelResponse
)
def get_hostel(
    hostel_id: UUID,
    db: Session = Depends(get_db)
):
    hostel = db.get(
        Hostel,
        hostel_id
    )

    if not hostel:
        raise HTTPException(
            status_code=404,
            detail="Hostel not found"
        )

    return hostel


@router.put(
    "/{hostel_id}",
    response_model=HostelResponse
)
def update_hostel(
    hostel_id: UUID,
    hostel_data: HostelUpdate,
    db: Session = Depends(get_db)
):
    hostel = db.get(
        Hostel,
        hostel_id
    )

    if not hostel:
        raise HTTPException(
            status_code=404,
            detail="Hostel not found"
        )

    try:
        update_data = hostel_data.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            if hasattr(hostel, key):
                setattr(
                    hostel,
                    key,
                    value
                )

        db.commit()
        db.refresh(hostel)

        return hostel

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.delete("/{hostel_id}")
def delete_hostel(
    hostel_id: UUID,
    db: Session = Depends(get_db)
):
    hostel = db.get(
        Hostel,
        hostel_id
    )

    if not hostel:
        raise HTTPException(
            status_code=404,
            detail="Hostel not found"
        )

    db.delete(hostel)
    db.commit()

    return {
        "message": "Hostel deleted successfully"
    }
