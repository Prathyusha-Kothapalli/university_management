import logging
from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.core.config import settings
from app.models.tenant import Base, Tenant
from app.models.user import User, UserRole
from app.core.security import get_password_hash

logger = logging.getLogger(__name__)

# Engine configuration with sqlite/postgres support
connect_args = {"check_same_thread": False} if settings.DATABASE_URL.startswith("sqlite") else {}

engine = create_engine(
    settings.DATABASE_URL,
    connect_args=connect_args,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    """Create tables and populate default seed data (SuperAdmin and demo tenants)"""
    Base.metadata.create_all(bind=engine)
    
    db: Session = SessionLocal()
    try:
        # 1. Seed Super Admin
        super_admin = db.query(User).filter(User.email == settings.DEFAULT_SUPERADMIN_EMAIL).first()
        if not super_admin:
            super_admin = User(
                email=settings.DEFAULT_SUPERADMIN_EMAIL,
                hashed_password=get_password_hash(settings.DEFAULT_SUPERADMIN_PASSWORD),
                full_name="UniSphere Global SuperAdmin",
                role=UserRole.SUPER_ADMIN,
                tenant_id=None,
                is_active=True
            )
            db.add(super_admin)
            db.commit()
            logger.info("Default Super Admin created: %s", settings.DEFAULT_SUPERADMIN_EMAIL)
        
        # 2. Seed Demo University Tenant 1: Stanford University
        stanford = db.query(Tenant).filter(Tenant.code == "STANFORD").first()
        if not stanford:
            stanford = Tenant(
                name="Stanford University",
                code="STANFORD",
                domain="stanford.edu",
                description="Stanford University Campus & Academic Portal",
                is_active=True
            )
            db.add(stanford)
            db.commit()
            db.refresh(stanford)

            # Stanford University Admin
            stanford_admin = User(
                email="admin@stanford.edu",
                hashed_password=get_password_hash("Admin@123"),
                full_name="Stanford Admin",
                role=UserRole.UNIVERSITY_ADMIN,
                tenant_id=stanford.id,
                department="Central Administration",
                is_active=True
            )
            # Stanford Faculty
            stanford_faculty = User(
                email="prof.alan@stanford.edu",
                hashed_password=get_password_hash("Faculty@123"),
                full_name="Prof. Alan Turing",
                role=UserRole.FACULTY,
                tenant_id=stanford.id,
                department="Computer Science",
                is_active=True
            )
            # Stanford Student
            stanford_student = User(
                email="john.doe@stanford.edu",
                hashed_password=get_password_hash("Student@123"),
                full_name="John Doe",
                role=UserRole.STUDENT,
                tenant_id=stanford.id,
                department="Computer Science",
                is_active=True
            )
            db.add_all([stanford_admin, stanford_faculty, stanford_student])
            db.commit()
            logger.info("Seeded Stanford University demo tenant and users")

        # 3. Seed Demo University Tenant 2: MIT
        mit = db.query(Tenant).filter(Tenant.code == "MIT").first()
        if not mit:
            mit = Tenant(
                name="Massachusetts Institute of Technology",
                code="MIT",
                domain="mit.edu",
                description="MIT Multi-Campus Academic System",
                is_active=True
            )
            db.add(mit)
            db.commit()
            db.refresh(mit)

            # MIT Admin
            mit_admin = User(
                email="admin@mit.edu",
                hashed_password=get_password_hash("Admin@123"),
                full_name="MIT Admin",
                role=UserRole.UNIVERSITY_ADMIN,
                tenant_id=mit.id,
                department="Information Services & Technology",
                is_active=True
            )
            db.add(mit_admin)
            db.commit()
            logger.info("Seeded MIT demo tenant and users")

    except Exception as e:
        logger.error("Error during database initialization: %s", e)
        db.rollback()
    finally:
        db.close()
