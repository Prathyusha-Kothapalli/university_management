import "package:flutter/material.dart";
import "placements_models.dart";

class PlacementsMainScreen extends StatefulWidget {
  const PlacementsMainScreen({Key? key}) : super(key: key);
  @override
  State<PlacementsMainScreen> createState() => _PlacementsMainScreenState();
}

class _PlacementsMainScreenState extends State<PlacementsMainScreen> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("Placements & Alumni Network"), backgroundColor: Colors.indigo),
      body: ListView.builder(
        itemCount: 50,
        padding: const EdgeInsets.all(16),
        itemBuilder: (context, index) {
          return Card(
            elevation: 2,
            margin: const EdgeInsets.only(bottom: 12),
            child: ListTile(
              leading: CircleAvatar(backgroundColor: Colors.indigo.shade100, child: Text("${index + 1}")),
              title: Text("Placements & Alumni Network Record #${index + 1}", style: const TextStyle(fontWeight: FontWeight.bold)),
              subtitle: Text("Code: PLACEMENTS-M-${index + 100}"),
              trailing: const Icon(Icons.arrow_forward_ios, size: 16),
            ),
          );
        },
      ),
    );
  }
}
