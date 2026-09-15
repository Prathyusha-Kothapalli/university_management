from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.role import Role
from app.schemas.role import (
    RoleCreate,
    RoleUpdate,
    RoleResponse,
)


router = APIRouter(
    prefix="/roles",
    tags=["Roles"]
)


@router.post(
    "/",
    response_model=RoleResponse
)
def create_role(
    role_data: RoleCreate,
    db: Session = Depends(get_db)
):
    try:
        role = Role(
            **role_data.model_dump()
        )

        db.add(role)
        db.commit()
        db.refresh(role)

        return role

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get(
    "/",
    response_model=list[RoleResponse]
)
def get_roles(
    db: Session = Depends(get_db)
):
    result = db.execute(
        select(Role)
    )

    return result.scalars().all()


@router.get(
    "/{role_id}",
    response_model=RoleResponse
)
def get_role(
    role_id: UUID,
    db: Session = Depends(get_db)
):
    role = db.get(Role, role_id)

    if not role:
        raise HTTPException(
            status_code=404,
            detail="Role not found"
        )

    return role


@router.put(
    "/{role_id}",
    response_model=RoleResponse
)
def update_role(
    role_id: UUID,
    role_data: RoleUpdate,
    db: Session = Depends(get_db)
):
    role = db.get(Role, role_id)

    if not role:
        raise HTTPException(
            status_code=404,
            detail="Role not found"
        )

    try:
        update_data = role_data.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            if hasattr(role, key):
                setattr(
                    role,
                    key,
                    value
                )

        db.commit()
        db.refresh(role)

        return role

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.delete("/{role_id}")
def delete_role(
    role_id: UUID,
    db: Session = Depends(get_db)
):
    role = db.get(Role, role_id)

    if not role:
        raise HTTPException(
            status_code=404,
            detail="Role not found"
        )

    db.delete(role)
    db.commit()

    return {
        "message": "Role deleted successfully"
    }