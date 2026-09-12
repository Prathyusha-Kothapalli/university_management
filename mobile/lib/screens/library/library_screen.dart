import 'package:flutter/material.dart';
import '../../core/theme/app_colors.dart';

class LibraryScreen extends StatefulWidget {
  const LibraryScreen({super.key});

  @override
  State<LibraryScreen> createState() => _LibraryScreenState();
}

class _LibraryScreenState extends State<LibraryScreen> with SingleTickerProviderStateMixin {
  late TabController _tabController;

  final List<Map<String, String>> _books = [
    {
      'title': 'Designing Data-Intensive Applications',
      'author': 'Martin Kleppmann',
      'category': 'Computer Science',
      'isbn': '978-1449373320',
      'copies': '3 / 8 Available',
      'shelf': 'Shelf CS-04',
    },
    {
      'title': 'Clean Code: Handbook of Software Craftsmanship',
      'author': 'Robert C. Martin',
      'category': 'Software Eng',
      'isbn': '978-0132350884',
      'copies': '1 / 5 Available',
      'shelf': 'Shelf CS-02',
    },
    {
      'title': 'Introduction to Algorithms (CLRS 4th Ed)',
      'author': 'Cormen, Leiserson, Rivest, Stein',
      'category': 'Algorithms',
      'isbn': '978-0262046305',
      'copies': '5 / 12 Available',
      'shelf': 'Shelf CS-01',
    },
  ];

  final List<Map<String, String>> _borrowed = [
    {
      'title': 'Database System Concepts (7th Ed)',
      'author': 'Silberschatz, Korth, Sudarshan',
      'dueDate': '14 Sep 2026',
      'status': 'Due Soon',
    },
    {
      'title': 'Artificial Intelligence: A Modern Approach',
      'author': 'Stuart Russell & Peter Norvig',
      'dueDate': '28 Sep 2026',
      'status': 'Issued',
    },
  ];

  @override
  void initState() {
    super.initState();
    _tabController = TabController(length: 2, vsync: this);
  }

  @override
  void dispose() {
    _tabController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFF090D16),
      appBar: AppBar(
        title: const Text('Central Library & Digital Pass', style: TextStyle(fontWeight: FontWeight.bold, color: Colors.white)),
        backgroundColor: const Color(0xFF0F172A),
        bottom: TabBar(
          controller: _tabController,
          indicatorColor: AppColors.primary,
          labelColor: AppColors.primary,
          unselectedLabelColor: Colors.grey,
          tabs: const [
            Tab(icon: Icon(Icons.menu_book), text: 'Book Catalog'),
            Tab(icon: Icon(Icons.bookmark_added), text: 'My Loans'),
          ],
        ),
      ),
      body: TabBarView(
        controller: _tabController,
        children: [
          // Catalog Tab
          ListView.builder(
            padding: const EdgeInsets.all(16),
            itemCount: _books.length,
            itemBuilder: (context, index) {
              final b = _books[index];
              return Card(
                color: const Color(0xFF1E293B),
                margin: const EdgeInsets.only(bottom: 12),
                shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
                child: ListTile(
                  leading: CircleAvatar(
                    backgroundColor: AppColors.primary.withOpacity(0.2),
                    child: const Icon(Icons.book, color: AppColors.primary),
                  ),
                  title: Text(b['title']!, style: const TextStyle(color: Colors.white, fontWeight: FontWeight.bold, fontSize: 14)),
                  subtitle: Text('${b['author']} • ${b['shelf']}', style: const TextStyle(color: Colors.grey, fontSize: 12)),
                  trailing: Container(
                    padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
                    decoration: BoxDecoration(
                      color: AppColors.primary.withOpacity(0.15),
                      borderRadius: BorderRadius.circular(8),
                    ),
                    child: Text(b['copies']!, style: const TextStyle(color: AppColors.primary, fontSize: 11, fontWeight: FontWeight.bold)),
                  ),
                ),
              );
            },
          ),

          // Loans Tab
          ListView.builder(
            padding: const EdgeInsets.all(16),
            itemCount: _borrowed.length,
            itemBuilder: (context, index) {
              final item = _borrowed[index];
              final isDueSoon = item['status'] == 'Due Soon';
              return Card(
                color: const Color(0xFF1E293B),
                margin: const EdgeInsets.only(bottom: 12),
                shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
                child: ListTile(
                  leading: CircleAvatar(
                    backgroundColor: isDueSoon ? Colors.orange.withOpacity(0.2) : Colors.green.withOpacity(0.2),
                    child: Icon(Icons.timer, color: isDueSoon ? Colors.orange : Colors.green),
                  ),
                  title: Text(item['title']!, style: const TextStyle(color: Colors.white, fontWeight: FontWeight.bold, fontSize: 14)),
                  subtitle: Text('Due: ${item['dueDate']}', style: TextStyle(color: isDueSoon ? Colors.orange : Colors.grey, fontSize: 12, fontWeight: isDueSoon ? FontWeight.bold : FontWeight.normal)),
                  trailing: ElevatedButton(
                    onPressed: () {
                      ScaffoldMessenger.of(context).showSnackBar(
                        SnackBar(content: Text('Extended loan for "${item['title']}" by +14 days')),
                      );
                    },
                    style: ElevatedButton.styleFrom(backgroundColor: const Color(0xFF2563EB), foregroundColor: Colors.white),
                    child: const Text('Extend', style: TextStyle(fontSize: 11)),
                  ),
                ),
              );
            },
          ),
        ],
      ),
    );
  }
}
