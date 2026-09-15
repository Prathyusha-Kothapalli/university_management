import "package:flutter/material.dart";
import "hr_models.dart";

class HrMainScreen extends StatefulWidget {
  const HrMainScreen({Key? key}) : super(key: key);
  @override
  State<HrMainScreen> createState() => _HrMainScreenState();
}

class _HrMainScreenState extends State<HrMainScreen> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("Human Resources & Faculty Management"), backgroundColor: Colors.indigo),
      body: ListView.builder(
        itemCount: 75,
        padding: const EdgeInsets.all(16),
        itemBuilder: (context, index) {
          return Card(
            elevation: 2,
            margin: const EdgeInsets.only(bottom: 12),
            child: ListTile(
              leading: CircleAvatar(backgroundColor: Colors.indigo.shade100, child: Text("${index + 1}")),
              title: Text("Human Resources & Faculty Management Record #${index + 1}", style: const TextStyle(fontWeight: FontWeight.bold)),
              subtitle: Text("Code: HR-M-${index + 100}"),
              trailing: const Icon(Icons.arrow_forward_ios, size: 16),
            ),
          );
        },
      ),
    );
  }
}
