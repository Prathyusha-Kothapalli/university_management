<<<<<<< HEAD
import 'dart:async';
import '../models/login_request.dart';
import '../models/login_response.dart';
import '../models/register_request.dart';
import '../models/user.dart';
import '../models/user_profile.dart';
import '../core/network/api_exceptions.dart';

class MockDataService {
  // Mock In-Memory User Database
  static final List<User> _mockUsers = [
    const User(
      id: 'usr_std_1001',
      name: 'Alex Mercer',
      email: 'student@university.edu',
      phone: '+1 (555) 234-5678',
      role: 'student',
      department: 'Computer Science & Engineering',
      studentId: 'UNIV-2023-CS-042',
      avatarUrl: 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=200',
    ),
    const User(
      id: 'usr_fac_2001',
      name: 'Dr. Evelyn Wright',
      email: 'faculty@university.edu',
      phone: '+1 (555) 345-6789',
      role: 'faculty',
      department: 'Electrical Engineering',
      studentId: 'FAC-ENG-108',
      avatarUrl: 'https://images.unsplash.com/photo-1580489944761-15a19d654956?w=200',
    ),
    const User(
      id: 'usr_adm_3001',
      name: 'Marcus Vance',
      email: 'admin@university.edu',
      phone: '+1 (555) 456-7890',
      role: 'admin',
      department: 'Registrar & Academic Operations',
      studentId: 'ADM-EXEC-001',
    ),
  ];

  static Future<LoginResponse> mockLogin(LoginRequest request) async {
    await Future.delayed(const Duration(milliseconds: 650)); // Realistic network latency

    final email = request.email.trim().toLowerCase();
    final password = request.password.trim();

    // Check credentials
    if (password.length < 6) {
      throw const UnauthorizedException(message: 'Invalid email or password.');
    }

    User? foundUser;
    for (final u in _mockUsers) {
      if (u.email.toLowerCase() == email) {
        foundUser = u;
        break;
      }
    }

    // Default to an authenticated mock student if email doesn't strictly match sample emails
    foundUser ??= User(
      id: 'usr_std_${DateTime.now().millisecondsSinceEpoch.toString().substring(7)}',
      name: email.split('@').first.replaceAll('.', ' ').toUpperCase(),
      email: email,
      phone: '+1 (555) 888-9999',
      role: 'student',
      department: 'Information Technology',
      studentId: 'UNIV-2026-IT-109',
    );

    final mockToken = 'mock_jwt_token_${DateTime.now().millisecondsSinceEpoch}_${foundUser.id}';
    return LoginResponse(
      accessToken: mockToken,
      tokenType: 'bearer',
      expiresIn: 86400,
      user: foundUser,
    );
  }

  static Future<LoginResponse> mockRegister(RegisterRequest request) async {
    await Future.delayed(const Duration(milliseconds: 750));

    final newUser = User(
      id: 'usr_reg_${DateTime.now().millisecondsSinceEpoch}',
      name: request.name,
      email: request.email,
      phone: request.phone,
      role: request.role,
      department: request.department ?? 'General Sciences',
      studentId: 'UNIV-2026-REG-${DateTime.now().millisecond}',
      createdAt: DateTime.now(),
    );

    _mockUsers.add(newUser);

    final mockToken = 'mock_jwt_token_${DateTime.now().millisecondsSinceEpoch}_${newUser.id}';
    return LoginResponse(
      accessToken: mockToken,
      tokenType: 'bearer',
      expiresIn: 86400,
      user: newUser,
    );
  }

  static Future<UserProfile> mockGetProfile(User user) async {
    await Future.delayed(const Duration(milliseconds: 400));
    return UserProfile(
      user: user,
      gpa: 3.85,
      attendancePercentage: 94.2,
      enrolledCredits: 18,
      totalCreditsCompleted: 74,
      currentSemester: 'Semester 5 (Fall 2026)',
      academicProgram: 'B.S. in Computer Science',
      enrollmentStatus: 'Active - Full Time',
      emergencyContact: '+1 (555) 999-0000',
    );
  }

  static Future<User> mockUpdateProfile(User current, {String? name, String? phone}) async {
    await Future.delayed(const Duration(milliseconds: 500));
    final updated = current.copyWith(
      name: name ?? current.name,
      phone: phone ?? current.phone,
    );

    final idx = _mockUsers.indexWhere((u) => u.id == current.id);
    if (idx != -1) {
      _mockUsers[idx] = updated;
    }
    return updated;
  }
=======
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
>>>>>>> 29907a7 (added flutter)
}
