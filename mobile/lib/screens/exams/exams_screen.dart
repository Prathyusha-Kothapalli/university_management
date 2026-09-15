import 'package:flutter/material.dart';
import '../../core/theme/app_colors.dart';
import '../../models/campus_features.dart';
import '../../services/mock_data_service.dart';

/// Exams Schedule & Semester Results Screen.
class ExamsScreen extends StatefulWidget {
  const ExamsScreen({super.key});

  @override
  State<ExamsScreen> createState() => _ExamsScreenState();
}

class _ExamsScreenState extends State<ExamsScreen> with SingleTickerProviderStateMixin {
  late TabController _tabController;

  @override
  void initState() {
    super.initState();
    _tabController = TabController(length: 2, vsync: this);
  }

  @override
  void dispose() {
    _tabController.dispose();
    super.dispose();
  }

  void _downloadHallTicket() {
    ScaffoldMessenger.of(context).showSnackBar(
      const SnackBar(
        content: Text('Hall Ticket downloaded to device storage (PDF verified).'),
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
        title: const Text('Exams & Results'),
        bottom: TabBar(
          controller: _tabController,
          labelColor: AppColors.primary,
          unselectedLabelColor: AppColors.textSecondaryLight,
          indicatorColor: AppColors.primary,
          indicatorWeight: 3,
          tabs: const [
            Tab(text: 'Exam Timetable'),
            Tab(text: 'Results & CGPA'),
          ],
        ),
      ),
      body: TabBarView(
        controller: _tabController,
        children: [
          _buildExamScheduleTab(),
          _buildResultsTab(),
        ],
      ),
    );
  }

  Widget _buildExamScheduleTab() {
    final exams = MockDataService.examSchedule;

    return SingleChildScrollView(
      padding: const EdgeInsets.all(20),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          // Hall Ticket Action Card
          Container(
            padding: const EdgeInsets.all(18),
            decoration: BoxDecoration(
              gradient: const LinearGradient(
                colors: [AppColors.primaryDark, AppColors.primary],
                begin: Alignment.topLeft,
                end: Alignment.bottomRight,
              ),
              borderRadius: BorderRadius.circular(16),
            ),
            child: Row(
              children: [
                Container(
                  padding: const EdgeInsets.all(10),
                  decoration: BoxDecoration(
                    color: Colors.white.withOpacity(0.2),
                    borderRadius: BorderRadius.circular(12),
                  ),
                  child: const Icon(Icons.badge_rounded, color: Colors.white, size: 28),
                ),
                const SizedBox(width: 14),
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: const [
                      Text(
                        'Midterm Hall Ticket Ready',
                        style: TextStyle(
                          color: Colors.white,
                          fontSize: 15,
                          fontWeight: FontWeight.w700,
                        ),
                      ),
                      SizedBox(height: 2),
                      Text(
                        'Fall 2026 Examination Admit Pass',
                        style: TextStyle(
                          color: Colors.white70,
                          fontSize: 12,
                        ),
                      ),
                    ],
                  ),
                ),
                ElevatedButton(
                  onPressed: _downloadHallTicket,
                  style: ElevatedButton.styleFrom(
                    backgroundColor: Colors.white,
                    foregroundColor: AppColors.primary,
                    padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 8),
                  ),
                  child: const Text('Download', style: TextStyle(fontWeight: FontWeight.w700)),
                ),
              ],
            ),
          ),
          const SizedBox(height: 24),

          const Text(
            'Upcoming Examinations',
            style: TextStyle(
              fontSize: 18,
              fontWeight: FontWeight.w700,
              color: AppColors.textPrimaryLight,
            ),
          ),
          const SizedBox(height: 12),

          ...exams.map((exam) => Container(
                margin: const EdgeInsets.only(bottom: 12),
                padding: const EdgeInsets.all(16),
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
                        Container(
                          padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 3),
                          decoration: BoxDecoration(
                            color: AppColors.primary.withOpacity(0.1),
                            borderRadius: BorderRadius.circular(6),
                          ),
                          child: Text(
                            exam.courseCode,
                            style: const TextStyle(
                              fontWeight: FontWeight.w700,
                              fontSize: 12,
                              color: AppColors.primary,
                            ),
                          ),
                        ),
                        Container(
                          padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 3),
                          decoration: BoxDecoration(
                            color: AppColors.surfaceElevatedLight,
                            borderRadius: BorderRadius.circular(6),
                          ),
                          child: Text(
                            exam.date,
                            style: const TextStyle(
                              fontSize: 12,
                              fontWeight: FontWeight.w700,
                              color: AppColors.textPrimaryLight,
                            ),
                          ),
                        ),
                      ],
                    ),
                    const SizedBox(height: 8),
                    Text(
                      exam.courseTitle,
                      style: const TextStyle(
                        fontSize: 15.5,
                        fontWeight: FontWeight.w700,
                        color: AppColors.textPrimaryLight,
                      ),
                    ),
                    const SizedBox(height: 8),
                    Row(
                      children: [
                        const Icon(Icons.schedule_rounded, size: 15, color: AppColors.textSecondaryLight),
                        const SizedBox(width: 4),
                        Text(exam.time, style: const TextStyle(fontSize: 12.5, color: AppColors.textSecondaryLight)),
                        const SizedBox(width: 14),
                        const Icon(Icons.place_outlined, size: 15, color: AppColors.textSecondaryLight),
                        const SizedBox(width: 4),
                        Text(exam.hall, style: const TextStyle(fontSize: 12.5, color: AppColors.textSecondaryLight)),
                        const SizedBox(width: 14),
                        const Icon(Icons.airline_seat_recline_normal_rounded, size: 15, color: AppColors.textSecondaryLight),
                        const SizedBox(width: 4),
                        Text(exam.seat, style: const TextStyle(fontSize: 12.5, color: AppColors.textSecondaryLight)),
                      ],
                    ),
                  ],
                ),
              )),
        ],
      ),
    );
  }

  Widget _buildResultsTab() {
    final results = MockDataService.examResults;

    return SingleChildScrollView(
      padding: const EdgeInsets.all(20),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          // CGPA Summary Banner
          Container(
            padding: const EdgeInsets.all(20),
            decoration: BoxDecoration(
              color: Colors.white,
              borderRadius: BorderRadius.circular(16),
              border: Border.all(color: AppColors.borderLight),
            ),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceAround,
              children: [
                Column(
                  children: const [
                    Text('Cumulative CGPA', style: TextStyle(fontSize: 12.5, color: AppColors.textSecondaryLight)),
                    SizedBox(height: 4),
                    Text('3.86', style: TextStyle(fontSize: 26, fontWeight: FontWeight.w800, color: AppColors.primary)),
                    SizedBox(height: 2),
                    Text('Out of 4.00', style: TextStyle(fontSize: 11, color: AppColors.textMutedLight)),
                  ],
                ),
                Container(height: 48, width: 1, color: AppColors.borderLight),
                Column(
                  children: const [
                    Text('Total Credits', style: TextStyle(fontSize: 12.5, color: AppColors.textSecondaryLight)),
                    SizedBox(height: 4),
                    Text('88', style: TextStyle(fontSize: 26, fontWeight: FontWeight.w800, color: AppColors.success)),
                    SizedBox(height: 2),
                    Text('Earned / 120', style: TextStyle(fontSize: 11, color: AppColors.textMutedLight)),
                  ],
                ),
                Container(height: 48, width: 1, color: AppColors.borderLight),
                Column(
                  children: const [
                    Text('Academic Status', style: TextStyle(fontSize: 12.5, color: AppColors.textSecondaryLight)),
                    SizedBox(height: 4),
                    Text("Dean's List", style: TextStyle(fontSize: 18, fontWeight: FontWeight.w800, color: AppColors.accent)),
                    SizedBox(height: 2),
                    Text('Top 5% Rank', style: TextStyle(fontSize: 11, color: AppColors.textMutedLight)),
                  ],
                ),
              ],
            ),
          ),
          const SizedBox(height: 24),

          const Text(
            'Semester Course Transcripts',
            style: TextStyle(
              fontSize: 18,
              fontWeight: FontWeight.w700,
              color: AppColors.textPrimaryLight,
            ),
          ),
          const SizedBox(height: 12),

          ...results.map((res) => Container(
                margin: const EdgeInsets.only(bottom: 10),
                padding: const EdgeInsets.all(16),
                decoration: BoxDecoration(
                  color: Colors.white,
                  borderRadius: BorderRadius.circular(14),
                  border: Border.all(color: AppColors.borderLight),
                ),
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Expanded(
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Text(
                            res.courseCode,
                            style: const TextStyle(
                              fontSize: 12,
                              fontWeight: FontWeight.w700,
                              color: AppColors.primary,
                            ),
                          ),
                          const SizedBox(height: 2),
                          Text(
                            res.courseTitle,
                            style: const TextStyle(
                              fontSize: 14.5,
                              fontWeight: FontWeight.w700,
                              color: AppColors.textPrimaryLight,
                            ),
                          ),
                          const SizedBox(height: 2),
                          Text(
                            'Credits: ${res.credits} • Grade Point: ${res.gradePoint}',
                            style: const TextStyle(
                              fontSize: 12,
                              color: AppColors.textSecondaryLight,
                            ),
                          ),
                        ],
                      ),
                    ),
                    Container(
                      padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 8),
                      decoration: BoxDecoration(
                        color: AppColors.successLight,
                        borderRadius: BorderRadius.circular(10),
                      ),
                      child: Text(
                        res.grade,
                        style: const TextStyle(
                          fontSize: 18,
                          fontWeight: FontWeight.w800,
                          color: AppColors.success,
                        ),
                      ),
                    ),
                  ],
                ),
              )),
        ],
      ),
    );
  }
}
