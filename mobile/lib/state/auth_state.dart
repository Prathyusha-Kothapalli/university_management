import 'package:flutter/foundation.dart';
<<<<<<< HEAD
=======
import '../core/network/api_exceptions.dart';
import '../models/login_request.dart';
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
import '../models/register_request.dart';
import '../models/user.dart';
import '../repositories/auth_repository.dart';

<<<<<<< HEAD
/// Central reactive authentication and session state provider.
class AuthState extends ChangeNotifier {
  final AuthRepository _authRepository;

  User? _currentUser;
  bool _isLoading = false;
  String? _errorMessage;
  bool _isInitialized = false;

  AuthState({AuthRepository? authRepository})
      : _authRepository = authRepository ?? AuthRepository();

  User? get currentUser => _currentUser;
  bool get isAuthenticated => _currentUser != null;
  bool get isLoading => _isLoading;
  String? get errorMessage => _errorMessage;
  bool get isInitialized => _isInitialized;

  /// Check whether the user already has a valid token/session
  Future<bool> checkAuth() async {
    _isLoading = true;
=======
enum AuthStatus {
  initial,
  loading,
  authenticated,
  unauthenticated,
  error,
}

class AuthState extends ChangeNotifier {
  final AuthRepository _repository;

  AuthStatus _status = AuthStatus.initial;
  User? _currentUser;
  String? _errorMessage;
  bool _rememberMe = false;
  String? _savedEmail;

  AuthState({AuthRepository? repository})
      : _repository = repository ?? AuthRepository();

  AuthStatus get status => _status;
  User? get currentUser => _currentUser;
  String? get errorMessage => _errorMessage;
  bool get isAuthenticated => _status == AuthStatus.authenticated && _currentUser != null;
  bool get isLoading => _status == AuthStatus.loading;
  bool get rememberMe => _rememberMe;
  String? get savedEmail => _savedEmail;

  /// Check token & user persistence upon app launch (Splash Screen)
  Future<void> checkAuthStatus() async {
    _status = AuthStatus.loading;
    notifyListeners();

    try {
      final isAuth = await _repository.isAuthenticated();
      _rememberMe = await _repository.getRememberMe();
      _savedEmail = await _repository.getSavedEmail();

      if (isAuth) {
        _currentUser = await _repository.getCurrentUser();
        _status = AuthStatus.authenticated;
      } else {
        _currentUser = null;
        _status = AuthStatus.unauthenticated;
      }
    } catch (_) {
      _currentUser = null;
      _status = AuthStatus.unauthenticated;
    }

    notifyListeners();
  }

  /// Perform login
  Future<bool> login({
    required String email,
    required String password,
    bool rememberMe = false,
  }) async {
    _status = AuthStatus.loading;
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
    _errorMessage = null;
    notifyListeners();

    try {
<<<<<<< HEAD
      final user = await _authRepository.checkAuth();
      _currentUser = user;
      _isInitialized = true;
      _isLoading = false;
      notifyListeners();
      return _currentUser != null;
    } catch (e) {
      _currentUser = null;
      _isInitialized = true;
      _isLoading = false;
=======
      final response = await _repository.login(
        LoginRequest(
          email: email.trim(),
          password: password,
          rememberMe: rememberMe,
        ),
      );

      _currentUser = response.user;
      _rememberMe = rememberMe;
      _savedEmail = rememberMe ? email.trim() : null;
      _status = AuthStatus.authenticated;
      _errorMessage = null;
      notifyListeners();
      return true;
    } on ApiException catch (e) {
      _status = AuthStatus.error;
      _errorMessage = e.message;
      notifyListeners();
      return false;
    } catch (e) {
      _status = AuthStatus.error;
      _errorMessage = 'An unexpected error occurred during login. Please try again.';
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
      notifyListeners();
      return false;
    }
  }

<<<<<<< HEAD
  /// Authenticate with email and password
  Future<bool> login(String email, String password) async {
    _isLoading = true;
    _errorMessage = null;
    notifyListeners();

    final result = await _authRepository.login(email, password);

    _isLoading = false;
    return result.fold(
      onSuccess: (user) {
        _currentUser = user;
        _errorMessage = null;
        notifyListeners();
        return true;
      },
      onFailure: (error) {
        _errorMessage = error;
        notifyListeners();
        return false;
      },
    );
  }

  /// Register a new account
  Future<bool> register(RegisterRequest request) async {
    _isLoading = true;
    _errorMessage = null;
    notifyListeners();

    final result = await _authRepository.register(request);

    _isLoading = false;
    return result.fold(
      onSuccess: (user) {
        _currentUser = user;
        _errorMessage = null;
        notifyListeners();
        return true;
      },
      onFailure: (error) {
        _errorMessage = error;
        notifyListeners();
        return false;
      },
    );
  }

  /// Update local user state
  void updateUser(User user) {
    _currentUser = user;
    notifyListeners();
  }

  /// Terminate session and reset state
  Future<void> logout() async {
    _isLoading = true;
    notifyListeners();

    await _authRepository.logout();

    _currentUser = null;
    _errorMessage = null;
    _isLoading = false;
    notifyListeners();
  }

  /// Clear active error banner
  void clearError() {
    if (_errorMessage != null) {
=======
  /// Perform registration
  Future<bool> register(RegisterRequest request) async {
    _status = AuthStatus.loading;
    _errorMessage = null;
    notifyListeners();

    try {
      final response = await _repository.register(request);
      _currentUser = response.user;
      _status = AuthStatus.authenticated;
      _errorMessage = null;
      notifyListeners();
      return true;
    } on ApiException catch (e) {
      _status = AuthStatus.error;
      _errorMessage = e.message;
      notifyListeners();
      return false;
    } catch (e) {
      _status = AuthStatus.error;
      _errorMessage = 'Registration failed. Please verify your details and try again.';
      notifyListeners();
      return false;
    }
  }

  /// Perform logout
  Future<void> logout() async {
    _status = AuthStatus.loading;
    notifyListeners();

    try {
      await _repository.logout();
    } catch (_) {
      // Ignored
    } finally {
      _currentUser = null;
      _status = AuthStatus.unauthenticated;
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
      _errorMessage = null;
      notifyListeners();
    }
  }
<<<<<<< HEAD
=======

  void updateUser(User updatedUser) {
    _currentUser = updatedUser;
    notifyListeners();
  }

  void clearError() {
    _errorMessage = null;
    if (_status == AuthStatus.error) {
      _status = _currentUser != null ? AuthStatus.authenticated : AuthStatus.unauthenticated;
    }
    notifyListeners();
  }
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
}
