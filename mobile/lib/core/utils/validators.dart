<<<<<<< HEAD
/// Form field validation utilities.
class Validators {
  Validators._();

  static final RegExp _emailRegExp = RegExp(
    r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
  );

  static final RegExp _phoneRegExp = RegExp(
    r'^\+?[0-9\s\-()]{7,15}$',
=======
class Validators {
  static final RegExp _emailRegExp = RegExp(
    r'^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$',
  );

  static final RegExp _phoneRegExp = RegExp(
    r'^\+?[0-9\s\-\(\)]{7,18}$',
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
  );

  static String? validateRequired(String? value, [String fieldName = 'Field']) {
    if (value == null || value.trim().isEmpty) {
      return '$fieldName is required';
    }
    return null;
  }

  static String? validateName(String? value) {
    if (value == null || value.trim().isEmpty) {
      return 'Full name is required';
    }
    if (value.trim().length < 2) {
<<<<<<< HEAD
      return 'Name must be at least 2 characters';
=======
      return 'Name must be at least 2 characters long';
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
    }
    return null;
  }

  static String? validateEmail(String? value) {
    if (value == null || value.trim().isEmpty) {
      return 'Email address is required';
    }
<<<<<<< HEAD
    if (!_emailRegExp.hasMatch(value.trim())) {
=======
    final trimmed = value.trim();
    if (!_emailRegExp.hasMatch(trimmed)) {
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
      return 'Please enter a valid email address';
    }
    return null;
  }

  static String? validatePassword(String? value) {
    if (value == null || value.isEmpty) {
      return 'Password is required';
    }
    if (value.length < 6) {
      return 'Password must be at least 6 characters long';
    }
    return null;
  }

<<<<<<< HEAD
  static String? validateConfirmPassword(String? confirmPassword, String? password) {
    if (confirmPassword == null || confirmPassword.isEmpty) {
      return 'Please confirm your password';
    }
    if (confirmPassword != password) {
=======
  static String? validateConfirmPassword(String? value, String? originalPassword) {
    if (value == null || value.isEmpty) {
      return 'Please confirm your password';
    }
    if (value != originalPassword) {
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
      return 'Passwords do not match';
    }
    return null;
  }

  static String? validatePhone(String? value) {
    if (value == null || value.trim().isEmpty) {
      return 'Phone number is required';
    }
<<<<<<< HEAD
    if (!_phoneRegExp.hasMatch(value.trim())) {
=======
    final trimmed = value.trim();
    if (!_phoneRegExp.hasMatch(trimmed)) {
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
      return 'Please enter a valid phone number';
    }
    return null;
  }
}
