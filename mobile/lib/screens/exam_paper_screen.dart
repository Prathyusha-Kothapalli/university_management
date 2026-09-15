import 'flutter/material.dart';

class ExamPaperScreen extends StatefulWidget {
  const ExamPaperScreen({Key? key}) : super(key: key);

  @override
  State<ExamPaperScreen> createState() => _ExamPaperScreenState();
}

class _ExamPaperScreenState extends State<ExamPaperScreen> {
  final List<Map<String, String>> _questions = [
    {
      "number": "1",
      "question": "What is the worst-case time complexity of QuickSort?",
      "optionA": "O(N log N)",
      "optionB": "O(N^2)",
      "optionC": "O(N)",
      "optionD": "O(1)",
    },
    {
      "number": "2",
      "question": "Which data structure operates on a Last In First Out (LIFO) order?",
      "optionA": "Queue",
      "optionB": "Array",
      "optionC": "Stack",
      "optionD": "Tree",
    }
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFF0F172A),
      appBar: AppBar(
        backgroundColor: const Color(0xFF1E293B),
        title: const Text(
          'Online Exam Session',
          style: TextStyle(fontWeight: FontWeight.bold, color: Colors.white),
        ),
        elevation: 0,
      ),
      body: ListView.builder(
        padding: const EdgeInsets.all(16),
        itemCount: _questions.length,
        itemBuilder: (context, index) {
          final q = _questions[index];
          return Card(
            color: const Color(0xFF1E293B),
            margin: const EdgeInsets.only(bottom: 16),
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(12),
              side: const BorderSide(color: Color(0xFF334155)),
            ),
            child: Padding(
              padding: const EdgeInsets.all(16),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    'Question ${q['number']}',
                    style: const TextStyle(color: Colors.indigoAccent, fontWeight: FontWeight.bold, fontSize: 12),
                  ),
                  const SizedBox(height: 8),
                  Text(
                    q['question']!,
                    style: const TextStyle(color: Colors.white, fontSize: 15, fontWeight: FontWeight.w600),
                  ),
                  const SizedBox(height: 12),
                  _buildOption(q['optionA']!),
                  _buildOption(q['optionB']!),
                  _buildOption(q['optionC']!),
                  _buildOption(q['optionD']!),
                ],
              ),
            ),
          );
        },
      ),
    );
  }

  Widget _buildOption(String optionText) {
    return Container(
      width: double.infinity,
      margin: const EdgeInsets.only(bottom: 8),
      padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 10),
      decoration: BoxDecoration(
        color: const Color(0xFF0F172A),
        borderRadius: BorderRadius.circular(8),
        border: Border.all(color: const Color(0xFF334155)),
      ),
      child: Text(
        optionText,
        style: const TextStyle(color: Colors.white70, fontSize: 13),
      ),
    );
  }
}
