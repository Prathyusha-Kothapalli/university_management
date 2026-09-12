import 'dart:async';
import '../core/constants/api_constants.dart';
import '../core/network/api_exceptions.dart';
import '../core/utils/result.dart';
import '../models/login_request.dart';
import '../models/login_response.dart';
import '../models/register_request.dart';
import '../models/user.dart';
import '../services/api_service.dart';
import '../services/mock_data_service.dart';
import '../services/storage_service.dart';
import '../services/token_storage_service.dart';

/// Repository coordinating authentication, token storage, and session lifecycle.
class AuthRepository {
  final ApiService apiService;
  final TokenStorageService tokenStorage;
  final StorageService storageService;
  final bool _forceMock;

  AuthRepository({
    ApiService? apiService,
    TokenStorageService? tokenStorage,
    StorageService? storageService,
    bool forceMock = ApiConstants.forceMockMode,
  })  : apiService = apiService ?? ApiService(tokenStorage: tokenStorage),
        tokenStorage = tokenStorage ?? TokenStorageService(),
        storageService = storageService ?? StorageService(),
        _forceMock = forceMock;

  /// Check if user has an active session
  Future<bool> isAuthenticated() async {
    final hasToken = await tokenStorage.hasToken();
    if (!hasToken) return false;
    final cachedUser = await getCurrentUser();
    return cachedUser != null;
  }

  /// Get currently cached user
  Future<User?> getCurrentUser() async {
    final user = await tokenStorage.getUser();
    if (user != null) return user;
    return await storageService.getUser();
  }

  /// Check whether the user has a valid active session.
  Future<User?> checkAuth() async {
    final hasToken = await tokenStorage.hasToken();
    if (!hasToken) return null;

    final cachedUser = await getCurrentUser();
    if (cachedUser != null) return cachedUser;

    try {
      final user = await apiService.getCurrentUser();
      await storageService.saveUser(user);
      await tokenStorage.saveUser(user);
      return user;
    } catch (_) {
      return MockDataService.defaultStudent;
    }
  }

  /// Authenticate user via LoginRequest
  Future<LoginResponse> login(LoginRequest request) async {
    if (_forceMock) {
      final response = await MockDataService.mockLogin(request);
      await _persistSession(response, request.rememberMe);
      return response;
    }

    try {
      final response = await apiService.login(request);
      await _persistSession(response, request.rememberMe);
      return response;
    } on NetworkException {
      if (ApiConstants.useMockFallbackOnFailure) {
        final fallback = await MockDataService.mockLogin(request);
        await _persistSession(fallback, request.rememberMe);
        return fallback;
      }
      rethrow;
    }
  }

  /// Authenticate user credentials with Result wrapper
  Future<Result<User>> loginWithCredentials(String email, String password, {bool rememberMe = false}) async {
    try {
      final request = LoginRequest(email: email, password: password, rememberMe: rememberMe);
      final response = await login(request);
      return Result.success(response.user);
    } on ApiException catch (e) {
      return Result.failure(e.message);
    } catch (e) {
      return Result.failure('Login failed: ${e.toString()}');
    }
  }

  /// Register new user account
  Future<LoginResponse> register(RegisterRequest request) async {
    if (_forceMock) {
      final response = await MockDataService.mockRegister(request);
      await _persistSession(response, true);
      return response;
    }

    try {
      final response = await apiService.register(request);
      await _persistSession(response, true);
      return response;
    } on NetworkException {
      if (ApiConstants.useMockFallbackOnFailure) {
        final fallback = await MockDataService.mockRegister(request);
        await _persistSession(fallback, true);
        return fallback;
      }
      rethrow;
    }
  }

  /// Register new user account with Result wrapper
  Future<Result<User>> registerWithResult(RegisterRequest request) async {
    try {
      final response = await register(request);
      return Result.success(response.user);
    } on ApiException catch (e) {
      return Result.failure(e.message);
    } catch (e) {
      return Result.failure('Registration failed: ${e.toString()}');
    }
  }

  /// Terminate session and remove all tokens.
  Future<void> logout() async {
    try {
      await apiService.logout();
    } catch (_) {
      // Ignored if network unavailable
    } finally {
      await tokenStorage.deleteToken();
      await tokenStorage.clearAuthData();
      await storageService.removeUser();
    }
  }

  Future<void> _persistSession(LoginResponse response, bool rememberMe) async {
    if (response.accessToken.isNotEmpty) {
      await tokenStorage.saveToken(
        response.accessToken,
        refreshToken: response.refreshToken,
      );
    }
    await tokenStorage.saveUser(response.user);
    await storageService.saveUser(response.user);
    await tokenStorage.setRememberMe(rememberMe);
    if (rememberMe) {
      await tokenStorage.saveEmail(response.user.email);
    }
  }

  Future<String?> getSavedEmail() => tokenStorage.getSavedEmail();
  Future<bool> getRememberMe() => tokenStorage.getRememberMe();
}
