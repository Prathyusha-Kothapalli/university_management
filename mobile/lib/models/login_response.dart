import 'user.dart';

class LoginResponse {
  final String accessToken;
  final String tokenType;
  final int? expiresIn;
  final User user;

  const LoginResponse({
    required this.accessToken,
    this.tokenType = 'bearer',
    this.expiresIn,
    required this.user,
  });

  factory LoginResponse.fromJson(Map<String, dynamic> json) {
    // Support standard token responses: { access_token: ..., user: ... }
    // or nested format: { token: ..., data: { user: ... } }
    final token = json['access_token']?.toString() ??
        json['token']?.toString() ??
        json['accessToken']?.toString() ??
        '';

    final tokenType = json['token_type']?.toString() ?? 'bearer';
    final expiresIn = (json['expires_in'] as num?)?.toInt();

    final userJson = json['user'] is Map<String, dynamic>
        ? json['user'] as Map<String, dynamic>
        : (json['data'] is Map<String, dynamic> && (json['data'] as Map<String, dynamic>)['user'] is Map
            ? (json['data'] as Map<String, dynamic>)['user'] as Map<String, dynamic>
            : json);

    return LoginResponse(
      accessToken: token,
      tokenType: tokenType,
      expiresIn: expiresIn,
      user: User.fromJson(userJson),
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'access_token': accessToken,
      'token_type': tokenType,
      'expires_in': expiresIn,
      'user': user.toJson(),
    };
  }
}
