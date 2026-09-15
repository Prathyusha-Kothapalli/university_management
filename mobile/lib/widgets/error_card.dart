import 'package:flutter/material.dart';
import '../core/theme/app_colors.dart';

/// Dismissible / retryable error notification card.
/// Dismissible / retryable error notification card.
/// Dismissible / retryable error notification card.
class ErrorCard extends StatelessWidget {
  final String message;
  final VoidCallback? onDismiss;
  final VoidCallback? onRetry;

  const ErrorCard({
    super.key,
    required this.message,
    this.onDismiss,
    this.onRetry,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      margin: const EdgeInsets.symmetric(vertical: 8),
      padding: const EdgeInsets.all(14),
      decoration: BoxDecoration(
        color: AppColors.errorLight,
        borderRadius: BorderRadius.circular(12),
        border: Border.all(color: AppColors.error.withOpacity(0.3)),
      width: double.infinity,
      margin: const EdgeInsets.symmetric(vertical: 8),
      padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
      decoration: BoxDecoration(
        color: AppColors.errorLight,
        borderRadius: BorderRadius.circular(12),
        border: Border.all(color: AppColors.error.withOpacity(0.3), width: 1),
      margin: const EdgeInsets.symmetric(vertical: 8),
      padding: const EdgeInsets.all(14),
      decoration: BoxDecoration(
        color: AppColors.errorLight,
        borderRadius: BorderRadius.circular(12),
        border: Border.all(color: AppColors.error.withOpacity(0.3)),
      ),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          const Icon(
            Icons.error_outline_rounded,
            color: AppColors.error,
            size: 20,
          const Padding(
            padding: EdgeInsets.only(top: 2),
            child: Icon(
              Icons.error_outline_rounded,
              color: AppColors.error,
              size: 20,
            ),
          const Icon(
            Icons.error_outline_rounded,
            color: AppColors.error,
            size: 20,
          ),
          const SizedBox(width: 12),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              mainAxisSize: MainAxisSize.min,
              mainAxisSize: MainAxisSize.min,
              mainAxisSize: MainAxisSize.min,
              children: [
                Text(
                  message,
                  style: const TextStyle(
                    fontSize: 13.5,
                    fontWeight: FontWeight.w500,
                    color: Color(0xFF991B1B),
                    height: 1.3,
                    color: Color(0xFF991B1B),
                    fontSize: 13,
                    fontWeight: FontWeight.w500,
                    height: 1.4,
                    fontSize: 13.5,
                    fontWeight: FontWeight.w500,
                    color: Color(0xFF991B1B),
                    height: 1.3,
                  ),
                ),
                if (onRetry != null) ...[
                  const SizedBox(height: 6),
                  GestureDetector(
                    onTap: onRetry,
                    child: const Text(
                      'Tap to retry',
                      style: TextStyle(
                        fontSize: 12.5,
                        fontWeight: FontWeight.w700,
                        color: AppColors.error,
                        color: AppColors.error,
                        fontSize: 12,
                        fontWeight: FontWeight.w700,
                        color: AppColors.error,
                        fontSize: 12,
                        fontWeight: FontWeight.w700,
                        color: AppColors.error,
                        fontSize: 12,
                        fontWeight: FontWeight.w700,
                        fontSize: 12.5,
                        fontWeight: FontWeight.w700,
                        color: AppColors.error,
                        decoration: TextDecoration.underline,
                      ),
                    ),
                  ),
                ],
              ],
            ),
          ),
          if (onDismiss != null)
            GestureDetector(
              onTap: onDismiss,
              child: const Padding(
                padding: EdgeInsets.only(left: 8),
                child: Icon(
                  Icons.close_rounded,
                  size: 18,
                  color: Color(0xFF991B1B),
                ),
              child: const Icon(
                Icons.close_rounded,
                size: 18,
                color: Color(0xFF991B1B),
              child: const Padding(
                padding: EdgeInsets.only(left: 8),
                child: Icon(
                  Icons.close,
                  size: 18,
                  color: Color(0xFF991B1B),
                ),
              child: const Icon(
                Icons.close_rounded,
                size: 18,
                color: Color(0xFF991B1B),
              ),
            ),
        ],
      ),
    );
  }
}