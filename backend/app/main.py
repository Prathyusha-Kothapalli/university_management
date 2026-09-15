from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.database.session import init_db
from app.api.v1 import api_v1_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize database tables and default seed data
    init_db()
    yield

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    lifespan=lifespan
)

# Set up CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API v1 router
app.include_router(api_v1_router, prefix=settings.API_V1_STR)

@app.get("/")
def read_root():
    return {
        "status": "healthy",
        "service": settings.PROJECT_NAME,
        "version": settings.VERSION,
        "message": "Welcome to UniSphere AI Multi-Tenant Platform Backend API Foundation"
    }

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "backend",
        "environment": settings.ENVIRONMENT
    }

