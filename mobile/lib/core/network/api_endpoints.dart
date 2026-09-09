class ApiEndpoints {
  ApiEndpoints._();

  // Authentication
  static const String login = '/auth/login';
  static const String register = '/auth/register';
  static const String logout = '/auth/logout';
  static const String refreshToken = '/auth/refresh';

  // Users & Profile
  static const String currentUser = '/users/me';
  static const String updateProfile = '/users/profile';

  // Academic & Student Modules
  static const String courses = '/academic/courses';
  static const String schedule = '/academic/schedule';
  static const String attendance = '/academic/attendance';
  static const String grades = '/academic/grades';
}
