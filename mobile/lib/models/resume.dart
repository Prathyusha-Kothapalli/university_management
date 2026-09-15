/// Resume domain model for career document management.
class Resume {
  final String id;
  final String userId;
  final String fileName;
  final int fileSizeBytes;
  final String fileExtension; // .pdf, .doc, .docx
  final DateTime uploadDate;
  final String? fileUrl;
  final bool isPrimary;

  const Resume({
    required this.id,
    required this.userId,
    required this.fileName,
    required this.fileSizeBytes,
    required this.fileExtension,
    required this.uploadDate,
    this.fileUrl,
    this.isPrimary = true,
  });

  String get fileSizeFormatted {
    if (fileSizeBytes < 1024) return '$fileSizeBytes B';
    if (fileSizeBytes < 1024 * 1024) {
      return '${(fileSizeBytes / 1024).toStringAsFixed(1)} KB';
    }
    return '${(fileSizeBytes / (1024 * 1024)).toStringAsFixed(1)} MB';
  }

  factory Resume.fromJson(Map<String, dynamic> json) {
    return Resume(
      id: json['id']?.toString() ?? '',
      userId: json['user_id']?.toString() ?? json['userId']?.toString() ?? '',
      fileName: json['file_name']?.toString() ?? json['fileName']?.toString() ?? 'resume.pdf',
      fileSizeBytes: (json['file_size_bytes'] as num? ?? json['fileSizeBytes'] as num?)?.toInt() ?? 1024 * 350,
      fileExtension: json['file_extension']?.toString() ?? json['fileExtension']?.toString() ?? '.pdf',
      uploadDate: json['upload_date'] != null
          ? DateTime.tryParse(json['upload_date'].toString()) ?? DateTime.now()
          : (json['uploadDate'] != null
              ? DateTime.tryParse(json['uploadDate'].toString()) ?? DateTime.now()
              : DateTime.now()),
      fileUrl: json['file_url']?.toString() ?? json['fileUrl']?.toString(),
      isPrimary: json['is_primary'] as bool? ?? json['isPrimary'] as bool? ?? true,
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'user_id': userId,
      'file_name': fileName,
      'file_size_bytes': fileSizeBytes,
      'file_extension': fileExtension,
      'upload_date': uploadDate.toIso8601String(),
      'file_url': fileUrl,
      'is_primary': isPrimary,
    };
  }

  Resume copyWith({
    String? id,
    String? userId,
    String? fileName,
    int? fileSizeBytes,
    String? fileExtension,
    DateTime? uploadDate,
    String? fileUrl,
    bool? isPrimary,
  }) {
    return Resume(
      id: id ?? this.id,
      userId: userId ?? this.userId,
      fileName: fileName ?? this.fileName,
      fileSizeBytes: fileSizeBytes ?? this.fileSizeBytes,
      fileExtension: fileExtension ?? this.fileExtension,
      uploadDate: uploadDate ?? this.uploadDate,
      fileUrl: fileUrl ?? this.fileUrl,
      isPrimary: isPrimary ?? this.isPrimary,
    );
  }
}
