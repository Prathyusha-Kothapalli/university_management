import 'package:flutter/material.dart';
import '../../core/theme/app_colors.dart';
import '../../services/mock_data_service.dart';

/// Interactive Timetable and Class Schedule Screen.
class TimetableScreen extends StatefulWidget {
  const TimetableScreen({super.key});

  @override
  State<TimetableScreen> createState() => _TimetableScreenState();
}

class _TimetableScreenState extends State<TimetableScreen> {
  String _selectedDay = 'Monday';
  final List<String> _days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'];

  @override
  Widget build(BuildContext context) {
    final schedule = MockDataService.weeklyTimetable
        .where((item) => item['day'] == _selectedDay)
        .toList();

    return Scaffold(
      backgroundColor: AppColors.backgroundLight,
      appBar: AppBar(
        title: const Text('Weekly Timetable'),
      ),
      body: Column(
        children: [
          // Day Selector Bar
          Container(
            padding: const EdgeInsets.symmetric(vertical: 12, horizontal: 16),
            color: Colors.white,
            child: SingleChildScrollView(
              scrollDirection: Axis.horizontal,
              child: Row(
                children: _days.map((day) {
                  final isSelected = _selectedDay == day;
                  return Padding(
                    padding: const EdgeInsets.only(right: 8),
                    child: ChoiceChip(
                      label: Text(day),
                      selected: isSelected,
                      onSelected: (selected) {
                        if (selected) setState(() => _selectedDay = day);
                      },
                      selectedColor: AppColors.primary,
                      labelStyle: TextStyle(
                        color: isSelected ? Colors.white : AppColors.textSecondaryLight,
                        fontWeight: isSelected ? FontWeight.w700 : FontWeight.w500,
                        fontSize: 13,
                      ),
                      showCheckmark: false,
                    ),
                  );
                }).toList(),
              ),
            ),
          ),
          const Divider(height: 1),

          // Lecture List
          Expanded(
            child: schedule.isNotEmpty
                ? ListView.separated(
                    padding: const EdgeInsets.all(20),
                    itemCount: schedule.length,
                    separatorBuilder: (_, __) => const SizedBox(height: 12),
                    itemBuilder: (context, index) {
                      final item = schedule[index];
                      return Container(
                        padding: const EdgeInsets.all(16),
                        decoration: BoxDecoration(
                          color: Colors.white,
                          borderRadius: BorderRadius.circular(16),
                          border: Border.all(color: AppColors.borderLight),
                        ),
                        child: Row(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Container(
                              width: 4,
                              height: 52,
                              decoration: BoxDecoration(
                                color: Color(item['colorHex'] as int),
                                borderRadius: BorderRadius.circular(4),
                              ),
                            ),
                            const SizedBox(width: 14),
                            Expanded(
                              child: Column(
                                crossAxisAlignment: CrossAxisAlignment.start,
                                children: [
                                  Row(
                                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                                    children: [
                                      Text(
                                        item['code'].toString(),
                                        style: const TextStyle(
                                          fontWeight: FontWeight.w800,
                                          fontSize: 13.5,
                                          color: AppColors.primary,
                                        ),
                                      ),
                                      Container(
                                        padding: const EdgeInsets.symmetric(
                                            horizontal: 8, vertical: 3),
                                        decoration: BoxDecoration(
                                          color: AppColors.surfaceElevatedLight,
                                          borderRadius: BorderRadius.circular(6),
                                        ),
                                        child: Text(
                                          item['time'].toString(),
                                          style: const TextStyle(
                                            fontSize: 12,
                                            fontWeight: FontWeight.w600,
                                            color: AppColors.textPrimaryLight,
                                          ),
                                        ),
                                      ),
                                    ],
                                  ),
                                  const SizedBox(height: 6),
                                  Text(
                                    item['title'].toString(),
                                    style: const TextStyle(
                                      fontSize: 15,
                                      fontWeight: FontWeight.w700,
                                      color: AppColors.textPrimaryLight,
                                    ),
                                  ),
                                  const SizedBox(height: 6),
                                  Row(
                                    children: [
                                      const Icon(Icons.place_outlined,
                                          size: 15, color: AppColors.textSecondaryLight),
                                      const SizedBox(width: 4),
                                      Text(
                                        item['room'].toString(),
                                        style: const TextStyle(
                                          fontSize: 12.5,
                                          color: AppColors.textSecondaryLight,
                                        ),
                                      ),
                                      const SizedBox(width: 16),
                                      const Icon(Icons.person_outline_rounded,
                                          size: 15, color: AppColors.textSecondaryLight),
                                      const SizedBox(width: 4),
                                      Text(
                                        item['instructor'].toString(),
                                        style: const TextStyle(
                                          fontSize: 12.5,
                                          color: AppColors.textSecondaryLight,
                                        ),
                                      ),
                                    ],
                                  ),
                                ],
                              ),
                            ),
                          ],
                        ),
                      );
                    },
                  )
                : Center(
                    child: Column(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                        const Icon(Icons.coffee_rounded, size: 48, color: AppColors.textMutedLight),
                        const SizedBox(height: 12),
                        Text(
                          'No lectures scheduled for $_selectedDay',
                          style: const TextStyle(
                            fontSize: 15,
                            fontWeight: FontWeight.w600,
                            color: AppColors.textSecondaryLight,
                          ),
                        ),
                      ],
                    ),
                  ),
          ),
        ],
      ),
    );
  }
}
