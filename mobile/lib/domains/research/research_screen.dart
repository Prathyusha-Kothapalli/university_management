import "package:flutter/material.dart";
import "research_models.dart";

class ResearchMainScreen extends StatefulWidget {
  const ResearchMainScreen({Key? key}) : super(key: key);
  @override
  State<ResearchMainScreen> createState() => _ResearchMainScreenState();
}

class _ResearchMainScreenState extends State<ResearchMainScreen> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("Research, Grants & Lab Inventory"), backgroundColor: Colors.indigo),
      body: ListView.builder(
        itemCount: 75,
        padding: const EdgeInsets.all(16),
        itemBuilder: (context, index) {
          return Card(
            elevation: 2,
            margin: const EdgeInsets.only(bottom: 12),
            child: ListTile(
              leading: CircleAvatar(backgroundColor: Colors.indigo.shade100, child: Text("${index + 1}")),
              title: Text("Research, Grants & Lab Inventory Record #${index + 1}", style: const TextStyle(fontWeight: FontWeight.bold)),
              subtitle: Text("Code: RESEARCH-M-${index + 100}"),
              trailing: const Icon(Icons.arrow_forward_ios, size: 16),
            ),
          );
        },
      ),
    );
  }
}
