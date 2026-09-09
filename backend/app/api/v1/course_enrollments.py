from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.course_enrollment import CourseEnrollment
from app.schemas.course_enrollment import (
    CourseEnrollmentCreate,
    CourseEnrollmentUpdate,
    CourseEnrollmentResponse,
)


router = APIRouter(
    prefix="/course-enrollments",
    tags=["Course Enrollments"]
)


@router.post(
    "/",
    response_model=CourseEnrollmentResponse
)
def create_course_enrollment(
    enrollment_data: CourseEnrollmentCreate,
    db: Session = Depends(get_db)
):
    try:
        enrollment = CourseEnrollment(
            **enrollment_data.model_dump()
        )

        db.add(enrollment)
        db.commit()
        db.refresh(enrollment)

        return enrollment

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get(
    "/",
    response_model=list[CourseEnrollmentResponse]
)
def get_course_enrollments(
    db: Session = Depends(get_db)
):
    result = db.execute(
        select(CourseEnrollment)
    )

    return result.scalars().all()


@router.get(
    "/{enrollment_id}",
    response_model=CourseEnrollmentResponse
)
def get_course_enrollment(
    enrollment_id: UUID,
    db: Session = Depends(get_db)
):
    enrollment = db.get(
        CourseEnrollment,
        enrollment_id
    )

    if not enrollment:
        raise HTTPException(
            status_code=404,
            detail="Course enrollment not found"
        )

    return enrollment


@router.put(
    "/{enrollment_id}",
    response_model=CourseEnrollmentResponse
)
def update_course_enrollment(
    enrollment_id: UUID,
    enrollment_data: CourseEnrollmentUpdate,
    db: Session = Depends(get_db)
):
    enrollment = db.get(
        CourseEnrollment,
        enrollment_id
    )

    if not enrollment:
        raise HTTPException(
            status_code=404,
            detail="Course enrollment not found"
        )

    try:
        update_data = enrollment_data.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            if hasattr(enrollment, key):
                setattr(
                    enrollment,
                    key,
                    value
                )

        db.commit()
        db.refresh(enrollment)

        return enrollment

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.delete("/{enrollment_id}")
def delete_course_enrollment(
    enrollment_id: UUID,
    db: Session = Depends(get_db)
):
    enrollment = db.get(
        CourseEnrollment,
        enrollment_id
    )

    if not enrollment:
        raise HTTPException(
            status_code=404,
            detail="Course enrollment not found"
        )

    db.delete(enrollment)
    db.commit()

    return {
        "message": "Course enrollment deleted successfully"
    }