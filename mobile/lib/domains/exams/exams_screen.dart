import 'package:flutter/material.dart';
import 'exams_model.dart';

class ExamsScreen extends StatefulWidget {
  const ExamsScreen({Key? key}) : super(key: key);

  @override
  State<ExamsScreen> createState() => _ExamsScreenState();
}

class _ExamsScreenState extends State<ExamsScreen> {
  final List<ExamsModel> _items = [
    ExamsModel(
      id: 1,
      entityCode: 'EXAMS_M01',
      name: 'Examinations & Result Management Primary Record',
      category: 'Mobile',
      status: 'ACTIVE',
      createdAt: DateTime.now(),
    ),
    ExamsModel(
      id: 2,
      entityCode: 'EXAMS_M02',
      name: 'Examinations & Result Management Secondary Sync',
      category: 'System',
      status: 'ACTIVE',
      createdAt: DateTime.now(),
    ),
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Examinations & Result Management'),
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
