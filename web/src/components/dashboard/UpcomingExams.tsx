import React from 'react';
import { Calendar, Clock, MapPin, FileCheck } from 'lucide-react';

export const UpcomingExams: React.FC = () => {
  const exams = [
    { subject: 'Database Systems (Mid-Term)', date: '12 Sep 2026', time: '10:00 AM - 12:00 PM', room: 'Room A-204', daysLeft: '2 Days Left' },
    { subject: 'Operating Systems (Mid-Term)', date: '15 Sep 2026', time: '02:00 PM - 04:00 PM', room: 'Room B-102', daysLeft: '5 Days Left' },
    { subject: 'Computer Networks (Mid-Term)', date: '18 Sep 2026', time: '10:00 AM - 12:00 PM', room: 'Room C-301', daysLeft: '8 Days Left' },
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
            Upcoming Examinations Schedule
          </h3>
          <p style={{ fontSize: '0.78rem', color: '#94a3b8', margin: '2px 0 0 0' }}>
            Mid-Semester Examination Schedule for Semester 5
          </p>
        </div>
        <FileCheck size={20} color="#38bdf8" />
      </div>

      <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
        {exams.map((e, index) => (
          <div
            key={index}
            style={{
              backgroundColor: 'rgba(15, 23, 42, 0.5)',
              border: '1px solid rgba(255, 255, 255, 0.05)',
              borderRadius: '10px',
              padding: '10px 12px',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'space-between',
            }}
          >
            <div>
              <div style={{ fontSize: '0.85rem', fontWeight: 700, color: '#f1f5f9' }}>{e.subject}</div>
              <div style={{ fontSize: '0.72rem', color: '#64748b', marginTop: '2px', display: 'flex', gap: '12px' }}>
                <span style={{ display: 'inline-flex', alignItems: 'center', gap: '3px' }}>
                  <Calendar size={12} /> {e.date}
                </span>
                <span style={{ display: 'inline-flex', alignItems: 'center', gap: '3px' }}>
                  <Clock size={12} /> {e.time}
                </span>
                <span style={{ display: 'inline-flex', alignItems: 'center', gap: '3px' }}>
                  <MapPin size={12} /> {e.room}
                </span>
              </div>
            </div>

            <span
              style={{
                backgroundColor: 'rgba(56, 189, 248, 0.15)',
                color: '#38bdf8',
                fontSize: '0.72rem',
                fontWeight: 700,
                padding: '3px 8px',
                borderRadius: '6px',
              }}
            >
              {e.daysLeft}
            </span>
          </div>
        ))}
      </div>
    </div>
  );
};
