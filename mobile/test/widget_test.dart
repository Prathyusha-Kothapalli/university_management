import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:unisphere_mobile/core/constants/app_constants.dart';
import 'package:unisphere_mobile/main.dart';
import 'package:unisphere_mobile/state/auth_state.dart';

void main() {
  testWidgets('App renders splash screen with UniSphere AI branding', (WidgetTester tester) async {
    final authState = AuthState();

    await tester.pumpWidget(UniSphereApp(authState: authState));

    // Verify UniSphere AI branding is displayed
    expect(find.text(AppConstants.appName), findsOneWidget);
    expect(find.byType(CircularProgressIndicator), findsOneWidget);
  });
}