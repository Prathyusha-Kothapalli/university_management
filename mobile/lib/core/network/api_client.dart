import 'dart:async';
import 'dart:convert';
import 'dart:io';
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
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
=======
>>>>>>> origin/web
=======
import 'package:http/http.dart' as http;
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689

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
<<<<<<< HEAD
        _httpClient = httpClient ??
            (HttpClient()
              ..connectionTimeout =
                  Duration(seconds: ApiConstants.connectTimeoutSeconds));

  Uri _buildUri(String endpoint, [Map<String, dynamic>? queryParams]) {
    final cleanBase = baseUrl.endsWith('/') ? baseUrl.substring(0, baseUrl.length - 1) : baseUrl;
    final cleanEndpoint = endpoint.startsWith('/') ? endpoint : '/$endpoint';
    final fullUrl = '$cleanBase$cleanEndpoint';

    final uri = Uri.parse(fullUrl);
    if (queryParams != null && queryParams.isNotEmpty) {
      final stringParams = queryParams.map((k, v) => MapEntry(k, v.toString()));
      return uri.replace(queryParameters: stringParams);
<<<<<<< HEAD
=======
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
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
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
<<<<<<< HEAD
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
    }
    return uri;
  }

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
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
=======
>>>>>>> origin/web
  Future<void> _applyHeaders(HttpClientRequest request, Map<String, String>? customHeaders) async {
    // Default headers
    request.headers.set(HttpHeaders.contentTypeHeader, 'application/json; charset=UTF-8');
    request.headers.set(HttpHeaders.acceptHeader, 'application/json');

    // Attach JWT Bearer Token if available
    final token = await tokenStorage.getToken();
    if (token != null && token.isNotEmpty) {
      request.headers.set(HttpHeaders.authorizationHeader, 'Bearer $token');
    }

    // Apply any custom headers
    if (customHeaders != null) {
      customHeaders.forEach((key, value) {
        request.headers.set(key, value);
      });
    }
  }

  Future<dynamic> _processResponse(HttpClientResponse response) async {
    final responseBody = await response.transform(utf8.decoder).join();
    final statusCode = response.statusCode;

    dynamic json;
    if (responseBody.isNotEmpty) {
      try {
        json = jsonDecode(responseBody);
      } catch (_) {
        json = {'message': responseBody};
      }
    } else {
      json = {};
    }

    if (statusCode >= 200 && statusCode < 300) {
      return json;
    }

    final message = (json is Map && json['message'] != null)
        ? json['message'].toString()
        : 'HTTP Error $statusCode';

    switch (statusCode) {
      case 401:
        await tokenStorage.deleteToken();
        throw UnauthorizedException(message);
      case 403:
        throw ForbiddenException(message);
      case 404:
        throw NotFoundException(message);
      case 422:
      case 400:
        throw ValidationException(message);
      case 500:
      case 502:
      case 503:
        throw ServerException(message);
      default:
        throw ApiException(message, statusCode: statusCode, details: json);
    }
  }

  /// Execute GET request
  Future<dynamic> get(
    String endpoint, {
    Map<String, dynamic>? queryParams,
    Map<String, String>? headers,
  }) async {
    try {
      final uri = _buildUri(endpoint, queryParams);
      final request = await _httpClient.getUrl(uri).timeout(
            Duration(seconds: ApiConstants.connectTimeoutSeconds),
          );
      await _applyHeaders(request, headers);

      final response = await request.close().timeout(
            Duration(seconds: ApiConstants.receiveTimeoutSeconds),
          );
      return await _processResponse(response);
    } on SocketException catch (e) {
      throw NetworkException('Unable to reach server: ${e.message}');
    } on TimeoutException {
      throw const TimeoutException('Request timed out. Please try again.');
    } on ApiException {
      rethrow;
    } catch (e) {
      throw ApiException('Unexpected network error: $e');
    }
  }

  /// Execute POST request
  Future<dynamic> post(
    String endpoint, {
    dynamic body,
    Map<String, String>? headers,
  }) async {
    try {
      final uri = _buildUri(endpoint);
      final request = await _httpClient.postUrl(uri).timeout(
            Duration(seconds: ApiConstants.connectTimeoutSeconds),
          );
      await _applyHeaders(request, headers);

      if (body != null) {
        final payload = body is String ? body : jsonEncode(body);
        request.write(payload);
      }

      final response = await request.close().timeout(
            Duration(seconds: ApiConstants.receiveTimeoutSeconds),
          );
      return await _processResponse(response);
    } on SocketException catch (e) {
      throw NetworkException('Unable to reach server: ${e.message}');
    } on TimeoutException {
      throw const TimeoutException('Request timed out. Please try again.');
    } on ApiException {
      rethrow;
    } catch (e) {
      throw ApiException('Unexpected network error: $e');
    }
  }

  /// Execute PUT request
  Future<dynamic> put(
    String endpoint, {
    dynamic body,
    Map<String, String>? headers,
  }) async {
    try {
      final uri = _buildUri(endpoint);
      final request = await _httpClient.putUrl(uri).timeout(
            Duration(seconds: ApiConstants.connectTimeoutSeconds),
          );
      await _applyHeaders(request, headers);

      if (body != null) {
        final payload = body is String ? body : jsonEncode(body);
        request.write(payload);
      }

      final response = await request.close().timeout(
            Duration(seconds: ApiConstants.receiveTimeoutSeconds),
          );
      return await _processResponse(response);
    } on SocketException catch (e) {
      throw NetworkException('Unable to reach server: ${e.message}');
    } on TimeoutException {
      throw const TimeoutException('Request timed out. Please try again.');
    } on ApiException {
      rethrow;
    } catch (e) {
      throw ApiException('Unexpected network error: $e');
    }
  }

  /// Execute DELETE request
  Future<dynamic> delete(
    String endpoint, {
    dynamic body,
    Map<String, String>? headers,
  }) async {
    try {
      final uri = _buildUri(endpoint);
      final request = await _httpClient.deleteUrl(uri).timeout(
            Duration(seconds: ApiConstants.connectTimeoutSeconds),
          );
      await _applyHeaders(request, headers);

      if (body != null) {
        final payload = body is String ? body : jsonEncode(body);
        request.write(payload);
      }

      final response = await request.close().timeout(
            Duration(seconds: ApiConstants.receiveTimeoutSeconds),
          );
      return await _processResponse(response);
    } on SocketException catch (e) {
      throw NetworkException('Unable to reach server: ${e.message}');
    } on TimeoutException {
      throw const TimeoutException('Request timed out. Please try again.');
    } on ApiException {
      rethrow;
    } catch (e) {
      throw ApiException('Unexpected network error: $e');
    }
<<<<<<< HEAD
=======
  Future<Map<String, String>> _buildHeaders([Map<String, String>? customHeaders]) async {
=======
  Future<Map<String, String>> _buildHeaders(Map<String, String>? customHeaders) async {
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
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
<<<<<<< HEAD
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
  }
}
