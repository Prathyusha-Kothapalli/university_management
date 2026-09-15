/// Placements & Alumni Network Mobile Domain Model
class PlacementsModel {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final String status;
  final DateTime createdAt;

  PlacementsModel({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.status,
    required this.createdAt,
  });

  factory PlacementsModel.fromJson(Map<String, dynamic> json) {
    return PlacementsModel(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      status: json['status'] ?? 'ACTIVE',
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'status': status,
    'created_at': createdAt.toIso8601String(),
  };
}
