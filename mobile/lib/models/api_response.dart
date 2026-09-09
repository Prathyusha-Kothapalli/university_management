class ApiResponse<T> {
  final bool success;
  final String? message;
  final T? data;
  final String? error;
  final int? statusCode;

  const ApiResponse({
    required this.success,
    this.message,
    this.data,
    this.error,
    this.statusCode,
  });

  factory ApiResponse.fromJson(
    Map<String, dynamic> json,
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
  }
}
