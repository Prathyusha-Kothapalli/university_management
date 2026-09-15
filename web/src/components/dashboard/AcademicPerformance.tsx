import React from 'react';
import { Award } from 'lucide-react';

export const AcademicPerformance: React.FC = () => {
  const semesters = [
    { sem: 'Sem 1', gpa: 8.10 },
    { sem: 'Sem 2', gpa: 8.35 },
    { sem: 'Sem 3', gpa: 8.50 },
    { sem: 'Sem 4', gpa: 8.40 },
    { sem: 'Sem 5 (Current)', gpa: 8.42 },
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
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1rem' }}>
        <div>
          <h3 style={{ fontSize: '1.05rem', fontWeight: 700, color: '#f8fafc', margin: 0 }}>
            Academic Standing & Semester Performance
          </h3>
          <p style={{ fontSize: '0.78rem', color: '#94a3b8', margin: '2px 0 0 0' }}>
            Overall CGPA: <strong style={{ color: '#34d399' }}>8.42</strong> | Credits Earned: <strong style={{ color: '#38bdf8' }}>76 / 120</strong> | Status: <strong style={{ color: '#34d399' }}>Good Standing</strong>
          </p>
        </div>
        <Award size={20} color="#f59e0b" />
      </div>

      {/* Credit Progress */}
      <div style={{ marginBottom: '1.25rem' }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.78rem', color: '#cbd5e1', marginBottom: '4px' }}>
          <span>Degree Credit Progress (63.3% Completed)</span>
          <span style={{ fontWeight: 600, color: '#38bdf8' }}>76 of 120 Credits</span>
        </div>
        <div style={{ height: '8px', width: '100%', backgroundColor: 'rgba(255, 255, 255, 0.08)', borderRadius: '4px', overflow: 'hidden' }}>
          <div style={{ height: '100%', width: '63.3%', background: 'linear-gradient(90deg, #2563eb, #38bdf8)', borderRadius: '4px' }} />
        </div>
      </div>

      {/* Semester GPA Trend */}
      <div>
        <div style={{ fontSize: '0.8rem', fontWeight: 600, color: '#cbd5e1', marginBottom: '8px' }}>
          Semester-to-Semester GPA Progression
        </div>
        <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
          {semesters.map((s) => (
            <div key={s.sem} style={{ fontSize: '0.78rem' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', color: '#94a3b8', marginBottom: '3px' }}>
                <span>{s.sem}</span>
                <span style={{ fontWeight: 700, color: '#34d399' }}>{s.gpa.toFixed(2)} GPA</span>
              </div>
              <div style={{ height: '5px', width: '100%', backgroundColor: 'rgba(255, 255, 255, 0.06)', borderRadius: '3px', overflow: 'hidden' }}>
                <div style={{ height: '100%', width: `${(s.gpa / 10) * 100}%`, backgroundColor: '#34d399', borderRadius: '3px' }} />
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};
