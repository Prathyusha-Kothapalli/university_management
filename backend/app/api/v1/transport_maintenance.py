import uuid
from typing import List, Dict, Optional
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

router = APIRouter(
    prefix="/transport-maintenance",
    tags=["Transport Fleet Maintenance & Fuel Ledger"]
)


class MaintenanceLogRequest(BaseModel):
    vehicle_id: UUID
    service_type: str = "SCHEDULED_SERVICING"  # SCHEDULED_SERVICING, TIRE_REPLACEMENT, ENGINE_REPAIR
    odometer_km: float = 45200.0
    cost_usd: float = 350.0
    description: str = "Routine oil change, brake pad replacement, filter swap."
    service_center: str = "Central Bus Depot"


class FuelLogRequest(BaseModel):
    vehicle_id: UUID
    fuel_liters: float = 120.0
    price_per_liter: float = 1.45
    current_odometer_km: float = 45450.0


# In-memory storage for vehicle maintenance & fuel records
MAINTENANCE_RECORDS = {}
FUEL_LOGS = {}


@router.post("/log-maintenance")
def log_vehicle_maintenance(req: MaintenanceLogRequest):
    vehicle_str = str(req.vehicle_id)
    record_id = str(uuid.uuid4())

    entry = {
        "record_id": record_id,
        "vehicle_id": vehicle_str,
        "service_type": req.service_type,
        "odometer_km": req.odometer_km,
        "cost_usd": req.cost_usd,
        "description": req.description,
        "service_center": req.service_center,
        "serviced_at": "2026-09-11T12:30:00Z"
    }

    if vehicle_str not in MAINTENANCE_RECORDS:
        MAINTENANCE_RECORDS[vehicle_str] = []
    MAINTENANCE_RECORDS[vehicle_str].append(entry)

    return {
        "message": "Vehicle maintenance log recorded successfully",
        "record": entry
    }


@router.post("/log-fuel")
def log_fuel_consumption(req: FuelLogRequest):
    vehicle_str = str(req.vehicle_id)
    fuel_id = str(uuid.uuid4())
    total_cost = round(req.fuel_liters * req.price_per_liter, 2)

    entry = {
        "fuel_id": fuel_id,
        "vehicle_id": vehicle_str,
        "fuel_liters": req.fuel_liters,
        "price_per_liter": req.price_per_liter,
        "total_cost_usd": total_cost,
        "current_odometer_km": req.current_odometer_km,
        "logged_at": "2026-09-11T12:35:00Z"
    }

    if vehicle_str not in FUEL_LOGS:
        FUEL_LOGS[vehicle_str] = []
    FUEL_LOGS[vehicle_str].append(entry)

    return {
        "message": "Fuel consumption entry logged",
        "fuel_entry": entry
    }


@router.get("/vehicle/{vehicle_id}")
def get_vehicle_maintenance_history(vehicle_id: UUID):
    vehicle_str = str(vehicle_id)
    m_records = MAINTENANCE_RECORDS.get(vehicle_str, [
        {
            "record_id": "mkt-101",
            "vehicle_id": vehicle_str,
            "service_type": "SCHEDULED_SERVICING",
            "odometer_km": 42000.0,
            "cost_usd": 320.0,
            "serviced_at": "2026-09-01T10:00:00Z"
        }
    ])
    f_records = FUEL_LOGS.get(vehicle_str, [])

    total_maint_cost = sum(r["cost_usd"] for r in m_records)

    return {
        "vehicle_id": vehicle_str,
        "total_maintenance_cost_usd": total_maint_cost,
        "maintenance_history": m_records,
        "fuel_history": f_records
    }
