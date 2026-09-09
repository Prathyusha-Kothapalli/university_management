import '../core/constants/api_constants.dart';
import '../core/network/api_exceptions.dart';
import '../models/login_request.dart';
import '../models/login_response.dart';
import '../models/register_request.dart';
import '../models/user.dart';
import '../services/api_service.dart';
import '../services/mock_data_service.dart';
import '../services/token_storage_service.dart';

class AuthRepository {
  final ApiService _apiService;
  final TokenStorageService _tokenStorage;
  final bool _forceMock;

  AuthRepository({
    ApiService? apiService,
    TokenStorageService? tokenStorage,
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
}
