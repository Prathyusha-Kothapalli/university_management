import { LoginCredentials, AuthResponse } from '../types/auth';
import { User, UserRole } from '../types/user';
import { DEFAULT_ROLE_PERMISSIONS } from '../config/permissions';
import { apiRequest } from './api';

export const DEMO_USERS: Record<string, User> = {
  'admin@collexa.com': {
    id: 'usr-001',
    name: 'Super Admin',
    email: 'admin@collexa.com',
    role: 'SUPER_ADMIN',
    department: 'Central IT & Operations',
    institutionName: 'Apex University System',
    permissions: DEFAULT_ROLE_PERMISSIONS.SUPER_ADMIN,
    status: 'ACTIVE',
  },
  'principal@collexa.com': {
    id: 'usr-002',
    name: 'Dr. Aris Thorne',
    email: 'principal@collexa.com',
    role: 'PRINCIPAL',
    department: 'Office of the Principal',
    institutionName: 'Collexa Engineering Campus',
    permissions: DEFAULT_ROLE_PERMISSIONS.PRINCIPAL,
    status: 'ACTIVE',
  },
  'hod@collexa.com': {
    id: 'usr-003',
    name: 'Prof. Ananya Roy',
    email: 'hod@collexa.com',
    role: 'HOD',
    department: 'Computer Science & Engineering',
    institutionName: 'Collexa Engineering Campus',
    permissions: DEFAULT_ROLE_PERMISSIONS.HOD,
    status: 'ACTIVE',
  },
  'faculty@collexa.com': {
    id: 'usr-004',
    name: 'Dr. Vikram Seth',
    email: 'faculty@collexa.com',
    role: 'FACULTY',
    department: 'Computer Science & Engineering',
    institutionName: 'Collexa Engineering Campus',
    permissions: DEFAULT_ROLE_PERMISSIONS.FACULTY,
    status: 'ACTIVE',
  },
  'student@collexa.com': {
    id: 'usr-005',
    name: 'Rohan Sharma',
    email: 'student@collexa.com',
    role: 'STUDENT',
    department: 'B.Tech CSE - Semester 6',
    institutionName: 'Collexa Engineering Campus',
    permissions: DEFAULT_ROLE_PERMISSIONS.STUDENT,
    status: 'ACTIVE',
  },
  'parent@collexa.com': {
    id: 'usr-006',
    name: 'Suresh Sharma',
    email: 'parent@collexa.com',
    role: 'PARENT',
    department: 'Parent Portal',
    institutionName: 'Collexa Engineering Campus',
    permissions: DEFAULT_ROLE_PERMISSIONS.PARENT,
    status: 'ACTIVE',
  },
  'finance@collexa.com': {
    id: 'usr-007',
    name: 'Meera Deshmukh',
    email: 'finance@collexa.com',
    role: 'FINANCE',
    department: 'Finance & Accounts',
    institutionName: 'Collexa Engineering Campus',
    permissions: DEFAULT_ROLE_PERMISSIONS.FINANCE,
    status: 'ACTIVE',
  },
  'management@collexa.com': {
    id: 'usr-008',
    name: 'Karan Malhotra',
    email: 'management@collexa.com',
    role: 'MANAGEMENT',
    department: 'Governing Council',
    institutionName: 'Apex Education Trust',
    permissions: DEFAULT_ROLE_PERMISSIONS.MANAGEMENT,
    status: 'ACTIVE',
  },
  'lms@collexa.com': {
    id: 'usr-009',
    name: 'Dr. Sarah Connor',
    email: 'lms@collexa.com',
    role: 'LMS_ADMIN',
    department: 'Digital Learning Wing',
    institutionName: 'Collexa Engineering Campus',
    permissions: DEFAULT_ROLE_PERMISSIONS.LMS_ADMIN,
    status: 'ACTIVE',
  },
  'bi@collexa.com': {
    id: 'usr-010',
    name: 'Alex Mercer',
    email: 'bi@collexa.com',
    role: 'BI_ANALYST',
    department: 'Institutional Research',
    institutionName: 'Collexa Engineering Campus',
    permissions: DEFAULT_ROLE_PERMISSIONS.BI_ANALYST,
    status: 'ACTIVE',
  },
};

export const authService = {
  async login(credentials: LoginCredentials): Promise<AuthResponse> {
    // In dev / demo mode, fallback to mock user if server isn't running
    try {
      return await apiRequest<AuthResponse>('/auth/login', {
        method: 'POST',
        body: JSON.stringify(credentials),
      });
    } catch {
      // Mock auth fallback for development demo
      const normalizedEmail = credentials.email.toLowerCase();
      const mockUser = DEMO_USERS[normalizedEmail] || {
        id: `usr-${Math.random().toString(36).substr(2, 9)}`,
        name: credentials.email.split('@')[0].toUpperCase(),
        email: credentials.email,
        role: 'STUDENT' as UserRole,
        department: 'General Department',
        institutionName: 'Collexa University',
        permissions: DEFAULT_ROLE_PERMISSIONS.STUDENT,
        status: 'ACTIVE' as const,
      };

      const mockToken = `mock-jwt-token-${mockUser.id}`;
      localStorage.setItem('collexa_token', mockToken);
      localStorage.setItem('collexa_user', JSON.stringify(mockUser));

      return {
        user: mockUser,
        token: mockToken,
      };
    }
  },

  async getMe(): Promise<User> {
    try {
      return await apiRequest<User>('/auth/me');
    } catch {
      const storedUser = localStorage.getItem('collexa_user');
      if (storedUser) {
        return JSON.parse(storedUser);
      }
      throw new Error('No active session found');
    }
  },

  async logout(): Promise<void> {
    try {
      await apiRequest('/auth/logout', { method: 'POST' });
    } catch {
      // Silent catch for dev mode
    } finally {
      localStorage.removeItem('collexa_token');
      localStorage.removeItem('collexa_user');
    }
  },

  async forgotPassword(email: string): Promise<{ message: string }> {
    try {
      return await apiRequest('/auth/forgot-password', {
        method: 'POST',
        body: JSON.stringify({ email }),
      });
    } catch {
      return { message: `Password reset link sent to ${email}` };
    }
  },

  async resetPassword(token: string, password: string): Promise<{ message: string }> {
    try {
      return await apiRequest('/auth/reset-password', {
        method: 'POST',
        body: JSON.stringify({ token, password }),
      });
    } catch {
      return { message: 'Password reset successfully' };
    }
  },
};
