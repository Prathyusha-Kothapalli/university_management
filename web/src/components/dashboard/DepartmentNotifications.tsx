import React from 'react';
import { Bell } from 'lucide-react';
import { useToast } from '../../hooks/useToast';

export const DepartmentNotifications: React.FC = () => {
  const { showToast } = useToast();

  const notifications = [
    { id: 1, title: 'Curriculum Revision Approval Pending', time: '10 mins ago', category: 'Academic Board', priority: 'High' },
    { id: 2, title: 'Lab 304 Equipment Inspection Report Submitted', time: '1 hour ago', category: 'Facilities', priority: 'Normal' },
    { id: 3, title: 'Mid-Sem Exam Timetable Feedback Requested', time: '3 hours ago', category: 'Exams', priority: 'High' },
    { id: 4, title: 'Guest Lecture Proposal: Quantum Computing in AI', time: 'Yesterday', category: 'Events', priority: 'Normal' },
  ];

  const handleAction = (title: string) => {
    showToast(`Approved action item: "${title}"`, 'success');
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
            Department Action Alerts & Notices
          </h3>
          <p style={{ fontSize: '0.78rem', color: '#94a3b8', margin: '2px 0 0 0' }}>
            Pending approvals and administrative updates
          </p>
        </div>
        <Bell size={20} color="#a855f7" />
      </div>

      <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
        {notifications.map((n) => (
          <div
            key={n.id}
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
              <div style={{ fontSize: '0.72rem', color: '#64748b', marginTop: '2px', display: 'flex', gap: '10px' }}>
                <span>{n.category}</span>
                <span>•</span>
                <span>{n.time}</span>
              </div>
            </div>

            <button
              onClick={() => handleAction(n.title)}
              style={{
                backgroundColor: 'rgba(168, 85, 247, 0.15)',
                border: '1px solid rgba(168, 85, 247, 0.3)',
                color: '#c084fc',
                borderRadius: '6px',
                padding: '4px 10px',
                fontSize: '0.72rem',
                fontWeight: 600,
                cursor: 'pointer',
              }}
            >
              Approve
            </button>
          </div>
        ))}
      </div>
    </div>
  );
};
