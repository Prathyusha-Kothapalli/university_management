import 'package:flutter/material.dart';
import '../core/theme/app_colors.dart';
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD

/// Reusable empty placeholder view with title, message, and optional action button.
=======
import 'custom_button.dart';

>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
import 'custom_button.dart';

=======

/// Reusable empty placeholder view with title, message, and optional action button.
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======

/// Reusable empty placeholder view with title, message, and optional action button.
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
class EmptyStateView extends StatelessWidget {
  final IconData icon;
  final String title;
  final String message;
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
  final String? actionText;
<<<<<<< HEAD
  final String? buttonText;
  final VoidCallback? onAction;
  final VoidCallback? onButtonPressed;

  const EmptyStateView({
    super.key,
    this.icon = Icons.inbox_outlined,
    required this.title,
    required this.message,
    this.actionText,
    this.buttonText,
    this.onAction,
    this.onButtonPressed,
=======
  final VoidCallback? onAction;

  const EmptyStateView({
    super.key,
    required this.icon,
    required this.title,
    required this.message,
    this.actionText,
    this.onAction,
<<<<<<< HEAD
=======
=======
>>>>>>> origin/web
  final String? buttonText;
  final VoidCallback? onButtonPressed;

  const EmptyStateView({
    super.key,
    this.icon = Icons.inbox_outlined,
    required this.title,
    required this.message,
    this.buttonText,
    this.onButtonPressed,
<<<<<<< HEAD
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
=======
  final String? actionText;
  final VoidCallback? onAction;

  const EmptyStateView({
    super.key,
    required this.icon,
    required this.title,
    required this.message,
    this.actionText,
    this.onAction,
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
  });

  @override
  Widget build(BuildContext context) {
    final label = actionText ?? buttonText;
    final callback = onAction ?? onButtonPressed;

    return Center(
      child: Padding(
        padding: const EdgeInsets.all(32),
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            Container(
              padding: const EdgeInsets.all(20),
              decoration: BoxDecoration(
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
                color: AppColors.primaryLight,
                shape: BoxShape.circle,
              ),
              child: Icon(icon, size: 48, color: AppColors.primary),
=======
>>>>>>> origin/web
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
                color: AppColors.primary.withOpacity(0.08),
                shape: BoxShape.circle,
              ),
              child: Icon(
                icon,
                size: 48,
                color: AppColors.primary,
              ),
<<<<<<< HEAD
<<<<<<< HEAD
=======
                color: AppColors.primaryLight,
                shape: BoxShape.circle,
              ),
              child: Icon(icon, size: 48, color: AppColors.primary),
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
            ),
            const SizedBox(height: 20),
            Text(
              title,
              style: const TextStyle(
                fontSize: 18,
                fontWeight: FontWeight.w700,
                color: AppColors.textPrimaryLight,
              ),
              textAlign: TextAlign.center,
            ),
            const SizedBox(height: 8),
            Text(
              message,
              style: const TextStyle(
                fontSize: 14,
                color: AppColors.textSecondaryLight,
                height: 1.4,
              ),
              textAlign: TextAlign.center,
            ),
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
            if (label != null && callback != null) ...[
              const SizedBox(height: 20),
              ElevatedButton(
                onPressed: callback,
                style: ElevatedButton.styleFrom(
                  backgroundColor: AppColors.primary,
                  foregroundColor: Colors.white,
                  shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(12),
                  ),
                  padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 12),
                ),
                child: Text(label),
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
            if (actionText != null && onAction != null) ...[
              const SizedBox(height: 20),
              OutlinedButton(
                onPressed: onAction,
                child: Text(actionText!),
<<<<<<< HEAD
=======
=======
>>>>>>> origin/web
            if (buttonText != null && onButtonPressed != null) ...[
              const SizedBox(height: 24),
              CustomButton(
                text: buttonText!,
                onPressed: onButtonPressed,
                width: 180,
                height: 44,
<<<<<<< HEAD
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
=======
            if (actionText != null && onAction != null) ...[
              const SizedBox(height: 20),
              OutlinedButton(
                onPressed: onAction,
                child: Text(actionText!),
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
              ),
            ],
          ],
        ),
      ),
    );
  }
}
