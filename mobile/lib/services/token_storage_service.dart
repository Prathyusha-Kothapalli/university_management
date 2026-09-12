import 'dart:convert';
import '../core/constants/app_constants.dart';
import '../models/user.dart';
import 'storage_service.dart';

/// Secure token & auth credential persistence service.
class TokenStorageService {
  final IStorageService _storage;

  TokenStorageService({IStorageService? storage})
      : _storage = storage ?? InMemoryStorageService();

  Future<void> saveToken(String accessToken, {String? refreshToken}) async {
    await _storage.write(AppConstants.tokenKey, accessToken);
    if (refreshToken != null) {
      await _storage.write(AppConstants.refreshTokenKey, refreshToken);
    }
  }

  Future<String?> getToken() async {
    return await _storage.read(AppConstants.tokenKey);
  }

  Future<String?> getRefreshToken() async {
    return await _storage.read(AppConstants.refreshTokenKey);
  }

  Future<bool> hasToken() async {
    final token = await getToken();
    return token != null && token.trim().isNotEmpty;
  }

  Future<void> deleteToken() async {
    await _storage.delete(AppConstants.tokenKey);
    await _storage.delete(AppConstants.refreshTokenKey);
  }

  Future<void> saveUser(User user) async {
    final userJson = jsonEncode(user.toJson());
    await _storage.write(AppConstants.userKey, userJson);
  }

  Future<User?> getUser() async {
    final userStr = await _storage.read(AppConstants.userKey);
    if (userStr == null || userStr.isEmpty) return null;
    try {
      final json = jsonDecode(userStr) as Map<String, dynamic>;
      return User.fromJson(json);
    } catch (_) {
      return null;
    }
  }

  Future<void> deleteUser() async {
    await _storage.delete(AppConstants.userKey);
  }

  Future<void> setRememberMe(bool value) async {
    await _storage.write(AppConstants.rememberMeKey, value.toString());
  }

  Future<bool> getRememberMe() async {
    final val = await _storage.read(AppConstants.rememberMeKey);
    return val == 'true';
  }

  Future<void> saveEmail(String email) async {
    await _storage.write(AppConstants.savedEmailKey, email);
  }

  Future<String?> getSavedEmail() async {
    return await _storage.read(AppConstants.savedEmailKey);
  }

  Future<void> clearAuthData() async {
    await deleteToken();
    await deleteUser();
    await _storage.delete(AppConstants.savedEmailKey);
    await _storage.delete(AppConstants.rememberMeKey);
  }

  Future<void> clearAll() async {
    await clearAuthData();
    await _storage.clear();
  }
}
