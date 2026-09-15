from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.hostel_allocation import HostelAllocation
from app.schemas.hostel_allocation import (
    HostelAllocationCreate,
    HostelAllocationUpdate,
    HostelAllocationResponse,
)


router = APIRouter(
    prefix="/hostel-allocations",
    tags=["Hostel Allocations"]
)


@router.post(
    "/",
    response_model=HostelAllocationResponse
)
def create_hostel_allocation(
    allocation_data: HostelAllocationCreate,
    db: Session = Depends(get_db)
):
    try:
        allocation = HostelAllocation(
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
    response_model=list[HostelAllocationResponse]
)
def get_hostel_allocations(
    db: Session = Depends(get_db)
):
    result = db.execute(
        select(HostelAllocation)
    )

    return result.scalars().all()


@router.get(
    "/{allocation_id}",
    response_model=HostelAllocationResponse
)
def get_hostel_allocation(
    allocation_id: UUID,
    db: Session = Depends(get_db)
):
    allocation = db.get(
        HostelAllocation,
        allocation_id
    )

    if not allocation:
        raise HTTPException(
            status_code=404,
            detail="Hostel allocation record not found"
        )

    return allocation


@router.put(
    "/{allocation_id}",
    response_model=HostelAllocationResponse
)
def update_hostel_allocation(
    allocation_id: UUID,
    allocation_data: HostelAllocationUpdate,
    db: Session = Depends(get_db)
):
    allocation = db.get(
        HostelAllocation,
        allocation_id
    )

    if not allocation:
        raise HTTPException(
            status_code=404,
            detail="Hostel allocation record not found"
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
def delete_hostel_allocation(
    allocation_id: UUID,
    db: Session = Depends(get_db)
):
    allocation = db.get(
        HostelAllocation,
        allocation_id
    )

    if not allocation:
        raise HTTPException(
            status_code=404,
            detail="Hostel allocation record not found"
        )

    db.delete(allocation)
    db.commit()

    return {
        "message": "Hostel allocation record deleted successfully"
    }
