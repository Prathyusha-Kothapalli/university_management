import "package:flutter/material.dart";
import "sports_models.dart";

class SportsMainScreen extends StatefulWidget {
  const SportsMainScreen({Key? key}) : super(key: key);
  @override
  State<SportsMainScreen> createState() => _SportsMainScreenState();
}

class _SportsMainScreenState extends State<SportsMainScreen> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("Sports & Extracurricular Activities"), backgroundColor: Colors.indigo),
      body: ListView.builder(
        itemCount: 100,
        padding: const EdgeInsets.all(16),
        itemBuilder: (context, index) {
          return Card(
            elevation: 2,
            margin: const EdgeInsets.only(bottom: 12),
            child: ListTile(
              leading: CircleAvatar(backgroundColor: Colors.indigo.shade100, child: Text("${index + 1}")),
              title: Text("Sports & Extracurricular Activities Record #${index + 1}", style: const TextStyle(fontWeight: FontWeight.bold)),
              subtitle: Text("Code: SPORTS-M-${index + 100}"),
              trailing: const Icon(Icons.arrow_forward_ios, size: 16),
            ),
          );
        },
      ),
    );
  }
}
