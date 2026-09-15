import React from 'react';
import { Percent, GraduationCap, BookOpen, CreditCard, TrendingUp } from 'lucide-react';

export interface ParentStatCardsProps {
  attendanceRate?: number;
  cgpa?: number;
  pendingAssignments?: number;
  outstandingFees?: number;
}

export const ParentStatCards: React.FC<ParentStatCardsProps> = ({
  attendanceRate = 86.4,
  cgpa = 8.42,
  pendingAssignments = 4,
  outstandingFees = 18500,
}) => {
  const stats = [
    {
      id: 'attendance',
      label: 'Overall Attendance',
      value: `${attendanceRate}%`,
      change: '142 Present / 22 Absent',
      icon: <Percent size={22} color="#38bdf8" />,
      bg: 'rgba(56, 189, 248, 0.12)',
      border: 'rgba(56, 189, 248, 0.25)',
    },
    {
      id: 'cgpa',
      label: 'Current CGPA',
      value: cgpa.toFixed(2),
      change: 'Top 15% of Batch',
      icon: <GraduationCap size={22} color="#34d399" />,
      bg: 'rgba(52, 211, 153, 0.12)',
      border: 'rgba(52, 211, 153, 0.25)',
    },
    {
      id: 'assignments',
      label: 'Pending Assignments',
      value: pendingAssignments.toString(),
      change: '2 Due This Week',
      icon: <BookOpen size={22} color="#a855f7" />,
      bg: 'rgba(168, 85, 247, 0.12)',
      border: 'rgba(168, 85, 247, 0.25)',
    },
    {
      id: 'fees',
      label: 'Outstanding Fees',
      value: `₹${outstandingFees.toLocaleString('en-IN')}`,
      change: 'Due 20 Sep 2026',
      icon: <CreditCard size={22} color="#f59e0b" />,
      bg: 'rgba(245, 158, 11, 0.12)',
      border: 'rgba(245, 158, 11, 0.25)',
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
          <div style={{ display: 'flex', alignItems: 'center', gap: '6px', fontSize: '0.75rem', fontWeight: 500, color: '#64748b' }}>
            <TrendingUp size={14} color="#34d399" />
            <span>{item.change}</span>
          </div>
        </div>
      ))}
    </div>
  );
};
