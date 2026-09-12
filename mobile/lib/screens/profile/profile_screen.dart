import 'package:flutter/material.dart';
<<<<<<< HEAD
import '../../core/constants/route_constants.dart';
=======
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9
import '../../core/theme/app_colors.dart';
import '../../models/user.dart';
import '../../state/auth_state.dart';
import '../../state/profile_state.dart';
import '../../widgets/custom_button.dart';
<<<<<<< HEAD
import '../../widgets/loading_indicator.dart';
import '../../widgets/user_avatar.dart';
=======
import '../../widgets/user_avatar.dart';
import '../auth/login_screen.dart';
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9
import 'edit_profile_dialog.dart';

/// User Profile Screen with details inspection, editing modal, and secure logout.
class ProfileScreen extends StatefulWidget {
  final AuthState authState;
<<<<<<< HEAD
  final ProfileState? profileState;
=======
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9

  const ProfileScreen({
    super.key,
    required this.authState,
<<<<<<< HEAD
    this.profileState,
=======
    required this.profileState,
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9
  });

  @override
  State<ProfileScreen> createState() => _ProfileScreenState();
}

class _ProfileScreenState extends State<ProfileScreen> {
  late final ProfileState _profileState;
  bool _createdOwnProfileState = false;

  @override
  void initState() {
    super.initState();
    if (widget.profileState != null) {
      _profileState = widget.profileState!;
    } else {
      _profileState = ProfileState();
      _createdOwnProfileState = true;
    }

    final user = widget.authState.currentUser;
    if (user != null && _profileState.profile == null) {
      _profileState.loadProfile(user);
    }
  }

  @override
  void dispose() {
<<<<<<< HEAD
    if (_createdOwnProfileState) {
      _profileState.dispose();
    }
    super.dispose();
  }

  void _showEditDialog() async {
    final user = widget.authState.currentUser;
    if (user == null) return;

    final updated = await EditProfileDialog.show(
      context,
      currentUser: user,
      authState: widget.authState,
      profileState: _profileState,
    );

    if (updated == true && mounted) {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(
          content: Text('Profile updated successfully!'),
          backgroundColor: AppColors.success,
        ),
      );
    }
  }

=======
    _profileState.dispose();
    super.dispose();
  }

>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9
  Future<void> _handleLogoutConfirmation() async {
    final shouldLogout = await showDialog<bool>(
      context: context,
      builder: (ctx) => AlertDialog(
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(18)),
        title: const Text('Sign Out'),
        content: const Text('Are you sure you want to log out of your university account?'),
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
<<<<<<< HEAD
  }

  @override
  Widget build(BuildContext context) {
=======
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9
    return Scaffold(
      backgroundColor: AppColors.backgroundLight,
      appBar: AppBar(
        title: const Text('User Profile'),
        actions: [
          IconButton(
<<<<<<< HEAD
            icon: const Icon(Icons.edit_outlined),
            tooltip: 'Edit Profile',
            onPressed: _showEditDialog,
          ),
          IconButton(
=======
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9
            icon: const Icon(Icons.logout_rounded, color: AppColors.error),
            tooltip: 'Sign Out',
            onPressed: _handleLogoutConfirmation,
          ),
        ],
      ),
      body: AnimatedBuilder(
        animation: Listenable.merge([widget.authState, _profileState]),
        builder: (context, _) {
          final user = widget.authState.currentUser ??
              const User(
                id: 'usr_guest',
                name: 'Campus User',
                email: 'user@university.edu',
                role: UserRole.student,
              );
          final profile = _profileState.profile;
          final isLoading = _profileState.isLoading;

          if (isLoading && profile == null) {
            return const Center(child: LoadingIndicator(message: 'Loading profile data...'));
          }

          return SingleChildScrollView(
            padding: const EdgeInsets.all(20),
            child: Column(
              children: [
                // Profile Header Card
                Container(
                  padding: const EdgeInsets.all(24),
                  decoration: BoxDecoration(
                    color: Colors.white,
                    borderRadius: BorderRadius.circular(20),
                    border: Border.all(color: AppColors.borderLight),
                  ),
                  child: Column(
                    children: [
                      UserAvatar(
                        user: user,
                        radius: 42,
                      ),
                      const SizedBox(height: 16),
                      Text(
                        user.name,
                        style: const TextStyle(
                          fontSize: 20,
                          fontWeight: FontWeight.w700,
                          color: AppColors.textPrimaryLight,
                        ),
                      ),
                      const SizedBox(height: 4),
                      Text(
                        user.email,
                        style: const TextStyle(
                          fontSize: 14,
                          color: AppColors.textSecondaryLight,
                        ),
                      ),
                      const SizedBox(height: 12),
                      Container(
                        padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
                        decoration: BoxDecoration(
                          color: AppColors.primary.withOpacity(0.1),
                          borderRadius: BorderRadius.circular(20),
                        ),
                        child: Text(
                          user.role.displayName.toUpperCase(),
                          style: const TextStyle(
                            fontSize: 12,
                            fontWeight: FontWeight.w700,
                            color: AppColors.primary,
                            letterSpacing: 0.5,
                          ),
                        ),
                      ),
                      const SizedBox(height: 20),
                      CustomButton(
                        text: 'Edit Profile Information',
                        onPressed: _showEditDialog,
                        variant: ButtonVariant.outline,
                        icon: Icons.edit_note_rounded,
                      ),
                    ],
                  ),
                ),
                const SizedBox(height: 20),

                // Personal Details Card
                _buildSectionCard(
                  title: 'Personal & Contact Info',
                  icon: Icons.badge_outlined,
                  items: [
                    _buildInfoTile(
                      icon: Icons.badge_outlined,
                      label: 'University ID',
                      value: user.studentId ?? 'US-2026-042',
                    ),
                    const Divider(indent: 56),
                    _buildInfoTile(
                      icon: Icons.phone_outlined,
                      label: 'Phone Number',
                      value: user.phone != null && user.phone!.isNotEmpty
                          ? user.phone!
                          : 'Not specified',
                    ),
                    const Divider(indent: 56),
                    _buildInfoTile(
                      icon: Icons.apartment_rounded,
                      label: 'Department',
                      value: user.department ?? 'Computer Science & Engineering',
                    ),
                    const Divider(indent: 56),
                    _buildInfoTile(
                      icon: Icons.verified_user_outlined,
                      label: 'Account Status',
                      value: 'Active (Good Standing)',
                      valueColor: AppColors.success,
                    ),
                  ],
                ),
                const SizedBox(height: 20),

                // Academic Details Card
                _buildSectionCard(
                  title: 'Academic Details',
                  icon: Icons.school_outlined,
                  items: [
                    _buildInfoTile(
                      icon: Icons.auto_graph_rounded,
                      label: 'Cumulative GPA',
                      value: profile?.gpa.toStringAsFixed(2) ??
                          (user.gpa != null ? user.gpa!.toStringAsFixed(2) : '3.85'),
                    ),
                    const Divider(indent: 56),
                    _buildInfoTile(
                      icon: Icons.fact_check_outlined,
                      label: 'Attendance Rate',
                      value: '${profile?.attendancePercentage.toStringAsFixed(1) ?? (user.attendanceRate != null ? user.attendanceRate!.toStringAsFixed(1) : '94.2')}%',
                      valueColor: AppColors.success,
                    ),
                    const Divider(indent: 56),
                    _buildInfoTile(
                      icon: Icons.calendar_today_rounded,
                      label: 'Current Term',
                      value: profile?.currentSemester ?? 'Semester 5 (Fall 2026)',
                    ),
                    const Divider(indent: 56),
                    _buildInfoTile(
                      icon: Icons.book_outlined,
                      label: 'Academic Program',
                      value: profile?.academicProgram ?? 'B.S. in Computer Science',
                    ),
                  ],
                ),
                const SizedBox(height: 24),

                // Sign Out Button
                CustomButton(
                  text: 'Sign Out Account',
                  onPressed: _handleLogoutConfirmation,
                  variant: ButtonVariant.danger,
                  icon: Icons.logout_rounded,
                ),
                const SizedBox(height: 24),
              ],
            ),
          );
        },
      ),
    );
  }

<<<<<<< HEAD
  Widget _buildSectionCard({
    required String title,
    required IconData icon,
    required List<Widget> items,
  }) {
    return Container(
      width: double.infinity,
      padding: const EdgeInsets.all(18),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: AppColors.borderLight),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: [
              Icon(icon, size: 20, color: AppColors.primary),
              const SizedBox(width: 8),
              Text(
                title,
                style: const TextStyle(
                  fontSize: 15,
                  fontWeight: FontWeight.w700,
                  color: AppColors.textPrimaryLight,
                ),
              ),
            ],
          ),
          const Divider(height: 24),
          ...items,
        ],
      ),
    );
  }

=======
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9
  Widget _buildInfoTile({
    required IconData icon,
    required String label,
    required String value,
    Color? valueColor,
  }) {
    return Padding(
<<<<<<< HEAD
      padding: const EdgeInsets.symmetric(vertical: 4),
=======
      padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 14),
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9
      child: Row(
        children: [
          Container(
            padding: const EdgeInsets.all(8),
            decoration: BoxDecoration(
              color: AppColors.surfaceElevatedLight,
              borderRadius: BorderRadius.circular(10),
            ),
<<<<<<< HEAD
            child: Icon(icon, size: 18, color: AppColors.primary),
          ),
          const SizedBox(width: 14),
=======
            child: Icon(icon, size: 20, color: AppColors.primary),
          ),
          const SizedBox(width: 16),
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  label,
                  style: const TextStyle(
                    fontSize: 12,
                    color: AppColors.textSecondaryLight,
                  ),
                ),
                const SizedBox(height: 2),
                Text(
                  value,
                  style: TextStyle(
<<<<<<< HEAD
                    fontSize: 14,
=======
                    fontSize: 15,
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9
                    fontWeight: FontWeight.w600,
                    color: valueColor ?? AppColors.textPrimaryLight,
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}