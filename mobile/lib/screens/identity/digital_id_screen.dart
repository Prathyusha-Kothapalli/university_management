import 'package:flutter/material.dart';
import '../../core/theme/app_colors.dart';

class DigitalIdScreen extends StatelessWidget {
  const DigitalIdScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: AppColors.backgroundLight,
      appBar: AppBar(
        title: const Text('Digital Student ID'),
        backgroundColor: Colors.transparent,
        elevation: 0,
      ),
      body: SafeArea(
        child: Padding(
          padding: const EdgeInsets.all(20.0),
          child: Center(
            child: Container(
              padding: const EdgeInsets.all(24),
              decoration: BoxDecoration(
                gradient: const LinearGradient(
                  colors: [AppColors.backgroundDark, AppColors.surfaceDark],
                  begin: Alignment.topLeft,
                  end: Alignment.bottomRight,
                ),
                borderRadius: BorderRadius.circular(24),
                boxShadow: const [BoxShadow(color: Colors.black26, blurRadius: 20)],
              ),
              child: Column(
                mainAxisSize: MainAxisSize.min,
                children: [
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      Image.asset('assets/logo.png', width: 32, height: 32, errorBuilder: (_, __, ___) => const Icon(Icons.school, color: Colors.white)),
                      Container(
                        padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
                        decoration: BoxDecoration(color: AppColors.success.withOpacity(0.2), borderRadius: BorderRadius.circular(10)),
                        child: const Text('ACTIVE STUDENT', style: TextStyle(color: AppColors.success, fontSize: 10, fontWeight: FontWeight.bold)),
                      ),
                    ],
                  ),
                  const SizedBox(height: 20),
                  const CircleAvatar(radius: 36, backgroundColor: AppColors.primary, child: Text('AM', style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold, color: Colors.white))),
                  const SizedBox(height: 12),
                  const Text('Alex Morgan', style: TextStyle(color: Colors.white, fontSize: 18, fontWeight: FontWeight.bold)),
                  const Text('US-ID-2026-8801A', style: TextStyle(color: AppColors.secondary, fontSize: 13)),
                  const SizedBox(height: 20),
                  Container(
                    padding: const EdgeInsets.all(16),
                    decoration: BoxDecoration(color: Colors.white, borderRadius: BorderRadius.circular(12)),
                    child: const Icon(Icons.qr_code_2_rounded, size: 120, color: Colors.black),
                  ),
                  const SizedBox(height: 12),
                  const Text('Scan at campus turnstiles', style: TextStyle(color: Colors.white70, fontSize: 12)),
                ],
              ),
            ),
          ),
        ),
      ),
    );
  }
}
