import '../core/constants/api_constants.dart';
import '../core/network/api_client.dart';
import '../core/network/api_endpoints.dart';
import '../models/login_request.dart';
import '../models/login_response.dart';
import '../models/register_request.dart';
import '../models/user.dart';
import '../models/user_profile.dart';
import 'token_storage_service.dart';

class ApiService {
  final ApiClient _client;
  final TokenStorageService _tokenStorage;

  ApiService({
    ApiClient? client,
    TokenStorageService? tokenStorage,
  })  : _tokenStorage = tokenStorage ?? TokenStorageService(),
        _client = client ??
            ApiClient(
              baseUrl: ApiConstants.API_BASE_URL,
              tokenProvider: () async => (tokenStorage ?? TokenStorageService()).getToken(),
            );

  Future<LoginResponse> login(LoginRequest request) async {
    final response = await _client.post(
      ApiEndpoints.login,
      body: request.toJson(),
    );
    return LoginResponse.fromJson(response as Map<String, dynamic>);
  }

  Future<LoginResponse> register(RegisterRequest request) async {
    final response = await _client.post(
      ApiEndpoints.register,
      body: request.toJson(),
    );
    return LoginResponse.fromJson(response as Map<String, dynamic>);
  }

  Future<void> logout() async {
    try {
      await _client.post(ApiEndpoints.logout);
    } catch (_) {
      // Non-fatal if backend token invalidation is unreachable
    }
  }

  Future<UserProfile> getUserProfile() async {
    final response = await _client.get(ApiEndpoints.currentUser);
    return UserProfile.fromJson(response as Map<String, dynamic>);
  }

  Future<User> updateProfile({String? name, String? phone}) async {
    final body = <String, dynamic>{};
    if (name != null) body['name'] = name;
    if (phone != null) body['phone'] = phone;

    final response = await _client.put(
      ApiEndpoints.updateProfile,
      body: body,
    );
    return User.fromJson(response as Map<String, dynamic>);
  }
}
