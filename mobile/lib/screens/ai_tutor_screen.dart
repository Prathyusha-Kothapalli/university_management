import 'flutter/material.dart';

class AiTutorScreen extends StatefulWidget {
  const AiTutorScreen({Key? key}) : super(key: key);

  @override
  State<AiTutorScreen> createState() => _AiTutorScreenState();
}

class _AiTutorScreenState extends State<AiTutorScreen> {
  final TextEditingController _queryController = TextEditingController();
  final List<Map<String, String>> _messages = [
    {
      "sender": "ai",
      "text": "Hello! I am your UniSphere AI Academic Tutor. How can I assist you with regulations, course materials, or timetable schedules today?"
    }
  ];

  void _sendMessage() {
    if (_queryController.text.trim().isEmpty) return;
    setState(() {
      _messages.add({"sender": "user", "text": _queryController.text});
      _messages.add({
        "sender": "ai",
        "text": "Based on the institutional knowledge base, minimum attendance requirement is 75% under Academic Regulations 2026."
      });
      _queryController.clear();
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFF0F172A),
      appBar: AppBar(
        backgroundColor: const Color(0xFF1E293B),
        title: const Text(
          'UniSphere AI Tutor',
          style: TextStyle(fontWeight: FontWeight.bold, color: Colors.white),
        ),
        elevation: 0,
      ),
      body: Column(
        children: [
          Expanded(
            child: ListView.builder(
              padding: const EdgeInsets.all(16),
              itemCount: _messages.length,
              itemBuilder: (context, index) {
                final msg = _messages[index];
                final bool isUser = msg['sender'] == 'user';
                return Align(
                  alignment: isUser ? Alignment.centerRight : Alignment.centerLeft,
                  child: Container(
                    margin: const EdgeInsets.only(bottom: 12),
                    padding: const EdgeInsets.all(14),
                    constraints: BoxConstraints(maxWidth: MediaQuery.of(context).size.width * 0.8),
                    decoration: BoxDecoration(
                      color: isUser ? Colors.indigoAccent : const Color(0xFF1E293B),
                      borderRadius: BorderRadius.circular(12),
                      border: isUser ? null : Border.all(color: const Color(0xFF334155)),
                    ),
                    child: Text(
                      msg['text']!,
                      style: const TextStyle(color: Colors.white, fontSize: 14),
                    ),
                  ),
                );
              },
            ),
          ),
          Container(
            padding: const EdgeInsets.all(12),
            color: const Color(0xFF1E293B),
            child: Row(
              children: [
                Expanded(
                  child: TextField(
                    controller: _queryController,
                    style: const TextStyle(color: Colors.white),
                    decoration: const InputDecoration(
                      hintText: 'Ask AI tutor a question...',
                      hintStyle: TextStyle(color: Colors.white54),
                      border: InputBorder.none,
                    ),
                  ),
                ),
                IconButton(
                  icon: const Icon(Icons.send, color: Colors.indigoAccent),
                  onPressed: _sendMessage,
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
