import 'package:flutter/material.dart';

class TransportSubWidget2 extends StatelessWidget {
  final String title;
  const TransportSubWidget2({Key? key, required this.title}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.all(12),
      decoration: BoxDecoration(
        color: Colors.grey.shade100,
        borderRadius: BorderRadius.circular(8),
      ),
      child: Row(
        children: [
          const Icon(Icons.check_circle, color: Colors.green),
          const SizedBox(width: 8),
          Text('$title - SubWidget #2'),
        ],
      ),
    );
  }
}
