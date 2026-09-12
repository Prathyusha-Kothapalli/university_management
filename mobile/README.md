# UniSphere AI — Mobile Application

<<<<<<< HEAD
A complete, production-ready Flutter mobile application for the **UniSphere AI** Multi-Tenant University Management Platform.

---

## 🏛️ Architecture & Clean Structure

```text
mobile/
├── android/                         # Android native project, manifests & Gradle
├── ios/                             # iOS native project, Runner & Podfile
├── lib/
│   ├── core/
│   │   ├── constants/
│   │   │   ├── api_constants.dart   # API_BASE_URL, headers, timeouts, mock toggles
│   │   │   ├── app_constants.dart   # App metadata, keys, demo credentials
│   │   │   └── route_constants.dart # Named route definitions
│   │   ├── network/
│   │   │   ├── api_client.dart      # HTTP client (GET/POST/PUT/DELETE, Bearer tokens)
│   │   │   ├── api_endpoints.dart   # Centralized REST route endpoints
│   │   │   └── api_exceptions.dart  # Structured network & server exceptions
│   │   ├── theme/
│   │   │   ├── app_colors.dart      # Material 3 color system (Sapphire, Sky, Emerald)
│   │   │   ├── app_theme.dart       # Light & Dark M3 ThemeData
│   │   │   └── app_typography.dart  # Type hierarchy & font scales
│   │   └── utils/
│   │       ├── formatters.dart      # String and date formatters
│   │       ├── result.dart          # Sealed Result<T, E> functional container
│   │       └── validators.dart      # Form field validation (Email, Password, Phone)
│   ├── models/
│   │   ├── api_response.dart        # Generic API response wrapper
│   │   ├── login_request.dart       # Login credential payload
│   │   ├── login_response.dart      # JWT token & user model response
│   │   ├── register_request.dart    # User registration payload
│   │   ├── user.dart                # User entity with JSON serialization
│   │   └── user_profile.dart        # Academic stats (GPA, Attendance, Credits)
│   ├── services/
│   │   ├── api_service.dart         # API integration layer
│   │   ├── mock_data_service.dart   # Realistic university mock layer & offline data
│   │   ├── storage_service.dart     # Key-value storage abstraction (Memory + Encrypted file)
│   │   └── token_storage_service.dart # Secure JWT token persistence & session management
│   ├── repositories/
│   │   ├── auth_repository.dart     # Authentication & token coordination with fallback
│   │   └── user_repository.dart     # Profile retrieval and updates
│   ├── state/
│   │   ├── auth_state.dart          # Observable authentication state notifier
│   │   └── profile_state.dart       # Observable profile state notifier
│   ├── screens/
│   │   ├── splash/
│   │   │   └── splash_screen.dart   # App branding, loading, auto session check
│   │   ├── auth/
│   │   │   ├── login_screen.dart    # Login form, quick demo fill, remember me
│   │   │   └── register_screen.dart # Registration form with confirm password
│   │   ├── home/
│   │   │   └── home_screen.dart     # University management dashboard & stats
│   │   └── profile/
│   │       ├── profile_screen.dart  # Profile details, academic cards, logout
│   │       └── edit_profile_dialog.dart # Edit user name & phone modal
│   ├── widgets/
│   │   ├── custom_button.dart       # Reusable button with variants & loading state
│   │   ├── custom_text_field.dart   # Input field with prefix icons & password toggle
│   │   ├── empty_state_view.dart    # Empty state graphic & message
│   │   ├── error_card.dart          # Dismissible error notification widget
│   │   ├── loading_indicator.dart   # M3 themed loading indicator
│   │   ├── stat_card.dart           # Dashboard metric cards
│   │   └── user_avatar.dart         # Remote image / initials avatar
│   └── main.dart                    # Application entry point & route generator
├── test/
│   ├── unit/
│   │   ├── auth_repository_test.dart
│   │   ├── models_test.dart
│   │   ├── token_storage_test.dart
│   │   └── validators_test.dart
│   └── widget_test.dart             # Smoke test for Splash -> Login navigation
└── pubspec.yaml
=======
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
>>>>>>> 29907a7 (added flutter)
```

---

<<<<<<< HEAD
## ⚙️ Backend API Configuration

The backend endpoint is centrally configured in:
[`lib/core/constants/api_constants.dart`](file:///c:/Users/abc/university_management/mobile/lib/core/constants/api_constants.dart)

```dart
class ApiConstants {
  // Set your backend API URL here:
  static const String API_BASE_URL = "http://10.0.2.2:8000/api/v1";

  // When true, automatically falls back to the mock layer if live backend is unreachable
  static const bool useMockFallbackOnFailure = true;

  // Force mock mode for offline testing and demos
  static const bool forceMockMode = false;
}
```

### URL Guide by Platform
- **Android Emulator**: `http://10.0.2.2:8000/api/v1`
- **iOS Simulator**: `http://127.0.0.1:8000/api/v1`
- **Physical Device**: `http://<YOUR_LOCAL_IP>:8000/api/v1`
- **Production Server**: `https://api.unisphere.edu/api/v1`

---

## 🔑 Demo Credentials

For quick testing without creating an account:
- **Email**: `student@university.edu`
- **Password**: `Password123!`
*(Or click the **Fill** button on the Login screen)*

---

## 🚀 Running the Application

1. **Install Dependencies:**
   ```bash
   flutter pub get
   ```

2. **Run All Tests:**
   ```bash
   flutter test
   ```

3. **Launch on Connected Device or Emulator:**
   ```bash
   flutter run
   ```
=======
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
>>>>>>> 29907a7 (added flutter)
