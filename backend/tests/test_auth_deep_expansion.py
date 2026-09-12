import pytest
import uuid
from fastapi.testclient import TestClient
from app.models import *
from app.services.auth_expansion_service import (
    evaluate_login_risk,
    evaluate_auth_policy,
    generate_mfa_recovery_codes,
    verify_and_consume_recovery_code,
    create_user_session,
)
from app.main import app
from app.database.base import Base
from app.database.session import engine, SessionLocal

Base.metadata.create_all(bind=engine)
client = TestClient(app)


def test_password_policy_strict_evaluation():
    db = SessionLocal()
    try:
        valid, errors = evaluate_auth_policy(db, None, "SecurePass123!")
        assert valid is True
        assert len(errors) == 0

        valid, errors = evaluate_auth_policy(db, None, "Short1!")
        assert valid is False
        assert any("at least 8 characters" in err for err in errors)

        valid, errors = evaluate_auth_policy(db, None, "NoSymbolPassword12")
        assert valid is False
        assert any("special character" in err for err in errors)
    finally:
        db.close()


def test_login_suspicious_risk_telemetry():
    db = SessionLocal()
    try:
        role = db.query(Role).filter(Role.name == "student").first()
        if not role:
            role = Role(name="student", description="Student role")
            db.add(role)
            db.commit()

        test_user = User(
            full_name="Risk Test User",
            email=f"risk.test.{uuid.uuid4().hex[:6]}@university.edu",
            password_hash="hashed_pw_test",
            role_id=role.id,
            is_active=True
        )
        db.add(test_user)
        db.commit()
        db.refresh(test_user)

        # Create prior session from known IP 10.0.0.1
        create_user_session(
            db,
            user_id=test_user.id,
            session_token=uuid.uuid4().hex,
            ip_address="10.0.0.1",
            user_agent="KnownBrowser/1.0"
        )

        # Evaluate login from unknown IP and unknown user agent
        risk_res = evaluate_login_risk(
            db,
            test_user.id,
            ip_address="198.51.100.44",
            user_agent="UnknownMobileAgent/1.0"
        )
        assert risk_res.is_suspicious is True
        assert risk_res.risk_score >= 0.35
        assert len(risk_res.reasons) > 0
    finally:
        db.close()


def test_mfa_recovery_codes_workflow():
    db = SessionLocal()
    try:
        role = db.query(Role).filter(Role.name == "student").first()
        if not role:
            role = Role(name="student", description="Student role")
            db.add(role)
            db.commit()

        email = f"mfa.recovery.{uuid.uuid4().hex[:6]}@university.edu"
        test_user = User(
            full_name="MFA Recovery User",
            email=email,
            password_hash="hashed_pw_test",
            role_id=role.id,
            is_active=True
        )
        db.add(test_user)
        db.commit()
        db.refresh(test_user)

        codes = generate_mfa_recovery_codes(db, test_user.id)
        assert len(codes) == 8
        first_code = codes[0]

        success = verify_and_consume_recovery_code(db, email, first_code)
        assert success is True

        fail_reuse = verify_and_consume_recovery_code(db, email, first_code)
        assert fail_reuse is False
    finally:
        db.close()


def test_auth_audit_logs_api_endpoint():
    response = client.get("/api/v1/auth/expansion/audit-logs")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
