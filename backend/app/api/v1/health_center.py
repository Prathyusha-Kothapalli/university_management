from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.health_center import (
    MedicalRecord,
    HealthAppointment,
    PharmacyItem,
    HealthEmergencyAlert,
)
from app.schemas.health_center import (
    MedicalRecordCreate,
    MedicalRecordUpdate,
    MedicalRecordResponse,
    HealthAppointmentCreate,
    HealthAppointmentUpdate,
    HealthAppointmentResponse,
    PharmacyItemCreate,
    PharmacyItemUpdate,
    PharmacyItemResponse,
    HealthEmergencyAlertCreate,
    HealthEmergencyAlertResponse,
)

router = APIRouter(
    prefix="/health-center",
    tags=["Campus Health Center"]
)


# --- Medical Records ---
@router.post("/medical-records", response_model=MedicalRecordResponse, status_code=status.HTTP_201_CREATED)
def create_medical_record(
    record_in: MedicalRecordCreate,
    db: Session = Depends(get_db)
):
    record = MedicalRecord(**record_in.model_dump())
    db.add(record)
    db.commit()
    db.refresh(record)
    return record


@router.get("/medical-records", response_model=List[MedicalRecordResponse])
def get_medical_records(
    student_id: UUID = None,
    db: Session = Depends(get_db)
):
    query = select(MedicalRecord)
    if student_id:
        query = query.where(MedicalRecord.student_id == student_id)
    result = db.execute(query)
    return result.scalars().all()


@router.get("/medical-records/{record_id}", response_model=MedicalRecordResponse)
def get_medical_record(
    record_id: UUID,
    db: Session = Depends(get_db)
):
    record = db.get(MedicalRecord, record_id)
    if not record:
        raise HTTPException(status_code=404, detail="Medical record not found")
    return record


# --- Health Appointments ---
@router.post("/appointments", response_model=HealthAppointmentResponse, status_code=status.HTTP_201_CREATED)
def create_appointment(
    appt_in: HealthAppointmentCreate,
    db: Session = Depends(get_db)
):
    appt = HealthAppointment(**appt_in.model_dump())
    db.add(appt)
    db.commit()
    db.refresh(appt)
    return appt


@router.get("/appointments", response_model=List[HealthAppointmentResponse])
def get_appointments(
    student_id: UUID = None,
    db: Session = Depends(get_db)
):
    query = select(HealthAppointment)
    if student_id:
        query = query.where(HealthAppointment.student_id == student_id)
    result = db.execute(query)
    return result.scalars().all()


@router.patch("/appointments/{appt_id}", response_model=HealthAppointmentResponse)
def update_appointment(
    appt_id: UUID,
    appt_in: HealthAppointmentUpdate,
    db: Session = Depends(get_db)
):
    appt = db.get(HealthAppointment, appt_id)
    if not appt:
        raise HTTPException(status_code=404, detail="Appointment not found")
    
    update_data = appt_in.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(appt, field, value)
        
    db.commit()
    db.refresh(appt)
    return appt


# --- Pharmacy Items ---
@router.post("/pharmacy", response_model=PharmacyItemResponse, status_code=status.HTTP_201_CREATED)
def create_pharmacy_item(
    item_in: PharmacyItemCreate,
    db: Session = Depends(get_db)
):
    item = PharmacyItem(**item_in.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


@router.get("/pharmacy", response_model=List[PharmacyItemResponse])
def get_pharmacy_items(
    db: Session = Depends(get_db)
):
    result = db.execute(select(PharmacyItem))
    return result.scalars().all()


# --- Emergency Alerts ---
@router.post("/emergencies", response_model=HealthEmergencyAlertResponse, status_code=status.HTTP_201_CREATED)
def trigger_emergency_alert(
    alert_in: HealthEmergencyAlertCreate,
    db: Session = Depends(get_db)
):
    alert = HealthEmergencyAlert(**alert_in.model_dump())
    db.add(alert)
    db.commit()
    db.refresh(alert)
    return alert


@router.get("/emergencies", response_model=List[HealthEmergencyAlertResponse])
def get_emergency_alerts(
    db: Session = Depends(get_db)
):
    result = db.execute(select(HealthEmergencyAlert))
    return result.scalars().all()
