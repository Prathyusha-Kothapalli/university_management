import uuid
import hashlib
import time
from datetime import datetime, timedelta
from typing import Dict, Any, List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import select

from app.models.attendance_record import AttendanceRecord
from app.models.attendance_session import AttendanceSession

ACTIVE_QR_TOKENS: Dict[str, Dict[str, Any]] = {}

def generate_qr_attendance_token(session_id: uuid.UUID, ttl_seconds: int = 60) -> str:
    """Generates dynamic time-sensitive QR check-in token."""
    token_id = str(uuid.uuid4().hex[:12])
    expires_at = time.time() + ttl_seconds
    raw_sig = f"{session_id}:{token_id}:{expires_at}:UNISPHERE_QR_SECRET"
    token_hash = hashlib.sha256(raw_sig.encode()).hexdigest()[:16]

    qr_payload = f"QR:{session_id}:{token_id}:{token_hash}"

    ACTIVE_QR_TOKENS[token_payload_key(session_id)] = {
        "session_id": str(session_id),
        "token_id": token_id,
        "hash": token_hash,
        "expires_at": expires_at
    }

    return qr_payload

def token_payload_key(session_id: uuid.UUID) -> str:
    return str(session_id)

def validate_qr_attendance_scan(qr_payload: str, student_id: uuid.UUID, db: Session) -> Dict[str, Any]:
    """Validates QR code payload and marks student attendance present."""
    parts = qr_payload.split(":")
    if len(parts) != 4 or parts[0] != "QR":
        return {"success": False, "error": "Invalid QR code format"}

    session_id_str, token_id, token_hash = parts[1], parts[2], parts[3]
    record = ACTIVE_QR_TOKENS.get(session_id_str)

    if not record or record.get("token_id") != token_id or record.get("hash") != token_hash:
        return {"success": False, "error": "Expired or invalid QR check-in token"}

    if time.time() > record["expires_at"]:
        return {"success": False, "error": "QR check-in code has expired"}

    # Record attendance entry
    att_entry = AttendanceRecord(
        attendance_session_id=uuid.UUID(session_id_str),
        student_id=student_id,
        status="PRESENT",
        remarks="QR Code Mobile Check-in"
    )
    db.add(att_entry)
    db.commit()

    return {"success": True, "message": "Attendance verified and recorded!", "student_id": str(student_id)}
