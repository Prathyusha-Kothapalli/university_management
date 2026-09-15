import "package:flutter/material.dart";
import "transport_models.dart";

class TransportMainScreen extends StatefulWidget {
  const TransportMainScreen({Key? key}) : super(key: key);
  @override
  State<TransportMainScreen> createState() => _TransportMainScreenState();
}

class _TransportMainScreenState extends State<TransportMainScreen> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("Transport & Fleet Logistics"), backgroundColor: Colors.indigo),
      body: ListView.builder(
        itemCount: 100,
        padding: const EdgeInsets.all(16),
        itemBuilder: (context, index) {
          return Card(
            elevation: 2,
            margin: const EdgeInsets.only(bottom: 12),
            child: ListTile(
              leading: CircleAvatar(backgroundColor: Colors.indigo.shade100, child: Text("${index + 1}")),
              title: Text("Transport & Fleet Logistics Record #${index + 1}", style: const TextStyle(fontWeight: FontWeight.bold)),
              subtitle: Text("Code: TRANSPORT-M-${index + 100}"),
              trailing: const Icon(Icons.arrow_forward_ios, size: 16),
            ),
          );
        },
      ),
    );
  }
}
