import "package:flutter/material.dart";
import "hostels_models.dart";

class HostelsMainScreen extends StatefulWidget {
  const HostelsMainScreen({Key? key}) : super(key: key);
  @override
  State<HostelsMainScreen> createState() => _HostelsMainScreenState();
}

class _HostelsMainScreenState extends State<HostelsMainScreen> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("Student Life & Hostel Operations"), backgroundColor: Colors.indigo),
      body: ListView.builder(
        itemCount: 50,
        padding: const EdgeInsets.all(16),
        itemBuilder: (context, index) {
          return Card(
            elevation: 2,
            margin: const EdgeInsets.only(bottom: 12),
            child: ListTile(
              leading: CircleAvatar(backgroundColor: Colors.indigo.shade100, child: Text("${index + 1}")),
              title: Text("Student Life & Hostel Operations Record #${index + 1}", style: const TextStyle(fontWeight: FontWeight.bold)),
              subtitle: Text("Code: HOSTELS-M-${index + 100}"),
              trailing: const Icon(Icons.arrow_forward_ios, size: 16),
            ),
          );
        },
      ),
    );
  }
}
