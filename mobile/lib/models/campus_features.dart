/// Domain models for campus modules: Attendance, Timetable, Assignments,
/// Exams, Results, Notifications, Chat, Placements, and AI Assistant.

class AttendanceRecord {
  final String id;
  final String courseCode;
  final String courseName;
  final int attendedHours;
  final int totalHours;
  final String instructor;

  const AttendanceRecord({
    required this.id,
    required this.courseCode,
    required this.courseName,
    required this.attendedHours,
    required this.totalHours,
    required this.instructor,
  });

  double get percentage => totalHours > 0 ? (attendedHours / totalHours) * 100 : 0.0;
  bool get isSafe => percentage >= 75.0;

  factory AttendanceRecord.fromJson(Map<String, dynamic> json) {
    return AttendanceRecord(
      id: json['id']?.toString() ?? '',
      courseCode: json['course_code'] as String? ?? '',
      courseName: json['course_name'] as String? ?? '',
      attendedHours: json['attended_hours'] as int? ?? 0,
      totalHours: json['total_hours'] as int? ?? 0,
      instructor: json['instructor'] as String? ?? '',
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'course_code': courseCode,
      'course_name': courseName,
      'attended_hours': attendedHours,
      'total_hours': totalHours,
      'instructor': instructor,
    };
  }
}

class AssignmentItem {
  final String id;
  final String courseCode;
  final String title;
  final String description;
  final String dueDate;
  final int maxScore;
  final int? obtainedScore;
  final String status; // 'Pending' | 'Submitted' | 'Graded'

  const AssignmentItem({
    required this.id,
    required this.courseCode,
    required this.title,
    required this.description,
    required this.dueDate,
    required this.maxScore,
    this.obtainedScore,
    required this.status,
  });

  factory AssignmentItem.fromJson(Map<String, dynamic> json) {
    return AssignmentItem(
      id: json['id']?.toString() ?? '',
      courseCode: json['course_code'] as String? ?? '',
      title: json['title'] as String? ?? '',
      description: json['description'] as String? ?? '',
      dueDate: json['due_date'] as String? ?? '',
      maxScore: json['max_score'] as int? ?? 100,
      obtainedScore: json['obtained_score'] as int?,
      status: json['status'] as String? ?? 'Pending',
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'course_code': courseCode,
      'title': title,
      'description': description,
      'due_date': dueDate,
      'max_score': maxScore,
      'obtained_score': obtainedScore,
      'status': status,
    };
  }
}

class ExamItem {
  final String id;
  final String courseCode;
  final String courseTitle;
  final String date;
  final String time;
  final String hall;
  final String seat;

  const ExamItem({
    required this.id,
    required this.courseCode,
    required this.courseTitle,
    required this.date,
    required this.time,
    required this.hall,
    required this.seat,
  });

  factory ExamItem.fromJson(Map<String, dynamic> json) {
    return ExamItem(
      id: json['id']?.toString() ?? '',
      courseCode: json['course_code'] as String? ?? '',
      courseTitle: json['course_title'] as String? ?? '',
      date: json['date'] as String? ?? '',
      time: json['time'] as String? ?? '',
      hall: json['hall'] as String? ?? '',
      seat: json['seat'] as String? ?? '',
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'course_code': courseCode,
      'course_title': courseTitle,
      'date': date,
      'time': time,
      'hall': hall,
      'seat': seat,
    };
  }
}

class ExamResultItem {
  final String id;
  final String courseCode;
  final String courseTitle;
  final int credits;
  final String grade;
  final double gradePoint;

  const ExamResultItem({
    required this.id,
    required this.courseCode,
    required this.courseTitle,
    required this.credits,
    required this.grade,
    required this.gradePoint,
  });

  factory ExamResultItem.fromJson(Map<String, dynamic> json) {
    return ExamResultItem(
      id: json['id']?.toString() ?? '',
      courseCode: json['course_code'] as String? ?? '',
      courseTitle: json['course_title'] as String? ?? '',
      credits: json['credits'] as int? ?? 3,
      grade: json['grade'] as String? ?? 'A',
      gradePoint: (json['grade_point'] as num?)?.toDouble() ?? 4.0,
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'course_code': courseCode,
      'course_title': courseTitle,
      'credits': credits,
      'grade': grade,
      'grade_point': gradePoint,
    };
  }
}

class PlacementDrive {
  final String id;
  final String company;
  final String role;
  final String ctc;
  final String location;
  final String eligibilityGpa;
  final String deadline;
  final String status; // 'Eligible' | 'Applied' | 'Shortlisted'

  const PlacementDrive({
    required this.id,
    required this.company,
    required this.role,
    required this.ctc,
    required this.location,
    required this.eligibilityGpa,
    required this.deadline,
    required this.status,
  });

  factory PlacementDrive.fromJson(Map<String, dynamic> json) {
    return PlacementDrive(
      id: json['id']?.toString() ?? '',
      company: json['company'] as String? ?? '',
      role: json['role'] as String? ?? '',
      ctc: json['ctc'] as String? ?? '',
      location: json['location'] as String? ?? '',
      eligibilityGpa: json['eligibility_gpa'] as String? ?? '7.5+',
      deadline: json['deadline'] as String? ?? '',
      status: json['status'] as String? ?? 'Eligible',
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'company': company,
      'role': role,
      'ctc': ctc,
      'location': location,
      'eligibility_gpa': eligibilityGpa,
      'deadline': deadline,
      'status': status,
    };
  }
}

class CampusNotification {
  final String id;
  final String title;
  final String content;
  final String date;
  final String category;
  final bool isRead;

  const CampusNotification({
    required this.id,
    required this.title,
    required this.content,
    required this.date,
    required this.category,
    this.isRead = false,
  });

  factory CampusNotification.fromJson(Map<String, dynamic> json) {
    return CampusNotification(
      id: json['id']?.toString() ?? '',
      title: json['title'] as String? ?? '',
      content: json['content'] as String? ?? '',
      date: json['date'] as String? ?? '',
      category: json['category'] as String? ?? 'Academic',
      isRead: json['is_read'] as bool? ?? false,
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'title': title,
      'content': content,
      'date': date,
      'category': category,
      'is_read': isRead,
    };
  }
}

class ChatMessage {
  final String id;
  final String sender;
  final String text;
  final String time;
  final bool isMe;

  const ChatMessage({
    required this.id,
    required this.sender,
    required this.text,
    required this.time,
    required this.isMe,
  });

  factory ChatMessage.fromJson(Map<String, dynamic> json) {
    return ChatMessage(
      id: json['id']?.toString() ?? '',
      sender: json['sender'] as String? ?? '',
      text: json['text'] as String? ?? '',
      time: json['time'] as String? ?? '',
      isMe: json['is_me'] as bool? ?? false,
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'sender': sender,
      'text': text,
      'time': time,
      'is_me': isMe,
    };
  }
}
