from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.book_issue import BookIssue
from app.schemas.book_issue import (
    BookIssueCreate,
    BookIssueUpdate,
    BookIssueResponse,
)


router = APIRouter(
    prefix="/book-issues",
    tags=["Book Issues"]
)


@router.post(
    "/",
    response_model=BookIssueResponse
)
def create_book_issue(
    issue_data: BookIssueCreate,
    db: Session = Depends(get_db)
):
    try:
        book_issue = BookIssue(
            **issue_data.model_dump()
        )

        db.add(book_issue)
        db.commit()
        db.refresh(book_issue)

        return book_issue

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get(
    "/",
    response_model=list[BookIssueResponse]
)
def get_book_issues(
    db: Session = Depends(get_db)
):
    result = db.execute(
        select(BookIssue)
    )

    return result.scalars().all()


@router.get(
    "/{issue_id}",
    response_model=BookIssueResponse
)
def get_book_issue(
    issue_id: UUID,
    db: Session = Depends(get_db)
):
    book_issue = db.get(
        BookIssue,
        issue_id
    )

    if not book_issue:
        raise HTTPException(
            status_code=404,
            detail="Book issue record not found"
        )

    return book_issue


@router.put(
    "/{issue_id}",
    response_model=BookIssueResponse
)
def update_book_issue(
    issue_id: UUID,
    issue_data: BookIssueUpdate,
    db: Session = Depends(get_db)
):
    book_issue = db.get(
        BookIssue,
        issue_id
    )

    if not book_issue:
        raise HTTPException(
            status_code=404,
            detail="Book issue record not found"
        )

    try:
        update_data = issue_data.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            if hasattr(book_issue, key):
                setattr(
                    book_issue,
                    key,
                    value
                )

        db.commit()
        db.refresh(book_issue)

        return book_issue

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.delete("/{issue_id}")
def delete_book_issue(
    issue_id: UUID,
    db: Session = Depends(get_db)
):
    book_issue = db.get(
        BookIssue,
        issue_id
    )

    if not book_issue:
        raise HTTPException(
            status_code=404,
            detail="Book issue record not found"
        )

    db.delete(book_issue)
    db.commit()

    return {
        "message": "Book issue record deleted successfully"
    }
