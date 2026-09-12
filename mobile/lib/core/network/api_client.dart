import 'dart:async';
import 'dart:convert';
import 'dart:io';
import 'package:http/http.dart' as http;

import '../constants/api_constants.dart';
import '../../services/token_storage_service.dart';
import 'api_exceptions.dart';

/// Centralized HTTP API Client with JSON handling and exception translation.
class ApiClient {
  final String baseUrl;
  final TokenStorageService tokenStorage;
  final http.Client _httpClient;

  ApiClient({
    String? baseUrl,
    TokenStorageService? tokenStorage,
    http.Client? httpClient,
  })  : baseUrl = baseUrl ?? ApiConstants.apiBaseUrl,
        tokenStorage = tokenStorage ?? TokenStorageService(),
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

  Future<Map<String, String>> _buildHeaders(Map<String, String>? customHeaders) async {
    final headers = <String, String>{
      'Content-Type': 'application/json; charset=UTF-8',
      'Accept': 'application/json',
    };

    final token = await tokenStorage.getToken();
    if (token != null && token.isNotEmpty) {
      headers['Authorization'] = 'Bearer $token';
    }

    if (customHeaders != null) {
      headers.addAll(customHeaders);
    }
    return headers;
  }

  dynamic _processResponse(http.Response response) {
    final statusCode = response.statusCode;
    dynamic jsonBody;

    if (response.body.isNotEmpty) {
      try {
        jsonBody = jsonDecode(response.body);
      } catch (_) {
        jsonBody = response.body;
      }
    }

    if (statusCode >= 200 && statusCode < 300) {
      return jsonBody;
    }

    String message = 'Request failed with status: $statusCode';
    if (jsonBody is Map<String, dynamic>) {
      if (jsonBody.containsKey('detail')) {
        final detail = jsonBody['detail'];
        message = detail is String ? detail : detail.toString();
      } else if (jsonBody.containsKey('message')) {
        message = jsonBody['message'].toString();
      }
    }

    switch (statusCode) {
      case 400:
      case 422:
        Map<String, dynamic>? errors;
        if (jsonBody is Map<String, dynamic> && jsonBody.containsKey('errors')) {
          errors = jsonBody['errors'] as Map<String, dynamic>?;
        }
        throw ValidationException(message, errors);
      case 401:
        throw UnauthorizedException(message, jsonBody);
      case 403:
        throw ForbiddenException(message);
      case 404:
        throw NotFoundException(message);
      case 408:
        throw TimeoutException(message);
      case 500:
      case 502:
      case 503:
        throw ServerException(message, statusCode);
      default:
        throw ApiException(message, statusCode, jsonBody, jsonBody);
    }
  }

  Future<dynamic> get(
    String endpoint, {
    Map<String, dynamic>? queryParameters,
    Map<String, String>? headers,
  }) async {
    final uri = _buildUri(endpoint, queryParameters);
    try {
      final requestHeaders = await _buildHeaders(headers);
      final response = await _httpClient
          .get(uri, headers: requestHeaders)
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

  Future<dynamic> post(
    String endpoint, {
    dynamic body,
    Map<String, dynamic>? queryParameters,
    Map<String, String>? headers,
  }) async {
    final uri = _buildUri(endpoint, queryParameters);
    try {
      final requestHeaders = await _buildHeaders(headers);
      final encodedBody = body != null ? jsonEncode(body) : null;
      final response = await _httpClient
          .post(uri, headers: requestHeaders, body: encodedBody)
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
    String endpoint, {
    dynamic body,
    Map<String, dynamic>? queryParameters,
    Map<String, String>? headers,
  }) async {
    final uri = _buildUri(endpoint, queryParameters);
    try {
      final requestHeaders = await _buildHeaders(headers);
      final encodedBody = body != null ? jsonEncode(body) : null;
      final response = await _httpClient
          .put(uri, headers: requestHeaders, body: encodedBody)
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
    String endpoint, {
    Map<String, dynamic>? queryParameters,
    Map<String, String>? headers,
  }) async {
    final uri = _buildUri(endpoint, queryParameters);
    try {
      final requestHeaders = await _buildHeaders(headers);
      final response = await _httpClient
          .delete(uri, headers: requestHeaders)
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

  void close() {
    _httpClient.close();
  }
}
