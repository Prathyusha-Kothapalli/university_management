/// Job domain model for campus recruitments, internships, and HR listings.
class Job {
  final String id;
  final String title;
  final String company;
  final String department;
  final String location;
  final String employmentType; // 'Full-time', 'Part-time', 'Internship', 'Contract'
  final String description;
  final List<String> responsibilities;
  final List<String> requiredSkills;
  final List<String> qualifications;
  final String? salary;
  final DateTime postedDate;
  final DateTime? deadline;
  final int applicantsCount;
  final bool isActive;

  const Job({
    required this.id,
    required this.title,
    required this.company,
    required this.department,
    required this.location,
    required this.employmentType,
    required this.description,
    this.responsibilities = const [],
    this.requiredSkills = const [],
    this.qualifications = const [],
    this.salary,
    required this.postedDate,
    this.deadline,
    this.applicantsCount = 0,
    this.isActive = true,
  });

  factory Job.fromJson(Map<String, dynamic> json) {
    return Job(
      id: json['id']?.toString() ?? '',
      title: json['title']?.toString() ?? '',
      company: json['company']?.toString() ?? 'UniSphere Partner',
      department: json['department']?.toString() ?? 'General',
      location: json['location']?.toString() ?? 'Hybrid',
      employmentType: json['employment_type']?.toString() ??
          json['employmentType']?.toString() ??
          'Full-time',
      description: json['description']?.toString() ?? '',
      responsibilities: (json['responsibilities'] as List<dynamic>?)
              ?.map((e) => e.toString())
              .toList() ??
          const [],
      requiredSkills: (json['required_skills'] as List<dynamic>? ??
              json['requiredSkills'] as List<dynamic>?)
          ?.map((e) => e.toString())
          .toList() ??
          const [],
      qualifications: (json['qualifications'] as List<dynamic>?)
              ?.map((e) => e.toString())
              .toList() ??
          const [],
      salary: json['salary']?.toString(),
      postedDate: json['posted_date'] != null
          ? DateTime.tryParse(json['posted_date'].toString()) ?? DateTime.now()
          : (json['postedDate'] != null
              ? DateTime.tryParse(json['postedDate'].toString()) ?? DateTime.now()
              : DateTime.now()),
      deadline: json['deadline'] != null
          ? DateTime.tryParse(json['deadline'].toString())
          : null,
      applicantsCount: (json['applicants_count'] as num? ??
              json['applicantsCount'] as num?)
          ?.toInt() ??
          0,
      isActive: json['is_active'] as bool? ?? json['isActive'] as bool? ?? true,
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'title': title,
      'company': company,
      'department': department,
      'location': location,
      'employment_type': employmentType,
      'description': description,
      'responsibilities': responsibilities,
      'required_skills': requiredSkills,
      'qualifications': qualifications,
      'salary': salary,
      'posted_date': postedDate.toIso8601String(),
      'deadline': deadline?.toIso8601String(),
      'applicants_count': applicantsCount,
      'is_active': isActive,
    };
  }

  Job copyWith({
    String? id,
    String? title,
    String? company,
    String? department,
    String? location,
    String? employmentType,
    String? description,
    List<String>? responsibilities,
    List<String>? requiredSkills,
    List<String>? qualifications,
    String? salary,
    DateTime? postedDate,
    DateTime? deadline,
    int? applicantsCount,
    bool? isActive,
  }) {
    return Job(
      id: id ?? this.id,
      title: title ?? this.title,
      company: company ?? this.company,
      department: department ?? this.department,
      location: location ?? this.location,
      employmentType: employmentType ?? this.employmentType,
      description: description ?? this.description,
      responsibilities: responsibilities ?? this.responsibilities,
      requiredSkills: requiredSkills ?? this.requiredSkills,
      qualifications: qualifications ?? this.qualifications,
      salary: salary ?? this.salary,
      postedDate: postedDate ?? this.postedDate,
      deadline: deadline ?? this.deadline,
      applicantsCount: applicantsCount ?? this.applicantsCount,
      isActive: isActive ?? this.isActive,
    );
  }
}
