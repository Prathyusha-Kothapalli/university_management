<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> origin/web
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
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
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
class User {
  final String id;
  final String name;
  final String email;
  final String? phone;
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
  final String role; // 'student', 'faculty', 'admin'
  final String? department;
  final String? studentId;
  final String? avatarUrl;
  final DateTime? createdAt;
=======
>>>>>>> origin/web
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
  final UserRole role;
  final String? department;
  final String? studentId;
  final String? avatarUrl;
  final String? enrolledYear;
  final double? gpa;
  final double? attendanceRate;
<<<<<<< HEAD
<<<<<<< HEAD
=======
  final String role; // 'student', 'faculty', 'admin'
  final String? department;
  final String? studentId;
  final String? avatarUrl;
  final DateTime? createdAt;
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
  final DateTime? createdAt;
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689

  const User({
    required this.id,
    required this.name,
    required this.email,
    this.phone,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
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
<<<<<<< HEAD
=======
=======
>>>>>>> origin/web
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
<<<<<<< HEAD
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
=======
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
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
      createdAt: json['created_at'] != null ? DateTime.tryParse(json['created_at'].toString()) : null,
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'name': name,
      'full_name': name,
      'email': email,
      'phone': phone,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
      'role': role,
      'department': department,
      'student_id': studentId,
      'avatar_url': avatarUrl,
      'created_at': createdAt?.toIso8601String(),
=======
>>>>>>> origin/web
      'role': role.name,
=======
      'role': role.roleString,
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
      'department': department,
      'student_id': studentId,
      'avatar_url': avatarUrl,
      'enrolled_year': enrolledYear,
      'gpa': gpa,
      'attendance_rate': attendanceRate,
<<<<<<< HEAD
<<<<<<< HEAD
=======
      'role': role,
      'department': department,
      'student_id': studentId,
      'avatar_url': avatarUrl,
      'created_at': createdAt?.toIso8601String(),
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
      'created_at': createdAt?.toIso8601String(),
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
    };
  }

  User copyWith({
    String? id,
    String? name,
    String? email,
    String? phone,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
    String? role,
    String? department,
    String? studentId,
    String? avatarUrl,
    DateTime? createdAt,
=======
>>>>>>> origin/web
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
    UserRole? role,
    String? department,
    String? studentId,
    String? avatarUrl,
    String? enrolledYear,
    double? gpa,
    double? attendanceRate,
<<<<<<< HEAD
<<<<<<< HEAD
=======
    String? role,
    String? department,
    String? studentId,
    String? avatarUrl,
    DateTime? createdAt,
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
    DateTime? createdAt,
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
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
<<<<<<< HEAD
<<<<<<< HEAD
      enrolledYear: enrolledYear ?? this.enrolledYear,
      gpa: gpa ?? this.gpa,
      attendanceRate: attendanceRate ?? this.attendanceRate,
    );
  }
=======
=======
>>>>>>> origin/web
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
<<<<<<< HEAD
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
=======
      enrolledYear: enrolledYear ?? this.enrolledYear,
      gpa: gpa ?? this.gpa,
      attendanceRate: attendanceRate ?? this.attendanceRate,
    );
  }
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
      enrolledYear: enrolledYear ?? this.enrolledYear,
      gpa: gpa ?? this.gpa,
      attendanceRate: attendanceRate ?? this.attendanceRate,
      createdAt: createdAt ?? this.createdAt,
    );
  }
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
}
