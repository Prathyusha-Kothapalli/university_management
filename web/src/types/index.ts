// Types matching UniSphere AI Backend Pydantic Schemas across Groups 1-11

export type UserRole = 'admin' | 'faculty' | 'student' | 'hod' | 'parent';

export interface StudentGuardian {
  id: string;
  student_id: string;
  name: string;
  guardian_relationship: string;
  phone: string;
  email?: string;
  address?: string;
  is_primary: boolean;
  created_at?: string;
  updated_at?: string;
}

// --- Group 1: Auth & Core Administration ---

export interface Role {
  id: string;
  name: string;
  code: string;
  description?: string;
  created_at?: string;
  updated_at?: string;
}

export interface User {
  id: string;
  full_name: string;
  email: string;
  role_id?: string;
  role?: string;
  phone_number?: string;
  is_active: boolean;
  is_superuser?: boolean;
  avatar_url?: string;
  created_at?: string;
  updated_at?: string;
  // Legacy / UI convenience fields
  name?: string;
  studentId?: string;
  department?: string;
  gpa?: number;
  attendanceRate?: number;
  creditsEarned?: number;
  totalCredits?: number;
}

export interface LoginRequest {
  username?: string;
  email?: string;
  password?: string;
}

export interface LoginResponse {
  access_token: string;
  token_type: string;
  user: User;
}

export interface University {
  id: string;
  name: string;
  code: string;
  address?: string;
  website?: string;
  established_year?: number;
  created_at?: string;
}

export interface Campus {
  id: string;
  university_id: string;
  name: string;
  code: string;
  location?: string;
  created_at?: string;
}

export interface Department {
  id: string;
  campus_id: string;
  name: string;
  code: string;
  head_of_department?: string;
  created_at?: string;
}

export interface Program {
  id: string;
  department_id: string;
  name: string;
  code: string;
  degree_level: string; // e.g. 'Bachelor', 'Master', 'PhD'
  duration_years: number;
  total_credits: number;
  created_at?: string;
}

export interface AcademicYear {
  id: string;
  year_label: string; // e.g. '2025-2026'
  start_date: string;
  end_date: string;
  is_current: boolean;
}

export interface Semester {
  id: string;
  academic_year_id: string;
  semester_number: number;
  term_type: string; // 'Fall', 'Spring', 'Summer'
  start_date: string;
  end_date: string;
  is_active: boolean;
}

// --- Group 2: Students & Faculty ---

export interface Student {
  id: string;
  user_id: string;
  enrollment_number: string;
  program_id: string;
  current_semester_id?: string;
  admission_date?: string;
  cgpa?: number;
  status: string; // 'Active', 'Graduated', 'Suspended'
  user?: User;
  program?: Program;
}

export interface Faculty {
  id: string;
  user_id: string;
  employee_id: string;
  department_id: string;
  designation: string; // e.g. 'Professor', 'Associate Professor'
  specialization?: string;
  joining_date?: string;
  user?: User;
  department?: Department;
}

// --- Group 3: Academics & Courses ---

export interface Course {
  id: string;
  department_id: string;
  course_code: string;
  title: string;
  credits: number;
  description?: string;
  syllabus?: string;
  department?: Department;
}

export interface CourseOffering {
  id: string;
  course_id: string;
  semester_id: string;
  section_name: string; // e.g. 'Section A'
  max_capacity: number;
  status: string; // 'Active', 'Completed'
  course?: Course;
  semester?: Semester;
}

export interface CourseFaculty {
  id: string;
  course_offering_id: string;
  faculty_id: string;
  role: string; // 'Primary Instructor', 'TA'
  faculty?: Faculty;
  course_offering?: CourseOffering;
}

export interface CourseEnrollment {
  id: string;
  course_offering_id: string;
  student_id: string;
  enrollment_date: string;
  grade?: string;
  attendance_percentage?: number;
  student?: Student;
  course_offering?: CourseOffering;
}

// --- Group 4: Timetable & Attendance ---

export interface Classroom {
  id: string;
  campus_id: string;
  building_name: string;
  room_number: string;
  capacity: number;
  type: string; // 'Lecture Hall', 'Lab', 'Seminar Room'
}

export interface Timetable {
  id: string;
  course_offering_id: string;
  classroom_id: string;
  day_of_week: string; // 'Monday', 'Tuesday', ...
  start_time: string;
  end_time: string;
  course_offering?: CourseOffering;
  classroom?: Classroom;
}

export interface AttendanceSession {
  id: string;
  course_offering_id: string;
  faculty_id: string;
  session_date: string;
  topic?: string;
  status: string; // 'Scheduled', 'Completed', 'Cancelled'
}

export interface AttendanceRecord {
  id: string;
  attendance_session_id: string;
  student_id: string;
  status: string; // 'Present', 'Absent', 'Late', 'Excused'
  remarks?: string;
  student?: Student;
}

// --- Group 5: Assignments & Learning ---

export interface Assignment {
  id: string;
  course_offering_id: string;
  title: string;
  description?: string;
  due_date: string;
  max_marks: number;
  attachment_url?: string;
}

export interface AssignmentSubmission {
  id: string;
  assignment_id: string;
  student_id: string;
  submission_date: string;
  file_url?: string;
  submission_text?: string;
  marks_obtained?: number;
  feedback?: string;
  status: string; // 'Submitted', 'Graded', 'Late'
  assignment?: Assignment;
  student?: Student;
}

export interface LearningMaterial {
  id: string;
  course_offering_id: string;
  title: string;
  material_type: string; // 'Lecture Notes', 'Syllabus', 'Video', 'Slides'
  file_url: string;
  description?: string;
  uploaded_at?: string;
}

// --- Group 6: Examinations & Results ---

export interface Exam {
  id: string;
  semester_id: string;
  name: string; // e.g. 'Mid-Term Spring 2026'
  exam_type: string; // 'Midterm', 'Final', 'Quiz'
  start_date: string;
  end_date: string;
}

export interface ExamSchedule {
  id: string;
  exam_id: string;
  course_offering_id: string;
  classroom_id: string;
  exam_date: string;
  start_time: string;
  end_time: string;
  exam?: Exam;
  course_offering?: CourseOffering;
  classroom?: Classroom;
}

export interface ExamResult {
  id: string;
  exam_schedule_id: string;
  student_id: string;
  marks_obtained: number;
  max_marks: number;
  grade?: string;
  remarks?: string;
  student?: Student;
}

export interface Transcript {
  id: string;
  student_id: string;
  generated_date: string;
  cgpa: number;
  total_credits_earned: number;
  pdf_url?: string;
  student?: Student;
}

// --- Group 7: Fee Management ---

export interface FeeStructure {
  id: string;
  program_id: string;
  academic_year_id: string;
  tuition_fee: number;
  library_fee: number;
  hostel_fee: number;
  transport_fee: number;
  total_amount: number;
  due_date: string;
  program?: Program;
}

export interface StudentFee {
  id: string;
  student_id: string;
  fee_structure_id: string;
  total_amount: number;
  amount_paid: number;
  due_amount: number;
  status: string; // 'Pending', 'Partial', 'Paid', 'Overdue'
  due_date: string;
  student?: Student;
  fee_structure?: FeeStructure;
}

export interface Payment {
  id: string;
  student_fee_id: string;
  payment_date: string;
  amount: number;
  payment_method: string; // 'Card', 'Bank Transfer', 'UPI', 'Cash'
  transaction_reference: string;
  receipt_url?: string;
  status: string; // 'Completed', 'Failed', 'Pending'
}

// --- Group 8: Library System ---

export interface LibraryBook {
  id: string;
  isbn: string;
  title: string;
  author: string;
  publisher?: string;
  category: string;
  total_copies: number;
  available_copies: number;
  shelf_location?: string;
}

export interface BookIssue {
  id: string;
  book_id: string;
  student_id: string;
  issue_date: string;
  due_date: string;
  return_date?: string;
  status: string; // 'Issued', 'Returned', 'Overdue'
  book?: LibraryBook;
  student?: Student;
}

export interface LibraryFine {
  id: string;
  book_issue_id: string;
  student_id: string;
  fine_amount: number;
  reason: string;
  status: string; // 'Pending', 'Paid'
  student?: Student;
}

// --- Group 9: Hostel & Transport ---

export interface Hostel {
  id: string;
  campus_id: string;
  name: string; // e.g. 'Newton Boys Hostel'
  gender_type: string; // 'Boys', 'Girls', 'Co-Ed'
  total_rooms: number;
  warden_name?: string;
  warden_contact?: string;
}

export interface HostelRoom {
  id: string;
  hostel_id: string;
  room_number: string;
  capacity: number;
  occupied_count: number;
  monthly_rent: number;
  status: string; // 'Available', 'Full', 'Maintenance'
  hostel?: Hostel;
}

export interface HostelAllocation {
  id: string;
  hostel_room_id: string;
  student_id: string;
  allocation_date: string;
  vacate_date?: string;
  status: string; // 'Active', 'Vacated'
  hostel_room?: HostelRoom;
  student?: Student;
}

export interface TransportRoute {
  id: string;
  route_name: string;
  start_point: string;
  end_point: string;
  stops_json?: string;
  fare_amount: number;
}

export interface TransportVehicle {
  id: string;
  vehicle_number: string; // e.g. 'KA-01-EQ-1024'
  capacity: number;
  driver_name: string;
  driver_contact: string;
  route_id: string;
  route?: TransportRoute;
}

export interface TransportAllocation {
  id: string;
  vehicle_id: string;
  student_id: string;
  pickup_point: string;
  status: string; // 'Active', 'Cancelled'
  vehicle?: TransportVehicle;
  student?: Student;
}

// --- Group 10: Placements, Notifications, Documents & AI ---

export interface PlacementDrive {
  id: string;
  company_name: string;
  job_title: string;
  job_description: string;
  package_lpa: number;
  drive_date: string;
  min_cgpa: number;
  location: string;
  status: string; // 'Upcoming', 'Ongoing', 'Completed'
}

export interface PlacementApplication {
  id: string;
  placement_drive_id: string;
  student_id: string;
  application_date: string;
  status: string; // 'Applied', 'Shortlisted', 'Interviewed', 'Selected', 'Rejected'
  placement_drive?: PlacementDrive;
  student?: Student;
}

export interface Notification {
  id: string;
  user_id?: string;
  title: string;
  message: string;
  category: string; // 'Academic', 'Fee', 'Exam', 'Placement', 'System'
  is_read: boolean;
  created_at: string;
}

export interface Document {
  id: string;
  user_id: string;
  title: string;
  document_type: string; // 'ID Card', 'Marksheet', 'Degree', 'Certificate', 'Fee Receipt'
  file_url: string;
  uploaded_at: string;
}

export interface AIConversation {
  id: string;
  user_id: string;
  title: string;
  created_at: string;
  updated_at: string;
}

export interface AIMessage {
  id: string;
  conversation_id: string;
  sender_role: 'user' | 'assistant' | 'system';
  content: string;
  created_at: string;
}
