# UniSphere AI - Mobile Application

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
```

---

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
