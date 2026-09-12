import 'package:flutter/material.dart';
import '../core/theme/app_colors.dart';
import '../models/user.dart';

/// User Avatar display widget with initial letters fallback.
class UserAvatar extends StatelessWidget {
  final User? user;
  final String? imageUrl;
  final String? initials;
  final double radius;
  final Color backgroundColor;
  final Color textColor;
  final VoidCallback? onTap;

  const UserAvatar({
    super.key,
    this.user,
    this.imageUrl,
    this.initials,
    this.radius = 24,
    this.backgroundColor = AppColors.primaryLight,
    this.textColor = AppColors.primaryDark,
    this.onTap,
  });

  String _calculateInitials() {
    if (initials != null && initials!.isNotEmpty) {
      return initials!;
    }
    final name = user?.name ?? 'User';
    if (name.trim().isEmpty) return 'U';
    final parts = name.trim().split(RegExp(r'\s+'));
    if (parts.length > 1) {
      return '${parts[0][0]}${parts[1][0]}'.toUpperCase();
    }
    return parts[0][0].toUpperCase();
  }

  @override
  Widget build(BuildContext context) {
    final effectiveInitials = _calculateInitials();
    final url = imageUrl ?? user?.avatarUrl;

    Widget avatar = CircleAvatar(
      radius: radius,
      backgroundColor: backgroundColor,
      backgroundImage: (url != null && url.startsWith('http'))
          ? NetworkImage(url)
          : null,
      child: (url == null || !url.startsWith('http'))
          ? Text(
              effectiveInitials,
              style: TextStyle(
                fontSize: radius * 0.75,
                fontWeight: FontWeight.w700,
                color: textColor,
              ),
            )
          : null,
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
