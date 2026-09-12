class RegisterRequest {
  final String name;
  final String email;
  final String phone;
  final String password;
  final String role;
  final String? department;

  const RegisterRequest({
    required this.name,
    required this.email,
    required this.phone,
    required this.password,
    this.role = 'student',
    this.department,
  });

  Map<String, dynamic> toJson() {
    return {
      'name': name,
      'full_name': name,
      'email': email,
      'phone': phone,
      'password': password,
      'role': role,
      'department': department,
    };
  }

  factory RegisterRequest.fromJson(Map<String, dynamic> json) {
    return RegisterRequest(
      name: (json['name'] ?? json['full_name']) as String? ?? '',
      email: json['email'] as String? ?? '',
      phone: json['phone'] as String? ?? '',
      password: json['password'] as String? ?? '',
      role: json['role'] as String? ?? 'student',
      department: json['department'] as String?,
    );
  }
}
