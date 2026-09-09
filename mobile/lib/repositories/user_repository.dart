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
    }
  }
}
