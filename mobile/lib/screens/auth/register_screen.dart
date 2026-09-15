import 'package:flutter/material.dart';
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
import '../../core/constants/route_constants.dart';
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
import '../../core/constants/route_constants.dart';
=======
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
import '../../core/constants/route_constants.dart';
=======
import '../../core/constants/app_constants.dart';
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
import '../../core/theme/app_colors.dart';
import '../../core/utils/validators.dart';
import '../../state/auth_state.dart';
import '../../widgets/custom_button.dart';
import '../../widgets/custom_text_field.dart';
import '../../widgets/error_card.dart';
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
import '../home/home_screen.dart';
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689

<<<<<<< HEAD
/// Complete, responsive Registration Screen.
=======
<<<<<<< HEAD

>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======

=======
import '../home/home_screen.dart';

/// Complete, responsive Registration Screen.
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
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
  final _fullNameController = TextEditingController();
  final _emailController = TextEditingController();
  final _passwordController = TextEditingController();
  final _confirmPasswordController = TextEditingController();

  String _selectedRole = 'student';
  bool _isLoading = false;
  String? _localError;

  @override
  void dispose() {
    _fullNameController.dispose();
    _emailController.dispose();
    _passwordController.dispose();
    _confirmPasswordController.dispose();
    super.dispose();
  }

  Future<void> _handleRegister() async {
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    if (!_formKey.currentState!.validate()) return;
=======
=======
>>>>>>> origin/web
=======
    widget.authState.clearError();
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
    if (!_formKey.currentState!.validate()) {
      return;
    }

    FocusScope.of(context).unfocus();
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
=======
    if (!_formKey.currentState!.validate()) return;
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
=======
    setState(() {
      _localError = null;
    });
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689

    if (!_formKey.currentState!.validate()) return;

    if (_passwordController.text != _confirmPasswordController.text) {
      setState(() {
        _localError = 'Passwords do not match';
      });
      return;
    }

    setState(() {
      _isLoading = true;
    });
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9

    final success = await widget.authState.register(
      fullName: _fullNameController.text.trim(),
      email: _emailController.text.trim(),
      password: _passwordController.text,
      role: _selectedRole,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
      department: _selectedRole == 'faculty' ? 'Academic Faculty' : 'Undergraduate Studies',
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
      department: _selectedRole == 'faculty' ? 'Academic Faculty' : 'Undergraduate Studies',
=======
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
      department: _selectedRole == 'faculty'
          ? 'Academic Faculty'
          : 'Undergraduate Studies',
=======
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
    );

    setState(() {
      _isLoading = false;
    });

    if (success && mounted) {
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
      Navigator.of(context).pushAndRemoveUntil(
        MaterialPageRoute(
          builder: (_) => HomeScreen(authState: widget.authState),
        ),
=======
=======
>>>>>>> origin/web
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(
          content: Text('Account registered successfully!'),
          backgroundColor: AppColors.success,
        ),
      );
<<<<<<< HEAD
      Navigator.of(context).pushNamedAndRemoveUntil(
        RouteConstants.home,
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
=======
      Navigator.of(context).pushAndRemoveUntil(
        MaterialPageRoute(
          builder: (_) => HomeScreen(authState: widget.authState),
        ),
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
        (route) => false,
      );
=======
      Navigator.of(context).pop();
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9
    }
  }

  @override
  Widget build(BuildContext context) {
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    final authState = widget.authState;
=======
    final isLoading = widget.authState.isLoading;
    final errorMessage = widget.authState.errorMessage;
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
    final isLoading = widget.authState.isLoading;
    final errorMessage = widget.authState.errorMessage;
=======
    final authState = widget.authState;
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
    final isLoading = widget.authState.isLoading;
    final errorMessage = widget.authState.errorMessage;
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689

    return Scaffold(
      backgroundColor: AppColors.backgroundLight,
      appBar: AppBar(
        title: const Text('Create Account'),
        leading: IconButton(
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
          icon: const Icon(Icons.arrow_back_ios_new_rounded, size: 20),
=======
          icon: const Icon(Icons.arrow_back_rounded),
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
          icon: const Icon(Icons.arrow_back_rounded),
=======
          icon: const Icon(Icons.arrow_back_ios_new_rounded, size: 20),
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
          icon: const Icon(Icons.arrow_back_rounded),
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
          onPressed: () => Navigator.of(context).pop(),
        ),
      ),
      body: SafeArea(
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
        child: Center(
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
                      fontSize: 22,
                      fontWeight: FontWeight.w700,
                      color: AppColors.textPrimaryLight,
                    ),
                  ),
                  const SizedBox(height: 4),
                  const Text(
                    'Set up your student or faculty academic credentials',
                    style: TextStyle(
                      fontSize: 13,
                      color: AppColors.textSecondaryLight,
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
                    ),
=======
<<<<<<< HEAD
=======
>>>>>>> origin/web
=======
    return Scaffold(
      backgroundColor: AppColors.backgroundLight,
      appBar: AppBar(
        title: const Text('Create UniSphere Account'),
        backgroundColor: Colors.transparent,
        elevation: 0,
      ),
      body: SafeArea(
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
        child: SingleChildScrollView(
          padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 16),
          child: Form(
            key: _formKey,
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.stretch,
              children: [
                const Text(
                  'Join UniSphere AI Platform',
                  style: TextStyle(
                    fontSize: 22,
                    fontWeight: FontWeight.bold,
                    color: AppColors.textPrimaryLight,
                  ),
                ),
                const SizedBox(height: 6),
                const Text(
                  'Fill in your details to create your campus account.',
                  style: TextStyle(
                    fontSize: 14,
                    color: AppColors.textSecondaryLight,
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9
                  ),
                  const SizedBox(height: 20),

<<<<<<< HEAD
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

                  // Error Message
                  if (errorMessage != null) ...[
                    ErrorCard(
                      message: errorMessage,
                      onDismiss: () => widget.authState.clearError(),
                    ),
                    const SizedBox(height: 16),
                  ],

                  // Full Name
                  CustomTextField(
                    controller: _nameController,
                    label: 'Full Name',
                    hint: 'e.g. Alex Mercer',
                    prefixIcon: Icons.person_outline_rounded,
                    validator: Validators.validateName,
                  ),
                  const SizedBox(height: 16),

                  // University Email
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
                        style: TextStyle(
                          fontSize: 14,
                          color: AppColors.textSecondaryLight,
                        ),
                      ),
                      GestureDetector(
                        onTap: () {
                          widget.authState.clearError();
                          Navigator.of(context).pop();
                        },
                        child: const Text(
                          'Sign In',
                          style: TextStyle(
                            fontSize: 14,
                            fontWeight: FontWeight.w700,
                            color: AppColors.primary,
                          ),
                        ),
                      ),
                    ],
                  ),
                ],
              ),
=======
                if (_localError != null || widget.authState.errorMessage != null)
                  ErrorCard(
                    message: _localError ?? widget.authState.errorMessage!,
                    onDismiss: () {
                      setState(() {
                        _localError = null;
                      });
                      widget.authState.clearError();
                    },
                  ),

                CustomTextField(
                  controller: _fullNameController,
                  label: 'Full Name',
                  hint: 'Alex Morgan',
                  prefixIcon: Icons.person_outline_rounded,
                  validator: (val) => val == null || val.isEmpty ? 'Enter full name' : null,
                  textInputAction: TextInputAction.next,
                ),
                const SizedBox(height: 16),

                CustomTextField(
                  controller: _emailController,
                  label: 'University Email',
                  hint: 'alex@unisphere.edu',
                  prefixIcon: Icons.email_outlined,
                  keyboardType: TextInputType.emailAddress,
                  validator: Validators.validateEmail,
                  textInputAction: TextInputAction.next,
                ),
                const SizedBox(height: 16),

                DropdownButtonFormField<String>(
                  value: _selectedRole,
                  decoration: InputDecoration(
                    labelText: 'Account Role',
                    prefixIcon: const Icon(Icons.badge_outlined),
                    border: OutlineInputBorder(borderRadius: BorderRadius.circular(12)),
                  ),
                  items: const [
                    DropdownMenuItem(value: 'student', child: Text('Student')),
                    DropdownMenuItem(value: 'faculty', child: Text('Faculty')),
                    DropdownMenuItem(value: 'hod', child: Text('Department Head (HOD)')),
                  ],
                  onChanged: (val) {
                    if (val != null) setState(() => _selectedRole = val);
                  },
                ),
                const SizedBox(height: 16),

                CustomTextField(
                  controller: _passwordController,
                  label: 'Password',
                  hint: '••••••••',
                  prefixIcon: Icons.lock_outline_rounded,
                  isPassword: true,
                  validator: Validators.validatePassword,
                  textInputAction: TextInputAction.next,
                ),
                const SizedBox(height: 16),

                CustomTextField(
                  controller: _confirmPasswordController,
                  label: 'Confirm Password',
                  hint: '••••••••',
                  prefixIcon: Icons.lock_clock_outlined,
                  isPassword: true,
                  validator: (val) => val == null || val.isEmpty ? 'Confirm password' : null,
                  textInputAction: TextInputAction.done,
                ),
                const SizedBox(height: 24),

                CustomButton(
                  text: 'Complete Registration',
                  onPressed: _handleRegister,
                  isLoading: _isLoading,
                  icon: Icons.person_add_alt_1_rounded,
                ),
<<<<<<< HEAD
                const SizedBox(height: 20),

                // Back to Login link
                Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    const Text(
                      'Already registered? ',
<<<<<<< HEAD
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
=======
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
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
                      style: TextStyle(
                        fontSize: 14,
                        color: AppColors.textSecondaryLight,
                      ),
                    ),
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
>>>>>>> origin/web
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
<<<<<<< HEAD
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
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
              ],
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9
            ),
          ),
<<<<<<< HEAD
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
        ),
      ),
    );
  }
}