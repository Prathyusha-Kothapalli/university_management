import uuid
import pytest
from fastapi.testclient import TestClient
from app.main import app

from app.database.base import Base
from app.database.session import engine

Base.metadata.create_all(bind=engine)

client = TestClient(app)


def test_tenant_registration():
    slug = f"univ_{uuid.uuid4().hex[:6]}"
    payload = {
        "name": "Polytechnic Institute of Tech",
        "slug": slug,
        "admin_email": "admin@poly.edu"
    }

    response = client.post("/api/v1/tenants/", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["tenant"]["slug"] == slug
    assert "feature_flags" in data


def test_tenant_feature_flag_update():
    slug = "global"
    payload = {
        "feature_name": "ai_assistant",
        "enabled": False
    }

    response = client.put(f"/api/v1/tenants/{slug}/feature-flags", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["feature_flags"]["ai_assistant"] is False
