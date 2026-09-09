import 'package:flutter_test/flutter_test.dart';
import 'package:unisphere_mobile/main.dart';

void main() {
  testWidgets('UniSphere App foundation smoke test', (WidgetTester tester) async {
    await tester.pumpWidget(const UniSphereApp());

    expect(find.text('UniSphere AI'), findsOneWidget);
    expect(find.text('Multi-Tenant University Management'), findsOneWidget);
    expect(find.text('Mobile Foundation Ready'), findsOneWidget);
  });
}
