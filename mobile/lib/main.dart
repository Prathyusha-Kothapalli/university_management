import 'package:flutter/material.dart';
<<<<<<< HEAD
import 'package:flutter/services.dart';
import 'core/constants/app_constants.dart';
import 'core/constants/route_constants.dart';
import 'core/theme/app_theme.dart';
=======
import 'core/constants/app_constants.dart';
import 'core/constants/route_constants.dart';
import 'core/theme/app_theme.dart';
import 'repositories/auth_repository.dart';
import 'repositories/user_repository.dart';
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
import 'screens/auth/login_screen.dart';
import 'screens/auth/register_screen.dart';
import 'screens/home/home_screen.dart';
import 'screens/profile/profile_screen.dart';
import 'screens/splash/splash_screen.dart';
<<<<<<< HEAD
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
=======
import 'services/api_service.dart';
import 'services/token_storage_service.dart';
import 'state/auth_state.dart';
import 'state/profile_state.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();

  // Initialize service & repository dependencies
  final tokenStorage = TokenStorageService();
  final apiService = ApiService(tokenStorage: tokenStorage);

  final authRepository = AuthRepository(
    apiService: apiService,
    tokenStorage: tokenStorage,
  );

  final userRepository = UserRepository(
    apiService: apiService,
    tokenStorage: tokenStorage,
  );

  final authState = AuthState(repository: authRepository);
  final profileState = ProfileState(repository: userRepository);

  runApp(
    UniSphereApp(
      authState: authState,
      profileState: profileState,
    ),
  );
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
}

/// Root Application Widget for UniSphere AI Mobile.
class UniSphereApp extends StatelessWidget {
  final AuthState authState;
<<<<<<< HEAD
=======
  final ProfileState profileState;
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd

  const UniSphereApp({
    super.key,
    required this.authState,
<<<<<<< HEAD
=======
    required this.profileState,
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
  });

  @override
  Widget build(BuildContext context) {
<<<<<<< HEAD
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
=======
    return AnimatedBuilder(
      animation: Listenable.merge([authState, profileState]),
      builder: (context, _) {
        return GestureDetector(
          // Dismiss keyboard on tapping outside of active inputs
          onTap: () => FocusManager.instance.primaryFocus?.unfocus(),
          child: MaterialApp(
            title: AppConstants.appName,
            debugShowCheckedModeBanner: false,
            theme: AppTheme.lightTheme,
            darkTheme: AppTheme.darkTheme,
            themeMode: ThemeMode.light,
            initialRoute: RouteConstants.splash,
            onGenerateRoute: (settings) {
              switch (settings.name) {
                case RouteConstants.splash:
                  return MaterialPageRoute(
                    settings: settings,
                    builder: (_) => SplashScreen(authState: authState),
                  );

                case RouteConstants.login:
                  return MaterialPageRoute(
                    settings: settings,
                    builder: (_) => LoginScreen(authState: authState),
                  );

                case RouteConstants.register:
                  return MaterialPageRoute(
                    settings: settings,
                    builder: (_) => RegisterScreen(authState: authState),
                  );

                case RouteConstants.home:
                  return MaterialPageRoute(
                    settings: settings,
                    builder: (_) => HomeScreen(
                      authState: authState,
                      profileState: profileState,
                    ),
                  );

                case RouteConstants.profile:
                  return MaterialPageRoute(
                    settings: settings,
                    builder: (_) => ProfileScreen(
                      authState: authState,
                      profileState: profileState,
                    ),
                  );

                default:
                  return MaterialPageRoute(
                    settings: settings,
                    builder: (_) => SplashScreen(authState: authState),
                  );
              }
            },
          ),
        );
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
      },
    );
  }
}
