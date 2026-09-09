import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'core/constants/app_constants.dart';
import 'core/constants/route_constants.dart';
import 'core/theme/app_theme.dart';
import 'screens/auth/login_screen.dart';
import 'screens/auth/register_screen.dart';
import 'screens/home/home_screen.dart';
import 'screens/profile/profile_screen.dart';
import 'screens/splash/splash_screen.dart';
import 'state/auth_state.dart';

void main() {
  WidgetsFlutterBinding.ensureInitialized();

  // Set system UI overlay style for modern transparent status bars
  SystemChrome.setSystemUIOverlayStyle(
    const SystemUiOverlayStyle(
      statusBarColor: Colors.transparent,
      statusBarIconBrightness: Brightness.dark,
      systemNavigationBarColor: Colors.white,
      systemNavigationBarIconBrightness: Brightness.dark,
    ),
  );

  final authState = AuthState();

  runApp(UniSphereApp(authState: authState));
}

/// Root Application Widget for UniSphere AI Mobile.
class UniSphereApp extends StatelessWidget {
  final AuthState authState;

  const UniSphereApp({
    super.key,
    required this.authState,
  });

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: AppConstants.appName,
      debugShowCheckedModeBanner: false,
      theme: AppTheme.lightTheme,
      darkTheme: AppTheme.darkTheme,
      themeMode: ThemeMode.light,
      initialRoute: RouteConstants.splash,
      routes: {
        RouteConstants.splash: (ctx) => SplashScreen(authState: authState),
        RouteConstants.login: (ctx) => LoginScreen(authState: authState),
        RouteConstants.register: (ctx) => RegisterScreen(authState: authState),
        RouteConstants.home: (ctx) => HomeScreen(authState: authState),
        RouteConstants.profile: (ctx) => ProfileScreen(authState: authState),
      },
    );
  }
}
