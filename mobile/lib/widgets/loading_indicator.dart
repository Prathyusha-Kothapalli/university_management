import 'package:flutter/material.dart';
import '../core/theme/app_colors.dart';

<<<<<<< HEAD
/// Clean centered loading spinner with optional text.
class LoadingIndicator extends StatelessWidget {
  final String? message;
=======
class LoadingIndicator extends StatelessWidget {
  final String? message;
  final double size;
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
  final Color color;

  const LoadingIndicator({
    super.key,
    this.message,
<<<<<<< HEAD
=======
    this.size = 36,
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
    this.color = AppColors.primary,
  });

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
<<<<<<< HEAD
          CircularProgressIndicator(
            valueColor: AlwaysStoppedAnimation<Color>(color),
            strokeWidth: 3,
=======
          SizedBox(
            width: size,
            height: size,
            child: CircularProgressIndicator(
              strokeWidth: 3,
              valueColor: AlwaysStoppedAnimation<Color>(color),
            ),
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
          ),
          if (message != null) ...[
            const SizedBox(height: 16),
            Text(
              message!,
              style: const TextStyle(
                fontSize: 14,
<<<<<<< HEAD
                fontWeight: FontWeight.w500,
                color: AppColors.textSecondaryLight,
              ),
=======
                color: AppColors.textSecondaryLight,
                fontWeight: FontWeight.w500,
              ),
              textAlign: TextAlign.center,
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
            ),
          ],
        ],
      ),
    );
  }
}
