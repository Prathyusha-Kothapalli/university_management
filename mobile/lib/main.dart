import 'package:flutter/material.dart';

void main() {
  runApp(const UniSphereApp());
}

class UniSphereApp extends StatelessWidget {
  const UniSphereApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'UniSphere AI',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: const Color(0xFF0284C7)),
        useMaterial3: true,
      ),
      home: const FoundationPlaceholderScreen(),
    );
  }
}

class FoundationPlaceholderScreen extends StatelessWidget {
  const FoundationPlaceholderScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFF0F172A),
      body: Center(
        child: Container(
          margin: const EdgeInsets.all(24.0),
          padding: const EdgeInsets.all(32.0),
          decoration: BoxDecoration(
            color: const Color(0xFF1E293B),
            borderRadius: BorderRadius.circular(16.0),
            border: Border.all(color: const Color(0xFF334155)),
          ),
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              const Icon(
                Icons.school_rounded,
                size: 64.0,
                color: Color(0xFF38BDF8),
              ),
              const SizedBox(height: 16.0),
              const Text(
                'UniSphere AI',
                style: TextStyle(
                  fontSize: 28.0,
                  fontWeight: FontWeight.bold,
                  color: Color(0xFF38BDF8),
                ),
              ),
              const SizedBox(height: 8.0),
              const Text(
                'Multi-Tenant University Management',
                style: TextStyle(
                  fontSize: 16.0,
                  color: Color(0xFF94A3B8),
                ),
                textAlign: TextAlign.center,
              ),
              const SizedBox(height: 24.0),
              Chip(
                backgroundColor: const Color(0xFF0369A1),
                label: const Text(
                  'Mobile Foundation Ready',
                  style: TextStyle(
                    color: Colors.white,
                    fontWeight: FontWeight.w600,
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
