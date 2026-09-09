# Models package initialization
from app.models.role import Role
from app.models.user import User

__all__ = ["Role", "User"]
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
    "AttendanceRecord"
]