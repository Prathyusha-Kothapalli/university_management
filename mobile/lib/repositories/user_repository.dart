<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
import 'dart:async';
import '../core/constants/api_constants.dart';
=======
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
import '../core/network/api_exceptions.dart';
import '../core/utils/result.dart';
import '../models/user.dart';
import '../models/user_profile.dart';
import '../services/api_service.dart';
import '../services/mock_data_service.dart';
import '../services/storage_service.dart';
import '../services/token_storage_service.dart';

/// Repository responsible for user profile retrieval and updates.
class UserRepository {
  final ApiService apiService;
  final TokenStorageService tokenStorage;
  final StorageService storageService;
  final bool _forceMock;

  UserRepository({
    ApiService? apiService,
    TokenStorageService? tokenStorage,
    StorageService? storageService,
    bool forceMock = ApiConstants.forceMockMode,
  })  : apiService = apiService ?? ApiService(tokenStorage: tokenStorage),
        tokenStorage = tokenStorage ?? TokenStorageService(),
        storageService = storageService ?? StorageService(),
        _forceMock = forceMock;

  /// Retrieve full user profile as UserProfile model
  Future<UserProfile> getUserProfile(User currentUser) async {
    if (_forceMock) {
      return await MockDataService.mockGetProfile(currentUser);
    }

    try {
      return await apiService.getUserProfile(currentUser);
    } on NetworkException {
      if (ApiConstants.useMockFallbackOnFailure) {
        return await MockDataService.mockGetProfile(currentUser);
      }
      rethrow;
    } catch (_) {
      return await MockDataService.mockGetProfile(currentUser);
    }
  }

  /// Retrieve full user profile wrapped in Result
  Future<Result<User>> getProfile() async {
    try {
      final user = await apiService.getCurrentUser();
      await storageService.saveUser(user);
      await tokenStorage.saveUser(user);
      return Result.success(user);
    } on ApiException catch (e) {
      return Result.failure(e.message);
    } catch (e) {
      return Result.failure('Failed to load profile: $e');
    }
  }

<<<<<<< HEAD
  /// Update profile details
  Future<User> updateProfile(User currentUser, {String? name, String? phone}) async {
    if (_forceMock) {
      final updated = await MockDataService.mockUpdateProfile(currentUser, name: name, phone: phone);
      await tokenStorage.saveUser(updated);
      await storageService.saveUser(updated);
      return updated;
    }

    try {
      final updated = await apiService.updateProfile(name: name, phone: phone);
      await tokenStorage.saveUser(updated);
      await storageService.saveUser(updated);
      return updated;
    } on NetworkException {
      if (ApiConstants.useMockFallbackOnFailure) {
        final updated = await MockDataService.mockUpdateProfile(currentUser, name: name, phone: phone);
        await tokenStorage.saveUser(updated);
        await storageService.saveUser(updated);
        return updated;
      }
      rethrow;
    } catch (_) {
      final updated = await MockDataService.mockUpdateProfile(currentUser, name: name, phone: phone);
      await tokenStorage.saveUser(updated);
      await storageService.saveUser(updated);
      return updated;
=======
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
<<<<<<< HEAD
=======
=======
>>>>>>> origin/web
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
<<<<<<< HEAD
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
=======
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
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
    }
  }
}
