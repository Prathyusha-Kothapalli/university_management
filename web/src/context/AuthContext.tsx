import React, { createContext, useState, useEffect, ReactNode } from 'react';
import { User, UserRole } from '../types';
import { authApi } from '../services/api';

interface AuthContextType {
  user: User | null;
  role: UserRole;
  token: string | null;
  isAuthenticated: boolean;
  login: (email?: string, password?: string) => Promise<void>;
  logout: () => void;
  switchRole: (newRole?: UserRole) => void;
  updateUser: (updated: Partial<User>) => void;
}

export const AuthContext = createContext<AuthContextType | undefined>(undefined);

const defaultMockUser: User = {
  id: 'u-101',
  full_name: 'Alex Morgan',
  name: 'Alex Morgan',
  email: 'alex.morgan@unisphere.edu',
  role: 'student',
  is_active: true,
  studentId: 'UNI-2026-8890',
  department: 'Computer Science & Engineering',
  gpa: 3.84,
  attendanceRate: 94.5,
  creditsEarned: 76,
  totalCredits: 120,
};

export const AuthProvider: React.FC<{ children: ReactNode }> = ({ children }) => {
  const [user, setUser] = useState<User | null>(() => {
    try {
      const saved = localStorage.getItem('unisphere_user');
      if (saved) return JSON.parse(saved);
    } catch (_) {}
    return defaultMockUser;
  });

  const [token, setToken] = useState<string | null>(() => {
    return localStorage.getItem('unisphere_token') || 'mock-jwt-token-12345';
  });

  const [role, setRole] = useState<UserRole>(() => {
    return (user?.role as UserRole) || 'student';
  });

  useEffect(() => {
    if (user) {
      localStorage.setItem('unisphere_user', JSON.stringify(user));
      setRole((user.role as UserRole) || 'student');
    } else {
      localStorage.removeItem('unisphere_user');
    }
  }, [user]);

  useEffect(() => {
    if (token) {
      localStorage.setItem('unisphere_token', token);
    } else {
      localStorage.removeItem('unisphere_token');
    }
  }, [token]);

  const login = async (email?: string, password?: string) => {
    try {
      const res = await authApi.login({ email, password });
      setUser(res.user);
      setToken(res.access_token);
      setRole((res.user.role as UserRole) || 'student');
    } catch (err) {
      console.error('Login failed', err);
      // Fallback
      setUser(defaultMockUser);
      setToken('mock-token');
      setRole('student');
    }
  };

  const logout = () => {
    setUser(null);
    setToken(null);
    localStorage.removeItem('unisphere_user');
    localStorage.removeItem('unisphere_token');
  };

  const switchRole = (newRole?: UserRole) => {
    const targetRole: UserRole = newRole
      ? newRole
      : role === 'student'
      ? 'faculty'
      : role === 'faculty'
      ? 'hod'
      : role === 'hod'
      ? 'parent'
      : role === 'parent'
      ? 'librarian'
      : role === 'librarian'
      ? 'admin'
      : 'student';

    setRole(targetRole);

    let updatedName = 'Alex Morgan';
    let updatedDept = 'Computer Science & Engineering';

    if (targetRole === 'faculty') {
      updatedName = 'Dr. Sarah Jenkins';
      updatedDept = 'Computer Science & Engineering (Prof)';
    } else if (targetRole === 'hod') {
      updatedName = 'Dr. Robert Rao';
      updatedDept = 'Computer Science & Engineering (HOD)';
    } else if (targetRole === 'parent') {
      updatedName = 'Mr. Ramesh Kumar';
      updatedDept = 'Parent / Guardian Portal (Rahul Kumar)';
    } else if (targetRole === 'librarian') {
      updatedName = 'Mrs. Eleanor Vance';
      updatedDept = 'Central University Library (Chief Librarian)';
    } else if (targetRole === 'admin') {
      updatedName = 'Admin Administrator';
      updatedDept = 'Central University Administration';
    }

    if (user) {
      const updatedUser: User = {
        ...user,
        role: targetRole,
        full_name: updatedName,
        name: updatedName,
        department: updatedDept,
      };
      setUser(updatedUser);
    }
  };

  const updateUser = (updated: Partial<User>) => {
    if (user) {
      setUser({ ...user, ...updated });
    }
  };

  return (
    <AuthContext.Provider
      value={{
        user,
        role,
        token,
        isAuthenticated: !!user,
        login,
        logout,
        switchRole,
        updateUser,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
};
