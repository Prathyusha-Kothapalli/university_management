/// Placements & Alumni Network Flutter Data Models
import "dart:convert";

class PlacementsFlutterModel1 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel1({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel1.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel1(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel2 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel2({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel2.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel2(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel3 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel3({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel3.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel3(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel4 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel4({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel4.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel4(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel5 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel5({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel5.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel5(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel6 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel6({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel6.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel6(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel7 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel7({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel7.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel7(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel8 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel8({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel8.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel8(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel9 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel9({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel9.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel9(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel10 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel10({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel10.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel10(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel11 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel11({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel11.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel11(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel12 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel12({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel12.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel12(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel13 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel13({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel13.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel13(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel14 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel14({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel14.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel14(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel15 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel15({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel15.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel15(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel16 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel16({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel16.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel16(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel17 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel17({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel17.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel17(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel18 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel18({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel18.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel18(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel19 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel19({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel19.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel19(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel20 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel20({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel20.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel20(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel21 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel21({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel21.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel21(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel22 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel22({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel22.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel22(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel23 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel23({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel23.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel23(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel24 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel24({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel24.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel24(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel25 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel25({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel25.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel25(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel26 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel26({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel26.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel26(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel27 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel27({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel27.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel27(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel28 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel28({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel28.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel28(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel29 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel29({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel29.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel29(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel30 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel30({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel30.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel30(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel31 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel31({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel31.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel31(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel32 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel32({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel32.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel32(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel33 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel33({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel33.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel33(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel34 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel34({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel34.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel34(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel35 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel35({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel35.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel35(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel36 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel36({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel36.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel36(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel37 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel37({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel37.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel37(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel38 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel38({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel38.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel38(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel39 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel39({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel39.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel39(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel40 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel40({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel40.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel40(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel41 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel41({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel41.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel41(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel42 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel42({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel42.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel42(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel43 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel43({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel43.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel43(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel44 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel44({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel44.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel44(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel45 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel45({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel45.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel45(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel46 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel46({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel46.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel46(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel47 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel47({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel47.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel47(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel48 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel48({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel48.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel48(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel49 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel49({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel49.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel49(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel50 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel50({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel50.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel50(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel51 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel51({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel51.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel51(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel52 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel52({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel52.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel52(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel53 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel53({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel53.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel53(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel54 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel54({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel54.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel54(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel55 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel55({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel55.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel55(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel56 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel56({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel56.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel56(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel57 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel57({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel57.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel57(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel58 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel58({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel58.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel58(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel59 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel59({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel59.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel59(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel60 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel60({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel60.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel60(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel61 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel61({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel61.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel61(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel62 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel62({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel62.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel62(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel63 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel63({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel63.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel63(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel64 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel64({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel64.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel64(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel65 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel65({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel65.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel65(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel66 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel66({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel66.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel66(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel67 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel67({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel67.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel67(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel68 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel68({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel68.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel68(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel69 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel69({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel69.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel69(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel70 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel70({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel70.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel70(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel71 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel71({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel71.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel71(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel72 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel72({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel72.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel72(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel73 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel73({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel73.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel73(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel74 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel74({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel74.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel74(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel75 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel75({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel75.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel75(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel76 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel76({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel76.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel76(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel77 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel77({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel77.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel77(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel78 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel78({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel78.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel78(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel79 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel79({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel79.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel79(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class PlacementsFlutterModel80 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  PlacementsFlutterModel80({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory PlacementsFlutterModel80.fromJson(Map<String, dynamic> json) {
    return PlacementsFlutterModel80(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

