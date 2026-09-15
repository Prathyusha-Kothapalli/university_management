<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
/// Generic API response wrapper.
=======
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
=======
/// Generic API response wrapper.
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
/// Generic API response wrapper.
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
class ApiResponse<T> {
  final bool success;
  final String? message;
  final T? data;
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
  final List<String>? errors;
  final String? error;
  final int? statusCode;
<<<<<<< HEAD
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
  final String? error;
  final int? statusCode;
=======
  final List<String>? errors;
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689

  const ApiResponse({
    required this.success,
    this.message,
    this.data,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
    this.errors,
    this.error,
    this.statusCode,
<<<<<<< HEAD
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
    this.error,
    this.statusCode,
=======
    this.errors,
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
  });

  factory ApiResponse.fromJson(
    Map<String, dynamic> json,
<<<<<<< HEAD
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
=======
>>>>>>> origin/web
    T Function(dynamic json) fromJsonT,
  ) {
=======
  });

  factory ApiResponse.fromJson(
    Map<String, dynamic> json, [
    T Function(dynamic data)? fromJsonT,
  ]) {
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
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
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
=======
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
=======
  }

  Map<String, dynamic> toJson([Map<String, dynamic> Function(T data)? toJsonT]) {
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
    return {
      'success': success,
      'message': message,
      'data': data != null && toJsonT != null ? toJsonT(data as T) : data,
      'errors': errors,
<<<<<<< HEAD
    };
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
      'error': error,
      'status_code': statusCode,
    };
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
  }
}
