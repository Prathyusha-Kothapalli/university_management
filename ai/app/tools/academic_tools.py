from typing import Dict, Any
from .base_tool import BaseTool

class GetStudentAcademicsTool(BaseTool):
    def __init__(self):
        super().__init__(
            name="get_student_academics",
            description="Retrieves GPA, credit breakdown, and degree completion for a student",
            required_role="student"
        )

    def execute(self, arguments: Dict[str, Any], user_id: str, user_role: str) -> Dict[str, Any]:
        return {
            "student_id": user_id,
            "cgpa": 3.84,
            "sgpa": 3.90,
            "credits_completed": 76,
            "total_credits_required": 120,
            "completion_percentage": 63.3,
            "major": "B.Tech Computer Science & Engineering",
            "academic_standing": "Good Standing (Top 5%)"
        }

class GetAttendanceSummaryTool(BaseTool):
    def __init__(self):
        super().__init__(
            name="get_attendance_summary",
            description="Retrieves course-wise attendance percentages and detention warning thresholds",
            required_role="student"
        )

    def execute(self, arguments: Dict[str, Any], user_id: str, user_role: str) -> Dict[str, Any]:
        return {
            "student_id": user_id,
            "overall_attendance_pct": 94.5,
            "classes_attended": 18,
            "total_classes": 19,
            "detention_risk": False,
            "courses": [
                {"code": "CS-401", "name": "Machine Learning", "attendance_pct": 95.0},
                {"code": "CS-302", "name": "Data Structures", "attendance_pct": 94.0}
            ]
        }

class CalculateGpaTool(BaseTool):
    def __init__(self):
        super().__init__(
            name="calculate_gpa",
            description="Calculates 'What-If' target GPA based on expected course grades",
            required_role="student"
        )

    def execute(self, arguments: Dict[str, Any], user_id: str, user_role: str) -> Dict[str, Any]:
        target_gpa = arguments.get("target_gpa", 3.90)
        current_gpa = 3.84
        current_credits = 76
        sem_credits = 18

        required_grade_points = (target_gpa * (current_credits + sem_credits) - current_gpa * current_credits) / sem_credits
        return {
            "current_gpa": current_gpa,
            "target_gpa": target_gpa,
            "required_semester_gpa": round(min(4.0, max(2.0, required_grade_points)), 2),
            "feasible": required_grade_points <= 4.0
        }
