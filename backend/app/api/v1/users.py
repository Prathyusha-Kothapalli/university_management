from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.user import User
from app.schemas.user import (
    UserCreate,
    UserUpdate,
    UserResponse,
)
from app.core.security import get_password_hash


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post(
    "/",
    response_model=UserResponse
)
def create_user(
    user_data: UserCreate,
    db: Session = Depends(get_db)
):
    try:
        user = User(
            full_name=user_data.full_name,
            email=user_data.email,
            password_hash=get_password_hash(
                user_data.password
            ),
            role_id=user_data.role_id,
            is_active=user_data.is_active,
        )

        db.add(user)
        db.commit()
        db.refresh(user)

        return user

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get(
    "/",
    response_model=list[UserResponse]
)
def get_users(
    db: Session = Depends(get_db)
):
    result = db.execute(
        select(User)
    )

    return result.scalars().all()


@router.get(
    "/{user_id}",
    response_model=UserResponse
)
def get_user(
    user_id: UUID,
    db: Session = Depends(get_db)
):
    user = db.get(User, user_id)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user


@router.put(
    "/{user_id}",
    response_model=UserResponse
)
def update_user(
    user_id: UUID,
    user_data: UserUpdate,
    db: Session = Depends(get_db)
):
    user = db.get(User, user_id)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    try:
        update_data = user_data.model_dump(
            exclude_unset=True
        )

        if "password" in update_data:
            user.password_hash = get_password_hash(
                update_data.pop("password")
            )

        for key, value in update_data.items():
            if hasattr(user, key):
                setattr(
                    user,
                    key,
                    value
                )

        db.commit()
        db.refresh(user)

        return user

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.delete("/{user_id}")
def delete_user(
    user_id: UUID,
    db: Session = Depends(get_db)
):
    user = db.get(User, user_id)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    db.delete(user)
    db.commit()

    return {
        "message": "User deleted successfully"
    }