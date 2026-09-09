import React from 'react';

export const AttendanceView: React.FC = () => {
  const records = [
    { code: 'CS-401', name: 'Deep Learning & Neural Architectures', attended: 38, total: 40, instructor: 'Prof. A. Vance' },
    { code: 'DS-310', name: 'Big Data Distributed Systems', attended: 32, total: 35, instructor: 'Dr. S. Mitchell' },
    { code: 'MATH-250', name: 'Stochastic Calculus & Optimization', attended: 28, total: 30, instructor: 'Dr. K. Rao' },
    { code: 'AI-480', name: 'Autonomous Robotics & Vision', attended: 26, total: 30, instructor: 'Dr. E. Thorne' },
    { code: 'ETH-102', name: 'AI Safety & Tech Ethics', attended: 19, total: 20, instructor: 'Prof. L. Chen' },
  ];

  const totalAttended = records.reduce((s, r) => s + r.attended, 0);
  const totalHours = records.reduce((s, r) => s + r.total, 0);
  const overallPct = ((totalAttended / totalHours) * 100).toFixed(1);

  return (
    <div style={{ padding: '1.25rem' }}>
      <div style={{
        background: 'linear-gradient(135deg, #1e40af, #0284c7)',
        padding: '1.5rem',
        borderRadius: '16px',
        color: '#fff',
        marginBottom: '1.25rem',
      }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <span style={{ fontSize: '0.8rem', fontWeight: 600, opacity: 0.9 }}>Overall Attendance</span>
          <span style={{
            fontSize: '0.7rem',
            padding: '2px 8px',
            borderRadius: '10px',
            backgroundColor: 'rgba(255,255,255,0.2)',
            fontWeight: 700,
          }}>
            Safe (≥75%)
          </span>
        </div>
        <div style={{ fontSize: '2rem', fontWeight: 800, marginTop: '6px' }}>{overallPct}%</div>
        <div style={{ fontSize: '0.8rem', opacity: 0.85, marginTop: '2px' }}>
          {totalAttended} of {totalHours} Academic Hours Attended
        </div>
      </div>

      <h3 style={{ fontSize: '1.05rem', fontWeight: 700, color: '#f8fafc', marginBottom: '0.75rem' }}>
        Subject Breakdown
      </h3>

      <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
        {records.map((r, idx) => {
          const pct = ((r.attended / r.total) * 100).toFixed(1);
          const isSafe = parseFloat(pct) >= 75;

          return (
            <div key={idx} className="glass-panel" style={{ padding: '1rem' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                <span style={{
                  fontSize: '0.75rem',
                  fontWeight: 700,
                  color: '#38bdf8',
                  padding: '2px 6px',
                  borderRadius: '6px',
                  backgroundColor: 'rgba(56, 189, 248, 0.15)',
                }}>
                  {r.code}
                </span>
                <span style={{
                  fontSize: '0.9rem',
                  fontWeight: 800,
                  color: isSafe ? '#10b981' : '#ef4444',
                }}>
                  {pct}%
                </span>
              </div>
              <div style={{ fontSize: '0.95rem', fontWeight: 700, color: '#f8fafc', marginTop: '6px' }}>
                {r.name}
              </div>
              <div style={{ fontSize: '0.75rem', color: '#94a3b8', marginTop: '2px' }}>
                {r.instructor} • {r.attended}/{r.total} Hours
              </div>
              <div style={{
                height: '6px',
                width: '100%',
                backgroundColor: 'rgba(15, 23, 42, 0.8)',
                borderRadius: '3px',
                marginTop: '8px',
                overflow: 'hidden',
              }}>
                <div style={{
                  height: '100%',
                  width: `${pct}%`,
                  backgroundColor: isSafe ? '#10b981' : '#ef4444',
                  borderRadius: '3px',
                }} />
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
};
