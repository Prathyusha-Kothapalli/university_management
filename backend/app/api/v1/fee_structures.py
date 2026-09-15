from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.fee_structure import FeeStructure
from app.schemas.fee_structure import (
    FeeStructureCreate,
    FeeStructureUpdate,
    FeeStructureResponse,
)


router = APIRouter(
    prefix="/fee-structures",
    tags=["Fee Structures"]
)


@router.post(
    "/",
    response_model=FeeStructureResponse
)
def create_fee_structure(
    fee_data: FeeStructureCreate,
    db: Session = Depends(get_db)
):
    try:
        fee_structure = FeeStructure(
            **fee_data.model_dump()
        )

        db.add(fee_structure)
        db.commit()
        db.refresh(fee_structure)

        return fee_structure

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get(
    "/",
    response_model=list[FeeStructureResponse]
)
def get_fee_structures(
    db: Session = Depends(get_db)
):
    result = db.execute(
        select(FeeStructure)
    )

    return result.scalars().all()


@router.get(
    "/{fee_structure_id}",
    response_model=FeeStructureResponse
)
def get_fee_structure(
    fee_structure_id: UUID,
    db: Session = Depends(get_db)
):
    fee_structure = db.get(
        FeeStructure,
        fee_structure_id
    )

    if not fee_structure:
        raise HTTPException(
            status_code=404,
            detail="Fee structure not found"
        )

    return fee_structure


@router.put(
    "/{fee_structure_id}",
    response_model=FeeStructureResponse
)
def update_fee_structure(
    fee_structure_id: UUID,
    fee_data: FeeStructureUpdate,
    db: Session = Depends(get_db)
):
    fee_structure = db.get(
        FeeStructure,
        fee_structure_id
    )

    if not fee_structure:
        raise HTTPException(
            status_code=404,
            detail="Fee structure not found"
        )

    try:
        update_data = fee_data.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            if hasattr(fee_structure, key):
                setattr(
                    fee_structure,
                    key,
                    value
                )

        db.commit()
        db.refresh(fee_structure)

        return fee_structure

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.delete("/{fee_structure_id}")
def delete_fee_structure(
    fee_structure_id: UUID,
    db: Session = Depends(get_db)
):
    fee_structure = db.get(
        FeeStructure,
        fee_structure_id
    )

    if not fee_structure:
        raise HTTPException(
            status_code=404,
            detail="Fee structure not found"
        )

    db.delete(fee_structure)
    db.commit()

    return {
        "message": "Fee structure deleted successfully"
    }
