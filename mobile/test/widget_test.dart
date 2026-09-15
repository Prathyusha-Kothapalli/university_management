import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:unisphere_mobile/core/constants/app_constants.dart';
import 'package:unisphere_mobile/main.dart';
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
import 'package:unisphere_mobile/state/auth_state.dart';

void main() {
  testWidgets('App renders splash screen with UniSphere AI branding', (WidgetTester tester) async {
    final authState = AuthState();

    await tester.pumpWidget(UniSphereApp(authState: authState));

    // Verify UniSphere AI branding is displayed
    expect(find.text(AppConstants.appName), findsOneWidget);
    expect(find.byType(CircularProgressIndicator), findsOneWidget);
=======
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
import 'package:unisphere_mobile/repositories/auth_repository.dart';
import 'package:unisphere_mobile/repositories/user_repository.dart';
import 'package:unisphere_mobile/services/storage_service.dart';
import 'package:unisphere_mobile/services/token_storage_service.dart';
import 'package:unisphere_mobile/state/auth_state.dart';
import 'package:unisphere_mobile/state/profile_state.dart';

void main() {
  testWidgets('UniSphere App initial splash and app load smoke test', (WidgetTester tester) async {
    final storage = InMemoryStorageService();
    final tokenStorage = TokenStorageService(storage: storage);
    final authRepository = AuthRepository(tokenStorage: tokenStorage, forceMock: true);
    final userRepository = UserRepository(tokenStorage: tokenStorage, forceMock: true);

=======
import 'package:unisphere_mobile/repositories/auth_repository.dart';
import 'package:unisphere_mobile/repositories/user_repository.dart';
import 'package:unisphere_mobile/services/storage_service.dart';
import 'package:unisphere_mobile/services/token_storage_service.dart';
import 'package:unisphere_mobile/state/auth_state.dart';
import 'package:unisphere_mobile/state/profile_state.dart';

void main() {
  testWidgets('UniSphere App initial splash and app load smoke test', (WidgetTester tester) async {
    final storage = InMemoryStorageService();
    final tokenStorage = TokenStorageService(storage: storage);
    final authRepository = AuthRepository(tokenStorage: tokenStorage, forceMock: true);
    final userRepository = UserRepository(tokenStorage: tokenStorage, forceMock: true);

>>>>>>> origin/web
    final authState = AuthState(repository: authRepository);
    final profileState = ProfileState(repository: userRepository);

    await tester.pumpWidget(
      UniSphereApp(
        authState: authState,
        profileState: profileState,
      ),
    );

    // Verify Splash Screen elements render immediately
    expect(find.text(AppConstants.appName), findsOneWidget);
    expect(find.text(AppConstants.appTagline), findsOneWidget);
    expect(find.byType(CircularProgressIndicator), findsOneWidget);

    // Advance time through splash animation and authentication check
    await tester.pump(const Duration(milliseconds: 1500));
    await tester.pumpAndSettle();

    // After unauthenticated splash check, should navigate to Login screen
    expect(find.text('Welcome Back'), findsOneWidget);
    expect(find.text('Sign In'), findsOneWidget);
    expect(find.text('Create an Account'), findsOneWidget);
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
=======
import 'package:unisphere_mobile/state/auth_state.dart';

void main() {
  testWidgets('App renders splash screen with UniSphere AI branding', (WidgetTester tester) async {
    final authState = AuthState();

    await tester.pumpWidget(UniSphereApp(authState: authState));

    // Verify UniSphere AI branding is displayed
    expect(find.text(AppConstants.appName), findsOneWidget);
    expect(find.byType(CircularProgressIndicator), findsOneWidget);
<<<<<<< HEAD
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
  });
}