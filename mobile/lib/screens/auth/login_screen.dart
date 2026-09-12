import 'package:flutter/material.dart';
import '../../core/constants/app_constants.dart';
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
=======

=======
>>>>>>> origin/web
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
import '../home/home_screen.dart';
import 'register_screen.dart';

/// Complete, responsive Login Screen.
<<<<<<< HEAD
<<<<<<< HEAD
=======

>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
class LoginScreen extends StatefulWidget {
  final AuthState authState;

  const LoginScreen({
    super.key,
    required this.authState,
  });

  @override
  State<LoginScreen> createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> {
  final _formKey = GlobalKey<FormState>();
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
  final _emailController = TextEditingController();
  final _passwordController = TextEditingController();
=======
=======
>>>>>>> origin/web
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
  late final TextEditingController _emailController;
  late final TextEditingController _passwordController;
  bool _rememberMe = false;

  @override
  void initState() {
    super.initState();
    _rememberMe = widget.authState.rememberMe;
    _emailController = TextEditingController(
      text: widget.authState.savedEmail ?? '',
    );
    _passwordController = TextEditingController();
  }
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
=======
  final _emailController = TextEditingController();
  final _passwordController = TextEditingController();
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
=======
  final _emailController = TextEditingController();
  final _passwordController = TextEditingController();
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689

  @override
  void dispose() {
    _emailController.dispose();
    _passwordController.dispose();
    super.dispose();
  }

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
  void _fillQuickDemo(String role) {
    setState(() {
      if (role == 'student') {
        _emailController.text = 'student@university.edu';
        _passwordController.text = 'Password123!';
      } else {
        _emailController.text = 'faculty@university.edu';
        _passwordController.text = 'Password123!';
      }
      _rememberMe = true;
    });
    widget.authState.clearError();
  }

=======
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
  Future<void> _handleLogin() async {
    widget.authState.clearError();
    if (!_formKey.currentState!.validate()) return;

<<<<<<< HEAD
    FocusScope.of(context).unfocus();

    final success = await widget.authState.login(
      email: _emailController.text.trim(),
      password: _passwordController.text,
      rememberMe: _rememberMe,
    );

    if (success && mounted) {
      // Clear navigation stack and go to Home
      Navigator.of(context).pushNamedAndRemoveUntil(
        RouteConstants.home,
        (route) => false,
=======
    final success = await widget.authState.login(
      _emailController.text.trim(),
      _passwordController.text,
    );

    if (success && mounted) {
      Navigator.of(context).pushReplacement(
        MaterialPageRoute(
          builder: (_) => HomeScreen(authState: widget.authState),
        ),
<<<<<<< HEAD
=======
=======
>>>>>>> origin/web
  void _fillDemoCredentials() {
    setState(() {
      _emailController.text = AppConstants.demoEmail;
      _passwordController.text = AppConstants.demoPassword;
      _rememberMe = true;
    });
    widget.authState.clearError();
  }

  Future<void> _handleLogin() async {
    widget.authState.clearError();
    if (!_formKey.currentState!.validate()) {
      return;
    }

    // Dismiss keyboard
    FocusScope.of(context).unfocus();

    final success = await widget.authState.login(
      email: _emailController.text,
      password: _passwordController.text,
      rememberMe: _rememberMe,
    );

    if (success && mounted) {
      // Clear navigation stack and go to Home
      Navigator.of(context).pushNamedAndRemoveUntil(
        RouteConstants.home,
        (route) => false,
<<<<<<< HEAD
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
=======
  Future<void> _handleLogin() async {
    widget.authState.clearError();
    if (!_formKey.currentState!.validate()) return;

    final success = await widget.authState.login(
      _emailController.text.trim(),
      _passwordController.text,
    );

    if (success && mounted) {
      Navigator.of(context).pushReplacement(
        MaterialPageRoute(
          builder: (_) => HomeScreen(authState: widget.authState),
        ),
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
      );
    }
  }

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
  @override
  Widget build(BuildContext context) {
    final isLoading = widget.authState.isLoading;
    final errorMessage = widget.authState.errorMessage;
=======
>>>>>>> origin/web
=======
  @override
  Widget build(BuildContext context) {
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
  void _fillQuickDemo(String role) {
    setState(() {
      if (role == 'student') {
        _emailController.text = 'alex.johnson@university.edu';
        _passwordController.text = 'Password123!';
      } else {
        _emailController.text = 'sarah.mitchell.faculty@university.edu';
        _passwordController.text = 'ProfPass2026!';
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    final authState = widget.authState;
<<<<<<< HEAD
<<<<<<< HEAD
=======
  @override
  Widget build(BuildContext context) {
    final isLoading = widget.authState.isLoading;
    final errorMessage = widget.authState.errorMessage;
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689

>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9
    return Scaffold(
      backgroundColor: AppColors.backgroundLight,
      body: SafeArea(
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
        child: AnimatedBuilder(
          animation: widget.authState,
          builder: (context, _) {
            final authState = widget.authState;
            final errorMessage = authState.errorMessage;

            return Center(
              child: SingleChildScrollView(
                padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 20),
                child: Form(
                  key: _formKey,
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.stretch,
                    children: [
                      // Header Icon & Title
                      Center(
                        child: Image.asset(
                          'assets/logo.png',
                          width: 78,
                          height: 78,
                          fit: BoxFit.contain,
                          errorBuilder: (context, error, stackTrace) => Container(
                            width: 72,
                            height: 72,
                            decoration: BoxDecoration(
                              gradient: const LinearGradient(
                                colors: [AppColors.primary, AppColors.secondary],
                                begin: Alignment.topLeft,
                                end: Alignment.bottomRight,
                              ),
                              borderRadius: BorderRadius.circular(20),
                            ),
                            child: const Icon(Icons.school_rounded, size: 38, color: Colors.white),
                          ),
                        ),
                      ),
                      const SizedBox(height: 20),
                      const Text(
                        AppConstants.appName,
                        textAlign: TextAlign.center,
                        style: TextStyle(
                          fontSize: 26,
                          fontWeight: FontWeight.w800,
                          color: AppColors.textPrimaryLight,
                          letterSpacing: -0.5,
                        ),
                      ),
                      const SizedBox(height: 6),
                      const Text(
                        'Sign in to access your student or faculty portal',
                        textAlign: TextAlign.center,
<<<<<<< HEAD
=======
=======
>>>>>>> origin/web
        child: Center(
          child: SingleChildScrollView(
            padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 20),
            child: Form(
              key: _formKey,
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                crossAxisAlignment: CrossAxisAlignment.stretch,
                children: [
                  // App Icon and Header
                  Center(
                    child: Container(
                      padding: const EdgeInsets.all(16),
                      decoration: BoxDecoration(
                        color: AppColors.primaryLight,
                        borderRadius: BorderRadius.circular(20),
                      ),
                      child: const Icon(
                        Icons.school_rounded,
                        size: 44,
                        color: AppColors.primary,
                      ),
                    ),
                  ),
                  const SizedBox(height: 20),
                  const Text(
                    'Welcome Back',
                    style: TextStyle(
                      fontSize: 26,
                      fontWeight: FontWeight.w800,
                      color: AppColors.textPrimaryLight,
                      letterSpacing: -0.5,
                    ),
                    textAlign: TextAlign.center,
                  ),
                  const SizedBox(height: 6),
                  const Text(
                    'Sign in to access your university dashboard',
                    style: TextStyle(
                      fontSize: 14,
                      color: AppColors.textSecondaryLight,
                    ),
                    textAlign: TextAlign.center,
                  ),
                  const SizedBox(height: 28),

                  // Quick Demo Autofill helper card
                  Container(
                    padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 10),
                    decoration: BoxDecoration(
                      color: const Color(0xFFF1F5F9),
                      borderRadius: BorderRadius.circular(12),
                      border: Border.all(color: const Color(0xFFCBD5E1)),
                    ),
                    child: Row(
                      children: [
                        const Icon(
                          Icons.touch_app_rounded,
                          size: 20,
                          color: AppColors.primary,
                        ),
                        const SizedBox(width: 10),
                        const Expanded(
                          child: Text(
                            'Quick Demo: Fill with sample student credentials',
                            style: TextStyle(
                              fontSize: 12,
                              fontWeight: FontWeight.w500,
                              color: Color(0xFF334155),
                            ),
                          ),
                        ),
                        TextButton(
                          onPressed: _fillDemoCredentials,
                          style: TextButton.styleFrom(
                            padding: const EdgeInsets.symmetric(horizontal: 8),
                            minimumSize: const Size(50, 30),
                          ),
                          child: const Text(
                            'Fill',
                            style: TextStyle(
                              fontSize: 12,
                              fontWeight: FontWeight.w700,
                              color: AppColors.primary,
                            ),
                          ),
                        ),
                      ],
                    ),
                  ),
                  const SizedBox(height: 18),

                  // Error Message
                  if (errorMessage != null) ...[
                    ErrorCard(
                      message: errorMessage,
                      onDismiss: () => widget.authState.clearError(),
                    ),
                    const SizedBox(height: 16),
                  ],

                  // Email Field
                  CustomTextField(
                    controller: _emailController,
                    label: 'Email or Username',
                    hint: 'student@university.edu',
                    prefixIcon: Icons.alternate_email_rounded,
                    keyboardType: TextInputType.emailAddress,
                    validator: Validators.validateEmail,
                  ),
                  const SizedBox(height: 18),

                  // Password Field
                  CustomTextField(
                    controller: _passwordController,
                    label: 'Password',
                    hint: 'Enter your password',
                    prefixIcon: Icons.lock_outline_rounded,
                    isPassword: true,
                    textInputAction: TextInputAction.done,
                    validator: Validators.validatePassword,
                    onSubmitted: (_) => _handleLogin(),
                  ),
                  const SizedBox(height: 12),

                  // Remember Me & Forgot Password row
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      Row(
                        children: [
                          SizedBox(
                            height: 24,
                            width: 24,
                            child: Checkbox(
                              value: _rememberMe,
                              onChanged: (value) {
                                setState(() {
                                  _rememberMe = value ?? false;
                                });
                              },
                              shape: RoundedRectangleBorder(
                                borderRadius: BorderRadius.circular(4),
                              ),
                              activeColor: AppColors.primary,
                            ),
                          ),
                          const SizedBox(width: 8),
                          const Text(
                            'Remember me',
                            style: TextStyle(
                              fontSize: 13,
                              color: AppColors.textSecondaryLight,
                              fontWeight: FontWeight.w500,
                            ),
                          ),
                        ],
                      ),
                      TextButton(
                        onPressed: () {
                          ScaffoldMessenger.of(context).showSnackBar(
                            const SnackBar(
                              content: Text('Password reset instructions have been sent to your registered email.'),
                              duration: Duration(seconds: 3),
                            ),
                          );
                        },
                        style: TextButton.styleFrom(
                          padding: EdgeInsets.zero,
                          minimumSize: const Size(50, 30),
                        ),
                        child: const Text(
                          'Forgot password?',
                          style: TextStyle(
                            fontSize: 13,
                            fontWeight: FontWeight.w600,
                            color: AppColors.primary,
                          ),
                        ),
                      ),
                    ],
                  ),
                  const SizedBox(height: 24),

                  // Login Button
                  CustomButton(
                    text: 'Sign In',
                    onPressed: _handleLogin,
                    isLoading: isLoading,
                    icon: Icons.login_rounded,
                  ),
                  const SizedBox(height: 24),

                  // Divider
                  const Row(
                    children: [
                      Expanded(child: Divider()),
                      Padding(
                        padding: EdgeInsets.symmetric(horizontal: 16),
                        child: Text(
                          'OR',
                          style: TextStyle(
                            fontSize: 12,
                            fontWeight: FontWeight.w600,
                            color: AppColors.textMutedLight,
                          ),
                        ),
                      ),
                      Expanded(child: Divider()),
                    ],
                  ),
                  const SizedBox(height: 24),

                  // Register Navigation Option
                  Row(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      const Text(
                        "Don't have an account? ",
<<<<<<< HEAD
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
=======
        child: AnimatedBuilder(
          animation: authState,
          builder: (context, _) {
            return Center(
              child: SingleChildScrollView(
                padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 20),
                child: Form(
                  key: _formKey,
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.stretch,
                    children: [
                      // Header Icon & Title
                      Center(
                        child: Container(
                          width: 72,
                          height: 72,
                          decoration: BoxDecoration(
                            gradient: const LinearGradient(
                              colors: [AppColors.primary, AppColors.secondary],
                              begin: Alignment.topLeft,
                              end: Alignment.bottomRight,
                            ),
                            borderRadius: BorderRadius.circular(20),
                            boxShadow: [
                              BoxShadow(
                                color: AppColors.primary.withOpacity(0.25),
                                blurRadius: 20,
                                offset: const Offset(0, 8),
                              ),
                            ],
                          ),
                          child: const Icon(
                            Icons.school_rounded,
                            size: 38,
                            color: Colors.white,
                          ),
                        ),
                      ),
                      const SizedBox(height: 20),
                      const Text(
                        AppConstants.appName,
                        textAlign: TextAlign.center,
                        style: TextStyle(
                          fontSize: 26,
                          fontWeight: FontWeight.w800,
                          color: AppColors.textPrimaryLight,
                          letterSpacing: -0.5,
                        ),
                      ),
                      const SizedBox(height: 6),
                      const Text(
                        'Sign in to access your student or faculty portal',
                        textAlign: TextAlign.center,
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
                        style: TextStyle(
                          fontSize: 14,
                          color: AppColors.textSecondaryLight,
                        ),
                      ),
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
                      GestureDetector(
                        onTap: () {
                          widget.authState.clearError();
                          Navigator.of(context).pushNamed(RouteConstants.register);
                        },
                        child: const Text(
                          'Create an Account',
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
            ),
          ),
=======
>>>>>>> origin/web
=======
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
                      const SizedBox(height: 28),

                      // Error Alert Banner
                      if (authState.errorMessage != null)
                        ErrorCard(
                          message: authState.errorMessage!,
                          onDismiss: authState.clearError,
                        ),

                      // Email Field
                      CustomTextField(
                        controller: _emailController,
                        label: 'University Email',
                        hint: 'name@university.edu',
                        prefixIcon: Icons.email_outlined,
                        keyboardType: TextInputType.emailAddress,
                        validator: Validators.validateEmail,
                        textInputAction: TextInputAction.next,
                      ),
                      const SizedBox(height: 16),

                      // Password Field
                      CustomTextField(
                        controller: _passwordController,
                        label: 'Password',
                        hint: '••••••••',
                        prefixIcon: Icons.lock_outline_rounded,
                        isPassword: true,
                        validator: Validators.validatePassword,
                        textInputAction: TextInputAction.done,
                        onFieldSubmitted: (_) => _handleLogin(),
                      ),
                      const SizedBox(height: 24),

                      // Login Action Button
                      CustomButton(
                        text: 'Sign In',
                        onPressed: _handleLogin,
                        isLoading: authState.isLoading,
                        icon: Icons.login_rounded,
                      ),
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9
                      const SizedBox(height: 20),

                      // Quick Demo Autofill Helper Card
                      Container(
                        padding: const EdgeInsets.all(12),
                        decoration: BoxDecoration(
                          color: AppColors.surfaceElevatedLight,
                          borderRadius: BorderRadius.circular(12),
                          border: Border.all(color: AppColors.borderLight),
                        ),
                        child: Column(
                          children: [
                            const Text(
                              'Quick Test Autofill',
                              style: TextStyle(
                                fontSize: 12,
                                fontWeight: FontWeight.w600,
                                color: AppColors.textSecondaryLight,
                              ),
                            ),
                            const SizedBox(height: 8),
                            Row(
                              children: [
                                Expanded(
                                  child: OutlinedButton(
                                    onPressed: () => _fillQuickDemo('student'),
                                    style: OutlinedButton.styleFrom(
                                      padding: const EdgeInsets.symmetric(vertical: 8),
                                      visualDensity: VisualDensity.compact,
                                    ),
                                    child: const Text('Student Demo', style: TextStyle(fontSize: 12)),
                                  ),
                                ),
                                const SizedBox(width: 8),
                                Expanded(
                                  child: OutlinedButton(
                                    onPressed: () => _fillQuickDemo('faculty'),
                                    style: OutlinedButton.styleFrom(
                                      padding: const EdgeInsets.symmetric(vertical: 8),
                                      visualDensity: VisualDensity.compact,
                                    ),
                                    child: const Text('Faculty Demo', style: TextStyle(fontSize: 12)),
                                  ),
                                ),
                              ],
                            ),
                          ],
                        ),
                      ),
                      const SizedBox(height: 18),

                      // Error Message
                      if (errorMessage != null) ...[
                        ErrorCard(
                          message: errorMessage,
                          onDismiss: () => authState.clearError(),
                        ),
                        const SizedBox(height: 16),
                      ],

                      // Email Field
                      CustomTextField(
                        controller: _emailController,
                        label: 'University Email',
                        hint: 'name@university.edu',
                        prefixIcon: Icons.alternate_email_rounded,
                        keyboardType: TextInputType.emailAddress,
                        validator: Validators.validateEmail,
                        textInputAction: TextInputAction.next,
                      ),
                      const SizedBox(height: 16),

                      // Password Field
                      CustomTextField(
                        controller: _passwordController,
                        label: 'Password',
                        hint: '••••••••',
                        prefixIcon: Icons.lock_outline_rounded,
                        isPassword: true,
                        textInputAction: TextInputAction.done,
                        validator: Validators.validatePassword,
                        onSubmitted: (_) => _handleLogin(),
                      ),
                      const SizedBox(height: 12),

                      // Remember Me & Forgot Password row
                      Row(
                        mainAxisAlignment: MainAxisAlignment.spaceBetween,
                        children: [
                          Row(
                            children: [
                              SizedBox(
                                height: 24,
                                width: 24,
                                child: Checkbox(
                                  value: _rememberMe,
                                  onChanged: (value) {
                                    setState(() {
                                      _rememberMe = value ?? false;
                                    });
                                  },
                                  shape: RoundedRectangleBorder(
                                    borderRadius: BorderRadius.circular(4),
                                  ),
                                  activeColor: AppColors.primary,
                                ),
                              ),
                              const SizedBox(width: 8),
                              const Text(
                                'Remember me',
                                style: TextStyle(
                                  fontSize: 13,
                                  color: AppColors.textSecondaryLight,
                                  fontWeight: FontWeight.w500,
                                ),
                              ),
                            ],
                          ),
                          TextButton(
                            onPressed: () {
                              ScaffoldMessenger.of(context).showSnackBar(
                                const SnackBar(
                                  content: Text('Password reset instructions have been sent to your registered email.'),
                                  duration: Duration(seconds: 3),
                                ),
                              );
                            },
                            style: TextButton.styleFrom(
                              padding: EdgeInsets.zero,
                              minimumSize: const Size(50, 30),
                            ),
                            child: const Text(
                              'Forgot password?',
                              style: TextStyle(
                                fontSize: 13,
                                fontWeight: FontWeight.w600,
                                color: AppColors.primary,
                              ),
                            ),
                          ),
                        ],
                      ),
                      const SizedBox(height: 24),

                      // Login Button
                      CustomButton(
                        text: 'Sign In',
                        onPressed: _handleLogin,
                        isLoading: authState.isLoading,
                        icon: Icons.login_rounded,
                      ),
                      const SizedBox(height: 24),

                      // Register Navigation Option
                      Row(
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: [
                          const Text(
                            "Don't have an account? ",
                            style: TextStyle(
                              fontSize: 14,
                              color: AppColors.textSecondaryLight,
                            ),
                          ),
                          GestureDetector(
                            onTap: () {
                              authState.clearError();
                              Navigator.of(context).pushNamed(RouteConstants.register);
                            },
                            child: const Text(
                              'Create an Account',
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
                ),
              ),
            );
          },
<<<<<<< HEAD
<<<<<<< HEAD
=======
                      GestureDetector(
                        onTap: () {
                          widget.authState.clearError();
                          Navigator.of(context).pushNamed(RouteConstants.register);
                        },
                        child: const Text(
                          'Create an Account',
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
            ),
          ),
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