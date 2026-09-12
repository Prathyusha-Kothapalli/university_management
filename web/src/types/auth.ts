export type UserRole = 'student' | 'faculty' | 'admin';

export interface User {
  id: string;
  name: string;
  email: string;
  phone?: string;
  role: UserRole;
  department: string;
  studentId: string;
  enrolledYear?: string;
  gpa: number;
  attendanceRate: number;
  creditsEarned?: number;
  totalCredits?: number;
}

export interface ScheduleItem {
  id: string;
  code: string;
  title: string;
  time: string;
  day: string;
  room: string;
  instructor: string;
  color: string;
  status: 'Ongoing' | 'Upcoming' | 'Completed';
}

export interface Course {
  id: string;
  code: string;
  title: string;
  credits: number;
  instructor: string;
  progress: number;
  schedule: string;
  grade?: string;
}

export interface Announcement {
  id: string;
  title: string;
  date: string;
  category: 'Exam' | 'Academic' | 'Campus' | 'Fee' | 'Placement' | 'Faculty';
  content: string;
  author?: string;
  targetRole?: 'all' | 'student' | 'faculty';
}
