class RegisterRequest {
  final String name;
  final String email;
  final String phone;
  final String password;
  final String role;
<<<<<<< HEAD
  final String? department;
=======
>>>>>>> 29907a7 (added flutter)

  const RegisterRequest({
    required this.name,
    required this.email,
    required this.phone,
    required this.password,
    this.role = 'student',
<<<<<<< HEAD
    this.department,
=======
>>>>>>> 29907a7 (added flutter)
  });

  Map<String, dynamic> toJson() {
    return {
      'name': name,
<<<<<<< HEAD
      'full_name': name,
=======
>>>>>>> 29907a7 (added flutter)
      'email': email,
      'phone': phone,
      'password': password,
      'role': role,
<<<<<<< HEAD
      'department': department,
    };
  }
=======
    };
  }

  factory RegisterRequest.fromJson(Map<String, dynamic> json) {
    return RegisterRequest(
      name: json['name'] as String? ?? '',
      email: json['email'] as String? ?? '',
      phone: json['phone'] as String? ?? '',
      password: json['password'] as String? ?? '',
      role: json['role'] as String? ?? 'student',
    );
  }
>>>>>>> 29907a7 (added flutter)
}
