import 'package:flutter/material.dart';
import '../core/theme/app_colors.dart';

/// Reusable empty placeholder view with title, message, and optional action button.
class EmptyStateView extends StatelessWidget {
  final IconData icon;
  final String title;
  final String message;
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
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9
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
                color: AppColors.primary.withOpacity(0.08),
                shape: BoxShape.circle,
              ),
              child: Icon(
                icon,
                size: 48,
                color: AppColors.primary,
              ),
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
            if (actionText != null && onAction != null) ...[
              const SizedBox(height: 20),
              OutlinedButton(
                onPressed: onAction,
                child: Text(actionText!),
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9
              ),
            ],
          ],
        ),
      ),
    );
  }
}
