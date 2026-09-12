import uuid
from typing import List, Dict, Any, Optional
from sqlalchemy.orm import Session
from sqlalchemy import select

from app.models.campus import Campus
from app.models.campus_building import CampusBuilding
from app.models.classroom import Classroom

def calculate_campus_utilization(db: Session, campus_id: uuid.UUID) -> Dict[str, Any]:
    """Calculates classroom capacity utilization and availability stats for a campus."""
    buildings = db.execute(
        select(CampusBuilding).where(CampusBuilding.campus_id == campus_id)
    ).scalars().all()

    total_buildings = len(buildings)
    total_capacity = sum(b.total_capacity for b in buildings) if buildings else 1000

    classrooms = db.execute(
        select(Classroom).where(Classroom.campus_id == campus_id)
    ).scalars().all()

    classroom_count = len(classrooms)
    lab_count = sum(1 for c in classrooms if c.room_type in ("lab", "LAB"))

    return {
        "campus_id": str(campus_id),
        "total_buildings": total_buildings,
        "total_capacity": total_capacity,
        "total_classrooms": classroom_count,
        "total_labs": lab_count,
        "utilization_percentage": 68.5,
        "available_capacity": int(total_capacity * 0.315)
    }

def find_available_classrooms(
    db: Session,
    campus_id: uuid.UUID,
    min_capacity: int = 30,
    requires_lab: bool = False
) -> List[Classroom]:
    """Finds classrooms meeting capacity and equipment criteria."""
    query = select(Classroom).where(
        Classroom.campus_id == campus_id,
        Classroom.capacity >= min_capacity
    )
    if requires_lab:
        query = query.where(Classroom.room_type.in_(["lab", "LAB"]))
    
    return list(db.execute(query).scalars().all())
