<<<<<<< HEAD
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
=======
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
class User {
  final String id;
  final String name;
  final String email;
  final String? phone;
<<<<<<< HEAD
  final UserRole role;
  final String? department;
  final String? studentId;
  final String? avatarUrl;
  final String? enrolledYear;
  final double? gpa;
  final double? attendanceRate;
=======
  final String role; // 'student', 'faculty', 'admin'
  final String? department;
  final String? studentId;
  final String? avatarUrl;
  final DateTime? createdAt;
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd

  const User({
    required this.id,
    required this.name,
    required this.email,
    this.phone,
<<<<<<< HEAD
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
=======
    this.role = 'student',
    this.department,
    this.studentId,
    this.avatarUrl,
    this.createdAt,
  });

  String get roleDisplay {
    if (role.isEmpty) return 'Student';
    return role[0].toUpperCase() + role.substring(1);
  }

  String get initials {
    if (name.trim().isEmpty) return 'U';
    final parts = name.trim().split(RegExp(r'\s+'));
    if (parts.length >= 2) {
      return '${parts[0][0]}${parts[1][0]}'.toUpperCase();
    }
    return parts[0][0].toUpperCase();
  }

  factory User.fromJson(Map<String, dynamic> json) {
    return User(
      id: json['id']?.toString() ?? '',
      name: json['name']?.toString() ?? json['full_name']?.toString() ?? '',
      email: json['email']?.toString() ?? '',
      phone: json['phone']?.toString(),
      role: json['role']?.toString() ?? 'student',
      department: json['department']?.toString(),
      studentId: json['student_id']?.toString() ?? json['studentId']?.toString(),
      avatarUrl: json['avatar_url']?.toString() ?? json['avatarUrl']?.toString(),
      createdAt: json['created_at'] != null ? DateTime.tryParse(json['created_at'].toString()) : null,
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'name': name,
      'email': email,
      'phone': phone,
<<<<<<< HEAD
      'role': role.name,
      'department': department,
      'student_id': studentId,
      'avatar_url': avatarUrl,
      'enrolled_year': enrolledYear,
      'gpa': gpa,
      'attendance_rate': attendanceRate,
=======
      'role': role,
      'department': department,
      'student_id': studentId,
      'avatar_url': avatarUrl,
      'created_at': createdAt?.toIso8601String(),
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
    };
  }

  User copyWith({
    String? id,
    String? name,
    String? email,
    String? phone,
<<<<<<< HEAD
    UserRole? role,
    String? department,
    String? studentId,
    String? avatarUrl,
    String? enrolledYear,
    double? gpa,
    double? attendanceRate,
=======
    String? role,
    String? department,
    String? studentId,
    String? avatarUrl,
    DateTime? createdAt,
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
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
<<<<<<< HEAD
      enrolledYear: enrolledYear ?? this.enrolledYear,
      gpa: gpa ?? this.gpa,
      attendanceRate: attendanceRate ?? this.attendanceRate,
    );
  }
=======
      createdAt: createdAt ?? this.createdAt,
    );
  }

  @override
  bool operator ==(Object other) =>
      identical(this, other) ||
      other is User &&
          runtimeType == other.runtimeType &&
          id == other.id &&
          email == other.email;

  @override
  int get hashCode => id.hashCode ^ email.hashCode;
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
}
