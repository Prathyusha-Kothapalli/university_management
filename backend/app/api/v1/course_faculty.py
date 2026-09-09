from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.course_faculty import CourseFaculty
from app.schemas.course_faculty import (
    CourseFacultyCreate,
    CourseFacultyUpdate,
    CourseFacultyResponse,
)


router = APIRouter(
    prefix="/course-faculty",
    tags=["Course Faculty"]
)


@router.post(
    "/",
    response_model=CourseFacultyResponse
)
def create_course_faculty(
    faculty_data: CourseFacultyCreate,
    db: Session = Depends(get_db)
):
    try:
        course_faculty = CourseFaculty(
            **faculty_data.model_dump()
        )

        db.add(course_faculty)
        db.commit()
        db.refresh(course_faculty)

        return course_faculty

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get(
    "/",
    response_model=list[CourseFacultyResponse]
)
def get_course_faculty(
    db: Session = Depends(get_db)
):
    result = db.execute(
        select(CourseFaculty)
    )

    return result.scalars().all()


@router.get(
    "/{course_faculty_id}",
    response_model=CourseFacultyResponse
)
def get_course_faculty_by_id(
    course_faculty_id: UUID,
    db: Session = Depends(get_db)
):
    course_faculty = db.get(
        CourseFaculty,
        course_faculty_id
    )

    if not course_faculty:
        raise HTTPException(
            status_code=404,
            detail="Course faculty assignment not found"
        )

    return course_faculty


@router.put(
    "/{course_faculty_id}",
    response_model=CourseFacultyResponse
)
def update_course_faculty(
    course_faculty_id: UUID,
    faculty_data: CourseFacultyUpdate,
    db: Session = Depends(get_db)
):
    course_faculty = db.get(
        CourseFaculty,
        course_faculty_id
    )

    if not course_faculty:
        raise HTTPException(
            status_code=404,
            detail="Course faculty assignment not found"
        )

    try:
        update_data = faculty_data.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            if hasattr(course_faculty, key):
                setattr(
                    course_faculty,
                    key,
                    value
                )

        db.commit()
        db.refresh(course_faculty)

        return course_faculty

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.delete("/{course_faculty_id}")
def delete_course_faculty(
    course_faculty_id: UUID,
    db: Session = Depends(get_db)
):
    course_faculty = db.get(
        CourseFaculty,
        course_faculty_id
    )

    if not course_faculty:
        raise HTTPException(
            status_code=404,
            detail="Course faculty assignment not found"
        )

    db.delete(course_faculty)
    db.commit()

    return {
        "message": "Course faculty assignment deleted successfully"
    }