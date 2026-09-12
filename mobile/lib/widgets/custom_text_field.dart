import 'package:flutter/material.dart';
import '../core/theme/app_colors.dart';

/// Reusable Material 3 text field with validation, icon support, and password visibility toggle.
class CustomTextField extends StatefulWidget {
  final TextEditingController? controller;
  final String? initialValue;
<<<<<<< HEAD
  final String? label;
  final String? hint;
  final IconData? prefixIcon;
  final Widget? suffixIcon;
=======
  final String label;
  final String? hint;
  final IconData? prefixIcon;
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9
  final bool isPassword;
  final TextInputType keyboardType;
  final TextInputAction textInputAction;
  final String? Function(String?)? validator;
  final void Function(String)? onChanged;
  final void Function(String)? onFieldSubmitted;
<<<<<<< HEAD
  final void Function(String)? onSubmitted;
  final bool enabled;
  final int maxLines;
  final FocusNode? focusNode;
=======
  final bool enabled;
  final int maxLines;
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9

  const CustomTextField({
    super.key,
    this.controller,
    this.initialValue,
<<<<<<< HEAD
    this.label,
    this.hint,
    this.prefixIcon,
    this.suffixIcon,
=======
    required this.label,
    this.hint,
    this.prefixIcon,
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9
    this.isPassword = false,
    this.keyboardType = TextInputType.text,
    this.textInputAction = TextInputAction.next,
    this.validator,
    this.onChanged,
    this.onFieldSubmitted,
<<<<<<< HEAD
    this.onSubmitted,
    this.enabled = true,
    this.maxLines = 1,
    this.focusNode,
=======
    this.enabled = true,
    this.maxLines = 1,
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9
  });

  @override
  State<CustomTextField> createState() => _CustomTextFieldState();
}

class _CustomTextFieldState extends State<CustomTextField> {
<<<<<<< HEAD
  late bool _obscureText;
=======
  bool _obscureText = true;
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9

  @override
  void initState() {
    super.initState();
    _obscureText = widget.isPassword;
  }

  @override
  Widget build(BuildContext context) {
<<<<<<< HEAD
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      mainAxisSize: MainAxisSize.min,
      children: [
        if (widget.label != null) ...[
          Text(
            widget.label!,
            style: const TextStyle(
              fontSize: 13,
              fontWeight: FontWeight.w600,
              color: AppColors.textSecondaryLight,
            ),
          ),
          const SizedBox(height: 6),
        ],
        TextFormField(
          controller: widget.controller,
          initialValue: widget.initialValue,
          focusNode: widget.focusNode,
          enabled: widget.enabled,
          obscureText: widget.isPassword && _obscureText,
          keyboardType: widget.keyboardType,
          textInputAction: widget.textInputAction,
          validator: widget.validator,
          onChanged: widget.onChanged,
          onFieldSubmitted: widget.onFieldSubmitted ?? widget.onSubmitted,
          maxLines: widget.maxLines,
          style: const TextStyle(
            fontSize: 15,
            fontWeight: FontWeight.w500,
            color: AppColors.textPrimaryLight,
          ),
          decoration: InputDecoration(
            hintText: widget.hint,
            prefixIcon: widget.prefixIcon != null
                ? Icon(widget.prefixIcon, size: 20, color: AppColors.textSecondaryLight)
                : null,
            suffixIcon: widget.isPassword
                ? IconButton(
                    icon: Icon(
                      _obscureText ? Icons.visibility_off_outlined : Icons.visibility_outlined,
                      size: 20,
                      color: AppColors.textSecondaryLight,
                    ),
                    onPressed: () {
                      setState(() {
                        _obscureText = !_obscureText;
                      });
                    },
                  )
                : widget.suffixIcon,
          ),
        ),
      ],
=======
    return TextFormField(
      controller: widget.controller,
      initialValue: widget.initialValue,
      obscureText: widget.isPassword && _obscureText,
      keyboardType: widget.keyboardType,
      textInputAction: widget.textInputAction,
      validator: widget.validator,
      onChanged: widget.onChanged,
      onFieldSubmitted: widget.onFieldSubmitted,
      enabled: widget.enabled,
      maxLines: widget.maxLines,
      style: const TextStyle(
        fontSize: 15,
        fontWeight: FontWeight.w500,
        color: AppColors.textPrimaryLight,
      ),
      decoration: InputDecoration(
        labelText: widget.label,
        hintText: widget.hint,
        prefixIcon: widget.prefixIcon != null
            ? Icon(widget.prefixIcon, size: 20, color: AppColors.textSecondaryLight)
            : null,
        suffixIcon: widget.isPassword
            ? IconButton(
                icon: Icon(
                  _obscureText ? Icons.visibility_outlined : Icons.visibility_off_outlined,
                  size: 20,
                  color: AppColors.textSecondaryLight,
                ),
                onPressed: () {
                  setState(() {
                    _obscureText = !_obscureText;
                  });
                },
              )
            : null,
      ),
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9
    );
  }
}
