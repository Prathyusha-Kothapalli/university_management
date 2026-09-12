import uuid
from datetime import datetime, timedelta
from typing import Dict, Any, List

def calculate_ticket_sla_deadline(priority: str) -> Dict[str, Any]:
    """Calculates SLA response & resolution deadlines based on ticket priority."""
    now = datetime.utcnow()

    if priority == "URGENT":
        sla_hours = 4
    elif priority == "HIGH":
        sla_hours = 12
    elif priority == "MEDIUM":
        sla_hours = 24
    else:
        sla_hours = 48

    deadline = now + timedelta(hours=sla_hours)

    return {
        "priority": priority,
        "sla_hours": sla_hours,
        "created_at": now.isoformat(),
        "sla_deadline": deadline.isoformat(),
        "is_breached": False
    }
