import 'package:flutter/material.dart';

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
class AppColors {
  // Brand Colors
  static const Color primary = Color(0xFF0284C7); // Sapphire Sky
  static const Color primaryDark = Color(0xFF0369A1);
  static const Color primaryLight = Color(0xFFE0F2FE);
  
  static const Color secondary = Color(0xFF6366F1); // Indigo
  static const Color secondaryDark = Color(0xFF4F46E5);
  static const Color secondaryLight = Color(0xFFEEF2FF);

  static const Color accent = Color(0xFF0EA5E9);

  // Status & Feedback Colors
=======
>>>>>>> origin/web
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
/// Design tokens: University-tailored palette with sapphire, slate, emerald, amber, and rose.
class AppColors {
  AppColors._();

  // Primary Brand Colors
  static const Color primary = Color(0xFF1E40AF); // Deep Sapphire
  static const Color primaryLight = Color(0xFF3B82F6);
  static const Color primaryDark = Color(0xFF1E3A8A);

  // Secondary & Accents
  static const Color secondary = Color(0xFF0284C7); // Cyan
  static const Color secondaryLight = Color(0xFF38BDF8);
  static const Color accent = Color(0xFF6366F1); // Indigo

  // Status & Semantic Colors
<<<<<<< HEAD
<<<<<<< HEAD
=======
class AppColors {
  // Brand Colors
  static const Color primary = Color(0xFF0284C7); // Sapphire Sky
  static const Color primaryDark = Color(0xFF0369A1);
  static const Color primaryLight = Color(0xFFE0F2FE);
  
  static const Color secondary = Color(0xFF6366F1); // Indigo
  static const Color secondaryDark = Color(0xFF4F46E5);
  static const Color secondaryLight = Color(0xFFEEF2FF);

  static const Color accent = Color(0xFF0EA5E9);

  // Status & Feedback Colors
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
  static const Color success = Color(0xFF10B981); // Emerald
  static const Color successLight = Color(0xFFD1FAE5);
  static const Color warning = Color(0xFFF59E0B); // Amber
  static const Color warningLight = Color(0xFFFEF3C7);
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
  static const Color error = Color(0xFFEF4444); // Rose Red
  static const Color errorLight = Color(0xFFFEE2E2);
  static const Color info = Color(0xFF3B82F6);
  static const Color infoLight = Color(0xFFDBEAFE);

  // Neutral Background & Surface Colors - Light Mode
  static const Color backgroundLight = Color(0xFFF8FAFC);
  static const Color surfaceLight = Color(0xFFFFFFFF);
<<<<<<< HEAD
  static const Color surfaceElevatedLight = Color(0xFFF1F5F9);
=======
=======
>>>>>>> origin/web
  static const Color error = Color(0xFFEF4444); // Rose/Red
  static const Color errorLight = Color(0xFFFEE2E2);
  static const Color info = Color(0xFF3B82F6); // Blue
  static const Color infoLight = Color(0xFFDBEAFE);

  // Light Mode Neutrals
  static const Color backgroundLight = Color(0xFFF8FAFC);
  static const Color surfaceLight = Color(0xFFFFFFFF);
  static const Color cardLight = Color(0xFFFFFFFF);
<<<<<<< HEAD
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
=======
  static const Color error = Color(0xFFEF4444); // Rose Red
  static const Color errorLight = Color(0xFFFEE2E2);
  static const Color info = Color(0xFF3B82F6);

  // Neutral Background & Surface Colors - Light Mode
  static const Color backgroundLight = Color(0xFFF8FAFC);
  static const Color surfaceLight = Color(0xFFFFFFFF);
  static const Color surfaceElevatedLight = Color(0xFFF1F5F9);
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
  static const Color cardLight = Color(0xFFFFFFFF);
  static const Color surfaceElevatedLight = Color(0xFFF1F5F9);
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
  static const Color borderLight = Color(0xFFE2E8F0);
  static const Color textPrimaryLight = Color(0xFF0F172A);
  static const Color textSecondaryLight = Color(0xFF64748B);
  static const Color textMutedLight = Color(0xFF94A3B8);

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
  // Neutral Background & Surface Colors - Dark Mode
  static const Color backgroundDark = Color(0xFF0F172A);
  static const Color surfaceDark = Color(0xFF1E293B);
  static const Color surfaceElevatedDark = Color(0xFF334155);
=======
=======
>>>>>>> origin/web
  // Dark Mode Neutrals
  static const Color backgroundDark = Color(0xFF0B1120);
  static const Color surfaceDark = Color(0xFF1E293B);
  static const Color cardDark = Color(0xFF1E293B);
<<<<<<< HEAD
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
=======
  // Neutral Background & Surface Colors - Dark Mode
  static const Color backgroundDark = Color(0xFF0F172A);
  static const Color surfaceDark = Color(0xFF1E293B);
  static const Color surfaceElevatedDark = Color(0xFF334155);
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
  // Neutral Background & Surface Colors - Dark Mode
  static const Color backgroundDark = Color(0xFF0F172A);
  static const Color surfaceDark = Color(0xFF1E293B);
  static const Color cardDark = Color(0xFF1E293B);
  static const Color surfaceElevatedDark = Color(0xFF334155);
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
  static const Color borderDark = Color(0xFF334155);
  static const Color textPrimaryDark = Color(0xFFF8FAFC);
  static const Color textSecondaryDark = Color(0xFF94A3B8);
  static const Color textMutedDark = Color(0xFF64748B);
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> origin/web
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689

  // Card Accents
  static const Color academicBlue = Color(0xFF2563EB);
  static const Color attendanceGreen = Color(0xFF059669);
  static const Color examsPurple = Color(0xFF7C3AED);
  static const Color feesOrange = Color(0xFFD97706);
  static const Color libraryTeal = Color(0xFF0D9488);
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6a60e1207df8248e24833e44ec6880a1db598bfd
=======
=======
>>>>>>> 29907a7 (added flutter)
>>>>>>> origin/web
=======
>>>>>>> 629409c69cda5a877356a91a0a657f327d20f689
}
