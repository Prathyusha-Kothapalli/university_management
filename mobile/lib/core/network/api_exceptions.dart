<<<<<<< HEAD
class ApiException implements Exception {
  final String message;
  final int? statusCode;
  final dynamic data;

  const ApiException({
    required this.message,
    this.statusCode,
    this.data,
  });

  @override
  String toString() => 'ApiException: $message (Status: $statusCode)';
}

class NetworkException extends ApiException {
  const NetworkException({
    String message = 'Unable to connect to the server. Please check your internet connection.',
  }) : super(message: message, statusCode: null);
}

class TimeoutException extends ApiException {
  const TimeoutException({
    String message = 'The server took too long to respond. Please try again.',
  }) : super(message: message, statusCode: 408);
}

class UnauthorizedException extends ApiException {
  const UnauthorizedException({
    String message = 'Your session has expired or credentials are invalid. Please log in again.',
    dynamic data,
  }) : super(message: message, statusCode: 401, data: data);
}

class ForbiddenException extends ApiException {
  const ForbiddenException({
    String message = 'You do not have permission to perform this action.',
  }) : super(message: message, statusCode: 403);
}

class NotFoundException extends ApiException {
  const NotFoundException({
    String message = 'The requested resource was not found.',
  }) : super(message: message, statusCode: 404);
}

class ValidationException extends ApiException {
  final Map<String, dynamic>? errors;

  const ValidationException({
    String message = 'Validation failed. Please check the entered information.',
    this.errors,
  }) : super(message: message, statusCode: 422, data: errors);
}

class ServerException extends ApiException {
  const ServerException({
    String message = 'The server encountered an error. Please try again later.',
    int? statusCode,
  }) : super(message: message, statusCode: statusCode ?? 500);
=======
/// Base class for all API and Network exceptions.
class ApiException implements Exception {
  final String message;
  final int? statusCode;
  final dynamic details;

  const ApiException(this.message, {this.statusCode, this.details});

  @override
  String toString() => message;
}

/// Thrown when device has no network connection.
class NetworkException extends ApiException {
  const NetworkException([String message = 'No internet connection. Please check your network.'])
      : super(message, statusCode: 0);
}

/// Thrown on HTTP request timeout.
class TimeoutException extends ApiException {
  const TimeoutException([String message = 'The connection has timed out. Please try again.'])
      : super(message, statusCode: 408);
}

/// Thrown when user credentials or token are invalid/expired (HTTP 401).
class UnauthorizedException extends ApiException {
  const UnauthorizedException([String message = 'Invalid credentials or session expired.'])
      : super(message, statusCode: 401);
}

/// Thrown when user lacks permission to access resource (HTTP 403).
class ForbiddenException extends ApiException {
  const ForbiddenException([String message = 'Access denied. You do not have permission.'])
      : super(message, statusCode: 403);
}

/// Thrown when resource is not found (HTTP 404).
class NotFoundException extends ApiException {
  const NotFoundException([String message = 'Requested resource was not found on the server.'])
      : super(message, statusCode: 404);
}

/// Thrown on backend 5xx errors.
class ServerException extends ApiException {
  const ServerException([String message = 'Server encountered an error. Please try again later.'])
      : super(message, statusCode: 500);
}

/// Thrown on 400 or 422 validation errors.
class ValidationException extends ApiException {
  final Map<String, List<String>> errors;

  const ValidationException(
    String message, {
    this.errors = const {},
  }) : super(message, statusCode: 422);
>>>>>>> 29907a7 (added flutter)
}
