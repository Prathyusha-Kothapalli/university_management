import React from 'react';
import { Calendar, Clock, MapPin, User } from 'lucide-react';

export const TodaysSchedule: React.FC = () => {
  const schedules = [
    { time: '09:00 AM - 10:00 AM', course: 'CS301 Database Systems', room: 'Lab 304', faculty: 'Dr. Sarah Jenkins', status: 'Ongoing' },
    { time: '10:15 AM - 11:15 AM', course: 'CS302 Operating Systems', room: 'Hall B-12', faculty: 'Prof. Alan Turing', status: 'Upcoming' },
    { time: '11:30 AM - 12:30 PM', course: 'CS401 Machine Learning', room: 'AI Lab 2', faculty: 'Dr. Emily Vance', status: 'Upcoming' },
    { time: '02:00 PM - 03:30 PM', course: 'CS201 Data Structures', room: 'Hall A-04', faculty: 'Dr. Grace Hopper', status: 'Upcoming' },
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
            Today's Department Timetable
          </h3>
          <p style={{ fontSize: '0.78rem', color: '#94a3b8', margin: '2px 0 0 0' }}>
            Live classroom and laboratory session tracking
          </p>
        </div>
        <Calendar size={20} color="#38bdf8" />
      </div>

      <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
        {schedules.map((s, i) => (
          <div
            key={i}
            style={{
              backgroundColor: 'rgba(15, 23, 42, 0.5)',
              border: s.status === 'Ongoing' ? '1px solid rgba(56, 189, 248, 0.4)' : '1px solid rgba(255, 255, 255, 0.05)',
              borderRadius: '10px',
              padding: '10px 12px',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'space-between',
            }}
          >
            <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
              <div
                style={{
                  display: 'flex',
                  alignItems: 'center',
                  gap: '4px',
                  fontSize: '0.75rem',
                  fontWeight: 600,
                  color: s.status === 'Ongoing' ? '#38bdf8' : '#94a3b8',
                  minWidth: '140px',
                }}
              >
                <Clock size={14} />
                {s.time}
              </div>
              <div>
                <div style={{ fontSize: '0.85rem', fontWeight: 700, color: '#f1f5f9' }}>{s.course}</div>
                <div style={{ fontSize: '0.72rem', color: '#64748b', display: 'flex', gap: '12px', marginTop: '2px' }}>
                  <span style={{ display: 'inline-flex', alignItems: 'center', gap: '3px' }}>
                    <MapPin size={12} /> {s.room}
                  </span>
                  <span style={{ display: 'inline-flex', alignItems: 'center', gap: '3px' }}>
                    <User size={12} /> {s.faculty}
                  </span>
                </div>
              </div>
            </div>

            <span
              style={{
                fontSize: '0.7rem',
                fontWeight: 700,
                padding: '3px 8px',
                borderRadius: '6px',
                backgroundColor: s.status === 'Ongoing' ? 'rgba(56, 189, 248, 0.2)' : 'rgba(255, 255, 255, 0.06)',
                color: s.status === 'Ongoing' ? '#38bdf8' : '#64748b',
              }}
            >
              {s.status}
            </span>
          </div>
        ))}
      </div>
    </div>
  );
};
