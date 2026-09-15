/// Finance, Billing & Payroll Flutter Data Models
import "dart:convert";

class FinanceFlutterModel1 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel1({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel1.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel1(
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

class FinanceFlutterModel2 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel2({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel2.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel2(
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

class FinanceFlutterModel3 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel3({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel3.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel3(
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

class FinanceFlutterModel4 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel4({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel4.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel4(
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

class FinanceFlutterModel5 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel5({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel5.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel5(
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

class FinanceFlutterModel6 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel6({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel6.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel6(
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

class FinanceFlutterModel7 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel7({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel7.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel7(
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

class FinanceFlutterModel8 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel8({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel8.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel8(
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

class FinanceFlutterModel9 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel9({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel9.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel9(
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

class FinanceFlutterModel10 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel10({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel10.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel10(
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

class FinanceFlutterModel11 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel11({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel11.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel11(
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

class FinanceFlutterModel12 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel12({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel12.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel12(
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

class FinanceFlutterModel13 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel13({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel13.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel13(
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

class FinanceFlutterModel14 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel14({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel14.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel14(
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

class FinanceFlutterModel15 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel15({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel15.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel15(
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

class FinanceFlutterModel16 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel16({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel16.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel16(
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

class FinanceFlutterModel17 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel17({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel17.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel17(
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

class FinanceFlutterModel18 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel18({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel18.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel18(
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

class FinanceFlutterModel19 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel19({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel19.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel19(
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

class FinanceFlutterModel20 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel20({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel20.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel20(
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

class FinanceFlutterModel21 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel21({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel21.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel21(
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

class FinanceFlutterModel22 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel22({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel22.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel22(
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

class FinanceFlutterModel23 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel23({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel23.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel23(
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

class FinanceFlutterModel24 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel24({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel24.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel24(
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

class FinanceFlutterModel25 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel25({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel25.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel25(
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

class FinanceFlutterModel26 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel26({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel26.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel26(
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

class FinanceFlutterModel27 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel27({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel27.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel27(
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

class FinanceFlutterModel28 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel28({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel28.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel28(
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

class FinanceFlutterModel29 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel29({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel29.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel29(
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

class FinanceFlutterModel30 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel30({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel30.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel30(
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

class FinanceFlutterModel31 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel31({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel31.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel31(
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

class FinanceFlutterModel32 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel32({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel32.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel32(
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

class FinanceFlutterModel33 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel33({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel33.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel33(
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

class FinanceFlutterModel34 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel34({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel34.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel34(
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

class FinanceFlutterModel35 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel35({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel35.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel35(
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

class FinanceFlutterModel36 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel36({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel36.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel36(
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

class FinanceFlutterModel37 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel37({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel37.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel37(
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

class FinanceFlutterModel38 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel38({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel38.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel38(
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

class FinanceFlutterModel39 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel39({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel39.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel39(
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

class FinanceFlutterModel40 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel40({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel40.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel40(
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

class FinanceFlutterModel41 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel41({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel41.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel41(
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

class FinanceFlutterModel42 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel42({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel42.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel42(
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

class FinanceFlutterModel43 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel43({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel43.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel43(
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

class FinanceFlutterModel44 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel44({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel44.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel44(
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

class FinanceFlutterModel45 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel45({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel45.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel45(
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

class FinanceFlutterModel46 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel46({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel46.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel46(
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

class FinanceFlutterModel47 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel47({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel47.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel47(
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

class FinanceFlutterModel48 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel48({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel48.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel48(
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

class FinanceFlutterModel49 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel49({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel49.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel49(
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

class FinanceFlutterModel50 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel50({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel50.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel50(
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

class FinanceFlutterModel51 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel51({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel51.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel51(
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

class FinanceFlutterModel52 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel52({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel52.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel52(
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

class FinanceFlutterModel53 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel53({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel53.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel53(
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

class FinanceFlutterModel54 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel54({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel54.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel54(
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

class FinanceFlutterModel55 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel55({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel55.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel55(
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

class FinanceFlutterModel56 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel56({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel56.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel56(
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

class FinanceFlutterModel57 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel57({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel57.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel57(
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

class FinanceFlutterModel58 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel58({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel58.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel58(
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

class FinanceFlutterModel59 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel59({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel59.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel59(
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

class FinanceFlutterModel60 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel60({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel60.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel60(
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

class FinanceFlutterModel61 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel61({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel61.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel61(
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

class FinanceFlutterModel62 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel62({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel62.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel62(
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

class FinanceFlutterModel63 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel63({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel63.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel63(
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

class FinanceFlutterModel64 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel64({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel64.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel64(
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

class FinanceFlutterModel65 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel65({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel65.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel65(
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

class FinanceFlutterModel66 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel66({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel66.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel66(
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

class FinanceFlutterModel67 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel67({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel67.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel67(
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

class FinanceFlutterModel68 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel68({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel68.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel68(
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

class FinanceFlutterModel69 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel69({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel69.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel69(
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

class FinanceFlutterModel70 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel70({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel70.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel70(
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

class FinanceFlutterModel71 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel71({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel71.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel71(
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

class FinanceFlutterModel72 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel72({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel72.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel72(
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

class FinanceFlutterModel73 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel73({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel73.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel73(
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

class FinanceFlutterModel74 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel74({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel74.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel74(
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

class FinanceFlutterModel75 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel75({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel75.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel75(
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

class FinanceFlutterModel76 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel76({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel76.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel76(
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

class FinanceFlutterModel77 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel77({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel77.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel77(
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

class FinanceFlutterModel78 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel78({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel78.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel78(
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

class FinanceFlutterModel79 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel79({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel79.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel79(
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

class FinanceFlutterModel80 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel80({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel80.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel80(
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

class FinanceFlutterModel81 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel81({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel81.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel81(
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

class FinanceFlutterModel82 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel82({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel82.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel82(
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

class FinanceFlutterModel83 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel83({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel83.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel83(
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

class FinanceFlutterModel84 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel84({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel84.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel84(
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

class FinanceFlutterModel85 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel85({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel85.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel85(
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

class FinanceFlutterModel86 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel86({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel86.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel86(
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

class FinanceFlutterModel87 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel87({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel87.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel87(
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

class FinanceFlutterModel88 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel88({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel88.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel88(
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

class FinanceFlutterModel89 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel89({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel89.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel89(
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

class FinanceFlutterModel90 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel90({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel90.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel90(
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

class FinanceFlutterModel91 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel91({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel91.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel91(
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

class FinanceFlutterModel92 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel92({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel92.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel92(
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

class FinanceFlutterModel93 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel93({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel93.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel93(
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

class FinanceFlutterModel94 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel94({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel94.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel94(
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

class FinanceFlutterModel95 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel95({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel95.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel95(
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

class FinanceFlutterModel96 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel96({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel96.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel96(
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

class FinanceFlutterModel97 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel97({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel97.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel97(
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

class FinanceFlutterModel98 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel98({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel98.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel98(
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

class FinanceFlutterModel99 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel99({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel99.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel99(
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

class FinanceFlutterModel100 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel100({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel100.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel100(
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

class FinanceFlutterModel101 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel101({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel101.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel101(
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

class FinanceFlutterModel102 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel102({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel102.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel102(
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

class FinanceFlutterModel103 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel103({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel103.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel103(
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

class FinanceFlutterModel104 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel104({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel104.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel104(
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

class FinanceFlutterModel105 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel105({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel105.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel105(
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

class FinanceFlutterModel106 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel106({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel106.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel106(
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

class FinanceFlutterModel107 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel107({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel107.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel107(
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

class FinanceFlutterModel108 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel108({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel108.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel108(
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

class FinanceFlutterModel109 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel109({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel109.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel109(
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

class FinanceFlutterModel110 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel110({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel110.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel110(
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

class FinanceFlutterModel111 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel111({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel111.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel111(
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

class FinanceFlutterModel112 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel112({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel112.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel112(
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

class FinanceFlutterModel113 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel113({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel113.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel113(
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

class FinanceFlutterModel114 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel114({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel114.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel114(
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

class FinanceFlutterModel115 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel115({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel115.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel115(
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

class FinanceFlutterModel116 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel116({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel116.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel116(
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

class FinanceFlutterModel117 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel117({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel117.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel117(
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

class FinanceFlutterModel118 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel118({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel118.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel118(
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

class FinanceFlutterModel119 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel119({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel119.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel119(
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

class FinanceFlutterModel120 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel120({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel120.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel120(
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

class FinanceFlutterModel121 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel121({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel121.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel121(
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

class FinanceFlutterModel122 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel122({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel122.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel122(
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

class FinanceFlutterModel123 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel123({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel123.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel123(
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

class FinanceFlutterModel124 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel124({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel124.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel124(
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

class FinanceFlutterModel125 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel125({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel125.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel125(
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

class FinanceFlutterModel126 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel126({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel126.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel126(
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

class FinanceFlutterModel127 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel127({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel127.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel127(
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

class FinanceFlutterModel128 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel128({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel128.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel128(
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

class FinanceFlutterModel129 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel129({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel129.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel129(
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

class FinanceFlutterModel130 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel130({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel130.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel130(
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

class FinanceFlutterModel131 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel131({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel131.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel131(
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

class FinanceFlutterModel132 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel132({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel132.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel132(
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

class FinanceFlutterModel133 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel133({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel133.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel133(
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

class FinanceFlutterModel134 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel134({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel134.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel134(
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

class FinanceFlutterModel135 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel135({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel135.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel135(
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

class FinanceFlutterModel136 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel136({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel136.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel136(
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

class FinanceFlutterModel137 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel137({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel137.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel137(
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

class FinanceFlutterModel138 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel138({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel138.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel138(
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

class FinanceFlutterModel139 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel139({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel139.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel139(
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

class FinanceFlutterModel140 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel140({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel140.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel140(
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

class FinanceFlutterModel141 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel141({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel141.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel141(
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

class FinanceFlutterModel142 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel142({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel142.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel142(
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

class FinanceFlutterModel143 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel143({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel143.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel143(
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

class FinanceFlutterModel144 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel144({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel144.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel144(
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

class FinanceFlutterModel145 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel145({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel145.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel145(
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

class FinanceFlutterModel146 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel146({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel146.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel146(
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

class FinanceFlutterModel147 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel147({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel147.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel147(
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

class FinanceFlutterModel148 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel148({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel148.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel148(
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

class FinanceFlutterModel149 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel149({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel149.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel149(
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

class FinanceFlutterModel150 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  FinanceFlutterModel150({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory FinanceFlutterModel150.fromJson(Map<String, dynamic> json) {
    return FinanceFlutterModel150(
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

