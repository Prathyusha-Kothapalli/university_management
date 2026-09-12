import 'package:flutter/material.dart';
import '../core/theme/app_colors.dart';

<<<<<<< HEAD
<<<<<<< HEAD
/// Dismissible / retryable error notification card.
=======
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
=======
/// Dismissible / retryable error notification card.
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
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
<<<<<<< HEAD
      margin: const EdgeInsets.symmetric(vertical: 8),
      padding: const EdgeInsets.all(14),
      decoration: BoxDecoration(
        color: AppColors.errorLight,
        borderRadius: BorderRadius.circular(12),
        border: Border.all(color: AppColors.error.withOpacity(0.3)),
=======
=======
>>>>>>> origin/web
      width: double.infinity,
      padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
      decoration: BoxDecoration(
        color: AppColors.errorLight,
        borderRadius: BorderRadius.circular(12),
        border: Border.all(color: AppColors.error.withOpacity(0.3), width: 1),
<<<<<<< HEAD
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
=======
      margin: const EdgeInsets.symmetric(vertical: 8),
      padding: const EdgeInsets.all(14),
      decoration: BoxDecoration(
        color: AppColors.errorLight,
        borderRadius: BorderRadius.circular(12),
        border: Border.all(color: AppColors.error.withOpacity(0.3)),
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
      ),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
<<<<<<< HEAD
<<<<<<< HEAD
          const Icon(
            Icons.error_outline_rounded,
            color: AppColors.error,
            size: 20,
=======
=======
>>>>>>> origin/web
          const Padding(
            padding: EdgeInsets.only(top: 2),
            child: Icon(
              Icons.error_outline_rounded,
              color: AppColors.error,
              size: 20,
            ),
<<<<<<< HEAD
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
=======
          const Icon(
            Icons.error_outline_rounded,
            color: AppColors.error,
            size: 20,
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
          ),
          const SizedBox(width: 12),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
<<<<<<< HEAD
<<<<<<< HEAD
=======
              mainAxisSize: MainAxisSize.min,
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
              mainAxisSize: MainAxisSize.min,
=======
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
              children: [
                Text(
                  message,
                  style: const TextStyle(
<<<<<<< HEAD
<<<<<<< HEAD
                    fontSize: 13.5,
                    fontWeight: FontWeight.w500,
                    color: Color(0xFF991B1B),
                    height: 1.3,
=======
=======
>>>>>>> origin/web
                    color: Color(0xFF991B1B),
                    fontSize: 13,
                    fontWeight: FontWeight.w500,
                    height: 1.4,
<<<<<<< HEAD
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
=======
                    fontSize: 13.5,
                    fontWeight: FontWeight.w500,
                    color: Color(0xFF991B1B),
                    height: 1.3,
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
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
<<<<<<< HEAD
                        fontSize: 12.5,
                        fontWeight: FontWeight.w700,
                        color: AppColors.error,
=======
                        color: AppColors.error,
                        fontSize: 12,
                        fontWeight: FontWeight.w700,
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
                        color: AppColors.error,
                        fontSize: 12,
                        fontWeight: FontWeight.w700,
=======
                        fontSize: 12.5,
                        fontWeight: FontWeight.w700,
                        color: AppColors.error,
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
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
<<<<<<< HEAD
              child: const Icon(
                Icons.close_rounded,
                size: 18,
                color: Color(0xFF991B1B),
=======
=======
>>>>>>> origin/web
              child: const Padding(
                padding: EdgeInsets.only(left: 8),
                child: Icon(
                  Icons.close,
                  size: 18,
                  color: Color(0xFF991B1B),
                ),
<<<<<<< HEAD
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
=======
              child: const Icon(
                Icons.close_rounded,
                size: 18,
                color: Color(0xFF991B1B),
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
              ),
            ),
        ],
      ),
    );
  }
}
