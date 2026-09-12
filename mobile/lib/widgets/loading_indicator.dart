import 'package:flutter/material.dart';
import '../core/theme/app_colors.dart';

<<<<<<< HEAD
class LoadingIndicator extends StatelessWidget {
  final String? message;
  final double size;
=======
/// Clean centered loading spinner with optional text.
class LoadingIndicator extends StatelessWidget {
  final String? message;
>>>>>>> 29907a7 (added flutter)
  final Color color;

  const LoadingIndicator({
    super.key,
    this.message,
<<<<<<< HEAD
    this.size = 36,
=======
>>>>>>> 29907a7 (added flutter)
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
>>>>>>> 29907a7 (added flutter)
          ),
          if (message != null) ...[
            const SizedBox(height: 16),
            Text(
              message!,
              style: const TextStyle(
                fontSize: 14,
<<<<<<< HEAD
                color: AppColors.textSecondaryLight,
                fontWeight: FontWeight.w500,
              ),
              textAlign: TextAlign.center,
=======
                fontWeight: FontWeight.w500,
                color: AppColors.textSecondaryLight,
              ),
>>>>>>> 29907a7 (added flutter)
            ),
          ],
        ],
      ),
    );
  }
}
