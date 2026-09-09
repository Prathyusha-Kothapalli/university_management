<<<<<<< HEAD
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

  /// Request timeout in seconds
  static const int connectTimeoutSeconds = 15;
  static const int receiveTimeoutSeconds = 15;

  /// Default headers
  static const Map<String, String> defaultHeaders = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
  };
=======
/// ============================================================================
/// BACKEND API CONFIGURATION
/// ============================================================================
/// 
/// BACKEND DEVELOPERS:
/// Change the [API_BASE_URL] below to point to your live or staging server.
/// Examples:
///   - Android Emulator: "http://10.0.2.2:8000/api/v1"
///   - iOS Simulator:    "http://127.0.0.1:8000/api/v1"
///   - Physical Device:  "http://192.168.1.X:8000/api/v1" (Your local machine LAN IP)
///   - Production/Cloud: "https://api.unisphere.edu/api/v1"
///
class ApiConstants {
  // --------------------------------------------------------------------------
  // EDIT HERE: Set your backend API URL
  // --------------------------------------------------------------------------
  static const String API_BASE_URL = "http://10.0.2.2:8000/api/v1";

  // When enabled, if the live backend is offline or unreachable, the application
  // gracefully activates the mock service layer so all screens and UI flows work seamlessly.
  static const bool useMockFallbackOnFailure = true;

  // Force mock mode always (useful for offline UI testing and demos)
  static const bool forceMockMode = false;

  // Network timeouts
  static const Duration connectTimeout = Duration(seconds: 10);
  static const Duration receiveTimeout = Duration(seconds: 10);

  // Headers
  static const String headerContentType = 'Content-Type';
  static const String headerAuthorization = 'Authorization';
  static const String contentTypeJson = 'application/json';
  static const String bearerPrefix = 'Bearer ';
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
}
