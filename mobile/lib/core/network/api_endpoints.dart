class ApiEndpoints {
<<<<<<< HEAD
=======
  ApiEndpoints._();

>>>>>>> 29907a7 (added flutter)
  // Authentication
  static const String login = '/auth/login';
  static const String register = '/auth/register';
  static const String logout = '/auth/logout';
  static const String refreshToken = '/auth/refresh';

<<<<<<< HEAD
  // User Profile
  static const String currentUser = '/users/me';
  static const String updateProfile = '/users/me';

  // University Modules
  static const String courses = '/courses';
  static const String attendance = '/attendance';
  static const String timetable = '/timetable';
  static const String notices = '/notices';
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
}
