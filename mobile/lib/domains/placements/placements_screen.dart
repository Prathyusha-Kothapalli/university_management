import 'package:flutter/material.dart';
import 'placements_model.dart';

class PlacementsScreen extends StatefulWidget {
  const PlacementsScreen({Key? key}) : super(key: key);

  @override
  State<PlacementsScreen> createState() => _PlacementsScreenState();
}

class _PlacementsScreenState extends State<PlacementsScreen> {
  final List<PlacementsModel> _items = [
    PlacementsModel(
      id: 1,
      entityCode: 'PLACEMENTS_M01',
      name: 'Placements & Alumni Network Primary Record',
      category: 'Mobile',
      status: 'ACTIVE',
      createdAt: DateTime.now(),
    ),
    PlacementsModel(
      id: 2,
      entityCode: 'PLACEMENTS_M02',
      name: 'Placements & Alumni Network Secondary Sync',
      category: 'System',
      status: 'ACTIVE',
      createdAt: DateTime.now(),
    ),
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Placements & Alumni Network'),
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
