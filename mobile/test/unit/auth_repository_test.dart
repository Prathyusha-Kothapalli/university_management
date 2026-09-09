import 'package:flutter_test/flutter_test.dart';
import 'package:unisphere_mobile/models/register_request.dart';
import 'package:unisphere_mobile/models/user.dart';
import 'package:unisphere_mobile/repositories/auth_repository.dart';
import 'package:unisphere_mobile/services/token_storage_service.dart';

void main() {
  group('AuthRepository Tests', () {
    late AuthRepository authRepository;
    late TokenStorageService tokenStorage;

    setUp(() async {
      tokenStorage = TokenStorageService();
      await tokenStorage.deleteToken();
      authRepository = AuthRepository(tokenStorage: tokenStorage);
    });

    test('login succeeds and persists session token', () async {
      final result = await authRepository.login('student@university.edu', 'password123');

      expect(result.isSuccess, isTrue);
      expect(result.data, isNotNull);
      expect(result.data?.email, 'student@university.edu');
      expect(result.data?.role, UserRole.student);

      // Verify token was stored
      final token = await tokenStorage.getToken();
      expect(token, isNotNull);
    });

    test('register creates new account and authenticates', () async {
      final request = RegisterRequest(
        name: 'Jamie Taylor',
        email: 'jamie@university.edu',
        phone: '+1 555-1234',
        password: 'PassWord123!',
        role: 'student',
      );

      final result = await authRepository.register(request);
      expect(result.isSuccess, isTrue);
      expect(result.data?.name, 'Jamie Taylor');
      expect(result.data?.email, 'jamie@university.edu');

      final hasToken = await tokenStorage.hasToken();
      expect(hasToken, isTrue);
    });

    test('logout deletes active token and clears auth state', () async {
      await authRepository.login('student@university.edu', 'password123');
      expect(await tokenStorage.hasToken(), isTrue);

      await authRepository.logout();
      expect(await tokenStorage.hasToken(), isFalse);
    });
  });
}
