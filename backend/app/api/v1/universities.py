from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.university import University
from app.schemas.university import (
    UniversityCreate,
    UniversityUpdate,
    UniversityResponse,
)


router = APIRouter(
    prefix="/universities",
    tags=["Universities"]
)


@router.post(
    "/",
    response_model=UniversityResponse
)
def create_university(
    university_data: UniversityCreate,
    db: Session = Depends(get_db)
):
    try:
        university = University(
            **university_data.model_dump()
        )

        db.add(university)
        db.commit()
        db.refresh(university)

        return university

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get(
    "/",
    response_model=list[UniversityResponse]
)
def get_universities(
    db: Session = Depends(get_db)
):
    result = db.execute(
        select(University)
    )

    return result.scalars().all()


@router.get(
    "/{university_id}",
    response_model=UniversityResponse
)
def get_university(
    university_id: UUID,
    db: Session = Depends(get_db)
):
    university = db.get(
        University,
        university_id
    )

    if not university:
        raise HTTPException(
            status_code=404,
            detail="University not found"
        )

    return university


@router.put(
    "/{university_id}",
    response_model=UniversityResponse
)
def update_university(
    university_id: UUID,
    university_data: UniversityUpdate,
    db: Session = Depends(get_db)
):
    university = db.get(
        University,
        university_id
    )

    if not university:
        raise HTTPException(
            status_code=404,
            detail="University not found"
        )

    try:
        update_data = university_data.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            if hasattr(university, key):
                setattr(
                    university,
                    key,
                    value
                )

        db.commit()
        db.refresh(university)

        return university

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.delete("/{university_id}")
def delete_university(
    university_id: UUID,
    db: Session = Depends(get_db)
):
    university = db.get(
        University,
        university_id
    )

    if not university:
        raise HTTPException(
            status_code=404,
            detail="University not found"
        )

    db.delete(university)
    db.commit()

    return {
        "message": "University deleted successfully"
    }