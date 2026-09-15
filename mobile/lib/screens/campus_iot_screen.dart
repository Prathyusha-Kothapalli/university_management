import 'flutter/material.dart';

class CampusIotScreen extends StatefulWidget {
  const CampusIotScreen({Key? key}) : super(key: key);

  @override
  State<CampusIotScreen> createState() => _CampusIotScreenState();
}

class _CampusIotScreenState extends State<CampusIotScreen> {
  final List<Map<String, dynamic>> _devices = [
    {
      "name": "HVAC Controller A-101",
      "type": "HVAC_CONTROLLER",
      "room": "Auditorium A-101",
      "temp": "21.5 °C",
      "status": "ONLINE",
    },
    {
      "name": "CO2 Ambient Sensor Lab-2",
      "type": "CO2_MONITOR",
      "room": "Lab CS-204",
      "temp": "450 ppm",
      "status": "ONLINE",
    }
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFF0F172A),
      appBar: AppBar(
        backgroundColor: const Color(0xFF1E293B),
        title: const Text(
          'Campus IoT & Sensors',
          style: TextStyle(fontWeight: FontWeight.bold, color: Colors.white),
        ),
        elevation: 0,
      ),
      body: ListView.builder(
        padding: const EdgeInsets.all(16),
        itemCount: _devices.length,
        itemBuilder: (context, index) {
          final d = _devices[index];
          return Card(
            color: const Color(0xFF1E293B),
            margin: const EdgeInsets.only(bottom: 12),
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(12),
              side: const BorderSide(color: Color(0xFF334155)),
            ),
            child: ListTile(
              leading: const Icon(Icons.sensors, color: Colors.indigoAccent),
              title: Text(
                d['name']!,
                style: const TextStyle(color: Colors.white, fontWeight: FontWeight.bold),
              ),
              subtitle: Text(
                'Location: ${d['room']}\nReading: ${d['temp']}',
                style: const TextStyle(color: Colors.white70, fontSize: 12),
              ),
              trailing: Container(
                padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
                decoration: BoxDecoration(
                  color: Colors.emerald.withOpacity(0.2),
                  borderRadius: BorderRadius.circular(6),
                ),
                child: Text(
                  d['status']!,
                  style: const TextStyle(color: Colors.emeraldAccent, fontSize: 10, fontWeight: FontWeight.bold),
                ),
              ),
            ),
          );
        },
      ),
    );
  }
}
