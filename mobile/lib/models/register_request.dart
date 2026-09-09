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
}
