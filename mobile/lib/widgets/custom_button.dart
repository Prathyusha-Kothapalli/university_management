import 'package:flutter/material.dart';
import '../core/theme/app_colors.dart';

enum ButtonVariant { primary, secondary, outline, outlined, text, danger }
enum ButtonVariant { primary, secondary, outline, text }

/// Reusable Material 3 custom button with loading state and icons.
enum ButtonVariant { primary, secondary, outlined, text, danger }

enum ButtonVariant { primary, secondary, outlined, text, danger }

enum ButtonVariant { primary, secondary, outline, text }

/// Reusable Material 3 custom button with loading state and icons.
class CustomButton extends StatelessWidget {
  final String text;
  final VoidCallback? onPressed;
  final bool isLoading;
  final ButtonVariant variant;
  final IconData? icon;
  final bool isFullWidth;
  final double? width;
  final double height;
  final double borderRadius;
  final double? width;
  final double height;
  final double borderRadius;
  final bool isFullWidth;
  final Color? backgroundColor;
  final Color? textColor;
  final Color? backgroundColor;
  final Color? textColor;

  const CustomButton({
    super.key,
    required this.text,
    required this.onPressed,
    this.isLoading = false,
    this.variant = ButtonVariant.primary,
    this.icon,
    this.isFullWidth = true,
    this.width,
    this.height = 50,
    this.borderRadius = 12,
    this.width = double.infinity,
    this.height = 50,
    this.borderRadius = 12,
    this.isFullWidth = true,
    this.backgroundColor,
    this.textColor,
    this.backgroundColor,
    this.textColor,
  });

  @override
  Widget build(BuildContext context) {
    final Widget child = isLoading
        ? SizedBox(
            height: 20,
            width: 20,
            child: CircularProgressIndicator(
              strokeWidth: 2.5,
              valueColor: AlwaysStoppedAnimation<Color>(
                variant == ButtonVariant.outline || variant == ButtonVariant.text
                    ? (textColor ?? AppColors.primary)
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
                variant == ButtonVariant.outlined || variant == ButtonVariant.text
                    ? AppColors.primary
                isOutline || isText
    final Widget child = isLoading
        ? SizedBox(
            height: 20,
            width: 20,
            child: CircularProgressIndicator(
              strokeWidth: 2.5,
              valueColor: AlwaysStoppedAnimation<Color>(
                variant == ButtonVariant.outline || variant == ButtonVariant.text
                    ? (textColor ?? AppColors.primary)
                    ? (textColor ?? AppColors.primary)
                    : Colors.white,
              ),
            ),
          )
        : Row(
            mainAxisSize: isFullWidth ? MainAxisSize.max : MainAxisSize.min,
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              if (icon != null) ...[
                Icon(icon, size: 20),
            mainAxisSize: MainAxisSize.min,
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              if (icon != null) ...[
                Icon(icon, size: 18),
            mainAxisSize: isFullWidth ? MainAxisSize.max : MainAxisSize.min,
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              if (icon != null) ...[
                Icon(icon, size: 20),
                Icon(icon, size: 18),
                Icon(icon, size: 20),
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
    switch (variant) {
      case ButtonVariant.primary:
        button = ElevatedButton(
          onPressed: isLoading ? null : onPressed,
          style: ElevatedButton.styleFrom(
            backgroundColor: backgroundColor ?? AppColors.primary,
            foregroundColor: textColor ?? Colors.white,
            disabledBackgroundColor: AppColors.primary.withOpacity(0.6),

    switch (variant) {
      case ButtonVariant.primary:
        button = ElevatedButton(
          onPressed: effectiveOnPressed,
    switch (variant) {
      case ButtonVariant.primary:
        button = ElevatedButton(
          onPressed: isLoading ? null : onPressed,
          style: ElevatedButton.styleFrom(
            backgroundColor: backgroundColor ?? AppColors.primary,
            foregroundColor: textColor ?? Colors.white,
            disabledBackgroundColor: AppColors.primary.withOpacity(0.6),
            elevation: 0,
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(borderRadius),
            ),
    switch (variant) {
      case ButtonVariant.primary:
        button = ElevatedButton(
          onPressed: isLoading ? null : onPressed,
          style: ElevatedButton.styleFrom(
            backgroundColor: backgroundColor ?? AppColors.primary,
            foregroundColor: textColor ?? Colors.white,
            disabledBackgroundColor: AppColors.primary.withOpacity(0.6),
          ),
          child: child,
        );
        break;

      case ButtonVariant.secondary:
        button = ElevatedButton(
          onPressed: isLoading ? null : onPressed,
          style: ElevatedButton.styleFrom(
            backgroundColor: backgroundColor ?? AppColors.secondary,
            foregroundColor: textColor ?? Colors.white,
          onPressed: effectiveOnPressed,
          style: ElevatedButton.styleFrom(
            backgroundColor: AppColors.secondary,
            foregroundColor: Colors.white,
          onPressed: effectiveOnPressed,
          style: ElevatedButton.styleFrom(
            backgroundColor: backgroundColor ?? AppColors.secondary,
            foregroundColor: textColor ?? Colors.white,
            disabledBackgroundColor: AppColors.secondary.withOpacity(0.6),
            elevation: 0,
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(borderRadius),
            ),
          onPressed: isLoading ? null : onPressed,
          style: ElevatedButton.styleFrom(
            backgroundColor: backgroundColor ?? AppColors.secondary,
            foregroundColor: textColor ?? Colors.white,
          ),
          child: child,
        );
        break;

      case ButtonVariant.outline:
        button = OutlinedButton(
          onPressed: isLoading ? null : onPressed,
          style: OutlinedButton.styleFrom(
            foregroundColor: textColor ?? AppColors.primary,
            side: BorderSide(color: backgroundColor ?? AppColors.primary, width: 1.5),
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
      case ButtonVariant.outline:
        button = OutlinedButton(
          onPressed: isLoading ? null : onPressed,
          style: OutlinedButton.styleFrom(
            foregroundColor: textColor ?? AppColors.primary,
            side: BorderSide(color: backgroundColor ?? AppColors.primary, width: 1.5),
          ),
          child: child,
        );
        break;

      case ButtonVariant.text:
        button = TextButton(
          onPressed: isLoading ? null : onPressed,
          style: TextButton.styleFrom(
            foregroundColor: textColor ?? AppColors.primary,
          onPressed: effectiveOnPressed,
          style: TextButton.styleFrom(
            foregroundColor: textColor ?? AppColors.primary,
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(borderRadius),
            ),
          onPressed: isLoading ? null : onPressed,
          style: TextButton.styleFrom(
            foregroundColor: textColor ?? AppColors.primary,
          ),
          child: child,
        );
        break;
    }

    if (isFullWidth) {
      return SizedBox(
        width: double.infinity,
        child: button,
      );
    }
    return button;
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
    if (isFullWidth) {
      return SizedBox(
        width: double.infinity,
        child: button,
      );
    }
    return button;
  }
}
