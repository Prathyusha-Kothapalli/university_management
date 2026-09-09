# UniSphere AI - Mobile Application

This is the Flutter + Dart mobile application for UniSphere AI.

## Project Structure

```text
mobile/
├── lib/
│   ├── core/      # Core utilities, theme, constants, network clients
│   ├── features/  # Modular feature slices (e.g. auth, attendance, grades)
│   ├── common/    # Shared widgets, dialogs, inputs
│   ├── services/  # Background services, storage, push notifications
│   ├── models/    # Data models & JSON serialization
│   ├── routes/    # Navigation and route definitions
│   └── main.dart  # Mobile application entry point
├── test/          # Unit & widget tests
├── pubspec.yaml   # Flutter project configuration & dependencies
└── README.md      # Mobile documentation
```

## Running Locally

1. Check Flutter installation:
   ```bash
   flutter doctor
   ```

2. Get pub dependencies:
   ```bash
   flutter pub get
   ```

3. Launch target device or emulator:
   ```bash
   flutter run
   ```
