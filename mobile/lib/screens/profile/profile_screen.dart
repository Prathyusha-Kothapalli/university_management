import 'package:flutter/material.dart';
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

  const ProfileScreen({
    super.key,
    required this.authState,
  });

  @override
  State<ProfileScreen> createState() => _ProfileScreenState();
}

class _ProfileScreenState extends State<ProfileScreen> {
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
        Navigator.of(context).pushAndRemoveUntil(
          MaterialPageRoute(
            builder: (_) => LoginScreen(authState: widget.authState),
          ),
          (route) => false,
        );
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: AppColors.backgroundLight,
      appBar: AppBar(
        title: const Text('User Profile'),
        actions: [
          IconButton(
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
            ),
          ),
        ],
      ),
    );
  }
}
