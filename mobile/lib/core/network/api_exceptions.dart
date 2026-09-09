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
}
