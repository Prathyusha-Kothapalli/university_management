import 'package:flutter/material.dart';
import '../core/theme/app_colors.dart';

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
class CustomTextField extends StatefulWidget {
  final TextEditingController? controller;
  final String? label;
  final String? hint;
  final IconData? prefixIcon;
  final Widget? suffixIcon;
=======
>>>>>>> origin/web
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
/// Reusable Material 3 text field with validation, icon support, and password visibility toggle.
class CustomTextField extends StatefulWidget {
  final TextEditingController? controller;
  final String? initialValue;
<<<<<<< HEAD
  final String label;
  final String? hint;
  final IconData? prefixIcon;
<<<<<<< HEAD
=======
class CustomTextField extends StatefulWidget {
  final TextEditingController? controller;
=======
<<<<<<< HEAD
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
  final String? label;
  final String? hint;
  final IconData? prefixIcon;
  final Widget? suffixIcon;
<<<<<<< HEAD
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
=======
  final String label;
  final String? hint;
  final IconData? prefixIcon;
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
  final bool isPassword;
  final TextInputType keyboardType;
  final TextInputAction textInputAction;
  final String? Function(String?)? validator;
  final void Function(String)? onChanged;
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
  final void Function(String)? onFieldSubmitted;
  final bool enabled;
  final int maxLines;
=======
=======
>>>>>>> origin/web
=======
  final void Function(String)? onFieldSubmitted;
<<<<<<< HEAD
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
  final void Function(String)? onSubmitted;
  final bool enabled;
  final int maxLines;
  final FocusNode? focusNode;
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
=======
  final void Function(String)? onFieldSubmitted;
  final bool enabled;
  final int maxLines;
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
=======
  final bool enabled;
  final int maxLines;
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689

  const CustomTextField({
    super.key,
    this.controller,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    this.initialValue,
    required this.label,
    this.hint,
    this.prefixIcon,
=======
=======
>>>>>>> origin/web
=======
    this.initialValue,
<<<<<<< HEAD
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
    this.label,
    this.hint,
    this.prefixIcon,
    this.suffixIcon,
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
=======
    this.initialValue,
    required this.label,
    this.hint,
    this.prefixIcon,
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
=======
    required this.label,
    this.hint,
    this.prefixIcon,
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
    this.isPassword = false,
    this.keyboardType = TextInputType.text,
    this.textInputAction = TextInputAction.next,
    this.validator,
    this.onChanged,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    this.onFieldSubmitted,
    this.enabled = true,
    this.maxLines = 1,
=======
=======
>>>>>>> origin/web
=======
    this.onFieldSubmitted,
<<<<<<< HEAD
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
    this.onSubmitted,
    this.enabled = true,
    this.maxLines = 1,
    this.focusNode,
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
=======
    this.onFieldSubmitted,
    this.enabled = true,
    this.maxLines = 1,
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
=======
    this.enabled = true,
    this.maxLines = 1,
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
  });

  @override
  State<CustomTextField> createState() => _CustomTextFieldState();
}

class _CustomTextFieldState extends State<CustomTextField> {
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
  bool _obscureText = true;
=======
  late bool _obscureText;
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
  late bool _obscureText;
=======
  bool _obscureText = true;
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
  late bool _obscureText;
=======
  bool _obscureText = true;
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689

  @override
  void initState() {
    super.initState();
    _obscureText = widget.isPassword;
  }

  @override
  Widget build(BuildContext context) {
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
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
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
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
<<<<<<< HEAD
=======
=======
>>>>>>> origin/web
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
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
          focusNode: widget.focusNode,
          enabled: widget.enabled,
          obscureText: _obscureText,
          keyboardType: widget.keyboardType,
          textInputAction: widget.textInputAction,
          validator: widget.validator,
          onChanged: widget.onChanged,
          onFieldSubmitted: widget.onSubmitted,
          maxLines: widget.maxLines,
          style: const TextStyle(
            fontSize: 15,
            fontWeight: FontWeight.w400,
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
<<<<<<< HEAD
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
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
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
    );
  }
}
