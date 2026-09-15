export type UserRole = 'SUPER_ADMIN' | 'UNIVERSITY_ADMIN' | 'FACULTY' | 'STUDENT' | 'STAFF';

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
  role: UserRole;
  tenant_id?: string | null;
  department?: string | null;
  phone_number?: string | null;
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

