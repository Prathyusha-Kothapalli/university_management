from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.transcript import Transcript
from app.schemas.transcript import (
    TranscriptCreate,
    TranscriptUpdate,
    TranscriptResponse,
)


router = APIRouter(
    prefix="/transcripts",
    tags=["Transcripts"]
)


@router.post(
    "/",
    response_model=TranscriptResponse
)
def create_transcript(
    transcript_data: TranscriptCreate,
    db: Session = Depends(get_db)
):
    try:
        transcript = Transcript(
            **transcript_data.model_dump()
        )

        db.add(transcript)
        db.commit()
        db.refresh(transcript)

        return transcript

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get(
    "/",
    response_model=list[TranscriptResponse]
)
def get_transcripts(
    db: Session = Depends(get_db)
):
    result = db.execute(
        select(Transcript)
    )

    return result.scalars().all()


@router.get(
    "/{transcript_id}",
    response_model=TranscriptResponse
)
def get_transcript(
    transcript_id: UUID,
    db: Session = Depends(get_db)
):
    transcript = db.get(
        Transcript,
        transcript_id
    )

    if not transcript:
        raise HTTPException(
            status_code=404,
            detail="Transcript not found"
        )

    return transcript


@router.put(
    "/{transcript_id}",
    response_model=TranscriptResponse
)
def update_transcript(
    transcript_id: UUID,
    transcript_data: TranscriptUpdate,
    db: Session = Depends(get_db)
):
    transcript = db.get(
        Transcript,
        transcript_id
    )

    if not transcript:
        raise HTTPException(
            status_code=404,
            detail="Transcript not found"
        )

    try:
        update_data = transcript_data.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            if hasattr(transcript, key):
                setattr(
                    transcript,
                    key,
                    value
                )

        db.commit()
        db.refresh(transcript)

        return transcript

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.delete("/{transcript_id}")
def delete_transcript(
    transcript_id: UUID,
    db: Session = Depends(get_db)
):
    transcript = db.get(
        Transcript,
        transcript_id
    )

    if not transcript:
        raise HTTPException(
            status_code=404,
            detail="Transcript not found"
        )

    db.delete(transcript)
    db.commit()

    return {
        "message": "Transcript deleted successfully"
    }
