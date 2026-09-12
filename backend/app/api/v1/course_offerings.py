from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.course_offering import CourseOffering
from app.schemas.course_offering import (
    CourseOfferingCreate,
    CourseOfferingUpdate,
    CourseOfferingResponse,
)


router = APIRouter(
    prefix="/course-offerings",
    tags=["Course Offerings"]
)


@router.post(
    "/",
    response_model=CourseOfferingResponse
)
def create_course_offering(
    offering_data: CourseOfferingCreate,
    db: Session = Depends(get_db)
):
    try:
        offering = CourseOffering(
            **offering_data.model_dump()
        )

        db.add(offering)
        db.commit()
        db.refresh(offering)

        return offering

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get(
    "/",
    response_model=list[CourseOfferingResponse]
)
def get_course_offerings(
    db: Session = Depends(get_db)
):
    result = db.execute(
        select(CourseOffering)
    )

    return result.scalars().all()


@router.get(
    "/{offering_id}",
    response_model=CourseOfferingResponse
)
def get_course_offering(
    offering_id: UUID,
    db: Session = Depends(get_db)
):
    offering = db.get(
        CourseOffering,
        offering_id
    )

    if not offering:
        raise HTTPException(
            status_code=404,
            detail="Course offering not found"
        )

    return offering


@router.put(
    "/{offering_id}",
    response_model=CourseOfferingResponse
)
def update_course_offering(
    offering_id: UUID,
    offering_data: CourseOfferingUpdate,
    db: Session = Depends(get_db)
):
    offering = db.get(
        CourseOffering,
        offering_id
    )

    if not offering:
        raise HTTPException(
            status_code=404,
            detail="Course offering not found"
        )

    try:
        update_data = offering_data.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            if hasattr(offering, key):
                setattr(
                    offering,
                    key,
                    value
                )

        db.commit()
        db.refresh(offering)

        return offering

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.delete("/{offering_id}")
def delete_course_offering(
    offering_id: UUID,
    db: Session = Depends(get_db)
):
    offering = db.get(
        CourseOffering,
        offering_id
    )

    if not offering:
        raise HTTPException(
            status_code=404,
            detail="Course offering not found"
        )

    db.delete(offering)
    db.commit()

    return {
        "message": "Course offering deleted successfully"
    }