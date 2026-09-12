import React from 'react';
import { Award } from 'lucide-react';

export const StudentPerformance: React.FC = () => {
  const gpaDistribution = [
    { grade: '9.0 - 10.0 (O)', count: 240, percentage: 19.2, color: '#38bdf8' },
    { grade: '8.0 - 8.9 (A+)', count: 480, percentage: 38.5, color: '#34d399' },
    { grade: '7.0 - 7.9 (A)', count: 320, percentage: 25.6, color: '#a855f7' },
    { grade: '6.0 - 6.9 (B+)', count: 140, percentage: 11.2, color: '#f59e0b' },
    { grade: '< 6.0 (Needs Imp.)', count: 68, percentage: 5.5, color: '#f43f5e' },
  ];

  const topPerformers = [
    { rank: 1, name: 'Siddharth Varma', roll: 'CS2023001', gpa: 9.92, semester: 'Sem 7' },
    { rank: 2, name: 'Priya Sundaram', roll: 'CS2023042', gpa: 9.88, semester: 'Sem 7' },
    { rank: 3, name: 'Rohan Mehta', roll: 'CS2024018', gpa: 9.85, semester: 'Sem 5' },
    { rank: 4, name: 'Ananya Sharma', roll: 'CS2025005', gpa: 9.80, semester: 'Sem 3' },
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
            Student Academic Performance & Distribution
          </h3>
          <p style={{ fontSize: '0.78rem', color: '#94a3b8', margin: '2px 0 0 0' }}>
            Overall pass rate: <strong style={{ color: '#34d399' }}>91.4%</strong> | Average CGPA: <strong style={{ color: '#38bdf8' }}>8.24</strong>
          </p>
        </div>
        <Award size={20} color="#f59e0b" />
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1rem' }}>
        {/* GPA Breakdown */}
        <div>
          <div style={{ fontSize: '0.8rem', fontWeight: 600, color: '#cbd5e1', marginBottom: '8px' }}>
            CGPA Grade Bands
          </div>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
            {gpaDistribution.map((item) => (
              <div key={item.grade} style={{ fontSize: '0.78rem' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '4px', color: '#94a3b8' }}>
                  <span>{item.grade}</span>
                  <span style={{ fontWeight: 600, color: '#f8fafc' }}>
                    {item.count} ({item.percentage}%)
                  </span>
                </div>
                <div
                  style={{
                    height: '6px',
                    width: '100%',
                    backgroundColor: 'rgba(255, 255, 255, 0.08)',
                    borderRadius: '3px',
                    overflow: 'hidden',
                  }}
                >
                  <div
                    style={{
                      height: '100%',
                      width: `${item.percentage}%`,
                      backgroundColor: item.color,
                      borderRadius: '3px',
                    }}
                  />
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Top Performers */}
        <div>
          <div style={{ fontSize: '0.8rem', fontWeight: 600, color: '#cbd5e1', marginBottom: '8px' }}>
            Department Merit Rankers
          </div>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
            {topPerformers.map((tp) => (
              <div
                key={tp.roll}
                style={{
                  backgroundColor: 'rgba(15, 23, 42, 0.5)',
                  border: '1px solid rgba(255, 255, 255, 0.05)',
                  borderRadius: '8px',
                  padding: '8px 10px',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'space-between',
                }}
              >
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                  <div
                    style={{
                      width: '24px',
                      height: '24px',
                      borderRadius: '50%',
                      backgroundColor: tp.rank === 1 ? 'rgba(245, 158, 11, 0.2)' : 'rgba(56, 189, 248, 0.2)',
                      color: tp.rank === 1 ? '#f59e0b' : '#38bdf8',
                      display: 'flex',
                      alignItems: 'center',
                      justifyContent: 'center',
                      fontWeight: 700,
                      fontSize: '0.75rem',
                    }}
                  >
                    #{tp.rank}
                  </div>
                  <div>
                    <div style={{ fontSize: '0.8rem', fontWeight: 600, color: '#f1f5f9' }}>{tp.name}</div>
                    <div style={{ fontSize: '0.7rem', color: '#64748b' }}>
                      {tp.roll} • {tp.semester}
                    </div>
                  </div>
                </div>
                <div
                  style={{
                    fontSize: '0.85rem',
                    fontWeight: 700,
                    color: '#34d399',
                    backgroundColor: 'rgba(52, 211, 153, 0.12)',
                    padding: '2px 8px',
                    borderRadius: '6px',
                  }}
                >
                  {tp.gpa} GPA
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};
