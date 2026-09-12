<<<<<<< HEAD
import 'dart:async';
import 'dart:convert';
import 'dart:io';

abstract class IStorageService {
  Future<void> write(String key, String value);
  Future<String?> read(String key);
  Future<void> delete(String key);
  Future<void> clear();
  Future<bool> containsKey(String key);
}

/// In-memory storage useful for unit tests, rapid testing, and fallbacks
class InMemoryStorageService implements IStorageService {
  final Map<String, String> _data = {};

  @override
  Future<void> write(String key, String value) async {
    _data[key] = value;
  }

  @override
  Future<String?> read(String key) async {
    return _data[key];
  }

  @override
  Future<void> delete(String key) async {
    _data.remove(key);
  }

  @override
  Future<void> clear() async {
    _data.clear();
  }

  @override
  Future<bool> containsKey(String key) async {
    return _data.containsKey(key);
  }
}

/// Persistent file-backed secure key-value store with obfuscation
/// Works reliably across Android, iOS, Windows, Mac, Linux without native binary dependency issues.
class SecureFileStorageService implements IStorageService {
  static final Map<String, String> _memoryCache = {};
  static bool _initialized = false;
  final String _storageFileName;

  SecureFileStorageService({String storageFileName = '.unisphere_secure_vault.dat'})
      : _storageFileName = storageFileName;

  File get _storageFile {
    try {
      final dir = Directory.systemTemp;
      return File('${dir.path}${Platform.pathSeparator}$_storageFileName');
    } catch (_) {
      return File(_storageFileName);
    }
  }

  Future<void> _ensureLoaded() async {
    if (_initialized) return;
    try {
      final file = _storageFile;
      if (await file.exists()) {
        final content = await file.readAsString();
        if (content.isNotEmpty) {
          final decoded = jsonDecode(_unobfuscate(content)) as Map<String, dynamic>;
          _memoryCache.clear();
          decoded.forEach((k, v) {
            _memoryCache[k] = v.toString();
          });
        }
      }
    } catch (_) {
      // If reading fails or file is corrupt, fallback gracefully to memory
    } finally {
      _initialized = true;
    }
  }

  Future<void> _persist() async {
    try {
      final file = _storageFile;
      final rawJson = jsonEncode(_memoryCache);
      final obfuscated = _obfuscate(rawJson);
      await file.writeAsString(obfuscated, flush: true);
    } catch (_) {
      // Non-fatal if filesystem is restricted (e.g. sandbox without temp access)
    }
  }

  String _obfuscate(String input) {
    final bytes = utf8.encode(input);
    // Simple XOR cipher with fixed salt for basic on-device resting obfuscation
    final obfuscated = bytes.map((b) => b ^ 0x5A).toList();
    return base64Encode(obfuscated);
  }

  String _unobfuscate(String input) {
    final bytes = base64Decode(input);
    final restored = bytes.map((b) => b ^ 0x5A).toList();
    return utf8.decode(restored);
  }

  @override
  Future<void> write(String key, String value) async {
    await _ensureLoaded();
    _memoryCache[key] = value;
    await _persist();
  }

  @override
  Future<String?> read(String key) async {
    await _ensureLoaded();
    return _memoryCache[key];
  }

  @override
  Future<void> delete(String key) async {
    await _ensureLoaded();
    _memoryCache.remove(key);
    await _persist();
  }

  @override
  Future<void> clear() async {
    await _ensureLoaded();
    _memoryCache.clear();
    await _persist();
  }

  @override
  Future<bool> containsKey(String key) async {
    await _ensureLoaded();
    return _memoryCache.containsKey(key);
=======
import 'dart:convert';
import '../models/user.dart';

/// Key-value storage service for non-sensitive cached data (e.g. user profile, settings).
class StorageService {
  static final Map<String, dynamic> _memoryStore = {};

  static const String _cachedUserKey = 'unisphere_cached_user';
  static const String _rememberEmailKey = 'unisphere_remember_email';

  Future<void> saveUser(User user) async {
    _memoryStore[_cachedUserKey] = jsonEncode(user.toJson());
  }

  Future<User?> getUser() async {
    final raw = _memoryStore[_cachedUserKey];
    if (raw == null) return null;
    try {
      final map = jsonDecode(raw.toString()) as Map<String, dynamic>;
      return User.fromJson(map);
    } catch (_) {
      return null;
    }
  }

  Future<void> removeUser() async {
    _memoryStore.remove(_cachedUserKey);
  }

  Future<void> saveRememberedEmail(String email) async {
    _memoryStore[_rememberEmailKey] = email;
  }

  Future<String?> getRememberedEmail() async {
    return _memoryStore[_rememberEmailKey] as String?;
  }

  Future<void> clearAll() async {
    _memoryStore.clear();
>>>>>>> 29907a7 (added flutter)
  }
}
