import React from 'react';
import { Award } from 'lucide-react';

export const ResultsOverview: React.FC = () => {
  const results = [
    { course: 'Data Structures', grade: 'A', score: '92%', status: 'Pass' },
    { course: 'Database Management Systems', grade: 'A-', score: '88%', status: 'Pass' },
    { course: 'Operating Systems', grade: 'B+', score: '82%', status: 'Pass' },
    { course: 'Computer Networks', grade: 'A', score: '94%', status: 'Pass' },
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
            Recent Examination Results & Transcript Summary
          </h3>
          <p style={{ fontSize: '0.78rem', color: '#94a3b8', margin: '2px 0 0 0' }}>
            Semester 4 Final Evaluation Results | Pass Rate: <strong style={{ color: '#34d399' }}>100%</strong>
          </p>
        </div>
        <Award size={20} color="#34d399" />
      </div>

      <div style={{ overflowX: 'auto' }}>
        <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: '0.825rem' }}>
          <thead>
            <tr style={{ borderBottom: '1px solid rgba(255, 255, 255, 0.1)', color: '#64748b', textAlign: 'left' }}>
              <th style={{ padding: '8px 10px', fontWeight: 600 }}>Course Title</th>
              <th style={{ padding: '8px 10px', fontWeight: 600 }}>Percentage</th>
              <th style={{ padding: '8px 10px', fontWeight: 600 }}>Grade Obtained</th>
              <th style={{ padding: '8px 10px', fontWeight: 600 }}>Status</th>
            </tr>
          </thead>
          <tbody>
            {results.map((r) => (
              <tr key={r.course} style={{ borderBottom: '1px solid rgba(255, 255, 255, 0.05)', color: '#e2e8f0' }}>
                <td style={{ padding: '10px 10px', fontWeight: 600, color: '#f8fafc' }}>{r.course}</td>
                <td style={{ padding: '10px 10px', color: '#cbd5e1' }}>{r.score}</td>
                <td style={{ padding: '10px 10px' }}>
                  <span style={{ fontWeight: 700, color: '#38bdf8' }}>{r.grade}</span>
                </td>
                <td style={{ padding: '10px 10px' }}>
                  <span
                    style={{
                      padding: '2px 8px',
                      borderRadius: '6px',
                      fontSize: '0.72rem',
                      fontWeight: 700,
                      backgroundColor: 'rgba(52, 211, 153, 0.15)',
                      color: '#34d399',
                    }}
                  >
                    {r.status}
                  </span>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};
