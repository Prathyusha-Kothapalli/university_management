class LoginRequest {
  final String email;
  final String password;
  final bool rememberMe;
  final bool rememberMe;
  final bool rememberMe;

  const LoginRequest({
    required this.email,
    required this.password,
    this.rememberMe = false,
    this.rememberMe = false,
    this.rememberMe = false,
  });

  Map<String, dynamic> toJson() {
    return {
      'username': email, // standard OAuth2 / FastAPI form compatibility
      'email': email,
      'password': password,
      'remember_me': rememberMe,
    };
  }
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
      'username': email, // standard OAuth2 / FastAPI form compatibility
      'username': email,
      'email': email,
      'password': password,
      'remember_me': rememberMe,
    };
  }

  factory LoginRequest.fromJson(Map<String, dynamic> json) {
    return LoginRequest(
      email: (json['email'] ?? json['username']) as String? ?? '',
      password: json['password'] as String? ?? '',
      rememberMe: json['remember_me'] as bool? ?? false,
    );
  }
}
