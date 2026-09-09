import '../core/network/api_client.dart';
import '../core/network/api_endpoints.dart';
import '../core/network/api_exceptions.dart';
import '../models/login_request.dart';
import '../models/login_response.dart';
import '../models/register_request.dart';
import '../models/user.dart';
import 'mock_data_service.dart';

/// High-level API Service delegating to [ApiClient] with graceful mock fallback.
class ApiService {
  final ApiClient apiClient;

  ApiService({ApiClient? apiClient}) : apiClient = apiClient ?? ApiClient();

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

  /// Update user profile attributes.
  Future<User> updateProfile(Map<String, dynamic> updates) async {
    try {
      final json = await apiClient.put(
        ApiEndpoints.updateProfile,
        body: updates,
      );
      final data = json is Map<String, dynamic> && json.containsKey('data')
          ? json['data'] as Map<String, dynamic>
          : json as Map<String, dynamic>;
      return User.fromJson(data);
    } on NetworkException {
      // Return updated mock user
      return MockDataService.defaultStudent.copyWith(
        name: updates['name'] as String?,
        phone: updates['phone'] as String?,
      );
    }
  }

  /// Send logout signal to backend.
  Future<void> logout() async {
    try {
      await apiClient.post(ApiEndpoints.logout);
    } catch (_) {
      // Ignore network errors on logout
    }
  }
}
