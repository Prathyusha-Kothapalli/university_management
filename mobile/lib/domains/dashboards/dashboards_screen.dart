import 'package:flutter/material.dart';
import 'dashboards_model.dart';

class DashboardsScreen extends StatefulWidget {
  const DashboardsScreen({Key? key}) : super(key: key);

  @override
  State<DashboardsScreen> createState() => _DashboardsScreenState();
}

class _DashboardsScreenState extends State<DashboardsScreen> {
  final List<DashboardsModel> _items = [
    DashboardsModel(
      id: 1,
      entityCode: 'DASHBOARDS_M01',
      name: 'Executive & Departmental Dashboards Primary Record',
      category: 'Mobile',
      status: 'ACTIVE',
      createdAt: DateTime.now(),
    ),
    DashboardsModel(
      id: 2,
      entityCode: 'DASHBOARDS_M02',
      name: 'Executive & Departmental Dashboards Secondary Sync',
      category: 'System',
      status: 'ACTIVE',
      createdAt: DateTime.now(),
    ),
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Executive & Departmental Dashboards'),
        backgroundColor: Colors.indigo,
      ),
      body: ListView.builder(
        itemCount: _items.length,
        padding: const EdgeInsets.all(16),
        itemBuilder: (context, index) {
          final item = _items[index];
          return Card(
            elevation: 2,
            margin: const EdgeInsets.only(bottom: 12),
            child: ListTile(
              leading: CircleAvatar(
                backgroundColor: Colors.indigo.shade100,
                child: Text(item.entityCode.substring(0, 2)),
              ),
              title: Text(item.name, style: const TextStyle(fontWeight: FontWeight.bold)),
              subtitle: Text('${item.category} • ${item.status}'),
              trailing: const Icon(Icons.arrow_forward_ios, size: 16),
              onTap: () {
                // Navigate to details
              },
            ),
          );
        },
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {},
        backgroundColor: Colors.indigo,
        child: const Icon(Icons.add),
      ),
    );
  }
}
