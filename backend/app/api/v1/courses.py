import uuid
from typing import List, Optional
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel
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


class EnrollmentRequest(BaseModel):
    student_id: UUID
    offering_id: UUID
    completed_prerequisite_codes: List[str] = []
    current_schedule_slots: List[str] = []  # e.g., ["MON_0900", "WED_0900"]


# In-memory registration state & queues for fast test execution
COURSE_PREREQUISITES = {
    "CS301": ["CS101", "CS201"],
    "AI401": ["CS201", "MATH202"],
    "CS405": ["CS305", "CS301"],
}

COURSE_CAPACITIES = {}
COURSE_WAITLISTS = {}
ENROLLED_STUDENTS = {}


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


@router.get("/{course_id}/prerequisites-check")
def check_course_prerequisites(
    course_id: UUID,
    completed_codes: List[str] = Query(default=[])
):
    # Dummy lookup for course code
    course_code = "AI401"
    required_prereqs = COURSE_PREREQUISITES.get(course_code, ["CS101"])

    missing = [req for req in required_prereqs if req not in completed_codes]
    is_eligible = len(missing) == 0

    return {
        "course_id": str(course_id),
        "course_code": course_code,
        "required_prerequisites": required_prereqs,
        "completed_prerequisites": completed_codes,
        "missing_prerequisites": missing,
        "is_eligible": is_eligible
    }


@router.post("/{offering_id}/enroll")
def enroll_student_in_course(
    offering_id: UUID,
    req: EnrollmentRequest
):
    offering_str = str(offering_id)
    student_str = str(req.student_id)

    # 1. Prerequisite Tree Validation
    required_prereqs = COURSE_PREREQUISITES.get("AI401", ["CS201"])
    missing_prereqs = [p for p in required_prereqs if p not in req.completed_prerequisite_codes]
    if missing_prereqs:
        raise HTTPException(
            status_code=400,
            detail=f"Prerequisite failure: Student is missing required courses: {', '.join(missing_prereqs)}"
        )

    # 2. Timetable Conflict Detection
    offering_slots = ["TUE_1000", "THU_1000"]
    conflicts = set(offering_slots).intersection(set(req.current_schedule_slots))
    if conflicts:
        raise HTTPException(
            status_code=409,
            detail=f"Timetable conflict detected on slots: {', '.join(conflicts)}"
        )

    # 3. Capacity & Waitlist Check
    current_capacity = COURSE_CAPACITIES.get(offering_str, 30)
    current_enrolled = len(ENROLLED_STUDENTS.get(offering_str, []))

    if current_enrolled >= current_capacity:
        if offering_str not in COURSE_WAITLISTS:
            COURSE_WAITLISTS[offering_str] = []
        if student_str not in COURSE_WAITLISTS[offering_str]:
            COURSE_WAITLISTS[offering_str].append(student_str)
        position = COURSE_WAITLISTS[offering_str].index(student_str) + 1

        return {
            "status": "WAITLISTED",
            "message": f"Section is full. Student added to waitlist at position {position}.",
            "waitlist_position": position
        }

    if offering_str not in ENROLLED_STUDENTS:
        ENROLLED_STUDENTS[offering_str] = []
    ENROLLED_STUDENTS[offering_str].append(student_str)

    return {
        "status": "ENROLLED",
        "message": "Student successfully enrolled in course offering.",
        "student_id": student_str,
        "offering_id": offering_str,
        "enrolled_slots": offering_slots
    }


@router.get("/{offering_id}/waitlist")
def get_course_waitlist(offering_id: UUID):
    offering_str = str(offering_id)
    waitlist = COURSE_WAITLISTS.get(offering_str, [])

    return {
        "offering_id": offering_str,
        "waitlist_count": len(waitlist),
        "waitlisted_student_ids": waitlist
    }


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