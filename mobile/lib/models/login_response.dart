import 'user.dart';

class LoginResponse {
  final String accessToken;
<<<<<<< HEAD
<<<<<<< HEAD
  final String? refreshToken;
  final String? tokenType;
  final int? expiresIn;
  final User? user;

  const LoginResponse({
    required this.accessToken,
    this.refreshToken,
    this.tokenType = 'Bearer',
    this.expiresIn,
    this.user,
  });

  factory LoginResponse.fromJson(Map<String, dynamic> json) {
    // Handle either direct token or nested data
    final data = json['data'] is Map<String, dynamic> ? json['data'] as Map<String, dynamic> : json;

    return LoginResponse(
      accessToken: data['access_token'] as String? ?? data['token'] as String? ?? '',
      refreshToken: data['refresh_token'] as String?,
      tokenType: data['token_type'] as String? ?? 'Bearer',
      expiresIn: data['expires_in'] as int?,
      user: data['user'] is Map<String, dynamic>
          ? User.fromJson(data['user'] as Map<String, dynamic>)
          : null,
=======
=======
>>>>>>> origin/web
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
<<<<<<< HEAD
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
=======
  final String? refreshToken;
  final String? tokenType;
  final int? expiresIn;
  final User? user;

  const LoginResponse({
    required this.accessToken,
    this.refreshToken,
    this.tokenType = 'Bearer',
    this.expiresIn,
    this.user,
  });

  factory LoginResponse.fromJson(Map<String, dynamic> json) {
    // Handle either direct token or nested data
    final data = json['data'] is Map<String, dynamic> ? json['data'] as Map<String, dynamic> : json;

    return LoginResponse(
      accessToken: data['access_token'] as String? ?? data['token'] as String? ?? '',
      refreshToken: data['refresh_token'] as String?,
      tokenType: data['token_type'] as String? ?? 'Bearer',
      expiresIn: data['expires_in'] as int?,
      user: data['user'] is Map<String, dynamic>
          ? User.fromJson(data['user'] as Map<String, dynamic>)
          : null,
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'access_token': accessToken,
<<<<<<< HEAD
<<<<<<< HEAD
=======
      'token_type': tokenType,
      'expires_in': expiresIn,
      'user': user.toJson(),
=======
>>>>>>> origin/web
      'refresh_token': refreshToken,
      'token_type': tokenType,
      'expires_in': expiresIn,
      'user': user?.toJson(),
<<<<<<< HEAD
=======
      'token_type': tokenType,
      'expires_in': expiresIn,
      'user': user.toJson(),
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
    };
  }
}
