import 'package:flutter/material.dart';
import '../core/theme/app_colors.dart';

<<<<<<< HEAD
<<<<<<< HEAD
/// Clean centered loading spinner with optional text.
class LoadingIndicator extends StatelessWidget {
  final String? message;
=======
class LoadingIndicator extends StatelessWidget {
  final String? message;
  final double size;
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
class LoadingIndicator extends StatelessWidget {
  final String? message;
  final double size;
=======
/// Clean centered loading spinner with optional text.
class LoadingIndicator extends StatelessWidget {
  final String? message;
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
  final Color color;

  const LoadingIndicator({
    super.key,
    this.message,
<<<<<<< HEAD
<<<<<<< HEAD
=======
    this.size = 36,
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
    this.size = 36,
=======
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
    this.color = AppColors.primary,
  });

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
<<<<<<< HEAD
<<<<<<< HEAD
          CircularProgressIndicator(
            valueColor: AlwaysStoppedAnimation<Color>(color),
            strokeWidth: 3,
=======
=======
>>>>>>> origin/web
          SizedBox(
            width: size,
            height: size,
            child: CircularProgressIndicator(
              strokeWidth: 3,
              valueColor: AlwaysStoppedAnimation<Color>(color),
            ),
<<<<<<< HEAD
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
=======
          CircularProgressIndicator(
            valueColor: AlwaysStoppedAnimation<Color>(color),
            strokeWidth: 3,
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
          ),
          if (message != null) ...[
            const SizedBox(height: 16),
            Text(
              message!,
              style: const TextStyle(
                fontSize: 14,
<<<<<<< HEAD
<<<<<<< HEAD
                fontWeight: FontWeight.w500,
                color: AppColors.textSecondaryLight,
              ),
=======
=======
>>>>>>> origin/web
                color: AppColors.textSecondaryLight,
                fontWeight: FontWeight.w500,
              ),
              textAlign: TextAlign.center,
<<<<<<< HEAD
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
=======
                fontWeight: FontWeight.w500,
                color: AppColors.textSecondaryLight,
              ),
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
            ),
          ],
        ],
      ),
    );
  }
}
