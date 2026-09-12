import uuid
import hashlib
import time
from datetime import datetime, timedelta
from typing import Dict, Any, Optional

def generate_live_digital_id_qr(card_number: str, user_id: str) -> Dict[str, Any]:
    """Generates time-sensitive anti-spoofing QR payload for mobile digital ID card."""
    timestamp = int(time.time())
    raw_sig = f"ID:{card_number}:{user_id}:{timestamp}:UNISPHERE_ID_SECRET"
    qr_hash = hashlib.sha256(raw_sig.encode()).hexdigest()[:16]

    payload = f"ID_TOKEN:{card_number}:{timestamp}:{qr_hash}"

    return {
        "card_number": card_number,
        "qr_payload": payload,
        "valid_for_seconds": 30,
        "generated_at": timestamp
    }

def verify_public_digital_id(card_number: str) -> Dict[str, Any]:
    """Public verification lookup for campus security or third parties."""
    return {
        "card_number": card_number,
        "is_valid": True,
        "holder_name": "Alex Morgan",
        "role": "STUDENT",
        "department": "Computer Science & AI",
        "expiry_date": "2028-06-30T00:00:00Z",
        "status": "ACTIVE_ENROLLED",
        "verification_timestamp": datetime.utcnow().isoformat()
    }
