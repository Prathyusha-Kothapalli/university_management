import 'package:flutter_test/flutter_test.dart';
import 'package:unisphere_mobile/repositories/auth_repository.dart';

void main() {
  group('AuthRepository Unit Tests', () {
    test('Mock login returns valid token and user', () async {
      final repo = AuthRepository();
      final result = await repo.login('student@university.edu', 'Password123!');

      expect(result.token, isNotEmpty);
      expect(result.user.email, 'student@university.edu');
    });
  });
}
