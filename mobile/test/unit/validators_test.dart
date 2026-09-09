import 'package:flutter_test/flutter_test.dart';
import 'package:unisphere_mobile/core/utils/validators.dart';

void main() {
  group('Validators Unit Tests', () {
    test('validateRequired tests', () {
      expect(Validators.validateRequired(null, 'Username'), 'Username is required');
      expect(Validators.validateRequired('', 'Username'), 'Username is required');
      expect(Validators.validateRequired('   ', 'Username'), 'Username is required');
      expect(Validators.validateRequired('alex', 'Username'), isNull);
    });

    test('validateEmail tests', () {
      expect(Validators.validateEmail(null), 'Email address is required');
      expect(Validators.validateEmail(''), 'Email address is required');
      expect(Validators.validateEmail('notanemail'), 'Please enter a valid email address');
      expect(Validators.validateEmail('missing@domain'), 'Please enter a valid email address');
      expect(Validators.validateEmail('student@university.edu'), isNull);
      expect(Validators.validateEmail('faculty.member@sub.college.org'), isNull);
    });

    test('validatePassword tests', () {
      expect(Validators.validatePassword(null), 'Password is required');
      expect(Validators.validatePassword(''), 'Password is required');
      expect(Validators.validatePassword('12345'), 'Password must be at least 6 characters long');
      expect(Validators.validatePassword('Password123!'), isNull);
    });

    test('validateConfirmPassword tests', () {
      expect(Validators.validateConfirmPassword(null, 'secret'), 'Please confirm your password');
      expect(Validators.validateConfirmPassword('mismatch', 'secret'), 'Passwords do not match');
      expect(Validators.validateConfirmPassword('secret', 'secret'), isNull);
    });

    test('validatePhone tests', () {
      expect(Validators.validatePhone(null), 'Phone number is required');
      expect(Validators.validatePhone('12'), 'Please enter a valid phone number');
      expect(Validators.validatePhone('+1 (555) 234-5678'), isNull);
      expect(Validators.validatePhone('9876543210'), isNull);
    });
  });
}
