import 'package:flutter/material.dart';
<<<<<<< HEAD
=======
import '../../core/constants/route_constants.dart';
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
import '../../core/theme/app_colors.dart';
import '../../core/utils/validators.dart';
import '../../models/register_request.dart';
import '../../state/auth_state.dart';
import '../../widgets/custom_button.dart';
import '../../widgets/custom_text_field.dart';
import '../../widgets/error_card.dart';
<<<<<<< HEAD
import '../home/home_screen.dart';

/// Complete, responsive Registration Screen.
=======

>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
class RegisterScreen extends StatefulWidget {
  final AuthState authState;

  const RegisterScreen({
    super.key,
    required this.authState,
  });

  @override
  State<RegisterScreen> createState() => _RegisterScreenState();
}

class _RegisterScreenState extends State<RegisterScreen> {
  final _formKey = GlobalKey<FormState>();
  final _nameController = TextEditingController();
  final _emailController = TextEditingController();
  final _phoneController = TextEditingController();
  final _passwordController = TextEditingController();
  final _confirmPasswordController = TextEditingController();
  String _selectedRole = 'student';

  @override
  void dispose() {
    _nameController.dispose();
    _emailController.dispose();
    _phoneController.dispose();
    _passwordController.dispose();
    _confirmPasswordController.dispose();
    super.dispose();
  }

  Future<void> _handleRegister() async {
    widget.authState.clearError();
<<<<<<< HEAD
    if (!_formKey.currentState!.validate()) return;
=======
    if (!_formKey.currentState!.validate()) {
      return;
    }

    FocusScope.of(context).unfocus();
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd

    final request = RegisterRequest(
      name: _nameController.text.trim(),
      email: _emailController.text.trim(),
      phone: _phoneController.text.trim(),
      password: _passwordController.text,
      role: _selectedRole,
<<<<<<< HEAD
=======
      department: _selectedRole == 'faculty' ? 'Academic Faculty' : 'Undergraduate Studies',
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
    );

    final success = await widget.authState.register(request);

    if (success && mounted) {
<<<<<<< HEAD
      Navigator.of(context).pushAndRemoveUntil(
        MaterialPageRoute(
          builder: (_) => HomeScreen(authState: widget.authState),
        ),
=======
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(
          content: Text('Account created successfully! Welcome to UniSphere.'),
          backgroundColor: AppColors.success,
        ),
      );
      Navigator.of(context).pushNamedAndRemoveUntil(
        RouteConstants.home,
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
        (route) => false,
      );
    }
  }

  @override
  Widget build(BuildContext context) {
<<<<<<< HEAD
    final authState = widget.authState;
=======
    final isLoading = widget.authState.isLoading;
    final errorMessage = widget.authState.errorMessage;
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd

    return Scaffold(
      backgroundColor: AppColors.backgroundLight,
      appBar: AppBar(
        title: const Text('Create Account'),
        leading: IconButton(
<<<<<<< HEAD
          icon: const Icon(Icons.arrow_back_ios_new_rounded, size: 20),
=======
          icon: const Icon(Icons.arrow_back_rounded),
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
          onPressed: () => Navigator.of(context).pop(),
        ),
      ),
      body: SafeArea(
<<<<<<< HEAD
        child: AnimatedBuilder(
          animation: authState,
          builder: (context, _) {
            return SingleChildScrollView(
              padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 16),
              child: Form(
                key: _formKey,
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.stretch,
                  children: [
                    const Text(
                      'Join UniSphere',
                      style: TextStyle(
                        fontSize: 22,
                        fontWeight: FontWeight.w700,
                        color: AppColors.textPrimaryLight,
                      ),
                    ),
                    const SizedBox(height: 4),
                    const Text(
                      'Register for unified campus access and resources',
=======
        child: SingleChildScrollView(
          padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 16),
          child: Form(
            key: _formKey,
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.stretch,
              children: [
                const Text(
                  'Join UniSphere',
                  style: TextStyle(
                    fontSize: 24,
                    fontWeight: FontWeight.w800,
                    color: AppColors.textPrimaryLight,
                    letterSpacing: -0.5,
                  ),
                ),
                const SizedBox(height: 6),
                const Text(
                  'Fill in your academic details to get started',
                  style: TextStyle(
                    fontSize: 14,
                    color: AppColors.textSecondaryLight,
                  ),
                ),
                const SizedBox(height: 24),

                if (errorMessage != null) ...[
                  ErrorCard(
                    message: errorMessage,
                    onDismiss: () => widget.authState.clearError(),
                  ),
                  const SizedBox(height: 16),
                ],

                // Role Selector Segment
                Container(
                  padding: const EdgeInsets.all(4),
                  decoration: BoxDecoration(
                    color: const Color(0xFFE2E8F0),
                    borderRadius: BorderRadius.circular(12),
                  ),
                  child: Row(
                    children: [
                      Expanded(
                        child: GestureDetector(
                          onTap: () => setState(() => _selectedRole = 'student'),
                          child: Container(
                            padding: const EdgeInsets.symmetric(vertical: 10),
                            decoration: BoxDecoration(
                              color: _selectedRole == 'student' ? Colors.white : Colors.transparent,
                              borderRadius: BorderRadius.circular(10),
                              boxShadow: _selectedRole == 'student'
                                  ? [
                                      BoxShadow(
                                        color: Colors.black.withOpacity(0.05),
                                        blurRadius: 4,
                                        offset: const Offset(0, 2),
                                      ),
                                    ]
                                  : null,
                            ),
                            child: Center(
                              child: Text(
                                'Student',
                                style: TextStyle(
                                  fontSize: 14,
                                  fontWeight: FontWeight.w600,
                                  color: _selectedRole == 'student'
                                      ? AppColors.primary
                                      : AppColors.textSecondaryLight,
                                ),
                              ),
                            ),
                          ),
                        ),
                      ),
                      Expanded(
                        child: GestureDetector(
                          onTap: () => setState(() => _selectedRole = 'faculty'),
                          child: Container(
                            padding: const EdgeInsets.symmetric(vertical: 10),
                            decoration: BoxDecoration(
                              color: _selectedRole == 'faculty' ? Colors.white : Colors.transparent,
                              borderRadius: BorderRadius.circular(10),
                              boxShadow: _selectedRole == 'faculty'
                                  ? [
                                      BoxShadow(
                                        color: Colors.black.withOpacity(0.05),
                                        blurRadius: 4,
                                        offset: const Offset(0, 2),
                                      ),
                                    ]
                                  : null,
                            ),
                            child: Center(
                              child: Text(
                                'Faculty',
                                style: TextStyle(
                                  fontSize: 14,
                                  fontWeight: FontWeight.w600,
                                  color: _selectedRole == 'faculty'
                                      ? AppColors.primary
                                      : AppColors.textSecondaryLight,
                                ),
                              ),
                            ),
                          ),
                        ),
                      ),
                    ],
                  ),
                ),
                const SizedBox(height: 20),

                // Name Field
                CustomTextField(
                  controller: _nameController,
                  label: 'Full Name',
                  hint: 'e.g. Alex Mercer',
                  prefixIcon: Icons.person_outline_rounded,
                  validator: Validators.validateName,
                ),
                const SizedBox(height: 16),

                // Email Field
                CustomTextField(
                  controller: _emailController,
                  label: 'Email Address',
                  hint: 'alex@university.edu',
                  prefixIcon: Icons.alternate_email_rounded,
                  keyboardType: TextInputType.emailAddress,
                  validator: Validators.validateEmail,
                ),
                const SizedBox(height: 16),

                // Phone Field
                CustomTextField(
                  controller: _phoneController,
                  label: 'Phone Number',
                  hint: '+1 (555) 234-5678',
                  prefixIcon: Icons.phone_outlined,
                  keyboardType: TextInputType.phone,
                  validator: Validators.validatePhone,
                ),
                const SizedBox(height: 16),

                // Password Field
                CustomTextField(
                  controller: _passwordController,
                  label: 'Password',
                  hint: 'At least 6 characters',
                  prefixIcon: Icons.lock_outline_rounded,
                  isPassword: true,
                  validator: Validators.validatePassword,
                ),
                const SizedBox(height: 16),

                // Confirm Password Field
                CustomTextField(
                  controller: _confirmPasswordController,
                  label: 'Confirm Password',
                  hint: 'Re-enter your password',
                  prefixIcon: Icons.lock_reset_rounded,
                  isPassword: true,
                  textInputAction: TextInputAction.done,
                  validator: (val) => Validators.validateConfirmPassword(
                    val,
                    _passwordController.text,
                  ),
                  onSubmitted: (_) => _handleRegister(),
                ),
                const SizedBox(height: 28),

                // Submit Button
                CustomButton(
                  text: 'Register Account',
                  onPressed: _handleRegister,
                  isLoading: isLoading,
                  icon: Icons.person_add_alt_1_rounded,
                ),
                const SizedBox(height: 20),

                // Back to Login link
                Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    const Text(
                      'Already registered? ',
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
                      style: TextStyle(
                        fontSize: 14,
                        color: AppColors.textSecondaryLight,
                      ),
                    ),
<<<<<<< HEAD
                    const SizedBox(height: 20),

                    // Error Notification Banner
                    if (authState.errorMessage != null)
                      ErrorCard(
                        message: authState.errorMessage!,
                        onDismiss: authState.clearError,
                      ),

                    // Role Picker Segment
                    Container(
                      decoration: BoxDecoration(
                        color: AppColors.surfaceElevatedLight,
                        borderRadius: BorderRadius.circular(12),
                        border: Border.all(color: AppColors.borderLight),
                      ),
                      padding: const EdgeInsets.all(4),
                      child: Row(
                        children: [
                          Expanded(
                            child: ChoiceChip(
                              label: const Center(child: Text('Student')),
                              selected: _selectedRole == 'student',
                              onSelected: (selected) {
                                if (selected) setState(() => _selectedRole = 'student');
                              },
                              selectedColor: AppColors.primary,
                              labelStyle: TextStyle(
                                color: _selectedRole == 'student'
                                    ? Colors.white
                                    : AppColors.textSecondaryLight,
                                fontWeight: FontWeight.w600,
                              ),
                              showCheckmark: false,
                            ),
                          ),
                          const SizedBox(width: 8),
                          Expanded(
                            child: ChoiceChip(
                              label: const Center(child: Text('Faculty / Staff')),
                              selected: _selectedRole == 'faculty',
                              onSelected: (selected) {
                                if (selected) setState(() => _selectedRole = 'faculty');
                              },
                              selectedColor: AppColors.primary,
                              labelStyle: TextStyle(
                                color: _selectedRole == 'faculty'
                                    ? Colors.white
                                    : AppColors.textSecondaryLight,
                                fontWeight: FontWeight.w600,
                              ),
                              showCheckmark: false,
                            ),
                          ),
                        ],
                      ),
                    ),
                    const SizedBox(height: 16),

                    // Full Name
                    CustomTextField(
                      controller: _nameController,
                      label: 'Full Name',
                      hint: 'e.g. Jordan Miller',
                      prefixIcon: Icons.person_outline_rounded,
                      validator: Validators.validateName,
                    ),
                    const SizedBox(height: 16),

                    // University Email
                    CustomTextField(
                      controller: _emailController,
                      label: 'University Email',
                      hint: 'jordan@university.edu',
                      prefixIcon: Icons.email_outlined,
                      keyboardType: TextInputType.emailAddress,
                      validator: Validators.validateEmail,
                    ),
                    const SizedBox(height: 16),

                    // Phone Number
                    CustomTextField(
                      controller: _phoneController,
                      label: 'Phone Number',
                      hint: '+1 (555) 000-0000',
                      prefixIcon: Icons.phone_outlined,
                      keyboardType: TextInputType.phone,
                      validator: Validators.validatePhone,
                    ),
                    const SizedBox(height: 16),

                    // Password
                    CustomTextField(
                      controller: _passwordController,
                      label: 'Password',
                      hint: 'Minimum 6 characters',
                      prefixIcon: Icons.lock_outline_rounded,
                      isPassword: true,
                      validator: Validators.validatePassword,
                    ),
                    const SizedBox(height: 16),

                    // Confirm Password
                    CustomTextField(
                      controller: _confirmPasswordController,
                      label: 'Confirm Password',
                      hint: 'Re-enter your password',
                      prefixIcon: Icons.lock_reset_rounded,
                      isPassword: true,
                      validator: (value) => Validators.validateConfirmPassword(
                        value,
                        _passwordController.text,
                      ),
                      textInputAction: TextInputAction.done,
                      onFieldSubmitted: (_) => _handleRegister(),
                    ),
                    const SizedBox(height: 24),

                    // Submit Registration Button
                    CustomButton(
                      text: 'Create Account',
                      onPressed: _handleRegister,
                      isLoading: authState.isLoading,
                      icon: Icons.person_add_alt_1_rounded,
                    ),
                    const SizedBox(height: 20),

                    // Return to Login
                    Row(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                        const Text(
                          'Already have an account? ',
                          style: TextStyle(
                            color: AppColors.textSecondaryLight,
                            fontSize: 14,
                          ),
                        ),
                        GestureDetector(
                          onTap: () {
                            authState.clearError();
                            Navigator.of(context).pop();
                          },
                          child: const Text(
                            'Sign In',
                            style: TextStyle(
                              color: AppColors.primary,
                              fontWeight: FontWeight.w700,
                              fontSize: 14,
                            ),
                          ),
                        ),
                      ],
                    ),
                    const SizedBox(height: 16),
                  ],
                ),
              ),
            );
          },
=======
                    GestureDetector(
                      onTap: () {
                        widget.authState.clearError();
                        Navigator.of(context).pop();
                      },
                      child: const Text(
                        'Log in',
                        style: TextStyle(
                          fontSize: 14,
                          fontWeight: FontWeight.w700,
                          color: AppColors.primary,
                        ),
                      ),
                    ),
                  ],
                ),
                const SizedBox(height: 16),
              ],
            ),
          ),
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
        ),
      ),
    );
  }
}
