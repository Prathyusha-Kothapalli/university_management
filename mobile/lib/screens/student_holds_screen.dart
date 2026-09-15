import 'flutter/material.dart';

class StudentHoldsScreen extends StatefulWidget {
  const StudentHoldsScreen({Key? key}) : super(key: key);

  @override
  State<StudentHoldsScreen> createState() => _StudentHoldsScreenState();
}

class _StudentHoldsScreenState extends State<StudentHoldsScreen> {
  final List<Map<String, String>> _holds = [
    {
      "id": "hold-01",
      "type": "FINANCIAL",
      "reason": "Outstanding semester fee payment balance (\$1,200).",
      "date": "2026-02-28",
      "status": "ACTIVE"
    },
    {
      "id": "hold-02",
      "type": "DOCUMENT_MISSING",
      "reason": "High school final transcript physical copy verification required.",
      "date": "2026-03-05",
      "status": "ACTIVE"
    }
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFF0F172A),
      appBar: AppBar(
        backgroundColor: const Color(0xFF1E293B),
        title: const Text(
          'Academic Holds & Advising',
          style: TextStyle(fontWeight: FontWeight.bold, color: Colors.white),
        ),
        elevation: 0,
      ),
      body: ListView.builder(
        padding: const EdgeInsets.all(16),
        itemCount: _holds.length,
        itemBuilder: (context, index) {
          final hold = _holds[index];
          return Card(
            color: const Color(0xFF1E293B),
            margin: const EdgeInsets.only(bottom: 12),
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(12),
              side: const BorderSide(color: Color(0xFF334155)),
            ),
            child: Padding(
              padding: const EdgeInsets.all(16),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      Container(
                        padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
                        decoration: BoxDecoration(
                          color: Colors.redAccent.withOpacity(0.2),
                          borderRadius: BorderRadius.circular(6),
                          border: Border.all(color: Colors.redAccent),
                        ),
                        child: Text(
                          hold['type']!,
                          style: const TextStyle(
                            color: Colors.redAccent,
                            fontSize: 12,
                            fontWeight: FontWeight.bold,
                          ),
                        ),
                      ),
                      Text(
                        hold['date']!,
                        style: const TextStyle(color: Colors.white70, fontSize: 12),
                      ),
                    ],
                  ),
                  const SizedBox(height: 12),
                  Text(
                    hold['reason']!,
                    style: const TextStyle(color: Colors.white, fontSize: 14),
                  ),
                ],
              ),
            ),
          );
        },
      ),
    );
  }
}
