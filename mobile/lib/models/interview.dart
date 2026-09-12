/// Interview domain model for scheduled, upcoming, and past career interviews.
class Interview {
  final String id;
  final String applicationId;
  final String jobId;
  final String jobTitle;
  final String company;
  final DateTime interviewDate;
  final String interviewTime; // e.g. "10:30 AM - 11:30 AM EST"
  final String interviewType; // "Technical", "HR Round", "Hiring Manager", "Campus Placement"
  final String interviewerName;
  final String interviewerRole;
  final String? meetingLink;
  final String status; // "Scheduled", "Completed", "Cancelled"
  final String instructions;
  final String location; // "Google Meet", "Room 402, CS Building", "Zoom"

  const Interview({
    required this.id,
    required this.applicationId,
    required this.jobId,
    required this.jobTitle,
    required this.company,
    required this.interviewDate,
    required this.interviewTime,
    required this.interviewType,
    required this.interviewerName,
    required this.interviewerRole,
    this.meetingLink,
    this.status = 'Scheduled',
    this.instructions = 'Please prepare with a stable connection, notebook, and portfolio projects.',
    this.location = 'Google Meet',
  });

  bool get isUpcoming {
    if (status.toLowerCase() != 'scheduled') return false;
    final now = DateTime.now();
    return interviewDate.isAfter(DateTime(now.year, now.month, now.day - 1));
  }

  factory Interview.fromJson(Map<String, dynamic> json) {
    return Interview(
      id: json['id']?.toString() ?? '',
      applicationId: json['application_id']?.toString() ?? json['applicationId']?.toString() ?? '',
      jobId: json['job_id']?.toString() ?? json['jobId']?.toString() ?? '',
      jobTitle: json['job_title']?.toString() ?? json['jobTitle']?.toString() ?? 'Software Engineer',
      company: json['company']?.toString() ?? 'Partner Enterprise',
      interviewDate: json['interview_date'] != null
          ? DateTime.tryParse(json['interview_date'].toString()) ?? DateTime.now().add(const Duration(days: 2))
          : (json['interviewDate'] != null
              ? DateTime.tryParse(json['interviewDate'].toString()) ?? DateTime.now().add(const Duration(days: 2))
              : DateTime.now().add(const Duration(days: 2))),
      interviewTime: json['interview_time']?.toString() ?? json['interviewTime']?.toString() ?? '10:00 AM - 11:00 AM',
      interviewType: json['interview_type']?.toString() ?? json['interviewType']?.toString() ?? 'Technical',
      interviewerName: json['interviewer_name']?.toString() ?? json['interviewerName']?.toString() ?? 'Senior Interviewer',
      interviewerRole: json['interviewer_role']?.toString() ?? json['interviewerRole']?.toString() ?? 'Tech Lead',
      meetingLink: json['meeting_link']?.toString() ?? json['meetingLink']?.toString(),
      status: json['status']?.toString() ?? 'Scheduled',
      instructions: json['instructions']?.toString() ??
          'Please prepare with a stable connection, notebook, and portfolio projects.',
      location: json['location']?.toString() ?? 'Google Meet',
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'application_id': applicationId,
      'job_id': jobId,
      'job_title': jobTitle,
      'company': company,
      'interview_date': interviewDate.toIso8601String(),
      'interview_time': interviewTime,
      'interview_type': interviewType,
      'interviewer_name': interviewerName,
      'interviewer_role': interviewerRole,
      'meeting_link': meetingLink,
      'status': status,
      'instructions': instructions,
      'location': location,
    };
  }

  Interview copyWith({
    String? id,
    String? applicationId,
    String? jobId,
    String? jobTitle,
    String? company,
    DateTime? interviewDate,
    String? interviewTime,
    String? interviewType,
    String? interviewerName,
    String? interviewerRole,
    String? meetingLink,
    String? status,
    String? instructions,
    String? location,
  }) {
    return Interview(
      id: id ?? this.id,
      applicationId: applicationId ?? this.applicationId,
      jobId: jobId ?? this.jobId,
      jobTitle: jobTitle ?? this.jobTitle,
      company: company ?? this.company,
      interviewDate: interviewDate ?? this.interviewDate,
      interviewTime: interviewTime ?? this.interviewTime,
      interviewType: interviewType ?? this.interviewType,
      interviewerName: interviewerName ?? this.interviewerName,
      interviewerRole: interviewerRole ?? this.interviewerRole,
      meetingLink: meetingLink ?? this.meetingLink,
      status: status ?? this.status,
      instructions: instructions ?? this.instructions,
      location: location ?? this.location,
    );
  }
}
