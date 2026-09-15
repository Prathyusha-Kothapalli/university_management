import React, { useState } from 'react';
import { Filter, CheckCircle2, AlertCircle } from 'lucide-react';

export const AttendanceOverview: React.FC = () => {
  const [selectedSem, setSelectedSem] = useState('Sem 5');

  const courses = [
    { code: 'CS501', name: 'Data Structures', attendance: 91, status: 'Good' },
    { code: 'CS502', name: 'Database Systems', attendance: 86, status: 'Good' },
    { code: 'CS503', name: 'Operating Systems', attendance: 79, status: 'Warning' },
    { code: 'CS504', name: 'Computer Networks', attendance: 93, status: 'Good' },
    { code: 'CS505', name: 'Software Engineering', attendance: 88, status: 'Good' },
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
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1rem', flexWrap: 'wrap', gap: '10px' }}>
        <div>
          <h3 style={{ fontSize: '1.05rem', fontWeight: 700, color: '#f8fafc', margin: 0 }}>
            Student Attendance Analytics
          </h3>
          <p style={{ fontSize: '0.78rem', color: '#94a3b8', margin: '2px 0 0 0' }}>
            Overall: <strong style={{ color: '#38bdf8' }}>86.4%</strong> | Present: <strong style={{ color: '#34d399' }}>142</strong> | Absent: <strong style={{ color: '#f43f5e' }}>22</strong> | Total: 164 Sessions
          </p>
        </div>

        <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
          <Filter size={14} color="#94a3b8" />
          <select
            value={selectedSem}
            onChange={(e) => setSelectedSem(e.target.value)}
            style={{
              backgroundColor: 'rgba(15, 23, 42, 0.8)',
              border: '1px solid rgba(255, 255, 255, 0.12)',
              borderRadius: '8px',
              color: '#f8fafc',
              padding: '4px 10px',
              fontSize: '0.78rem',
              outline: 'none',
              cursor: 'pointer',
            }}
          >
            <option value="Sem 5">Semester 5</option>
            <option value="Sem 4">Semester 4</option>
          </select>
        </div>
      </div>

      {/* Low Attendance Alert if any course <80% */}
      <div
        style={{
          backgroundColor: 'rgba(245, 158, 11, 0.12)',
          border: '1px solid rgba(245, 158, 11, 0.3)',
          borderRadius: '10px',
          padding: '10px 12px',
          marginBottom: '1rem',
          display: 'flex',
          alignItems: 'center',
          gap: '8px',
          fontSize: '0.78rem',
          color: '#f59e0b',
        }}
      >
        <AlertCircle size={16} color="#f59e0b" />
        <span>
          <strong>Attendance Advisory:</strong> Operating Systems attendance is currently at <strong>79%</strong> (threshold: 80%). Regular attendance is advised.
        </span>
      </div>

      {/* Course-wise Breakdown */}
      <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
        {courses.map((c) => (
          <div
            key={c.code}
            style={{
              backgroundColor: 'rgba(15, 23, 42, 0.5)',
              border: '1px solid rgba(255, 255, 255, 0.05)',
              borderRadius: '10px',
              padding: '10px 12px',
              display: 'flex',
              flexDirection: 'column',
              gap: '6px',
            }}
          >
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                <span style={{ backgroundColor: 'rgba(37, 99, 235, 0.2)', color: '#60a5fa', padding: '2px 6px', borderRadius: '4px', fontSize: '0.72rem', fontWeight: 700 }}>
                  {c.code}
                </span>
                <span style={{ fontSize: '0.85rem', fontWeight: 600, color: '#f1f5f9' }}>{c.name}</span>
              </div>
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                <span style={{ fontSize: '0.85rem', fontWeight: 700, color: c.attendance < 80 ? '#f59e0b' : '#34d399' }}>
                  {c.attendance}%
                </span>
                {c.attendance < 80 ? <AlertCircle size={15} color="#f59e0b" /> : <CheckCircle2 size={15} color="#34d399" />}
              </div>
            </div>

            <div style={{ height: '6px', width: '100%', backgroundColor: 'rgba(255, 255, 255, 0.08)', borderRadius: '3px', overflow: 'hidden' }}>
              <div
                style={{
                  height: '100%',
                  width: `${c.attendance}%`,
                  backgroundColor: c.attendance < 80 ? '#f59e0b' : '#34d399',
                  borderRadius: '3px',
                }}
              />
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
