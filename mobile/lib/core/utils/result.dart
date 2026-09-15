<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
/// Generic Result monad for clean error/success handling without messy try/catches in UI.
class Result<T> {
  final T? data;
  final String? error;
  final bool isSuccess;

  const Result.success(this.data)
      : error = null,
        isSuccess = true;

  const Result.failure(this.error)
      : data = null,
        isSuccess = false;

  bool get isFailure => !isSuccess;
  T? get dataOrNull => data;
  String? get errorOrNull => error;

  R fold<R>({
    required R Function(T data) onSuccess,
    required R Function(String error) onFailure,
  }) {
    if (isSuccess) {
      return onSuccess(data as T);
    } else {
      return onFailure(error ?? 'An unexpected error occurred');
    }
  }
<<<<<<< HEAD
=======
=======
>>>>>>> origin/web
sealed class Result<T, E> {
  const Result();

  bool get isSuccess => this is Success<T, E>;
  bool get isFailure => this is Failure<T, E>;

  T? get dataOrNull => switch (this) {
        Success(:final data) => data,
        Failure() => null,
      };

  E? get errorOrNull => switch (this) {
        Success() => null,
        Failure(:final error) => error,
      };
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689

  R when<R>({
    required R Function(T data) success,
    required R Function(String error) failure,
  }) =>
<<<<<<< HEAD
      switch (this) {
        Success(:final data) => success(data),
        Failure(:final error) => failure(error),
      };
}

class Success<T, E> extends Result<T, E> {
  final T data;
  const Success(this.data);
}

class Failure<T, E> extends Result<T, E> {
  final E error;
  const Failure(this.error);
<<<<<<< HEAD
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
=======
/// Generic Result monad for clean error/success handling without messy try/catches in UI.
class Result<T> {
  final T? data;
  final String? error;
  final bool isSuccess;

  const Result.success(this.data)
      : error = null,
        isSuccess = true;

  const Result.failure(this.error)
      : data = null,
        isSuccess = false;

  R fold<R>({
    required R Function(T data) onSuccess,
    required R Function(String error) onFailure,
  }) {
    if (isSuccess) {
      return onSuccess(data as T);
    } else {
      return onFailure(error ?? 'An unexpected error occurred');
    }
  }
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
      fold(onSuccess: success, onFailure: failure);
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
}
