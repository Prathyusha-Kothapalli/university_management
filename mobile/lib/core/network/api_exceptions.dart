/// Base class for all API and Network exceptions.
class ApiException implements Exception {
  final String message;
  final int? statusCode;
  final dynamic details;
  final dynamic data;

  const ApiException([
    this.message = 'An error occurred. Please try again.',
    this.statusCode,
    this.details,
    this.data,
  ]);

  @override
  String toString() => message;
}

/// Thrown when device has no network connection.
class NetworkException extends ApiException {
  const NetworkException([
    String message = 'Unable to connect to the server. Please check your network connection.',
  ]) : super(message, 0);
}

/// Thrown on HTTP request timeout.
class TimeoutException extends ApiException {
  const TimeoutException([
    String message = 'The connection has timed out. Please try again.',
  ]) : super(message, 408);
}

/// Thrown when user credentials or token are invalid/expired (HTTP 401).
class UnauthorizedException extends ApiException {
  const UnauthorizedException([
    String message = 'Invalid credentials or session expired. Please log in again.',
    dynamic data,
  ]) : super(message, 401, null, data);
}

/// Thrown when user lacks permission to access resource (HTTP 403).
class ForbiddenException extends ApiException {
  const ForbiddenException([
    String message = 'Access denied. You do not have permission to perform this action.',
  ]) : super(message, 403);
}

/// Thrown when resource is not found (HTTP 404).
class NotFoundException extends ApiException {
  const NotFoundException([
    String message = 'Requested resource was not found on the server.',
  ]) : super(message, 404);
}

/// Thrown on 400 or 422 validation errors.
class ValidationException extends ApiException {
  final Map<String, dynamic>? errors;

  const ValidationException([
    String message = 'Validation failed. Please verify your input.',
    this.errors,
  ]) : super(message, 422, errors, errors);
}

/// Thrown on backend 5xx errors.
class ServerException extends ApiException {
  const ServerException([
    String message = 'Server encountered an error. Please try again later.',
    int? statusCode,
  ]) : super(message, statusCode ?? 500);
}
