from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.department import Department
from app.schemas.department import (
    DepartmentCreate,
    DepartmentUpdate,
    DepartmentResponse,
)


router = APIRouter(
    prefix="/departments",
    tags=["Departments"]
)


@router.post(
    "/",
    response_model=DepartmentResponse
)
def create_department(
    department_data: DepartmentCreate,
    db: Session = Depends(get_db)
):
    try:
        department = Department(
            **department_data.model_dump()
        )

        db.add(department)
        db.commit()
        db.refresh(department)

        return department

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get(
    "/",
    response_model=list[DepartmentResponse]
)
def get_departments(
    db: Session = Depends(get_db)
):
    result = db.execute(
        select(Department)
    )

    return result.scalars().all()


@router.get(
    "/{department_id}",
    response_model=DepartmentResponse
)
def get_department(
    department_id: UUID,
    db: Session = Depends(get_db)
):
    department = db.get(
        Department,
        department_id
    )

    if not department:
        raise HTTPException(
            status_code=404,
            detail="Department not found"
        )

    return department


@router.put(
    "/{department_id}",
    response_model=DepartmentResponse
)
def update_department(
    department_id: UUID,
    department_data: DepartmentUpdate,
    db: Session = Depends(get_db)
):
    department = db.get(
        Department,
        department_id
    )

    if not department:
        raise HTTPException(
            status_code=404,
            detail="Department not found"
        )

    try:
        update_data = department_data.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            if hasattr(department, key):
                setattr(
                    department,
                    key,
                    value
                )

        db.commit()
        db.refresh(department)

        return department

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.delete("/{department_id}")
def delete_department(
    department_id: UUID,
    db: Session = Depends(get_db)
):
    department = db.get(
        Department,
        department_id
    )

    if not department:
        raise HTTPException(
            status_code=404,
            detail="Department not found"
        )

    db.delete(department)
    db.commit()

    return {
        "message": "Department deleted successfully"
    }