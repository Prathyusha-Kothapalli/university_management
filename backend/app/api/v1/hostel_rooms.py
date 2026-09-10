from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.hostel_room import HostelRoom
from app.schemas.hostel_room import (
    HostelRoomCreate,
    HostelRoomUpdate,
    HostelRoomResponse,
)


router = APIRouter(
    prefix="/hostel-rooms",
    tags=["Hostel Rooms"]
)


@router.post(
    "/",
    response_model=HostelRoomResponse
)
def create_hostel_room(
    room_data: HostelRoomCreate,
    db: Session = Depends(get_db)
):
    try:
        room = HostelRoom(
            **room_data.model_dump()
        )

        db.add(room)
        db.commit()
        db.refresh(room)

        return room

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get(
    "/",
    response_model=list[HostelRoomResponse]
)
def get_hostel_rooms(
    db: Session = Depends(get_db)
):
    result = db.execute(
        select(HostelRoom)
    )

    return result.scalars().all()


@router.get(
    "/{room_id}",
    response_model=HostelRoomResponse
)
def get_hostel_room(
    room_id: UUID,
    db: Session = Depends(get_db)
):
    room = db.get(
        HostelRoom,
        room_id
    )

    if not room:
        raise HTTPException(
            status_code=404,
            detail="Hostel room not found"
        )

    return room


@router.put(
    "/{room_id}",
    response_model=HostelRoomResponse
)
def update_hostel_room(
    room_id: UUID,
    room_data: HostelRoomUpdate,
    db: Session = Depends(get_db)
):
    room = db.get(
        HostelRoom,
        room_id
    )

    if not room:
        raise HTTPException(
            status_code=404,
            detail="Hostel room not found"
        )

    try:
        update_data = room_data.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            if hasattr(room, key):
                setattr(
                    room,
                    key,
                    value
                )

        db.commit()
        db.refresh(room)

        return room

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.delete("/{room_id}")
def delete_hostel_room(
    room_id: UUID,
    db: Session = Depends(get_db)
):
    room = db.get(
        HostelRoom,
        room_id
    )

    if not room:
        raise HTTPException(
            status_code=404,
            detail="Hostel room not found"
        )

    db.delete(room)
    db.commit()

    return {
        "message": "Hostel room deleted successfully"
    }
