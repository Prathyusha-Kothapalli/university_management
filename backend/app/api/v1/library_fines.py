from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.library_fine import LibraryFine
from app.schemas.library_fine import (
    LibraryFineCreate,
    LibraryFineUpdate,
    LibraryFineResponse,
)


router = APIRouter(
    prefix="/library-fines",
    tags=["Library Fines"]
)


@router.post(
    "/",
    response_model=LibraryFineResponse
)
def create_library_fine(
    fine_data: LibraryFineCreate,
    db: Session = Depends(get_db)
):
    try:
        fine = LibraryFine(
            **fine_data.model_dump()
        )

        db.add(fine)
        db.commit()
        db.refresh(fine)

        return fine

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get(
    "/",
    response_model=list[LibraryFineResponse]
)
def get_library_fines(
    db: Session = Depends(get_db)
):
    result = db.execute(
        select(LibraryFine)
    )

    return result.scalars().all()


@router.get(
    "/{fine_id}",
    response_model=LibraryFineResponse
)
def get_library_fine(
    fine_id: UUID,
    db: Session = Depends(get_db)
):
    fine = db.get(
        LibraryFine,
        fine_id
    )

    if not fine:
        raise HTTPException(
            status_code=404,
            detail="Library fine not found"
        )

    return fine


@router.put(
    "/{fine_id}",
    response_model=LibraryFineResponse
)
def update_library_fine(
    fine_id: UUID,
    fine_data: LibraryFineUpdate,
    db: Session = Depends(get_db)
):
    fine = db.get(
        LibraryFine,
        fine_id
    )

    if not fine:
        raise HTTPException(
            status_code=404,
            detail="Library fine not found"
        )

    try:
        update_data = fine_data.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            if hasattr(fine, key):
                setattr(
                    fine,
                    key,
                    value
                )

        db.commit()
        db.refresh(fine)

        return fine

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.delete("/{fine_id}")
def delete_library_fine(
    fine_id: UUID,
    db: Session = Depends(get_db)
):
    fine = db.get(
        LibraryFine,
        fine_id
    )

    if not fine:
        raise HTTPException(
            status_code=404,
            detail="Library fine not found"
        )

    db.delete(fine)
    db.commit()

    return {
        "message": "Library fine deleted successfully"
    }
