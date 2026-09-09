import '../models/user.dart';
import '../models/login_response.dart';

/// Embedded Mock Data Provider
/// Allows complete end-to-end testing of the Flutter application when the backend API
/// server is offline or unreachable.
class MockDataService {
  MockDataService._();

  static User get defaultStudent => const User(
        id: 'usr_student_001',
        name: 'Alex Johnson',
        email: 'alex.johnson@university.edu',
        phone: '+1 (555) 234-5678',
        role: UserRole.student,
        department: 'Artificial Intelligence & Data Science',
        studentId: 'US-2026-AI-042',
        enrolledYear: '2024 - 2028 (Year 3)',
        gpa: 3.86,
        attendanceRate: 94.8,
      );

  static User get defaultFaculty => const User(
        id: 'usr_faculty_002',
        name: 'Dr. Sarah Mitchell',
        email: 'sarah.mitchell@university.edu',
        phone: '+1 (555) 987-6543',
        role: UserRole.faculty,
        department: 'Department of Computer Science',
        studentId: 'FAC-ENG-108',
        enrolledYear: 'Tenured Faculty',
        gpa: 4.0,
        attendanceRate: 99.1,
      );

  static LoginResponse get studentLoginResponse => LoginResponse(
        accessToken: 'mock_jwt_token_header.payload.unisphere_signature_student_2026',
        refreshToken: 'mock_refresh_token_student_2026',
        tokenType: 'Bearer',
        expiresIn: 86400,
        user: defaultStudent,
      );

  static LoginResponse get facultyLoginResponse => LoginResponse(
        accessToken: 'mock_jwt_token_header.payload.unisphere_signature_faculty_2026',
        refreshToken: 'mock_refresh_token_faculty_2026',
        tokenType: 'Bearer',
        expiresIn: 86400,
        user: defaultFaculty,
      );

  static List<Map<String, dynamic>> get todaySchedule => [
        {
          'code': 'CS-401',
          'name': 'Deep Learning & Neural Architectures',
          'time': '09:00 AM - 10:30 AM',
          'room': 'Hall C-302',
          'instructor': 'Prof. A. Vance',
          'colorHex': 0xFF1E40AF,
          'status': 'Ongoing',
        },
        {
          'code': 'DS-310',
          'name': 'Big Data Distributed Systems',
          'time': '11:00 AM - 12:30 PM',
          'room': 'Lab 4B',
          'instructor': 'Dr. S. Mitchell',
          'colorHex': 0xFF0284C7,
          'status': 'Upcoming',
        },
        {
          'code': 'MATH-250',
          'name': 'Stochastic Calculus & Linear Optimization',
          'time': '02:00 PM - 03:30 PM',
          'room': 'Auditorium 1',
          'instructor': 'Dr. K. Rao',
          'colorHex': 0xFF6366F1,
          'status': 'Upcoming',
        },
      ];

  static List<Map<String, dynamic>> get quickModules => [
        {
          'title': 'Courses',
          'subtitle': '5 Active Semesters',
          'icon': 'school_rounded',
          'colorHex': 0xFF1E40AF,
        },
        {
          'title': 'Timetable',
          'subtitle': 'Weekly Calendar',
          'icon': 'calendar_month_rounded',
          'colorHex': 0xFF0284C7,
        },
        {
          'title': 'Exams & Grades',
          'subtitle': 'Fall 2026 Results',
          'icon': 'analytics_rounded',
          'colorHex': 0xFF10B981,
        },
        {
          'title': 'Tuition & Fees',
          'subtitle': 'Paid in Full',
          'icon': 'account_balance_wallet_rounded',
          'colorHex': 0xFFF59E0B,
        },
        {
          'title': 'Digital Library',
          'subtitle': '42,000+ Journals',
          'icon': 'menu_book_rounded',
          'colorHex': 0xFF8B5CF6,
        },
        {
          'title': 'Campus Services',
          'subtitle': 'Hostel & Transport',
          'icon': 'domain_rounded',
          'colorHex': 0xFFEC4899,
        },
      ];
}
