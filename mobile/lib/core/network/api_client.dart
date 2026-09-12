import 'dart:async';
import 'dart:convert';
import 'dart:io';

import '../constants/api_constants.dart';
import '../../services/token_storage_service.dart';
import 'api_exceptions.dart';

/// Centralized HTTP API Client.
///
/// Handles:
/// - Base URL resolution from [ApiConstants]
/// - Automatic `Authorization: Bearer <token>` injection
/// - REST verbs: GET, POST, PUT, DELETE
/// - JSON serialization and deserialization
/// - Robust HTTP & socket exception translation
class ApiClient {
  final String baseUrl;
  final TokenStorageService tokenStorage;
  final HttpClient _httpClient;

  ApiClient({
    String? baseUrl,
    TokenStorageService? tokenStorage,
    HttpClient? httpClient,
  })  : baseUrl = baseUrl ?? ApiConstants.apiBaseUrl,
        tokenStorage = tokenStorage ?? TokenStorageService(),
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
    }
    return uri;
  }

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
  }
}
