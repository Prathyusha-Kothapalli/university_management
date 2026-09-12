import uuid
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database.base import Base
from app.database.session import engine

Base.metadata.create_all(bind=engine)
client = TestClient(app)

def test_password_policy_and_registration():
    email = f"user_{uuid.uuid4().hex[:6]}@unisphere.edu"
    
    # Fail weak password
    resp = client.post("/api/v1/auth/register", json={
        "full_name": "Test User",
        "email": email,
        "password": "123",
        "role_name": "student"
    })
    assert resp.status_code == 400
    assert "Password does not meet security criteria" in resp.json()["detail"]

    # Success strong password
    resp_success = client.post("/api/v1/auth/register", json={
        "full_name": "Test User",
        "email": email,
        "password": "StrongPassword123!",
        "role_name": "student"
    })
    assert resp_success.status_code == 200
    data = resp_success.json()
    assert "access_token" in data
    assert "verification_token" in data

def test_forgot_and_reset_password_flow():
    email = f"reset_{uuid.uuid4().hex[:6]}@unisphere.edu"
    client.post("/api/v1/auth/register", json={
        "full_name": "Reset Tester",
        "email": email,
        "password": "Password123!",
        "role_name": "student"
    })

    # Forgot password
    forgot_resp = client.post("/api/v1/auth/forgot-password", json={"email": email})
    assert forgot_resp.status_code == 200
    token = forgot_resp.json().get("reset_token")
    assert token is not None

    # Reset password
    reset_resp = client.post("/api/v1/auth/reset-password", json={
        "token": token,
        "new_password": "NewStrongPassword2026!"
    })
    assert reset_resp.status_code == 200
    assert "Password reset successfully" in reset_resp.json()["message"]

def test_mfa_enable_and_verify():
    mfa_resp = client.post("/api/v1/auth/mfa/enable", headers={"Authorization": "Bearer DEMO_TOKEN"})
    assert mfa_resp.status_code == 200
    data = mfa_resp.json()
    assert "secret" in data
    assert len(data["backup_codes"]) == 8

    verify_resp = client.post("/api/v1/auth/mfa/verify", json={"user_id": str(uuid.uuid4()), "code": "123456"})
    assert verify_resp.status_code == 200

def test_session_listing_and_revocation():
    sess_resp = client.get("/api/v1/auth/sessions")
    assert sess_resp.status_code == 200
    assert "active_sessions" in sess_resp.json()
