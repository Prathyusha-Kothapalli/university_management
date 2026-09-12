from sqlalchemy.orm import Session

from app.models.user import User
from app.repositories.user_repository import (
    create_user,
    get_user_by_email,
)


def create_new_user(
    db: Session,
    full_name: str,
    email: str,
    password_hash: str,
    role_id,
) -> User:

    existing_user = get_user_by_email(
        db,
        email,
    )

    if existing_user:
        raise ValueError("User with this email already exists")

    user = User(
        full_name=full_name,
        email=email,
        password_hash=password_hash,
        role_id=role_id,
    )

    return create_user(db, user)