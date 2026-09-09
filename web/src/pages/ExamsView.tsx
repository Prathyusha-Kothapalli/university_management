import React, { useState } from 'react';

export const ExamsView: React.FC = () => {
  const [tab, setTab] = useState<'schedule' | 'results'>('schedule');
  const [downloaded, setDownloaded] = useState(false);

  const exams = [
    {
      code: 'CS-401',
      name: 'Deep Learning & Neural Architectures',
      date: 'Oct 12, 2026',
      time: '09:30 AM - 12:30 PM',
      hall: 'Turing Hall B-204',
      seat: 'Row 3, Seat 14',
    },
    {
      code: 'DS-310',
      name: 'Big Data Distributed Systems',
      date: 'Oct 15, 2026',
      time: '02:00 PM - 05:00 PM',
      hall: 'Newton Complex N-101',
      seat: 'Row 1, Seat 08',
    },
    {
      code: 'MATH-250',
      name: 'Stochastic Calculus & Optimization',
      date: 'Oct 19, 2026',
      time: '09:30 AM - 12:30 PM',
      hall: 'Euler Auditorium E-302',
      seat: 'Row 4, Seat 22',
    },
    {
      code: 'AI-480',
      name: 'Autonomous Robotics & Computer Vision',
      date: 'Oct 23, 2026',
      time: '02:00 PM - 05:00 PM',
      hall: 'Robotics Lab R-04',
      seat: 'Station 12',
    },
  ];

  const results = [
    { sem: 'Semester 5 (Spring 2026)', sgpa: '9.50', credits: 24, status: 'Passed with Distinction' },
    { sem: 'Semester 4 (Fall 2025)', sgpa: '9.35', credits: 22, status: 'Passed with Distinction' },
    { sem: 'Semester 3 (Spring 2025)', sgpa: '9.40', credits: 24, status: 'Passed' },
    { sem: 'Semester 2 (Fall 2024)', sgpa: '9.20', credits: 20, status: 'Passed' },
    { sem: 'Semester 1 (Spring 2024)', sgpa: '9.65', credits: 22, status: 'Passed with Distinction' },
  ];

  return (
    <div style={{ padding: '1.25rem' }}>
      {/* CGPA Banner */}
      <div style={{
        background: 'linear-gradient(135deg, #7c3aed, #4f46e5)',
        padding: '1.25rem',
        borderRadius: '16px',
        color: '#fff',
        marginBottom: '1rem',
      }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <span style={{ fontSize: '0.8rem', fontWeight: 600, opacity: 0.9 }}>Cumulative GPA (CGPA)</span>
          <span style={{
            fontSize: '0.7rem',
            padding: '2px 8px',
            borderRadius: '10px',
            backgroundColor: 'rgba(255,255,255,0.2)',
            fontWeight: 700,
          }}>
            Rank #4 in Dept
          </span>
        </div>
        <div style={{ fontSize: '2.1rem', fontWeight: 800, marginTop: '4px' }}>9.42 / 10.0</div>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginTop: '8px' }}>
          <span style={{ fontSize: '0.78rem', opacity: 0.85 }}>112 Credits Completed</span>
          <button
            onClick={() => setDownloaded(true)}
            style={{
              background: downloaded ? '#10b981' : 'rgba(255, 255, 255, 0.25)',
              border: 'none',
              color: '#fff',
              fontSize: '0.72rem',
              fontWeight: 700,
              padding: '4px 10px',
              borderRadius: '8px',
              cursor: 'pointer',
            }}
          >
            {downloaded ? '✓ Hall Ticket Saved' : '📥 Hall Ticket'}
          </button>
        </div>
      </div>

      {/* Tabs */}
      <div style={{ display: 'flex', gap: '8px', marginBottom: '1rem' }}>
        <button
          onClick={() => setTab('schedule')}
          className={`btn ${tab === 'schedule' ? 'btn-primary' : 'btn-secondary'}`}
          style={{ flex: 1, padding: '8px', fontSize: '0.825rem' }}
        >
          Upcoming Exams ({exams.length})
        </button>
        <button
          onClick={() => setTab('results')}
          className={`btn ${tab === 'results' ? 'btn-primary' : 'btn-secondary'}`}
          style={{ flex: 1, padding: '8px', fontSize: '0.825rem' }}
        >
          Semester Transcripts
        </button>
      </div>

      {/* Content */}
      {tab === 'schedule' ? (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
          {exams.map((exam, i) => (
            <div key={i} className="glass-panel" style={{ padding: '1rem' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '6px' }}>
                <span style={{
                  fontSize: '0.75rem',
                  fontWeight: 700,
                  color: '#a78bfa',
                  padding: '2px 8px',
                  borderRadius: '6px',
                  background: 'rgba(167, 139, 250, 0.15)',
                }}>
                  {exam.code}
                </span>
                <span style={{ fontSize: '0.75rem', color: '#f59e0b', fontWeight: 600 }}>
                  📅 {exam.date}
                </span>
              </div>
              <div style={{ fontSize: '0.925rem', fontWeight: 700, color: '#f8fafc', marginBottom: '6px' }}>
                {exam.name}
              </div>
              <div style={{ fontSize: '0.78rem', color: '#94a3b8', display: 'flex', flexDirection: 'column', gap: '3px' }}>
                <div>⏰ <strong>Time:</strong> {exam.time}</div>
                <div>🏛️ <strong>Venue:</strong> {exam.hall}</div>
                <div>🪑 <strong>Allocation:</strong> {exam.seat}</div>
              </div>
            </div>
          ))}
        </div>
      ) : (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
          {results.map((res, i) => (
            <div key={i} className="glass-panel" style={{ padding: '1rem' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                <span style={{ fontSize: '0.85rem', fontWeight: 700, color: '#f8fafc' }}>
                  {res.sem}
                </span>
                <span style={{
                  fontSize: '0.95rem',
                  fontWeight: 800,
                  color: '#34d399',
                }}>
                  {res.sgpa} SGPA
                </span>
              </div>
              <div style={{ display: 'flex', justifyContent: 'space-between', marginTop: '6px', fontSize: '0.78rem', color: '#94a3b8' }}>
                <span>Credits: {res.credits}</span>
                <span style={{ color: '#60a5fa' }}>{res.status}</span>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};
