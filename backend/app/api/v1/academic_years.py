from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.academic_year import AcademicYear
from app.schemas.academic_year import (
    AcademicYearCreate,
    AcademicYearUpdate,
    AcademicYearResponse,
)


router = APIRouter(
    prefix="/academic-years",
    tags=["Academic Years"]
)


@router.post(
    "/",
    response_model=AcademicYearResponse
)
def create_academic_year(
    academic_year_data: AcademicYearCreate,
    db: Session = Depends(get_db)
):
    try:
        academic_year = AcademicYear(
            **academic_year_data.model_dump()
        )

        db.add(academic_year)
        db.commit()
        db.refresh(academic_year)

        return academic_year

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get(
    "/",
    response_model=list[AcademicYearResponse]
)
def get_academic_years(
    db: Session = Depends(get_db)
):
    result = db.execute(
        select(AcademicYear)
    )

    return result.scalars().all()


@router.get(
    "/{academic_year_id}",
    response_model=AcademicYearResponse
)
def get_academic_year(
    academic_year_id: UUID,
    db: Session = Depends(get_db)
):
    academic_year = db.get(
        AcademicYear,
        academic_year_id
    )

    if not academic_year:
        raise HTTPException(
            status_code=404,
            detail="Academic year not found"
        )

    return academic_year


@router.put(
    "/{academic_year_id}",
    response_model=AcademicYearResponse
)
def update_academic_year(
    academic_year_id: UUID,
    academic_year_data: AcademicYearUpdate,
    db: Session = Depends(get_db)
):
    academic_year = db.get(
        AcademicYear,
        academic_year_id
    )

    if not academic_year:
        raise HTTPException(
            status_code=404,
            detail="Academic year not found"
        )

    try:
        update_data = academic_year_data.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            if hasattr(academic_year, key):
                setattr(
                    academic_year,
                    key,
                    value
                )

        db.commit()
        db.refresh(academic_year)

        return academic_year

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.delete("/{academic_year_id}")
def delete_academic_year(
    academic_year_id: UUID,
    db: Session = Depends(get_db)
):
    academic_year = db.get(
        AcademicYear,
        academic_year_id
    )

    if not academic_year:
        raise HTTPException(
            status_code=404,
            detail="Academic year not found"
        )

    db.delete(academic_year)
    db.commit()

    return {
        "message": "Academic year deleted successfully"
    }