import React from 'react';
import { ShieldCheck, BookOpen, GraduationCap } from 'lucide-react';

export interface StudentProfileCardProps {
  studentName?: string;
  studentId?: string;
  program?: string;
  department?: string;
  semester?: string;
  academicStanding?: string;
}

export const StudentProfileCard: React.FC<StudentProfileCardProps> = ({
  studentName = 'Rahul Kumar',
  studentId = 'STU-2026-001',
  program = 'B.Tech Computer Science',
  department = 'Computer Science & Engineering',
  semester = 'Semester 5',
  academicStanding = 'Good',
}) => {
  return (
    <div
      style={{
        backgroundColor: 'rgba(30, 41, 59, 0.7)',
        backdropFilter: 'blur(12px)',
        border: '1px solid rgba(56, 189, 248, 0.25)',
        borderRadius: '16px',
        padding: '1.25rem',
        display: 'flex',
        alignItems: 'center',
        gap: '1.25rem',
        boxShadow: '0 4px 20px rgba(0, 0, 0, 0.2)',
        flexWrap: 'wrap',
      }}
    >
      {/* Student Avatar */}
      <div
        style={{
          width: '72px',
          height: '72px',
          borderRadius: '18px',
          background: 'linear-gradient(135deg, #2563eb, #0ea5e9)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          color: '#ffffff',
          fontWeight: 800,
          fontSize: '1.8rem',
          boxShadow: '0 4px 16px rgba(37, 99, 235, 0.4)',
        }}
      >
        {studentName.charAt(0)}
      </div>

      {/* Student Details */}
      <div style={{ flex: 1, minWidth: '220px' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '4px' }}>
          <span
            style={{
              backgroundColor: 'rgba(52, 211, 153, 0.15)',
              color: '#34d399',
              fontSize: '0.72rem',
              fontWeight: 700,
              padding: '2px 8px',
              borderRadius: '12px',
              border: '1px solid rgba(52, 211, 153, 0.3)',
              display: 'inline-flex',
              alignItems: 'center',
              gap: '4px',
            }}
          >
            <ShieldCheck size={12} /> Standing: {academicStanding}
          </span>
          <span style={{ fontSize: '0.75rem', color: '#94a3b8' }}>ID: {studentId}</span>
        </div>

        <h2 style={{ fontSize: '1.35rem', fontWeight: 800, color: '#f8fafc', margin: '2px 0 4px 0' }}>
          {studentName}
        </h2>

        <div style={{ display: 'flex', alignItems: 'center', gap: '12px', fontSize: '0.8rem', color: '#cbd5e1', flexWrap: 'wrap' }}>
          <span style={{ display: 'inline-flex', alignItems: 'center', gap: '4px' }}>
            <GraduationCap size={14} color="#38bdf8" /> {program}
          </span>
          <span>•</span>
          <span style={{ display: 'inline-flex', alignItems: 'center', gap: '4px' }}>
            <BookOpen size={14} color="#a855f7" /> {department} ({semester})
          </span>
        </div>
      </div>
    </div>
  );
};
