import 'package:flutter/material.dart';
import '../core/theme/app_colors.dart';
<<<<<<< HEAD
<<<<<<< HEAD
import '../models/user.dart';

/// User Avatar display widget with initial letters fallback.
class UserAvatar extends StatelessWidget {
  final User? user;
  final double radius;
=======
=======
>>>>>>> origin/web

class UserAvatar extends StatelessWidget {
  final String? imageUrl;
  final String initials;
  final double radius;
  final Color backgroundColor;
  final Color textColor;
<<<<<<< HEAD
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
=======
import '../models/user.dart';

/// User Avatar display widget with initial letters fallback.
class UserAvatar extends StatelessWidget {
  final User? user;
  final double radius;
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
  final VoidCallback? onTap;

  const UserAvatar({
    super.key,
<<<<<<< HEAD
<<<<<<< HEAD
=======
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
=======
>>>>>>> origin/web
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

<<<<<<< HEAD
=======
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
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
    return avatar;
  }
}
