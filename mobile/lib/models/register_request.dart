class RegisterRequest {
  final String name;
  final String email;
  final String phone;
  final String password;
  final String role;
<<<<<<< HEAD
=======
  final String? department;
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd

  const RegisterRequest({
    required this.name,
    required this.email,
    required this.phone,
    required this.password,
    this.role = 'student',
<<<<<<< HEAD
=======
    this.department,
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
  });

  Map<String, dynamic> toJson() {
    return {
      'name': name,
<<<<<<< HEAD
=======
      'full_name': name,
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
      'email': email,
      'phone': phone,
      'password': password,
      'role': role,
<<<<<<< HEAD
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
=======
      'department': department,
    };
  }
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
}
