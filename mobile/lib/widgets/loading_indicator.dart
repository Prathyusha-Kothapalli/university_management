import 'package:flutter/material.dart';
import '../core/theme/app_colors.dart';

/// Clean centered loading spinner with optional text.
class LoadingIndicator extends StatelessWidget {
  final String? message;
  final double size;
class LoadingIndicator extends StatelessWidget {
  final String? message;
  final double size;
/// Clean centered loading spinner with optional text.
class LoadingIndicator extends StatelessWidget {
  final String? message;
  final Color color;

  const LoadingIndicator({
    super.key,
    this.message,
    this.size = 36,
    this.size = 36,
    this.size = 36,
    this.color = AppColors.primary,
  });

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          CircularProgressIndicator(
            valueColor: AlwaysStoppedAnimation<Color>(color),
            strokeWidth: 3,
          SizedBox(
            width: size,
            height: size,
            child: CircularProgressIndicator(
              strokeWidth: 3,
              valueColor: AlwaysStoppedAnimation<Color>(color),
            ),
          CircularProgressIndicator(
            valueColor: AlwaysStoppedAnimation<Color>(color),
            strokeWidth: 3,
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
                fontWeight: FontWeight.w500,
                color: AppColors.textSecondaryLight,
              ),
                color: AppColors.textSecondaryLight,
                fontWeight: FontWeight.w500,
              ),
              textAlign: TextAlign.center,
                fontWeight: FontWeight.w500,
                color: AppColors.textSecondaryLight,
              ),
              textAlign: TextAlign.center,
            ),
          ],
        ],
      ),
    );
  }
}