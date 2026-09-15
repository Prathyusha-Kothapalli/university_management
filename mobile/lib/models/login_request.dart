class LoginRequest {
  final String email;
  final String password;
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
  final bool rememberMe;
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
  final bool rememberMe;
=======
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
  final bool rememberMe;
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689

  const LoginRequest({
    required this.email,
    required this.password,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
    this.rememberMe = false,
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
    this.rememberMe = false,
=======
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
    this.rememberMe = false,
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
  });

  Map<String, dynamic> toJson() {
    return {
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
      'username': email, // standard OAuth2 / FastAPI form compatibility
      'email': email,
      'password': password,
      'remember_me': rememberMe,
    };
  }
=======
>>>>>>> origin/web
      'email': email,
      'password': password,
    };
  }

  factory LoginRequest.fromJson(Map<String, dynamic> json) {
    return LoginRequest(
      email: json['email'] as String? ?? '',
      password: json['password'] as String? ?? '',
    );
  }
<<<<<<< HEAD
=======
      'username': email, // standard OAuth2 / FastAPI form compatibility
=======
      'username': email,
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
      'email': email,
      'password': password,
      'remember_me': rememberMe,
    };
  }
<<<<<<< HEAD
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======

  factory LoginRequest.fromJson(Map<String, dynamic> json) {
    return LoginRequest(
      email: (json['email'] ?? json['username']) as String? ?? '',
      password: json['password'] as String? ?? '',
      rememberMe: json['remember_me'] as bool? ?? false,
    );
  }
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
}
