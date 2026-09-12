import 'package:flutter/material.dart';
import '../../core/theme/app_colors.dart';
import '../../core/utils/validators.dart';
import '../../models/user.dart';
import '../../state/auth_state.dart';
import '../../state/profile_state.dart';
import '../../widgets/custom_button.dart';
import '../../widgets/custom_text_field.dart';

<<<<<<< HEAD
<<<<<<< HEAD
/// Modal dialog for modifying user contact details.
=======
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
=======
/// Modal dialog for modifying user contact details.
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
class EditProfileDialog extends StatefulWidget {
  final User currentUser;
  final AuthState authState;
  final ProfileState profileState;

  const EditProfileDialog({
    super.key,
    required this.currentUser,
    required this.authState,
    required this.profileState,
  });

  static Future<bool?> show(
    BuildContext context, {
    required User currentUser,
    required AuthState authState,
    required ProfileState profileState,
  }) {
    return showDialog<bool>(
      context: context,
      builder: (ctx) => EditProfileDialog(
        currentUser: currentUser,
        authState: authState,
        profileState: profileState,
      ),
    );
  }

  @override
  State<EditProfileDialog> createState() => _EditProfileDialogState();
}

class _EditProfileDialogState extends State<EditProfileDialog> {
  final _formKey = GlobalKey<FormState>();
  late final TextEditingController _nameController;
  late final TextEditingController _phoneController;

  @override
  void initState() {
    super.initState();
    _nameController = TextEditingController(text: widget.currentUser.name);
    _phoneController = TextEditingController(text: widget.currentUser.phone ?? '');
  }

  @override
  void dispose() {
    _nameController.dispose();
    _phoneController.dispose();
    super.dispose();
  }

  Future<void> _handleSave() async {
    if (!_formKey.currentState!.validate()) return;

    final updated = await widget.profileState.updateProfile(
      widget.currentUser,
      name: _nameController.text.trim(),
      phone: _phoneController.text.trim(),
    );

    if (updated != null && mounted) {
      widget.authState.updateUser(updated);
      Navigator.of(context).pop(true);
    }
  }

  @override
  Widget build(BuildContext context) {
    final isSaving = widget.profileState.isSaving;

    return Dialog(
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(20)),
      child: Padding(
        padding: const EdgeInsets.all(24),
        child: Form(
          key: _formKey,
          child: Column(
            mainAxisSize: MainAxisSize.min,
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  const Text(
                    'Edit Profile',
                    style: TextStyle(
                      fontSize: 18,
                      fontWeight: FontWeight.w700,
                      color: AppColors.textPrimaryLight,
                    ),
                  ),
                  IconButton(
                    icon: const Icon(Icons.close_rounded, size: 20),
                    onPressed: isSaving ? null : () => Navigator.of(context).pop(false),
                  ),
                ],
              ),
              const SizedBox(height: 16),
              CustomTextField(
                controller: _nameController,
                label: 'Full Name',
                prefixIcon: Icons.person_outline_rounded,
                validator: Validators.validateName,
              ),
              const SizedBox(height: 16),
              CustomTextField(
                controller: _phoneController,
                label: 'Phone Number',
                prefixIcon: Icons.phone_outlined,
                keyboardType: TextInputType.phone,
                validator: Validators.validatePhone,
              ),
              const SizedBox(height: 24),
              CustomButton(
                text: 'Save Changes',
                onPressed: _handleSave,
                isLoading: isSaving,
                icon: Icons.check_circle_outline_rounded,
              ),
            ],
          ),
        ),
      ),
    );
  }
}
