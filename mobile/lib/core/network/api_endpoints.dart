<<<<<<< HEAD
/// Shared API endpoint paths matching the Python FastAPI backend.
class ApiEndpoints {
  ApiEndpoints._();

  // Authentication & Session
=======
class ApiEndpoints {
  // Authentication
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
  static const String login = '/auth/login';
  static const String register = '/auth/register';
  static const String logout = '/auth/logout';
  static const String refreshToken = '/auth/refresh';

<<<<<<< HEAD
  // Users & Profile
  static const String currentUser = '/users/me';
  static const String updateProfile = '/users/profile';

  // Academic Modules
  static const String courses = '/academic/courses';
  static const String timetable = '/academic/timetable';
  static const String schedule = '/academic/schedule';
  static const String attendance = '/academic/attendance';
  static const String assignments = '/academic/assignments';
  static const String exams = '/academic/exams';
  static const String results = '/academic/results';

  // Communication & Services
  static const String notifications = '/notifications';
  static const String chatMessages = '/chat/messages';
  static const String placements = '/placements/drives';
  static const String aiChat = '/ai/chat';
=======
  // User Profile
  static const String currentUser = '/users/me';
  static const String updateProfile = '/users/me';

  // University Modules
  static const String courses = '/courses';
  static const String attendance = '/attendance';
  static const String timetable = '/timetable';
  static const String notices = '/notices';
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
}
