import 'dart:async';
import 'package:flutter/material.dart';
import '../../core/constants/app_constants.dart';
<<<<<<< HEAD
import '../../core/theme/app_colors.dart';
import '../../state/auth_state.dart';
import '../auth/login_screen.dart';
import '../home/home_screen.dart';

/// Professional Splash Screen with authentication session check.
=======
import '../../core/constants/route_constants.dart';
import '../../core/theme/app_colors.dart';
import '../../state/auth_state.dart';

>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
class SplashScreen extends StatefulWidget {
  final AuthState authState;

  const SplashScreen({
    super.key,
    required this.authState,
  });

  @override
  State<SplashScreen> createState() => _SplashScreenState();
}

<<<<<<< HEAD
class _SplashScreenState extends State<SplashScreen>
    with SingleTickerProviderStateMixin {
  late AnimationController _animController;
  late Animation<double> _scaleAnimation;
  late Animation<double> _fadeAnimation;
=======
class _SplashScreenState extends State<SplashScreen> with SingleTickerProviderStateMixin {
  late AnimationController _animController;
  late Animation<double> _fadeAnimation;
  late Animation<double> _scaleAnimation;
  Timer? _timeoutTimer;
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd

  @override
  void initState() {
    super.initState();

    _animController = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 1200),
    );

<<<<<<< HEAD
=======
    _fadeAnimation = CurvedAnimation(
      parent: _animController,
      curve: Curves.easeIn,
    );

>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
    _scaleAnimation = Tween<double>(begin: 0.85, end: 1.0).animate(
      CurvedAnimation(parent: _animController, curve: Curves.easeOutBack),
    );

<<<<<<< HEAD
    _fadeAnimation = Tween<double>(begin: 0.0, end: 1.0).animate(
      CurvedAnimation(parent: _animController, curve: Curves.easeIn),
    );

    _animController.forward();
    _checkSessionAndNavigate();
  }

  Future<void> _checkSessionAndNavigate() async {
    // Artificial minimum delay for smooth visual transition
    await Future.delayed(const Duration(milliseconds: 1600));

    final isAuthenticated = await widget.authState.checkAuth();

    if (!mounted) return;

    if (isAuthenticated) {
      Navigator.of(context).pushReplacement(
        MaterialPageRoute(
          builder: (_) => HomeScreen(authState: widget.authState),
        ),
      );
    } else {
      Navigator.of(context).pushReplacement(
        MaterialPageRoute(
          builder: (_) => LoginScreen(authState: widget.authState),
        ),
      );
    }
  }

  @override
  void dispose() {
=======
    _animController.forward();

    // Start checking auth status
    _initializeApp();
  }

  Future<void> _initializeApp() async {
    // Ensure splash is visible for at least 1.2s for pleasant UX
    final minSplashWait = Future.delayed(const Duration(milliseconds: 1200));

    // Fallback safety timeout so user is never stuck
    _timeoutTimer = Timer(const Duration(seconds: 4), () {
      if (mounted) {
        _navigate(RouteConstants.login);
      }
    });

    try {
      await Future.wait([
        widget.authState.checkAuthStatus(),
        minSplashWait,
      ]);

      if (!mounted) return;
      _timeoutTimer?.cancel();

      if (widget.authState.isAuthenticated) {
        _navigate(RouteConstants.home);
      } else {
        _navigate(RouteConstants.login);
      }
    } catch (_) {
      if (mounted) {
        _timeoutTimer?.cancel();
        _navigate(RouteConstants.login);
      }
    }
  }

  void _navigate(String routeName) {
    Navigator.of(context).pushReplacementNamed(routeName);
  }

  @override
  void dispose() {
    _timeoutTimer?.cancel();
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
    _animController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: AppColors.backgroundDark,
<<<<<<< HEAD
      body: Center(
        child: FadeTransition(
          opacity: _fadeAnimation,
          child: ScaleTransition(
            scale: _scaleAnimation,
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                // University Emblem
                Container(
                  width: 100,
                  height: 100,
                  decoration: BoxDecoration(
                    gradient: const LinearGradient(
                      colors: [AppColors.primary, AppColors.secondary],
                      begin: Alignment.topLeft,
                      end: Alignment.bottomRight,
                    ),
                    borderRadius: BorderRadius.circular(28),
                    boxShadow: [
                      BoxShadow(
                        color: AppColors.secondary.withOpacity(0.35),
                        blurRadius: 28,
                        offset: const Offset(0, 10),
                      ),
                    ],
                  ),
                  child: const Icon(
                    Icons.school_rounded,
                    size: 54,
                    color: Colors.white,
                  ),
                ),
                const SizedBox(height: 28),

                // App Title
                const Text(
                  AppConstants.appName,
                  style: TextStyle(
                    fontSize: 30,
                    fontWeight: FontWeight.w800,
                    color: Colors.white,
                    letterSpacing: -0.5,
                  ),
                ),
                const SizedBox(height: 8),

                // Tagline
                const Text(
                  AppConstants.appTagline,
                  style: TextStyle(
                    fontSize: 14,
                    fontWeight: FontWeight.w400,
                    color: AppColors.textMutedDark,
                    letterSpacing: 0.2,
                  ),
                ),
                const SizedBox(height: 48),

                // Loading Indicator
                const SizedBox(
                  width: 28,
                  height: 28,
                  child: CircularProgressIndicator(
                    strokeWidth: 2.8,
                    valueColor: AlwaysStoppedAnimation<Color>(AppColors.secondaryLight),
                  ),
                ),
              ],
            ),
          ),
        ),
=======
      body: Stack(
        children: [
          // Background ambient gradient glow
          Positioned(
            top: -100,
            right: -100,
            child: Container(
              width: 300,
              height: 300,
              decoration: BoxDecoration(
                shape: BoxShape.circle,
                color: AppColors.primary.withOpacity(0.15),
              ),
            ),
          ),
          Positioned(
            bottom: -80,
            left: -80,
            child: Container(
              width: 260,
              height: 260,
              decoration: BoxDecoration(
                shape: BoxShape.circle,
                color: AppColors.secondary.withOpacity(0.15),
              ),
            ),
          ),
          Center(
            child: FadeTransition(
              opacity: _fadeAnimation,
              child: ScaleTransition(
                scale: _scaleAnimation,
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    // Brand Logo Icon Card
                    Container(
                      padding: const EdgeInsets.all(24),
                      decoration: BoxDecoration(
                        gradient: const LinearGradient(
                          colors: [Color(0xFF0284C7), Color(0xFF6366F1)],
                          begin: Alignment.topLeft,
                          end: Alignment.bottomRight,
                        ),
                        borderRadius: BorderRadius.circular(28),
                        boxShadow: [
                          BoxShadow(
                            color: AppColors.primary.withOpacity(0.4),
                            blurRadius: 24,
                            offset: const Offset(0, 8),
                          ),
                        ],
                      ),
                      child: const Icon(
                        Icons.school_rounded,
                        size: 64,
                        color: Colors.white,
                      ),
                    ),
                    const SizedBox(height: 28),

                    // App Title
                    const Text(
                      AppConstants.appName,
                      style: TextStyle(
                        fontSize: 32,
                        fontWeight: FontWeight.w800,
                        letterSpacing: -0.5,
                        color: Colors.white,
                      ),
                    ),
                    const SizedBox(height: 8),

                    // Tagline
                    Text(
                      AppConstants.appTagline,
                      style: TextStyle(
                        fontSize: 15,
                        fontWeight: FontWeight.w400,
                        color: Colors.white.withOpacity(0.7),
                        letterSpacing: 0.2,
                      ),
                    ),
                    const SizedBox(height: 48),

                    // Material 3 Loading Spinner
                    SizedBox(
                      width: 28,
                      height: 28,
                      child: CircularProgressIndicator(
                        strokeWidth: 2.8,
                        valueColor: AlwaysStoppedAnimation<Color>(
                          AppColors.primaryLight.withOpacity(0.9),
                        ),
                      ),
                    ),
                  ],
                ),
              ),
            ),
          ),

          // Bottom Version label
          Positioned(
            bottom: 24,
            left: 0,
            right: 0,
            child: Center(
              child: Text(
                'Version ${AppConstants.appVersion}',
                style: TextStyle(
                  fontSize: 12,
                  color: Colors.white.withOpacity(0.4),
                ),
              ),
            ),
          ),
        ],
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
      ),
    );
  }
}
