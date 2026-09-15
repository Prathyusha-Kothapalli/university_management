import 'package:flutter_test/flutter_test.dart';
import 'package:unisphere_mobile/models/user_model.dart';
import 'package:unisphere_mobile/models/course_model.dart';

void main() {
  group('Models Unit Tests', () {
    test('UserModel serialization and deserialization', () {
      final user = UserModel(
        id: 'usr-101',
        name: 'Alex Johnson',
        email: 'alex@university.edu',
        role: 'STUDENT',
        department: 'Computer Science',
      );

      expect(user.id, 'usr-101');
      expect(user.name, 'Alex Johnson');
      expect(user.email, 'alex@university.edu');
      expect(user.role, 'STUDENT');
      expect(user.department, 'Computer Science');

      final json = user.toJson();
      expect(json['id'], 'usr-101');
      expect(json['email'], 'alex@university.edu');

      final fromJson = UserModel.fromJson(json);
      expect(fromJson.id, user.id);
      expect(fromJson.email, user.email);
    });

    test('CourseModel serialization and deserialization', () {
      final course = CourseModel(
        id: 'cs-101',
        code: 'CS101',
        title: 'Introduction to AI',
        credits: 4,
        instructor: 'Dr. Sarah Connor',
      );

      expect(course.code, 'CS101');
      expect(course.credits, 4);

      final json = course.toJson();
      expect(json['code'], 'CS101');
    });
  });
}
