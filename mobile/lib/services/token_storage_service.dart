<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
/// Service interface and implementation for secure JWT token persistence.
///
/// Follows security best practice:
/// - Never stores passwords locally.
/// - Stores only JWT access and refresh tokens.
/// - Provides memory cache and persistence hooks.
class TokenStorageService {
  // In-memory cache for fast, secure synchronous access
  static String? _cachedAccessToken;
  static String? _cachedRefreshToken;

  // Simple in-process key-value backing store
  static final Map<String, String> _secureStore = {};

  static const String _accessTokenKey = 'secure_access_token';
  static const String _refreshTokenKey = 'secure_refresh_token';

  /// Save access token and optional refresh token
  Future<void> saveToken(String accessToken, {String? refreshToken}) async {
    _cachedAccessToken = accessToken;
    _secureStore[_accessTokenKey] = accessToken;

    if (refreshToken != null) {
      _cachedRefreshToken = refreshToken;
      _secureStore[_refreshTokenKey] = refreshToken;
    }
  }

  /// Retrieve active access token
  Future<String?> getToken() async {
    if (_cachedAccessToken != null) return _cachedAccessToken;
    return _secureStore[_accessTokenKey];
  }

  /// Synchronous quick check for auth token
  String? get currentToken => _cachedAccessToken ?? _secureStore[_accessTokenKey];

  /// Retrieve refresh token
  Future<String?> getRefreshToken() async {
    if (_cachedRefreshToken != null) return _cachedRefreshToken;
    return _secureStore[_refreshTokenKey];
  }

  /// Check if an access token exists
  Future<bool> hasToken() async {
    final token = await getToken();
    return token != null && token.isNotEmpty;
  }

  /// Delete all stored tokens on logout
  Future<void> deleteToken() async {
    _cachedAccessToken = null;
    _cachedRefreshToken = null;
    _secureStore.remove(_accessTokenKey);
    _secureStore.remove(_refreshTokenKey);
  }

  /// Clear all secure storage
  Future<void> clearAll() async {
    await deleteToken();
=======
=======
>>>>>>> origin/web
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
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
<<<<<<< HEAD
    // Intentionally keep saved email if Remember Me is checked, otherwise wipe
    final remember = await getRememberMe();
    if (!remember) {
      await _storage.delete(AppConstants.savedEmailKey);
      await _storage.delete(AppConstants.rememberMeKey);
    }
<<<<<<< HEAD
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
=======
/// Service interface and implementation for secure JWT token persistence.
///
/// Follows security best practice:
/// - Never stores passwords locally.
/// - Stores only JWT access and refresh tokens.
/// - Provides memory cache and persistence hooks.
class TokenStorageService {
  // In-memory cache for fast, secure synchronous access
  static String? _cachedAccessToken;
  static String? _cachedRefreshToken;

  // Simple in-process key-value backing store
  static final Map<String, String> _secureStore = {};

  static const String _accessTokenKey = 'secure_access_token';
  static const String _refreshTokenKey = 'secure_refresh_token';

  /// Save access token and optional refresh token
  Future<void> saveToken(String accessToken, {String? refreshToken}) async {
    _cachedAccessToken = accessToken;
    _secureStore[_accessTokenKey] = accessToken;

    if (refreshToken != null) {
      _cachedRefreshToken = refreshToken;
      _secureStore[_refreshTokenKey] = refreshToken;
    }
  }

  /// Retrieve active access token
  Future<String?> getToken() async {
    if (_cachedAccessToken != null) return _cachedAccessToken;
    return _secureStore[_accessTokenKey];
  }

  /// Synchronous quick check for auth token
  String? get currentToken => _cachedAccessToken ?? _secureStore[_accessTokenKey];

  /// Retrieve refresh token
  Future<String?> getRefreshToken() async {
    if (_cachedRefreshToken != null) return _cachedRefreshToken;
    return _secureStore[_refreshTokenKey];
  }

  /// Check if an access token exists
  Future<bool> hasToken() async {
    final token = await getToken();
    return token != null && token.isNotEmpty;
  }

  /// Delete all stored tokens on logout
  Future<void> deleteToken() async {
    _cachedAccessToken = null;
    _cachedRefreshToken = null;
    _secureStore.remove(_accessTokenKey);
    _secureStore.remove(_refreshTokenKey);
  }

  /// Clear all secure storage
  Future<void> clearAll() async {
    await deleteToken();
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
    await _storage.delete(AppConstants.savedEmailKey);
    await _storage.delete(AppConstants.rememberMeKey);
  }

  Future<void> clearAll() async {
    await clearAuthData();
    await _storage.clear();
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
  }
}
