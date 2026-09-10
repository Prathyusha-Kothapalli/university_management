import axios, { AxiosInstance, AxiosRequestConfig } from 'axios';
import * as T from '../types';

const API_BASE_URL = 'http://localhost:8000/api/v1';

// Create Axios Instance
export const apiClient: AxiosInstance = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
  timeout: 10000,
});

// Request Interceptor: Attach JWT Token if available
apiClient.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('unisphere_token');
    if (token && config.headers) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

// Response Interceptor: Handle auth errors
apiClient.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      // Optional: Clear token or notify auth context
    }
    return Promise.reject(error);
  }
);

// --- Generic Helper with Mock Fallback for stand-alone mode ---
export async function apiRequest<ResData>(
  config: AxiosRequestConfig,
  fallbackData: ResData
): Promise<ResData> {
  try {
    const res = await apiClient.request<ResData>(config);
    return res.data;
  } catch (err) {
    console.warn(`API call failed for ${config.method || 'GET'} ${config.url}. Using realistic fallback data.`, err);
    return fallbackData;
  }
}

// --- Domain API Services ---

// 1. Auth & Users
export const authApi = {
  login: (data: T.LoginRequest) =>
    apiRequest<T.LoginResponse>(
      { method: 'POST', url: '/auth/login', data },
      {
        access_token: 'mock-jwt-token-xyz-12345',
        token_type: 'bearer',
        user: {
          id: 'u-101',
          full_name: 'Alex Morgan',
          email: data.email || 'alex.morgan@unisphere.edu',
          role: 'student',
          is_active: true,
          studentId: 'UNI-2026-8890',
          department: 'Computer Science & Engineering',
          gpa: 3.84,
          attendanceRate: 94.5,
          creditsEarned: 76,
          totalCredits: 120,
        },
      }
    ),
  getUsers: () =>
    apiRequest<T.User[]>(
      { method: 'GET', url: '/users/' },
      [
        { id: 'u-101', full_name: 'Alex Morgan', email: 'alex.morgan@unisphere.edu', role: 'student', is_active: true },
        { id: 'u-102', full_name: 'Dr. Sarah Jenkins', email: 'sarah.jenkins@unisphere.edu', role: 'faculty', is_active: true },
        { id: 'u-103', full_name: 'Admin User', email: 'admin@unisphere.edu', role: 'admin', is_active: true },
      ]
    ),
  createUser: (data: Partial<T.User>) =>
    apiRequest<T.User>(
      { method: 'POST', url: '/users/', data },
      { id: `u-${Date.now()}`, full_name: data.full_name || 'New User', email: data.email || 'user@unisphere.edu', is_active: true, ...data }
    ),
  updateUser: (id: string, data: Partial<T.User>) =>
    apiRequest<T.User>(
      { method: 'PUT', url: `/users/${id}`, data },
      { id, full_name: data.full_name || 'Updated User', email: data.email || 'user@unisphere.edu', is_active: true, ...data }
    ),
  deleteUser: (id: string) =>
    apiRequest<{ message: string }>({ method: 'DELETE', url: `/users/${id}` }, { message: 'User deleted successfully' }),
  getRoles: () =>
    apiRequest<T.Role[]>(
      { method: 'GET', url: '/roles/' },
      [
        { id: 'r-1', name: 'Admin', code: 'admin', description: 'System Administrator' },
        { id: 'r-2', name: 'Faculty', code: 'faculty', description: 'Academic Teaching Staff' },
        { id: 'r-3', name: 'Student', code: 'student', description: 'Enrolled Student' },
      ]
    ),
};

// 2. Structure & Academics
export const structureApi = {
  getUniversities: () =>
    apiRequest<T.University[]>(
      { method: 'GET', url: '/universities/' },
      [{ id: 'univ-1', name: 'UniSphere Central University', code: 'UCU', address: 'Tech Campus Square', established_year: 1995 }]
    ),
  getCampuses: () =>
    apiRequest<T.Campus[]>(
      { method: 'GET', url: '/campuses/' },
      [{ id: 'camp-1', university_id: 'univ-1', name: 'Main City Campus', code: 'MCC', location: 'Metropolis North' }]
    ),
  getDepartments: () =>
    apiRequest<T.Department[]>(
      { method: 'GET', url: '/departments/' },
      [
        { id: 'dept-1', campus_id: 'camp-1', name: 'Computer Science & Engineering', code: 'CSE', head_of_department: 'Dr. Sarah Jenkins' },
        { id: 'dept-2', campus_id: 'camp-1', name: 'Data Science & AI', code: 'DSAI', head_of_department: 'Dr. Alan Turing' },
        { id: 'dept-3', campus_id: 'camp-1', name: 'Electrical Engineering', code: 'EE', head_of_department: 'Dr. Nikola Tesla' },
      ]
    ),
  getPrograms: () =>
    apiRequest<T.Program[]>(
      { method: 'GET', url: '/programs/' },
      [
        { id: 'prog-1', department_id: 'dept-1', name: 'B.Tech Computer Science', code: 'BS-CS', degree_level: 'Bachelor', duration_years: 4, total_credits: 120 },
        { id: 'prog-2', department_id: 'dept-2', name: 'M.Sc Artificial Intelligence', code: 'MS-AI', degree_level: 'Master', duration_years: 2, total_credits: 60 },
      ]
    ),
  getAcademicYears: () =>
    apiRequest<T.AcademicYear[]>(
      { method: 'GET', url: '/academic-years/' },
      [{ id: 'ay-1', year_label: '2025-2026', start_date: '2025-09-01', end_date: '2026-06-30', is_current: true }]
    ),
  getSemesters: () =>
    apiRequest<T.Semester[]>(
      { method: 'GET', url: '/semesters/' },
      [
        { id: 'sem-1', academic_year_id: 'ay-1', semester_number: 6, term_type: 'Spring', start_date: '2026-01-15', end_date: '2026-05-30', is_active: true },
      ]
    ),
};

// 3. Students & Faculty
export const peopleApi = {
  getStudents: () =>
    apiRequest<T.Student[]>(
      { method: 'GET', url: '/students/' },
      [
        { id: 'st-1', user_id: 'u-101', enrollment_number: 'UNI-2026-8890', program_id: 'prog-1', cgpa: 3.84, status: 'Active' },
      ]
    ),
  getFaculty: () =>
    apiRequest<T.Faculty[]>(
      { method: 'GET', url: '/faculty/' },
      [
        { id: 'fac-1', user_id: 'u-102', employee_id: 'FAC-2018-044', department_id: 'dept-1', designation: 'Professor', specialization: 'Deep Learning & Neural Networks' },
      ]
    ),
};

// 4. Courses & Offerings
export const academicsApi = {
  getCourses: () =>
    apiRequest<T.Course[]>(
      { method: 'GET', url: '/courses/' },
      [
        { id: 'c-101', department_id: 'dept-1', course_code: 'CS301', title: 'Advanced Machine Learning', credits: 4, description: 'Deep supervised learning, CNNs, Transformers, and Reinforcement Learning.' },
        { id: 'c-102', department_id: 'dept-1', course_code: 'CS402', title: 'Distributed Systems & Cloud', credits: 4, description: 'Consensus algorithms, microservices, Docker, Kubernetes, and AWS architecture.' },
        { id: 'c-103', department_id: 'dept-2', course_code: 'AI505', title: 'Natural Language Processing', credits: 3, description: 'Tokenization, Embeddings, Attention mechanisms, and Large Language Models.' },
        { id: 'c-104', department_id: 'dept-1', course_code: 'CS204', title: 'Database Management Systems', credits: 3, description: 'Relational algebra, SQL optimization, ACID transactions, and indexing.' },
      ]
    ),
  getCourseOfferings: () =>
    apiRequest<T.CourseOffering[]>(
      { method: 'GET', url: '/course-offerings/' },
      [
        { id: 'co-1', course_id: 'c-101', semester_id: 'sem-1', section_name: 'Section A', max_capacity: 60, status: 'Active' },
        { id: 'co-2', course_id: 'c-102', semester_id: 'sem-1', section_name: 'Section B', max_capacity: 45, status: 'Active' },
      ]
    ),
  getCourseFaculty: () =>
    apiRequest<T.CourseFaculty[]>(
      { method: 'GET', url: '/course-faculty/' },
      [{ id: 'cf-1', course_offering_id: 'co-1', faculty_id: 'fac-1', role: 'Primary Instructor' }]
    ),
  getCourseEnrollments: () =>
    apiRequest<T.CourseEnrollment[]>(
      { method: 'GET', url: '/course-enrollments/' },
      [{ id: 'ce-1', course_offering_id: 'co-1', student_id: 'st-1', enrollment_date: '2026-01-16', grade: 'A', attendance_percentage: 95.0 }]
    ),
};

// 5. Timetable & Attendance
export const timetableApi = {
  getClassrooms: () =>
    apiRequest<T.Classroom[]>(
      { method: 'GET', url: '/classrooms/' },
      [
        { id: 'cr-1', campus_id: 'camp-1', building_name: 'Alan Turing Hall', room_number: 'ATH-302', capacity: 80, type: 'Lecture Hall' },
        { id: 'cr-2', campus_id: 'camp-1', building_name: 'Ada Lovelace Building', room_number: 'ALB-105', capacity: 40, type: 'Lab' },
      ]
    ),
  getTimetables: () =>
    apiRequest<T.Timetable[]>(
      { method: 'GET', url: '/timetables/' },
      [
        { id: 'tt-1', course_offering_id: 'co-1', classroom_id: 'cr-1', day_of_week: 'Monday', start_time: '09:00:00', end_time: '10:30:00' },
        { id: 'tt-2', course_offering_id: 'co-2', classroom_id: 'cr-2', day_of_week: 'Wednesday', start_time: '11:00:00', end_time: '12:30:00' },
        { id: 'tt-3', course_offering_id: 'co-1', classroom_id: 'cr-1', day_of_week: 'Friday', start_time: '14:00:00', end_time: '15:30:00' },
      ]
    ),
  getAttendanceSessions: () =>
    apiRequest<T.AttendanceSession[]>(
      { method: 'GET', url: '/attendance-sessions/' },
      [
        { id: 'ats-1', course_offering_id: 'co-1', faculty_id: 'fac-1', session_date: '2026-09-08', topic: 'Transformer Architecture & Attention Layers', status: 'Completed' },
      ]
    ),
  getAttendanceRecords: () =>
    apiRequest<T.AttendanceRecord[]>(
      { method: 'GET', url: '/attendance-records/' },
      [{ id: 'atr-1', attendance_session_id: 'ats-1', student_id: 'st-1', status: 'Present', remarks: 'On time' }]
    ),
};

// 6. Assignments & Learning
export const learningApi = {
  getAssignments: () =>
    apiRequest<T.Assignment[]>(
      { method: 'GET', url: '/assignments/' },
      [
        { id: 'asg-1', course_offering_id: 'co-1', title: 'Assignment 3: Fine-Tuning LLaMA 3', description: 'Implement LoRA adapter layers for domain adaptation on financial dataset.', due_date: '2026-09-25T23:59:00', max_marks: 100 },
        { id: 'asg-2', course_offering_id: 'co-2', title: 'Lab 2: Kubernetes StatefulSet Cluster', description: 'Deploy a multi-node PostgreSQL cluster with automated failover on K8s.', due_date: '2026-09-30T23:59:00', max_marks: 50 },
      ]
    ),
  getAssignmentSubmissions: () =>
    apiRequest<T.AssignmentSubmission[]>(
      { method: 'GET', url: '/assignment-submissions/' },
      [
        { id: 'sub-1', assignment_id: 'asg-1', student_id: 'st-1', submission_date: '2026-09-20T14:30:00', submission_text: 'Submitted notebook and GitHub repo link.', marks_obtained: 96, feedback: 'Excellent implementation of QLoRA optimization.', status: 'Graded' },
      ]
    ),
  submitAssignment: (data: Partial<T.AssignmentSubmission>) =>
    apiRequest<T.AssignmentSubmission>(
      { method: 'POST', url: '/assignment-submissions/', data },
      { id: `sub-${Date.now()}`, assignment_id: data.assignment_id || 'asg-1', student_id: 'st-1', submission_date: new Date().toISOString(), status: 'Submitted', ...data }
    ),
  getLearningMaterials: () =>
    apiRequest<T.LearningMaterial[]>(
      { method: 'GET', url: '/learning-materials/' },
      [
        { id: 'lm-1', course_offering_id: 'co-1', title: 'Lecture 08: Multi-Head Self-Attention', material_type: 'Lecture Notes', file_url: '#', description: 'Comprehensive mathematical breakdown of QKV projections.', uploaded_at: '2026-09-05' },
        { id: 'lm-2', course_offering_id: 'co-2', title: 'Slide Deck: Distributed Consensus & Raft', material_type: 'Slides', file_url: '#', description: 'Visual explanation of leader election and log replication.', uploaded_at: '2026-09-07' },
      ]
    ),
};

// 7. Examinations & Results
export const examsApi = {
  getExams: () =>
    apiRequest<T.Exam[]>(
      { method: 'GET', url: '/exams/' },
      [{ id: 'ex-1', semester_id: 'sem-1', name: 'Spring 2026 End-Semester Exams', exam_type: 'Final', start_date: '2026-05-10', end_date: '2026-05-25' }]
    ),
  getExamSchedules: () =>
    apiRequest<T.ExamSchedule[]>(
      { method: 'GET', url: '/exam-schedules/' },
      [
        { id: 'exs-1', exam_id: 'ex-1', course_offering_id: 'co-1', classroom_id: 'cr-1', exam_date: '2026-05-12', start_time: '09:00:00', end_time: '12:00:00' },
      ]
    ),
  getExamResults: () =>
    apiRequest<T.ExamResult[]>(
      { method: 'GET', url: '/exam-results/' },
      [
        { id: 'exr-1', exam_schedule_id: 'exs-1', student_id: 'st-1', marks_obtained: 94, max_marks: 100, grade: 'A+', remarks: 'Outstanding performance' },
      ]
    ),
  getTranscripts: () =>
    apiRequest<T.Transcript[]>(
      { method: 'GET', url: '/transcripts/' },
      [{ id: 'tr-1', student_id: 'st-1', generated_date: '2026-06-01', cgpa: 3.84, total_credits_earned: 76, pdf_url: '#' }]
    ),
};

// 8. Fee Management
export const financeApi = {
  getFeeStructures: () =>
    apiRequest<T.FeeStructure[]>(
      { method: 'GET', url: '/fee-structures/' },
      [
        { id: 'fs-1', program_id: 'prog-1', academic_year_id: 'ay-1', tuition_fee: 4500, library_fee: 250, hostel_fee: 1200, transport_fee: 350, total_amount: 6300, due_date: '2026-10-15' },
      ]
    ),
  getStudentFees: () =>
    apiRequest<T.StudentFee[]>(
      { method: 'GET', url: '/student-fees/' },
      [
        { id: 'sf-1', student_id: 'st-1', fee_structure_id: 'fs-1', total_amount: 6300, amount_paid: 4500, due_amount: 1800, status: 'Partial', due_date: '2026-10-15' },
      ]
    ),
  getPayments: () =>
    apiRequest<T.Payment[]>(
      { method: 'GET', url: '/payments/' },
      [
        { id: 'pay-1', student_fee_id: 'sf-1', payment_date: '2026-01-10', amount: 4500, payment_method: 'UPI', transaction_reference: 'TXN-908123491', status: 'Completed', receipt_url: '#' },
      ]
    ),
  createPayment: (data: Partial<T.Payment>) =>
    apiRequest<T.Payment>(
      { method: 'POST', url: '/payments/', data },
      { id: `pay-${Date.now()}`, student_fee_id: data.student_fee_id || 'sf-1', payment_date: new Date().toISOString(), amount: data.amount || 1800, payment_method: data.payment_method || 'Card', transaction_reference: `TXN-${Math.floor(Math.random() * 1000000000)}`, status: 'Completed' }
    ),
};

// 9. Library System
export const libraryApi = {
  getLibraryBooks: () =>
    apiRequest<T.LibraryBook[]>(
      { method: 'GET', url: '/library-books/' },
      [
        { id: 'bk-1', isbn: '978-0262035613', title: 'Deep Learning', author: 'Ian Goodfellow, Yoshua Bengio, Aaron Courville', publisher: 'MIT Press', category: 'Artificial Intelligence', total_copies: 15, available_copies: 4, shelf_location: 'Stack A-12' },
        { id: 'bk-2', isbn: '978-0134685991', title: 'Effective Java (3rd Edition)', author: 'Joshua Bloch', publisher: 'Addison-Wesley', category: 'Computer Science', total_copies: 20, available_copies: 12, shelf_location: 'Stack B-04' },
        { id: 'bk-3', isbn: '978-1491950296', title: 'Designing Data-Intensive Applications', author: 'Martin Kleppmann', publisher: 'O\'Reilly', category: 'Distributed Systems', total_copies: 18, available_copies: 7, shelf_location: 'Stack C-08' },
      ]
    ),
  getBookIssues: () =>
    apiRequest<T.BookIssue[]>(
      { method: 'GET', url: '/book-issues/' },
      [
        { id: 'bi-1', book_id: 'bk-1', student_id: 'st-1', issue_date: '2026-09-01', due_date: '2026-09-21', status: 'Issued' },
      ]
    ),
  getLibraryFines: () =>
    apiRequest<T.LibraryFine[]>(
      { method: 'GET', url: '/library-fines/' },
      [
        { id: 'lf-1', book_issue_id: 'bi-0', student_id: 'st-1', fine_amount: 15.00, reason: '3 Days Overdue Return', status: 'Pending' },
      ]
    ),
  issueBook: (bookId: string) =>
    apiRequest<T.BookIssue>(
      { method: 'POST', url: '/book-issues/', data: { book_id: bookId } },
      { id: `bi-${Date.now()}`, book_id: bookId, student_id: 'st-1', issue_date: new Date().toISOString().split('T')[0], due_date: '2026-10-01', status: 'Issued' }
    ),
};

// 10. Hostel & Transport
export const facilitiesApi = {
  getHostels: () =>
    apiRequest<T.Hostel[]>(
      { method: 'GET', url: '/hostels/' },
      [
        { id: 'h-1', campus_id: 'camp-1', name: 'Sir CV Raman Hall of Residence', gender_type: 'Boys', total_rooms: 120, warden_name: 'Dr. Robert Vance', warden_contact: '+1-555-0192' },
        { id: 'h-2', campus_id: 'camp-1', name: 'Kalpana Chawla International Hostel', gender_type: 'Girls', total_rooms: 100, warden_name: 'Dr. Maria Santos', warden_contact: '+1-555-0193' },
      ]
    ),
  getHostelRooms: () =>
    apiRequest<T.HostelRoom[]>(
      { method: 'GET', url: '/hostel-rooms/' },
      [
        { id: 'hr-301', hostel_id: 'h-1', room_number: 'Room 304-B', capacity: 2, occupied_count: 1, monthly_rent: 300, status: 'Available' },
      ]
    ),
  getHostelAllocations: () =>
    apiRequest<T.HostelAllocation[]>(
      { method: 'GET', url: '/hostel-allocations/' },
      [
        { id: 'ha-1', hostel_room_id: 'hr-301', student_id: 'st-1', allocation_date: '2025-09-01', status: 'Active' },
      ]
    ),
  getTransportRoutes: () =>
    apiRequest<T.TransportRoute[]>(
      { method: 'GET', url: '/transport-routes/' },
      [
        { id: 'tr-1', route_name: 'Route 12: Metro Terminal -> Campus Gate 2', start_point: 'Central Metro Hub', end_point: 'University Main Plaza', fare_amount: 45 },
        { id: 'tr-2', route_name: 'Route 04: Tech Park Express', start_point: 'Silicon Valley Residency', end_point: 'Engineering Complex', fare_amount: 50 },
      ]
    ),
  getTransportVehicles: () =>
    apiRequest<T.TransportVehicle[]>(
      { method: 'GET', url: '/transport-vehicles/' },
      [
        { id: 'tv-1', vehicle_number: 'KA-01-EQ-9810', capacity: 42, driver_name: 'John Miller', driver_contact: '+1-555-4819', route_id: 'tr-1' },
      ]
    ),
  getTransportAllocations: () =>
    apiRequest<T.TransportAllocation[]>(
      { method: 'GET', url: '/transport-allocations/' },
      [
        { id: 'ta-1', vehicle_id: 'tv-1', student_id: 'st-1', pickup_point: 'Central Metro Stop 3', status: 'Active' },
      ]
    ),
};

// 11. Placements, Notifications, Documents & AI
export const placementsApi = {
  getPlacementDrives: () =>
    apiRequest<T.PlacementDrive[]>(
      { method: 'GET', url: '/placement-drives/' },
      [
        { id: 'pd-1', company_name: 'Google Research', job_title: 'AI Systems Engineer', job_description: 'Work on distributed LLM training infrastructure and hardware accelerators.', package_lpa: 38.5, drive_date: '2026-10-12', min_cgpa: 3.5, location: 'Mountain View, CA / Hybrid', status: 'Upcoming' },
        { id: 'pd-2', company_name: 'Anthropic AI', job_title: 'Research Scientist', job_description: 'Mechanistic interpretability and alignment research on frontier models.', package_lpa: 42.0, drive_date: '2026-10-18', min_cgpa: 3.7, location: 'San Francisco, CA', status: 'Upcoming' },
        { id: 'pd-3', company_name: 'NVIDIA AI Tech', job_title: 'CUDA Optimization Engineer', job_description: 'Kernel acceleration and TensorRT runtime optimization.', package_lpa: 35.0, drive_date: '2026-11-02', min_cgpa: 3.2, location: 'Austin, TX', status: 'Upcoming' },
      ]
    ),
  getPlacementApplications: () =>
    apiRequest<T.PlacementApplication[]>(
      { method: 'GET', url: '/placement-applications/' },
      [
        { id: 'pa-1', placement_drive_id: 'pd-1', student_id: 'st-1', application_date: '2026-09-08', status: 'Shortlisted' },
      ]
    ),
  applyForDrive: (driveId: string) =>
    apiRequest<T.PlacementApplication>(
      { method: 'POST', url: '/placement-applications/', data: { placement_drive_id: driveId } },
      { id: `pa-${Date.now()}`, placement_drive_id: driveId, student_id: 'st-1', application_date: new Date().toISOString().split('T')[0], status: 'Applied' }
    ),
};

export const aiApi = {
  getConversations: () =>
    apiRequest<T.AIConversation[]>(
      { method: 'GET', url: '/ai-conversations/' },
      [
        { id: 'conv-1', user_id: 'u-101', title: 'Study Plan for Advanced ML Final Exam', created_at: '2026-09-08T10:00:00', updated_at: '2026-09-08T10:15:00' },
        { id: 'conv-2', user_id: 'u-101', title: 'Campus Hostel Rent Payment Guidance', created_at: '2026-09-05T14:20:00', updated_at: '2026-09-05T14:25:00' },
      ]
    ),
  getMessages: (conversationId: string) =>
    apiRequest<T.AIMessage[]>(
      { method: 'GET', url: `/ai-messages/?conversation_id=${conversationId}` },
      [
        { id: 'msg-1', conversation_id: conversationId, sender_role: 'user', content: 'What topics should I focus on for the CS301 Machine Learning midterm exam?', created_at: '2026-09-08T10:01:00' },
        { id: 'msg-2', conversation_id: conversationId, sender_role: 'assistant', content: 'Hello Alex! Based on your course syllabus for **CS301 Advanced Machine Learning**, key priority topics are:\n1. **Attention Mechanisms & Transformer Architecture** (QKV Matrices, Multi-Head projections)\n2. **Convolutional Neural Networks** (ResNet skip connections & receptive fields)\n3. **Optimization Algorithms** (AdamW, Learning Rate Schedulers, Gradient Clipping)\n\nWould you like me to generate practice quiz questions on any of these topics?', created_at: '2026-09-08T10:01:05' },
      ]
    ),
  sendMessage: (conversationId: string, content: string) =>
    apiRequest<T.AIMessage>(
      { method: 'POST', url: '/ai-messages/', data: { conversation_id: conversationId, content } },
      {
        id: `msg-${Date.now()}`,
        conversation_id: conversationId,
        sender_role: 'assistant',
        content: `UniSphere Copilot Response: I analyzed your query regarding "${content}". I am retrieving live context from your course schedule and official university database records. Here is a recommended next step for your academic progress.`,
        created_at: new Date().toISOString(),
      }
    ),
};

export const documentsApi = {
  getDocuments: () =>
    apiRequest<T.Document[]>(
      { method: 'GET', url: '/documents/' },
      [
        { id: 'doc-1', user_id: 'u-101', title: 'Official Identity Card (2025-2029)', document_type: 'ID Card', file_url: '#', uploaded_at: '2025-09-01' },
        { id: 'doc-2', user_id: 'u-101', title: 'Semester 5 Official Grade Sheet', document_type: 'Marksheet', file_url: '#', uploaded_at: '2026-01-20' },
        { id: 'doc-3', user_id: 'u-101', title: 'Fee Payment Receipt - Fall 2025', document_type: 'Fee Receipt', file_url: '#', uploaded_at: '2025-09-10' },
      ]
    ),
  getNotifications: () =>
    apiRequest<T.Notification[]>(
      { method: 'GET', url: '/notifications/' },
      [
        { id: 'notif-1', title: 'Assignment 3 Posted', message: 'CS301 Assignment 3: Fine-Tuning LLaMA 3 is now available.', category: 'Academic', is_read: false, created_at: '2026-09-09T09:00:00' },
        { id: 'notif-2', title: 'Google Research Drive Open', message: 'Registration for AI Systems Engineer role closes on Oct 5.', category: 'Placement', is_read: false, created_at: '2026-09-08T11:30:00' },
        { id: 'notif-3', title: 'Fee Payment Reminder', message: 'Second installment of tuition fee due by Oct 15.', category: 'Fee', is_read: true, created_at: '2026-09-01T08:00:00' },
      ]
    ),
};
