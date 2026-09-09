import 'package:flutter/material.dart';
import '../core/theme/app_colors.dart';

<<<<<<< HEAD
enum ButtonVariant { primary, secondary, outline, text }

/// Reusable Material 3 custom button with loading state and icons.
=======
enum ButtonVariant { primary, secondary, outlined, text, danger }

>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
class CustomButton extends StatelessWidget {
  final String text;
  final VoidCallback? onPressed;
  final bool isLoading;
  final ButtonVariant variant;
  final IconData? icon;
<<<<<<< HEAD
  final bool isFullWidth;
  final Color? backgroundColor;
  final Color? textColor;
=======
  final double? width;
  final double height;
  final double borderRadius;
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd

  const CustomButton({
    super.key,
    required this.text,
    required this.onPressed,
    this.isLoading = false,
    this.variant = ButtonVariant.primary,
    this.icon,
<<<<<<< HEAD
    this.isFullWidth = true,
    this.backgroundColor,
    this.textColor,
=======
    this.width = double.infinity,
    this.height = 50,
    this.borderRadius = 12,
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
  });

  @override
  Widget build(BuildContext context) {
<<<<<<< HEAD
    final Widget child = isLoading
        ? SizedBox(
            height: 20,
            width: 20,
            child: CircularProgressIndicator(
              strokeWidth: 2.5,
              valueColor: AlwaysStoppedAnimation<Color>(
                variant == ButtonVariant.outline || variant == ButtonVariant.text
                    ? (textColor ?? AppColors.primary)
=======
    final effectiveOnPressed = isLoading ? null : onPressed;

    Widget child = isLoading
        ? SizedBox(
            height: 22,
            width: 22,
            child: CircularProgressIndicator(
              strokeWidth: 2.5,
              valueColor: AlwaysStoppedAnimation<Color>(
                variant == ButtonVariant.outlined || variant == ButtonVariant.text
                    ? AppColors.primary
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
                    : Colors.white,
              ),
            ),
          )
        : Row(
<<<<<<< HEAD
            mainAxisSize: isFullWidth ? MainAxisSize.max : MainAxisSize.min,
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              if (icon != null) ...[
                Icon(icon, size: 20),
=======
            mainAxisSize: MainAxisSize.min,
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              if (icon != null) ...[
                Icon(icon, size: 18),
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
                const SizedBox(width: 8),
              ],
              Text(
                text,
                style: const TextStyle(
                  fontSize: 15,
                  fontWeight: FontWeight.w600,
                  letterSpacing: 0.2,
                ),
              ),
            ],
          );

    Widget button;
<<<<<<< HEAD
    switch (variant) {
      case ButtonVariant.primary:
        button = ElevatedButton(
          onPressed: isLoading ? null : onPressed,
          style: ElevatedButton.styleFrom(
            backgroundColor: backgroundColor ?? AppColors.primary,
            foregroundColor: textColor ?? Colors.white,
            disabledBackgroundColor: AppColors.primary.withOpacity(0.6),
=======

    switch (variant) {
      case ButtonVariant.primary:
        button = ElevatedButton(
          onPressed: effectiveOnPressed,
          style: ElevatedButton.styleFrom(
            backgroundColor: AppColors.primary,
            foregroundColor: Colors.white,
            disabledBackgroundColor: AppColors.primary.withOpacity(0.6),
            elevation: 0,
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(borderRadius),
            ),
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
          ),
          child: child,
        );
        break;

      case ButtonVariant.secondary:
        button = ElevatedButton(
<<<<<<< HEAD
          onPressed: isLoading ? null : onPressed,
          style: ElevatedButton.styleFrom(
            backgroundColor: backgroundColor ?? AppColors.secondary,
            foregroundColor: textColor ?? Colors.white,
=======
          onPressed: effectiveOnPressed,
          style: ElevatedButton.styleFrom(
            backgroundColor: AppColors.secondary,
            foregroundColor: Colors.white,
            disabledBackgroundColor: AppColors.secondary.withOpacity(0.6),
            elevation: 0,
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(borderRadius),
            ),
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
          ),
          child: child,
        );
        break;

<<<<<<< HEAD
      case ButtonVariant.outline:
        button = OutlinedButton(
          onPressed: isLoading ? null : onPressed,
          style: OutlinedButton.styleFrom(
            foregroundColor: textColor ?? AppColors.primary,
            side: BorderSide(color: backgroundColor ?? AppColors.primary, width: 1.5),
=======
      case ButtonVariant.danger:
        button = ElevatedButton(
          onPressed: effectiveOnPressed,
          style: ElevatedButton.styleFrom(
            backgroundColor: AppColors.error,
            foregroundColor: Colors.white,
            disabledBackgroundColor: AppColors.error.withOpacity(0.6),
            elevation: 0,
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(borderRadius),
            ),
          ),
          child: child,
        );
        break;

      case ButtonVariant.outlined:
        button = OutlinedButton(
          onPressed: effectiveOnPressed,
          style: OutlinedButton.styleFrom(
            foregroundColor: AppColors.primary,
            side: const BorderSide(color: AppColors.primary, width: 1.5),
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(borderRadius),
            ),
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
          ),
          child: child,
        );
        break;

      case ButtonVariant.text:
        button = TextButton(
<<<<<<< HEAD
          onPressed: isLoading ? null : onPressed,
          style: TextButton.styleFrom(
            foregroundColor: textColor ?? AppColors.primary,
=======
          onPressed: effectiveOnPressed,
          style: TextButton.styleFrom(
            foregroundColor: AppColors.primary,
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(borderRadius),
            ),
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
          ),
          child: child,
        );
        break;
    }

<<<<<<< HEAD
    if (isFullWidth) {
      return SizedBox(
        width: double.infinity,
        child: button,
      );
    }
    return button;
=======
    if (width != null) {
      return SizedBox(
        width: width,
        height: height,
        child: button,
      );
    }

    return SizedBox(height: height, child: button);
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
  }
}
