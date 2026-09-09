import React, { useState } from 'react';
import { mockSchedule } from '../services/mockData';

export const SchedulePage: React.FC = () => {
  const [selectedDay, setSelectedDay] = useState('Monday');
  const days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'];

  const filtered = mockSchedule.filter((s) => s.day === selectedDay);

  return (
    <div style={{ maxWidth: '1200px', margin: '0 auto', padding: '2rem 1.5rem', width: '100%' }}>
      <div style={{ marginBottom: '1.75rem' }}>
        <h1 style={{ fontSize: '1.8rem', fontWeight: 800, color: '#f8fafc', letterSpacing: '-0.5px' }}>
          Weekly Lecture Timetable
        </h1>
        <p style={{ fontSize: '0.9rem', color: '#94a3b8' }}>
          Interactive campus lecture and lab hours for the active semester
        </p>
      </div>

      {/* Day Selector Buttons */}
      <div style={{ display: 'flex', gap: '8px', marginBottom: '1.5rem', overflowX: 'auto', paddingBottom: '4px' }}>
        {days.map((d) => (
          <button
            key={d}
            onClick={() => setSelectedDay(d)}
            style={{
              padding: '8px 18px',
              borderRadius: '10px',
              border: selectedDay === d ? '1.5px solid #38bdf8' : '1px solid var(--color-border)',
              backgroundColor: selectedDay === d ? 'rgba(56, 189, 248, 0.2)' : 'rgba(28, 37, 65, 0.6)',
              color: selectedDay === d ? '#38bdf8' : '#94a3b8',
              fontWeight: 700,
              fontSize: '0.875rem',
              cursor: 'pointer',
              transition: 'all 0.2s',
            }}
          >
            {d}
          </button>
        ))}
      </div>

      {/* Schedule Items */}
      <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
        {filtered.length > 0 ? (
          filtered.map((item) => (
            <div
              key={item.id}
              className="glass-panel"
              style={{
                padding: '1.25rem 1.5rem',
                borderLeft: `5px solid ${item.color}`,
                display: 'flex',
                justifyContent: 'space-between',
                alignItems: 'center',
                flexWrap: 'wrap',
                gap: '1rem',
              }}
            >
              <div>
                <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                  <span style={{ fontWeight: 800, fontSize: '1rem', color: '#f8fafc' }}>
                    {item.code}
                  </span>
                  <span style={{
                    fontSize: '0.72rem',
                    padding: '2px 8px',
                    borderRadius: '10px',
                    backgroundColor: item.status === 'Ongoing' ? 'rgba(16, 185, 129, 0.2)' : 'rgba(14, 165, 233, 0.15)',
                    color: item.status === 'Ongoing' ? '#34d399' : '#38bdf8',
                    fontWeight: 700,
                  }}>
                    {item.status}
                  </span>
                </div>
                <div style={{ fontSize: '1.05rem', fontWeight: 600, color: '#e2e8f0', marginTop: '4px' }}>
                  {item.title}
                </div>
                <div style={{ fontSize: '0.85rem', color: '#94a3b8', marginTop: '4px' }}>
                  Faculty: <strong style={{ color: '#cbd5e1' }}>{item.instructor}</strong>
                </div>
              </div>

              <div style={{
                textAlign: 'right',
                backgroundColor: 'rgba(15, 23, 42, 0.6)',
                padding: '10px 16px',
                borderRadius: '12px',
                border: '1px solid var(--color-border)',
              }}>
                <div style={{ fontSize: '0.9rem', fontWeight: 700, color: '#38bdf8' }}>
                  ⏰ {item.time}
                </div>
                <div style={{ fontSize: '0.8rem', color: '#94a3b8', marginTop: '2px' }}>
                  📍 {item.room}
                </div>
              </div>
            </div>
          ))
        ) : (
          <div className="glass-panel" style={{ padding: '3rem', textAlign: 'center', color: '#94a3b8' }}>
            <div style={{ fontSize: '2.5rem', marginBottom: '8px' }}>☕</div>
            <div style={{ fontWeight: 700, fontSize: '1.1rem', color: '#f8fafc' }}>
              No Lectures Scheduled for {selectedDay}
            </div>
            <div style={{ fontSize: '0.85rem', marginTop: '4px' }}>
              Enjoy your study break or use the Digital Library resources!
            </div>
          </div>
        )}
      </div>
    </div>
  );
};
