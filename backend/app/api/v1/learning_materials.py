from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.learning_material import LearningMaterial
from app.schemas.learning_material import (
    LearningMaterialCreate,
    LearningMaterialUpdate,
    LearningMaterialResponse,
)


router = APIRouter(
    prefix="/learning-materials",
    tags=["Learning Materials"]
)


@router.post(
    "/",
    response_model=LearningMaterialResponse
)
def create_learning_material(
    material_data: LearningMaterialCreate,
    db: Session = Depends(get_db)
):
    try:
        material = LearningMaterial(
            **material_data.model_dump()
        )

        db.add(material)
        db.commit()
        db.refresh(material)

        return material

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get(
    "/",
    response_model=list[LearningMaterialResponse]
)
def get_learning_materials(
    db: Session = Depends(get_db)
):
    result = db.execute(
        select(LearningMaterial)
    )

    return result.scalars().all()


@router.get(
    "/{material_id}",
    response_model=LearningMaterialResponse
)
def get_learning_material(
    material_id: UUID,
    db: Session = Depends(get_db)
):
    material = db.get(
        LearningMaterial,
        material_id
    )

    if not material:
        raise HTTPException(
            status_code=404,
            detail="Learning material not found"
        )

    return material


@router.put(
    "/{material_id}",
    response_model=LearningMaterialResponse
)
def update_learning_material(
    material_id: UUID,
    material_data: LearningMaterialUpdate,
    db: Session = Depends(get_db)
):
    material = db.get(
        LearningMaterial,
        material_id
    )

    if not material:
        raise HTTPException(
            status_code=404,
            detail="Learning material not found"
        )

    try:
        update_data = material_data.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            if hasattr(material, key):
                setattr(
                    material,
                    key,
                    value
                )

        db.commit()
        db.refresh(material)

        return material

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.delete("/{material_id}")
def delete_learning_material(
    material_id: UUID,
    db: Session = Depends(get_db)
):
    material = db.get(
        LearningMaterial,
        material_id
    )

    if not material:
        raise HTTPException(
            status_code=404,
            detail="Learning material not found"
        )

    db.delete(material)
    db.commit()

    return {
        "message": "Learning material deleted successfully"
    }
