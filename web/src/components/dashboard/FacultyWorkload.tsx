import React from 'react';
import { UserCheck, Clock, BookOpen } from 'lucide-react';

export const FacultyWorkload: React.FC = () => {
  const facultyList = [
    { name: 'Dr. Sarah Jenkins', designation: 'Professor', loadHours: 16, totalStudents: 180, courses: 2, status: 'Optimal' },
    { name: 'Prof. Alan Turing', designation: 'Professor', loadHours: 20, totalStudents: 220, courses: 3, status: 'Heavy' },
    { name: 'Dr. Robert Rao', designation: 'HOD & Professor', loadHours: 12, totalStudents: 140, courses: 2, status: 'Optimal' },
    { name: 'Dr. Emily Vance', designation: 'Associate Professor', loadHours: 18, totalStudents: 195, courses: 3, status: 'Optimal' },
    { name: 'Prof. Michael Scott', designation: 'Assistant Professor', loadHours: 22, totalStudents: 240, courses: 3, status: 'Heavy' },
    { name: 'Dr. Grace Hopper', designation: 'Associate Professor', loadHours: 14, totalStudents: 150, courses: 2, status: 'Optimal' },
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
            Faculty Teaching Load & Allocation
          </h3>
          <p style={{ fontSize: '0.78rem', color: '#94a3b8', margin: '2px 0 0 0' }}>
            Weekly teaching hours and course load distribution
          </p>
        </div>
        <UserCheck size={20} color="#a855f7" />
      </div>

      <div style={{ overflowX: 'auto' }}>
        <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: '0.825rem' }}>
          <thead>
            <tr style={{ borderBottom: '1px solid rgba(255, 255, 255, 0.1)', color: '#64748b', textAlign: 'left' }}>
              <th style={{ padding: '8px 10px', fontWeight: 600 }}>Faculty Member</th>
              <th style={{ padding: '8px 10px', fontWeight: 600 }}>Designation</th>
              <th style={{ padding: '8px 10px', fontWeight: 600 }}>Courses</th>
              <th style={{ padding: '8px 10px', fontWeight: 600 }}>Weekly Hrs</th>
              <th style={{ padding: '8px 10px', fontWeight: 600 }}>Students</th>
              <th style={{ padding: '8px 10px', fontWeight: 600 }}>Status</th>
            </tr>
          </thead>
          <tbody>
            {facultyList.map((f) => (
              <tr
                key={f.name}
                style={{
                  borderBottom: '1px solid rgba(255, 255, 255, 0.05)',
                  color: '#e2e8f0',
                  transition: 'background 0.15s ease',
                }}
              >
                <td style={{ padding: '10px 10px', fontWeight: 600, color: '#f8fafc' }}>{f.name}</td>
                <td style={{ padding: '10px 10px', color: '#94a3b8' }}>{f.designation}</td>
                <td style={{ padding: '10px 10px' }}>
                  <span style={{ display: 'inline-flex', alignItems: 'center', gap: '4px', color: '#38bdf8' }}>
                    <BookOpen size={13} /> {f.courses}
                  </span>
                </td>
                <td style={{ padding: '10px 10px' }}>
                  <span style={{ display: 'inline-flex', alignItems: 'center', gap: '4px', color: '#f8fafc' }}>
                    <Clock size={13} color="#94a3b8" /> {f.loadHours} hrs
                  </span>
                </td>
                <td style={{ padding: '10px 10px', color: '#94a3b8' }}>{f.totalStudents}</td>
                <td style={{ padding: '10px 10px' }}>
                  <span
                    style={{
                      padding: '2px 8px',
                      borderRadius: '6px',
                      fontSize: '0.72rem',
                      fontWeight: 600,
                      backgroundColor:
                        f.status === 'Heavy'
                          ? 'rgba(245, 158, 11, 0.15)'
                          : 'rgba(52, 211, 153, 0.15)',
                      color: f.status === 'Heavy' ? '#f59e0b' : '#34d399',
                    }}
                  >
                    {f.status}
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
