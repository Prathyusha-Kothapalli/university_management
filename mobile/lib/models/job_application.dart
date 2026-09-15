/// Status timeline entry for an application
class ApplicationTimelineEntry {
  final String status;
  final String description;
  final DateTime timestamp;

  const ApplicationTimelineEntry({
    required this.status,
    required this.description,
    required this.timestamp,
  });

  factory ApplicationTimelineEntry.fromJson(Map<String, dynamic> json) {
    return ApplicationTimelineEntry(
      status: json['status']?.toString() ?? 'Applied',
      description: json['description']?.toString() ?? '',
      timestamp: json['timestamp'] != null
          ? DateTime.tryParse(json['timestamp'].toString()) ?? DateTime.now()
          : DateTime.now(),
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'status': status,
      'description': description,
      'timestamp': timestamp.toIso8601String(),
    };
  }
}

/// Job Application domain model representing a candidate's submission.
class JobApplication {
  final String id;
  final String jobId;
  final String jobTitle;
  final String company;
  final String department;
  final String applicantId;
  final String applicantName;
  final String applicantEmail;
  final String applicantPhone;
  final String resumeFileName;
  final String? resumeUrl;
  final String coverLetter;
  final DateTime applicationDate;
  final String status; // 'Applied', 'Under Review', 'Shortlisted', 'Interview Scheduled', 'Selected', 'Rejected'
  final String interviewStatus; // 'None', 'Scheduled', 'Completed', 'Cancelled'
  final DateTime lastUpdated;
  final List<ApplicationTimelineEntry> timeline;

  const JobApplication({
    required this.id,
    required this.jobId,
    required this.jobTitle,
    required this.company,
    this.department = 'Engineering',
    required this.applicantId,
    required this.applicantName,
    required this.applicantEmail,
    required this.applicantPhone,
    required this.resumeFileName,
    this.resumeUrl,
    required this.coverLetter,
    required this.applicationDate,
    this.status = 'Applied',
    this.interviewStatus = 'None',
    required this.lastUpdated,
    this.timeline = const [],
  });

  factory JobApplication.fromJson(Map<String, dynamic> json) {
    return JobApplication(
      id: json['id']?.toString() ?? '',
      jobId: json['job_id']?.toString() ?? json['jobId']?.toString() ?? '',
      jobTitle: json['job_title']?.toString() ?? json['jobTitle']?.toString() ?? '',
      company: json['company']?.toString() ?? '',
      department: json['department']?.toString() ?? 'General',
      applicantId: json['applicant_id']?.toString() ?? json['applicantId']?.toString() ?? '',
      applicantName: json['applicant_name']?.toString() ?? json['applicantName']?.toString() ?? '',
      applicantEmail: json['applicant_email']?.toString() ?? json['applicantEmail']?.toString() ?? '',
      applicantPhone: json['applicant_phone']?.toString() ?? json['applicantPhone']?.toString() ?? '',
      resumeFileName: json['resume_file_name']?.toString() ?? json['resumeFileName']?.toString() ?? 'resume.pdf',
      resumeUrl: json['resume_url']?.toString() ?? json['resumeUrl']?.toString(),
      coverLetter: json['cover_letter']?.toString() ?? json['coverLetter']?.toString() ?? '',
      applicationDate: json['application_date'] != null
          ? DateTime.tryParse(json['application_date'].toString()) ?? DateTime.now()
          : (json['applicationDate'] != null
              ? DateTime.tryParse(json['applicationDate'].toString()) ?? DateTime.now()
              : DateTime.now()),
      status: json['status']?.toString() ?? 'Applied',
      interviewStatus: json['interview_status']?.toString() ?? json['interviewStatus']?.toString() ?? 'None',
      lastUpdated: json['last_updated'] != null
          ? DateTime.tryParse(json['last_updated'].toString()) ?? DateTime.now()
          : (json['lastUpdated'] != null
              ? DateTime.tryParse(json['lastUpdated'].toString()) ?? DateTime.now()
              : DateTime.now()),
      timeline: (json['timeline'] as List<dynamic>?)
              ?.map((e) => ApplicationTimelineEntry.fromJson(e as Map<String, dynamic>))
              .toList() ??
          const [],
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'job_id': jobId,
      'job_title': jobTitle,
      'company': company,
      'department': department,
      'applicant_id': applicantId,
      'applicant_name': applicantName,
      'applicant_email': applicantEmail,
      'applicant_phone': applicantPhone,
      'resume_file_name': resumeFileName,
      'resume_url': resumeUrl,
      'cover_letter': coverLetter,
      'application_date': applicationDate.toIso8601String(),
      'status': status,
      'interview_status': interviewStatus,
      'last_updated': lastUpdated.toIso8601String(),
      'timeline': timeline.map((e) => e.toJson()).toList(),
    };
  }

  JobApplication copyWith({
    String? id,
    String? jobId,
    String? jobTitle,
    String? company,
    String? department,
    String? applicantId,
    String? applicantName,
    String? applicantEmail,
    String? applicantPhone,
    String? resumeFileName,
    String? resumeUrl,
    String? coverLetter,
    DateTime? applicationDate,
    String? status,
    String? interviewStatus,
    DateTime? lastUpdated,
    List<ApplicationTimelineEntry>? timeline,
  }) {
    return JobApplication(
      id: id ?? this.id,
      jobId: jobId ?? this.jobId,
      jobTitle: jobTitle ?? this.jobTitle,
      company: company ?? this.company,
      department: department ?? this.department,
      applicantId: applicantId ?? this.applicantId,
      applicantName: applicantName ?? this.applicantName,
      applicantEmail: applicantEmail ?? this.applicantEmail,
      applicantPhone: applicantPhone ?? this.applicantPhone,
      resumeFileName: resumeFileName ?? this.resumeFileName,
      resumeUrl: resumeUrl ?? this.resumeUrl,
      coverLetter: coverLetter ?? this.coverLetter,
      applicationDate: applicationDate ?? this.applicationDate,
      status: status ?? this.status,
      interviewStatus: interviewStatus ?? this.interviewStatus,
      lastUpdated: lastUpdated ?? this.lastUpdated,
      timeline: timeline ?? this.timeline,
    );
  }
}
