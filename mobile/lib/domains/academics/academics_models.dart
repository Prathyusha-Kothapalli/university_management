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

