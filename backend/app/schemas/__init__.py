# Schemas package initialization
from app.schemas.role import (
    RoleCreate,
    RoleUpdate,
    RoleResponse,
)

from app.schemas.user import (
    UserCreate,
    UserUpdate,
    UserResponse,
)

from app.schemas.university import (
    UniversityCreate,
    UniversityUpdate,
    UniversityResponse,
)

from app.schemas.campus import (
    CampusCreate,
    CampusUpdate,
    CampusResponse,
)

from app.schemas.department import (
    DepartmentCreate,
    DepartmentUpdate,
    DepartmentResponse,
)

from app.schemas.academic_year import (
    AcademicYearCreate,
    AcademicYearUpdate,
    AcademicYearResponse,
)

from app.schemas.semester import (
    SemesterCreate,
    SemesterUpdate,
    SemesterResponse,
)

from app.schemas.program import (
    ProgramCreate,
    ProgramUpdate,
    ProgramResponse,
)

from app.schemas.course import (
    CourseCreate,
    CourseUpdate,
    CourseResponse,
)

from app.schemas.course_offering import (
    CourseOfferingCreate,
    CourseOfferingUpdate,
    CourseOfferingResponse,
)

from app.schemas.course_faculty import (
    CourseFacultyCreate,
    CourseFacultyUpdate,
    CourseFacultyResponse,
)

from app.schemas.course_enrollment import (
    CourseEnrollmentCreate,
    CourseEnrollmentUpdate,
    CourseEnrollmentResponse,
)