class AppConstants {
  AppConstants._();

  static const String appName = 'UniSphere AI';
  static const String appTagline = 'Intelligent Campus & Career Platform';
  static const String appVersion = '1.0.0';

  // Storage Keys
  static const String tokenKey = 'unisphere_jwt_token';
  static const String refreshTokenKey = 'unisphere_refresh_token';
  static const String userKey = 'unisphere_cached_user';
  static const String themeKey = 'unisphere_theme_mode';
  static const String rememberMeKey = 'remember_me_state';
  static const String savedEmailKey = 'saved_email';

  // Demo Credentials for quick testing
  static const String demoEmail = 'student@university.edu';
  static const String demoPassword = 'Password123!';
  static const String demoName = 'Alex Mercer';
  static const String demoPhone = '+1 (555) 234-5678';
}
