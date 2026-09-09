# UniSphere AI — Mobile Application

A production-ready, multi-tenant Flutter mobile application built with **Material 3**, **JWT authentication**, and a clean layered architecture.

---

## 📱 Navigation & App Flow

```
           ┌──────────────┐
           │ SplashScreen │
           └──────┬───────┘
                  │ (Check Token)
        ┌─────────┴─────────┐
        ▼                   ▼
 [Unauthenticated]    [Authenticated]
        │                   │
  ┌─────▼───────┐           │
  │ LoginScreen │◄──────────┼───────────────┐
  └──┬──────────┘           │               │
     │       ▲              │               │
(Go) │       │ (Back)       │               │
     ▼       │              │               │
┌────────────┴───┐          │               │
│ RegisterScreen │          │               │
└────────────────┘          │               │
                            ▼               │
                    ┌──────────────┐        │
                    │  HomeScreen  │        │
                    │  Dashboard   │        │
                    └───────┬──────┘        │
                            │               │
                      (View Profile)        │
                            ▼               │
                    ┌──────────────┐        │
                    │ProfileScreen │        │
                    └───────┬──────┘        │
                            │               │
                         (Logout)───────────┘
```

---

## 🏗️ Project Architecture

```
lib/
├── core/
│   ├── constants/
│   │   ├── api_constants.dart    <-- Backend Developer API Base URL
│   │   ├── app_constants.dart    <-- App branding & storage keys
│   │   └── route_constants.dart  <-- Named navigation routes
│   ├── network/
│   │   ├── api_client.dart       <-- Centralized HTTP client (GET, POST, PUT, DELETE)
│   │   ├── api_endpoints.dart    <-- REST API path constants
│   │   └── api_exceptions.dart   <-- Network, Timeout, 401, 403, 404, 500 exceptions
│   ├── theme/
│   │   ├── app_colors.dart       <-- Sapphire, Slate, Emerald, Amber, Rose palette
│   │   ├── app_theme.dart        <-- Material 3 Light & Dark themes
│   │   └── app_typography.dart   <-- Standardized type scale
│   └── utils/
│       ├── result.dart           <-- Result monad (Result.success / Result.failure)
│       └── validators.dart       <-- Email, password, phone, name validators
├── models/
│   ├── api_response.dart         <-- Generic ApiResponse<T> wrapper
│   ├── login_request.dart        <-- Email & password payload
│   ├── login_response.dart       <-- Access token, refresh token & user parser
│   ├── register_request.dart     <-- Registration payload
│   └── user.dart                 <-- User profile domain model (roles, GPA, student ID)
├── repositories/
│   ├── auth_repository.dart      <-- Session lifecycle, login, register, logout
│   └── user_repository.dart      <-- User profile fetching & updating
├── screens/
│   ├── auth/
│   │   ├── login_screen.dart     <-- Login with quick demo buttons & validation
│   │   └── register_screen.dart  <-- Registration with role selector
│   ├── home/
│   │   └── home_screen.dart      <-- KPI cards, campus modules & today's classes
│   ├── profile/
│   │   ├── edit_profile_dialog.dart <-- Modal to update name and phone
│   │   └── profile_screen.dart   <-- Profile inspection & logout
│   └── splash/
│       └── splash_screen.dart    <-- Animated university crest & token check
├── services/
│   ├── api_service.dart          <-- High-level API calls with mock fallback
│   ├── mock_data_service.dart    <-- Offline demo data (Alex Johnson, Dr. Mitchell)
│   ├── storage_service.dart      <-- User profile caching
│   └── token_storage_service.dart<-- Secure JWT access & refresh token persistence
├── state/
│   ├── auth_state.dart           <-- Reactive ChangeNotifier for authentication
│   └── profile_state.dart        <-- Reactive ChangeNotifier for profile updates
├── widgets/
│   ├── custom_button.dart        <-- Material 3 button with loading spinner
│   ├── custom_text_field.dart    <-- Input field with validation & password toggle
│   ├── empty_state_view.dart     <-- Placeholder for empty views
│   ├── error_card.dart           <-- Dismissible error alert
│   ├── loading_indicator.dart    <-- Centered progress indicator
│   ├── stat_card.dart            <-- Academic metric card (GPA, Attendance)
│   └── user_avatar.dart          <-- User initials avatar
└── main.dart                     <-- App bootstrap, themes & routing
```

---

## ⚙️ Backend API Configuration

To connect the mobile app to a live backend server, edit **[`lib/core/constants/api_constants.dart`](lib/core/constants/api_constants.dart)**:

```dart
class ApiConstants {
  // Update this URL to point to your live server:
  static const String apiBaseUrl = 'http://10.0.2.2:8000/api/v1'; // Android Emulator
  // static const String apiBaseUrl = 'http://localhost:8000/api/v1'; // iOS / Web
  // static const String apiBaseUrl = 'https://api.youruniversity.edu/api/v1'; // Production
}
```

> **Note:** If the backend server is unreachable or offline, the app automatically switches to **`MockDataService`**, allowing complete offline testing of all screens, authentication, and profiles without errors.

---

## 🧪 Testing & Execution

Run the automated test suite:

```bash
cd mobile
flutter test
```

Run code analysis:

```bash
flutter analyze
```

Run on an active emulator or device:

```bash
flutter run
```
