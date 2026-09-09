class LoginRequest {
  final String email;
  final String password;
<<<<<<< HEAD
=======
  final bool rememberMe;
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd

  const LoginRequest({
    required this.email,
    required this.password,
<<<<<<< HEAD
=======
    this.rememberMe = false,
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
  });

  Map<String, dynamic> toJson() {
    return {
<<<<<<< HEAD
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
=======
      'username': email, // standard OAuth2 / FastAPI form compatibility
      'email': email,
      'password': password,
      'remember_me': rememberMe,
    };
  }
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
}
