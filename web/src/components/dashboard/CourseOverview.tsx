import React from 'react';
import { BookOpen } from 'lucide-react';

export const CourseOverview: React.FC = () => {
  const courses = [
    { code: 'CS501', title: 'Advanced Algorithms', faculty: 'Dr. Rao', credits: 4, semester: 'Semester 5', attendance: 91, grade: 'A' },
    { code: 'CS502', title: 'Database Management Systems', faculty: 'Dr. Sarah Jenkins', credits: 4, semester: 'Semester 5', attendance: 86, grade: 'A-' },
    { code: 'CS503', title: 'Operating Systems', faculty: 'Prof. Alan Turing', credits: 4, semester: 'Semester 5', attendance: 79, grade: 'B+' },
    { code: 'CS504', title: 'Computer Networks', faculty: 'Dr. Robert Rao', credits: 3, semester: 'Semester 5', attendance: 93, grade: 'A' },
    { code: 'CS505', title: 'Software Engineering', faculty: 'Prof. Michael Scott', credits: 3, semester: 'Semester 5', attendance: 88, grade: 'A' },
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
            Enrolled Courses & Academic Metrics
          </h3>
          <p style={{ fontSize: '0.78rem', color: '#94a3b8', margin: '2px 0 0 0' }}>
            5 active courses enrolled in Semester 5 (Total 18 Credits)
          </p>
        </div>
        <BookOpen size={20} color="#38bdf8" />
      </div>

      <div style={{ overflowX: 'auto' }}>
        <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: '0.825rem' }}>
          <thead>
            <tr style={{ borderBottom: '1px solid rgba(255, 255, 255, 0.1)', color: '#64748b', textAlign: 'left' }}>
              <th style={{ padding: '8px 10px', fontWeight: 600 }}>Code</th>
              <th style={{ padding: '8px 10px', fontWeight: 600 }}>Course Name</th>
              <th style={{ padding: '8px 10px', fontWeight: 600 }}>Faculty</th>
              <th style={{ padding: '8px 10px', fontWeight: 600 }}>Credits</th>
              <th style={{ padding: '8px 10px', fontWeight: 600 }}>Attendance</th>
              <th style={{ padding: '8px 10px', fontWeight: 600 }}>Grade</th>
            </tr>
          </thead>
          <tbody>
            {courses.map((c) => (
              <tr
                key={c.code}
                style={{
                  borderBottom: '1px solid rgba(255, 255, 255, 0.05)',
                  color: '#e2e8f0',
                }}
              >
                <td style={{ padding: '10px 10px', fontWeight: 700, color: '#38bdf8' }}>{c.code}</td>
                <td style={{ padding: '10px 10px', fontWeight: 600, color: '#f8fafc' }}>{c.title}</td>
                <td style={{ padding: '10px 10px', color: '#94a3b8' }}>{c.faculty}</td>
                <td style={{ padding: '10px 10px', color: '#cbd5e1' }}>{c.credits}</td>
                <td style={{ padding: '10px 10px' }}>
                  <span style={{ color: c.attendance < 80 ? '#f59e0b' : '#34d399', fontWeight: 700 }}>
                    {c.attendance}%
                  </span>
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
                    {c.grade}
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
