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

from app.api.v1.analytics import router as analytics_router
from app.api.v1.scholarships import router as scholarships_router

def include_v1_routers(app: FastAPI):
    app.include_router(analytics_router, prefix="/api/v1")
    app.include_router(scholarships_router, prefix="/api/v1")