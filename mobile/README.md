# UniSphere Mobile — University Management Application

A complete, production-ready Flutter mobile application built for Android & iOS with **Material 3**, **JWT authentication**, and offline functionality, sharing the exact same **Python FastAPI** backend as the React web application.

---

## 🚀 Core Features

- 🔐 **Authentication & Session**: Login, registration, role switcher (Student / Faculty), secure JWT token persistence (never stores raw passwords).
- 📊 **Attendance Tracking**: Overall attendance percentage, subject-by-subject breakdown, and minimum 75% examination eligibility indicator.
- 📅 **Weekly Timetable**: Filterable day-by-day (Mon–Fri) schedule with room numbers, instructors, and lecture statuses.
- 📝 **Assignments & Coursework**: Tabbed pending and submitted coursework with deadlines, grading feedback, and submission actions.
- 🎓 **Exams & Transcripts**: Midterm and final exam schedules, hall ticket download pass, and SGPA/CGPA transcript history.
- 🔔 **Campus Notifications**: Real-time push and campus notices categorized by Exams, Placements, Fees, and Academic announcements.
- 💬 **Faculty & Peer Chat**: Direct messaging channels with course professors and academic advisors.
- 💼 **Placement Cell**: Campus recruitment drives, hiring partners (Google, Microsoft, AWS, NVIDIA), CTC compensation, and 1-tap applications.
- 🤖 **Campus AI Concierge**: Built-in intelligent AI assistant answering queries about attendance, exam venues, course syllabi, and university policies.
- 📶 **100% Offline Functionality**: Integrated caching and `MockDataService` fallback so all screens remain fully functional even when offline or during backend maintenance.
- 🐍 **Shared Python Backend**: Aligned REST endpoints with the FastAPI backend (`/auth`, `/academic`, `/placements`, `/notifications`, `/ai/chat`).

---

## 📱 Navigation & App Flow

```
                      ┌──────────────┐
                      │ SplashScreen │
                      └──────┬───────┘
                             │
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
                               └──┬─┬─┬─┬─┬─┬─┘        │
         ┌─────────────┬──────────┘ │ │ │ │ └──────────┤
         ▼             ▼            ▼ │ │ ▼            ▼
   ┌───────────┐ ┌───────────┐ ┌──────┼─┴────────┐ ┌───────────────┐
   │Attendance │ │ Timetable │ │ Assignments/    │ │ ProfileScreen │
   │  Screen   │ │  Screen   │ │ Exams / Results │ │ (Edit/Logout) ─┘
   └───────────┘ └───────────┘ └─────────────────┘ └───────────────┘
         │             │                │
         ▼             ▼                ▼
   ┌───────────┐ ┌───────────┐ ┌─────────────────┐
   │Placements │ │ Campus    │ │  AI Assistant   │
   │  Screen   │ │   Chat    │ │  (Floating Bot) │
   └───────────┘ └───────────┘ └─────────────────┘
```

---

## 🏗️ Folder Architecture

```
lib/
├── core/
│   ├── constants/
│   │   ├── api_constants.dart      <-- Backend Developer API Base URL
│   │   ├── app_constants.dart      <-- App branding & storage keys
│   │   └── route_constants.dart    <-- Named navigation routes
│   ├── network/
│   │   ├── api_client.dart         <-- Centralized HTTP client (GET, POST, PUT, DELETE)
│   │   ├── api_endpoints.dart      <-- Shared Python FastAPI endpoints
│   │   └── api_exceptions.dart     <-- Network, Timeout, 401, 403, 404, 500 exceptions
│   ├── theme/
│   │   ├── app_colors.dart         <-- Sapphire, Slate, Emerald, Amber, Rose palette
│   │   ├── app_theme.dart          <-- Material 3 Light & Dark themes
│   │   └── app_typography.dart     <-- Standardized type scale
│   └── utils/
│       ├── result.dart             <-- Result monad (Result.success / Result.failure)
│       └── validators.dart         <-- Email, password, phone, name validators
├── models/
│   ├── api_response.dart           <-- Generic ApiResponse<T> wrapper
│   ├── campus_features.dart        <-- Attendance, Assignment, Exam, Placement & Chat models
│   ├── login_request.dart          <-- Email & password payload
│   ├── login_response.dart         <-- Access token, refresh token & user parser
│   ├── register_request.dart       <-- Registration payload
│   └── user.dart                   <-- User profile domain model (roles, GPA, student ID)
├── repositories/
│   ├── auth_repository.dart        <-- Session lifecycle, login, register, logout
│   └── user_repository.dart        <-- Profile fetch and updates
├── screens/
│   ├── ai_assistant/               <-- Campus AI Copilot
│   ├── assignments/                <-- Assignments & Coursework
│   ├── attendance/                 <-- Attendance Tracking
│   ├── auth/                       <-- Login & Registration
│   ├── chat/                       <-- Direct Messaging
│   ├── exams/                      <-- Exam Schedules & Hall Tickets
│   ├── home/                       <-- Main Dashboard & Navigation
│   ├── notifications/              <-- Campus Notices & Alerts
│   ├── placements/                 <-- Campus Placements & Recruitment
│   ├── profile/                    <-- User Profile & Settings
│   ├── splash/                     <-- Initial splash screen
│   └── timetable/                  <-- Weekly Timetable
├── services/
│   ├── api_service.dart            <-- High-level REST API service with fallback
│   ├── mock_data_service.dart      <-- Demo data for offline testing
│   ├── storage_service.dart        <-- Local persistence service
│   └── token_storage_service.dart  <-- Secure token storage
├── state/
│   ├── auth_state.dart             <-- Authentication state notifier
│   └── profile_state.dart          <-- Profile state notifier
├── widgets/                        <-- Reusable UI components
└── main.dart                       <-- Application entrypoint
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
- **Student**: `student@university.edu` / `Password123!`
- **Faculty**: `faculty@university.edu` / `Password123!`

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
## ⚙️ Backend API Configuration (Python FastAPI)

Both the Flutter mobile application and React web frontend communicate with the shared Python FastAPI backend.
To switch the mobile app's active backend address, edit **[`lib/core/constants/api_constants.dart`](lib/core/constants/api_constants.dart)**:

```dart
class ApiConstants {
  // Android Emulator:
  static const String apiBaseUrl = 'http://10.0.2.2:8000/api/v1';

  // iOS Simulator / Web / Desktop:
  // static const String apiBaseUrl = 'http://localhost:8000/api/v1';

  // Physical Phone on LAN:
  // static const String apiBaseUrl = 'http://192.168.1.X:8000/api/v1';
}
```

---

## 🧪 Automated Testing

```bash
cd mobile
flutter test
```
>>>>>>> 7121f436592fb7bf0e48800a4e83cf8d44066dc9
