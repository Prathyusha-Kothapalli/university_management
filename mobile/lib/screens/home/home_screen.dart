import 'package:flutter/material.dart';
import '../../core/constants/app_constants.dart';
import '../../core/constants/route_constants.dart';
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
  final ProfileState? profileState;

  const HomeScreen({
    super.key,
    required this.authState,
    this.profileState,
  });

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
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
            child: const Text('Cancel'),
          ),
          ElevatedButton(
            style: ElevatedButton.styleFrom(
              backgroundColor: AppColors.error,
              foregroundColor: Colors.white,
            ),
            onPressed: () => Navigator.of(ctx).pop(true),
            child: const Text('Sign Out'),
          ),
        ],
      ),
    );

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

  void _navigateTo(Widget screen) {
    Navigator.of(context).push(
      MaterialPageRoute(builder: (_) => screen),
    );
  }

  @override
  Widget build(BuildContext context) {
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
                Container(
                  width: double.infinity,
                  padding: const EdgeInsets.all(20),
                  decoration: BoxDecoration(
                    gradient: const LinearGradient(
                      colors: [AppColors.primary, Color(0xFF1D4ED8)],
                      begin: Alignment.topLeft,
                      end: Alignment.bottomRight,
                    ),
                    borderRadius: BorderRadius.circular(20),
                    boxShadow: [
                      BoxShadow(
                        color: AppColors.primary.withOpacity(0.28),
                        blurRadius: 18,
                        offset: const Offset(0, 8),
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
                              borderRadius: BorderRadius.circular(12),
                            ),
                            child: Text(
                              user.role.displayName.toUpperCase(),
                              style: const TextStyle(
                                color: Colors.white,
                                fontSize: 11,
                                fontWeight: FontWeight.w700,
                                letterSpacing: 0.5,
                              ),
                            ),
                          ),
                          Text(
                            user.studentId ?? 'US-2026',
                            style: TextStyle(
                              color: Colors.white.withOpacity(0.8),
                              fontSize: 12,
                              fontWeight: FontWeight.w500,
                            ),
                          ),
                        ],
                      ),
                      const SizedBox(height: 12),
                      Text(
                        'Welcome back, ${user.name.split(' ').first}!',
                        style: const TextStyle(
                          color: Colors.white,
                          fontSize: 22,
                          fontWeight: FontWeight.w800,
                          letterSpacing: -0.3,
                        ),
                      ),
                      const SizedBox(height: 4),
                      Text(
                        user.department ?? 'Computer Science & Engineering',
                        style: TextStyle(
                          color: Colors.white.withOpacity(0.85),
                          fontSize: 13,
                        ),
                      ),
                    ],
                  ),
                ),
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
                    ),
                  ],
                ),
                const SizedBox(height: 24),

                // Main Campus Modules Section
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
                const SizedBox(height: 20),
              ],
            ),
          ),
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
          ),
        );
      },
    );
  }

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
              ),
            ],
          ),
        ),
      ),
    );
  }
}
