from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.transport_route import TransportRoute
from app.schemas.transport_route import (
    TransportRouteCreate,
    TransportRouteUpdate,
    TransportRouteResponse,
)


router = APIRouter(
    prefix="/transport-routes",
    tags=["Transport Routes"]
)


@router.post(
    "/",
    response_model=TransportRouteResponse
)
def create_transport_route(
    route_data: TransportRouteCreate,
    db: Session = Depends(get_db)
):
    try:
        route = TransportRoute(
            **route_data.model_dump()
        )

        db.add(route)
        db.commit()
        db.refresh(route)

        return route

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.get(
    "/",
    response_model=list[TransportRouteResponse]
)
def get_transport_routes(
    db: Session = Depends(get_db)
):
    result = db.execute(
        select(TransportRoute)
    )

    return result.scalars().all()


@router.get(
    "/{route_id}",
    response_model=TransportRouteResponse
)
def get_transport_route(
    route_id: UUID,
    db: Session = Depends(get_db)
):
    route = db.get(
        TransportRoute,
        route_id
    )

    if not route:
        raise HTTPException(
            status_code=404,
            detail="Transport route not found"
        )

    return route


@router.put(
    "/{route_id}",
    response_model=TransportRouteResponse
)
def update_transport_route(
    route_id: UUID,
    route_data: TransportRouteUpdate,
    db: Session = Depends(get_db)
):
    route = db.get(
        TransportRoute,
        route_id
    )

    if not route:
        raise HTTPException(
            status_code=404,
            detail="Transport route not found"
        )

    try:
        update_data = route_data.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            if hasattr(route, key):
                setattr(
                    route,
                    key,
                    value
                )

        db.commit()
        db.refresh(route)

        return route

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.delete("/{route_id}")
def delete_transport_route(
    route_id: UUID,
    db: Session = Depends(get_db)
):
    route = db.get(
        TransportRoute,
        route_id
    )

    if not route:
        raise HTTPException(
            status_code=404,
            detail="Transport route not found"
        )

    db.delete(route)
    db.commit()

    return {
        "message": "Transport route deleted successfully"
    }
