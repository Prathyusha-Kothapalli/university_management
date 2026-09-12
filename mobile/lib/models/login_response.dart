import 'user.dart';

class LoginResponse {
  final String accessToken;
  final String? refreshToken;
  final String tokenType;
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
    final data = json['data'] is Map<String, dynamic> ? json['data'] as Map<String, dynamic> : json;

    final token = data['access_token']?.toString() ??
        data['token']?.toString() ??
        data['accessToken']?.toString() ??
        '';

    final refreshToken = data['refresh_token']?.toString();
    final tokenType = data['token_type']?.toString() ?? 'Bearer';
    final expiresIn = (data['expires_in'] as num?)?.toInt();

    User? parsedUser;
    if (data['user'] is Map<String, dynamic>) {
      parsedUser = User.fromJson(data['user'] as Map<String, dynamic>);
    } else if (data.containsKey('email')) {
      parsedUser = User.fromJson(data);
    }

    return LoginResponse(
      accessToken: token,
      refreshToken: refreshToken,
      tokenType: tokenType,
      expiresIn: expiresIn,
      user: parsedUser,
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'access_token': accessToken,
      'refresh_token': refreshToken,
      'token_type': tokenType,
      'expires_in': expiresIn,
      'user': user?.toJson(),
    };
  }
}
