class RegisterRequest {
  final String name;
  final String email;
  final String phone;
  final String password;
  final String role;
<<<<<<< HEAD
<<<<<<< HEAD
=======
  final String? department;
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
  final String? department;
=======
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web

  const RegisterRequest({
    required this.name,
    required this.email,
    required this.phone,
    required this.password,
    this.role = 'student',
<<<<<<< HEAD
<<<<<<< HEAD
=======
    this.department,
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
    this.department,
=======
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
  });

  Map<String, dynamic> toJson() {
    return {
      'name': name,
<<<<<<< HEAD
<<<<<<< HEAD
=======
      'full_name': name,
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
      'full_name': name,
=======
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
      'email': email,
      'phone': phone,
      'password': password,
      'role': role,
<<<<<<< HEAD
<<<<<<< HEAD
=======
      'department': department,
    };
  }
=======
>>>>>>> origin/web
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
<<<<<<< HEAD
=======
      'department': department,
    };
  }
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
}
