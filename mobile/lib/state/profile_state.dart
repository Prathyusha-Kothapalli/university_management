import 'package:flutter/foundation.dart';
import '../models/user.dart';
<<<<<<< HEAD
import '../models/user_profile.dart';
import '../repositories/user_repository.dart';
import '../core/network/api_exceptions.dart';

class ProfileState extends ChangeNotifier {
  final UserRepository _repository;

  UserProfile? _profile;
  bool _isLoading = false;
  bool _isSaving = false;
  String? _errorMessage;

  ProfileState({UserRepository? repository})
      : _repository = repository ?? UserRepository();

  UserProfile? get profile => _profile;
  bool get isLoading => _isLoading;
  bool get isSaving => _isSaving;
  String? get errorMessage => _errorMessage;

  Future<void> loadProfile(User currentUser) async {
    _isLoading = true;
    _errorMessage = null;
    notifyListeners();

    try {
      _profile = await _repository.getProfile(currentUser);
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

  Future<User?> updateProfile(User currentUser, {String? name, String? phone}) async {
=======
import '../repositories/user_repository.dart';

/// Profile management state provider.
class ProfileState extends ChangeNotifier {
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
>>>>>>> 29907a7 (added flutter)
    _isSaving = true;
    _errorMessage = null;
    notifyListeners();

<<<<<<< HEAD
    try {
      final updatedUser = await _repository.updateProfile(currentUser, name: name, phone: phone);
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
  }

  void clear() {
    _profile = null;
    _errorMessage = null;
    _isLoading = false;
    _isSaving = false;
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
    notifyListeners();
  }
}
