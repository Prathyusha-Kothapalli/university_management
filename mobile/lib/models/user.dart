/// User role enum
enum UserRole {
  student,
  faculty,
  admin,
  staff;

  static UserRole fromString(String? role) {
    switch (role?.toLowerCase()) {
      case 'faculty':
      case 'teacher':
      case 'professor':
        return UserRole.faculty;
      case 'admin':
      case 'administrator':
        return UserRole.admin;
      case 'staff':
        return UserRole.staff;
      case 'student':
      default:
        return UserRole.student;
    }
  }

  String get displayName {
    switch (this) {
      case UserRole.student:
        return 'Student';
      case UserRole.faculty:
        return 'Faculty';
      case UserRole.admin:
        return 'Administrator';
      case UserRole.staff:
        return 'Staff';
    }
  }

  String get roleString {
    switch (this) {
      case UserRole.student:
        return 'student';
      case UserRole.faculty:
        return 'faculty';
      case UserRole.admin:
        return 'admin';
      case UserRole.staff:
        return 'staff';
    }
  }
}

/// User domain model representing an authenticated university member.
class User {
  final String id;
  final String name;
  final String email;
  final String? phone;
  final UserRole role;
  final String? department;
  final String? studentId;
  final String? avatarUrl;
  final String? enrolledYear;
  final double? gpa;
  final double? attendanceRate;
  final DateTime? createdAt;

  const User({
    required this.id,
    required this.name,
    required this.email,
    this.phone,
    this.role = UserRole.student,
    this.department,
    this.studentId,
    this.avatarUrl,
    this.enrolledYear,
    this.gpa,
    this.attendanceRate,
    this.createdAt,
  });

  String get roleDisplay => role.displayName;

  String get initials {
    final parts = name.trim().split(RegExp(r'\s+'));
    if (parts.isEmpty || parts[0].isEmpty) return 'U';
    if (parts.length == 1) return parts[0][0].toUpperCase();
    return '${parts[0][0]}${parts[parts.length - 1][0]}'.toUpperCase();
  }

  factory User.fromJson(Map<String, dynamic> json) {
    final rawRole = json['role']?.toString();
    final roleEnum = rawRole != null ? UserRole.fromString(rawRole) : UserRole.student;

    return User(
      id: json['id']?.toString() ?? '',
      name: json['name'] as String? ?? json['full_name'] as String? ?? '',
      email: json['email'] as String? ?? '',
      phone: json['phone'] as String?,
      role: roleEnum,
      department: json['department'] as String? ?? 'Computer Science & AI',
      studentId: json['student_id'] as String? ?? json['roll_no'] as String? ?? 'US-2026-042',
      avatarUrl: json['avatar_url'] as String?,
      enrolledYear: json['enrolled_year'] as String? ?? '2024 - 2028',
      gpa: (json['gpa'] as num?)?.toDouble() ?? 3.82,
      attendanceRate: (json['attendance_rate'] as num?)?.toDouble() ?? 94.5,
      createdAt: json['created_at'] != null ? DateTime.tryParse(json['created_at'].toString()) : null,
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'name': name,
      'full_name': name,
      'email': email,
      'phone': phone,
      'role': role.roleString,
      'department': department,
      'student_id': studentId,
      'avatar_url': avatarUrl,
      'enrolled_year': enrolledYear,
      'gpa': gpa,
      'attendance_rate': attendanceRate,
      'created_at': createdAt?.toIso8601String(),
    };
  }

  User copyWith({
    String? id,
    String? name,
    String? email,
    String? phone,
    UserRole? role,
    String? department,
    String? studentId,
    String? avatarUrl,
    String? enrolledYear,
    double? gpa,
    double? attendanceRate,
    DateTime? createdAt,
  }) {
    return User(
      id: id ?? this.id,
      name: name ?? this.name,
      email: email ?? this.email,
      phone: phone ?? this.phone,
      role: role ?? this.role,
      department: department ?? this.department,
      studentId: studentId ?? this.studentId,
      avatarUrl: avatarUrl ?? this.avatarUrl,
      enrolledYear: enrolledYear ?? this.enrolledYear,
      gpa: gpa ?? this.gpa,
      attendanceRate: attendanceRate ?? this.attendanceRate,
      createdAt: createdAt ?? this.createdAt,
    );
  }
}
