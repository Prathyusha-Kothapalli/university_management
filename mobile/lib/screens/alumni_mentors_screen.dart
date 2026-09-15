import 'flutter/material.dart';

class AlumniMentorsScreen extends StatefulWidget {
  const AlumniMentorsScreen({Key? key}) : super(key: key);

  @override
  State<AlumniMentorsScreen> createState() => _AlumniMentorsScreenState();
}

class _AlumniMentorsScreenState extends State<AlumniMentorsScreen> {
  final List<Map<String, String>> _mentors = [
    {
      "name": "David Miller",
      "company": "Google",
      "designation": "Senior Staff Software Engineer",
      "year": "Class of 2018",
    },
    {
      "name": "Elena Rostova",
      "company": "OpenAI",
      "designation": "Research Scientist - Multi-Agent AI",
      "year": "Class of 2020",
    }
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFF0F172A),
      appBar: AppBar(
        backgroundColor: const Color(0xFF1E293B),
        title: const Text(
          'Alumni Mentor Network',
          style: TextStyle(fontWeight: FontWeight.bold, color: Colors.white),
        ),
        elevation: 0,
      ),
      body: ListView.builder(
        padding: const EdgeInsets.all(16),
        itemCount: _mentors.length,
        itemBuilder: (context, index) {
          final mentor = _mentors[index];
          return Card(
            color: const Color(0xFF1E293B),
            margin: const EdgeInsets.only(bottom: 12),
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(12),
              side: const BorderSide(color: Color(0xFF334155)),
            ),
            child: ListTile(
              contentPadding: const EdgeInsets.all(16),
              title: Text(
                mentor['name']!,
                style: const TextStyle(color: Colors.white, fontWeight: FontWeight.bold, fontSize: 16),
              ),
              subtitle: Padding(
                padding: const EdgeInsets.only(top: 6),
                child: Text(
                  '${mentor['designation']} at ${mentor['company']}\n${mentor['year']}',
                  style: const TextStyle(color: Colors.white70, fontSize: 13),
                ),
              ),
              trailing: ElevatedButton(
                style: ElevatedButton.styleFrom(backgroundColor: Colors.indigoAccent),
                onPressed: () {},
                child: const Text('Connect', style: TextStyle(color: Colors.white)),
              ),
            ),
          );
        },
      ),
    );
  }
}
