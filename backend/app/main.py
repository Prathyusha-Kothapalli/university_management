from contextlib import asynccontextmanager
from fastapi import FastAPI

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

app.include_router(batch1_admissions_router, prefix="/api/v1")
app.include_router(batch1_scholarships_router, prefix="/api/v1")
app.include_router(batch1_academic_advising_router, prefix="/api/v1")
app.include_router(batch1_graduation_audit_router, prefix="/api/v1")
app.include_router(batch1_clubs_organizations_router, prefix="/api/v1")
app.include_router(batch1_approval_workflows_router, prefix="/api/v1")
app.include_router(batch1_digital_certificates_router, prefix="/api/v1")

app.include_router(
    attendance_records_router,
    prefix="/api/v1"
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

app.include_router(
    courses_router,
    prefix="/api/v1"
)


app.include_router(
    assignments_router,
    prefix="/api/v1"
)

app.include_router(
    assignment_submissions_router,
    prefix="/api/v1"
)

app.include_router(
    learning_materials_router,
    prefix="/api/v1"
)

app.include_router(
    exams_router,
    prefix="/api/v1"
)

app.include_router(
    exam_schedules_router,
    prefix="/api/v1"
)

app.include_router(
    exam_results_router,
    prefix="/api/v1"
)

app.include_router(
    transcripts_router,
    prefix="/api/v1"
)

app.include_router(
    fee_structures_router,
    prefix="/api/v1"
)

app.include_router(
    student_fees_router,
    prefix="/api/v1"
)

app.include_router(
    payments_router,
    prefix="/api/v1"
)

app.include_router(
    library_books_router,
    prefix="/api/v1"
)

app.include_router(
    book_issues_router,
    prefix="/api/v1"
)

app.include_router(
    library_fines_router,
    prefix="/api/v1"
)

app.include_router(
    hostels_router,
    prefix="/api/v1"
)

app.include_router(
    hostel_rooms_router,
    prefix="/api/v1"
)

app.include_router(
    hostel_allocations_router,
    prefix="/api/v1"
)

app.include_router(
    transport_routes_router,
    prefix="/api/v1"
)

app.include_router(
    transport_vehicles_router,
    prefix="/api/v1"
)

app.include_router(
    transport_allocations_router,
    prefix="/api/v1"
)

app.include_router(
    placement_drives_router,
    prefix="/api/v1"
)

app.include_router(
    placement_applications_router,
    prefix="/api/v1"
)

app.include_router(
    notifications_router,
    prefix="/api/v1"
)

app.include_router(
    documents_router,
    prefix="/api/v1"
)

app.include_router(
    ai_conversations_router,
    prefix="/api/v1"
)

app.include_router(
    ai_messages_router,
    prefix="/api/v1"
)

app.include_router(
    tenants_router,
    prefix="/api/v1"
)

app.include_router(
    curriculum_router,
    prefix="/api/v1"
)

app.include_router(
    exam_attempts_router,
    prefix="/api/v1"
)

app.include_router(
    payment_gateways_router,
    prefix="/api/v1"
)

app.include_router(
    ai_copilot_router,
    prefix="/api/v1"
)

app.include_router(
    student_requests_router,
    prefix="/api/v1"
)

app.include_router(
    guardians_router,
    prefix="/api/v1"
)

app.include_router(
    department_budgets_router,
    prefix="/api/v1"
)

app.include_router(
    accreditation_router,
    prefix="/api/v1"
)

app.include_router(
    transport_maintenance_router,
    prefix="/api/v1"
)

from app.api.v1.auth_expansion import router as auth_expansion_router
from app.api.v1.tenancy_expansion import router as tenancy_expansion_router
from app.api.v1.student_lifecycle import router as student_lifecycle_router
from app.api.v1.faculty_expansion import router as faculty_expansion_router
from app.api.v1.curriculum_obe import router as curriculum_obe_router
from app.api.v1.exam_expansion import router as exam_expansion_router
from app.api.v1.smart_campus_transport import router as smart_campus_transport_router
from app.api.v1.finance_expansion import router as finance_expansion_router
from app.api.v1.alumni_endowment import router as alumni_endowment_router
from app.api.v1.campus_iot_telemetry import router as campus_iot_telemetry_router
from app.api.v1.evaluation_ast_grading import router as evaluation_ast_grading_router
from app.api.v1.hostel_expansion import router as hostel_expansion_router

app.include_router(
    auth_expansion_router,
    prefix="/api/v1"
)

app.include_router(
    tenancy_expansion_router,
    prefix="/api/v1"
)

app.include_router(
    student_lifecycle_router,
    prefix="/api/v1"
)

app.include_router(
    faculty_expansion_router,
    prefix="/api/v1"
)

app.include_router(
    curriculum_obe_router,
    prefix="/api/v1"
)

app.include_router(
    exam_expansion_router,
    prefix="/api/v1"
)

app.include_router(
    smart_campus_transport_router,
    prefix="/api/v1"
)

app.include_router(
    finance_expansion_router,
    prefix="/api/v1"
)

app.include_router(
    alumni_endowment_router,
    prefix="/api/v1"
)

app.include_router(
    campus_iot_telemetry_router,
    prefix="/api/v1"
)

app.include_router(
    evaluation_ast_grading_router,
    prefix="/api/v1"
)

app.include_router(
    hostel_expansion_router,
    prefix="/api/v1"
)

app.include_router(
    health_center_router,
    prefix="/api/v1"
)

app.include_router(
    canteen_router,
    prefix="/api/v1"
)

app.include_router(
    lost_and_found_router,
    prefix="/api/v1"
)


@app.get("/health/")
def health_check():
    return {
        "status": "ok",
        "service": "backend",
        "environment": settings.ENVIRONMENT
    }

