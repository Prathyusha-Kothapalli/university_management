import os
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "UniSphere AI Backend"
    VERSION: str = "0.1.0"
    API_V1_STR: str = "/api/v1"
    
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL", 
        "sqlite:///./unisphere.db" if os.getenv("ENVIRONMENT") != "production" else "postgresql://unisphere_user:unisphere_password@localhost:5432/unisphere_db"
    )
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")

    # JWT Authentication
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY", "unisphere-ai-super-secret-key-change-in-production-2026")
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 24 hours

    # Super Admin Seed Defaults
    DEFAULT_SUPERADMIN_EMAIL: str = os.getenv("DEFAULT_SUPERADMIN_EMAIL", "superadmin@unisphere.ai")
    DEFAULT_SUPERADMIN_PASSWORD: str = os.getenv("DEFAULT_SUPERADMIN_PASSWORD", "SuperAdmin@123")

    model_config = SettingsConfigDict(case_sensitive=True)

settings = Settings()

