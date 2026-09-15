import 'package:flutter/material.dart';
import '../../core/theme/app_colors.dart';
import '../../services/mock_data_service.dart';

/// Interactive UniSphere Campus AI Assistant Chat Screen.
class AiAssistantScreen extends StatefulWidget {
  const AiAssistantScreen({super.key});

  @override
  State<AiAssistantScreen> createState() => _AiAssistantScreenState();
}

class _AiAssistantScreenState extends State<AiAssistantScreen> {
  final List<Map<String, dynamic>> _messages = [
    {
      'isAi': true,
      'text':
          'Hello Alex! I am your UniSphere AI Campus Assistant. Ask me anything about your attendance, exam schedule, placement drives, courses, or campus rules.',
      'time': 'Just now',
    },
  ];

  final TextEditingController _controller = TextEditingController();
  bool _isTyping = false;

  void _sendQuery(String prompt) {
    if (prompt.trim().isEmpty) return;

    setState(() {
      _messages.add({
        'isAi': false,
        'text': prompt,
        'time': 'Just now',
      });
      _isTyping = true;
      _controller.clear();
    });

    // Simulate AI response delay
    Future.delayed(const Duration(milliseconds: 700), () {
      if (!mounted) return;
      final answer = MockDataService.getAiAnswer(prompt);
      setState(() {
        _isTyping = false;
        _messages.add({
          'isAi': true,
          'text': answer,
          'time': 'Just now',
        });
      });
    });
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final suggestions = [
      'What is my attendance status?',
      'When do my midterm exams start?',
      'Are there active placement drives?',
      'Tell me about the digital library access',
    ];

    return Scaffold(
      backgroundColor: AppColors.backgroundLight,
      appBar: AppBar(
        title: Row(
          children: [
            Container(
              padding: const EdgeInsets.all(6),
              decoration: BoxDecoration(
                gradient: const LinearGradient(
                  colors: [AppColors.primary, AppColors.secondary],
                ),
                borderRadius: BorderRadius.circular(8),
              ),
              child: const Icon(Icons.auto_awesome, color: Colors.white, size: 16),
            ),
            const SizedBox(width: 10),
            const Text('UniSphere AI Concierge'),
          ],
        ),
      ),
      body: Column(
        children: [
          // Chat history
          Expanded(
            child: ListView.builder(
              padding: const EdgeInsets.all(16),
              itemCount: _messages.length,
              itemBuilder: (context, index) {
                final msg = _messages[index];
                final isAi = msg['isAi'] as bool;

                return Align(
                  alignment: isAi ? Alignment.centerLeft : Alignment.centerRight,
                  child: Container(
                    margin: const EdgeInsets.symmetric(vertical: 6),
                    padding: const EdgeInsets.all(14),
                    constraints: BoxConstraints(
                      maxWidth: MediaQuery.of(context).size.width * 0.82,
                    ),
                    decoration: BoxDecoration(
                      color: isAi ? Colors.white : AppColors.primary,
                      borderRadius: BorderRadius.circular(16),
                      border: isAi ? Border.all(color: AppColors.borderLight) : null,
                      boxShadow: [
                        BoxShadow(
                          color: Colors.black.withOpacity(0.04),
                          blurRadius: 6,
                          offset: const Offset(0, 2),
                        ),
                      ],
                    ),
                    child: Column(
                      crossAxisAlignment:
                          isAi ? CrossAxisAlignment.start : CrossAxisAlignment.end,
                      children: [
                        if (isAi)
                          Row(
                            children: const [
                              Icon(Icons.smart_toy_outlined, size: 14, color: AppColors.primary),
                              SizedBox(width: 4),
                              Text(
                                'UniSphere AI',
                                style: TextStyle(
                                  fontSize: 11,
                                  fontWeight: FontWeight.w700,
                                  color: AppColors.primary,
                                ),
                              ),
                            ],
                          ),
                        const SizedBox(height: 4),
                        Text(
                          msg['text'].toString(),
                          style: TextStyle(
                            fontSize: 14,
                            color: isAi ? AppColors.textPrimaryLight : Colors.white,
                            height: 1.4,
                          ),
                        ),
                      ],
                    ),
                  ),
                );
              },
            ),
          ),

          if (_isTyping)
            Padding(
              padding: const EdgeInsets.only(left: 20, bottom: 8),
              child: Row(
                children: const [
                  SizedBox(
                    width: 14,
                    height: 14,
                    child: CircularProgressIndicator(strokeWidth: 2),
                  ),
                  SizedBox(width: 8),
                  Text('UniSphere AI is thinking...',
                      style: TextStyle(fontSize: 12, color: AppColors.textSecondaryLight)),
                ],
              ),
            ),

          // Quick Prompt Suggestions
          Container(
            padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 8),
            color: Colors.white,
            child: SingleChildScrollView(
              scrollDirection: Axis.horizontal,
              child: Row(
                children: suggestions.map((s) {
                  return Padding(
                    padding: const EdgeInsets.only(right: 8),
                    child: ActionChip(
                      label: Text(s, style: const TextStyle(fontSize: 11.5)),
                      onPressed: () => _sendQuery(s),
                      backgroundColor: AppColors.surfaceElevatedLight,
                    ),
                  );
                }).toList(),
              ),
            ),
          ),

          // Input Bar
          Container(
            padding: const EdgeInsets.all(12),
            color: Colors.white,
            child: SafeArea(
              child: Row(
                children: [
                  Expanded(
                    child: TextField(
                      controller: _controller,
                      decoration: InputDecoration(
                        hintText: 'Ask campus AI assistant...',
                        contentPadding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
                        border: OutlineInputBorder(
                          borderRadius: BorderRadius.circular(24),
                          borderSide: const BorderSide(color: AppColors.borderLight),
                        ),
                      ),
                      onSubmitted: _sendQuery,
                    ),
                  ),
                  const SizedBox(width: 8),
                  CircleAvatar(
                    backgroundColor: AppColors.primary,
                    child: IconButton(
                      icon: const Icon(Icons.send_rounded, color: Colors.white, size: 18),
                      onPressed: () => _sendQuery(_controller.text),
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
