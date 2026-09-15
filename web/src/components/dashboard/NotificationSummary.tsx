import React from 'react';
import { Bell } from 'lucide-react';
import { useToast } from '../../hooks/useToast';

export const NotificationSummary: React.FC = () => {
  const { showToast } = useToast();

  const notifications = [
    { title: 'Attendance Advisory: Operating Systems (79%)', time: 'Today', type: 'warning' },
    { title: 'Mid-Term Exam Timetable Released for Semester 5', time: 'Yesterday', type: 'info' },
    { title: 'Semester 5 Fee Payment Receipt Generated (₹25,000)', time: '3 days ago', type: 'success' },
  ];

  const handleMarkRead = (title: string) => {
    showToast(`Marked notification as read: "${title}"`, 'info');
  };

  return (
    <div
      style={{
        backgroundColor: 'rgba(30, 41, 59, 0.7)',
        backdropFilter: 'blur(12px)',
        border: '1px solid rgba(255, 255, 255, 0.08)',
        borderRadius: '16px',
        padding: '1.25rem',
        boxShadow: '0 4px 20px rgba(0, 0, 0, 0.2)',
      }}
    >
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1rem' }}>
        <div>
          <h3 style={{ fontSize: '1.05rem', fontWeight: 700, color: '#f8fafc', margin: 0 }}>
            Recent Parent Alerts & Notifications
          </h3>
          <p style={{ fontSize: '0.78rem', color: '#94a3b8', margin: '2px 0 0 0' }}>
            Official university communications for your student
          </p>
        </div>
        <Bell size={20} color="#a855f7" />
      </div>

      <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
        {notifications.map((n, i) => (
          <div
            key={i}
            style={{
              backgroundColor: 'rgba(15, 23, 42, 0.5)',
              border: '1px solid rgba(255, 255, 255, 0.05)',
              borderRadius: '10px',
              padding: '10px 12px',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'space-between',
            }}
          >
            <div>
              <div style={{ fontSize: '0.85rem', fontWeight: 600, color: '#f1f5f9' }}>{n.title}</div>
              <div style={{ fontSize: '0.72rem', color: '#64748b', marginTop: '2px' }}>{n.time}</div>
            </div>
            <button
              onClick={() => handleMarkRead(n.title)}
              style={{
                backgroundColor: 'rgba(168, 85, 247, 0.15)',
                border: '1px solid rgba(168, 85, 247, 0.3)',
                color: '#c084fc',
                borderRadius: '6px',
                padding: '3px 8px',
                fontSize: '0.72rem',
                cursor: 'pointer',
              }}
            >
              Mark Read
            </button>
          </div>
        ))}
      </div>
    </div>
  );
};
