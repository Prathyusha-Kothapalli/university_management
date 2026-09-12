import 'package:flutter_test/flutter_test.dart';
import 'package:unisphere_mobile/models/register_request.dart';
<<<<<<< HEAD
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
=======
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
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9
      expect(await tokenStorage.hasToken(), isFalse);
    });
  });
}