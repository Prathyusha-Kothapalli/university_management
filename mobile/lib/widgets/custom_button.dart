import 'package:flutter/material.dart';
import '../core/theme/app_colors.dart';

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
enum ButtonVariant { primary, secondary, outline, outlined, text, danger }
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
enum ButtonVariant { primary, secondary, outline, text }
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9

/// Reusable Material 3 custom button with loading state and icons.
<<<<<<< HEAD
=======
enum ButtonVariant { primary, secondary, outlined, text, danger }

>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
enum ButtonVariant { primary, secondary, outlined, text, danger }

=======
enum ButtonVariant { primary, secondary, outline, text }

/// Reusable Material 3 custom button with loading state and icons.
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
class CustomButton extends StatelessWidget {
  final String text;
  final VoidCallback? onPressed;
  final bool isLoading;
  final ButtonVariant variant;
  final IconData? icon;
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
  final bool isFullWidth;
<<<<<<< HEAD
  final double? width;
  final double height;
  final double borderRadius;
<<<<<<< HEAD
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
  final double? width;
  final double height;
  final double borderRadius;
=======
  final bool isFullWidth;
  final Color? backgroundColor;
  final Color? textColor;
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
=======
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9
  final Color? backgroundColor;
  final Color? textColor;
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689

  const CustomButton({
    super.key,
    required this.text,
    required this.onPressed,
    this.isLoading = false,
    this.variant = ButtonVariant.primary,
    this.icon,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
    this.isFullWidth = true,
<<<<<<< HEAD
    this.width,
    this.height = 50,
    this.borderRadius = 12,
<<<<<<< HEAD
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
    this.width = double.infinity,
    this.height = 50,
    this.borderRadius = 12,
=======
    this.isFullWidth = true,
    this.backgroundColor,
    this.textColor,
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
=======
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9
    this.backgroundColor,
    this.textColor,
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
  });

  @override
  Widget build(BuildContext context) {
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
>>>>>>> origin/web
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
    final effectiveOnPressed = isLoading ? null : onPressed;

    final isOutline = variant == ButtonVariant.outline || variant == ButtonVariant.outlined;
    final isText = variant == ButtonVariant.text;

    Widget child = isLoading
        ? SizedBox(
            height: 22,
            width: 22,
            child: CircularProgressIndicator(
              strokeWidth: 2.5,
              valueColor: AlwaysStoppedAnimation<Color>(
<<<<<<< HEAD
                variant == ButtonVariant.outlined || variant == ButtonVariant.text
                    ? AppColors.primary
<<<<<<< HEAD
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
=======
                isOutline || isText
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
=======
    final Widget child = isLoading
        ? SizedBox(
            height: 20,
            width: 20,
            child: CircularProgressIndicator(
              strokeWidth: 2.5,
              valueColor: AlwaysStoppedAnimation<Color>(
                variant == ButtonVariant.outline || variant == ButtonVariant.text
<<<<<<< HEAD
                    ? (textColor ?? AppColors.primary)
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9
                    ? (textColor ?? AppColors.primary)
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
                    : Colors.white,
              ),
            ),
          )
        : Row(
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
            mainAxisSize: isFullWidth ? MainAxisSize.max : MainAxisSize.min,
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              if (icon != null) ...[
<<<<<<< HEAD
                Icon(icon, size: 20),
=======
=======
>>>>>>> origin/web
            mainAxisSize: MainAxisSize.min,
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              if (icon != null) ...[
                Icon(icon, size: 18),
<<<<<<< HEAD
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
=======
            mainAxisSize: isFullWidth ? MainAxisSize.max : MainAxisSize.min,
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              if (icon != null) ...[
                Icon(icon, size: 20),
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
<<<<<<< HEAD
                Icon(icon, size: 18),
=======
                Icon(icon, size: 20),
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
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
<<<<<<< HEAD
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
=======
>>>>>>> origin/web
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689

    switch (variant) {
      case ButtonVariant.primary:
        button = ElevatedButton(
          onPressed: effectiveOnPressed,
=======
    switch (variant) {
      case ButtonVariant.primary:
        button = ElevatedButton(
          onPressed: isLoading ? null : onPressed,
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9
          style: ElevatedButton.styleFrom(
            backgroundColor: backgroundColor ?? AppColors.primary,
            foregroundColor: textColor ?? Colors.white,
            disabledBackgroundColor: AppColors.primary.withOpacity(0.6),
<<<<<<< HEAD
            elevation: 0,
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(borderRadius),
            ),
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
=======
    switch (variant) {
      case ButtonVariant.primary:
        button = ElevatedButton(
          onPressed: isLoading ? null : onPressed,
          style: ElevatedButton.styleFrom(
            backgroundColor: backgroundColor ?? AppColors.primary,
            foregroundColor: textColor ?? Colors.white,
            disabledBackgroundColor: AppColors.primary.withOpacity(0.6),
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
=======
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
          ),
          child: child,
        );
        break;

      case ButtonVariant.secondary:
        button = ElevatedButton(
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
          onPressed: isLoading ? null : onPressed,
          style: ElevatedButton.styleFrom(
            backgroundColor: backgroundColor ?? AppColors.secondary,
            foregroundColor: textColor ?? Colors.white,
=======
=======
>>>>>>> origin/web
          onPressed: effectiveOnPressed,
          style: ElevatedButton.styleFrom(
            backgroundColor: AppColors.secondary,
            foregroundColor: Colors.white,
=======
          onPressed: effectiveOnPressed,
          style: ElevatedButton.styleFrom(
            backgroundColor: backgroundColor ?? AppColors.secondary,
            foregroundColor: textColor ?? Colors.white,
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
            disabledBackgroundColor: AppColors.secondary.withOpacity(0.6),
            elevation: 0,
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(borderRadius),
            ),
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
=======
          onPressed: isLoading ? null : onPressed,
          style: ElevatedButton.styleFrom(
            backgroundColor: backgroundColor ?? AppColors.secondary,
            foregroundColor: textColor ?? Colors.white,
<<<<<<< HEAD
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
          ),
          child: child,
        );
        break;

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
      case ButtonVariant.outline:
        button = OutlinedButton(
          onPressed: isLoading ? null : onPressed,
          style: OutlinedButton.styleFrom(
            foregroundColor: textColor ?? AppColors.primary,
            side: BorderSide(color: backgroundColor ?? AppColors.primary, width: 1.5),
=======
=======
>>>>>>> origin/web
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
      case ButtonVariant.danger:
        button = ElevatedButton(
          onPressed: effectiveOnPressed,
          style: ElevatedButton.styleFrom(
            backgroundColor: backgroundColor ?? AppColors.error,
            foregroundColor: textColor ?? Colors.white,
            disabledBackgroundColor: AppColors.error.withOpacity(0.6),
            elevation: 0,
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(borderRadius),
            ),
          ),
          child: child,
        );
        break;

      case ButtonVariant.outline:
      case ButtonVariant.outlined:
        button = OutlinedButton(
          onPressed: effectiveOnPressed,
          style: OutlinedButton.styleFrom(
            foregroundColor: textColor ?? AppColors.primary,
            side: BorderSide(
              color: backgroundColor ?? AppColors.primary,
              width: 1.5,
            ),
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(borderRadius),
            ),
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
=======
      case ButtonVariant.outline:
        button = OutlinedButton(
          onPressed: isLoading ? null : onPressed,
          style: OutlinedButton.styleFrom(
            foregroundColor: textColor ?? AppColors.primary,
            side: BorderSide(color: backgroundColor ?? AppColors.primary, width: 1.5),
<<<<<<< HEAD
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
          ),
          child: child,
        );
        break;

      case ButtonVariant.text:
        button = TextButton(
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
          onPressed: isLoading ? null : onPressed,
          style: TextButton.styleFrom(
            foregroundColor: textColor ?? AppColors.primary,
=======
=======
>>>>>>> origin/web
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
          onPressed: effectiveOnPressed,
          style: TextButton.styleFrom(
            foregroundColor: textColor ?? AppColors.primary,
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(borderRadius),
            ),
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
=======
          onPressed: isLoading ? null : onPressed,
          style: TextButton.styleFrom(
            foregroundColor: textColor ?? AppColors.primary,
<<<<<<< HEAD
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
          ),
          child: child,
        );
        break;
    }

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    if (isFullWidth) {
      return SizedBox(
        width: double.infinity,
        child: button,
      );
    }
    return button;
=======
=======
>>>>>>> origin/web
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
    if (width != null) {
      return SizedBox(
        width: width,
        height: height,
        child: button,
      );
    }

    if (isFullWidth) {
      return SizedBox(
        width: double.infinity,
        height: height,
        child: button,
      );
    }

    return SizedBox(height: height, child: button);
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
=======
    if (isFullWidth) {
      return SizedBox(
        width: double.infinity,
        child: button,
      );
    }
    return button;
<<<<<<< HEAD
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
  }
}
