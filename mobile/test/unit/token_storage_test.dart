import 'package:flutter_test/flutter_test.dart';
import 'package:unisphere_mobile/services/token_storage_service.dart';

void main() {
  group('TokenStorageService Unit Tests', () {
    test('Stores and retrieves auth token correctly', () async {
      final storage = TokenStorageService();
      await storage.saveToken('test_jwt_token_12345');

      final token = await storage.getToken();
      expect(token, 'test_jwt_token_12345');

      await storage.clearToken();
      final clearedToken = await storage.getToken();
      expect(clearedToken, isNull);
    });
  });
}
