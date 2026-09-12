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
│   └── user_repository.dart        <-- User profile fetching & updating
├── screens/
│   ├── ai_assistant/
│   │   └── ai_assistant_screen.dart<-- Interactive Campus AI Chatbot
│   ├── assignments/
│   │   └── assignments_screen.dart <-- Coursework tasks and submissions
│   ├── attendance/
│   │   └── attendance_screen.dart  <-- Subject-wise attendance and safety thresholds
│   ├── auth/
│   │   ├── login_screen.dart       <-- Login with quick demo buttons & validation
│   │   └── register_screen.dart    <-- Registration with role selector
│   ├── chat/
│   │   └── chat_screen.dart        <-- Messaging with professors and advisors
│   ├── exams/
│   │   └── exams_screen.dart       <-- Exam schedules, hall tickets, CGPA transcripts
│   ├── home/
│   │   └── home_screen.dart        <-- Main dashboard connecting all campus modules
│   ├── notifications/
│   │   └── notifications_screen.dart<-- Push alerts & campus notices
│   ├── placements/
│   │   └── placements_screen.dart  <-- Campus recruitment drives & applications
│   ├── profile/
│   │   ├── edit_profile_dialog.dart<-- Modal to update name and phone
│   │   └── profile_screen.dart     <-- Profile inspection & logout
│   └── splash/
│       └── splash_screen.dart      <-- Animated university crest & token check
├── services/
│   ├── api_service.dart            <-- High-level API calls with mock fallback
│   ├── mock_data_service.dart      <-- Offline demo datasets
│   ├── storage_service.dart        <-- User profile caching
│   └── token_storage_service.dart  <-- Secure JWT access & refresh token persistence
├── state/
│   ├── auth_state.dart             <-- Reactive ChangeNotifier for authentication
│   └── profile_state.dart          <-- Reactive ChangeNotifier for profile updates
├── widgets/
│   ├── custom_button.dart          <-- Material 3 button with loading spinner
│   ├── custom_text_field.dart      <-- Input field with validation & password toggle
│   ├── empty_state_view.dart       <-- Placeholder for empty views
│   ├── error_card.dart             <-- Dismissible error alert
│   ├── loading_indicator.dart      <-- Centered progress indicator
│   ├── stat_card.dart              <-- Academic metric card (GPA, Attendance)
│   └── user_avatar.dart            <-- User initials avatar
└── main.dart                       <-- App bootstrap, themes & routing
```

---

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