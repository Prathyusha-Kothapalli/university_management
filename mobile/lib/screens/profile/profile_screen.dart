import 'package:flutter/material.dart';
<<<<<<< HEAD
import '../../core/constants/route_constants.dart';
import '../../core/theme/app_colors.dart';
import '../../state/auth_state.dart';
import '../../state/profile_state.dart';
import '../../widgets/custom_button.dart';
import '../../widgets/loading_indicator.dart';
import '../../widgets/user_avatar.dart';
import 'edit_profile_dialog.dart';

class ProfileScreen extends StatefulWidget {
  final AuthState authState;
  final ProfileState profileState;
=======
import '../../core/theme/app_colors.dart';
import '../../models/user.dart';
import '../../state/auth_state.dart';
import '../../state/profile_state.dart';
import '../../widgets/custom_button.dart';
import '../../widgets/user_avatar.dart';
import '../auth/login_screen.dart';
import 'edit_profile_dialog.dart';

/// User Profile Screen with details inspection, editing modal, and secure logout.
class ProfileScreen extends StatefulWidget {
  final AuthState authState;
>>>>>>> 29907a7 (added flutter)

  const ProfileScreen({
    super.key,
    required this.authState,
<<<<<<< HEAD
    required this.profileState,
=======
>>>>>>> 29907a7 (added flutter)
  });

  @override
  State<ProfileScreen> createState() => _ProfileScreenState();
}

class _ProfileScreenState extends State<ProfileScreen> {
<<<<<<< HEAD
  @override
  void initState() {
    super.initState();
    final user = widget.authState.currentUser;
    if (user != null && widget.profileState.profile == null) {
      widget.profileState.loadProfile(user);
    }
  }

  void _showEditDialog() async {
    final user = widget.authState.currentUser;
    if (user == null) return;

    final updated = await EditProfileDialog.show(
      context,
      currentUser: user,
      authState: widget.authState,
      profileState: widget.profileState,
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

  void _confirmLogout() {
    showDialog(
      context: context,
      builder: (ctx) => AlertDialog(
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
        title: const Text('Confirm Logout'),
        content: const Text('Are you sure you want to sign out?'),
        actions: [
          TextButton(
            onPressed: () => Navigator.of(ctx).pop(),
=======
  late final ProfileState _profileState;

  @override
  void initState() {
    super.initState();
    _profileState = ProfileState();
  }

  @override
  void dispose() {
    _profileState.dispose();
    super.dispose();
  }

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
>>>>>>> 29907a7 (added flutter)
            child: const Text('Cancel'),
          ),
          ElevatedButton(
            style: ElevatedButton.styleFrom(
              backgroundColor: AppColors.error,
              foregroundColor: Colors.white,
            ),
<<<<<<< HEAD
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
=======
            onPressed: () => Navigator.of(ctx).pop(true),
            child: const Text('Sign Out'),
>>>>>>> 29907a7 (added flutter)
          ),
        ],
      ),
    );
<<<<<<< HEAD
=======

    if (shouldLogout == true && mounted) {
      await widget.authState.logout();
      if (mounted) {
        Navigator.of(context).pushAndRemoveUntil(
          MaterialPageRoute(
            builder: (_) => LoginScreen(authState: widget.authState),
          ),
          (route) => false,
        );
      }
    }
>>>>>>> 29907a7 (added flutter)
  }

  @override
  Widget build(BuildContext context) {
<<<<<<< HEAD
    final user = widget.authState.currentUser;
    final profile = widget.profileState.profile;
    final isLoading = widget.profileState.isLoading;

    if (user == null) {
      return const Scaffold(
        body: Center(child: Text('No active user session.')),
      );
    }

=======
>>>>>>> 29907a7 (added flutter)
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
        ],
      ),
      body: SafeArea(
        child: isLoading && profile == null
            ? const Center(child: LoadingIndicator(message: 'Loading profile data...'))
            : SingleChildScrollView(
                padding: const EdgeInsets.all(20),
                child: Column(
                  children: [
                    // Avatar & Main Header
                    Center(
                      child: Column(
                        children: [
                          Stack(
                            children: [
                              UserAvatar(
                                imageUrl: user.avatarUrl,
                                initials: user.initials,
                                radius: 46,
                              ),
                              Positioned(
                                bottom: 0,
                                right: 0,
                                child: GestureDetector(
                                  onTap: _showEditDialog,
                                  child: Container(
                                    padding: const EdgeInsets.all(6),
                                    decoration: BoxDecoration(
                                      color: AppColors.primary,
                                      shape: BoxShape.circle,
                                      border: Border.all(color: Colors.white, width: 2),
                                    ),
                                    child: const Icon(
                                      Icons.camera_alt_rounded,
                                      size: 16,
                                      color: Colors.white,
                                    ),
                                  ),
                                ),
                              ),
                            ],
                          ),
                          const SizedBox(height: 14),
                          Text(
                            user.name,
                            style: const TextStyle(
                              fontSize: 22,
                              fontWeight: FontWeight.w700,
                              color: AppColors.textPrimaryLight,
                              letterSpacing: -0.3,
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
                          const SizedBox(height: 10),
                          Container(
                            padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 4),
                            decoration: BoxDecoration(
                              color: AppColors.primaryLight,
                              borderRadius: BorderRadius.circular(20),
                            ),
                            child: Text(
                              user.roleDisplay.toUpperCase(),
                              style: const TextStyle(
                                fontSize: 11,
                                fontWeight: FontWeight.w700,
                                color: AppColors.primaryDark,
                                letterSpacing: 0.8,
                              ),
                            ),
                          ),
                        ],
                      ),
                    ),
                    const SizedBox(height: 24),

                    // Edit Profile Action Button
                    CustomButton(
                      text: 'Edit Profile Information',
                      onPressed: _showEditDialog,
                      variant: ButtonVariant.outlined,
                      icon: Icons.edit_note_rounded,
                      height: 44,
                    ),
                    const SizedBox(height: 20),

                    // Contact & University Info Card
                    _buildSectionCard(
                      title: 'Personal & Contact Info',
                      icon: Icons.badge_outlined,
                      items: [
                        _buildInfoRow('Full Name', user.name),
                        _buildInfoRow('Email Address', user.email),
                        _buildInfoRow('Phone Number', user.phone ?? 'Not provided'),
                        _buildInfoRow('Account Type', user.roleDisplay),
                        _buildInfoRow('Member Since', 'September 2024'),
                      ],
                    ),
                    const SizedBox(height: 16),

                    // Academic Profile Card
                    _buildSectionCard(
                      title: 'Academic Details',
                      icon: Icons.school_outlined,
                      items: [
                        _buildInfoRow('Student / Faculty ID', user.studentId ?? 'UNIV-2026-CS-042'),
                        _buildInfoRow('Department', user.department ?? 'Computer Science & Engineering'),
                        _buildInfoRow('Academic Program', profile?.academicProgram ?? 'B.S. Computer Science'),
                        _buildInfoRow('Current Term', profile?.currentSemester ?? 'Semester 5 (Fall 2026)'),
                        _buildInfoRow('Enrollment Status', profile?.enrollmentStatus ?? 'Active - Full Time'),
                        _buildInfoRow('Cumulative GPA', profile?.gpa.toStringAsFixed(2) ?? '3.85'),
                        _buildInfoRow('Attendance', '${profile?.attendancePercentage.toStringAsFixed(1) ?? '94.2'}%'),
                      ],
                    ),
                    const SizedBox(height: 28),

                    // Logout Button
                    CustomButton(
                      text: 'Sign Out Account',
                      onPressed: _confirmLogout,
                      variant: ButtonVariant.danger,
                      icon: Icons.logout_rounded,
                    ),
                    const SizedBox(height: 24),
                  ],
                ),
              ),
      ),
    );
  }

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
        border: Border.all(color: const Color(0xFFE2E8F0)),
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

  Widget _buildInfoRow(String label, String value) {
    return Padding(
      padding: const EdgeInsets.only(bottom: 12),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          SizedBox(
            width: 130,
            child: Text(
              label,
              style: const TextStyle(
                fontSize: 13,
                color: AppColors.textSecondaryLight,
                fontWeight: FontWeight.w500,
              ),
            ),
          ),
          Expanded(
            child: Text(
              value,
              style: const TextStyle(
                fontSize: 13,
                color: AppColors.textPrimaryLight,
                fontWeight: FontWeight.w600,
              ),
=======
            icon: const Icon(Icons.logout_rounded, color: AppColors.error),
            tooltip: 'Sign Out',
            onPressed: _handleLogoutConfirmation,
          ),
        ],
      ),
      body: AnimatedBuilder(
        animation: widget.authState,
        builder: (context, _) {
          final user = widget.authState.currentUser ??
              const User(
                id: 'usr_guest',
                name: 'Campus User',
                email: 'user@university.edu',
                role: UserRole.student,
              );

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
                        radius: 40,
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
                        text: 'Edit Profile',
                        onPressed: () {
                          EditProfileDialog.show(
                            context,
                            currentUser: user,
                            authState: widget.authState,
                            profileState: _profileState,
                          );
                        },
                        variant: ButtonVariant.outline,
                        icon: Icons.edit_outlined,
                      ),
                    ],
                  ),
                ),
                const SizedBox(height: 20),

                // Details List Card
                Container(
                  decoration: BoxDecoration(
                    color: Colors.white,
                    borderRadius: BorderRadius.circular(20),
                    border: Border.all(color: AppColors.borderLight),
                  ),
                  child: Column(
                    children: [
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
                        value: user.department ?? 'Computer Science',
                      ),
                      const Divider(indent: 56),
                      _buildInfoTile(
                        icon: Icons.calendar_today_rounded,
                        label: 'Academic Batch',
                        value: user.enrolledYear ?? '2024 - 2028',
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
                ),
                const SizedBox(height: 24),

                // Sign Out Button
                CustomButton(
                  text: 'Sign Out',
                  onPressed: _handleLogoutConfirmation,
                  variant: ButtonVariant.outline,
                  backgroundColor: AppColors.error,
                  textColor: AppColors.error,
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

  Widget _buildInfoTile({
    required IconData icon,
    required String label,
    required String value,
    Color? valueColor,
  }) {
    return Padding(
      padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 14),
      child: Row(
        children: [
          Container(
            padding: const EdgeInsets.all(8),
            decoration: BoxDecoration(
              color: AppColors.surfaceElevatedLight,
              borderRadius: BorderRadius.circular(10),
            ),
            child: Icon(icon, size: 20, color: AppColors.primary),
          ),
          const SizedBox(width: 16),
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
                    fontSize: 15,
                    fontWeight: FontWeight.w600,
                    color: valueColor ?? AppColors.textPrimaryLight,
                  ),
                ),
              ],
>>>>>>> 29907a7 (added flutter)
            ),
          ),
        ],
      ),
    );
  }
}
