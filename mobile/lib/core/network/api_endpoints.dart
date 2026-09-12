<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
/// Shared API endpoint paths matching the Python FastAPI backend.
=======
/// Shared API endpoint paths for UniSphere AI Mobile Application.
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
class ApiEndpoints {
  ApiEndpoints._();

  // Authentication & Session
<<<<<<< HEAD
=======
class ApiEndpoints {
  // Authentication
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
class ApiEndpoints {
<<<<<<< HEAD
=======
  ApiEndpoints._();

>>>>>>> 29907a7 (added flutter)
  // Authentication
>>>>>>> origin/web
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
  static const String login = '/auth/login';
  static const String register = '/auth/register';
  static const String logout = '/auth/logout';
  static const String refreshToken = '/auth/refresh';

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
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
<<<<<<< HEAD
=======
=======
>>>>>>> origin/web
  // User Profile
  static const String currentUser = '/users/me';
  static const String updateProfile = '/users/me';

  // University Modules
  static const String courses = '/courses';
  static const String attendance = '/attendance';
  static const String timetable = '/timetable';
  static const String notices = '/notices';
<<<<<<< HEAD
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
=======
  // Users & Profile
  static const String currentUser = '/users/me';
  static const String updateProfile = '/users/profile';

  // Academic & Student Modules
  static const String courses = '/academic/courses';
  static const String schedule = '/academic/schedule';
  static const String attendance = '/academic/attendance';
  static const String grades = '/academic/grades';
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
}
