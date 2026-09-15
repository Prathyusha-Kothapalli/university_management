import 'package:flutter/material.dart';
import 'health_model.dart';

class HealthScreen extends StatefulWidget {
  const HealthScreen({Key? key}) : super(key: key);

  @override
  State<HealthScreen> createState() => _HealthScreenState();
}

class _HealthScreenState extends State<HealthScreen> {
  final List<HealthModel> _items = [
    HealthModel(
      id: 1,
      entityCode: 'HEALTH_M01',
      name: 'Campus Health & Clinic Management Primary Record',
      category: 'Mobile',
      status: 'ACTIVE',
      createdAt: DateTime.now(),
    ),
    HealthModel(
      id: 2,
      entityCode: 'HEALTH_M02',
      name: 'Campus Health & Clinic Management Secondary Sync',
      category: 'System',
      status: 'ACTIVE',
      createdAt: DateTime.now(),
    ),
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Campus Health & Clinic Management'),
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
