from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.ai_message import AIMessage
from app.schemas.ai_message import (
    AIMessageCreate,
    AIMessageUpdate,
    AIMessageResponse,
)


router = APIRouter(
    prefix="/ai-messages",
    tags=["AI Messages"]
)


@router.post(
    "/",
    response_model=AIMessageResponse
)
def create_ai_message(
    message_data: AIMessageCreate,
    db: Session = Depends(get_db)
):
    try:
        message = AIMessage(
            **message_data.model_dump()
        )

        db.add(message)
        db.commit()
        db.refresh(message)

        return message

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get(
    "/",
    response_model=list[AIMessageResponse]
)
def get_ai_messages(
    db: Session = Depends(get_db)
):
    result = db.execute(
        select(AIMessage)
    )

    return result.scalars().all()


@router.get(
    "/{message_id}",
    response_model=AIMessageResponse
)
def get_ai_message(
    message_id: UUID,
    db: Session = Depends(get_db)
):
    message = db.get(
        AIMessage,
        message_id
    )

    if not message:
        raise HTTPException(
            status_code=404,
            detail="AI message not found"
        )

    return message


@router.put(
    "/{message_id}",
    response_model=AIMessageResponse
)
def update_ai_message(
    message_id: UUID,
    message_data: AIMessageUpdate,
    db: Session = Depends(get_db)
):
    message = db.get(
        AIMessage,
        message_id
    )

    if not message:
        raise HTTPException(
            status_code=404,
            detail="AI message not found"
        )

    try:
        update_data = message_data.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            if hasattr(message, key):
                setattr(
                    message,
                    key,
                    value
                )

        db.commit()
        db.refresh(message)

        return message

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.delete("/{message_id}")
def delete_ai_message(
    message_id: UUID,
    db: Session = Depends(get_db)
):
    message = db.get(
        AIMessage,
        message_id
    )

    if not message:
        raise HTTPException(
            status_code=404,
            detail="AI message not found"
        )

    db.delete(message)
    db.commit()

    return {
        "message": "AI message deleted successfully"
    }
