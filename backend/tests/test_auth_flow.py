import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.core.security import create_access_token, create_refresh_token, decode_token, check_permission, ROLE_PERMISSIONS

client = TestClient(app)


def test_jwt_creation_and_decoding():
    payload = {"sub": "user-123", "email": "test@unisphere.edu", "role": "faculty"}
    token = create_access_token(payload)
    assert token is not None

    decoded = decode_token(token)
    assert decoded["sub"] == "user-123"
    assert decoded["email"] == "test@unisphere.edu"
    assert decoded["role"] == "faculty"
    assert decoded["type"] == "access"


def test_refresh_token_rotation():
    payload = {"sub": "user-456", "email": "student@unisphere.edu", "role": "student"}
    refresh_token = create_refresh_token(payload)

    response = client.post("/api/v1/auth/refresh", json={"refresh_token": refresh_token})
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert "refresh_token" in data
    assert data["token_type"] == "bearer"

    # Verify previous refresh token is now revoked
    response2 = client.post("/api/v1/auth/refresh", json={"refresh_token": refresh_token})
    assert response2.status_code == 401
    assert "revoked" in response2.json()["detail"].lower()


def test_role_permission_mask():
    assert check_permission("admin", 1 << 5) is True
    assert check_permission("student", 1 << 0) is True
    assert check_permission("student", 1 << 2) is False  # Cannot manage faculty


def test_auth_me_endpoint():
    response = client.get("/api/v1/auth/me")
    assert response.status_code == 200
    data = response.json()
    assert "email" in data
    assert "role" in data
    assert "permissions_mask" in data
