import 'package:flutter/material.dart';
import '../core/theme/app_colors.dart';

class UserAvatar extends StatelessWidget {
  final String? imageUrl;
  final String initials;
  final double radius;
  final Color backgroundColor;
  final Color textColor;
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
    return avatar;
  }
}
