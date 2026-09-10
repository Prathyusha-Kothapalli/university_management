from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.assignment import Assignment
from app.schemas.assignment import (
    AssignmentCreate,
    AssignmentUpdate,
    AssignmentResponse,
)


router = APIRouter(
    prefix="/assignments",
    tags=["Assignments"]
)


@router.post(
    "/",
    response_model=AssignmentResponse
)
def create_assignment(
    assignment_data: AssignmentCreate,
    db: Session = Depends(get_db)
):
    try:
        assignment = Assignment(
            **assignment_data.model_dump()
        )

        db.add(assignment)
        db.commit()
        db.refresh(assignment)

        return assignment

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get(
    "/",
    response_model=list[AssignmentResponse]
)
def get_assignments(
    db: Session = Depends(get_db)
):
    result = db.execute(
        select(Assignment)
    )

    return result.scalars().all()


@router.get(
    "/{assignment_id}",
    response_model=AssignmentResponse
)
def get_assignment(
    assignment_id: UUID,
    db: Session = Depends(get_db)
):
    assignment = db.get(
        Assignment,
        assignment_id
    )

    if not assignment:
        raise HTTPException(
            status_code=404,
            detail="Assignment not found"
        )

    return assignment


@router.put(
    "/{assignment_id}",
    response_model=AssignmentResponse
)
def update_assignment(
    assignment_id: UUID,
    assignment_data: AssignmentUpdate,
    db: Session = Depends(get_db)
):
    assignment = db.get(
        Assignment,
        assignment_id
    )

    if not assignment:
        raise HTTPException(
            status_code=404,
            detail="Assignment not found"
        )

    try:
        update_data = assignment_data.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            if hasattr(assignment, key):
                setattr(
                    assignment,
                    key,
                    value
                )

        db.commit()
        db.refresh(assignment)

        return assignment

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.delete("/{assignment_id}")
def delete_assignment(
    assignment_id: UUID,
    db: Session = Depends(get_db)
):
    assignment = db.get(
        Assignment,
        assignment_id
    )

    if not assignment:
        raise HTTPException(
            status_code=404,
            detail="Assignment not found"
        )

    db.delete(assignment)
    db.commit()

    return {
        "message": "Assignment deleted successfully"
    }
