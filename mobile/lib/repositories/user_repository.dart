<<<<<<< HEAD
import '../core/network/api_exceptions.dart';
import '../core/utils/result.dart';
import '../models/user.dart';
import '../services/api_service.dart';
import '../services/storage_service.dart';

/// Repository responsible for user profile retrieval and updates.
class UserRepository {
  final ApiService apiService;
  final StorageService storageService;

  UserRepository({
    ApiService? apiService,
    StorageService? storageService,
  })  : apiService = apiService ?? ApiService(),
        storageService = storageService ?? StorageService();

  /// Retrieve full user profile
  Future<Result<User>> getProfile() async {
    try {
      final user = await apiService.getCurrentUser();
      await storageService.saveUser(user);
      return Result.success(user);
    } on ApiException catch (e) {
      return Result.failure(e.message);
    } catch (e) {
      return Result.failure('Failed to load profile: $e');
    }
  }

  /// Update profile details (e.g. name, phone)
  Future<Result<User>> updateProfile({
    required String name,
    String? phone,
  }) async {
    try {
      final updates = {
        'name': name,
        if (phone != null) 'phone': phone,
      };

      final updatedUser = await apiService.updateProfile(updates);
      await storageService.saveUser(updatedUser);
      return Result.success(updatedUser);
    } on ApiException catch (e) {
      return Result.failure(e.message);
    } catch (e) {
      return Result.failure('Failed to update profile: $e');
=======
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
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
    }
  }
}
