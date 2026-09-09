import 'dart:async';
import 'dart:convert';
import 'dart:io';
import 'package:http/http.dart' as http;

import '../constants/api_constants.dart';
import 'api_exceptions.dart';

typedef TokenProvider = Future<String?> Function();

class ApiClient {
  final String baseUrl;
  final http.Client _httpClient;
  final TokenProvider? tokenProvider;

  ApiClient({
    String? baseUrl,
    http.Client? httpClient,
    this.tokenProvider,
  })  : baseUrl = baseUrl ?? ApiConstants.API_BASE_URL,
        _httpClient = httpClient ?? http.Client();

  Uri _buildUri(String path, [Map<String, dynamic>? queryParameters]) {
    final cleanBase = baseUrl.endsWith('/') ? baseUrl.substring(0, baseUrl.length - 1) : baseUrl;
    final cleanPath = path.startsWith('/') ? path : '/$path';
    final fullUrl = '$cleanBase$cleanPath';
    final uri = Uri.parse(fullUrl);

    if (queryParameters != null && queryParameters.isNotEmpty) {
      return uri.replace(
        queryParameters: queryParameters.map((k, v) => MapEntry(k, v.toString())),
      );
    }
    return uri;
  }

  Future<Map<String, String>> _buildHeaders([Map<String, String>? customHeaders]) async {
    final headers = <String, String>{
      ApiConstants.headerContentType: ApiConstants.contentTypeJson,
      'Accept': ApiConstants.contentTypeJson,
    };

    if (tokenProvider != null) {
      final token = await tokenProvider!();
      if (token != null && token.isNotEmpty) {
        headers[ApiConstants.headerAuthorization] = '${ApiConstants.bearerPrefix}$token';
      }
    }

    if (customHeaders != null) {
      headers.addAll(customHeaders);
    }
    return headers;
  }

  Future<dynamic> get(
    String path, {
    Map<String, dynamic>? queryParameters,
    Map<String, String>? headers,
  }) async {
    final uri = _buildUri(path, queryParameters);
    final requestHeaders = await _buildHeaders(headers);

    try {
      final response = await _httpClient
          .get(uri, headers: requestHeaders)
          .timeout(ApiConstants.receiveTimeout);
      return _processResponse(response);
    } on SocketException {
      throw const NetworkException();
    } on TimeoutException {
      throw const TimeoutException();
    } on http.ClientException {
      throw const NetworkException();
    }
  }

  Future<dynamic> post(
    String path, {
    dynamic body,
    Map<String, String>? headers,
  }) async {
    final uri = _buildUri(path);
    final requestHeaders = await _buildHeaders(headers);

    try {
      final response = await _httpClient
          .post(
            uri,
            headers: requestHeaders,
            body: body != null ? jsonEncode(body) : null,
          )
          .timeout(ApiConstants.connectTimeout);
      return _processResponse(response);
    } on SocketException {
      throw const NetworkException();
    } on TimeoutException {
      throw const TimeoutException();
    } on http.ClientException {
      throw const NetworkException();
    }
  }

  Future<dynamic> put(
    String path, {
    dynamic body,
    Map<String, String>? headers,
  }) async {
    final uri = _buildUri(path);
    final requestHeaders = await _buildHeaders(headers);

    try {
      final response = await _httpClient
          .put(
            uri,
            headers: requestHeaders,
            body: body != null ? jsonEncode(body) : null,
          )
          .timeout(ApiConstants.connectTimeout);
      return _processResponse(response);
    } on SocketException {
      throw const NetworkException();
    } on TimeoutException {
      throw const TimeoutException();
    } on http.ClientException {
      throw const NetworkException();
    }
  }

  Future<dynamic> delete(
    String path, {
    dynamic body,
    Map<String, String>? headers,
  }) async {
    final uri = _buildUri(path);
    final requestHeaders = await _buildHeaders(headers);

    try {
      final response = await _httpClient
          .delete(
            uri,
            headers: requestHeaders,
            body: body != null ? jsonEncode(body) : null,
          )
          .timeout(ApiConstants.connectTimeout);
      return _processResponse(response);
    } on SocketException {
      throw const NetworkException();
    } on TimeoutException {
      throw const TimeoutException();
    } on http.ClientException {
      throw const NetworkException();
    }
  }

  dynamic _processResponse(http.Response response) {
    dynamic jsonBody;
    if (response.body.isNotEmpty) {
      try {
        jsonBody = jsonDecode(response.body);
      } catch (_) {
        jsonBody = response.body;
      }
    }

    final statusCode = response.statusCode;
    if (statusCode >= 200 && statusCode < 300) {
      return jsonBody;
    }

    String errorMessage = 'Server request failed';
    if (jsonBody is Map<String, dynamic>) {
      if (jsonBody.containsKey('message')) {
        errorMessage = jsonBody['message'].toString();
      } else if (jsonBody.containsKey('detail')) {
        errorMessage = jsonBody['detail'].toString();
      } else if (jsonBody.containsKey('error')) {
        errorMessage = jsonBody['error'].toString();
      }
    }

    switch (statusCode) {
      case 400:
        throw ApiException(message: errorMessage, statusCode: 400, data: jsonBody);
      case 401:
        throw UnauthorizedException(message: errorMessage, data: jsonBody);
      case 403:
        throw ForbiddenException(message: errorMessage);
      case 404:
        throw NotFoundException(message: errorMessage);
      case 422:
        Map<String, dynamic>? errors;
        if (jsonBody is Map<String, dynamic> && jsonBody['errors'] is Map) {
          errors = Map<String, dynamic>.from(jsonBody['errors']);
        }
        throw ValidationException(message: errorMessage, errors: errors);
      case 500:
      case 502:
      case 503:
      case 504:
        throw ServerException(message: errorMessage, statusCode: statusCode);
      default:
        throw ApiException(message: errorMessage, statusCode: statusCode, data: jsonBody);
    }
  }

  void close() {
    _httpClient.close();
  }
}
