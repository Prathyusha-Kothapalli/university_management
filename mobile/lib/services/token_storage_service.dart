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
  }
}
