export type UserRole =
  | 'SUPER_ADMIN'
  | 'MANAGEMENT'
  | 'PRINCIPAL'
  | 'DEAN'
  | 'HOD'
  | 'FACULTY'
  | 'STUDENT'
  | 'PARENT'
  | 'ADMISSION_TEAM'
  | 'EXAM_CELL'
  | 'FINANCE'
  | 'HR'
  | 'LIBRARIAN'
  | 'CAMPUS_OPERATIONS'
  | 'PLACEMENT_TEAM'
  | 'LMS_ADMIN'
  | 'RESEARCH_TEAM'
  | 'INVENTORY_MANAGER'
  | 'COMPLIANCE_OFFICER'
  | 'HELPDESK_AGENT'
  | 'GRIEVANCE_OFFICER'
  | 'SECURITY_ADMIN'
  | 'SYSTEM_ADMIN'
  | 'TENANT_ADMIN'
  | 'BI_ANALYST';

export interface UserPermission {
  id: string;
  code: string;
  name: string;
  module: string;
}

export interface User {
  id: string;
  name: string;
  email: string;
  role: UserRole;
  avatarUrl?: string;
  department?: string;
  institutionId?: string;
  institutionName?: string;
  permissions: string[];
  phone?: string;
  joinedDate?: string;
  status: 'ACTIVE' | 'INACTIVE' | 'SUSPENDED';
}

export interface UserProfile extends User {
  designation?: string;
  employeeId?: string;
  studentId?: string;
  address?: string;
  emergencyContact?: string;
  bio?: string;
  lastLogin?: string;
}
