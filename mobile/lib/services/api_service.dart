<<<<<<< HEAD
import '../core/constants/api_constants.dart';
=======
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9
import '../core/network/api_client.dart';
import '../core/network/api_endpoints.dart';
import '../core/network/api_exceptions.dart';
import '../models/login_request.dart';
import '../models/login_response.dart';
import '../models/register_request.dart';
import '../models/user.dart';
<<<<<<< HEAD
import '../models/user_profile.dart';
=======
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9
import 'mock_data_service.dart';
import 'token_storage_service.dart';

/// High-level API Service delegating to [ApiClient] with graceful mock fallback.
class ApiService {
  final ApiClient apiClient;
  final TokenStorageService tokenStorage;

  ApiService({
    ApiClient? apiClient,
    ApiClient? client,
    TokenStorageService? tokenStorage,
  })  : tokenStorage = tokenStorage ?? TokenStorageService(),
        apiClient = apiClient ??
            client ??
            ApiClient(
              baseUrl: ApiConstants.API_BASE_URL,
              tokenProvider: () async =>
                  (tokenStorage ?? TokenStorageService()).getToken(),
            );

  /// Authenticate user via backend API with offline mock fallback.
  Future<LoginResponse> login(LoginRequest request) async {
    try {
      final json = await apiClient.post(
        ApiEndpoints.login,
        body: request.toJson(),
      );
      return LoginResponse.fromJson(json as Map<String, dynamic>);
    } on NetworkException {
      // Backend server is offline -> fallback to mock demo data for development/testing
      if (request.email.toLowerCase().contains('faculty')) {
        return MockDataService.facultyLoginResponse;
      }
      return MockDataService.studentLoginResponse;
    }
  }

  /// Register new user account with offline mock fallback.
  Future<LoginResponse> register(RegisterRequest request) async {
    try {
      final json = await apiClient.post(
        ApiEndpoints.register,
        body: request.toJson(),
      );
      return LoginResponse.fromJson(json as Map<String, dynamic>);
    } on NetworkException {
      // Offline fallback: create simulated user profile
      final newUser = User(
        id: 'usr_${DateTime.now().millisecondsSinceEpoch}',
        name: request.name,
        email: request.email,
        phone: request.phone,
        role: UserRole.fromString(request.role),
        department: 'College of Computing & Informatics',
        studentId: 'US-2026-${DateTime.now().millisecond}',
      );
      return LoginResponse(
        accessToken: 'mock_jwt_token_${DateTime.now().millisecondsSinceEpoch}',
        tokenType: 'Bearer',
        expiresIn: 86400,
        user: newUser,
      );
    }
  }

  /// Fetch currently authenticated user profile.
  Future<User> getCurrentUser() async {
    try {
      final json = await apiClient.get(ApiEndpoints.currentUser);
      final data = json is Map<String, dynamic> && json.containsKey('data')
          ? json['data'] as Map<String, dynamic>
          : json as Map<String, dynamic>;
      return User.fromJson(data);
    } on NetworkException {
      return MockDataService.defaultStudent;
    }
  }

  /// Fetch detailed user profile.
  Future<UserProfile> getUserProfile([User? user]) async {
    try {
      final json = await apiClient.get(ApiEndpoints.currentUser);
      final data = json is Map<String, dynamic> && json.containsKey('data')
          ? json['data'] as Map<String, dynamic>
          : json as Map<String, dynamic>;
      return UserProfile.fromJson(data);
    } on NetworkException {
      return MockDataService.mockGetProfile(user ?? MockDataService.defaultStudent);
    }
  }

  /// Update user profile attributes.
  Future<User> updateProfile({
    String? name,
    String? phone,
    Map<String, dynamic>? updates,
  }) async {
    try {
      final body = <String, dynamic>{};
      if (updates != null) {
        body.addAll(updates);
      }
      if (name != null) body['name'] = name;
      if (phone != null) body['phone'] = phone;

      final json = await apiClient.put(
        ApiEndpoints.updateProfile,
        body: body,
      );
      final data = json is Map<String, dynamic> && json.containsKey('data')
          ? json['data'] as Map<String, dynamic>
          : json as Map<String, dynamic>;
      return User.fromJson(data);
    } on NetworkException {
      return MockDataService.defaultStudent.copyWith(
        name: name ?? updates?['name'] as String?,
        phone: phone ?? updates?['phone'] as String?,
      );
    }
  }

  /// Send logout signal to backend.
  Future<void> logout() async {
    try {
      await apiClient.post(ApiEndpoints.logout);
    } catch (_) {
<<<<<<< HEAD
      // Non-fatal if backend token invalidation is unreachable
=======
      // Ignore network errors on logout
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9
    }
  }
}
