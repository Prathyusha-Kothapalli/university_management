import 'dart:convert';
import 'package:http/http.dart' as http;

class HostelService {
  final String baseUrl;

  HostelService({this.baseUrl = 'http://10.0.2.2:8000/api/v1'});

  Future<Map<String, dynamic>> getDashboardOverview() async {
    try {
      final response = await http.get(Uri.parse('$baseUrl/hostel/dashboard/overview'));
      if (response.statusCode == 200) {
        return json.decode(response.body);
      }
    } catch (_) {}
    // Fallback data
    return {
      'total_hostels': 4,
      'total_rooms': 240,
      'total_beds': 480,
      'occupied_beds': 384,
      'available_beds': 96,
      'occupancy_percentage': 80.0,
      'current_residents': 384,
      'pending_applications': 18,
      'open_complaints': 7,
      'outstanding_hostel_fees': 14500.0,
    };
  }

  Future<List<dynamic>> getComplaints() async {
    try {
      final response = await http.get(Uri.parse('$baseUrl/hostel/complaints'));
      if (response.statusCode == 200) {
        return json.decode(response.body);
      }
    } catch (_) {}
    return [
      {
        'id': 'comp-1',
        'room_number': '204',
        'category': 'PLUMBING',
        'priority': 'HIGH',
        'subject': 'Water tap leaking',
        'status': 'OPEN',
      }
    ];
  }
}
