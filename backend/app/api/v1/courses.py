from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.course import Course
from app.schemas.course import (
    CourseCreate,
    CourseUpdate,
    CourseResponse,
)


router = APIRouter(
    prefix="/courses",
    tags=["Courses"]
)


@router.post(
    "/",
    response_model=CourseResponse
)
def create_course(
    course_data: CourseCreate,
    db: Session = Depends(get_db)
):
    try:
        course = Course(
            **course_data.model_dump()
        )

        db.add(course)
        db.commit()
        db.refresh(course)

        return course

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get(
    "/",
    response_model=list[CourseResponse]
)
def get_courses(
    db: Session = Depends(get_db)
):
    result = db.execute(
        select(Course)
    )

    return result.scalars().all()


@router.get(
    "/{course_id}",
    response_model=CourseResponse
)
def get_course(
    course_id: UUID,
    db: Session = Depends(get_db)
):
    course = db.get(
        Course,
        course_id
    )

    if not course:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    return course


@router.put(
    "/{course_id}",
    response_model=CourseResponse
)
def update_course(
    course_id: UUID,
    course_data: CourseUpdate,
    db: Session = Depends(get_db)
):
    course = db.get(
        Course,
        course_id
    )

    if not course:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    try:
        update_data = course_data.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            if hasattr(course, key):
                setattr(
                    course,
                    key,
                    value
                )

        db.commit()
        db.refresh(course)

        return course

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.delete("/{course_id}")
def delete_course(
    course_id: UUID,
    db: Session = Depends(get_db)
):
    course = db.get(
        Course,
        course_id
    )

    if not course:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    db.delete(course)
    db.commit()

    return {
        "message": "Course deleted successfully"
    }