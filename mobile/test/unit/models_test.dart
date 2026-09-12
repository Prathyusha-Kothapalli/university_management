import 'package:flutter_test/flutter_test.dart';
import 'package:unisphere_mobile/models/api_response.dart';
import 'package:unisphere_mobile/models/login_request.dart';
import 'package:unisphere_mobile/models/login_response.dart';
import 'package:unisphere_mobile/models/register_request.dart';
import 'package:unisphere_mobile/models/user.dart';
<<<<<<< HEAD
import 'package:unisphere_mobile/models/user_profile.dart';

void main() {
  group('Models JSON Serialization Tests', () {
    test('User fromJson and toJson', () {
      final json = {
        'id': 'usr_101',
        'name': 'Alex Mercer',
        'email': 'alex@university.edu',
        'phone': '+1 555-0199',
        'role': 'student',
        'department': 'CS',
        'student_id': 'UNIV-101',
      };

      final user = User.fromJson(json);
      expect(user.id, 'usr_101');
      expect(user.name, 'Alex Mercer');
      expect(user.email, 'alex@university.edu');
      expect(user.roleDisplay, 'Student');
      expect(user.initials, 'AM');

      final serialized = user.toJson();
      expect(serialized['id'], 'usr_101');
      expect(serialized['name'], 'Alex Mercer');
      expect(serialized['role'], 'student');
    });

    test('LoginRequest toJson', () {
      const req = LoginRequest(
        email: 'alex@university.edu',
        password: 'Password123!',
        rememberMe: true,
      );
      final json = req.toJson();
      expect(json['email'], 'alex@university.edu');
      expect(json['password'], 'Password123!');
      expect(json['remember_me'], true);
    });

    test('LoginResponse fromJson and toJson', () {
      final json = {
        'access_token': 'jwt_secret_token_123',
        'token_type': 'bearer',
        'expires_in': 3600,
        'user': {
          'id': 'usr_1',
          'name': 'Alex Mercer',
          'email': 'alex@university.edu',
          'role': 'student',
=======

void main() {
  group('Models Serialization Tests', () {
    test('User fromJson and toJson work symmetrically', () {
      final json = {
        'id': 'usr_123',
        'name': 'Taylor Swift',
        'email': 'taylor@university.edu',
        'phone': '+1 555-0199',
        'role': 'student',
        'department': 'Computer Science',
        'student_id': 'US-2026-99',
        'avatar_url': 'https://example.com/avatar.jpg',
        'enrolled_year': '2024 - 2028',
        'gpa': 3.95,
        'attendance_rate': 98.2,
      };

      final user = User.fromJson(json);
      expect(user.id, 'usr_123');
      expect(user.name, 'Taylor Swift');
      expect(user.email, 'taylor@university.edu');
      expect(user.role, UserRole.student);
      expect(user.gpa, 3.95);

      final exportedJson = user.toJson();
      expect(exportedJson['id'], 'usr_123');
      expect(exportedJson['email'], 'taylor@university.edu');
      expect(exportedJson['role'], 'student');
    });

    test('LoginRequest serialization', () {
      const req = LoginRequest(
        email: 'alex@university.edu',
        password: 'SecurePassword123!',
      );

      final json = req.toJson();
      expect(json['email'], 'alex@university.edu');
      expect(json['password'], 'SecurePassword123!');

      final parsed = LoginRequest.fromJson(json);
      expect(parsed.email, req.email);
      expect(parsed.password, req.password);
    });

    test('LoginResponse parsing with user payload', () {
      final json = {
        'access_token': 'jwt.token.abc',
        'refresh_token': 'refresh.token.xyz',
        'token_type': 'Bearer',
        'expires_in': 3600,
        'user': {
          'id': 'usr_456',
          'name': 'Morgan Reed',
          'email': 'morgan@university.edu',
          'role': 'faculty',
>>>>>>> 29907a7 (added flutter)
        },
      };

      final res = LoginResponse.fromJson(json);
<<<<<<< HEAD
      expect(res.accessToken, 'jwt_secret_token_123');
      expect(res.tokenType, 'bearer');
      expect(res.user.name, 'Alex Mercer');

      final serialized = res.toJson();
      expect(serialized['access_token'], 'jwt_secret_token_123');
    });

    test('RegisterRequest toJson', () {
      const reg = RegisterRequest(
        name: 'Jordan Lee',
        email: 'jordan@university.edu',
        phone: '+1 555-1234',
        password: 'Password123!',
        role: 'student',
        department: 'Physics',
      );
      final json = reg.toJson();
      expect(json['name'], 'Jordan Lee');
      expect(json['email'], 'jordan@university.edu');
      expect(json['role'], 'student');
      expect(json['department'], 'Physics');
    });

    test('ApiResponse fromJson and factory methods', () {
      final successResp = ApiResponse.success('Test data', message: 'Operation successful');
      expect(successResp.success, isTrue);
      expect(successResp.data, 'Test data');
      expect(successResp.statusCode, 200);

      final failResp = ApiResponse<String>.failure('Invalid token', statusCode: 401);
      expect(failResp.success, isFalse);
      expect(failResp.error, 'Invalid token');
      expect(failResp.statusCode, 401);

      final jsonWrapper = {
        'status': 'success',
        'message': 'Loaded',
        'data': {'id': 'usr_2', 'name': 'Sam', 'email': 'sam@uni.edu'},
      };
      final parsed = ApiResponse.fromJson(
        jsonWrapper,
        (data) => User.fromJson(data as Map<String, dynamic>),
      );
      expect(parsed.success, isTrue);
      expect(parsed.data?.name, 'Sam');
    });

    test('UserProfile fromJson and copyWith', () {
      const user = User(id: '1', name: 'Alex', email: 'alex@uni.edu');
      const profile = UserProfile(user: user, gpa: 3.9);
      expect(profile.gpa, 3.9);
      expect(profile.attendancePercentage, 94.2);

      final updated = profile.copyWith(gpa: 4.0);
      expect(updated.gpa, 4.0);
      expect(updated.user.name, 'Alex');
=======
      expect(res.accessToken, 'jwt.token.abc');
      expect(res.refreshToken, 'refresh.token.xyz');
      expect(res.user?.name, 'Morgan Reed');
      expect(res.user?.role, UserRole.faculty);
    });

    test('RegisterRequest serialization', () {
      const req = RegisterRequest(
        name: 'Jordan Lee',
        email: 'jordan@university.edu',
        phone: '+15551234567',
        password: 'SecretPassword99!',
        role: 'student',
      );

      final json = req.toJson();
      expect(json['name'], 'Jordan Lee');
      expect(json['email'], 'jordan@university.edu');
      expect(json['role'], 'student');
    });

    test('ApiResponse generic parsing', () {
      final json = {
        'success': true,
        'message': 'Operation completed',
        'data': {'count': 42},
      };

      final res = ApiResponse<Map<String, dynamic>>.fromJson(
        json,
        (data) => data as Map<String, dynamic>,
      );

      expect(res.success, isTrue);
      expect(res.message, 'Operation completed');
      expect(res.data?['count'], 42);
>>>>>>> 29907a7 (added flutter)
    });
  });
}
