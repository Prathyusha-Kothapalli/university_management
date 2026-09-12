import pytest
import uuid
from fastapi.testclient import TestClient
from app.models import *
from app.main import app
from app.database.base import Base
from app.database.session import engine, SessionLocal
from app.services.tenancy_service import (
    onboard_new_tenant,
    generate_tenant_css_theme,
    get_tenant_storage_status,
    is_feature_enabled_for_tenant,
)

Base.metadata.create_all(bind=engine)
client = TestClient(app)


def test_tenant_onboarding_and_branding():
    db = SessionLocal()
    try:
        code = f"OXFORD-{uuid.uuid4().hex[:6].upper()}"
        uni, branding = onboard_new_tenant(
            db,
            university_name="Oxford Tech University",
            university_code=code,
            admin_email="admin@oxfordtech.edu",
            domain="oxfordtech.edu"
        )
        assert uni.id is not None
        assert branding.university_id == uni.id
        assert branding.primary_color == "#1E40AF"

        css = generate_tenant_css_theme(branding)
        assert "--color-primary: #1E40AF" in css

        storage_res = get_tenant_storage_status(db, uni.id)
        assert storage_res.university_id == uni.id
        assert storage_res.storage_quota_bytes > 0
    finally:
        db.close()


def test_tenant_feature_flags_default():
    db = SessionLocal()
    try:
        test_uni_id = uuid.uuid4()
        enabled = is_feature_enabled_for_tenant(db, test_uni_id, "ai_copilot")
        assert enabled is True
    finally:
        db.close()


def test_tenancy_onboard_api_route():
    code = f"MIT-{uuid.uuid4().hex[:6].upper()}"
    response = client.post(
        "/api/v1/tenancy/onboard",
        params={
            "name": "MIT Science Institute",
            "code": code,
            "admin_email": "dean@mitsci.edu"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["portal_title"] == "MIT Science Institute Portal"
