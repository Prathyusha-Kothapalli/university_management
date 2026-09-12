from typing import Set, Dict

class ToolPermissionValidator:
    """
    Strict Role-Based Tool Authorization Matrix for UniSphere AI Agents.
    Prevents role elevation or tool execution outside user privileges.
    """
    def __init__(self):
        self.role_tool_matrix: Dict[str, Set[str]] = {
            "student": {
                "get_student_academics",
                "get_attendance_summary",
                "get_enrolled_courses",
                "get_assignments",
                "submit_assignment",
                "get_exam_results",
                "calculate_gpa",
                "get_fee_ledger",
                "search_library_books",
                "get_bus_schedule",
                "get_hostel_tickets",
                "get_placement_drives"
            },
            "faculty": {
                "get_faculty_courses",
                "mark_attendance_session",
                "grade_assignment_submission",
                "get_course_roster",
                "submit_exam_marks",
                "get_faculty_schedule",
                "search_library_books",
                "file_patent_disclosure"
            },
            "hod": {
                "get_dept_analytics",
                "get_faculty_workload",
                "get_at_risk_students",
                "approve_syllabus_revision",
                "view_dept_budget",
                "get_dept_placement_stats",
                "dispatch_emergency_alert"
            },
            "parent": {
                "get_linked_student_academics",
                "get_linked_student_attendance",
                "get_linked_student_fees",
                "schedule_ptm_slot",
                "send_advisor_message"
            },
            "librarian": {
                "search_library_books",
                "issue_book",
                "return_book",
                "calculate_overdue_fine",
                "get_borrower_history",
                "add_new_ebook"
            },
            "finance": {
                "get_student_fee_status",
                "process_fee_payment",
                "generate_fee_receipt",
                "get_defaulters_ledger",
                "calculate_installment_plan",
                "process_refund_claim"
            },
            "exam": {
                "create_exam_schedule",
                "allocate_exam_seats",
                "verify_attendance_clearance",
                "publish_semester_results",
                "generate_hall_ticket",
                "issue_plagiarism_certificate"
            },
            "placement": {
                "create_placement_drive",
                "check_drive_eligibility",
                "shortlist_candidates",
                "verify_offer_letter",
                "get_placement_analytics"
            },
            "admin": {
                "get_system_audit_log",
                "manage_user_roles",
                "dispatch_emergency_alert",
                "get_data_export",
                "configure_mfa_settings"
            },
            "super_admin": {
                "*"  # Super admin has unrestricted access to all tools
            }
        }

    def is_tool_authorized(self, user_role: str, tool_name: str) -> bool:
        role_lower = user_role.lower()
        allowed_tools = self.role_tool_matrix.get(role_lower, set())
        if "*" in allowed_tools:
            return True
        return tool_name in allowed_tools
