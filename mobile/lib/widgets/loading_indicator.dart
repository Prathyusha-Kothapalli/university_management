import 'package:flutter/material.dart';
import '../core/theme/app_colors.dart';

/// Clean centered loading spinner with optional text.
class LoadingIndicator extends StatelessWidget {
  final String? message;
<<<<<<< HEAD
  final double size;
=======
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9
  final Color color;

  const LoadingIndicator({
    super.key,
    this.message,
    this.size = 36,
    this.color = AppColors.primary,
  });

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
<<<<<<< HEAD
          SizedBox(
            width: size,
            height: size,
            child: CircularProgressIndicator(
              strokeWidth: 3,
              valueColor: AlwaysStoppedAnimation<Color>(color),
            ),
=======
          CircularProgressIndicator(
            valueColor: AlwaysStoppedAnimation<Color>(color),
            strokeWidth: 3,
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9
          ),
          if (message != null) ...[
            const SizedBox(height: 16),
            Text(
              message!,
              style: const TextStyle(
                fontSize: 14,
                fontWeight: FontWeight.w500,
                color: AppColors.textSecondaryLight,
              ),
<<<<<<< HEAD
              textAlign: TextAlign.center,
=======
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9
            ),
          ],
        ],
      ),
    );
  }
}