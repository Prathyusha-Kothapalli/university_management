class RegisterRequest {
  final String name;
  final String email;
  final String phone;
  final String password;
  final String role;
<<<<<<< HEAD
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
=======
  final String? department;
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689

  const RegisterRequest({
    required this.name,
    required this.email,
    required this.phone,
    required this.password,
    this.role = 'student',
<<<<<<< HEAD
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
=======
    this.department,
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
  });

  Map<String, dynamic> toJson() {
    return {
      'name': name,
<<<<<<< HEAD
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
=======
      'full_name': name,
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
      'email': email,
      'phone': phone,
      'password': password,
      'role': role,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
      'department': department,
    };
  }
=======
>>>>>>> origin/web
=======
      'department': department,
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
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
<<<<<<< HEAD
<<<<<<< HEAD
=======
      'department': department,
    };
  }
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
}
