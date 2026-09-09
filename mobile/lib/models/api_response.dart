<<<<<<< HEAD
/// Generic API response wrapper.
=======
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
class ApiResponse<T> {
  final bool success;
  final String? message;
  final T? data;
<<<<<<< HEAD
  final List<String>? errors;
=======
  final String? error;
  final int? statusCode;
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd

  const ApiResponse({
    required this.success,
    this.message,
    this.data,
<<<<<<< HEAD
    this.errors,
=======
    this.error,
    this.statusCode,
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
  });

  factory ApiResponse.fromJson(
    Map<String, dynamic> json,
<<<<<<< HEAD
    T Function(dynamic data)? fromJsonT,
  ) {
    return ApiResponse(
      success: json['success'] as bool? ?? true,
      message: json['message'] as String?,
      data: json['data'] != null && fromJsonT != null
          ? fromJsonT(json['data'])
          : json['data'] as T?,
      errors: (json['errors'] as List<dynamic>?)?.map((e) => e.toString()).toList(),
    );
  }

  Map<String, dynamic> toJson(Map<String, dynamic> Function(T data)? toJsonT) {
    return {
      'success': success,
      'message': message,
      'data': data != null && toJsonT != null ? toJsonT(data as T) : data,
      'errors': errors,
    };
=======
    T Function(dynamic json) fromJsonT,
  ) {
    final isSuccess = json['success'] as bool? ??
        (json['status'] == 'success' || json['status'] == 'ok' || !json.containsKey('error'));

    dynamic dataJson = json['data'] ?? json['result'] ?? json;

    return ApiResponse<T>(
      success: isSuccess,
      message: json['message']?.toString(),
      data: dataJson != null ? fromJsonT(dataJson) : null,
      error: json['error']?.toString() ?? json['detail']?.toString(),
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
      statusCode: statusCode ?? 400,
    );
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
  }
}
