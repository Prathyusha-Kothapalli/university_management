from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.program import Program
from app.schemas.program import (
    ProgramCreate,
    ProgramUpdate,
    ProgramResponse,
)


router = APIRouter(
    prefix="/programs",
    tags=["Programs"]
)


@router.post(
    "/",
    response_model=ProgramResponse
)
def create_program(
    program_data: ProgramCreate,
    db: Session = Depends(get_db)
):
    try:
        program = Program(
            **program_data.model_dump()
        )

        db.add(program)
        db.commit()
        db.refresh(program)

        return program

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get(
    "/",
    response_model=list[ProgramResponse]
)
def get_programs(
    db: Session = Depends(get_db)
):
    result = db.execute(
        select(Program)
    )

    return result.scalars().all()


@router.get(
    "/{program_id}",
    response_model=ProgramResponse
)
def get_program(
    program_id: UUID,
    db: Session = Depends(get_db)
):
    program = db.get(
        Program,
        program_id
    )

    if not program:
        raise HTTPException(
            status_code=404,
            detail="Program not found"
        )

    return program


@router.put(
    "/{program_id}",
    response_model=ProgramResponse
)
def update_program(
    program_id: UUID,
    program_data: ProgramUpdate,
    db: Session = Depends(get_db)
):
    program = db.get(
        Program,
        program_id
    )

    if not program:
        raise HTTPException(
            status_code=404,
            detail="Program not found"
        )

    try:
        update_data = program_data.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            if hasattr(program, key):
                setattr(
                    program,
                    key,
                    value
                )

        db.commit()
        db.refresh(program)

        return program

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.delete("/{program_id}")
def delete_program(
    program_id: UUID,
    db: Session = Depends(get_db)
):
    program = db.get(
        Program,
        program_id
    )

    if not program:
        raise HTTPException(
            status_code=404,
            detail="Program not found"
        )

    db.delete(program)
    db.commit()

    return {
        "message": "Program deleted successfully"
    }