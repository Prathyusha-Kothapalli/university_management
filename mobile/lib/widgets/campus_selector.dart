import 'package:flutter/material.dart';
import '../core/theme/app_colors.dart';

class CampusSelector extends StatelessWidget {
  final String selectedCampus;
  final ValueChanged<String> onCampusChanged;

  const CampusSelector({
    super.key,
    required this.selectedCampus,
    required this.onCampusChanged,
  });

  @override
  Widget build(BuildContext context) {
    final campuses = [
      'UniSphere Main Campus',
      'North Technology Campus',
      'Medical Science Quad',
    ];

    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 4),
      decoration: BoxDecoration(
        color: AppColors.surfaceElevatedLight,
        borderRadius: BorderRadius.circular(12),
        border: Border.all(color: AppColors.borderLight),
      ),
      child: DropdownButtonHideUnderline(
        child: DropdownButton<String>(
          value: selectedCampus,
          icon: const Icon(Icons.keyboard_arrow_down_rounded, color: AppColors.primary),
          isExpanded: true,
          items: campuses.map((campus) {
            return DropdownMenuItem<String>(
              value: campus,
              child: Row(
                children: [
                  const Icon(Icons.location_city_rounded, size: 18, color: AppColors.primary),
                  const SizedBox(width: 8),
                  Expanded(
                    child: Text(
                      campus,
                      style: const TextStyle(
                        fontSize: 13,
                        fontWeight: FontWeight.w600,
                        color: AppColors.textPrimaryLight,
                      ),
                      overflow: TextOverflow.ellipsis,
                    ),
                  ),
                ],
              ),
            );
          }).toList(),
          onChanged: (val) {
            if (val != null) onCampusChanged(val);
          },
        ),
      ),
    );
  }
}
