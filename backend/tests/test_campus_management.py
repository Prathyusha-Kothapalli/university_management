import uuid
import pytest
from fastapi.testclient import TestClient
from app.models import *
from app.main import app
from app.database.base import Base
from app.database.session import engine

Base.metadata.create_all(bind=engine)
client = TestClient(app)

def test_tenant_branding_and_usage_analytics():
    univ_id = str(uuid.uuid4())
    
    # Get branding fallback
    b_resp = client.get(f"/api/v1/universities/{univ_id}/branding")
    assert b_resp.status_code == 200
    assert b_resp.json()["primary_color"] == "#2563eb"

    # Update branding
    u_resp = client.put(f"/api/v1/universities/{univ_id}/branding", json={
        "logo_url": "https://assets.unisphere.edu/logo.png",
        "primary_color": "#1e3a8a",
        "secondary_color": "#0284c7",
        "portal_domain": "custom.unisphere.edu",
        "email_sender_name": "Custom University Portal",
        "is_whitelabel_enabled": True
    })
    assert u_resp.status_code == 200

    # Tenant usage analytics
    usage_resp = client.get(f"/api/v1/universities/{univ_id}/usage-analytics")
    assert usage_resp.status_code == 200
    assert usage_resp.json()["quota_status"] == "HEALTHY"
