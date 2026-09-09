import 'package:flutter/material.dart';
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

  const ProfileScreen({
    super.key,
    required this.authState,
    required this.profileState,
  });

  @override
  State<ProfileScreen> createState() => _ProfileScreenState();
}

class _ProfileScreenState extends State<ProfileScreen> {
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
    final profile = widget.profileState.profile;
    final isLoading = widget.profileState.isLoading;

    if (user == null) {
      return const Scaffold(
        body: Center(child: Text('No active user session.')),
      );
    }

    return Scaffold(
      backgroundColor: AppColors.backgroundLight,
      appBar: AppBar(
        title: const Text('User Profile'),
        actions: [
          IconButton(
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
            ),
          ),
        ],
      ),
    );
  }
}
