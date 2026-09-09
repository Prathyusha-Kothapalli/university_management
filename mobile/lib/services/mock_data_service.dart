<<<<<<< HEAD
import '../models/campus_features.dart';
import '../models/login_response.dart';
import '../models/user.dart';

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

  // Today's schedule summary
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

  // Full weekly timetable
  static List<Map<String, dynamic>> get weeklyTimetable => [
        {
          'day': 'Monday',
          'code': 'CS-401',
          'title': 'Deep Learning & Neural Architectures',
          'time': '09:00 AM - 10:30 AM',
          'room': 'Hall C-302',
          'instructor': 'Prof. A. Vance',
          'colorHex': 0xFF1E40AF,
        },
        {
          'day': 'Monday',
          'code': 'DS-310',
          'title': 'Big Data Distributed Systems',
          'time': '11:00 AM - 12:30 PM',
          'room': 'Lab 4B',
          'instructor': 'Dr. S. Mitchell',
          'colorHex': 0xFF0284C7,
        },
        {
          'day': 'Tuesday',
          'code': 'AI-480',
          'title': 'Autonomous Robotics & Computer Vision',
          'time': '10:00 AM - 11:30 AM',
          'room': 'Robotics Wing R1',
          'instructor': 'Dr. E. Thorne',
          'colorHex': 0xFF10B981,
        },
        {
          'day': 'Wednesday',
          'code': 'ETH-102',
          'title': 'AI Safety & Technological Ethics',
          'time': '01:00 PM - 02:30 PM',
          'room': 'Seminar Hall 2',
          'instructor': 'Prof. L. Chen',
          'colorHex': 0xFF8B5CF6,
        },
        {
          'day': 'Thursday',
          'code': 'DS-310',
          'title': 'Distributed Cloud Lab Workshop',
          'time': '09:30 AM - 12:00 PM',
          'room': 'Cloud Server Lab',
          'instructor': 'Dr. S. Mitchell',
          'colorHex': 0xFF0284C7,
        },
        {
          'day': 'Friday',
          'code': 'MATH-250',
          'title': 'Applied Convex Optimization',
          'time': '02:00 PM - 03:30 PM',
          'room': 'Auditorium 1',
          'instructor': 'Dr. K. Rao',
          'colorHex': 0xFF6366F1,
        },
      ];

  // Subject-wise Attendance
  static List<AttendanceRecord> get attendanceRecords => [
        const AttendanceRecord(
          id: 'att_1',
          courseCode: 'CS-401',
          courseName: 'Deep Learning & Neural Architectures',
          attendedHours: 38,
          totalHours: 40,
          instructor: 'Prof. A. Vance',
        ),
        const AttendanceRecord(
          id: 'att_2',
          courseCode: 'DS-310',
          courseName: 'Big Data Distributed Systems',
          attendedHours: 32,
          totalHours: 35,
          instructor: 'Dr. S. Mitchell',
        ),
        const AttendanceRecord(
          id: 'att_3',
          courseCode: 'MATH-250',
          courseName: 'Stochastic Calculus & Linear Optimization',
          attendedHours: 28,
          totalHours: 30,
          instructor: 'Dr. K. Rao',
        ),
        const AttendanceRecord(
          id: 'att_4',
          courseCode: 'AI-480',
          courseName: 'Autonomous Robotics & Computer Vision',
          attendedHours: 26,
          totalHours: 30,
          instructor: 'Dr. E. Thorne',
        ),
        const AttendanceRecord(
          id: 'att_5',
          courseCode: 'ETH-102',
          courseName: 'AI Safety & Technological Ethics',
          attendedHours: 19,
          totalHours: 20,
          instructor: 'Prof. L. Chen',
        ),
      ];

  // Coursework Assignments
  static List<AssignmentItem> get assignments => [
        const AssignmentItem(
          id: 'asg_1',
          courseCode: 'CS-401',
          title: 'Transformer Architecture Implementation',
          description: 'Implement multi-head self-attention in PyTorch from scratch.',
          dueDate: 'Sep 18, 2026',
          maxScore: 100,
          status: 'Pending',
        ),
        const AssignmentItem(
          id: 'asg_2',
          courseCode: 'DS-310',
          title: 'MapReduce Distributed Log Analyzer',
          description: 'Process 10GB web access logs using PySpark and generate analytics.',
          dueDate: 'Sep 22, 2026',
          maxScore: 100,
          status: 'Pending',
        ),
        const AssignmentItem(
          id: 'asg_3',
          courseCode: 'MATH-250',
          title: 'Constrained Lagrangian Dual Problem Set',
          description: 'Solve analytical optimization problems with KKT conditions.',
          dueDate: 'Sep 05, 2026',
          maxScore: 50,
          obtainedScore: 48,
          status: 'Graded',
        ),
        const AssignmentItem(
          id: 'asg_4',
          courseCode: 'ETH-102',
          title: 'Algorithmic Fairness Case Study',
          description: 'Essay analyzing bias mitigation in automated medical diagnosis.',
          dueDate: 'Aug 29, 2026',
          maxScore: 50,
          obtainedScore: 46,
          status: 'Graded',
        ),
      ];

  // Examination Schedule
  static List<ExamItem> get examSchedule => [
        const ExamItem(
          id: 'ex_1',
          courseCode: 'CS-401',
          courseTitle: 'Deep Learning Midterms',
          date: 'Oct 12, 2026',
          time: '09:30 AM - 12:30 PM',
          hall: 'Examination Hall B-2',
          seat: 'Desk #42',
        ),
        const ExamItem(
          id: 'ex_2',
          courseCode: 'DS-310',
          courseTitle: 'Distributed Systems Written Exam',
          date: 'Oct 15, 2026',
          time: '02:00 PM - 05:00 PM',
          hall: 'Main Auditorium',
          seat: 'Desk #118',
        ),
        const ExamItem(
          id: 'ex_3',
          courseCode: 'MATH-250',
          courseTitle: 'Stochastic Calculus Comprehensive',
          date: 'Oct 19, 2026',
          time: '09:30 AM - 12:30 PM',
          hall: 'Math Complex Room 10',
          seat: 'Desk #27',
        ),
      ];

  // Exam Results & Transcripts
  static List<ExamResultItem> get examResults => [
        const ExamResultItem(
          id: 'res_1',
          courseCode: 'CS-301',
          courseTitle: 'Data Structures & Algorithms',
          credits: 4,
          grade: 'A+',
          gradePoint: 4.0,
        ),
        const ExamResultItem(
          id: 'res_2',
          courseCode: 'CS-302',
          courseTitle: 'Operating Systems & Concurrency',
          credits: 4,
          grade: 'A',
          gradePoint: 4.0,
        ),
        const ExamResultItem(
          id: 'res_3',
          courseCode: 'AI-201',
          courseTitle: 'Introduction to Artificial Intelligence',
          credits: 3,
          grade: 'A-',
          gradePoint: 3.7,
        ),
        const ExamResultItem(
          id: 'res_4',
          courseCode: 'MATH-102',
          courseTitle: 'Multivariate Calculus & Linear Algebra',
          credits: 4,
          grade: 'A',
          gradePoint: 4.0,
        ),
      ];

  // Placement Drives
  static List<PlacementDrive> get placementDrives => [
        const PlacementDrive(
          id: 'plc_1',
          company: 'Google',
          role: 'Associate AI Engineer / SWE',
          ctc: '\$145,000 / annum',
          location: 'Mountain View, CA / Remote',
          eligibilityGpa: '3.50+ GPA',
          deadline: 'Sep 30, 2026',
          status: 'Eligible',
        ),
        const PlacementDrive(
          id: 'plc_2',
          company: 'Microsoft',
          role: 'Software Development Engineer I',
          ctc: '\$138,000 / annum',
          location: 'Redmond, WA',
          eligibilityGpa: '3.40+ GPA',
          deadline: 'Oct 05, 2026',
          status: 'Applied',
        ),
        const PlacementDrive(
          id: 'plc_3',
          company: 'Amazon Web Services (AWS)',
          role: 'Cloud Systems Solutions Architect',
          ctc: '\$132,000 / annum',
          location: 'Seattle, WA',
          eligibilityGpa: '3.20+ GPA',
          deadline: 'Oct 15, 2026',
          status: 'Eligible',
        ),
        const PlacementDrive(
          id: 'plc_4',
          company: 'NVIDIA',
          role: 'Deep Learning Acceleration Intern',
          ctc: '\$58 / hour + Stipend',
          location: 'Santa Clara, CA',
          eligibilityGpa: '3.60+ GPA',
          deadline: 'Nov 01, 2026',
          status: 'Shortlisted',
        ),
      ];

  // Campus Notifications
  static List<CampusNotification> get notifications => [
        const CampusNotification(
          id: 'notif_1',
          title: 'Fall 2026 Midterm Exam Schedule Announced',
          content: 'The finalized timetable for the midterm examinations is now published.',
          date: '2 hours ago',
          category: 'Exam',
          isRead: false,
        ),
        const CampusNotification(
          id: 'notif_2',
          title: 'Placement Drive: Google On-Campus Registrations',
          content: 'Eligible CS & AI students can apply via the Placements portal before Sep 30.',
          date: 'Yesterday',
          category: 'Placement',
          isRead: false,
        ),
        const CampusNotification(
          id: 'notif_3',
          title: 'Fee Payment Receipt Generated',
          content: 'Tuition fees for Fall 2026 have been verified and cleared.',
          date: 'Sep 06',
          category: 'Fee',
          isRead: true,
        ),
        const CampusNotification(
          id: 'notif_4',
          title: 'Library 24/7 Access for Exam Prep',
          content: 'Digital and physical reading halls remain open all night through exam week.',
          date: 'Sep 04',
          category: 'Campus',
          isRead: true,
        ),
      ];

  // Peer & Professor Chat
  static List<ChatMessage> get sampleChat => [
        const ChatMessage(
          id: 'm1',
          sender: 'Prof. A. Vance',
          text: 'Welcome to CS-401! Please review the self-attention paper before next Monday.',
          time: '09:15 AM',
          isMe: false,
        ),
        const ChatMessage(
          id: 'm2',
          sender: 'Alex Johnson',
          text: 'Thank you Professor Vance. Is PyTorch 2.4 acceptable for the assignments?',
          time: '09:20 AM',
          isMe: true,
        ),
        const ChatMessage(
          id: 'm3',
          sender: 'Prof. A. Vance',
          text: 'Yes, PyTorch 2.0+ is fully supported on the university compute cluster.',
          time: '09:24 AM',
          isMe: false,
        ),
      ];

  // AI Assistant responses
  static String getAiAnswer(String query) {
    final q = query.toLowerCase();
    if (q.contains('attendance') || q.contains('absent') || q.contains('minimum')) {
      return 'According to the university handbook, a minimum of 75% attendance is required in each course to sit for semester examinations. Your current overall attendance is 94.8%, safely above the threshold.';
    } else if (q.contains('exam') || q.contains('midterm') || q.contains('date')) {
      return 'Midterm examinations begin on October 12, 2026. Your first examination is CS-401 in Examination Hall B-2 at 09:30 AM.';
    } else if (q.contains('placement') || q.contains('job') || q.contains('drive') || q.contains('package')) {
      return 'Campus placement drives for Google, Microsoft, and NVIDIA are currently open. You meet the GPA eligibility requirements for all 4 listed companies.';
    } else if (q.contains('fee') || q.contains('tuition') || q.contains('pay')) {
      return 'Your tuition fees for the Fall 2026 semester are fully paid with a zero remaining balance. You can download the official receipt in your profile.';
    } else if (q.contains('library') || q.contains('book') || q.contains('journal')) {
      return 'The campus digital library provides 24/7 off-campus proxy access to IEEE, ACM, and Springer journals using your university email.';
    } else {
      return 'I am your UniSphere AI Campus Assistant. You can ask me about class timetables, attendance requirements, exam schedules, placement eligibility, or academic regulations!';
    }
=======
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
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
  }
}
