import 'dart:convert';
import '../models/user.dart';

/// Key-value storage service for non-sensitive cached data (e.g. user profile, settings).
class StorageService {
  static final Map<String, dynamic> _memoryStore = {};

  static const String _cachedUserKey = 'unisphere_cached_user';
  static const String _rememberEmailKey = 'unisphere_remember_email';

  Future<void> saveUser(User user) async {
    _memoryStore[_cachedUserKey] = jsonEncode(user.toJson());
  }

  Future<User?> getUser() async {
    final raw = _memoryStore[_cachedUserKey];
    if (raw == null) return null;
    try {
      final map = jsonDecode(raw.toString()) as Map<String, dynamic>;
      return User.fromJson(map);
    } catch (_) {
      return null;
    }
  }

  Future<void> removeUser() async {
    _memoryStore.remove(_cachedUserKey);
  }

  Future<void> saveRememberedEmail(String email) async {
    _memoryStore[_rememberEmailKey] = email;
  }

  Future<String?> getRememberedEmail() async {
    return _memoryStore[_rememberEmailKey] as String?;
  }

  Future<void> clearAll() async {
    _memoryStore.clear();
  }
}
