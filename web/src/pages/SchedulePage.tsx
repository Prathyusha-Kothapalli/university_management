import React, { useState, useEffect } from 'react';
import { User, ScheduleItem } from '../types/auth';
import { getStoredSchedule } from '../services/scheduleStore';
import { FacultyTimetableModal } from '../components/FacultyTimetableModal';

interface SchedulePageProps {
  user?: User | null;
}

export const SchedulePage: React.FC<SchedulePageProps> = ({ user }) => {
  const [schedule, setSchedule] = useState<ScheduleItem[]>(() => getStoredSchedule());
  const [selectedDay, setSelectedDay] = useState('Monday');
  const [modalOpen, setModalOpen] = useState(false);
  const [editingItem, setEditingItem] = useState<ScheduleItem | null>(null);

  const days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'];

  const reloadSchedule = () => {
    setSchedule(getStoredSchedule());
  };

  useEffect(() => {
    const handleUpdated = () => reloadSchedule();
    window.addEventListener('unisphere_schedule_updated', handleUpdated);
    return () => window.removeEventListener('unisphere_schedule_updated', handleUpdated);
  }, []);

  const filtered = schedule.filter((s) => s.day === selectedDay);
  const isFaculty = user?.role === 'faculty';

  const handleOpenAdd = () => {
    setEditingItem(null);
    setModalOpen(true);
  };

  const handleOpenEdit = (item: ScheduleItem) => {
    setEditingItem(item);
    setModalOpen(true);
  };

  return (
    <div style={{ maxWidth: '1200px', margin: '0 auto', padding: '2rem 1.5rem', width: '100%' }}>
      {/* Header with Title and Faculty Actions */}
      <div style={{
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'flex-start',
        flexWrap: 'wrap',
        gap: '1rem',
        marginBottom: '1.75rem',
      }}>
        <div>
          <h1 style={{ fontSize: '1.8rem', fontWeight: 800, color: '#f8fafc', letterSpacing: '-0.5px' }}>
            Weekly Lecture Timetable
          </h1>
          <p style={{ fontSize: '0.9rem', color: '#94a3b8' }}>
            {isFaculty
              ? 'Faculty Class Schedule Management • Add or reschedule your lecture slots'
              : 'Interactive campus lecture and lab hours for the active semester'}
          </p>
        </div>

        {isFaculty && (
          <button
            onClick={handleOpenAdd}
            className="btn btn-primary"
            style={{ display: 'flex', alignItems: 'center', gap: '8px' }}
          >
            <span>➕</span>
            <span>Add Lecture Slot</span>
          </button>
        )}
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

              <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
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

                {isFaculty && (
                  <button
                    onClick={() => handleOpenEdit(item)}
                    className="btn btn-secondary"
                    style={{ padding: '8px 14px', fontSize: '0.825rem', whiteSpace: 'nowrap' }}
                    title="Change or reschedule this lecture"
                  >
                    ✏️ Change
                  </button>
                )}
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
              {isFaculty ? 'No teaching duties scheduled for this day. Click "+ Add Lecture Slot" to create one.' : 'Enjoy your study break or use the Digital Library resources!'}
            </div>
          </div>
        )}
      </div>

      {/* Faculty Timetable Edit/Add Modal */}
      {isFaculty && (
        <FacultyTimetableModal
          isOpen={modalOpen}
          onClose={() => setModalOpen(false)}
          onScheduleUpdated={reloadSchedule}
          initialItem={editingItem}
          instructorName={user?.name || 'Prof. Arthur Vance'}
        />
      )}
    </div>
  );
};
