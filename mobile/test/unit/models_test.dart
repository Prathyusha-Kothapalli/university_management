import 'package:flutter_test/flutter_test.dart';
import 'package:unisphere_mobile/models/api_response.dart';
import 'package:unisphere_mobile/models/login_request.dart';
import 'package:unisphere_mobile/models/login_response.dart';
import 'package:unisphere_mobile/models/register_request.dart';
import 'package:unisphere_mobile/models/user.dart';

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
        },
      };

      final res = LoginResponse.fromJson(json);
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
    });
  });
}
