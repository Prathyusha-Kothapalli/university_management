import 'package:flutter/material.dart';
import '../core/theme/app_colors.dart';

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
/// Clean centered loading spinner with optional text.
class LoadingIndicator extends StatelessWidget {
  final String? message;
<<<<<<< HEAD
  final double size;
<<<<<<< HEAD
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
=======
=======
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
  final Color color;

  const LoadingIndicator({
    super.key,
    this.message,
<<<<<<< HEAD
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
=======
    this.size = 36,
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
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
<<<<<<< HEAD
          CircularProgressIndicator(
            valueColor: AlwaysStoppedAnimation<Color>(color),
            strokeWidth: 3,
=======
=======
>>>>>>> origin/web
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
          SizedBox(
            width: size,
            height: size,
            child: CircularProgressIndicator(
              strokeWidth: 3,
              valueColor: AlwaysStoppedAnimation<Color>(color),
            ),
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
=======
          CircularProgressIndicator(
            valueColor: AlwaysStoppedAnimation<Color>(color),
            strokeWidth: 3,
<<<<<<< HEAD
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
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
=======
              textAlign: TextAlign.center,
=======
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
            ),
          ],
        ],
      ),
    );
  }
}