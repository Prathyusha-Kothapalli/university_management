import 'package:flutter/material.dart';
import '../../core/theme/app_colors.dart';

class TenantSwitchScreen extends StatefulWidget {
  const TenantSwitchScreen({super.key});

  @override
  State<TenantSwitchScreen> createState() => _TenantSwitchScreenState();
}

class _TenantSwitchScreenState extends State<TenantSwitchScreen> {
  String _selectedTenantCode = 'UNI-MAIN';

  final List<Map<String, String>> _tenants = [
    {
      'code': 'UNI-MAIN',
      'name': 'UniSphere Main Campus',
      'domain': 'main.unisphere.edu',
      'status': 'Active'
    },
    {
      'code': 'STANFORD-TECH',
      'name': 'Stanford Technological Institute',
      'domain': 'stanford.unisphere.edu',
      'status': 'Active'
    },
    {
      'code': 'OXFORD-ACADEMICS',
      'name': 'Oxford Global University',
      'domain': 'oxford.unisphere.edu',
      'status': 'Active'
    },
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Switch University Tenant'),
      ),
      body: ListView(
        padding: const EdgeInsets.all(16),
        children: [
          const Text(
            'Select an active tenant organization instance to switch portal context:',
            style: TextStyle(fontSize: 14, color: AppColors.textSecondaryLight),
          ),
          const SizedBox(height: 16),
          ..._tenants.map((t) {
            final isSelected = t['code'] == _selectedTenantCode;
            return Card(
              margin: const EdgeInsets.only(bottom: 12),
              shape: RoundedRectangleBorder(
                borderRadius: BorderRadius.circular(12),
                side: BorderSide(
                  color: isSelected ? AppColors.primary : AppColors.borderLight,
                  width: isSelected ? 2 : 1,
                ),
              ),
              child: ListTile(
                leading: CircleAvatar(
                  backgroundColor: isSelected ? AppColors.primary : Colors.grey.shade300,
                  child: Icon(
                    Icons.account_balance_rounded,
                    color: isSelected ? Colors.white : Colors.grey.shade700,
                  ),
                ),
                title: Text(
                  t['name']!,
                  style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 15),
                ),
                subtitle: Text('Code: ${t['code']} • ${t['domain']}'),
                trailing: isSelected
                    ? const Icon(Icons.check_circle, color: AppColors.primary)
                    : OutlinedButton(
                        onPressed: () {
                          setState(() {
                            _selectedTenantCode = t['code']!;
                          });
                          ScaffoldMessenger.of(context).showSnackBar(
                            SnackBar(content: Text('Switched context to ${t['name']}')),
                          );
                        },
                        child: const Text('Select'),
                      ),
              ),
            );
          }),
        ],
      ),
    );
  }
}
