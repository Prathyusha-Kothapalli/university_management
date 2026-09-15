/// Library & Digital Repositories Flutter Data Models
import "dart:convert";

class LibraryFlutterModel1 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel1({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel1.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel1(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel2 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel2({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel2.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel2(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel3 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel3({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel3.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel3(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel4 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel4({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel4.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel4(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel5 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel5({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel5.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel5(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel6 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel6({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel6.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel6(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel7 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel7({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel7.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel7(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel8 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel8({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel8.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel8(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel9 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel9({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel9.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel9(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel10 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel10({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel10.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel10(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel11 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel11({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel11.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel11(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel12 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel12({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel12.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel12(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel13 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel13({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel13.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel13(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel14 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel14({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel14.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel14(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel15 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel15({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel15.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel15(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel16 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel16({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel16.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel16(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel17 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel17({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel17.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel17(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel18 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel18({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel18.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel18(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel19 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel19({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel19.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel19(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel20 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel20({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel20.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel20(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel21 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel21({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel21.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel21(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel22 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel22({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel22.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel22(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel23 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel23({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel23.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel23(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel24 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel24({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel24.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel24(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel25 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel25({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel25.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel25(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel26 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel26({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel26.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel26(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel27 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel27({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel27.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel27(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel28 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel28({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel28.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel28(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel29 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel29({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel29.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel29(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel30 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel30({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel30.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel30(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel31 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel31({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel31.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel31(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel32 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel32({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel32.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel32(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel33 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel33({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel33.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel33(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel34 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel34({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel34.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel34(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel35 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel35({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel35.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel35(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel36 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel36({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel36.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel36(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel37 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel37({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel37.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel37(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel38 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel38({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel38.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel38(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel39 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel39({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel39.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel39(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel40 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel40({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel40.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel40(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel41 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel41({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel41.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel41(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel42 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel42({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel42.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel42(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel43 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel43({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel43.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel43(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel44 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel44({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel44.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel44(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel45 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel45({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel45.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel45(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel46 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel46({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel46.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel46(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel47 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel47({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel47.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel47(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel48 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel48({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel48.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel48(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel49 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel49({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel49.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel49(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel50 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel50({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel50.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel50(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel51 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel51({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel51.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel51(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel52 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel52({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel52.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel52(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel53 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel53({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel53.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel53(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel54 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel54({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel54.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel54(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel55 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel55({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel55.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel55(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel56 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel56({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel56.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel56(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel57 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel57({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel57.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel57(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel58 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel58({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel58.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel58(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel59 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel59({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel59.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel59(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel60 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel60({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel60.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel60(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel61 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel61({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel61.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel61(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel62 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel62({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel62.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel62(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel63 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel63({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel63.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel63(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel64 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel64({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel64.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel64(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel65 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel65({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel65.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel65(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel66 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel66({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel66.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel66(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel67 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel67({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel67.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel67(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel68 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel68({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel68.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel68(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel69 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel69({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel69.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel69(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel70 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel70({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel70.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel70(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel71 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel71({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel71.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel71(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel72 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel72({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel72.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel72(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel73 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel73({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel73.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel73(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel74 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel74({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel74.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel74(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel75 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel75({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel75.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel75(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel76 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel76({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel76.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel76(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel77 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel77({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel77.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel77(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel78 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel78({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel78.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel78(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel79 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel79({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel79.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel79(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel80 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel80({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel80.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel80(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel81 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel81({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel81.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel81(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel82 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel82({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel82.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel82(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel83 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel83({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel83.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel83(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel84 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel84({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel84.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel84(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel85 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel85({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel85.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel85(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel86 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel86({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel86.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel86(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel87 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel87({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel87.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel87(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel88 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel88({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel88.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel88(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel89 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel89({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel89.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel89(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel90 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel90({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel90.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel90(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel91 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel91({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel91.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel91(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel92 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel92({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel92.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel92(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel93 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel93({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel93.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel93(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel94 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel94({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel94.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel94(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel95 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel95({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel95.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel95(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel96 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel96({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel96.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel96(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel97 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel97({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel97.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel97(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel98 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel98({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel98.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel98(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel99 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel99({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel99.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel99(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel100 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel100({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel100.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel100(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel101 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel101({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel101.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel101(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel102 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel102({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel102.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel102(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel103 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel103({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel103.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel103(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel104 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel104({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel104.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel104(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel105 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel105({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel105.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel105(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel106 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel106({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel106.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel106(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel107 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel107({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel107.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel107(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel108 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel108({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel108.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel108(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel109 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel109({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel109.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel109(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel110 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel110({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel110.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel110(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel111 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel111({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel111.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel111(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel112 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel112({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel112.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel112(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel113 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel113({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel113.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel113(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel114 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel114({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel114.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel114(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel115 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel115({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel115.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel115(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel116 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel116({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel116.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel116(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel117 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel117({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel117.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel117(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel118 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel118({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel118.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel118(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel119 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel119({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel119.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel119(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel120 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel120({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel120.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel120(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel121 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel121({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel121.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel121(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel122 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel122({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel122.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel122(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel123 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel123({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel123.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel123(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel124 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel124({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel124.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel124(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel125 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel125({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel125.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel125(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel126 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel126({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel126.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel126(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel127 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel127({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel127.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel127(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel128 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel128({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel128.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel128(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel129 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel129({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel129.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel129(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel130 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel130({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel130.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel130(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel131 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel131({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel131.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel131(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel132 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel132({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel132.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel132(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel133 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel133({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel133.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel133(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel134 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel134({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel134.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel134(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel135 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel135({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel135.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel135(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel136 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel136({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel136.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel136(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel137 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel137({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel137.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel137(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel138 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel138({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel138.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel138(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel139 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel139({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel139.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel139(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel140 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel140({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel140.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel140(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel141 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel141({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel141.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel141(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel142 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel142({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel142.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel142(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel143 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel143({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel143.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel143(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel144 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel144({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel144.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel144(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel145 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel145({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel145.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel145(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel146 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel146({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel146.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel146(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel147 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel147({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel147.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel147(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel148 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel148({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel148.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel148(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel149 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel149({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel149.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel149(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

class LibraryFlutterModel150 {
  final int id;
  final String entityCode;
  final String name;
  final String category;
  final double valueAmount;
  final bool isActive;
  final DateTime createdAt;

  LibraryFlutterModel150({
    required this.id,
    required this.entityCode,
    required this.name,
    required this.category,
    required this.valueAmount,
    required this.isActive,
    required this.createdAt,
  });

  factory LibraryFlutterModel150.fromJson(Map<String, dynamic> json) {
    return LibraryFlutterModel150(
      id: json['id'] ?? 0,
      entityCode: json['entity_code'] ?? '',
      name: json['name'] ?? '',
      category: json['category'] ?? 'General',
      valueAmount: (json['value_amount'] ?? 0.0).toDouble(),
      isActive: json['is_active'] ?? true,
      createdAt: DateTime.parse(json['created_at'] ?? DateTime.now().toIso8601String()),
    );
  }

  Map<String, dynamic> toJson() => {
    'id': id,
    'entity_code': entityCode,
    'name': name,
    'category': category,
    'value_amount': valueAmount,
    'is_active': isActive,
    'created_at': createdAt.toIso8601String(),
  };
}

