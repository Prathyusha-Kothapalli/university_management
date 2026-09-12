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
from app.api.v1.courses import router as courses_router
from app.api.v1.assignments import router as assignments_router

from app.api.v1.assignment_submissions import router as assignment_submissions_router
from app.api.v1.learning_materials import router as learning_materials_router
from app.api.v1.exams import router as exams_router
from app.api.v1.exam_schedules import router as exam_schedules_router
from app.api.v1.exam_results import router as exam_results_router
from app.api.v1.transcripts import router as transcripts_router
from app.api.v1.fee_structures import router as fee_structures_router
from app.api.v1.student_fees import router as student_fees_router
from app.api.v1.payments import router as payments_router
from app.api.v1.library_books import router as library_books_router
from app.api.v1.book_issues import router as book_issues_router
from app.api.v1.library_fines import router as library_fines_router
from app.api.v1.hostels import router as hostels_router
from app.api.v1.hostel_rooms import router as hostel_rooms_router
from app.api.v1.hostel_allocations import router as hostel_allocations_router
from app.api.v1.transport_routes import router as transport_routes_router
from app.api.v1.transport_vehicles import router as transport_vehicles_router
from app.api.v1.transport_allocations import router as transport_allocations_router
from app.api.v1.placement_drives import router as placement_drives_router
from app.api.v1.placement_applications import router as placement_applications_router
from app.api.v1.notifications import router as notifications_router
from app.api.v1.documents import router as documents_router
from app.api.v1.ai_conversations import router as ai_conversations_router
from app.api.v1.ai_messages import router as ai_messages_router
from app.api.v1.tenants import router as tenants_router
from app.api.v1.curriculum import router as curriculum_router
from app.api.v1.exam_attempts import router as exam_attempts_router
from app.api.v1.payment_gateways import router as payment_gateways_router
from app.api.v1.ai_copilot import router as ai_copilot_router
from app.api.v1.student_requests import router as student_requests_router
from app.api.v1.guardians import router as guardians_router
from app.api.v1.department_budgets import router as department_budgets_router
from app.api.v1.accreditation import router as accreditation_router
from app.api.v1.transport_maintenance import router as transport_maintenance_router
from app.api.v1.attendance_records import router as attendance_records_router

app = FastAPI(
    title="UniSphere AI Backend",
    version="1.0.0"
)

app.include_router(
    attendance_records_router,
    prefix="/api/v1"
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


@app.get("/health/")
def health_check():
    return {
        "status": "ok",
        "service": "UniSphere AI Backend"
    }