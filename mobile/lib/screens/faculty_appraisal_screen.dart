import 'flutter/material.dart';

class FacultyAppraisalScreen extends StatefulWidget {
  const FacultyAppraisalScreen({Key? key}) : super(key: key);

  @override
  State<FacultyAppraisalScreen> createState() => _FacultyAppraisalScreenState();
}

class _FacultyAppraisalScreenState extends State<FacultyAppraisalScreen> {
  double _teachingScore = 4.5;
  double _researchScore = 4.0;
  double _serviceScore = 4.2;

  double get _overallScore => (_teachingScore * 0.4) + (_researchScore * 0.4) + (_serviceScore * 0.2);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFF0F172A),
      appBar: AppBar(
        backgroundColor: const Color(0xFF1E293B),
        title: const Text(
          'Faculty Appraisal Portal',
          style: TextStyle(fontWeight: FontWeight.bold, color: Colors.white),
        ),
        elevation: 0,
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Container(
              padding: const EdgeInsets.all(16),
              decoration: BoxDecoration(
                color: const Color(0xFF1E293B),
                borderRadius: BorderRadius.circular(12),
                border: Border.all(color: const Color(0xFF334155)),
              ),
              child: Column(
                children: [
                  const Text(
                    'Overall Performance Score',
                    style: TextStyle(color: Colors.white70, fontSize: 14),
                  ),
                  const SizedBox(height: 8),
                  Text(
                    '${_overallScore.toStringAsFixed(2)} / 5.0',
                    style: const TextStyle(
                      color: Colors.indigoAccent,
                      fontSize: 28,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                ],
              ),
            ),
            const SizedBox(height: 20),
            const Text(
              'Self Assessment Scores',
              style: TextStyle(color: Colors.white, fontSize: 16, fontWeight: FontWeight.bold),
            ),
            const SizedBox(height: 12),
            _buildScoreSlider('Teaching (40%)', _teachingScore, (val) => setState(() => _teachingScore = val)),
            _buildScoreSlider('Research (40%)', _researchScore, (val) => setState(() => _researchScore = val)),
            _buildScoreSlider('Service (20%)', _serviceScore, (val) => setState(() => _serviceScore = val)),
          ],
        ),
      ),
    );
  }

  Widget _buildScoreSlider(String label, double value, ValueChanged<double> onChanged) {
    return Container(
      margin: const EdgeInsets.only(bottom: 12),
      padding: const EdgeInsets.all(12),
      decoration: BoxDecoration(
        color: const Color(0xFF1E293B),
        borderRadius: BorderRadius.circular(10),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Text(label, style: const TextStyle(color: Colors.white, fontSize: 14)),
              Text(value.toStringAsFixed(1), style: const TextStyle(color: Colors.indigoAccent, fontWeight: FontWeight.bold)),
            ],
          ),
          Slider(
            value: value,
            min: 1.0,
            max: 5.0,
            divisions: 40,
            activeColor: Colors.indigoAccent,
            onChanged: onChanged,
          ),
        ],
      ),
    );
  }
}
