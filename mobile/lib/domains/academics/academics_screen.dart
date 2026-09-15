import 'package:flutter/material.dart';
import 'academics_model.dart';

class AcademicsScreen extends StatefulWidget {
  const AcademicsScreen({Key? key}) : super(key: key);

  @override
  State<AcademicsScreen> createState() => _AcademicsScreenState();
}

class _AcademicsScreenState extends State<AcademicsScreen> {
  final List<AcademicsModel> _items = [
    AcademicsModel(
      id: 1,
      entityCode: 'ACADEMICS_M01',
      name: 'Academic & Curriculum Management Primary Record',
      category: 'Mobile',
      status: 'ACTIVE',
      createdAt: DateTime.now(),
    ),
    AcademicsModel(
      id: 2,
      entityCode: 'ACADEMICS_M02',
      name: 'Academic & Curriculum Management Secondary Sync',
      category: 'System',
      status: 'ACTIVE',
      createdAt: DateTime.now(),
    ),
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Academic & Curriculum Management'),
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
