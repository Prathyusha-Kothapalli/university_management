/// Centralized API configuration for UniSphere AI Mobile Application.
///
/// ============================================================================
/// BACKEND DEVELOPER NOTICE:
/// Configure your active backend API URL here.
/// - For local Android Emulator: use 'http://10.0.2.2:8000/api/v1'
/// - For iOS Simulator / Web / Desktop: use 'http://localhost:8000/api/v1'
/// - For physical device over LAN: use 'http://<YOUR_LAN_IP>:8000/api/v1'
/// - For production / staging: use 'https://api.unisphere.edu/api/v1'
/// ============================================================================
class ApiConstants {
  ApiConstants._();

  /// Primary Backend API Base URL.
  /// Update this single constant to switch environments.
  static const String apiBaseUrl = 'http://10.0.2.2:8000/api/v1';
  static const String API_BASE_URL = apiBaseUrl;

  /// Graceful mock fallback when backend is unreachable or offline
  static const bool useMockFallbackOnFailure = true;

  /// Force mock mode (useful for offline UI testing and demos)
  static const bool forceMockMode = false;

  /// Request timeout in seconds
  static const int connectTimeoutSeconds = 15;
  static const int receiveTimeoutSeconds = 15;
  static const Duration connectTimeout = Duration(seconds: connectTimeoutSeconds);
  static const Duration receiveTimeout = Duration(seconds: receiveTimeoutSeconds);

  /// Default headers
  static const Map<String, String> defaultHeaders = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
  };

  static const String headerContentType = 'Content-Type';
  static const String headerAuthorization = 'Authorization';
  static const String contentTypeJson = 'application/json';
  static const String bearerPrefix = 'Bearer ';
}
