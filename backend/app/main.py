from fastapi import FastAPI

from app.api.v1.auth import router as auth_router
from app.api.v1.users import router as users_router
from app.api.v1.universities import router as universities_router
from app.api.v1.campuses import router as campuses_router
from app.api.v1.departments import router as departments_router
from app.api.v1.programs import router as programs_router
from app.api.v1.academic_years import router as academic_years_router
from app.api.v1.semesters import router as semesters_router
from app.api.v1.students import router as students_router
from app.api.v1.faculty import router as faculty_router


app = FastAPI(
    title="UniSphere AI Backend",
    version="1.0.0"
)


app.include_router(
    auth_router,
    prefix="/api/v1"
)

app.include_router(
    users_router,
    prefix="/api/v1"
)

app.include_router(
    universities_router,
    prefix="/api/v1"
)

app.include_router(
    campuses_router,
    prefix="/api/v1"
)

app.include_router(
    departments_router,
    prefix="/api/v1"
)

app.include_router(
    programs_router,
    prefix="/api/v1"
)

app.include_router(
    academic_years_router,
    prefix="/api/v1"
)

app.include_router(
    semesters_router,
    prefix="/api/v1"
)

app.include_router(
    students_router,
    prefix="/api/v1"
)

app.include_router(
    faculty_router,
    prefix="/api/v1"
)


@app.get("/health/")
def health_check():
    return {
        "status": "ok",
        "service": "UniSphere AI Backend"
    }