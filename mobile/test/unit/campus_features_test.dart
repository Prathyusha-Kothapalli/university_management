import 'package:flutter_test/flutter_test.dart';
import 'package:unisphere_mobile/models/campus_features.dart';

void main() {
  group('Campus Features Models Tests', () {
    test('AttendanceRecord computes percentage and safety threshold', () {
      const safeRecord = AttendanceRecord(
        id: 'att_1',
        courseCode: 'CS-401',
        courseName: 'Deep Learning',
        attendedHours: 38,
        totalHours: 40,
        instructor: 'Prof. Vance',
      );

      expect(safeRecord.percentage, 95.0);
      expect(safeRecord.isSafe, isTrue);

      const dangerRecord = AttendanceRecord(
        id: 'att_2',
        courseCode: 'DS-310',
        courseName: 'Big Data',
        attendedHours: 20,
        totalHours: 30,
        instructor: 'Dr. Mitchell',
      );

      expect(dangerRecord.percentage, closeTo(66.66, 0.1));
      expect(dangerRecord.isSafe, isFalse);
    });

    test('AssignmentItem parses JSON correctly', () {
      final json = {
        'id': 'asg_1',
        'course_code': 'CS-401',
        'title': 'Neural Nets Assignment',
        'description': 'PyTorch implementation',
        'due_date': 'Sep 18, 2026',
        'max_score': 100,
        'obtained_score': 95,
        'status': 'Graded',
      };

      final item = AssignmentItem.fromJson(json);
      expect(item.id, 'asg_1');
      expect(item.courseCode, 'CS-401');
      expect(item.obtainedScore, 95);
      expect(item.status, 'Graded');

      final exported = item.toJson();
      expect(exported['title'], 'Neural Nets Assignment');
      expect(exported['status'], 'Graded');
    });

    test('PlacementDrive parses details and status', () {
      final json = {
        'id': 'plc_1',
        'company': 'Google',
        'role': 'AI Engineer',
        'ctc': '\$145,000 / annum',
        'location': 'Mountain View, CA',
        'eligibility_gpa': '3.50+ GPA',
        'deadline': 'Sep 30, 2026',
        'status': 'Eligible',
      };

      final drive = PlacementDrive.fromJson(json);
      expect(drive.company, 'Google');
      expect(drive.role, 'AI Engineer');
      expect(drive.status, 'Eligible');
    });

    test('ChatMessage serializes correctly', () {
      final json = {
        'id': 'msg_1',
        'sender': 'Alex Johnson',
        'text': 'Hello Professor!',
        'time': '10:00 AM',
        'is_me': true,
      };

      final chat = ChatMessage.fromJson(json);
      expect(chat.sender, 'Alex Johnson');
      expect(chat.isMe, isTrue);
    });
  });
}
