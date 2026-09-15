import 'package:flutter/material.dart';
import '../../core/theme/app_colors.dart';

class StudentHoldsView extends StatelessWidget {
  const StudentHoldsView({super.key});

  @override
  Widget build(BuildContext context) {
    final holds = [
      {
        'type': 'FINANCIAL HOLD',
        'reason': 'Unpaid Library Overdue Fee (\$45.00)',
        'office': 'Bursar Office',
        'date': 'Sep 1, 2026',
      }
    ];

    return Scaffold(
      backgroundColor: AppColors.backgroundLight,
      appBar: AppBar(
        title: const Text('Academic & Financial Holds'),
        backgroundColor: Colors.transparent,
        elevation: 0,
      ),
      body: SafeArea(
        child: Padding(
          padding: const EdgeInsets.all(16.0),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              const Text(
                'Active Registration Blocks',
                style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
              ),
              const SizedBox(height: 6),
              const Text(
                'Holds prevent course registration and transcript issuance until resolved.',
                style: TextStyle(color: AppColors.textSecondaryLight, fontSize: 13),
              ),
              const SizedBox(height: 16),

              if (holds.isEmpty)
                const Center(
                  child: Padding(
                    padding: EdgeInsets.all(32.0),
                    child: Text('No active holds on your account.', style: TextStyle(color: AppColors.success)),
                  ),
                )
              else
                Expanded(
                  child: ListView.builder(
                    itemCount: holds.length,
                    itemBuilder: (context, idx) {
                      final item = holds[idx];
                      return Container(
                        margin: const EdgeInsets.only(bottom: 12),
                        padding: const EdgeInsets.all(16),
                        decoration: BoxDecoration(
                          color: AppColors.error.withOpacity(0.08),
                          borderRadius: BorderRadius.circular(16),
                          border: Border.all(color: AppColors.error.withOpacity(0.3)),
                        ),
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Row(
                              children: [
                                const Icon(Icons.warning_amber_rounded, color: AppColors.error),
                                const SizedBox(width: 8),
                                Text(
                                  item['type']!,
                                  style: const TextStyle(
                                    fontWeight: FontWeight.bold,
                                    color: AppColors.error,
                                    fontSize: 14,
                                  ),
                                ),
                              ],
                            ),
                            const SizedBox(height: 8),
                            Text(
                              item['reason']!,
                              style: const TextStyle(
                                fontSize: 14,
                                fontWeight: FontWeight.w600,
                                color: AppColors.textPrimaryLight,
                              ),
                            ),
                            const SizedBox(height: 6),
                            Text(
                              'Placed by ${item['office']} on ${item['date']}',
                              style: const TextStyle(
                                fontSize: 12,
                                color: AppColors.textSecondaryLight,
                              ),
                            ),
                          ],
                        ),
                      );
                    },
                  ),
                ),
            ],
          ),
        ),
      ),
    );
  }
}
