class LoginRequest {
  final String email;
  final String password;
<<<<<<< HEAD
  final bool rememberMe;
=======
>>>>>>> 29907a7 (added flutter)

  const LoginRequest({
    required this.email,
    required this.password,
<<<<<<< HEAD
    this.rememberMe = false,
=======
>>>>>>> 29907a7 (added flutter)
  });

  Map<String, dynamic> toJson() {
    return {
<<<<<<< HEAD
      'username': email, // standard OAuth2 / FastAPI form compatibility
      'email': email,
      'password': password,
      'remember_me': rememberMe,
    };
  }
=======
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
>>>>>>> 29907a7 (added flutter)
}
