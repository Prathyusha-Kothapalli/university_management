import React from 'react';
import { NavLink } from 'react-router-dom';
import { useAuth } from '../hooks/useAuth';
import {
  LayoutDashboard,
  GraduationCap,
  BookOpen,
  FileCheck,
  CreditCard,
  Library,
  Building2,
  Briefcase,
  Bot,
  User,
  ShieldAlert,
  Sparkles,
} from 'lucide-react';

export const Sidebar: React.FC = () => {
  const { role } = useAuth();

  const navItems = [
    { to: '/dashboard', label: 'Student Dashboard', icon: <LayoutDashboard size={18} />, roles: ['student'] },
    { to: '/admin/dashboard', label: 'Admin Governance', icon: <LayoutDashboard size={18} />, roles: ['admin'] },
    { to: '/faculty/dashboard', label: 'Faculty Portal', icon: <LayoutDashboard size={18} />, roles: ['faculty'] },
    { to: '/hod/dashboard', label: 'HOD Dashboard', icon: <LayoutDashboard size={18} />, roles: ['hod'] },
    { to: '/parent/dashboard', label: 'Parent Dashboard', icon: <LayoutDashboard size={18} />, roles: ['parent'] },
    { to: '/librarian/dashboard', label: 'Librarian Dashboard', icon: <LayoutDashboard size={18} />, roles: ['librarian'] },
    { to: '/features/hub', label: '20 Smart Features Suite', icon: <Sparkles size={18} />, roles: ['admin', 'faculty', 'student', 'hod', 'parent', 'librarian'], highlight: true },
    { to: '/parent/student', label: 'My Student Profile', icon: <User size={18} />, roles: ['parent'] },
    { to: '/parent/academics', label: 'Academics & Courses', icon: <GraduationCap size={18} />, roles: ['parent'] },
    { to: '/parent/assignments', label: 'Assignments', icon: <BookOpen size={18} />, roles: ['parent'] },
    { to: '/parent/exams', label: 'Exams & Results', icon: <FileCheck size={18} />, roles: ['parent'] },
    { to: '/parent/fees', label: 'Fees & Payments', icon: <CreditCard size={18} />, roles: ['parent'] },
    { to: '/parent/library', label: 'Library & Facilities', icon: <Library size={18} />, roles: ['parent'] },
    { to: '/parent/placements', label: 'Placements', icon: <Briefcase size={18} />, roles: ['parent'] },
    { to: '/parent/ai', label: 'AI Parent Copilot', icon: <Bot size={18} />, roles: ['parent'], highlight: true },
    { to: '/hod/department', label: 'Department Overview', icon: <Building2 size={18} />, roles: ['hod'] },
    { to: '/hod/students', label: 'Dept Students', icon: <GraduationCap size={18} />, roles: ['hod'] },
    { to: '/hod/faculty', label: 'Dept Faculty', icon: <User size={18} />, roles: ['hod'] },
    { to: '/hod/courses', label: 'Dept Courses', icon: <BookOpen size={18} />, roles: ['hod'] },
    { to: '/academics', label: 'Academics', icon: <GraduationCap size={18} />, roles: ['admin', 'faculty', 'student', 'hod'] },
    { to: '/learning', label: 'Learning & Materials', icon: <BookOpen size={18} />, roles: ['admin', 'faculty', 'student', 'hod'] },
    { to: '/exams', label: 'Exams & Results', icon: <FileCheck size={18} />, roles: ['admin', 'faculty', 'student', 'hod'] },
    { to: '/finance', label: 'Finance & Fees', icon: <CreditCard size={18} />, roles: ['admin', 'student'] },
    { to: '/library', label: 'Library System', icon: <Library size={18} />, roles: ['admin', 'faculty', 'student', 'hod', 'librarian'] },
    { to: '/facilities', label: 'Hostel & Transport', icon: <Building2 size={18} />, roles: ['admin', 'student'] },
    { to: '/placements', label: 'Placements', icon: <Briefcase size={18} />, roles: ['admin', 'faculty', 'student', 'hod'] },
    { to: '/ai', label: 'AI Copilot', icon: <Bot size={18} />, roles: ['admin', 'faculty', 'student', 'hod', 'librarian'], highlight: true },
    { to: '/profile', label: 'My Profile & Vault', icon: <User size={18} />, roles: ['admin', 'faculty', 'student', 'hod', 'parent', 'librarian'] },
  ];

  const filteredItems = navItems.filter((item) => item.roles.includes(role));

  return (
    <aside
      style={{
        width: '240px',
        backgroundColor: 'rgba(15, 23, 42, 0.95)',
        backdropFilter: 'blur(16px)',
        borderRight: '1px solid rgba(255, 255, 255, 0.08)',
        display: 'flex',
        flexDirection: 'column',
        height: 'calc(100vh - 65px)',
        position: 'sticky',
        top: '65px',
        padding: '1.25rem 0.75rem',
        gap: '4px',
        zIndex: 50,
      }}
    >
      <div
        style={{
          padding: '0 12px 12px 12px',
          fontSize: '0.7rem',
          fontWeight: 700,
          color: '#64748b',
          textTransform: 'uppercase',
          letterSpacing: '1px',
        }}
      >
        Navigation
      </div>

      {filteredItems.map((item) => (
        <NavLink
          key={item.to}
          to={item.to}
          style={({ isActive }) => ({
            display: 'flex',
            alignItems: 'center',
            gap: '12px',
            padding: '10px 14px',
            borderRadius: '10px',
            fontSize: '0.875rem',
            fontWeight: isActive ? 600 : 500,
            textDecoration: 'none',
            color: isActive ? '#38bdf8' : item.highlight ? '#a855f7' : '#94a3b8',
            backgroundColor: isActive
              ? 'rgba(37, 99, 235, 0.18)'
              : item.highlight
              ? 'rgba(168, 85, 247, 0.1)'
              : 'transparent',
            border: isActive
              ? '1px solid rgba(56, 189, 248, 0.3)'
              : item.highlight
              ? '1px solid rgba(168, 85, 247, 0.2)'
              : '1px solid transparent',
            transition: 'all 0.15s ease',
          })}
        >
          {item.icon}
          <span>{item.label}</span>
        </NavLink>
      ))}

      {/* Role Indicator Footer in Sidebar */}
      <div
        style={{
          marginTop: 'auto',
          padding: '12px',
          backgroundColor: 'rgba(255, 255, 255, 0.03)',
          border: '1px solid rgba(255, 255, 255, 0.06)',
          borderRadius: '10px',
          display: 'flex',
          alignItems: 'center',
          gap: '10px',
        }}
      >
        <ShieldAlert size={16} style={{ color: '#38bdf8' }} />
        <div style={{ display: 'flex', flexDirection: 'column' }}>
          <span style={{ fontSize: '0.72rem', color: '#64748b' }}>Active Portal</span>
          <span style={{ fontSize: '0.8rem', fontWeight: 700, color: '#f8fafc', textTransform: 'capitalize' }}>
            {role} Workspace
          </span>
        </div>
      </div>
    </aside>
  );
};
