import 'user.dart';

class UserProfile {
  final User user;
  final double gpa;
  final double attendancePercentage;
  final int enrolledCredits;
  final int totalCreditsCompleted;
  final String currentSemester;
  final String academicProgram;
  final String enrollmentStatus;
  final String? emergencyContact;

  const UserProfile({
    required this.user,
    this.gpa = 3.85,
    this.attendancePercentage = 94.2,
    this.enrolledCredits = 18,
    this.totalCreditsCompleted = 74,
    this.currentSemester = 'Semester 5 (Fall 2026)',
    this.academicProgram = 'B.S. Computer Science & Engineering',
    this.enrollmentStatus = 'Active - Full Time',
    this.emergencyContact,
  });

  factory UserProfile.fromJson(Map<String, dynamic> json) {
    return UserProfile(
      user: User.fromJson(json['user'] as Map<String, dynamic>? ?? json),
      gpa: (json['gpa'] as num?)?.toDouble() ?? 3.85,
      attendancePercentage: (json['attendance_percentage'] as num?)?.toDouble() ?? 94.2,
      enrolledCredits: (json['enrolled_credits'] as num?)?.toInt() ?? 18,
      totalCreditsCompleted: (json['total_credits_completed'] as num?)?.toInt() ?? 74,
      currentSemester: json['current_semester']?.toString() ?? 'Semester 5 (Fall 2026)',
      academicProgram: json['academic_program']?.toString() ?? 'B.S. Computer Science & Engineering',
      enrollmentStatus: json['enrollment_status']?.toString() ?? 'Active - Full Time',
      emergencyContact: json['emergency_contact']?.toString(),
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'user': user.toJson(),
      'gpa': gpa,
      'attendance_percentage': attendancePercentage,
      'enrolled_credits': enrolledCredits,
      'total_credits_completed': totalCreditsCompleted,
      'current_semester': currentSemester,
      'academic_program': academicProgram,
      'enrollment_status': enrollmentStatus,
      'emergency_contact': emergencyContact,
    };
  }

  UserProfile copyWith({
    User? user,
    double? gpa,
    double? attendancePercentage,
    int? enrolledCredits,
    int? totalCreditsCompleted,
    String? currentSemester,
    String? academicProgram,
    String? enrollmentStatus,
    String? emergencyContact,
  }) {
    return UserProfile(
      user: user ?? this.user,
      gpa: gpa ?? this.gpa,
      attendancePercentage: attendancePercentage ?? this.attendancePercentage,
      enrolledCredits: enrolledCredits ?? this.enrolledCredits,
      totalCreditsCompleted: totalCreditsCompleted ?? this.totalCreditsCompleted,
      currentSemester: currentSemester ?? this.currentSemester,
      academicProgram: academicProgram ?? this.academicProgram,
      enrollmentStatus: enrollmentStatus ?? this.enrollmentStatus,
      emergencyContact: emergencyContact ?? this.emergencyContact,
    );
  }
}
