import React from 'react';
import { BookOpen, Calendar } from 'lucide-react';

export const AssignmentSummary: React.FC = () => {
  const assignments = [
    { id: '1', course: 'Data Structures', title: 'Binary Search Tree Optimization Lab', due: '12 Sep 2026', status: 'Submitted', score: '87%' },
    { id: '2', course: 'Database Systems', title: 'Relational Schema Normalization (3NF)', due: '15 Sep 2026', status: 'Pending' },
    { id: '3', course: 'Operating Systems', title: 'Process Scheduling Simulator in C++', due: '18 Sep 2026', status: 'Overdue' },
    { id: '4', course: 'Computer Networks', title: 'TCP/IP Packet Capture Analysis', due: '22 Sep 2026', status: 'Pending' },
  ];

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
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1rem', flexWrap: 'wrap', gap: '10px' }}>
        <div>
          <h3 style={{ fontSize: '1.05rem', fontWeight: 700, color: '#f8fafc', margin: 0 }}>
            Assignments Tracker & Submissions
          </h3>
          <p style={{ fontSize: '0.78rem', color: '#94a3b8', margin: '2px 0 0 0' }}>
            Pending: <strong style={{ color: '#f59e0b' }}>4</strong> | Submitted: <strong style={{ color: '#34d399' }}>12</strong> | Overdue: <strong style={{ color: '#f43f5e' }}>1</strong>
          </p>
        </div>
        <BookOpen size={20} color="#a855f7" />
      </div>

      <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
        {assignments.map((a) => (
          <div
            key={a.id}
            style={{
              backgroundColor: 'rgba(15, 23, 42, 0.5)',
              border: '1px solid rgba(255, 255, 255, 0.05)',
              borderRadius: '10px',
              padding: '10px 12px',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'space-between',
              flexWrap: 'wrap',
              gap: '8px',
            }}
          >
            <div>
              <div style={{ fontSize: '0.85rem', fontWeight: 700, color: '#f1f5f9' }}>{a.title}</div>
              <div style={{ fontSize: '0.75rem', color: '#64748b', marginTop: '2px', display: 'flex', gap: '12px' }}>
                <span style={{ color: '#38bdf8' }}>{a.course}</span>
                <span>•</span>
                <span style={{ display: 'inline-flex', alignItems: 'center', gap: '3px' }}>
                  <Calendar size={12} /> Due: {a.due}
                </span>
              </div>
            </div>

            <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
              {a.score && (
                <span style={{ fontSize: '0.78rem', fontWeight: 700, color: '#34d399' }}>
                  Grade: {a.score}
                </span>
              )}
              <span
                style={{
                  padding: '2px 8px',
                  borderRadius: '6px',
                  fontSize: '0.72rem',
                  fontWeight: 700,
                  backgroundColor:
                    a.status === 'Submitted'
                      ? 'rgba(52, 211, 153, 0.15)'
                      : a.status === 'Overdue'
                      ? 'rgba(244, 63, 94, 0.15)'
                      : 'rgba(245, 158, 11, 0.15)',
                  color:
                    a.status === 'Submitted'
                      ? '#34d399'
                      : a.status === 'Overdue'
                      ? '#f43f5e'
                      : '#f59e0b',
                }}
              >
                {a.status}
              </span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
