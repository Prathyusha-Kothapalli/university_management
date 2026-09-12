<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
=======
>>>>>>> origin/web
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
import 'dart:async';
import 'dart:convert';
import 'dart:io';
import '../models/user.dart';

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

/// Persistent file-backed secure key-value store
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
          final decoded = jsonDecode(content) as Map<String, dynamic>;
          decoded.forEach((k, v) => _memoryCache[k] = v.toString());
        }
      }
    } catch (_) {
      // Gracefully continue with memory cache
    }
    _initialized = true;
  }

  Future<void> _flush() async {
    try {
      final file = _storageFile;
      await file.writeAsString(jsonEncode(_memoryCache));
    } catch (_) {
      // Ignored for environments without write permissions
    }
  }

  @override
  Future<void> write(String key, String value) async {
    await _ensureLoaded();
    _memoryCache[key] = value;
    await _flush();
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
    await _flush();
  }

  @override
  Future<void> clear() async {
    _memoryCache.clear();
    await _flush();
  }

  @override
  Future<bool> containsKey(String key) async {
    await _ensureLoaded();
    return _memoryCache.containsKey(key);
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
=======
import 'dart:convert';
import '../models/user.dart';

/// Key-value storage service for non-sensitive cached data (e.g. user profile, settings).
class StorageService {
  static final Map<String, dynamic> _memoryStore = {};
=======
  }
}

/// Key-value storage service for user preferences and profile caching.
class StorageService {
  final IStorageService _storage;

  StorageService({IStorageService? storage})
      : _storage = storage ?? InMemoryStorageService();
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689

  static const String _cachedUserKey = 'unisphere_cached_user';
  static const String _rememberEmailKey = 'unisphere_remember_email';

  Future<void> saveUser(User user) async {
<<<<<<< HEAD
    _memoryStore[_cachedUserKey] = jsonEncode(user.toJson());
  }

  Future<User?> getUser() async {
    final raw = _memoryStore[_cachedUserKey];
    if (raw == null) return null;
    try {
      final map = jsonDecode(raw.toString()) as Map<String, dynamic>;
=======
    await _storage.write(_cachedUserKey, jsonEncode(user.toJson()));
  }

  Future<User?> getUser() async {
    final raw = await _storage.read(_cachedUserKey);
    if (raw == null) return null;
    try {
      final map = jsonDecode(raw) as Map<String, dynamic>;
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
      return User.fromJson(map);
    } catch (_) {
      return null;
    }
  }

  Future<void> removeUser() async {
<<<<<<< HEAD
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
>>>>>>> origin/web
=======
    await _storage.delete(_cachedUserKey);
  }

  Future<void> saveRememberedEmail(String email) async {
    await _storage.write(_rememberEmailKey, email);
  }

  Future<String?> getRememberedEmail() async {
    return await _storage.read(_rememberEmailKey);
  }

  Future<void> clearAll() async {
    await _storage.clear();
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
  }
}
