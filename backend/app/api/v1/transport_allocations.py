from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.transport_allocation import TransportAllocation
from app.schemas.transport_allocation import (
    TransportAllocationCreate,
    TransportAllocationUpdate,
    TransportAllocationResponse,
)


router = APIRouter(
    prefix="/transport-allocations",
    tags=["Transport Allocations"]
)


@router.post(
    "/",
    response_model=TransportAllocationResponse
)
def create_transport_allocation(
    allocation_data: TransportAllocationCreate,
    db: Session = Depends(get_db)
):
    try:
        allocation = TransportAllocation(
            **allocation_data.model_dump()
        )

        db.add(allocation)
        db.commit()
        db.refresh(allocation)

        return allocation

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get(
    "/",
    response_model=list[TransportAllocationResponse]
)
def get_transport_allocations(
    db: Session = Depends(get_db)
):
    result = db.execute(
        select(TransportAllocation)
    )

    return result.scalars().all()


@router.get(
    "/{allocation_id}",
    response_model=TransportAllocationResponse
)
def get_transport_allocation(
    allocation_id: UUID,
    db: Session = Depends(get_db)
):
    allocation = db.get(
        TransportAllocation,
        allocation_id
    )

    if not allocation:
        raise HTTPException(
            status_code=404,
            detail="Transport allocation record not found"
        )

    return allocation


@router.put(
    "/{allocation_id}",
    response_model=TransportAllocationResponse
)
def update_transport_allocation(
    allocation_id: UUID,
    allocation_data: TransportAllocationUpdate,
    db: Session = Depends(get_db)
):
    allocation = db.get(
        TransportAllocation,
        allocation_id
    )

    if not allocation:
        raise HTTPException(
            status_code=404,
            detail="Transport allocation record not found"
        )

    try:
        update_data = allocation_data.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            if hasattr(allocation, key):
                setattr(
                    allocation,
                    key,
                    value
                )

        db.commit()
        db.refresh(allocation)

        return allocation

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.delete("/{allocation_id}")
def delete_transport_allocation(
    allocation_id: UUID,
    db: Session = Depends(get_db)
):
    allocation = db.get(
        TransportAllocation,
        allocation_id
    )

    if not allocation:
        raise HTTPException(
            status_code=404,
            detail="Transport allocation record not found"
        )

    db.delete(allocation)
    db.commit()

    return {
        "message": "Transport allocation record deleted successfully"
    }
