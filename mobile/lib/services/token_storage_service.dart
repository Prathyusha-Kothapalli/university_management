import 'dart:convert';
import '../core/constants/app_constants.dart';
import '../models/user.dart';
import 'storage_service.dart';

class TokenStorageService {
  final IStorageService _storage;

  TokenStorageService({IStorageService? storage})
      : _storage = storage ?? SecureFileStorageService();

  Future<void> saveToken(String token) async {
    await _storage.write(AppConstants.tokenKey, token);
  }

  Future<String?> getToken() async {
    return await _storage.read(AppConstants.tokenKey);
  }

  Future<void> deleteToken() async {
    await _storage.delete(AppConstants.tokenKey);
  }

  Future<bool> hasToken() async {
    final token = await getToken();
    return token != null && token.trim().isNotEmpty;
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

  Future<void> setRememberMe(bool remember) async {
    await _storage.write(AppConstants.rememberMeKey, remember.toString());
  }

  Future<bool> getRememberMe() async {
    final value = await _storage.read(AppConstants.rememberMeKey);
    return value == 'true';
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
    // Intentionally keep saved email if Remember Me is checked, otherwise wipe
    final remember = await getRememberMe();
    if (!remember) {
      await _storage.delete(AppConstants.savedEmailKey);
      await _storage.delete(AppConstants.rememberMeKey);
    }
  }
}
