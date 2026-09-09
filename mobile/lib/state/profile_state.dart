import 'package:flutter/foundation.dart';
import '../models/user.dart';
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
    _isSaving = true;
    _errorMessage = null;
    notifyListeners();

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
    notifyListeners();
  }
}
