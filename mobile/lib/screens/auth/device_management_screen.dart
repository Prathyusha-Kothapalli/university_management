import 'package:flutter/material.dart';
import '../../core/theme/app_colors.dart';
import '../../state/auth_state.dart';

class DeviceManagementScreen extends StatefulWidget {
  final AuthState authState;

  const DeviceManagementScreen({
    super.key,
    required this.authState,
  });

  @override
  State<DeviceManagementScreen> createState() => _DeviceManagementScreenState();
}

class _DeviceManagementScreenState extends State<DeviceManagementScreen> {
  final List<Map<String, dynamic>> _devices = [
    {
      'id': 'sess-1',
      'device_type': 'Mobile App',
      'operating_system': 'Android 14',
      'browser': 'UniSphere Mobile Client',
      'ip_address': '192.168.1.45',
      'is_current': true,
      'last_active': 'Just now',
    },
    {
      'id': 'sess-2',
      'device_type': 'Desktop Web',
      'operating_system': 'Windows 11',
      'browser': 'Chrome 124.0',
      'ip_address': '49.207.18.92',
      'is_current': false,
      'last_active': '2 hours ago',
    },
    {
      'id': 'sess-3',
      'device_type': 'Tablet',
      'operating_system': 'iPadOS 17.4',
      'browser': 'Safari 17.0',
      'ip_address': '182.73.91.10',
      'is_current': false,
      'last_active': 'Yesterday',
    },
  ];

  void _revokeDevice(String id) {
    setState(() {
      _devices.removeWhere((d) => d['id'] == id);
    });
    ScaffoldMessenger.of(context).showSnackBar(
      const SnackBar(content: Text('Device session revoked successfully.')),
    );
  }

  void _revokeAllSessions() {
    setState(() {
      _devices.removeWhere((d) => d['is_current'] != true);
    });
    ScaffoldMessenger.of(context).showSnackBar(
      const SnackBar(content: Text('All other active sessions have been terminated.')),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Active Device Sessions'),
        actions: [
          IconButton(
            icon: const Icon(Icons.phonelink_erase_rounded),
            tooltip: 'Log Out All Other Devices',
            onPressed: _revokeAllSessions,
          )
        ],
      ),
      body: ListView(
        padding: const EdgeInsets.all(16),
        children: [
          const Text(
            'Manage devices currently logged into your UniSphere account.',
            style: TextStyle(fontSize: 14, color: AppColors.textSecondaryLight),
          ),
          const SizedBox(height: 16),
          ..._devices.map((device) {
            final isCurrent = device['is_current'] == true;
            return Card(
              margin: const EdgeInsets.only(bottom: 12),
              shape: RoundedRectangleBorder(
                borderRadius: BorderRadius.circular(12),
                side: BorderSide(
                  color: isCurrent ? AppColors.primary.withOpacity(0.5) : AppColors.borderLight,
                ),
              ),
              child: ListTile(
                leading: CircleAvatar(
                  backgroundColor: isCurrent ? AppColors.primary.withOpacity(0.1) : Colors.grey.withOpacity(0.1),
                  child: Icon(
                    device['device_type'] == 'Mobile App' ? Icons.phone_android : Icons.computer,
                    color: isCurrent ? AppColors.primary : Colors.grey,
                  ),
                ),
                title: Row(
                  children: [
                    Text(
                      '${device['device_type']} (${device['operating_system']})',
                      style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 14),
                    ),
                    if (isCurrent) ...[
                      const SizedBox(width: 8),
                      Container(
                        padding: const EdgeInsets.symmetric(horizontal: 6, vertical: 2),
                        decoration: BoxDecoration(
                          color: AppColors.success.withOpacity(0.2),
                          borderRadius: BorderRadius.circular(8),
                        ),
                        child: const Text(
                          'THIS DEVICE',
                          style: TextStyle(fontSize: 10, color: AppColors.success, fontWeight: FontWeight.bold),
                        ),
                      ),
                    ],
                  ],
                ),
                subtitle: Text(
                  '${device['browser']} • IP: ${device['ip_address']}\nActive: ${device['last_active']}',
                  style: const TextStyle(fontSize: 12),
                ),
                trailing: isCurrent
                    ? null
                    : IconButton(
                        icon: const Icon(Icons.delete_outline, color: Colors.red),
                        onPressed: () => _revokeDevice(device['id']),
                      ),
              ),
            );
          }),
        ],
      ),
    );
  }
}
