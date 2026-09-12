import 'package:flutter/material.dart';
import '../core/theme/app_colors.dart';
import '../models/user.dart';

/// User Avatar display widget with initial letters fallback.
class UserAvatar extends StatelessWidget {
  final User? user;
  final double radius;
  final VoidCallback? onTap;

  const UserAvatar({
    super.key,
    this.user,
    this.radius = 24,
    this.onTap,
  });

  String _getInitials(String name) {
    if (name.trim().isEmpty) return 'U';
    final parts = name.trim().split(RegExp(r'\s+'));
    if (parts.length > 1) {
      return '${parts[0][0]}${parts[1][0]}'.toUpperCase();
    }
    return parts[0][0].toUpperCase();
  }

  @override
  Widget build(BuildContext context) {
    final name = user?.name ?? 'User';
    final initials = _getInitials(name);

    final avatar = CircleAvatar(
      radius: radius,
      backgroundColor: AppColors.primaryLight,
      child: Text(
        initials,
        style: TextStyle(
          color: Colors.white,
          fontSize: radius * 0.8,
          fontWeight: FontWeight.w700,
        ),
      ),
    );

    if (onTap != null) {
      return InkWell(
        onTap: onTap,
        borderRadius: BorderRadius.circular(radius),
        child: avatar,
      );
    }

    return avatar;
  }
}
