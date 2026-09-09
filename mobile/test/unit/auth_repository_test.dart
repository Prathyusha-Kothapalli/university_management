import 'package:flutter_test/flutter_test.dart';
import 'package:unisphere_mobile/models/login_request.dart';
import 'package:unisphere_mobile/models/register_request.dart';
import 'package:unisphere_mobile/repositories/auth_repository.dart';
import 'package:unisphere_mobile/services/storage_service.dart';
import 'package:unisphere_mobile/services/token_storage_service.dart';
import 'package:unisphere_mobile/state/auth_state.dart';

void main() {
  group('AuthRepository & AuthState Unit Tests', () {
    late InMemoryStorageService inMemoryStorage;
    late TokenStorageService tokenStorage;
    late AuthRepository authRepository;
    late AuthState authState;

    setUp(() {
      inMemoryStorage = InMemoryStorageService();
      tokenStorage = TokenStorageService(storage: inMemoryStorage);
      authRepository = AuthRepository(
        tokenStorage: tokenStorage,
        forceMock: true, // test through mock layer
      );
      authState = AuthState(repository: authRepository);
    });

    test('initial auth check when unauthenticated', () async {
      expect(authState.status, AuthStatus.initial);
      await authState.checkAuthStatus();
      expect(authState.status, AuthStatus.unauthenticated);
      expect(authState.isAuthenticated, isFalse);
      expect(authState.currentUser, isNull);
    });

    test('login success flow updates state and persists token', () async {
      final success = await authState.login(
        email: 'student@university.edu',
        password: 'Password123!',
        rememberMe: true,
      );

      expect(success, isTrue);
      expect(authState.status, AuthStatus.authenticated);
      expect(authState.isAuthenticated, isTrue);
      expect(authState.currentUser?.email, 'student@university.edu');
      expect(await tokenStorage.hasToken(), isTrue);
      expect(await tokenStorage.getRememberMe(), isTrue);
    });

    test('login failure with short password emits error', () async {
      final success = await authState.login(
        email: 'student@university.edu',
        password: '123', // shorter than 6 characters
      );

      expect(success, isFalse);
      expect(authState.status, AuthStatus.error);
      expect(authState.errorMessage, isNotNull);
      expect(authState.isAuthenticated, isFalse);
    });

    test('registration success updates state and creates user', () async {
      final success = await authState.register(
        const RegisterRequest(
          name: 'Morgan Blake',
          email: 'morgan@university.edu',
          phone: '+1 555-4321',
          password: 'Password123!',
          role: 'student',
          department: 'Engineering',
        ),
      );

      expect(success, isTrue);
      expect(authState.status, AuthStatus.authenticated);
      expect(authState.currentUser?.name, 'Morgan Blake');
      expect(authState.currentUser?.email, 'morgan@university.edu');
      expect(await tokenStorage.hasToken(), isTrue);
    });

    test('logout clears auth token and updates status', () async {
      await authState.login(
        email: 'student@university.edu',
        password: 'Password123!',
      );
      expect(authState.isAuthenticated, isTrue);

      await authState.logout();
      expect(authState.status, AuthStatus.unauthenticated);
      expect(authState.isAuthenticated, isFalse);
      expect(authState.currentUser, isNull);
      expect(await tokenStorage.hasToken(), isFalse);
    });
  });
}
