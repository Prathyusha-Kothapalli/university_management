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
}
