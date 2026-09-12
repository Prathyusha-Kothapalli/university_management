/// Generic API response wrapper.
class ApiResponse<T> {
  final bool success;
  final String? message;
  final T? data;
  final List<String>? errors;
  final String? error;
  final int? statusCode;

  const ApiResponse({
    required this.success,
    this.message,
    this.data,
    this.errors,
    this.error,
    this.statusCode,
  });

  factory ApiResponse.fromJson(
    Map<String, dynamic> json, [
    T Function(dynamic data)? fromJsonT,
  ]) {
    final isSuccess = json['success'] as bool? ??
        (json['status'] == 'success' || json['status'] == 'ok' || !json.containsKey('error'));

    dynamic rawData = json['data'] ?? json['result'];
    T? parsedData;
    if (rawData != null && fromJsonT != null) {
      parsedData = fromJsonT(rawData);
    } else if (rawData != null && rawData is T) {
      parsedData = rawData;
    }

    final errString = json['error']?.toString() ?? json['detail']?.toString();
    List<String>? errList;
    if (json['errors'] is List) {
      errList = (json['errors'] as List).map((e) => e.toString()).toList();
    } else if (errString != null) {
      errList = [errString];
    }

    return ApiResponse<T>(
      success: isSuccess,
      message: json['message'] as String?,
      data: parsedData,
      errors: errList,
      error: errString,
      statusCode: (json['status_code'] as num?)?.toInt(),
    );
  }

  factory ApiResponse.success(T data, {String? message, int? statusCode}) {
    return ApiResponse(
      success: true,
      data: data,
      message: message,
      statusCode: statusCode ?? 200,
    );
  }

  factory ApiResponse.failure(String error, {int? statusCode}) {
    return ApiResponse(
      success: false,
      error: error,
      message: error,
      errors: [error],
      statusCode: statusCode ?? 400,
    );
  }

  Map<String, dynamic> toJson([Map<String, dynamic> Function(T data)? toJsonT]) {
    return {
      'success': success,
      'message': message,
      'data': data != null && toJsonT != null ? toJsonT(data as T) : data,
      'errors': errors,
      'error': error,
      'status_code': statusCode,
    };
  }
}
