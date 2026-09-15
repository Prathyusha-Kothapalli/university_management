import 'package:flutter/material.dart';
import 'hostels_model.dart';

class HostelsScreen extends StatefulWidget {
  const HostelsScreen({Key? key}) : super(key: key);

  @override
  State<HostelsScreen> createState() => _HostelsScreenState();
}

class _HostelsScreenState extends State<HostelsScreen> {
  final List<HostelsModel> _items = [
    HostelsModel(
      id: 1,
      entityCode: 'HOSTELS_M01',
      name: 'Student Life & Hostel Operations Primary Record',
      category: 'Mobile',
      status: 'ACTIVE',
      createdAt: DateTime.now(),
    ),
    HostelsModel(
      id: 2,
      entityCode: 'HOSTELS_M02',
      name: 'Student Life & Hostel Operations Secondary Sync',
      category: 'System',
      status: 'ACTIVE',
      createdAt: DateTime.now(),
    ),
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Student Life & Hostel Operations'),
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
