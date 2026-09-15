import React from 'react';
import { Users, GraduationCap, BookOpen, Percent, AlertTriangle, TrendingUp, TrendingDown } from 'lucide-react';

export interface HODStatCardsProps {
  totalStudents?: number;
  totalFaculty?: number;
  activeCourses?: number;
  avgAttendance?: number;
  atRiskCount?: number;
}

export const HODStatCards: React.FC<HODStatCardsProps> = ({
  totalStudents = 1248,
  totalFaculty = 42,
  activeCourses = 28,
  avgAttendance = 86.4,
  atRiskCount = 12,
}) => {
  const stats = [
    {
      id: 'students',
      label: 'Department Students',
      value: totalStudents.toLocaleString(),
      change: '+4.2% vs last term',
      isPositive: true,
      icon: <Users size={22} color="#38bdf8" />,
      bg: 'rgba(56, 189, 248, 0.12)',
      border: 'rgba(56, 189, 248, 0.25)',
    },
    {
      id: 'faculty',
      label: 'Department Faculty',
      value: totalFaculty.toString(),
      change: '4 Professors, 12 Assoc, 26 Asst',
      isPositive: true,
      icon: <GraduationCap size={22} color="#a855f7" />,
      bg: 'rgba(168, 85, 247, 0.12)',
      border: 'rgba(168, 85, 247, 0.25)',
    },
    {
      id: 'courses',
      label: 'Active Offered Courses',
      value: activeCourses.toString(),
      change: '8 Semesters Covered',
      isPositive: true,
      icon: <BookOpen size={22} color="#34d399" />,
      bg: 'rgba(52, 211, 153, 0.12)',
      border: 'rgba(52, 211, 153, 0.25)',
    },
    {
      id: 'attendance',
      label: 'Avg Dept Attendance',
      value: `${avgAttendance}%`,
      change: '+1.8% target exceeded',
      isPositive: true,
      icon: <Percent size={22} color="#f59e0b" />,
      bg: 'rgba(245, 158, 11, 0.12)',
      border: 'rgba(245, 158, 11, 0.25)',
    },
    {
      id: 'at-risk',
      label: 'At-Risk Students',
      value: atRiskCount.toString(),
      change: 'Attendance <75% or GPA <6.0',
      isPositive: false,
      icon: <AlertTriangle size={22} color="#f43f5e" />,
      bg: 'rgba(244, 63, 94, 0.12)',
      border: 'rgba(244, 63, 94, 0.25)',
    },
  ];

  return (
    <div
      style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))',
        gap: '1rem',
        marginBottom: '1.5rem',
      }}
    >
      {stats.map((item) => (
        <div
          key={item.id}
          style={{
            backgroundColor: 'rgba(30, 41, 59, 0.7)',
            backdropFilter: 'blur(12px)',
            border: `1px solid ${item.border}`,
            borderRadius: '16px',
            padding: '1.25rem',
            display: 'flex',
            flexDirection: 'column',
            gap: '12px',
            boxShadow: '0 4px 20px rgba(0, 0, 0, 0.2)',
          }}
        >
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <span style={{ fontSize: '0.825rem', fontWeight: 600, color: '#94a3b8' }}>{item.label}</span>
            <div
              style={{
                width: '40px',
                height: '40px',
                borderRadius: '10px',
                backgroundColor: item.bg,
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
              }}
            >
              {item.icon}
            </div>
          </div>
          <div style={{ fontSize: '1.85rem', fontWeight: 800, color: '#f8fafc', letterSpacing: '-0.5px' }}>
            {item.value}
          </div>
          <div style={{ display: 'flex', alignItems: 'center', gap: '6px', fontSize: '0.75rem', fontWeight: 500 }}>
            {item.id === 'at-risk' ? (
              <TrendingDown size={14} color="#f43f5e" />
            ) : (
              <TrendingUp size={14} color="#34d399" />
            )}
            <span style={{ color: item.id === 'at-risk' ? '#f43f5e' : '#64748b' }}>{item.change}</span>
          </div>
        </div>
      ))}
    </div>
  );
};
