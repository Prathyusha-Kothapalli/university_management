import "package:flutter/material.dart";
import "finance_models.dart";

class FinanceMainScreen extends StatefulWidget {
  const FinanceMainScreen({Key? key}) : super(key: key);
  @override
  State<FinanceMainScreen> createState() => _FinanceMainScreenState();
}

class _FinanceMainScreenState extends State<FinanceMainScreen> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("Finance, Billing & Payroll"), backgroundColor: Colors.indigo),
      body: ListView.builder(
        itemCount: 75,
        padding: const EdgeInsets.all(16),
        itemBuilder: (context, index) {
          return Card(
            elevation: 2,
            margin: const EdgeInsets.only(bottom: 12),
            child: ListTile(
              leading: CircleAvatar(backgroundColor: Colors.indigo.shade100, child: Text("${index + 1}")),
              title: Text("Finance, Billing & Payroll Record #${index + 1}", style: const TextStyle(fontWeight: FontWeight.bold)),
              subtitle: Text("Code: FINANCE-M-${index + 100}"),
              trailing: const Icon(Icons.arrow_forward_ios, size: 16),
            ),
          );
        },
      ),
    );
  }
}
