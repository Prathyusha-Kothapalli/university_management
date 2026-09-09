from fastapi import FastAPI

from app.api.v1.universities import router as universities_router
from app.api.v1.campuses import router as campuses_router
from app.api.v1.departments import router as departments_router
from app.api.v1.academic_years import router as academic_years_router
from app.api.v1.semesters import router as semesters_router
from app.api.v1.programs import router as programs_router
from app.api.v1.roles import router as roles_router
from app.api.v1.users import router as users_router
from app.api.v1.courses import router as courses_router
from app.api.v1.course_offerings import router as course_offerings_router
from app.api.v1.course_faculty import router as course_faculty_router
from app.api.v1.course_enrollments import router as course_enrollments_router
from app.api.v1.classrooms import router as classrooms_router
from app.api.v1.timetables import router as timetables_router
from app.api.v1.attendance_sessions import router as attendance_sessions_router
from app.api.v1.attendance_records import router as attendance_records_router


app = FastAPI(
    title="UniSphere AI Backend"
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
    academic_years_router,
    prefix="/api/v1"
)

app.include_router(
    semesters_router,
    prefix="/api/v1"
)

app.include_router(
    programs_router,
    prefix="/api/v1"
)

app.include_router(
    roles_router,
    prefix="/api/v1"
)

app.include_router(
    users_router,
    prefix="/api/v1"
)

app.include_router(
    classrooms_router,
    prefix="/api/v1"
)

app.include_router(
    timetables_router,
    prefix="/api/v1"
)

app.include_router(
    attendance_sessions_router,
    prefix="/api/v1"
)

app.include_router(
    attendance_records_router,
    prefix="/api/v1"
)