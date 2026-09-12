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
