import 'package:flutter_test/flutter_test.dart';
import 'package:unisphere_mobile/services/token_storage_service.dart';

void main() {
  group('TokenStorageService Tests', () {
    late TokenStorageService service;

    setUp(() async {
      service = TokenStorageService();
      await service.deleteToken();
    });

    test('saveToken and getToken persist tokens', () async {
      expect(await service.hasToken(), isFalse);
      expect(await service.getToken(), isNull);

      await service.saveToken(
        'sample_jwt_access_token_123',
        refreshToken: 'sample_refresh_token_456',
      );

      expect(await service.hasToken(), isTrue);
      expect(await service.getToken(), 'sample_jwt_access_token_123');
      expect(await service.getRefreshToken(), 'sample_refresh_token_456');
    });

    test('deleteToken clears credentials safely', () async {
      await service.saveToken('token_to_remove');
      expect(await service.hasToken(), isTrue);

      await service.deleteToken();
      expect(await service.hasToken(), isFalse);
      expect(await service.getToken(), isNull);
    });
  });
}