import "package:flutter/material.dart";
import "dashboards_models.dart";

class DashboardsMainScreen extends StatefulWidget {
  const DashboardsMainScreen({Key? key}) : super(key: key);
  @override
  State<DashboardsMainScreen> createState() => _DashboardsMainScreenState();
}

class _DashboardsMainScreenState extends State<DashboardsMainScreen> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("Executive & Departmental Dashboards"), backgroundColor: Colors.indigo),
      body: ListView.builder(
        itemCount: 100,
        padding: const EdgeInsets.all(16),
        itemBuilder: (context, index) {
          return Card(
            elevation: 2,
            margin: const EdgeInsets.only(bottom: 12),
            child: ListTile(
              leading: CircleAvatar(backgroundColor: Colors.indigo.shade100, child: Text("${index + 1}")),
              title: Text("Executive & Departmental Dashboards Record #${index + 1}", style: const TextStyle(fontWeight: FontWeight.bold)),
              subtitle: Text("Code: DASHBOARDS-M-${index + 100}"),
              trailing: const Icon(Icons.arrow_forward_ios, size: 16),
            ),
          );
        },
      ),
    );
  }
}
