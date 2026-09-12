import React, { useState } from 'react';
import { MessageSquare, Send } from 'lucide-react';
import { useToast } from '../../hooks/useToast';

interface CounselingRecord {
  id: string;
  studentName: string;
  roll: string;
  guardianName: string;
  phone: string;
  reason: string;
  lastContactDate: string;
  status: 'Notice Sent' | 'Pending Call' | 'Resolved';
}

export const ParentAdvisoryManager: React.FC = () => {
  const { showToast } = useToast();

  const [records, setRecords] = useState<CounselingRecord[]>([
    {
      id: 'REC-01',
      studentName: 'Vikram Patel',
      roll: 'CS2024045',
      guardianName: 'Ramesh Patel',
      phone: '+91 98765-43210',
      reason: 'Critical Attendance (68.4%) & CGPA (5.8)',
      lastContactDate: 'Sept 04, 2026',
      status: 'Pending Call',
    },
    {
      id: 'REC-02',
      studentName: 'Meera Deshmukh',
      roll: 'CS2023078',
      guardianName: 'Sanjay Deshmukh',
      phone: '+91 98123-45678',
      reason: 'Low Attendance (65.2%) in Semester 7',
      lastContactDate: 'Sept 01, 2026',
      status: 'Notice Sent',
    },
  ]);

  const handleSendSMS = (name: string, guardian: string) => {
    showToast(`Official HOD SMS & Email advisory dispatched to ${guardian} (${name})`, 'success');
    setRecords((prev) =>
      prev.map((r) => (r.studentName === name ? { ...r, status: 'Notice Sent' } : r))
    );
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
            Parent Advisory & Student Counseling Manager
          </h3>
          <p style={{ fontSize: '0.78rem', color: '#94a3b8', margin: '2px 0 0 0' }}>
            Automated parent communication triggers for academic intervention
          </p>
        </div>
        <MessageSquare size={20} color="#f59e0b" />
      </div>

      <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
        {records.map((r) => (
          <div
            key={r.id}
            style={{
              backgroundColor: 'rgba(15, 23, 42, 0.5)',
              border: '1px solid rgba(255, 255, 255, 0.05)',
              borderRadius: '10px',
              padding: '10px 12px',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'space-between',
              flexWrap: 'wrap',
              gap: '10px',
            }}
          >
            <div>
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                <span style={{ fontSize: '0.85rem', fontWeight: 700, color: '#f1f5f9' }}>{r.studentName}</span>
                <span style={{ fontSize: '0.75rem', color: '#64748b' }}>({r.roll})</span>
                <span
                  style={{
                    backgroundColor: r.status === 'Resolved' ? 'rgba(52, 211, 153, 0.15)' : 'rgba(245, 158, 11, 0.15)',
                    color: r.status === 'Resolved' ? '#34d399' : '#f59e0b',
                    fontSize: '0.7rem',
                    fontWeight: 700,
                    padding: '2px 6px',
                    borderRadius: '4px',
                  }}
                >
                  {r.status}
                </span>
              </div>
              <div style={{ fontSize: '0.75rem', color: '#94a3b8', marginTop: '2px' }}>
                Guardian: <strong>{r.guardianName}</strong> ({r.phone}) • Reason: <span style={{ color: '#f43f5e' }}>{r.reason}</span>
              </div>
            </div>

            <button
              onClick={() => handleSendSMS(r.studentName, r.guardianName)}
              style={{
                backgroundColor: 'rgba(245, 158, 11, 0.15)',
                border: '1px solid rgba(245, 158, 11, 0.3)',
                color: '#f59e0b',
                borderRadius: '6px',
                padding: '4px 10px',
                fontSize: '0.72rem',
                fontWeight: 600,
                cursor: 'pointer',
                display: 'flex',
                alignItems: 'center',
                gap: '4px',
              }}
            >
              <Send size={13} /> Dispatch Parent Notice
            </button>
          </div>
        ))}
      </div>
    </div>
  );
};
