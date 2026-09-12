import 'package:flutter/material.dart';
import '../core/theme/app_colors.dart';

<<<<<<< HEAD
=======
/// Dismissible / retryable error notification card.
>>>>>>> 29907a7 (added flutter)
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
<<<<<<< HEAD
      width: double.infinity,
      padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
      decoration: BoxDecoration(
        color: AppColors.errorLight,
        borderRadius: BorderRadius.circular(12),
        border: Border.all(color: AppColors.error.withOpacity(0.3), width: 1),
=======
      margin: const EdgeInsets.symmetric(vertical: 8),
      padding: const EdgeInsets.all(14),
      decoration: BoxDecoration(
        color: AppColors.errorLight,
        borderRadius: BorderRadius.circular(12),
        border: Border.all(color: AppColors.error.withOpacity(0.3)),
>>>>>>> 29907a7 (added flutter)
      ),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
<<<<<<< HEAD
          const Padding(
            padding: EdgeInsets.only(top: 2),
            child: Icon(
              Icons.error_outline_rounded,
              color: AppColors.error,
              size: 20,
            ),
=======
          const Icon(
            Icons.error_outline_rounded,
            color: AppColors.error,
            size: 20,
>>>>>>> 29907a7 (added flutter)
          ),
          const SizedBox(width: 12),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
<<<<<<< HEAD
              mainAxisSize: MainAxisSize.min,
=======
>>>>>>> 29907a7 (added flutter)
              children: [
                Text(
                  message,
                  style: const TextStyle(
<<<<<<< HEAD
                    color: Color(0xFF991B1B),
                    fontSize: 13,
                    fontWeight: FontWeight.w500,
                    height: 1.4,
=======
                    fontSize: 13.5,
                    fontWeight: FontWeight.w500,
                    color: Color(0xFF991B1B),
                    height: 1.3,
>>>>>>> 29907a7 (added flutter)
                  ),
                ),
                if (onRetry != null) ...[
                  const SizedBox(height: 6),
                  GestureDetector(
                    onTap: onRetry,
                    child: const Text(
                      'Tap to retry',
                      style: TextStyle(
<<<<<<< HEAD
                        color: AppColors.error,
                        fontSize: 12,
                        fontWeight: FontWeight.w700,
=======
                        fontSize: 12.5,
                        fontWeight: FontWeight.w700,
                        color: AppColors.error,
>>>>>>> 29907a7 (added flutter)
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
<<<<<<< HEAD
              child: const Padding(
                padding: EdgeInsets.only(left: 8),
                child: Icon(
                  Icons.close,
                  size: 18,
                  color: Color(0xFF991B1B),
                ),
=======
              child: const Icon(
                Icons.close_rounded,
                size: 18,
                color: Color(0xFF991B1B),
>>>>>>> 29907a7 (added flutter)
              ),
            ),
        ],
      ),
    );
  }
}
