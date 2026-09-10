import React, { useState } from 'react';
import { Filter, CheckCircle2, AlertCircle } from 'lucide-react';

export const AttendanceAnalytics: React.FC = () => {
  const [selectedSemester, setSelectedSemester] = useState<string>('all');

  const courseData = [
    { code: 'CS301', name: 'Database Management Systems', semester: 'Sem 5', faculty: 'Dr. Sarah Jenkins', attendance: 92.4, status: 'Good' },
    { code: 'CS302', name: 'Operating Systems', semester: 'Sem 5', faculty: 'Prof. Alan Turing', attendance: 88.1, status: 'Good' },
    { code: 'CS303', name: 'Computer Networks', semester: 'Sem 5', faculty: 'Dr. Robert Rao', attendance: 84.6, status: 'Good' },
    { code: 'CS401', name: 'Machine Learning & AI', semester: 'Sem 7', faculty: 'Dr. Emily Vance', attendance: 94.0, status: 'Good' },
    { code: 'CS402', name: 'Distributed Systems', semester: 'Sem 7', faculty: 'Prof. Michael Scott', attendance: 73.2, status: 'Warning' },
    { code: 'CS201', name: 'Data Structures & Algorithms', semester: 'Sem 3', faculty: 'Dr. Grace Hopper', attendance: 89.5, status: 'Good' },
    { code: 'CS202', name: 'Discrete Mathematics', semester: 'Sem 3', faculty: 'Prof. David Miller', attendance: 71.8, status: 'Warning' },
  ];

  const filtered = selectedSemester === 'all'
    ? courseData
    : courseData.filter((c) => c.semester.toLowerCase() === selectedSemester.toLowerCase());

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
      <div
        style={{
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          marginBottom: '1rem',
          flexWrap: 'wrap',
          gap: '10px',
        }}
      >
        <div>
          <h3 style={{ fontSize: '1.05rem', fontWeight: 700, color: '#f8fafc', margin: 0 }}>
            Department Attendance Analytics
          </h3>
          <p style={{ fontSize: '0.78rem', color: '#94a3b8', margin: '2px 0 0 0' }}>
            Course-wise real-time student attendance monitoring
          </p>
        </div>

        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
          <Filter size={15} color="#94a3b8" />
          <select
            value={selectedSemester}
            onChange={(e) => setSelectedSemester(e.target.value)}
            style={{
              backgroundColor: 'rgba(15, 23, 42, 0.8)',
              border: '1px solid rgba(255, 255, 255, 0.12)',
              borderRadius: '8px',
              color: '#f8fafc',
              padding: '6px 12px',
              fontSize: '0.8rem',
              outline: 'none',
              cursor: 'pointer',
            }}
          >
            <option value="all">All Semesters</option>
            <option value="sem 3">Semester 3</option>
            <option value="sem 5">Semester 5</option>
            <option value="sem 7">Semester 7</option>
          </select>
        </div>
      </div>

      <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
        {filtered.map((item) => (
          <div
            key={item.code}
            style={{
              backgroundColor: 'rgba(15, 23, 42, 0.5)',
              border: '1px solid rgba(255, 255, 255, 0.05)',
              borderRadius: '10px',
              padding: '12px 14px',
              display: 'flex',
              flexDirection: 'column',
              gap: '8px',
            }}
          >
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                <span
                  style={{
                    backgroundColor: 'rgba(37, 99, 235, 0.2)',
                    color: '#60a5fa',
                    padding: '2px 8px',
                    borderRadius: '6px',
                    fontSize: '0.72rem',
                    fontWeight: 700,
                  }}
                >
                  {item.code}
                </span>
                <span style={{ fontSize: '0.875rem', fontWeight: 600, color: '#f1f5f9' }}>{item.name}</span>
                <span style={{ fontSize: '0.75rem', color: '#64748b' }}>({item.semester})</span>
              </div>
              <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                <span style={{ fontSize: '0.875rem', fontWeight: 700, color: item.attendance < 75 ? '#f43f5e' : '#34d399' }}>
                  {item.attendance}%
                </span>
                {item.attendance < 75 ? (
                  <AlertCircle size={16} color="#f43f5e" />
                ) : (
                  <CheckCircle2 size={16} color="#34d399" />
                )}
              </div>
            </div>

            {/* Attendance Bar */}
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
                  width: `${item.attendance}%`,
                  backgroundColor: item.attendance < 75 ? '#f43f5e' : item.attendance < 85 ? '#f59e0b' : '#34d399',
                  borderRadius: '3px',
                  transition: 'width 0.4s ease',
                }}
              />
            </div>

            <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.75rem', color: '#64748b' }}>
              <span>Faculty: {item.faculty}</span>
              <span>
                {item.attendance < 75 ? (
                  <span style={{ color: '#f43f5e', fontWeight: 600 }}>Action Required (&lt;75%)</span>
                ) : (
                  'Optimal'
                )}
              </span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
