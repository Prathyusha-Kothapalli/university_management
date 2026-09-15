from datetime import datetime
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.hostel_expansion import (
    HostelAnnouncement,
    HostelApplication,
    HostelAttendance,
    HostelBed,
    HostelBuilding,
    HostelCheckIn,
    HostelCheckOut,
    HostelComplaint,
    HostelFloor,
    HostelIncident,
    HostelInventory,
    HostelMaintenanceRequest,
    HostelMealFeedback,
    HostelMess,
    HostelStaff,
    HostelTransfer,
    HostelVisitor,
)
from app.schemas.hostel_expansion import (
    HostelAnalyticsResponse,
    HostelAnnouncementCreate,
    HostelAnnouncementResponse,
    HostelApplicationCreate,
    HostelApplicationResponse,
    HostelApplicationStatusUpdate,
    HostelAttendanceRecordCreate,
    HostelAttendanceResponse,
    HostelBedCreate,
    HostelBedResponse,
    HostelBedUpdate,
    HostelBuildingCreate,
    HostelBuildingResponse,
    HostelBuildingUpdate,
    HostelCheckInCreate,
    HostelCheckInResponse,
    HostelCheckOutCreate,
    HostelCheckOutResponse,
    HostelComplaintCreate,
    HostelComplaintResponse,
    HostelComplaintUpdate,
    HostelDashboardOverview,
    HostelFloorCreate,
    HostelFloorResponse,
    HostelIncidentCreate,
    HostelIncidentResponse,
    HostelKpiCards,
    HostelMaintenanceCreate,
    HostelMaintenanceResponse,
    HostelMaintenanceUpdate,
    HostelMealFeedbackCreate,
    HostelMealFeedbackResponse,
    HostelMessCreate,
    HostelMessResponse,
    HostelTransferCreate,
    HostelTransferResponse,
    HostelTransferStatusUpdate,
    HostelVisitorCreate,
    HostelVisitorResponse,
    HostelVisitorStatusUpdate,
)
from app.services.hostel_expansion_service import HostelExpansionService

router = APIRouter(
    prefix="/hostel",
    tags=["Hostel Management Dashboard"]
)


# --- Dashboard Overview & KPIs ---
@router.get("/dashboard/overview", response_model=HostelDashboardOverview)
def get_dashboard_overview(db: Session = Depends(get_db)):
    return HostelExpansionService.get_dashboard_overview(db)


@router.get("/dashboard/kpis", response_model=HostelKpiCards)
def get_kpi_cards(db: Session = Depends(get_db)):
    return HostelExpansionService.get_kpi_cards(db)


@router.get("/dashboard/analytics", response_model=HostelAnalyticsResponse)
def get_dashboard_analytics(db: Session = Depends(get_db)):
    return HostelExpansionService.get_analytics(db)


@router.get("/dashboard/ai-insights")
def get_ai_insights(hostel_id: UUID | None = None, db: Session = Depends(get_db)):
    return HostelExpansionService.get_ai_insights(db, hostel_id)


# --- Building APIs ---
@router.get("/buildings", response_model=list[HostelBuildingResponse])
def get_buildings(hostel_id: UUID | None = None, db: Session = Depends(get_db)):
    try:
        stmt = select(HostelBuilding)
        if hostel_id:
            stmt = stmt.where(HostelBuilding.hostel_id == hostel_id)
        return list(db.execute(stmt).scalars().all())
    except Exception:
        return []


@router.post("/buildings", response_model=HostelBuildingResponse)
def create_building(data: HostelBuildingCreate, db: Session = Depends(get_db)):
    building = HostelBuilding(**data.model_dump())
    db.add(building)
    db.commit()
    db.refresh(building)
    return building


@router.put("/buildings/{building_id}", response_model=HostelBuildingResponse)
def update_building(building_id: UUID, data: HostelBuildingUpdate, db: Session = Depends(get_db)):
    b = db.get(HostelBuilding, building_id)
    if not b:
        raise HTTPException(status_code=404, detail="Building not found")
    for k, v in data.model_dump(exclude_unset=True).items():
        setattr(b, k, v)
    db.commit()
    db.refresh(b)
    return b


# --- Floor APIs ---
@router.get("/floors", response_model=list[HostelFloorResponse])
def get_floors(building_id: UUID | None = None, db: Session = Depends(get_db)):
    try:
        stmt = select(HostelFloor)
        if building_id:
            stmt = stmt.where(HostelFloor.building_id == building_id)
        return list(db.execute(stmt).scalars().all())
    except Exception:
        return []


@router.post("/floors", response_model=HostelFloorResponse)
def create_floor(data: HostelFloorCreate, db: Session = Depends(get_db)):
    floor = HostelFloor(**data.model_dump())
    db.add(floor)
    db.commit()
    db.refresh(floor)
    return floor


# --- Bed APIs ---
@router.get("/beds", response_model=list[HostelBedResponse])
def get_beds(room_id: UUID | None = None, status: str | None = None, db: Session = Depends(get_db)):
    try:
        stmt = select(HostelBed)
        if room_id:
            stmt = stmt.where(HostelBed.room_id == room_id)
        if status:
            stmt = stmt.where(HostelBed.status == status)
        return list(db.execute(stmt).scalars().all())
    except Exception:
        return []


@router.post("/beds", response_model=HostelBedResponse)
def create_bed(data: HostelBedCreate, db: Session = Depends(get_db)):
    bed = HostelBed(**data.model_dump())
    db.add(bed)
    db.commit()
    db.refresh(bed)
    return bed


@router.put("/beds/{bed_id}", response_model=HostelBedResponse)
def update_bed(bed_id: UUID, data: HostelBedUpdate, db: Session = Depends(get_db)):
    bed = db.get(HostelBed, bed_id)
    if not bed:
        raise HTTPException(status_code=404, detail="Bed not found")
    for k, v in data.model_dump(exclude_unset=True).items():
        setattr(bed, k, v)
    db.commit()
    db.refresh(bed)
    return bed


# --- Application APIs ---
@router.get("/applications", response_model=list[HostelApplicationResponse])
def get_applications(status: str | None = None, db: Session = Depends(get_db)):
    try:
        stmt = select(HostelApplication)
        if status:
            stmt = stmt.where(HostelApplication.status == status)
        return list(db.execute(stmt).scalars().all())
    except Exception:
        return []


@router.post("/applications", response_model=HostelApplicationResponse)
def create_application(data: HostelApplicationCreate, db: Session = Depends(get_db)):
    app = HostelApplication(**data.model_dump())
    db.add(app)
    db.commit()
    db.refresh(app)
    return app


@router.put("/applications/{app_id}/status", response_model=HostelApplicationResponse)
def update_application_status(app_id: UUID, data: HostelApplicationStatusUpdate, db: Session = Depends(get_db)):
    app = db.get(HostelApplication, app_id)
    if not app:
        raise HTTPException(status_code=404, detail="Application not found")
    app.status = data.status
    if data.remarks:
        app.remarks = data.remarks
    db.commit()
    db.refresh(app)
    return app


# --- Transfer APIs ---
@router.get("/transfers", response_model=list[HostelTransferResponse])
def get_transfers(status: str | None = None, db: Session = Depends(get_db)):
    try:
        stmt = select(HostelTransfer)
        if status:
            stmt = stmt.where(HostelTransfer.status == status)
        return list(db.execute(stmt).scalars().all())
    except Exception:
        return []


@router.post("/transfers", response_model=HostelTransferResponse)
def create_transfer(data: HostelTransferCreate, db: Session = Depends(get_db)):
    tr = HostelTransfer(**data.model_dump())
    db.add(tr)
    db.commit()
    db.refresh(tr)
    return tr


@router.put("/transfers/{transfer_id}/status", response_model=HostelTransferResponse)
def update_transfer_status(transfer_id: UUID, data: HostelTransferStatusUpdate, db: Session = Depends(get_db)):
    tr = db.get(HostelTransfer, transfer_id)
    if not tr:
        raise HTTPException(status_code=404, detail="Transfer not found")
    tr.status = data.status
    if data.approved_by_id:
        tr.approved_by_id = data.approved_by_id
    if data.status == "APPROVED":
        tr.transfer_date = datetime.utcnow()
    db.commit()
    db.refresh(tr)
    return tr


# --- CheckIn & CheckOut APIs ---
@router.post("/checkins", response_model=HostelCheckInResponse)
def checkin_resident(data: HostelCheckInCreate, db: Session = Depends(get_db)):
    ci = HostelCheckIn(**data.model_dump())
    db.add(ci)
    db.commit()
    db.refresh(ci)
    return ci


@router.post("/checkouts", response_model=HostelCheckOutResponse)
def checkout_resident(data: HostelCheckOutCreate, db: Session = Depends(get_db)):
    co = HostelCheckOut(**data.model_dump())
    db.add(co)
    db.commit()
    db.refresh(co)
    return co


# --- Attendance APIs ---
@router.get("/attendance", response_model=list[HostelAttendanceResponse])
def get_attendance(room_id: UUID | None = None, date_str: str | None = None, db: Session = Depends(get_db)):
    try:
        stmt = select(HostelAttendance)
        if room_id:
            stmt = stmt.where(HostelAttendance.room_id == room_id)
        return list(db.execute(stmt).scalars().all())
    except Exception:
        return []


@router.post("/attendance", response_model=HostelAttendanceResponse)
def record_attendance(data: HostelAttendanceRecordCreate, db: Session = Depends(get_db)):
    att = HostelAttendance(**data.model_dump())
    db.add(att)
    db.commit()
    db.refresh(att)
    return att


# --- Visitor APIs ---
@router.get("/visitors", response_model=list[HostelVisitorResponse])
def get_visitors(student_id: UUID | None = None, db: Session = Depends(get_db)):
    try:
        stmt = select(HostelVisitor)
        if student_id:
            stmt = stmt.where(HostelVisitor.student_id == student_id)
        return list(db.execute(stmt).scalars().all())
    except Exception:
        return []


@router.post("/visitors", response_model=HostelVisitorResponse)
def register_visitor(data: HostelVisitorCreate, db: Session = Depends(get_db)):
    vis = HostelVisitor(**data.model_dump())
    db.add(vis)
    db.commit()
    db.refresh(vis)
    return vis


@router.put("/visitors/{visitor_id}/status", response_model=HostelVisitorResponse)
def update_visitor_status(visitor_id: UUID, data: HostelVisitorStatusUpdate, db: Session = Depends(get_db)):
    vis = db.get(HostelVisitor, visitor_id)
    if not vis:
        raise HTTPException(status_code=404, detail="Visitor not found")
    vis.status = data.status
    if data.check_out_time:
        vis.check_out_time = data.check_out_time
    db.commit()
    db.refresh(vis)
    return vis


# --- Complaint APIs ---
@router.get("/complaints", response_model=list[HostelComplaintResponse])
def get_complaints(hostel_id: UUID | None = None, status: str | None = None, db: Session = Depends(get_db)):
    try:
        stmt = select(HostelComplaint)
        if hostel_id:
            stmt = stmt.where(HostelComplaint.hostel_id == hostel_id)
        if status:
            stmt = stmt.where(HostelComplaint.status == status)
        return list(db.execute(stmt).scalars().all())
    except Exception:
        return []


@router.post("/complaints", response_model=HostelComplaintResponse)
def create_complaint(data: HostelComplaintCreate, db: Session = Depends(get_db)):
    comp = HostelComplaint(**data.model_dump())
    db.add(comp)
    db.commit()
    db.refresh(comp)
    return comp


@router.put("/complaints/{complaint_id}", response_model=HostelComplaintResponse)
def update_complaint(complaint_id: UUID, data: HostelComplaintUpdate, db: Session = Depends(get_db)):
    comp = db.get(HostelComplaint, complaint_id)
    if not comp:
        raise HTTPException(status_code=404, detail="Complaint not found")
    for k, v in data.model_dump(exclude_unset=True).items():
        setattr(comp, k, v)
    if data.status == "RESOLVED":
        comp.resolved_at = datetime.utcnow()
    db.commit()
    db.refresh(comp)
    return comp


# --- Maintenance APIs ---
@router.get("/maintenance", response_model=list[HostelMaintenanceResponse])
def get_maintenance_requests(hostel_id: UUID | None = None, status: str | None = None, db: Session = Depends(get_db)):
    try:
        stmt = select(HostelMaintenanceRequest)
        if hostel_id:
            stmt = stmt.where(HostelMaintenanceRequest.hostel_id == hostel_id)
        if status:
            stmt = stmt.where(HostelMaintenanceRequest.status == status)
        return list(db.execute(stmt).scalars().all())
    except Exception:
        return []


@router.post("/maintenance", response_model=HostelMaintenanceResponse)
def create_maintenance_request(data: HostelMaintenanceCreate, db: Session = Depends(get_db)):
    m = HostelMaintenanceRequest(**data.model_dump())
    db.add(m)
    db.commit()
    db.refresh(m)
    return m


@router.put("/maintenance/{m_id}", response_model=HostelMaintenanceResponse)
def update_maintenance_request(m_id: UUID, data: HostelMaintenanceUpdate, db: Session = Depends(get_db)):
    m = db.get(HostelMaintenanceRequest, m_id)
    if not m:
        raise HTTPException(status_code=404, detail="Maintenance request not found")
    for k, v in data.model_dump(exclude_unset=True).items():
        setattr(m, k, v)
    if data.status == "COMPLETED":
        m.completed_at = datetime.utcnow()
    db.commit()
    db.refresh(m)
    return m


# --- Mess & Feedback APIs ---
@router.get("/mess", response_model=list[HostelMessResponse])
def get_mess_menu(hostel_id: UUID | None = None, db: Session = Depends(get_db)):
    try:
        stmt = select(HostelMess)
        if hostel_id:
            stmt = stmt.where(HostelMess.hostel_id == hostel_id)
        return list(db.execute(stmt).scalars().all())
    except Exception:
        return []


@router.post("/mess", response_model=HostelMessResponse)
def create_mess_menu(data: HostelMessCreate, db: Session = Depends(get_db)):
    mess = HostelMess(**data.model_dump())
    db.add(mess)
    db.commit()
    db.refresh(mess)
    return mess


@router.post("/mess/feedback", response_model=HostelMealFeedbackResponse)
def submit_meal_feedback(data: HostelMealFeedbackCreate, db: Session = Depends(get_db)):
    fb = HostelMealFeedback(**data.model_dump())
    db.add(fb)
    db.commit()
    db.refresh(fb)
    return fb


# --- Incident APIs ---
@router.get("/incidents", response_model=list[HostelIncidentResponse])
def get_incidents(hostel_id: UUID | None = None, db: Session = Depends(get_db)):
    try:
        stmt = select(HostelIncident)
        if hostel_id:
            stmt = stmt.where(HostelIncident.hostel_id == hostel_id)
        return list(db.execute(stmt).scalars().all())
    except Exception:
        return []


@router.post("/incidents", response_model=HostelIncidentResponse)
def create_incident(data: HostelIncidentCreate, db: Session = Depends(get_db)):
    inc = HostelIncident(**data.model_dump())
    db.add(inc)
    db.commit()
    db.refresh(inc)
    return inc


# --- Announcement APIs ---
@router.get("/announcements", response_model=list[HostelAnnouncementResponse])
def get_announcements(hostel_id: UUID | None = None, db: Session = Depends(get_db)):
    try:
        stmt = select(HostelAnnouncement)
        if hostel_id:
            stmt = stmt.where(HostelAnnouncement.hostel_id == hostel_id)
        return list(db.execute(stmt).scalars().all())
    except Exception:
        return []


@router.post("/announcements", response_model=HostelAnnouncementResponse)
def create_announcement(data: HostelAnnouncementCreate, db: Session = Depends(get_db)):
    anc = HostelAnnouncement(**data.model_dump())
    db.add(anc)
    db.commit()
    db.refresh(anc)
    return anc
