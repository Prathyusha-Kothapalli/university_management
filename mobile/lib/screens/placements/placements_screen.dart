import 'package:flutter/material.dart';
import '../../core/theme/app_colors.dart';
import '../../models/campus_features.dart';
import '../../services/mock_data_service.dart';

/// Campus Placement Drives & Career Opportunities Screen.
class PlacementsScreen extends StatefulWidget {
  const PlacementsScreen({super.key});

  @override
  State<PlacementsScreen> createState() => _PlacementsScreenState();
}

class _PlacementsScreenState extends State<PlacementsScreen> {
  late List<PlacementDrive> _drives;

  @override
  void initState() {
    super.initState();
    _drives = List.from(MockDataService.placementDrives);
  }

  void _apply(PlacementDrive drive) {
    setState(() {
      final idx = _drives.indexWhere((d) => d.id == drive.id);
      if (idx != -1) {
        _drives[idx] = PlacementDrive(
          id: drive.id,
          company: drive.company,
          role: drive.role,
          ctc: drive.ctc,
          location: drive.location,
          eligibilityGpa: drive.eligibilityGpa,
          deadline: drive.deadline,
          status: 'Applied',
        );
      }
    });

    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        content: Text('Application submitted for ${drive.company} - ${drive.role}!'),
        behavior: SnackBarBehavior.floating,
        backgroundColor: AppColors.success,
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: AppColors.backgroundLight,
      appBar: AppBar(
        title: const Text('Placement Cell'),
      ),
      body: ListView.separated(
        padding: const EdgeInsets.all(20),
        itemCount: _drives.length,
        separatorBuilder: (_, __) => const SizedBox(height: 14),
        itemBuilder: (context, index) {
          final item = _drives[index];
          final isApplied = item.status == 'Applied';
          final isShortlisted = item.status == 'Shortlisted';

          return Container(
            padding: const EdgeInsets.all(18),
            decoration: BoxDecoration(
              color: Colors.white,
              borderRadius: BorderRadius.circular(16),
              border: Border.all(color: AppColors.borderLight),
            ),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Text(
                      item.company,
                      style: const TextStyle(
                        fontSize: 18,
                        fontWeight: FontWeight.w800,
                        color: AppColors.textPrimaryLight,
                      ),
                    ),
                    Container(
                      padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
                      decoration: BoxDecoration(
                        color: isShortlisted
                            ? const Color(0xFFFEF3C7)
                            : isApplied
                                ? AppColors.successLight
                                : const Color(0xFFEFF6FF),
                        borderRadius: BorderRadius.circular(8),
                      ),
                      child: Text(
                        item.status,
                        style: TextStyle(
                          fontSize: 12,
                          fontWeight: FontWeight.w700,
                          color: isShortlisted
                              ? const Color(0xFFD97706)
                              : isApplied
                                  ? AppColors.success
                                  : AppColors.primary,
                        ),
                      ),
                    ),
                  ],
                ),
                const SizedBox(height: 4),
                Text(
                  item.role,
                  style: const TextStyle(
                    fontSize: 14.5,
                    fontWeight: FontWeight.w600,
                    color: AppColors.primary,
                  ),
                ),
                const SizedBox(height: 10),
                Row(
                  children: [
                    const Icon(Icons.attach_money_rounded, size: 16, color: AppColors.success),
                    Text(item.ctc, style: const TextStyle(fontWeight: FontWeight.w700, fontSize: 13, color: AppColors.success)),
                    const SizedBox(width: 14),
                    const Icon(Icons.place_outlined, size: 16, color: AppColors.textSecondaryLight),
                    Text(item.location, style: const TextStyle(fontSize: 12.5, color: AppColors.textSecondaryLight)),
                  ],
                ),
                const SizedBox(height: 6),
                Row(
                  children: [
                    const Icon(Icons.school_outlined, size: 16, color: AppColors.textSecondaryLight),
                    const SizedBox(width: 4),
                    Text('Eligibility: ${item.eligibilityGpa}', style: const TextStyle(fontSize: 12.5, color: AppColors.textSecondaryLight)),
                    const SizedBox(width: 14),
                    const Icon(Icons.event_outlined, size: 16, color: AppColors.textSecondaryLight),
                    const SizedBox(width: 4),
                    Text('Deadline: ${item.deadline}', style: const TextStyle(fontSize: 12.5, color: AppColors.textSecondaryLight)),
                  ],
                ),
                const SizedBox(height: 14),
                SizedBox(
                  width: double.infinity,
                  child: ElevatedButton(
                    onPressed: isApplied || isShortlisted ? null : () => _apply(item),
                    style: ElevatedButton.styleFrom(
                      backgroundColor: AppColors.primary,
                      padding: const EdgeInsets.symmetric(vertical: 10),
                    ),
                    child: Text(
                      isShortlisted
                          ? '🎉 Shortlisted for Interview'
                          : isApplied
                              ? '✓ Application Submitted'
                              : 'Apply for Drive',
                      style: const TextStyle(fontWeight: FontWeight.w700),
                    ),
                  ),
                ),
              ],
            ),
          );
        },
      ),
    );
  }
}
