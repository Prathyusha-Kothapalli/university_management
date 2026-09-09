import 'package:flutter/foundation.dart';
import '../models/register_request.dart';
import '../models/user.dart';
import '../repositories/auth_repository.dart';

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
    _errorMessage = null;
    notifyListeners();

    try {
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
      notifyListeners();
      return false;
    }
  }

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
      _errorMessage = null;
      notifyListeners();
    }
  }
}
