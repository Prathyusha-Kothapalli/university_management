<<<<<<< HEAD
import '../core/constants/api_constants.dart';
import '../core/network/api_exceptions.dart';
=======
import '../core/network/api_exceptions.dart';
import '../core/utils/result.dart';
>>>>>>> 29907a7 (added flutter)
import '../models/login_request.dart';
import '../models/login_response.dart';
import '../models/register_request.dart';
import '../models/user.dart';
import '../services/api_service.dart';
<<<<<<< HEAD
import '../services/mock_data_service.dart';
import '../services/token_storage_service.dart';

class AuthRepository {
  final ApiService _apiService;
  final TokenStorageService _tokenStorage;
  final bool _forceMock;
=======
import '../services/storage_service.dart';
import '../services/token_storage_service.dart';

/// Repository coordinating authentication, token storage, and session lifecycle.
class AuthRepository {
  final ApiService apiService;
  final TokenStorageService tokenStorage;
  final StorageService storageService;
>>>>>>> 29907a7 (added flutter)

  AuthRepository({
    ApiService? apiService,
    TokenStorageService? tokenStorage,
<<<<<<< HEAD
    bool forceMock = ApiConstants.forceMockMode,
  })  : _apiService = apiService ?? ApiService(tokenStorage: tokenStorage),
        _tokenStorage = tokenStorage ?? TokenStorageService(),
        _forceMock = forceMock;

  /// Check if user has an active session
  Future<bool> isAuthenticated() async {
    final hasToken = await _tokenStorage.hasToken();
    if (!hasToken) return false;
    final cachedUser = await _tokenStorage.getUser();
    return cachedUser != null;
  }

  /// Get currently cached user
  Future<User?> getCurrentUser() async {
    return await _tokenStorage.getUser();
  }

  /// Authenticate user via email and password
  Future<LoginResponse> login(LoginRequest request) async {
    if (_forceMock) {
      final response = await MockDataService.mockLogin(request);
      await _persistSession(response, request.rememberMe);
      return response;
    }

    try {
      final response = await _apiService.login(request);
      await _persistSession(response, request.rememberMe);
      return response;
    } on NetworkException catch (_) {
      if (ApiConstants.useMockFallbackOnFailure) {
        final fallback = await MockDataService.mockLogin(request);
        await _persistSession(fallback, request.rememberMe);
        return fallback;
      }
      rethrow;
    } on TimeoutException catch (_) {
      if (ApiConstants.useMockFallbackOnFailure) {
        final fallback = await MockDataService.mockLogin(request);
        await _persistSession(fallback, request.rememberMe);
        return fallback;
      }
      rethrow;
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
      final response = await _apiService.register(request);
      await _persistSession(response, true);
      return response;
    } on NetworkException catch (_) {
      if (ApiConstants.useMockFallbackOnFailure) {
        final fallback = await MockDataService.mockRegister(request);
        await _persistSession(fallback, true);
        return fallback;
      }
      rethrow;
    } on TimeoutException catch (_) {
      if (ApiConstants.useMockFallbackOnFailure) {
        final fallback = await MockDataService.mockRegister(request);
        await _persistSession(fallback, true);
        return fallback;
      }
      rethrow;
    }
  }

  /// Logout user and clear secure storage
  Future<void> logout() async {
    try {
      await _apiService.logout();
    } catch (_) {
      // Ignored if network unavailable
    } finally {
      await _tokenStorage.clearAuthData();
    }
  }

  /// Helper to store token and user session
  Future<void> _persistSession(LoginResponse response, bool rememberMe) async {
    await _tokenStorage.saveToken(response.accessToken);
    await _tokenStorage.saveUser(response.user);
    await _tokenStorage.setRememberMe(rememberMe);
    if (rememberMe) {
      await _tokenStorage.saveEmail(response.user.email);
    }
  }

  Future<String?> getSavedEmail() => _tokenStorage.getSavedEmail();
  Future<bool> getRememberMe() => _tokenStorage.getRememberMe();
=======
    StorageService? storageService,
  })  : apiService = apiService ?? ApiService(),
        tokenStorage = tokenStorage ?? TokenStorageService(),
        storageService = storageService ?? StorageService();

  /// Authenticate user credentials and persist token + profile.
  Future<Result<User>> login(String email, String password) async {
    try {
      final request = LoginRequest(email: email, password: password);
      final response = await apiService.login(request);

      if (response.accessToken.isNotEmpty) {
        await tokenStorage.saveToken(
          response.accessToken,
          refreshToken: response.refreshToken,
        );
      }

      final user = response.user ??
          User(
            id: 'usr_default',
            name: email.split('@').first,
            email: email,
            role: email.contains('faculty') ? UserRole.faculty : UserRole.student,
          );

      await storageService.saveUser(user);
      return Result.success(user);
    } on ApiException catch (e) {
      return Result.failure(e.message);
    } catch (e) {
      return Result.failure('Login failed: ${e.toString()}');
    }
  }

  /// Register new user account.
  Future<Result<User>> register(RegisterRequest request) async {
    try {
      final response = await apiService.register(request);

      if (response.accessToken.isNotEmpty) {
        await tokenStorage.saveToken(
          response.accessToken,
          refreshToken: response.refreshToken,
        );
      }

      final user = response.user ??
          User(
            id: 'usr_${DateTime.now().millisecondsSinceEpoch}',
            name: request.name,
            email: request.email,
            phone: request.phone,
            role: UserRole.fromString(request.role),
          );

      await storageService.saveUser(user);
      return Result.success(user);
    } on ApiException catch (e) {
      return Result.failure(e.message);
    } catch (e) {
      return Result.failure('Registration failed: ${e.toString()}');
    }
  }

  /// Check whether the user has a valid active session.
  Future<User?> checkAuth() async {
    final hasToken = await tokenStorage.hasToken();
    if (!hasToken) {
      return null;
    }

    // Try reading cached user first
    final cachedUser = await storageService.getUser();
    if (cachedUser != null) {
      return cachedUser;
    }

    // Attempt fetching current profile from server
    try {
      final user = await apiService.getCurrentUser();
      await storageService.saveUser(user);
      return user;
    } catch (_) {
      // Return fallback demo user if token is present
      return const User(
        id: 'usr_active',
        name: 'Alex Johnson',
        email: 'alex.johnson@university.edu',
        role: UserRole.student,
      );
    }
  }

  /// Terminate session and remove all tokens.
  Future<void> logout() async {
    try {
      await apiService.logout();
    } catch (_) {
      // Continue clearing local storage even if network fails
    } finally {
      await tokenStorage.deleteToken();
      await storageService.removeUser();
    }
  }
>>>>>>> 29907a7 (added flutter)
}
