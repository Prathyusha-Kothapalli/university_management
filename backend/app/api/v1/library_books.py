from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.library_book import LibraryBook
from app.schemas.library_book import (
    LibraryBookCreate,
    LibraryBookUpdate,
    LibraryBookResponse,
)


router = APIRouter(
    prefix="/library-books",
    tags=["Library Books"]
)


@router.post(
    "/",
    response_model=LibraryBookResponse
)
def create_library_book(
    book_data: LibraryBookCreate,
    db: Session = Depends(get_db)
):
    try:
        book = LibraryBook(
            **book_data.model_dump()
        )

        db.add(book)
        db.commit()
        db.refresh(book)

        return book

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get(
    "/",
    response_model=list[LibraryBookResponse]
)
def get_library_books(
    db: Session = Depends(get_db)
):
    result = db.execute(
        select(LibraryBook)
    )

    return result.scalars().all()


@router.get(
    "/{book_id}",
    response_model=LibraryBookResponse
)
def get_library_book(
    book_id: UUID,
    db: Session = Depends(get_db)
):
    book = db.get(
        LibraryBook,
        book_id
    )

    if not book:
        raise HTTPException(
            status_code=404,
            detail="Library book not found"
        )

    return book


@router.put(
    "/{book_id}",
    response_model=LibraryBookResponse
)
def update_library_book(
    book_id: UUID,
    book_data: LibraryBookUpdate,
    db: Session = Depends(get_db)
):
    book = db.get(
        LibraryBook,
        book_id
    )

    if not book:
        raise HTTPException(
            status_code=404,
            detail="Library book not found"
        )

    try:
        update_data = book_data.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            if hasattr(book, key):
                setattr(
                    book,
                    key,
                    value
                )

        db.commit()
        db.refresh(book)

        return book

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.delete("/{book_id}")
def delete_library_book(
    book_id: UUID,
    db: Session = Depends(get_db)
):
    book = db.get(
        LibraryBook,
        book_id
    )

    if not book:
        raise HTTPException(
            status_code=404,
            detail="Library book not found"
        )

    db.delete(book)
    db.commit()

    return {
        "message": "Library book deleted successfully"
    }
