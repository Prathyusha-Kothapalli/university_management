import 'flutter/material.dart';

class FeeInstallmentsScreen extends StatefulWidget {
  const FeeInstallmentsScreen({Key? key}) : super(key: key);

  @override
  State<FeeInstallmentsScreen> createState() => _FeeInstallmentsScreenState();
}

class _FeeInstallmentsScreenState extends State<FeeInstallmentsScreen> {
  final List<Map<String, dynamic>> _installments = [
    {"num": 1, "amount": 2500, "due": "Jan 15, 2026", "status": "PAID"},
    {"num": 2, "amount": 2500, "due": "Mar 15, 2026", "status": "PENDING"},
    {"num": 3, "amount": 2500, "due": "May 15, 2026", "status": "PENDING"},
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFF0F172A),
      appBar: AppBar(
        backgroundColor: const Color(0xFF1E293B),
        title: const Text(
          'Fee Payment Installments',
          style: TextStyle(fontWeight: FontWeight.bold, color: Colors.white),
        ),
        elevation: 0,
      ),
      body: ListView.builder(
        padding: const EdgeInsets.all(16),
        itemCount: _installments.length,
        itemBuilder: (context, index) {
          final inst = _installments[index];
          final bool isPaid = inst['status'] == 'PAID';
          return Card(
            color: const Color(0xFF1E293B),
            margin: const EdgeInsets.only(bottom: 12),
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(12),
              side: const BorderSide(color: Color(0xFF334155)),
            ),
            child: ListTile(
              contentPadding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
              leading: CircleAvatar(
                backgroundColor: isPaid ? Colors.emerald.withOpacity(0.2) : Colors.indigo.withOpacity(0.2),
                child: Text(
                  '#${inst['num']}',
                  style: TextStyle(
                    color: isPaid ? Colors.emeraldAccent : Colors.indigoAccent,
                    fontWeight: FontWeight.bold,
                  ),
                ),
              ),
              title: Text(
                '\$${inst['amount']}',
                style: const TextStyle(color: Colors.white, fontWeight: FontWeight.bold, fontSize: 16),
              ),
              subtitle: Text(
                'Due: ${inst['due']}',
                style: const TextStyle(color: Colors.white70, fontSize: 12),
              ),
              trailing: isPaid
                  ? const Text(
                      'PAID',
                      style: TextStyle(color: Colors.emeraldAccent, fontWeight: FontWeight.bold, fontSize: 12),
                    )
                  : ElevatedButton(
                      style: ElevatedButton.styleFrom(backgroundColor: Colors.indigoAccent),
                      onPressed: () {},
                      child: const Text('Pay', style: TextStyle(color: Colors.white)),
                    ),
            ),
          );
        },
      ),
    );
  }
}
