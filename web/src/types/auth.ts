export type UserRole =
  | 'SUPER_ADMIN'
  | 'UNIVERSITY_ADMIN'
  | 'FACULTY'
  | 'STUDENT'
  | 'STAFF'
  | 'student'
  | 'faculty'
  | 'admin'
  | 'hod'
  | 'parent'
  | 'librarian';

export interface Tenant {
  id: string;
  name: string;
  code: string;
  domain?: string | null;
  description?: string | null;
  is_active: boolean;
  created_at: string;
  updated_at: string;
}

export interface User {
  id: string;
  email: string;
  full_name: string;
  name?: string;
  role: UserRole;
  tenant_id?: string | null;
  department?: string | null;
  phone_number?: string | null;
  phone?: string | null;
  studentId?: string | null;
  enrolledYear?: string | number | null;
  gpa?: number | null;
  attendanceRate?: number | null;
  is_active: boolean;
  created_at: string;
  updated_at: string;
  tenant?: Tenant | null;
}

export interface AuthResponse {
  access_token: string;
  token_type: string;
  user: User;
}

export interface RegisterTenantData {
  tenant_name: string;
  tenant_code: string;
  tenant_domain?: string;
  tenant_description?: string;
  admin_email: string;
  admin_password: string;
  admin_name: string;
  admin_department?: string;
}

export interface RegisterUserData {
  email: string;
  password: string;
  full_name: string;
  role: UserRole;
  tenant_id?: string;
  department?: string;
  phone_number?: string;
}

export interface ScheduleItem {
  id: string;
  courseCode: string;
  courseName: string;
  instructor: string;
  room: string;
  day: string;
  startTime: string;
  endTime: string;
  color?: string;
}

export interface Course {
  id: string;
  code: string;
  name: string;
  department?: string;
  credits?: number;
  instructor?: string;
  description?: string;
  schedule?: string;
}

export interface Announcement {
  id: string;
  title: string;
  content: string;
  author: string;
  date: string;
  priority?: 'low' | 'medium' | 'high';
  tags?: string[];
}

