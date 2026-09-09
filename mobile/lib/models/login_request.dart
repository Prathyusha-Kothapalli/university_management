class LoginRequest {
  final String email;
  final String password;
  final bool rememberMe;

  const LoginRequest({
    required this.email,
    required this.password,
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
}
