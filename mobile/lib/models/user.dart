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
}

/// User domain model representing an authenticated university member.

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
  });

  factory User.fromJson(Map<String, dynamic> json) {
    return User(
      id: json['id']?.toString() ?? '',
      name: json['name'] as String? ?? json['full_name'] as String? ?? '',
      email: json['email'] as String? ?? '',
      phone: json['phone'] as String?,
      role: UserRole.fromString(json['role'] as String?),
      department: json['department'] as String? ?? 'Computer Science & AI',
      studentId: json['student_id'] as String? ?? json['roll_no'] as String? ?? 'US-2026-042',
      avatarUrl: json['avatar_url'] as String?,
      enrolledYear: json['enrolled_year'] as String? ?? '2024 - 2028',
      gpa: (json['gpa'] as num?)?.toDouble() ?? 3.82,
      attendanceRate: (json['attendance_rate'] as num?)?.toDouble() ?? 94.5,
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'name': name,
      'email': email,
      'phone': phone,
      'role': role.name,
      'department': department,
      'student_id': studentId,
      'avatar_url': avatarUrl,
      'enrolled_year': enrolledYear,
      'gpa': gpa,
      'attendance_rate': attendanceRate,
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
    );
  }
}
