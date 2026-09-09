import 'package:flutter/material.dart';
import '../../core/constants/app_constants.dart';
import '../../core/constants/route_constants.dart';
import '../../core/theme/app_colors.dart';
import '../../state/auth_state.dart';
import '../../state/profile_state.dart';
import '../../widgets/stat_card.dart';
import '../../widgets/user_avatar.dart';

class HomeScreen extends StatefulWidget {
  final AuthState authState;
  final ProfileState profileState;

  const HomeScreen({
    super.key,
    required this.authState,
    required this.profileState,
  });

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
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
            child: const Text('Cancel'),
          ),
          ElevatedButton(
            style: ElevatedButton.styleFrom(
              backgroundColor: AppColors.error,
              foregroundColor: Colors.white,
            ),
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
          ),
        ],
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
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
                Container(
                  width: double.infinity,
                  padding: const EdgeInsets.all(20),
                  decoration: BoxDecoration(
                    gradient: const LinearGradient(
                      colors: [Color(0xFF0284C7), Color(0xFF1E3A8A)],
                      begin: Alignment.topLeft,
                      end: Alignment.bottomRight,
                    ),
                    borderRadius: BorderRadius.circular(20),
                    boxShadow: [
                      BoxShadow(
                        color: AppColors.primary.withOpacity(0.3),
                        blurRadius: 16,
                        offset: const Offset(0, 6),
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
                              borderRadius: BorderRadius.circular(20),
                            ),
                            child: Text(
                              userRole.toUpperCase(),
                              style: const TextStyle(
                                color: Colors.white,
                                fontSize: 11,
                                fontWeight: FontWeight.w700,
                                letterSpacing: 0.8,
                              ),
                            ),
                          ),
                          Text(
                            user?.studentId ?? 'ID: UNIV-2026',
                            style: TextStyle(
                              color: Colors.white.withOpacity(0.8),
                              fontSize: 12,
                              fontWeight: FontWeight.w500,
                            ),
                          ),
                        ],
                      ),
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
                        style: const TextStyle(
                          color: Colors.white,
                          fontSize: 22,
                          fontWeight: FontWeight.w800,
                          letterSpacing: -0.3,
                        ),
                      ),
                      const SizedBox(height: 6),
                      Text(
                        user?.department ?? 'Computer Science & Engineering',
                        style: TextStyle(
                          color: Colors.white.withOpacity(0.9),
                          fontSize: 13,
                        ),
                      ),
                    ],
                  ),
                ),
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
                    ),
                  ],
                ),
                const SizedBox(height: 24),

                // Main University Management Feature Modules
                const Text(
                  'Campus Modules',
                  style: TextStyle(
                    fontSize: 16,
                    fontWeight: FontWeight.w700,
                    color: AppColors.textPrimaryLight,
                  ),
                ),
                const SizedBox(height: 12),

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
                      ),
                    ),
                    const SizedBox(width: 12),
                    Expanded(
                      child: OutlinedButton.icon(
                        icon: const Icon(Icons.logout_rounded, size: 18, color: AppColors.error),
                        label: const Text('Sign Out', style: TextStyle(color: AppColors.error)),
                        onPressed: _confirmLogout,
                        style: OutlinedButton.styleFrom(
                          side: const BorderSide(color: AppColors.error),
                          padding: const EdgeInsets.symmetric(vertical: 12),
                          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
                        ),
                      ),
                    ),
                  ],
                ),
                const SizedBox(height: 20),
              ],
            ),
          ),
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
          ),
        );
      },
    );
  }

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
              ),
            ],
          ),
        ),
      ],
    );
  }
}
