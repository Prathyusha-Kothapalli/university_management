/// Academic & Curriculum Management Flutter Data Models
import "dart:convert";

class AcademicsFlutterModel1 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel1({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel1.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel1(
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

class AcademicsFlutterModel2 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel2({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel2.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel2(
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

class AcademicsFlutterModel3 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel3({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel3.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel3(
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

class AcademicsFlutterModel4 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel4({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel4.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel4(
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

class AcademicsFlutterModel5 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel5({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel5.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel5(
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

class AcademicsFlutterModel6 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel6({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel6.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel6(
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

class AcademicsFlutterModel7 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel7({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel7.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel7(
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

class AcademicsFlutterModel8 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel8({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel8.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel8(
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

class AcademicsFlutterModel9 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel9({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel9.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel9(
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

class AcademicsFlutterModel10 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel10({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel10.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel10(
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

class AcademicsFlutterModel11 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel11({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel11.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel11(
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

class AcademicsFlutterModel12 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel12({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel12.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel12(
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

class AcademicsFlutterModel13 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel13({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel13.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel13(
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

class AcademicsFlutterModel14 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel14({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel14.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel14(
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

class AcademicsFlutterModel15 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel15({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel15.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel15(
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

class AcademicsFlutterModel16 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel16({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel16.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel16(
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

class AcademicsFlutterModel17 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel17({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel17.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel17(
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

class AcademicsFlutterModel18 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel18({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel18.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel18(
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

class AcademicsFlutterModel19 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel19({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel19.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel19(
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

class AcademicsFlutterModel20 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel20({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel20.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel20(
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

class AcademicsFlutterModel21 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel21({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel21.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel21(
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

class AcademicsFlutterModel22 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel22({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel22.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel22(
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

class AcademicsFlutterModel23 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel23({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel23.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel23(
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

class AcademicsFlutterModel24 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel24({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel24.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel24(
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

class AcademicsFlutterModel25 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel25({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel25.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel25(
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

class AcademicsFlutterModel26 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel26({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel26.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel26(
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

class AcademicsFlutterModel27 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel27({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel27.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel27(
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

class AcademicsFlutterModel28 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel28({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel28.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel28(
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

class AcademicsFlutterModel29 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel29({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel29.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel29(
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

class AcademicsFlutterModel30 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel30({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel30.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel30(
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

class AcademicsFlutterModel31 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel31({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel31.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel31(
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

class AcademicsFlutterModel32 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel32({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel32.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel32(
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

class AcademicsFlutterModel33 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel33({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel33.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel33(
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

class AcademicsFlutterModel34 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel34({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel34.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel34(
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

class AcademicsFlutterModel35 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel35({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel35.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel35(
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

class AcademicsFlutterModel36 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel36({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel36.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel36(
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

class AcademicsFlutterModel37 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel37({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel37.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel37(
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

class AcademicsFlutterModel38 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel38({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel38.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel38(
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

class AcademicsFlutterModel39 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel39({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel39.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel39(
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

class AcademicsFlutterModel40 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel40({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel40.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel40(
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

class AcademicsFlutterModel41 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel41({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel41.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel41(
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

class AcademicsFlutterModel42 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel42({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel42.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel42(
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

class AcademicsFlutterModel43 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel43({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel43.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel43(
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

class AcademicsFlutterModel44 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel44({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel44.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel44(
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

class AcademicsFlutterModel45 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel45({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel45.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel45(
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

class AcademicsFlutterModel46 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel46({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel46.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel46(
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

class AcademicsFlutterModel47 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel47({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel47.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel47(
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

class AcademicsFlutterModel48 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel48({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel48.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel48(
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

class AcademicsFlutterModel49 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel49({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel49.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel49(
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

class AcademicsFlutterModel50 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel50({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel50.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel50(
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

class AcademicsFlutterModel51 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel51({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel51.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel51(
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

class AcademicsFlutterModel52 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel52({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel52.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel52(
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

class AcademicsFlutterModel53 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel53({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel53.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel53(
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

class AcademicsFlutterModel54 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel54({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel54.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel54(
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

class AcademicsFlutterModel55 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel55({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel55.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel55(
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

class AcademicsFlutterModel56 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel56({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel56.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel56(
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

class AcademicsFlutterModel57 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel57({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel57.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel57(
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

class AcademicsFlutterModel58 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel58({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel58.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel58(
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

class AcademicsFlutterModel59 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel59({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel59.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel59(
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

class AcademicsFlutterModel60 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel60({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel60.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel60(
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

class AcademicsFlutterModel61 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel61({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel61.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel61(
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

class AcademicsFlutterModel62 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel62({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel62.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel62(
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

class AcademicsFlutterModel63 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel63({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel63.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel63(
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

class AcademicsFlutterModel64 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel64({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel64.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel64(
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

class AcademicsFlutterModel65 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel65({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel65.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel65(
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

class AcademicsFlutterModel66 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel66({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel66.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel66(
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

class AcademicsFlutterModel67 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel67({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel67.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel67(
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

class AcademicsFlutterModel68 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel68({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel68.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel68(
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

class AcademicsFlutterModel69 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel69({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel69.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel69(
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

class AcademicsFlutterModel70 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel70({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel70.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel70(
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

class AcademicsFlutterModel71 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel71({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel71.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel71(
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

class AcademicsFlutterModel72 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel72({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel72.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel72(
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

class AcademicsFlutterModel73 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel73({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel73.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel73(
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

class AcademicsFlutterModel74 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel74({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel74.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel74(
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

class AcademicsFlutterModel75 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel75({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel75.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel75(
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

class AcademicsFlutterModel76 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel76({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel76.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel76(
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

class AcademicsFlutterModel77 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel77({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel77.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel77(
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

class AcademicsFlutterModel78 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel78({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel78.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel78(
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

class AcademicsFlutterModel79 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel79({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel79.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel79(
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

class AcademicsFlutterModel80 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  AcademicsFlutterModel80({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory AcademicsFlutterModel80.fromJson(Map<String, dynamic> json) {
    return AcademicsFlutterModel80(
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

