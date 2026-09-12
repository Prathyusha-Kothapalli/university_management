# Models package initialization
from app.models.role import Role
from app.models.user import User
from app.models.university import University
from app.models.campus import Campus
from app.models.department import Department
from app.models.program import Program
from app.models.academic_year import AcademicYear
from app.models.semester import Semester

from app.models.student import Student
from app.models.faculty import Faculty
from app.models.student_guardian import StudentGuardian
from app.models.faculty_department import FacultyDepartment

from app.models.course import Course
from app.models.course_offering import CourseOffering
from app.models.course_faculty import CourseFaculty
from app.models.course_enrollment import CourseEnrollment

from app.models.classroom import Classroom
from app.models.timetable import Timetable
from app.models.attendance_session import AttendanceSession
from app.models.attendance_record import AttendanceRecord

from app.models.assignment import Assignment
from app.models.assignment_submission import AssignmentSubmission
from app.models.learning_material import LearningMaterial

from app.models.exam import Exam
from app.models.exam_schedule import ExamSchedule
from app.models.exam_result import ExamResult
from app.models.transcript import Transcript

from app.models.fee_structure import FeeStructure
from app.models.student_fee import StudentFee
from app.models.payment import Payment

from app.models.library_book import LibraryBook
from app.models.book_issue import BookIssue
from app.models.library_fine import LibraryFine

from app.models.hostel import Hostel
from app.models.hostel_room import HostelRoom
from app.models.hostel_allocation import HostelAllocation
from app.models.hostel_expansion import (
    HostelBuilding,
    HostelFloor,
    HostelBed,
    HostelApplication,
    HostelTransfer,
    HostelCheckIn,
    HostelCheckOut,
    HostelAttendance,
    HostelVisitor,
    HostelComplaint,
    HostelMaintenanceRequest,
    HostelStaff,
    HostelShift,
    HostelInventory,
    HostelMess,
    HostelMealFeedback,
    HostelIncident,
    HostelAnnouncement,
)
from app.models.transport_route import TransportRoute
from app.models.transport_vehicle import TransportVehicle
from app.models.transport_allocation import TransportAllocation

from app.models.placement_drive import PlacementDrive
from app.models.placement_application import PlacementApplication
from app.models.notification import Notification
from app.models.document import Document
from app.models.ai_conversation import AIConversation
from app.models.ai_message import AIMessage
from app.models.user_session import UserSession
from app.models.mfa_recovery import MfaRecoveryCode
from app.models.auth_policy import AuthPolicy
from app.models.tenant_branding import TenantBranding
from app.models.tenant_invitation import TenantInvitation
from app.models.tenant_storage_log import TenantStorageLog
from app.models.tenant_feature_flag import TenantFeatureFlag
from app.models.disciplinary_record import DisciplinaryRecord
from app.models.student_lifecycle import (
    AcademicHold,
    StudentConductCase,
    StudentAchievement,
    SupportCase,
    AcademicGoal,
)
from app.models.faculty_expansion import (
    FacultyQualification,
    FacultyAppraisal,
    ResearchProject,
    ResearchPublication,
)
from app.models.curriculum_obe import (
    CourseOutcome,
    ProgramOutcome,
    CoPoMapping,
    WaitlistEntry,
)
from app.models.exam_expansion import (
    QuestionBankItem,
    ExamPaper,
    ExamPaperQuestion,
    ProctorTelemetryLog,
)
from app.models.smart_campus_transport import (
    VehicleFuelLog,
    VehicleMaintenanceLog,
    HostelMaintenanceTicket,
)
from app.models.finance_expansion import (
    FeeInstallmentPlan,
    FeeInstallment,
    PaymentGatewayConfig,
    PaymentTransaction,
)
from app.models.alumni_endowment import (
    AlumniProfile,
    EndowmentFund,
    AlumniDonation,
)
from app.models.campus_iot_telemetry import (
    IotDevice,
    IotTelemetryLog,
    SmartBuildingControl,
)
from app.models.evaluation_ast_grading import (
    CodeSubmissionAst,
    PlagiarismScanReport,
)


__all__ = [
    "Role",
    "User",
    "University",
    "Campus",
    "Department",
    "Program",
    "AcademicYear",
    "Semester",
    "Student",
    "Faculty",
    "StudentGuardian",
    "FacultyDepartment",
    "Course",
    "CourseOffering",
    "CourseFaculty",
    "CourseEnrollment",
    "Classroom",
    "Timetable",
    "AttendanceSession",
    "AttendanceRecord",
    "Assignment",
    "AssignmentSubmission",
    "LearningMaterial",
    "Exam",
    "ExamSchedule",
    "ExamResult",
    "Transcript",
    "FeeStructure",
    "StudentFee",
    "Payment",
    "LibraryBook",
    "BookIssue",
    "LibraryFine",
    "Hostel",
    "HostelRoom",
    "HostelAllocation",
    "TransportRoute",
    "TransportVehicle",
    "TransportAllocation",
    "PlacementDrive",
    "PlacementApplication",
    "Notification",
    "Document",
    "AIConversation",
    "AIMessage",
    "UserSession",
    "MfaRecoveryCode",
    "AuthPolicy",
    "TenantBranding",
    "TenantInvitation",
    "TenantStorageLog",
    "TenantFeatureFlag",
    "AcademicHold",
    "DisciplinaryRecord",
    "StudentConductCase",
    "StudentAchievement",
    "SupportCase",
    "AcademicGoal",
    "FacultyQualification",
    "FacultyAppraisal",
    "ResearchProject",
    "ResearchPublication",
    "CourseOutcome",
    "ProgramOutcome",
    "CoPoMapping",
    "WaitlistEntry",
    "QuestionBankItem",
    "ExamPaper",
    "ExamPaperQuestion",
    "ProctorTelemetryLog",
    "VehicleFuelLog",
    "VehicleMaintenanceLog",
    "HostelMaintenanceTicket",
    "FeeInstallmentPlan",
    "FeeInstallment",
    "PaymentGatewayConfig",
    "PaymentTransaction",
    "AlumniProfile",
    "EndowmentFund",
    "AlumniDonation",
    "IotDevice",
    "IotTelemetryLog",
    "SmartBuildingControl",
    "CodeSubmissionAst",
    "PlagiarismScanReport",
]