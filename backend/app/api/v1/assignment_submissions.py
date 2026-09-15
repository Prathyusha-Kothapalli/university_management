from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.assignment_submission import AssignmentSubmission
from app.schemas.assignment_submission import (
    AssignmentSubmissionCreate,
    AssignmentSubmissionUpdate,
    AssignmentSubmissionResponse,
)


router = APIRouter(
    prefix="/assignment-submissions",
    tags=["Assignment Submissions"]
)


@router.post(
    "/",
    response_model=AssignmentSubmissionResponse
)
def create_assignment_submission(
    submission_data: AssignmentSubmissionCreate,
    db: Session = Depends(get_db)
):
    try:
        submission = AssignmentSubmission(
            **submission_data.model_dump()
        )

        db.add(submission)
        db.commit()
        db.refresh(submission)

        return submission

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get(
    "/",
    response_model=list[AssignmentSubmissionResponse]
)
def get_assignment_submissions(
    db: Session = Depends(get_db)
):
    result = db.execute(
        select(AssignmentSubmission)
    )

    return result.scalars().all()


@router.get(
    "/{submission_id}",
    response_model=AssignmentSubmissionResponse
)
def get_assignment_submission(
    submission_id: UUID,
    db: Session = Depends(get_db)
):
    submission = db.get(
        AssignmentSubmission,
        submission_id
    )

    if not submission:
        raise HTTPException(
            status_code=404,
            detail="Assignment submission not found"
        )

    return submission


@router.put(
    "/{submission_id}",
    response_model=AssignmentSubmissionResponse
)
def update_assignment_submission(
    submission_id: UUID,
    submission_data: AssignmentSubmissionUpdate,
    db: Session = Depends(get_db)
):
    submission = db.get(
        AssignmentSubmission,
        submission_id
    )

    if not submission:
        raise HTTPException(
            status_code=404,
            detail="Assignment submission not found"
        )

    try:
        update_data = submission_data.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            if hasattr(submission, key):
                setattr(
                    submission,
                    key,
                    value
                )

        db.commit()
        db.refresh(submission)

        return submission

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.delete("/{submission_id}")
def delete_assignment_submission(
    submission_id: UUID,
    db: Session = Depends(get_db)
):
    submission = db.get(
        AssignmentSubmission,
        submission_id
    )

    if not submission:
        raise HTTPException(
            status_code=404,
            detail="Assignment submission not found"
        )

    db.delete(submission)
    db.commit()

    return {
        "message": "Assignment submission deleted successfully"
    }
