import React from 'react';
import { BookOpen, BookmarkPlus, AlertTriangle, Users } from 'lucide-react';

export const LibrarianStatCards: React.FC = () => {
  const stats = [
    {
      title: 'Total Books Cataloged',
      value: '24,850',
      subtitle: 'Across 18 academic departments',
      icon: <BookOpen size={22} style={{ color: '#38bdf8' }} />,
      bg: 'rgba(56, 189, 248, 0.1)',
      border: 'rgba(56, 189, 248, 0.25)',
      badge: '+350 this semester',
      badgeColor: '#38bdf8',
    },
    {
      title: 'Active Book Loans',
      value: '1,420',
      subtitle: '92.4% return compliance rate',
      icon: <BookmarkPlus size={22} style={{ color: '#818cf8' }} />,
      bg: 'rgba(129, 140, 248, 0.1)',
      border: 'rgba(129, 140, 248, 0.25)',
      badge: 'Active Loan Volume',
      badgeColor: '#818cf8',
    },
    {
      title: 'Overdue Loans & Fines',
      value: '84 Items',
      subtitle: '₹14,250 pending fine collections',
      icon: <AlertTriangle size={22} style={{ color: '#f59e0b' }} />,
      bg: 'rgba(245, 158, 11, 0.1)',
      border: 'rgba(245, 158, 11, 0.25)',
      badge: '12 Reminders Sent',
      badgeColor: '#f59e0b',
    },
    {
      title: 'Daily Footfall & E-Books',
      value: '412 Readers',
      subtitle: '1,280 digital e-book downloads today',
      icon: <Users size={22} style={{ color: '#c084fc' }} />,
      bg: 'rgba(192, 132, 252, 0.1)',
      border: 'rgba(192, 132, 252, 0.25)',
      badge: '+18% vs last week',
      badgeColor: '#c084fc',
    },
  ];

  return (
    <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(260px, 1fr))', gap: '1.25rem' }}>
      {stats.map((stat, idx) => (
        <div
          key={idx}
          style={{
            backgroundColor: 'rgba(30, 41, 59, 0.7)',
            backdropFilter: 'blur(16px)',
            border: `1px solid ${stat.border}`,
            borderRadius: '16px',
            padding: '1.25rem',
            display: 'flex',
            flexDirection: 'column',
            justifyContent: 'space-between',
            gap: '1rem',
            boxShadow: '0 4px 20px rgba(0, 0, 0, 0.25)',
            transition: 'transform 0.2s ease, boxShadow 0.2s ease',
          }}
        >
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
            <div>
              <span style={{ fontSize: '0.78rem', fontWeight: 600, color: '#94a3b8', textTransform: 'uppercase', letterSpacing: '0.5px' }}>
                {stat.title}
              </span>
              <div style={{ fontSize: '1.75rem', fontWeight: 800, color: '#f8fafc', margin: '4px 0 0 0', letterSpacing: '-0.5px' }}>
                {stat.value}
              </div>
            </div>
            <div
              style={{
                width: '46px',
                height: '46px',
                borderRadius: '12px',
                backgroundColor: stat.bg,
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
              }}
            >
              {stat.icon}
            </div>
          </div>

          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderTop: '1px solid rgba(255, 255, 255, 0.06)', paddingTop: '10px' }}>
            <span style={{ fontSize: '0.75rem', color: '#64748b' }}>{stat.subtitle}</span>
            <span
              style={{
                fontSize: '0.7rem',
                fontWeight: 700,
                color: stat.badgeColor,
                backgroundColor: stat.bg,
                padding: '2px 8px',
                borderRadius: '12px',
                border: `1px solid ${stat.border}`,
              }}
            >
              {stat.badge}
            </span>
          </div>
        </div>
      ))}
    </div>
  );
};
