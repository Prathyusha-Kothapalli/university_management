import 'package:flutter/material.dart';
import '../core/theme/app_colors.dart';
import '../models/user.dart';

/// User Avatar display widget with initial letters fallback.
class UserAvatar extends StatelessWidget {
  final User? user;
  final double radius;

class UserAvatar extends StatelessWidget {
  final String? imageUrl;
  final String? initials;
  final double radius;
  final Color backgroundColor;
  final Color textColor;
import '../models/user.dart';

/// User Avatar display widget with initial letters fallback.
class UserAvatar extends StatelessWidget {
  final User? user;
  final double radius;
  final double radius;
  final VoidCallback? onTap;

  const UserAvatar({
    super.key,
    this.imageUrl,
    required this.initials,
    this.radius = 24,
    this.backgroundColor = AppColors.primaryLight,
    this.textColor = AppColors.primaryDark,
    this.onTap,
  });

  @override
  Widget build(BuildContext context) {
    Widget avatar = CircleAvatar(
      radius: radius,
      backgroundColor: backgroundColor,
      backgroundImage: imageUrl != null && imageUrl!.startsWith('http')
          ? NetworkImage(imageUrl!)
          : null,
      child: (imageUrl == null || !imageUrl!.startsWith('http'))
          ? Text(
              initials,
              style: TextStyle(
                fontSize: radius * 0.75,
                fontWeight: FontWeight.w700,
                color: textColor,
              ),
            )
          : null,
    );

    if (onTap != null) {
      return GestureDetector(onTap: onTap, child: avatar);
    }
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


  @override
  Widget build(BuildContext context) {
    Widget avatar = CircleAvatar(
      radius: radius,
      backgroundColor: backgroundColor,
      backgroundImage: imageUrl != null && imageUrl!.startsWith('http')
          ? NetworkImage(imageUrl!)
          : null,
      child: (imageUrl == null || !imageUrl!.startsWith('http'))
          ? Text(
              initials,
              style: TextStyle(
                fontSize: radius * 0.75,
                fontWeight: FontWeight.w700,
                color: textColor,
              ),
            )
          : null,
    );

    if (onTap != null) {
      return GestureDetector(onTap: onTap, child: avatar);
    }
    return avatar;
  }
}
