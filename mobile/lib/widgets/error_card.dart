import 'package:flutter/material.dart';
import '../core/theme/app_colors.dart';

<<<<<<< HEAD
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
=======
/// Dismissible / retryable error notification card.
<<<<<<< HEAD
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
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
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
      width: double.infinity,
      margin: const EdgeInsets.symmetric(vertical: 8),
      padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
      decoration: BoxDecoration(
        color: AppColors.errorLight,
        borderRadius: BorderRadius.circular(12),
        border: Border.all(color: AppColors.error.withOpacity(0.3), width: 1),
<<<<<<< HEAD
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
=======
=======
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
      ),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
          const Icon(
            Icons.error_outline_rounded,
            color: AppColors.error,
            size: 20,
=======
=======
>>>>>>> origin/web
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
          const Padding(
            padding: EdgeInsets.only(top: 2),
            child: Icon(
              Icons.error_outline_rounded,
              color: AppColors.error,
              size: 20,
            ),
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
=======
          const Icon(
            Icons.error_outline_rounded,
            color: AppColors.error,
            size: 20,
<<<<<<< HEAD
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
          ),
          const SizedBox(width: 12),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
<<<<<<< HEAD
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
=======
              mainAxisSize: MainAxisSize.min,
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
              children: [
                Text(
                  message,
                  style: const TextStyle(
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                    fontSize: 13.5,
                    fontWeight: FontWeight.w500,
                    color: Color(0xFF991B1B),
                    height: 1.3,
=======
=======
>>>>>>> origin/web
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
                    color: Color(0xFF991B1B),
                    fontSize: 13,
                    fontWeight: FontWeight.w500,
                    height: 1.4,
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
=======
                    fontSize: 13.5,
                    fontWeight: FontWeight.w500,
                    color: Color(0xFF991B1B),
                    height: 1.3,
<<<<<<< HEAD
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
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
                        color: AppColors.error,
                        fontSize: 12,
                        fontWeight: FontWeight.w700,
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
=======
                        fontSize: 12.5,
                        fontWeight: FontWeight.w700,
                        color: AppColors.error,
<<<<<<< HEAD
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
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
<<<<<<< HEAD
=======
              child: const Padding(
                padding: EdgeInsets.only(left: 8),
                child: Icon(
                  Icons.close_rounded,
                  size: 18,
                  color: Color(0xFF991B1B),
                ),
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
              child: const Icon(
                Icons.close_rounded,
                size: 18,
                color: Color(0xFF991B1B),
<<<<<<< HEAD
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
=======
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
              ),
            ),
        ],
      ),
    );
  }
}