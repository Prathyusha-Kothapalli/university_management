from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.ai_conversation import AIConversation
from app.schemas.ai_conversation import (
    AIConversationCreate,
    AIConversationUpdate,
    AIConversationResponse,
)


router = APIRouter(
    prefix="/ai-conversations",
    tags=["AI Conversations"]
)


@router.post(
    "/",
    response_model=AIConversationResponse
)
def create_ai_conversation(
    conversation_data: AIConversationCreate,
    db: Session = Depends(get_db)
):
    try:
        conversation = AIConversation(
            **conversation_data.model_dump()
        )

        db.add(conversation)
        db.commit()
        db.refresh(conversation)

        return conversation

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get(
    "/",
    response_model=list[AIConversationResponse]
)
def get_ai_conversations(
    db: Session = Depends(get_db)
):
    result = db.execute(
        select(AIConversation)
    )

    return result.scalars().all()


@router.get(
    "/{conversation_id}",
    response_model=AIConversationResponse
)
def get_ai_conversation(
    conversation_id: UUID,
    db: Session = Depends(get_db)
):
    conversation = db.get(
        AIConversation,
        conversation_id
    )

    if not conversation:
        raise HTTPException(
            status_code=404,
            detail="AI conversation not found"
        )

    return conversation


@router.put(
    "/{conversation_id}",
    response_model=AIConversationResponse
)
def update_ai_conversation(
    conversation_id: UUID,
    conversation_data: AIConversationUpdate,
    db: Session = Depends(get_db)
):
    conversation = db.get(
        AIConversation,
        conversation_id
    )

    if not conversation:
        raise HTTPException(
            status_code=404,
            detail="AI conversation not found"
        )

    try:
        update_data = conversation_data.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            if hasattr(conversation, key):
                setattr(
                    conversation,
                    key,
                    value
                )

        db.commit()
        db.refresh(conversation)

        return conversation

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.delete("/{conversation_id}")
def delete_ai_conversation(
    conversation_id: UUID,
    db: Session = Depends(get_db)
):
    conversation = db.get(
        AIConversation,
        conversation_id
    )

    if not conversation:
        raise HTTPException(
            status_code=404,
            detail="AI conversation not found"
        )

    db.delete(conversation)
    db.commit()

    return {
        "message": "AI conversation deleted successfully"
    }
