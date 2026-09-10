import React from 'react';
import { AlertTriangle, Mail } from 'lucide-react';
import { useToast } from '../../hooks/useToast';

export const AtRiskStudents: React.FC = () => {
  const { showToast } = useToast();

  const atRiskList = [
    { id: 'S101', name: 'Vikram Patel', roll: 'CS2024045', semester: 'Sem 5', attendance: 68.4, gpa: 5.8, issue: 'Low Attendance & Low GPA', mentor: 'Dr. Sarah Jenkins' },
    { id: 'S102', name: 'Kavya Nair', roll: 'CS2024089', semester: 'Sem 5', attendance: 71.0, gpa: 7.2, issue: 'Low Attendance', mentor: 'Prof. Alan Turing' },
    { id: 'S103', name: 'Devendra Singh', roll: 'CS2025012', semester: 'Sem 3', attendance: 82.5, gpa: 5.4, issue: 'Low GPA & Backlog', mentor: 'Dr. Grace Hopper' },
    { id: 'S104', name: 'Meera Deshmukh', roll: 'CS2023078', semester: 'Sem 7', attendance: 65.2, gpa: 6.1, issue: 'Critical Attendance (<70%)', mentor: 'Dr. Emily Vance' },
  ];

  const handleSendNotice = (name: string) => {
    showToast(`HOD academic intervention alert sent for ${name}`, 'info');
  };

  return (
    <div
      style={{
        backgroundColor: 'rgba(30, 41, 59, 0.7)',
        backdropFilter: 'blur(12px)',
        border: '1px solid rgba(244, 63, 94, 0.25)',
        borderRadius: '16px',
        padding: '1.25rem',
        boxShadow: '0 4px 20px rgba(244, 63, 94, 0.08)',
      }}
    >
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1rem' }}>
        <div>
          <h3 style={{ fontSize: '1.05rem', fontWeight: 700, color: '#f8fafc', margin: 0, display: 'flex', alignItems: 'center', gap: '8px' }}>
            <AlertTriangle size={18} color="#f43f5e" />
            At-Risk Students Requiring HOD Intervention
          </h3>
          <p style={{ fontSize: '0.78rem', color: '#94a3b8', margin: '2px 0 0 0' }}>
            Students with attendance below 75% or GPA below 6.0 requiring academic support
          </p>
        </div>
        <span
          style={{
            backgroundColor: 'rgba(244, 63, 94, 0.15)',
            color: '#f43f5e',
            fontSize: '0.75rem',
            fontWeight: 700,
            padding: '4px 10px',
            borderRadius: '20px',
            border: '1px solid rgba(244, 63, 94, 0.3)',
          }}
        >
          {atRiskList.length} Immediate Cases
        </span>
      </div>

      <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
        {atRiskList.map((st) => (
          <div
            key={st.id}
            style={{
              backgroundColor: 'rgba(15, 23, 42, 0.6)',
              border: '1px solid rgba(255, 255, 255, 0.06)',
              borderRadius: '12px',
              padding: '12px 14px',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'space-between',
              flexWrap: 'wrap',
              gap: '10px',
            }}
          >
            <div>
              <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                <span style={{ fontSize: '0.9rem', fontWeight: 700, color: '#f1f5f9' }}>{st.name}</span>
                <span style={{ fontSize: '0.75rem', color: '#64748b' }}>({st.roll} • {st.semester})</span>
                <span
                  style={{
                    backgroundColor: 'rgba(244, 63, 94, 0.12)',
                    color: '#f43f5e',
                    fontSize: '0.7rem',
                    fontWeight: 600,
                    padding: '2px 8px',
                    borderRadius: '6px',
                  }}
                >
                  {st.issue}
                </span>
              </div>
              <div style={{ fontSize: '0.75rem', color: '#94a3b8', marginTop: '4px', display: 'flex', gap: '16px' }}>
                <span>Attendance: <strong style={{ color: st.attendance < 75 ? '#f43f5e' : '#34d399' }}>{st.attendance}%</strong></span>
                <span>GPA: <strong style={{ color: st.gpa < 6.0 ? '#f43f5e' : '#38bdf8' }}>{st.gpa}</strong></span>
                <span>Mentor: {st.mentor}</span>
              </div>
            </div>

            <button
              onClick={() => handleSendNotice(st.name)}
              style={{
                backgroundColor: 'rgba(37, 99, 235, 0.2)',
                border: '1px solid rgba(56, 189, 248, 0.3)',
                color: '#38bdf8',
                borderRadius: '8px',
                padding: '6px 12px',
                fontSize: '0.78rem',
                fontWeight: 600,
                cursor: 'pointer',
                display: 'flex',
                alignItems: 'center',
                gap: '6px',
                transition: 'all 0.15s ease',
              }}
            >
              <Mail size={14} /> Send Advisory
            </button>
          </div>
        ))}
      </div>
    </div>
  );
};
