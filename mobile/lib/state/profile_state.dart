import 'package:flutter/foundation.dart';
import '../core/network/api_exceptions.dart';
import '../models/user.dart';
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
import '../models/user_profile.dart';
=======
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
import '../repositories/user_repository.dart';

/// Profile management state provider.
class ProfileState extends ChangeNotifier {
<<<<<<< HEAD
  final UserRepository _userRepository;

  bool _isSaving = false;
  String? _errorMessage;

  ProfileState({UserRepository? userRepository})
      : _userRepository = userRepository ?? UserRepository();

  bool get isSaving => _isSaving;
  String? get errorMessage => _errorMessage;

  /// Update user profile attributes
  Future<User?> updateProfile(
    User currentUser, {
    required String name,
    String? phone,
  }) async {
=======
=======
>>>>>>> origin/web
import '../models/user_profile.dart';
import '../repositories/user_repository.dart';
import '../core/network/api_exceptions.dart';

class ProfileState extends ChangeNotifier {
=======
<<<<<<< HEAD
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
  final UserRepository _repository;

  UserProfile? _profile;
  bool _isLoading = false;
  bool _isSaving = false;
  String? _errorMessage;

  ProfileState({
    UserRepository? repository,
    UserRepository? userRepository,
  }) : _repository = repository ?? userRepository ?? UserRepository();

  UserProfile? get profile => _profile;
  bool get isLoading => _isLoading;
  bool get isSaving => _isSaving;
  String? get errorMessage => _errorMessage;

  Future<void> loadProfile(User currentUser) async {
    _isLoading = true;
    _errorMessage = null;
    notifyListeners();

    try {
      _profile = await _repository.getUserProfile(currentUser);
      _errorMessage = null;
    } on ApiException catch (e) {
      _errorMessage = e.message;
    } catch (_) {
      _errorMessage = 'Failed to load profile details.';
    } finally {
      _isLoading = false;
      notifyListeners();
    }
  }

<<<<<<< HEAD
  Future<User?> updateProfile(User currentUser, {String? name, String? phone}) async {
<<<<<<< HEAD
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
=======
import '../repositories/user_repository.dart';

/// Profile management state provider.
class ProfileState extends ChangeNotifier {
=======
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
  final UserRepository _userRepository;

  bool _isSaving = false;
  String? _errorMessage;

  ProfileState({UserRepository? userRepository})
      : _userRepository = userRepository ?? UserRepository();

  bool get isSaving => _isSaving;
  String? get errorMessage => _errorMessage;

  /// Update user profile attributes
<<<<<<< HEAD
=======
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
  Future<User?> updateProfile(
    User currentUser, {
    required String name,
    String? phone,
  }) async {
<<<<<<< HEAD
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
    _isSaving = true;
    _errorMessage = null;
    notifyListeners();

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    final result = await _userRepository.updateProfile(name: name, phone: phone);

    _isSaving = false;
    return result.fold(
      onSuccess: (updatedUser) {
        _errorMessage = null;
        notifyListeners();
        return updatedUser;
      },
      onFailure: (error) {
        _errorMessage = error;
        notifyListeners();
        return null;
      },
    );
  }

  void clearError() {
    _errorMessage = null;
=======
=======
>>>>>>> origin/web
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
    try {
      final updatedUser = await _repository.updateProfile(
        currentUser,
        name: name,
        phone: phone,
      );
      if (_profile != null) {
        _profile = _profile!.copyWith(user: updatedUser);
      } else {
        _profile = UserProfile(user: updatedUser);
      }
      _errorMessage = null;
      notifyListeners();
      return updatedUser;
    } on ApiException catch (e) {
      _errorMessage = e.message;
      notifyListeners();
      return null;
    } catch (_) {
      _errorMessage = 'Failed to update profile. Please try again.';
      notifyListeners();
      return null;
    } finally {
      _isSaving = false;
      notifyListeners();
    }
=======
    final result = await _userRepository.updateProfile(name: name, phone: phone);

    _isSaving = false;
    return result.fold(
      onSuccess: (updatedUser) {
        _errorMessage = null;
        notifyListeners();
        return updatedUser;
      },
      onFailure: (error) {
        _errorMessage = error;
        notifyListeners();
        return null;
      },
    );
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9
  }

  void clearError() {
    _errorMessage = null;
<<<<<<< HEAD
    notifyListeners();
  }

  void clear() {
    _profile = null;
    _errorMessage = null;
    _isLoading = false;
    _isSaving = false;
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
=======
    final result = await _userRepository.updateProfile(name: name, phone: phone);

    _isSaving = false;
    return result.fold(
      onSuccess: (updatedUser) {
        _errorMessage = null;
        notifyListeners();
        return updatedUser;
      },
      onFailure: (error) {
        _errorMessage = error;
        notifyListeners();
        return null;
      },
    );
  }

  void clearError() {
    _errorMessage = null;
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
=======
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
    notifyListeners();
  }
}
