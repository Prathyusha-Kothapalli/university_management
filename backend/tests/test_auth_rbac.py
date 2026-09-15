import pytest
import uuid
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.main import app
from app.database.session import get_db, init_db
from app.models.tenant import Base, Tenant
from app.models.user import User, UserRole
from app.core.config import settings
from app.core.security import get_password_hash

# Setup in-memory SQLite database for test suite
TEST_DATABASE_URL = "sqlite:///:memory:"
test_engine = create_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

# Create schema and seed data in test database
Base.metadata.create_all(bind=test_engine)

# Seed superadmin
db = TestingSessionLocal()
super_admin = User(
    email=settings.DEFAULT_SUPERADMIN_EMAIL,
    hashed_password=get_password_hash(settings.DEFAULT_SUPERADMIN_PASSWORD),
    full_name="UniSphere Global SuperAdmin",
    role=UserRole.SUPER_ADMIN,
    tenant_id=None,
    is_active=True
)
stanford = Tenant(
    name="Stanford University",
    code="STANFORD",
    domain="stanford.edu",
    description="Stanford University Demo Campus",
    is_active=True
)
db.add_all([super_admin, stanford])
db.commit()
db.refresh(stanford)

stanford_admin = User(
    email="admin@stanford.edu",
    hashed_password=get_password_hash("Admin@123"),
    full_name="Stanford Admin",
    role=UserRole.UNIVERSITY_ADMIN,
    tenant_id=stanford.id,
    department="Central Administration",
    is_active=True
)
db.add(stanford_admin)
db.commit()
db.close()

client = TestClient(app)

def test_health_and_root():
    res = client.get("/")
    assert res.status_code == 200
    res_health = client.get("/health")
    assert res_health.status_code == 200

def test_superadmin_login_and_me():
    login_res = client.post(f"{settings.API_V1_STR}/auth/login", json={
        "email": settings.DEFAULT_SUPERADMIN_EMAIL,
        "password": settings.DEFAULT_SUPERADMIN_PASSWORD
    })
    assert login_res.status_code == 200, login_res.text
    data = login_res.json()
    assert "access_token" in data
    assert data["user"]["role"] == "SUPER_ADMIN"

    token = data["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    me_res = client.get(f"{settings.API_V1_STR}/auth/me", headers=headers)
    assert me_res.status_code == 200
    me_data = me_res.json()
    assert me_data["email"] == settings.DEFAULT_SUPERADMIN_EMAIL
    assert me_data["role"] == "SUPER_ADMIN"

def test_tenant_registration_and_login():
    unique_suffix = uuid.uuid4().hex[:6]
    tenant_code = f"OXFORD_{unique_suffix}".upper()
    admin_email = f"admin_{unique_suffix}@oxford.edu"

    reg_res = client.post(f"{settings.API_V1_STR}/auth/register-tenant", json={
        "tenant_name": f"Oxford Academy {unique_suffix}",
        "tenant_code": tenant_code,
        "tenant_domain": f"oxford_{unique_suffix}.edu",
        "tenant_description": "Oxford University Demo Campus",
        "admin_email": admin_email,
        "admin_password": "OxfordAdmin@123",
        "admin_name": "Oxford Administrator",
        "admin_department": "Central Office"
    })
    assert reg_res.status_code == 201, reg_res.text
    data = reg_res.json()
    assert "access_token" in data
    assert data["user"]["role"] == "UNIVERSITY_ADMIN"
    assert data["user"]["email"] == admin_email

    login_res = client.post(f"{settings.API_V1_STR}/auth/login", json={
        "email": admin_email,
        "password": "OxfordAdmin@123"
    })
    assert login_res.status_code == 200
    assert login_res.json()["user"]["role"] == "UNIVERSITY_ADMIN"

def test_user_creation_and_tenant_isolation():
    # 1. Login as Stanford Admin
    stanford_login = client.post(f"{settings.API_V1_STR}/auth/login", json={
        "email": "admin@stanford.edu",
        "password": "Admin@123"
    })
    stanford_token = stanford_login.json()["access_token"]
    stanford_headers = {"Authorization": f"Bearer {stanford_token}"}
    stanford_tenant_id = stanford_login.json()["user"]["tenant_id"]

    # 2. Register a student under Stanford
    student_res = client.post(f"{settings.API_V1_STR}/auth/register-user", json={
        "email": "student_test@stanford.edu",
        "password": "StudentPass@123",
        "full_name": "Bob Student",
        "role": "STUDENT",
        "department": "Computer Science"
    }, headers=stanford_headers)
    assert student_res.status_code == 201, student_res.text
    student_data = student_res.json()
    assert student_data["tenant_id"] == stanford_tenant_id

    # 3. List users as Stanford Admin - verify tenant isolation
    users_res = client.get(f"{settings.API_V1_STR}/users", headers=stanford_headers)
    assert users_res.status_code == 200
    users_list = users_res.json()
    for u in users_list:
        assert u["tenant_id"] == stanford_tenant_id

    # 4. Super Admin can see users across all tenants
    super_login = client.post(f"{settings.API_V1_STR}/auth/login", json={
        "email": settings.DEFAULT_SUPERADMIN_EMAIL,
        "password": settings.DEFAULT_SUPERADMIN_PASSWORD
    })
    super_headers = {"Authorization": f"Bearer {super_login.json()['access_token']}"}
    all_users_res = client.get(f"{settings.API_V1_STR}/users", headers=super_headers)
    assert all_users_res.status_code == 200
    assert len(all_users_res.json()) >= 2

def test_role_based_access_control():
    # Login as student
    student_login = client.post(f"{settings.API_V1_STR}/auth/login", json={
        "email": "student_test@stanford.edu",
        "password": "StudentPass@123"
    })
    student_token = student_login.json()["access_token"]
    student_headers = {"Authorization": f"Bearer {student_token}"}

    # Student cannot register new users -> 403 Forbidden
    reg_attempt = client.post(f"{settings.API_V1_STR}/auth/register-user", json={
        "email": "hacker@stanford.edu",
        "password": "HackerPass@123",
        "full_name": "Hacker",
        "role": "UNIVERSITY_ADMIN"
    }, headers=student_headers)
    assert reg_attempt.status_code == 403

    # Student cannot create a new tenant institution -> 403 Forbidden
    tenant_create_attempt = client.post(f"{settings.API_V1_STR}/tenants", json={
        "name": "Rogue University",
        "code": "ROGUE"
    }, headers=student_headers)
    assert tenant_create_attempt.status_code == 403

def test_invalid_login():
    res = client.post(f"{settings.API_V1_STR}/auth/login", json={
        "email": "nonexistent@unisphere.ai",
        "password": "WrongPassword@123"
    })
    assert res.status_code == 401

