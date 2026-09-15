from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.document import Document
from app.schemas.document import (
    DocumentCreate,
    DocumentUpdate,
    DocumentResponse,
)


router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)


@router.post(
    "/",
    response_model=DocumentResponse
)
def create_document(
    document_data: DocumentCreate,
    db: Session = Depends(get_db)
):
    try:
        document = Document(
            **document_data.model_dump()
        )

        db.add(document)
        db.commit()
        db.refresh(document)

        return document

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get(
    "/",
    response_model=list[DocumentResponse]
)
def get_documents(
    db: Session = Depends(get_db)
):
    result = db.execute(
        select(Document)
    )

    return result.scalars().all()


@router.get(
    "/{document_id}",
    response_model=DocumentResponse
)
def get_document(
    document_id: UUID,
    db: Session = Depends(get_db)
):
    document = db.get(
        Document,
        document_id
    )

    if not document:
        raise HTTPException(
            status_code=404,
            detail="Document not found"
        )

    return document


@router.put(
    "/{document_id}",
    response_model=DocumentResponse
)
def update_document(
    document_id: UUID,
    document_data: DocumentUpdate,
    db: Session = Depends(get_db)
):
    document = db.get(
        Document,
        document_id
    )

    if not document:
        raise HTTPException(
            status_code=404,
            detail="Document not found"
        )

    try:
        update_data = document_data.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            if hasattr(document, key):
                setattr(
                    document,
                    key,
                    value
                )

        db.commit()
        db.refresh(document)

        return document

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.delete("/{document_id}")
def delete_document(
    document_id: UUID,
    db: Session = Depends(get_db)
):
    document = db.get(
        Document,
        document_id
    )

    if not document:
        raise HTTPException(
            status_code=404,
            detail="Document not found"
        )

    db.delete(document)
    db.commit()

    return {
        "message": "Document deleted successfully"
    }
