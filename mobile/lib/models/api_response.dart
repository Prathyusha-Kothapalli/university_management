/// Generic API response wrapper.

  const ApiResponse({
    required this.success,
    this.message,
    this.data,
    this.errors,
  });

  factory ApiResponse.fromJson(
    Map<String, dynamic> json,
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
  }
}
