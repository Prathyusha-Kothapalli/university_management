import "package:flutter/material.dart";
import "exams_models.dart";

class ExamsMainScreen extends StatefulWidget {
  const ExamsMainScreen({Key? key}) : super(key: key);
  @override
  State<ExamsMainScreen> createState() => _ExamsMainScreenState();
}

class _ExamsMainScreenState extends State<ExamsMainScreen> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("Examinations & Result Management"), backgroundColor: Colors.indigo),
      body: ListView.builder(
        itemCount: 100,
        padding: const EdgeInsets.all(16),
        itemBuilder: (context, index) {
          return Card(
            elevation: 2,
            margin: const EdgeInsets.only(bottom: 12),
            child: ListTile(
              leading: CircleAvatar(backgroundColor: Colors.indigo.shade100, child: Text("${index + 1}")),
              title: Text("Examinations & Result Management Record #${index + 1}", style: const TextStyle(fontWeight: FontWeight.bold)),
              subtitle: Text("Code: EXAMS-M-${index + 100}"),
              trailing: const Icon(Icons.arrow_forward_ios, size: 16),
            ),
          );
        },
      ),
    );
  }
}
