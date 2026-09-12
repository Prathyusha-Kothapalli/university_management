from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.notification import Notification
from app.schemas.notification import (
    NotificationCreate,
    NotificationUpdate,
    NotificationResponse,
)


router = APIRouter(
    prefix="/notifications",
    tags=["Notifications"]
)


@router.post(
    "/",
    response_model=NotificationResponse
)
def create_notification(
    notification_data: NotificationCreate,
    db: Session = Depends(get_db)
):
    try:
        notification = Notification(
            **notification_data.model_dump()
        )

        db.add(notification)
        db.commit()
        db.refresh(notification)

        return notification

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get(
    "/",
    response_model=list[NotificationResponse]
)
def get_notifications(
    db: Session = Depends(get_db)
):
    result = db.execute(
        select(Notification)
    )

    return result.scalars().all()


@router.get(
    "/{notification_id}",
    response_model=NotificationResponse
)
def get_notification(
    notification_id: UUID,
    db: Session = Depends(get_db)
):
    notification = db.get(
        Notification,
        notification_id
    )

    if not notification:
        raise HTTPException(
            status_code=404,
            detail="Notification not found"
        )

    return notification


@router.put(
    "/{notification_id}",
    response_model=NotificationResponse
)
def update_notification(
    notification_id: UUID,
    notification_data: NotificationUpdate,
    db: Session = Depends(get_db)
):
    notification = db.get(
        Notification,
        notification_id
    )

    if not notification:
        raise HTTPException(
            status_code=404,
            detail="Notification not found"
        )

    try:
        update_data = notification_data.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            if hasattr(notification, key):
                setattr(
                    notification,
                    key,
                    value
                )

        db.commit()
        db.refresh(notification)

        return notification

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.delete("/{notification_id}")
def delete_notification(
    notification_id: UUID,
    db: Session = Depends(get_db)
):
    notification = db.get(
        Notification,
        notification_id
    )

    if not notification:
        raise HTTPException(
            status_code=404,
            detail="Notification not found"
        )

    db.delete(notification)
    db.commit()

    return {
        "message": "Notification deleted successfully"
    }
