import "package:flutter/material.dart";
import "academics_models.dart";

class AcademicsMainScreen extends StatefulWidget {
  const AcademicsMainScreen({Key? key}) : super(key: key);
  @override
  State<AcademicsMainScreen> createState() => _AcademicsMainScreenState();
}

class _AcademicsMainScreenState extends State<AcademicsMainScreen> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("Academic & Curriculum Management"), backgroundColor: Colors.indigo),
      body: ListView.builder(
        itemCount: 30,
        padding: const EdgeInsets.all(16),
        itemBuilder: (context, index) {
          return Card(
            elevation: 2,
            margin: const EdgeInsets.only(bottom: 12),
            child: ListTile(
              leading: CircleAvatar(backgroundColor: Colors.indigo.shade100, child: Text("${index + 1}")),
              title: Text("Academic & Curriculum Management Record #${index + 1}", style: const TextStyle(fontWeight: FontWeight.bold)),
              subtitle: Text("Code: ACADEMICS-M-${index + 100}"),
              trailing: const Icon(Icons.arrow_forward_ios, size: 16),
            ),
          );
        },
      ),
    );
  }
}
