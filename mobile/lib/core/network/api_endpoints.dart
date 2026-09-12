/// Shared API endpoint paths for UniSphere AI Mobile Application.
class ApiEndpoints {
  ApiEndpoints._();

  // Authentication & Session
  static const String login = '/auth/login';
  static const String register = '/auth/register';
  static const String logout = '/auth/logout';
  static const String refreshToken = '/auth/refresh';

  // Users & Profile
  static const String currentUser = '/users/me';
  static const String updateProfile = '/users/profile';

  // HR & Career Management
  static const String jobs = '/jobs';
  static const String jobDetails = '/jobs'; // append /{id}
  static const String applyJob = '/applications';
  static const String myApplications = '/applications/me';
  static const String resume = '/resume';
  static const String interviews = '/interviews';
  static const String myInterviews = '/interviews/me';

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
  static const String notices = '/notices';
  static const String chatMessages = '/chat/messages';
  static const String placements = '/placements/drives';
  static const String aiChat = '/ai/chat';
}
