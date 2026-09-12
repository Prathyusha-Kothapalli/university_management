import 'package:flutter/material.dart';
import '../../core/theme/app_colors.dart';
import '../../widgets/custom_button.dart';

class QrScannerScreen extends StatefulWidget {
  const QrScannerScreen({super.key});

  @override
  State<QrScannerScreen> createState() => _QrScannerScreenState();
}

class _QrScannerScreenState extends State<QrScannerScreen> {
  bool _isScanning = false;
  bool _isSuccess = false;

  void _simulateScan() async {
    setState(() {
      _isScanning = true;
    });

    await Future.delayed(const Duration(seconds: 2));

    setState(() {
      _isScanning = false;
      _isSuccess = true;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.black,
      appBar: AppBar(
        title: const Text('Scan Lecture Attendance QR'),
        backgroundColor: Colors.transparent,
        elevation: 0,
      ),
      body: SafeArea(
        child: Column(
          children: [
            Expanded(
              child: Center(
                child: Container(
                  width: 260,
                  height: 260,
                  decoration: BoxDecoration(
                    border: Border.all(
                      color: _isSuccess ? AppColors.success : AppColors.primary,
                      width: 3,
                    ),
                    borderRadius: BorderRadius.circular(20),
                  ),
                  child: Center(
                    child: _isScanning
                        ? const CircularProgressIndicator(color: AppColors.primary)
                        : _isSuccess
                            ? const Icon(Icons.check_circle_rounded, size: 80, color: AppColors.success)
                            : const Icon(Icons.qr_code_scanner_rounded, size: 80, color: Colors.white54),
                  ),
                ),
              ),
            ),
            Padding(
              padding: const EdgeInsets.all(24.0),
              child: Column(
                children: [
                  Text(
                    _isSuccess
                        ? 'Attendance Recorded Successfully!'
                        : 'Align the lecture projector QR code within the frame to check in.',
                    textAlign: TextAlign.center,
                    style: TextStyle(
                      color: _isSuccess ? AppColors.success : Colors.white70,
                      fontSize: 14,
                      fontWeight: FontWeight.w600,
                    ),
                  ),
                  const SizedBox(height: 20),
                  CustomButton(
                    text: _isSuccess ? 'Done' : 'Simulate Camera QR Scan',
                    onPressed: _isSuccess ? () => Navigator.of(context).pop() : _simulateScan,
                    isLoading: _isScanning,
                    icon: Icons.camera_alt_rounded,
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}
