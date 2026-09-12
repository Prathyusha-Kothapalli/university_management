import 'package:flutter/material.dart';
import '../../core/constants/app_constants.dart';
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
import '../../core/constants/route_constants.dart';
=======
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
import '../../core/theme/app_colors.dart';
import '../../models/user.dart';
import '../../services/mock_data_service.dart';
import '../../state/auth_state.dart';
import '../../state/profile_state.dart';
import '../../widgets/stat_card.dart';
import '../../widgets/user_avatar.dart';
import '../ai_assistant/ai_assistant_screen.dart';
import '../assignments/assignments_screen.dart';
import '../attendance/attendance_screen.dart';
import '../auth/login_screen.dart';
import '../chat/chat_screen.dart';
import '../exams/exams_screen.dart';
import '../notifications/notifications_screen.dart';
import '../placements/placements_screen.dart';
import '../profile/profile_screen.dart';
import '../timetable/timetable_screen.dart';

/// Professional University Mobile Dashboard with all core campus modules.
class HomeScreen extends StatefulWidget {
  final AuthState authState;
<<<<<<< HEAD
  final ProfileState? profileState;
=======
<<<<<<< HEAD
=======
>>>>>>> origin/web
import '../../core/constants/route_constants.dart';
import '../../core/theme/app_colors.dart';
import '../../state/auth_state.dart';
import '../../state/profile_state.dart';
import '../../widgets/stat_card.dart';
import '../../widgets/user_avatar.dart';

class HomeScreen extends StatefulWidget {
  final AuthState authState;
  final ProfileState profileState;
<<<<<<< HEAD
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
=======
import '../../core/theme/app_colors.dart';
import '../../models/user.dart';
import '../../services/mock_data_service.dart';
import '../../state/auth_state.dart';
import '../../widgets/stat_card.dart';
import '../../widgets/user_avatar.dart';
import '../auth/login_screen.dart';
import '../profile/profile_screen.dart';

/// Professional University Mobile Dashboard.
class HomeScreen extends StatefulWidget {
  final AuthState authState;
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689

  const HomeScreen({
    super.key,
    required this.authState,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
    required this.profileState,
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
    required this.profileState,
=======
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
    this.profileState,
=======
    required this.profileState,
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
  });

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
  int _selectedBottomTab = 0;

  @override
  void initState() {
    super.initState();
    final user = widget.authState.currentUser;
    if (user != null && widget.profileState != null) {
      widget.profileState!.loadProfile(user);
    }
  }

  Future<void> _handleLogout() async {
    final shouldLogout = await showDialog<bool>(
      context: context,
      builder: (ctx) => AlertDialog(
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(18)),
        title: const Text('Sign Out'),
        content: const Text('Are you sure you want to log out of UniSphere?'),
        actions: [
          TextButton(
            onPressed: () => Navigator.of(ctx).pop(false),
<<<<<<< HEAD
=======
=======
>>>>>>> origin/web
  @override
  void initState() {
    super.initState();
    // Pre-load profile details if available
    final user = widget.authState.currentUser;
    if (user != null) {
      widget.profileState.loadProfile(user);
    }
  }

  void _confirmLogout() {
    showDialog(
      context: context,
      builder: (ctx) => AlertDialog(
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
        title: const Text('Confirm Logout'),
        content: const Text('Are you sure you want to sign out of your university account?'),
        actions: [
          TextButton(
            onPressed: () => Navigator.of(ctx).pop(),
<<<<<<< HEAD
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
=======
  int _selectedBottomTab = 0;

  Future<void> _handleLogout() async {
    final shouldLogout = await showDialog<bool>(
      context: context,
      builder: (ctx) => AlertDialog(
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(18)),
        title: const Text('Sign Out'),
        content: const Text('Are you sure you want to log out of UniSphere?'),
        actions: [
          TextButton(
            onPressed: () => Navigator.of(ctx).pop(false),
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
            child: const Text('Cancel'),
          ),
          ElevatedButton(
            style: ElevatedButton.styleFrom(
              backgroundColor: AppColors.error,
              foregroundColor: Colors.white,
            ),
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            onPressed: () => Navigator.of(ctx).pop(true),
            child: const Text('Sign Out'),
=======
=======
>>>>>>> origin/web
            onPressed: () async {
              Navigator.of(ctx).pop();
              await widget.authState.logout();
              if (mounted) {
                Navigator.of(context).pushNamedAndRemoveUntil(
                  RouteConstants.login,
                  (route) => false,
                );
              }
            },
            child: const Text('Logout'),
<<<<<<< HEAD
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
=======
            onPressed: () => Navigator.of(ctx).pop(true),
            child: const Text('Sign Out'),
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
            onPressed: () => Navigator.of(ctx).pop(true),
            child: const Text('Sign Out'),
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
          ),
        ],
      ),
    );
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> origin/web
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689

    if (shouldLogout == true && mounted) {
      await widget.authState.logout();
      if (mounted) {
        Navigator.of(context).pushNamedAndRemoveUntil(
          RouteConstants.login,
          (route) => false,
        );
      }
    }
  }

<<<<<<< HEAD
  void _navigateTo(Widget screen) {
    Navigator.of(context).push(
      MaterialPageRoute(builder: (_) => screen),
    );
<<<<<<< HEAD
=======
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
  void _navigateToProfile() {
    Navigator.of(context).push(
      MaterialPageRoute(
        builder: (_) => ProfileScreen(authState: widget.authState),
      ),
    );
  }

  void _showModuleNotification(String moduleTitle) {
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        content: Text('$moduleTitle module accessed'),
        duration: const Duration(seconds: 2),
        behavior: SnackBarBehavior.floating,
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(10)),
      ),
    );
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
<<<<<<< HEAD
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
  }

  @override
  Widget build(BuildContext context) {
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
    return AnimatedBuilder(
      animation: widget.authState,
      builder: (context, _) {
        final user = widget.authState.currentUser ?? MockDataService.defaultStudent;

        return Scaffold(
          backgroundColor: AppColors.backgroundLight,
          appBar: AppBar(
            elevation: 0,
            title: Row(
              children: [
                Container(
                  padding: const EdgeInsets.all(6),
                  decoration: BoxDecoration(
                    color: AppColors.primary,
                    borderRadius: BorderRadius.circular(8),
                  ),
                  child: const Icon(Icons.school_rounded, color: Colors.white, size: 18),
                ),
                const SizedBox(width: 10),
                const Text(
                  AppConstants.appName,
                  style: TextStyle(
                    fontWeight: FontWeight.w800,
                    letterSpacing: -0.3,
                  ),
                ),
              ],
            ),
            actions: [
              IconButton(
                icon: const Icon(Icons.notifications_none_rounded),
                tooltip: 'Notifications',
                onPressed: () => _navigateTo(const NotificationsScreen()),
              ),
              Padding(
                padding: const EdgeInsets.only(right: 12),
                child: UserAvatar(
                  user: user,
                  radius: 17,
                  onTap: () => _navigateTo(ProfileScreen(
                    authState: widget.authState,
                    profileState: widget.profileState,
                  )),
                ),
              ),
            ],
          ),
          body: SingleChildScrollView(
            padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 16),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                // Welcome Hero Card
=======
<<<<<<< HEAD
=======
>>>>>>> origin/web
    final user = widget.authState.currentUser;
    final userName = user?.name ?? 'Student';
    final userRole = user?.roleDisplay ?? 'Student';
    final userInitials = user?.initials ?? 'U';
    final profile = widget.profileState.profile;

    return Scaffold(
      backgroundColor: AppColors.backgroundLight,
      appBar: AppBar(
        elevation: 0,
        backgroundColor: Colors.white,
        title: Row(
          children: [
            Container(
              padding: const EdgeInsets.all(6),
              decoration: BoxDecoration(
                color: AppColors.primaryLight,
                borderRadius: BorderRadius.circular(8),
              ),
              child: const Icon(Icons.school_rounded, color: AppColors.primary, size: 20),
            ),
            const SizedBox(width: 10),
            const Text(
              AppConstants.appName,
              style: TextStyle(
                fontSize: 18,
                fontWeight: FontWeight.w800,
                color: AppColors.textPrimaryLight,
              ),
            ),
          ],
        ),
        actions: [
          IconButton(
            icon: const Icon(Icons.notifications_none_rounded, color: AppColors.textPrimaryLight),
            onPressed: () {
              ScaffoldMessenger.of(context).showSnackBar(
                const SnackBar(content: Text('No new campus notifications.')),
              );
            },
          ),
          Padding(
            padding: const EdgeInsets.only(right: 16),
            child: UserAvatar(
              imageUrl: user?.avatarUrl,
              initials: userInitials,
              radius: 18,
              onTap: () {
                Navigator.of(context).pushNamed(RouteConstants.profile);
              },
            ),
          ),
        ],
      ),
      body: SafeArea(
        child: RefreshIndicator(
          onRefresh: () async {
            if (user != null) {
              await widget.profileState.loadProfile(user);
            }
          },
          child: SingleChildScrollView(
            physics: const AlwaysScrollableScrollPhysics(),
            padding: const EdgeInsets.all(18),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                // Welcome Card Banner
<<<<<<< HEAD
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
=======
    return AnimatedBuilder(
      animation: widget.authState,
      builder: (context, _) {
        final user = widget.authState.currentUser ?? MockDataService.defaultStudent;

        return Scaffold(
          backgroundColor: AppColors.backgroundLight,
          appBar: AppBar(
            elevation: 0,
            title: Row(
              children: [
                Container(
                  padding: const EdgeInsets.all(6),
                  decoration: BoxDecoration(
                    color: AppColors.primary,
                    borderRadius: BorderRadius.circular(8),
                  ),
                  child: const Icon(Icons.school_rounded, color: Colors.white, size: 18),
                ),
                const SizedBox(width: 10),
                const Text(
                  AppConstants.appName,
                  style: TextStyle(
                    fontWeight: FontWeight.w800,
                    letterSpacing: -0.3,
                  ),
                ),
              ],
            ),
            actions: [
              IconButton(
                icon: const Icon(Icons.notifications_none_rounded),
                tooltip: 'Notifications',
                onPressed: () {
                  ScaffoldMessenger.of(context).showSnackBar(
                    const SnackBar(
                      content: Text('No new campus alerts at this time.'),
                      behavior: SnackBarBehavior.floating,
                    ),
                  );
                },
              ),
              Padding(
                padding: const EdgeInsets.only(right: 12),
                child: UserAvatar(
                  user: user,
                  radius: 17,
                  onTap: _navigateToProfile,
                ),
              ),
            ],
          ),
          body: SingleChildScrollView(
            padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 16),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                // Welcome Card
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
                Container(
                  width: double.infinity,
                  padding: const EdgeInsets.all(20),
                  decoration: BoxDecoration(
                    gradient: const LinearGradient(
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                      colors: [AppColors.primary, Color(0xFF1D4ED8)],
=======
                      colors: [Color(0xFF0284C7), Color(0xFF1E3A8A)],
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
                      colors: [Color(0xFF0284C7), Color(0xFF1E3A8A)],
=======
                      colors: [AppColors.primary, Color(0xFF1D4ED8)],
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
                      colors: [AppColors.primary, Color(0xFF1D4ED8)],
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
                      begin: Alignment.topLeft,
                      end: Alignment.bottomRight,
                    ),
                    borderRadius: BorderRadius.circular(20),
                    boxShadow: [
                      BoxShadow(
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                        color: AppColors.primary.withOpacity(0.28),
                        blurRadius: 18,
                        offset: const Offset(0, 8),
=======
                        color: AppColors.primary.withOpacity(0.3),
                        blurRadius: 16,
                        offset: const Offset(0, 6),
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
                        color: AppColors.primary.withOpacity(0.3),
                        blurRadius: 16,
                        offset: const Offset(0, 6),
=======
                        color: AppColors.primary.withOpacity(0.28),
                        blurRadius: 18,
                        offset: const Offset(0, 8),
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
                        color: AppColors.primary.withOpacity(0.28),
                        blurRadius: 18,
                        offset: const Offset(0, 8),
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
                      ),
                    ],
                  ),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Row(
                        mainAxisAlignment: MainAxisAlignment.spaceBetween,
                        children: [
                          Container(
                            padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
                            decoration: BoxDecoration(
                              color: Colors.white.withOpacity(0.2),
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
                              borderRadius: BorderRadius.circular(12),
                            ),
                            child: Text(
                              user.role.displayName.toUpperCase(),
<<<<<<< HEAD
=======
=======
>>>>>>> origin/web
                              borderRadius: BorderRadius.circular(20),
                            ),
                            child: Text(
                              userRole.toUpperCase(),
<<<<<<< HEAD
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
=======
                              borderRadius: BorderRadius.circular(12),
                            ),
                            child: Text(
                              user.role.displayName.toUpperCase(),
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
                              style: const TextStyle(
                                color: Colors.white,
                                fontSize: 11,
                                fontWeight: FontWeight.w700,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                                letterSpacing: 0.5,
=======
                                letterSpacing: 0.8,
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
                                letterSpacing: 0.8,
=======
                                letterSpacing: 0.5,
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
                                letterSpacing: 0.5,
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
                              ),
                            ),
                          ),
                          Text(
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                            user.studentId ?? 'US-2026',
=======
                            user?.studentId ?? 'ID: UNIV-2026',
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
                            user?.studentId ?? 'ID: UNIV-2026',
=======
                            user.studentId ?? 'US-2026',
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
                            user.studentId ?? 'US-2026',
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
                            style: TextStyle(
                              color: Colors.white.withOpacity(0.8),
                              fontSize: 12,
                              fontWeight: FontWeight.w500,
                            ),
                          ),
                        ],
                      ),
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                      const SizedBox(height: 12),
                      Text(
                        'Welcome back, ${user.name.split(' ').first}!',
=======
=======
>>>>>>> origin/web
                      const SizedBox(height: 14),
                      Text(
                        'Welcome back,',
                        style: TextStyle(
                          color: Colors.white.withOpacity(0.85),
                          fontSize: 14,
                        ),
                      ),
                      const SizedBox(height: 2),
                      Text(
                        userName,
<<<<<<< HEAD
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
=======
                      const SizedBox(height: 12),
                      Text(
                        'Welcome back, ${user.name.split(' ').first}!',
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
                      const SizedBox(height: 12),
                      Text(
                        'Welcome back, ${user.name.split(' ').first}!',
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
                        style: const TextStyle(
                          color: Colors.white,
                          fontSize: 22,
                          fontWeight: FontWeight.w800,
                          letterSpacing: -0.3,
                        ),
                      ),
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
                      const SizedBox(height: 4),
                      Text(
                        user.department ?? 'Computer Science & Engineering',
                        style: TextStyle(
                          color: Colors.white.withOpacity(0.85),
<<<<<<< HEAD
=======
=======
>>>>>>> origin/web
                      const SizedBox(height: 6),
                      Text(
                        user?.department ?? 'Computer Science & Engineering',
                        style: TextStyle(
                          color: Colors.white.withOpacity(0.9),
<<<<<<< HEAD
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
=======
                      const SizedBox(height: 4),
                      Text(
                        user.department ?? 'Computer Science & Engineering',
                        style: TextStyle(
                          color: Colors.white.withOpacity(0.85),
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
                          fontSize: 13,
                        ),
                      ),
                    ],
                  ),
                ),
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
                const SizedBox(height: 24),

                // Academic Metrics / KPI Row (Clickable)
                Row(
                  children: [
                    Expanded(
                      child: GestureDetector(
                        onTap: () => _navigateTo(const ExamsScreen()),
                        child: StatCard(
                          title: 'Current GPA',
                          value: user.gpa?.toStringAsFixed(2) ?? '3.86',
                          subtitle: 'Tap for Transcripts',
                          icon: Icons.auto_graph_rounded,
                          color: AppColors.primary,
                        ),
                      ),
                    ),
                    const SizedBox(width: 12),
                    Expanded(
                      child: GestureDetector(
                        onTap: () => _navigateTo(const AttendanceScreen()),
                        child: StatCard(
                          title: 'Attendance',
                          value: '${user.attendanceRate?.toStringAsFixed(1) ?? '94.8'}%',
                          subtitle: 'Subject Breakdown',
                          icon: Icons.check_circle_outline_rounded,
                          color: AppColors.success,
                        ),
                      ),
<<<<<<< HEAD
=======
=======
>>>>>>> origin/web
                const SizedBox(height: 20),

                // Quick Academic Stats
                const Text(
                  'Academic Overview',
                  style: TextStyle(
                    fontSize: 16,
                    fontWeight: FontWeight.w700,
                    color: AppColors.textPrimaryLight,
                  ),
                ),
                const SizedBox(height: 12),
                GridView.count(
                  crossAxisCount: 2,
                  shrinkWrap: true,
                  physics: const NeverScrollableScrollPhysics(),
                  crossAxisSpacing: 12,
                  mainAxisSpacing: 12,
                  childAspectRatio: 1.5,
                  children: [
                    StatCard(
                      title: 'Cumulative GPA',
                      value: profile?.gpa.toStringAsFixed(2) ?? '3.85',
                      subtitle: 'Top 5%',
                      icon: Icons.auto_graph_rounded,
                      color: AppColors.primary,
                      backgroundColor: AppColors.primaryLight,
                    ),
                    StatCard(
                      title: 'Attendance Rate',
                      value: '${profile?.attendancePercentage.toStringAsFixed(1) ?? '94.2'}%',
                      subtitle: 'Good',
                      icon: Icons.check_circle_outline_rounded,
                      color: AppColors.attendanceGreen,
                      backgroundColor: const Color(0xFFD1FAE5),
                    ),
                    StatCard(
                      title: 'Enrolled Credits',
                      value: '${profile?.enrolledCredits ?? 18} Cr',
                      subtitle: '6 Courses',
                      icon: Icons.book_outlined,
                      color: AppColors.examsPurple,
                      backgroundColor: const Color(0xFFEDE9FE),
                    ),
                    StatCard(
                      title: 'Current Term',
                      value: 'Sem 5',
                      subtitle: 'Fall 2026',
                      icon: Icons.calendar_today_rounded,
                      color: AppColors.feesOrange,
                      backgroundColor: const Color(0xFFFEF3C7),
<<<<<<< HEAD
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
>>>>>>> origin/web
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
                    ),
                  ],
                ),
                const SizedBox(height: 24),

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
                // Main Campus Modules Section
                const Text(
                  'Campus Modules',
                  style: TextStyle(
                    fontSize: 18,
<<<<<<< HEAD
=======
=======
>>>>>>> origin/web
                // Main University Management Feature Modules
                const Text(
                  'Campus Modules',
                  style: TextStyle(
                    fontSize: 16,
<<<<<<< HEAD
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
>>>>>>> origin/web
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
                    fontWeight: FontWeight.w700,
                    color: AppColors.textPrimaryLight,
                  ),
                ),
                const SizedBox(height: 12),

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
                GridView.count(
                  crossAxisCount: 2,
                  shrinkWrap: true,
                  physics: const NeverScrollableScrollPhysics(),
                  mainAxisSpacing: 12,
                  crossAxisSpacing: 12,
                  childAspectRatio: 1.35,
                  children: [
                    _buildModuleCard(
                      title: 'Attendance',
                      subtitle: '94.8% Safe',
                      icon: Icons.fact_check_outlined,
                      color: AppColors.success,
                      onTap: () => _navigateTo(const AttendanceScreen()),
                    ),
                    _buildModuleCard(
                      title: 'Timetable',
                      subtitle: 'Weekly Schedule',
                      icon: Icons.calendar_today_rounded,
                      color: AppColors.primary,
                      onTap: () => _navigateTo(const TimetableScreen()),
                    ),
                    _buildModuleCard(
                      title: 'Assignments',
                      subtitle: '2 Pending Tasks',
                      icon: Icons.assignment_outlined,
                      color: AppColors.warning,
                      onTap: () => _navigateTo(const AssignmentsScreen()),
                    ),
                    _buildModuleCard(
                      title: 'Exams & Results',
                      subtitle: 'Admit Cards & CGPA',
                      icon: Icons.analytics_outlined,
                      color: AppColors.accent,
                      onTap: () => _navigateTo(const ExamsScreen()),
                    ),
                    _buildModuleCard(
                      title: 'Placements',
                      subtitle: 'Google, Microsoft',
                      icon: Icons.work_outline_rounded,
                      color: const Color(0xFF0284C7),
                      onTap: () => _navigateTo(const PlacementsScreen()),
                    ),
                    _buildModuleCard(
                      title: 'Faculty Chat',
                      subtitle: 'Professors & Peers',
                      icon: Icons.chat_bubble_outline_rounded,
                      color: const Color(0xFFEC4899),
                      onTap: () => _navigateTo(const ChatScreen()),
                    ),
                  ],
                ),
                const SizedBox(height: 24),

                // Today's Class Schedule Preview
                Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    const Text(
                      "Today's Classes",
                      style: TextStyle(
                        fontSize: 18,
                        fontWeight: FontWeight.w700,
                        color: AppColors.textPrimaryLight,
                      ),
                    ),
                    TextButton(
                      onPressed: () => _navigateTo(const TimetableScreen()),
                      child: const Text('View All'),
                    ),
                  ],
                ),
                const SizedBox(height: 8),

                ...MockDataService.todaySchedule.map((item) {
                  return Container(
                    margin: const EdgeInsets.only(bottom: 10),
                    padding: const EdgeInsets.all(14),
                    decoration: BoxDecoration(
                      color: Colors.white,
                      borderRadius: BorderRadius.circular(14),
                      border: Border.all(color: AppColors.borderLight),
                    ),
                    child: Row(
                      children: [
                        Container(
                          width: 4,
                          height: 48,
                          decoration: BoxDecoration(
                            color: Color(item['colorHex'] as int),
                            borderRadius: BorderRadius.circular(4),
                          ),
                        ),
                        const SizedBox(width: 14),
                        Expanded(
                          child: Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: [
                              Text(
                                '${item['code']} - ${item['name']}',
                                style: const TextStyle(
                                  fontWeight: FontWeight.w700,
                                  fontSize: 14,
                                  color: AppColors.textPrimaryLight,
                                ),
                              ),
                              const SizedBox(height: 4),
                              Row(
                                children: [
                                  const Icon(Icons.schedule_rounded,
                                      size: 13, color: AppColors.textSecondaryLight),
                                  const SizedBox(width: 4),
                                  Text(
                                    item['time'].toString(),
                                    style: const TextStyle(
                                      fontSize: 12,
                                      color: AppColors.textSecondaryLight,
                                    ),
                                  ),
                                  const SizedBox(width: 12),
                                  const Icon(Icons.place_outlined,
                                      size: 13, color: AppColors.textSecondaryLight),
                                  const SizedBox(width: 4),
                                  Text(
                                    item['room'].toString(),
                                    style: const TextStyle(
                                      fontSize: 12,
                                      color: AppColors.textSecondaryLight,
                                    ),
                                  ),
                                ],
                              ),
                            ],
                          ),
                        ),
                      ],
                    ),
                  );
                }),
<<<<<<< HEAD
=======
=======
>>>>>>> origin/web
                _buildFeatureGrid(context),
                const SizedBox(height: 24),

                // Upcoming Schedule Preview
                Container(
                  padding: const EdgeInsets.all(16),
                  decoration: BoxDecoration(
                    color: Colors.white,
                    borderRadius: BorderRadius.circular(16),
                    border: Border.all(color: const Color(0xFFE2E8F0)),
                  ),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Row(
                        mainAxisAlignment: MainAxisAlignment.spaceBetween,
                        children: [
                          const Row(
                            children: [
                              Icon(Icons.schedule_rounded, size: 18, color: AppColors.primary),
                              SizedBox(width: 8),
                              Text(
                                "Today's Schedule",
                                style: TextStyle(
                                  fontSize: 15,
                                  fontWeight: FontWeight.w700,
                                  color: AppColors.textPrimaryLight,
                                ),
                              ),
                            ],
                          ),
                          Container(
                            padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 3),
                            decoration: BoxDecoration(
                              color: AppColors.primaryLight,
                              borderRadius: BorderRadius.circular(6),
                            ),
                            child: const Text(
                              'Live',
                              style: TextStyle(
                                fontSize: 11,
                                fontWeight: FontWeight.w700,
                                color: AppColors.primaryDark,
                              ),
                            ),
                          ),
                        ],
                      ),
                      const SizedBox(height: 14),
                      _buildScheduleItem(
                        time: '11:00 AM - 12:30 PM',
                        subject: 'CS402: Distributed Systems',
                        room: 'Hall 3B • Prof. Wright',
                        isOngoing: true,
                      ),
                      const Divider(height: 20),
                      _buildScheduleItem(
                        time: '02:00 PM - 03:30 PM',
                        subject: 'CS415: Artificial Intelligence & ML',
                        room: 'Lab 2A • Dr. Vance',
                        isOngoing: false,
                      ),
                    ],
                  ),
                ),
                const SizedBox(height: 24),

                // Quick Navigation Actions
                Row(
                  children: [
                    Expanded(
                      child: OutlinedButton.icon(
                        icon: const Icon(Icons.person_outline_rounded, size: 18),
                        label: const Text('My Profile'),
                        onPressed: () {
                          Navigator.of(context).pushNamed(RouteConstants.profile);
                        },
                        style: OutlinedButton.styleFrom(
                          padding: const EdgeInsets.symmetric(vertical: 12),
                          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
                        ),
<<<<<<< HEAD
=======
=======
                const SizedBox(height: 24),

                // Academic Metrics / KPI Row
                Row(
                  children: [
                    Expanded(
                      child: StatCard(
                        title: 'Current GPA',
                        value: user.gpa?.toStringAsFixed(2) ?? '3.82',
                        subtitle: 'Top 5% of class',
                        icon: Icons.auto_graph_rounded,
                        color: AppColors.primary,
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
                      ),
                    ),
                    const SizedBox(width: 12),
                    Expanded(
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> origin/web
                      child: OutlinedButton.icon(
                        icon: const Icon(Icons.logout_rounded, size: 18, color: AppColors.error),
                        label: const Text('Sign Out', style: TextStyle(color: AppColors.error)),
                        onPressed: _confirmLogout,
                        style: OutlinedButton.styleFrom(
                          side: const BorderSide(color: AppColors.error),
                          padding: const EdgeInsets.symmetric(vertical: 12),
                          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
                        ),
<<<<<<< HEAD
=======
=======
                      child: StatCard(
                        title: 'Attendance',
                        value: '${user.attendanceRate?.toStringAsFixed(1) ?? '94.5'}%',
                        subtitle: 'Above requirement',
                        icon: Icons.check_circle_outline_rounded,
                        color: AppColors.success,
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
                      ),
                    ),
                  ],
                ),
<<<<<<< HEAD
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
<<<<<<< HEAD
=======
                const SizedBox(height: 24),

                // Main University Features Section
                const Text(
                  'Campus Modules',
                  style: TextStyle(
                    fontSize: 18,
                    fontWeight: FontWeight.w700,
                    color: AppColors.textPrimaryLight,
                  ),
                ),
                const SizedBox(height: 12),

                GridView.count(
                  crossAxisCount: 2,
                  shrinkWrap: true,
                  physics: const NeverScrollableScrollPhysics(),
                  mainAxisSpacing: 12,
                  crossAxisSpacing: 12,
                  childAspectRatio: 1.35,
                  children: [
                    _buildModuleCard(
                      title: 'Courses',
                      subtitle: '5 Enrolled',
                      icon: Icons.menu_book_rounded,
                      color: AppColors.primary,
                      onTap: () => _showModuleNotification('Courses'),
                    ),
                    _buildModuleCard(
                      title: 'Timetable',
                      subtitle: 'Full Week',
                      icon: Icons.calendar_today_rounded,
                      color: AppColors.secondary,
                      onTap: () => _showModuleNotification('Timetable'),
                    ),
                    _buildModuleCard(
                      title: 'Exams & Grades',
                      subtitle: 'Transcripts',
                      icon: Icons.analytics_outlined,
                      color: AppColors.accent,
                      onTap: () => _showModuleNotification('Exams & Grades'),
                    ),
                    _buildModuleCard(
                      title: 'Tuition & Fees',
                      subtitle: 'Zero Balance',
                      icon: Icons.account_balance_wallet_outlined,
                      color: AppColors.success,
                      onTap: () => _showModuleNotification('Tuition & Fees'),
                    ),
                    _buildModuleCard(
                      title: 'Digital Library',
                      subtitle: 'Research Portal',
                      icon: Icons.local_library_outlined,
                      color: AppColors.warning,
                      onTap: () => _showModuleNotification('Digital Library'),
                    ),
                    _buildModuleCard(
                      title: 'Campus Services',
                      subtitle: 'ID, Shuttle & Cafeteria',
                      icon: Icons.domain_rounded,
                      color: const Color(0xFFEC4899),
                      onTap: () => _showModuleNotification('Campus Services'),
                    ),
                  ],
                ),
                const SizedBox(height: 24),

                // Today's Class Schedule Preview
                Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    const Text(
                      "Today's Classes",
                      style: TextStyle(
                        fontSize: 18,
                        fontWeight: FontWeight.w700,
                        color: AppColors.textPrimaryLight,
                      ),
                    ),
                    TextButton(
                      onPressed: () => _showModuleNotification('Weekly Schedule'),
                      child: const Text('View All'),
                    ),
                  ],
                ),
                const SizedBox(height: 8),

                ...MockDataService.todaySchedule.map((item) {
                  return Container(
                    margin: const EdgeInsets.only(bottom: 10),
                    padding: const EdgeInsets.all(14),
                    decoration: BoxDecoration(
                      color: Colors.white,
                      borderRadius: BorderRadius.circular(14),
                      border: Border.all(color: AppColors.borderLight),
                    ),
                    child: Row(
                      children: [
                        Container(
                          width: 4,
                          height: 48,
                          decoration: BoxDecoration(
                            color: Color(item['colorHex'] as int),
                            borderRadius: BorderRadius.circular(4),
                          ),
                        ),
                        const SizedBox(width: 14),
                        Expanded(
                          child: Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: [
                              Text(
                                '${item['code']} - ${item['name']}',
                                style: const TextStyle(
                                  fontWeight: FontWeight.w700,
                                  fontSize: 14,
                                  color: AppColors.textPrimaryLight,
                                ),
                              ),
                              const SizedBox(height: 4),
                              Row(
                                children: [
                                  Icon(Icons.schedule_rounded,
                                      size: 13, color: AppColors.textSecondaryLight),
                                  const SizedBox(width: 4),
                                  Text(
                                    item['time'].toString(),
                                    style: const TextStyle(
                                      fontSize: 12,
                                      color: AppColors.textSecondaryLight,
                                    ),
                                  ),
                                  const SizedBox(width: 12),
                                  Icon(Icons.place_outlined,
                                      size: 13, color: AppColors.textSecondaryLight),
                                  const SizedBox(width: 4),
                                  Text(
                                    item['room'].toString(),
                                    style: const TextStyle(
                                      fontSize: 12,
                                      color: AppColors.textSecondaryLight,
                                    ),
                                  ),
                                ],
                              ),
                            ],
                          ),
                        ),
                      ],
                    ),
                  );
                }),
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
                const SizedBox(height: 20),
              ],
            ),
          ),
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
          floatingActionButton: FloatingActionButton.extended(
            onPressed: () => _navigateTo(const AiAssistantScreen()),
            backgroundColor: AppColors.primary,
            icon: const Icon(Icons.auto_awesome, color: Colors.white),
            label: const Text('AI Assistant',
                style: TextStyle(color: Colors.white, fontWeight: FontWeight.w700)),
          ),
          bottomNavigationBar: NavigationBar(
            selectedIndex: _selectedBottomTab,
            onDestinationSelected: (idx) {
              if (idx == 1) {
                _navigateTo(const TimetableScreen());
              } else if (idx == 2) {
                _navigateTo(const ChatScreen());
              } else if (idx == 3) {
                _navigateTo(ProfileScreen(
                  authState: widget.authState,
                  profileState: widget.profileState,
                ));
              } else {
                setState(() => _selectedBottomTab = idx);
              }
            },
            destinations: const [
              NavigationDestination(
                icon: Icon(Icons.dashboard_outlined),
                selectedIcon: Icon(Icons.dashboard_rounded),
                label: 'Dashboard',
              ),
              NavigationDestination(
                icon: Icon(Icons.calendar_month_outlined),
                selectedIcon: Icon(Icons.calendar_month_rounded),
                label: 'Timetable',
              ),
              NavigationDestination(
                icon: Icon(Icons.chat_bubble_outline_rounded),
                selectedIcon: Icon(Icons.chat_bubble_rounded),
                label: 'Messages',
              ),
              NavigationDestination(
                icon: Icon(Icons.person_outline_rounded),
                selectedIcon: Icon(Icons.person_rounded),
                label: 'Profile',
              ),
            ],
<<<<<<< HEAD
=======
=======
>>>>>>> origin/web
        ),
      ),
    );
  }

  Widget _buildFeatureGrid(BuildContext context) {
    final modules = [
      {'title': 'Courses', 'icon': Icons.menu_book_rounded, 'color': AppColors.academicBlue},
      {'title': 'Attendance', 'icon': Icons.how_to_reg_rounded, 'color': AppColors.attendanceGreen},
      {'title': 'Timetable', 'icon': Icons.calendar_month_rounded, 'color': AppColors.feesOrange},
      {'title': 'Exams', 'icon': Icons.assignment_turned_in_rounded, 'color': AppColors.examsPurple},
      {'title': 'Fees & Dues', 'icon': Icons.payment_rounded, 'color': const Color(0xFF0284C7)},
      {'title': 'Library', 'icon': Icons.local_library_rounded, 'color': AppColors.libraryTeal},
    ];

    return GridView.builder(
      shrinkWrap: true,
      physics: const NeverScrollableScrollPhysics(),
      gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
        crossAxisCount: 3,
        crossAxisSpacing: 10,
        mainAxisSpacing: 10,
        childAspectRatio: 1.05,
      ),
      itemCount: modules.length,
      itemBuilder: (ctx, index) {
        final mod = modules[index];
        final color = mod['color'] as Color;
        final icon = mod['icon'] as IconData;
        final title = mod['title'] as String;

        return InkWell(
          borderRadius: BorderRadius.circular(14),
          onTap: () {
            ScaffoldMessenger.of(context).showSnackBar(
              SnackBar(
                content: Text('$title module opened.'),
                duration: const Duration(seconds: 1),
              ),
            );
          },
          child: Container(
            decoration: BoxDecoration(
              color: Colors.white,
              borderRadius: BorderRadius.circular(14),
              border: Border.all(color: const Color(0xFFE2E8F0)),
            ),
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Container(
                  padding: const EdgeInsets.all(10),
                  decoration: BoxDecoration(
                    color: color.withOpacity(0.12),
                    shape: BoxShape.circle,
                  ),
                  child: Icon(icon, color: color, size: 22),
                ),
                const SizedBox(height: 8),
                Text(
                  title,
                  style: const TextStyle(
                    fontSize: 12,
                    fontWeight: FontWeight.w600,
                    color: AppColors.textPrimaryLight,
                  ),
                  textAlign: TextAlign.center,
                ),
              ],
            ),
<<<<<<< HEAD
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
=======
          bottomNavigationBar: NavigationBar(
            selectedIndex: _selectedBottomTab,
            onDestinationSelected: (idx) {
              if (idx == 2) {
                _navigateToProfile();
              } else if (idx == 3) {
                _handleLogout();
              } else {
                setState(() => _selectedBottomTab = idx);
              }
            },
            destinations: const [
              NavigationDestination(
                icon: Icon(Icons.dashboard_outlined),
                selectedIcon: Icon(Icons.dashboard_rounded),
                label: 'Dashboard',
              ),
              NavigationDestination(
                icon: Icon(Icons.calendar_month_outlined),
                selectedIcon: Icon(Icons.calendar_month_rounded),
                label: 'Schedule',
              ),
              NavigationDestination(
                icon: Icon(Icons.person_outline_rounded),
                selectedIcon: Icon(Icons.person_rounded),
                label: 'Profile',
              ),
              NavigationDestination(
                icon: Icon(Icons.logout_rounded, color: AppColors.error),
                label: 'Sign Out',
              ),
            ],
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
          ),
        );
      },
    );
  }

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
  Widget _buildScheduleItem({
    required String time,
    required String subject,
    required String room,
    required bool isOngoing,
  }) {
    return Row(
      children: [
        Container(
          width: 4,
          height: 42,
          decoration: BoxDecoration(
            color: isOngoing ? AppColors.success : const Color(0xFFCBD5E1),
            borderRadius: BorderRadius.circular(2),
          ),
        ),
        const SizedBox(width: 12),
        Expanded(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(
                subject,
                style: const TextStyle(
                  fontSize: 14,
                  fontWeight: FontWeight.w600,
                  color: AppColors.textPrimaryLight,
                ),
              ),
              const SizedBox(height: 2),
              Text(
                '$time • $room',
                style: const TextStyle(
                  fontSize: 12,
                  color: AppColors.textSecondaryLight,
                ),
=======
>>>>>>> origin/web
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
  Widget _buildModuleCard({
    required String title,
    required String subtitle,
    required IconData icon,
    required Color color,
    required VoidCallback onTap,
  }) {
    return Card(
      elevation: 0,
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(16),
        side: const BorderSide(color: AppColors.borderLight),
      ),
      child: InkWell(
        onTap: onTap,
        borderRadius: BorderRadius.circular(16),
        child: Padding(
          padding: const EdgeInsets.all(14),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Container(
                padding: const EdgeInsets.all(8),
                decoration: BoxDecoration(
                  color: color.withOpacity(0.12),
                  borderRadius: BorderRadius.circular(10),
                ),
                child: Icon(icon, size: 20, color: color),
              ),
              Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    title,
                    style: const TextStyle(
                      fontSize: 14,
                      fontWeight: FontWeight.w700,
                      color: AppColors.textPrimaryLight,
                    ),
                  ),
                  const SizedBox(height: 2),
                  Text(
                    subtitle,
                    style: const TextStyle(
                      fontSize: 11.5,
                      color: AppColors.textSecondaryLight,
                    ),
                  ),
                ],
<<<<<<< HEAD
<<<<<<< HEAD
=======
  Widget _buildScheduleItem({
    required String time,
    required String subject,
    required String room,
    required bool isOngoing,
  }) {
    return Row(
      children: [
        Container(
          width: 4,
          height: 42,
          decoration: BoxDecoration(
            color: isOngoing ? AppColors.success : const Color(0xFFCBD5E1),
            borderRadius: BorderRadius.circular(2),
          ),
        ),
        const SizedBox(width: 12),
        Expanded(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(
                subject,
                style: const TextStyle(
                  fontSize: 14,
                  fontWeight: FontWeight.w600,
                  color: AppColors.textPrimaryLight,
                ),
              ),
              const SizedBox(height: 2),
              Text(
                '$time • $room',
                style: const TextStyle(
                  fontSize: 12,
                  color: AppColors.textSecondaryLight,
                ),
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
              ),
            ],
          ),
        ),
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
      ),
=======
      ],
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
      ],
=======
      ),
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
      ),
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
    );
  }
}