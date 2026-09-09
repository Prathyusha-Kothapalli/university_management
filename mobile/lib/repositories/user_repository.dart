import '../core/constants/api_constants.dart';
import '../core/network/api_exceptions.dart';
import '../models/user.dart';
import '../models/user_profile.dart';
import '../services/api_service.dart';
import '../services/mock_data_service.dart';
import '../services/token_storage_service.dart';

class UserRepository {
  final ApiService _apiService;
  final TokenStorageService _tokenStorage;
  final bool _forceMock;

  UserRepository({
    ApiService? apiService,
    TokenStorageService? tokenStorage,
    bool forceMock = ApiConstants.forceMockMode,
  })  : _apiService = apiService ?? ApiService(tokenStorage: tokenStorage),
        _tokenStorage = tokenStorage ?? TokenStorageService(),
        _forceMock = forceMock;

  Future<UserProfile> getProfile(User currentUser) async {
    if (_forceMock) {
      return await MockDataService.mockGetProfile(currentUser);
    }

    try {
      return await _apiService.getUserProfile();
    } on NetworkException catch (_) {
      if (ApiConstants.useMockFallbackOnFailure) {
        return await MockDataService.mockGetProfile(currentUser);
      }
      rethrow;
    } on TimeoutException catch (_) {
      if (ApiConstants.useMockFallbackOnFailure) {
        return await MockDataService.mockGetProfile(currentUser);
      }
      rethrow;
    } catch (_) {
      // Fallback to local profile synthesis
      return await MockDataService.mockGetProfile(currentUser);
    }
  }

  Future<User> updateProfile(User currentUser, {String? name, String? phone}) async {
    if (_forceMock) {
      final updated = await MockDataService.mockUpdateProfile(currentUser, name: name, phone: phone);
      await _tokenStorage.saveUser(updated);
      return updated;
    }

    try {
      final updated = await _apiService.updateProfile(name: name, phone: phone);
      await _tokenStorage.saveUser(updated);
      return updated;
    } on NetworkException catch (_) {
      if (ApiConstants.useMockFallbackOnFailure) {
        final updated = await MockDataService.mockUpdateProfile(currentUser, name: name, phone: phone);
        await _tokenStorage.saveUser(updated);
        return updated;
      }
      rethrow;
    } catch (_) {
      final updated = await MockDataService.mockUpdateProfile(currentUser, name: name, phone: phone);
      await _tokenStorage.saveUser(updated);
      return updated;
    }
  }
}
