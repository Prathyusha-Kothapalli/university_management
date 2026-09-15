import 'package:flutter/material.dart';
import '../../core/theme/app_colors.dart';
import '../../widgets/custom_button.dart';
import '../../widgets/custom_text_field.dart';

class OtpVerificationScreen extends StatefulWidget {
  const OtpVerificationScreen({super.key});

  @override
  State<OtpVerificationScreen> createState() => _OtpVerificationScreenState();
}

class _OtpVerificationScreenState extends State<OtpVerificationScreen> {
  final _otpController = TextEditingController();
  bool _isLoading = false;

  @override
  void dispose() {
    _otpController.dispose();
    super.dispose();
  }

  void _verifyOtp() async {
    if (_otpController.text.length < 6) return;

    setState(() {
      _isLoading = true;
    });

    await Future.delayed(const Duration(seconds: 1));

    setState(() {
      _isLoading = false;
    });

    if (mounted) {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(content: Text('2FA Verification Successful!')),
      );
      Navigator.of(context).pop();
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: AppColors.backgroundLight,
      appBar: AppBar(
        title: const Text('2FA Verification'),
        backgroundColor: Colors.transparent,
        elevation: 0,
      ),
      body: SafeArea(
        child: Padding(
          padding: const EdgeInsets.all(24.0),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              const Icon(Icons.security_rounded, size: 60, color: AppColors.primary),
              const SizedBox(height: 16),
              const Text(
                'Enter Authenticator Code',
                textAlign: TextAlign.center,
                style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold),
              ),
              const SizedBox(height: 8),
              const Text(
                'Enter the 6-digit code from your authenticator application to verify login.',
                textAlign: TextAlign.center,
                style: TextStyle(color: AppColors.textSecondaryLight),
              ),
              const SizedBox(height: 32),

              CustomTextField(
                controller: _otpController,
                label: 'OTP Verification Code',
                hint: '123456',
                prefixIcon: Icons.phonelink_lock_rounded,
                keyboardType: TextInputType.number,
              ),
              const SizedBox(height: 24),

              CustomButton(
                text: 'Verify Code',
                onPressed: _verifyOtp,
                isLoading: _isLoading,
                icon: Icons.check_circle_outline_rounded,
              ),
            ],
          ),
        ),
      ),
    );
  }
}
