import 'package:flutter_test/flutter_test.dart';
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
=======
>>>>>>> origin/web
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
import 'package:unisphere_mobile/models/user.dart';
import 'package:unisphere_mobile/services/storage_service.dart';
import 'package:unisphere_mobile/services/token_storage_service.dart';

void main() {
  group('TokenStorageService Unit Tests', () {
    late InMemoryStorageService inMemoryStorage;
    late TokenStorageService tokenStorage;

    setUp(() {
      inMemoryStorage = InMemoryStorageService();
      tokenStorage = TokenStorageService(storage: inMemoryStorage);
    });

    test('save, get, and delete token operations', () async {
      expect(await tokenStorage.hasToken(), isFalse);
      expect(await tokenStorage.getToken(), isNull);

      await tokenStorage.saveToken('jwt_mock_token_abc123', refreshToken: 'jwt_refresh_456');
      expect(await tokenStorage.hasToken(), isTrue);
      expect(await tokenStorage.getToken(), 'jwt_mock_token_abc123');
      expect(await tokenStorage.getRefreshToken(), 'jwt_refresh_456');

      await tokenStorage.deleteToken();
      expect(await tokenStorage.hasToken(), isFalse);
      expect(await tokenStorage.getToken(), isNull);
    });

    test('save, get, and delete user operations', () async {
      const user = User(
        id: 'usr_test',
        name: 'Alex Mercer',
        email: 'alex@uni.edu',
      );

      expect(await tokenStorage.getUser(), isNull);
      await tokenStorage.saveUser(user);

      final retrieved = await tokenStorage.getUser();
      expect(retrieved, isNotNull);
      expect(retrieved?.id, 'usr_test');
      expect(retrieved?.name, 'Alex Mercer');

      await tokenStorage.deleteUser();
      expect(await tokenStorage.getUser(), isNull);
    });

    test('remember me and saved email behavior', () async {
      expect(await tokenStorage.getRememberMe(), isFalse);

      await tokenStorage.setRememberMe(true);
      await tokenStorage.saveEmail('student@university.edu');

      expect(await tokenStorage.getRememberMe(), isTrue);
      expect(await tokenStorage.getSavedEmail(), 'student@university.edu');
    });

    test('clearAuthData resets session state correctly', () async {
      await tokenStorage.saveToken('sample_token');
      await tokenStorage.saveUser(const User(id: '1', name: 'Alex', email: 'alex@uni.edu'));
      await tokenStorage.setRememberMe(false);
      await tokenStorage.saveEmail('alex@uni.edu');

      await tokenStorage.clearAuthData();

      expect(await tokenStorage.hasToken(), isFalse);
      expect(await tokenStorage.getUser(), isNull);
      expect(await tokenStorage.getSavedEmail(), isNull);
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
=======
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
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
    });
  });
}