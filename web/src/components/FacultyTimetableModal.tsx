import React, { useState } from 'react';
import { ScheduleItem } from '../types/auth';
import { addScheduleItem, updateScheduleItem, deleteScheduleItem } from '../services/scheduleStore';

interface FacultyTimetableModalProps {
  isOpen: boolean;
  onClose: () => void;
  onScheduleUpdated: () => void;
  initialItem?: ScheduleItem | null;
  instructorName: string;
}

export const FacultyTimetableModal: React.FC<FacultyTimetableModalProps> = ({
  isOpen,
  onClose,
  onScheduleUpdated,
  initialItem,
  instructorName,
}) => {
  const isEditing = Boolean(initialItem);

  const [code, setCode] = useState(initialItem?.code || 'CS-401');
  const [title, setTitle] = useState(initialItem?.title || 'Deep Learning & Neural Architectures');
  const [day, setDay] = useState(initialItem?.day || 'Monday');
  const [time, setTime] = useState(initialItem?.time || '10:00 AM - 11:30 AM');
  const [room, setRoom] = useState(initialItem?.room || 'Turing Hall B-204');
  const [status, setStatus] = useState<ScheduleItem['status']>(initialItem?.status || 'Upcoming');
  const [color, setColor] = useState(initialItem?.color || '#2563eb');

  if (!isOpen) return null;

  const days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'];
  const commonColors = [
    { label: 'Blue', val: '#2563eb' },
    { label: 'Cyan', val: '#0ea5e9' },
    { label: 'Emerald', val: '#10b981' },
    { label: 'Purple', val: '#8b5cf6' },
    { label: 'Amber', val: '#f59e0b' },
  ];

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!code || !title || !time || !room) {
      alert('Please fill out all timetable fields.');
      return;
    }

    if (isEditing && initialItem) {
      updateScheduleItem(initialItem.id, {
        code,
        title,
        day,
        time,
        room,
        status,
        color,
        instructor: instructorName,
      });
    } else {
      addScheduleItem({
        code,
        title,
        day,
        time,
        room,
        status,
        color,
        instructor: instructorName,
      });
    }

    onScheduleUpdated();
    onClose();
  };

  const handleDelete = () => {
    if (!initialItem) return;
    if (window.confirm(`Are you sure you want to cancel and remove ${initialItem.code} from the timetable?`)) {
      deleteScheduleItem(initialItem.id);
      onScheduleUpdated();
      onClose();
    }
  };

  return (
    <div style={{
      position: 'fixed',
      top: 0,
      left: 0,
      right: 0,
      bottom: 0,
      backgroundColor: 'rgba(0, 0, 0, 0.75)',
      backdropFilter: 'blur(8px)',
      zIndex: 9999,
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      padding: '1rem',
    }}>
      <div style={{
        background: '#1c2541',
        border: '1px solid var(--color-border)',
        borderRadius: '20px',
        width: '100%',
        maxWidth: '520px',
        boxShadow: '0 20px 50px rgba(0, 0, 0, 0.6)',
        overflow: 'hidden',
        animation: 'fadeIn 0.2s ease-out',
      }}>
        {/* Modal Header */}
        <div style={{
          padding: '1.25rem 1.5rem',
          background: 'linear-gradient(135deg, #1e3a8a, #2563eb)',
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          color: '#ffffff',
        }}>
          <div>
            <h3 style={{ fontSize: '1.2rem', fontWeight: 800 }}>
              {isEditing ? '✏️ Change & Reschedule Lecture' : '➕ Add Faculty Lecture Slot'}
            </h3>
            <p style={{ fontSize: '0.8rem', opacity: 0.9, marginTop: '2px' }}>
              Instructor: {instructorName}
            </p>
          </div>
          <button
            onClick={onClose}
            style={{
              background: 'rgba(255, 255, 255, 0.2)',
              border: 'none',
              color: '#ffffff',
              borderRadius: '50%',
              width: '32px',
              height: '32px',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              cursor: 'pointer',
              fontWeight: 700,
              fontSize: '1rem',
            }}
          >
            ✕
          </button>
        </div>

        {/* Modal Form */}
        <form onSubmit={handleSubmit} style={{ padding: '1.5rem', display: 'flex', flexDirection: 'column', gap: '14px' }}>
          <div style={{ display: 'grid', gridTemplateColumns: '1fr 2fr', gap: '12px' }}>
            <div className="form-group" style={{ marginBottom: 0 }}>
              <label className="form-label">Course Code</label>
              <input
                type="text"
                className="form-input"
                value={code}
                onChange={(e) => setCode(e.target.value)}
                placeholder="e.g. CS-401"
                required
              />
            </div>
            <div className="form-group" style={{ marginBottom: 0 }}>
              <label className="form-label">Course Name</label>
              <input
                type="text"
                className="form-input"
                value={title}
                onChange={(e) => setTitle(e.target.value)}
                placeholder="e.g. Deep Learning"
                required
              />
            </div>
          </div>

          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '12px' }}>
            <div className="form-group" style={{ marginBottom: 0 }}>
              <label className="form-label">Day of Week</label>
              <select
                className="form-input"
                value={day}
                onChange={(e) => setDay(e.target.value)}
                style={{ cursor: 'pointer' }}
              >
                {days.map((d) => (
                  <option key={d} value={d}>{d}</option>
                ))}
              </select>
            </div>

            <div className="form-group" style={{ marginBottom: 0 }}>
              <label className="form-label">Lecture Time Slot</label>
              <input
                type="text"
                className="form-input"
                value={time}
                onChange={(e) => setTime(e.target.value)}
                placeholder="e.g. 10:00 AM - 11:30 AM"
                required
              />
            </div>
          </div>

          <div style={{ display: 'grid', gridTemplateColumns: '1.2fr 1fr', gap: '12px' }}>
            <div className="form-group" style={{ marginBottom: 0 }}>
              <label className="form-label">Classroom / Lab Venue</label>
              <input
                type="text"
                className="form-input"
                value={room}
                onChange={(e) => setRoom(e.target.value)}
                placeholder="e.g. Turing Hall B-204"
                required
              />
            </div>

            <div className="form-group" style={{ marginBottom: 0 }}>
              <label className="form-label">Lecture Status</label>
              <select
                className="form-input"
                value={status}
                onChange={(e) => setStatus(e.target.value as ScheduleItem['status'])}
                style={{ cursor: 'pointer' }}
              >
                <option value="Upcoming">Upcoming</option>
                <option value="Ongoing">Ongoing (In Progress)</option>
                <option value="Completed">Completed</option>
              </select>
            </div>
          </div>

          {/* Color accent */}
          <div>
            <label className="form-label" style={{ marginBottom: '6px', display: 'block' }}>
              Color Tag
            </label>
            <div style={{ display: 'flex', gap: '10px' }}>
              {commonColors.map((c) => (
                <div
                  key={c.val}
                  onClick={() => setColor(c.val)}
                  style={{
                    width: '28px',
                    height: '28px',
                    borderRadius: '8px',
                    backgroundColor: c.val,
                    cursor: 'pointer',
                    border: color === c.val ? '2px solid #ffffff' : '2px solid transparent',
                    boxShadow: color === c.val ? '0 0 10px rgba(255,255,255,0.4)' : 'none',
                  }}
                  title={c.label}
                />
              ))}
            </div>
          </div>

          {/* Form Actions */}
          <div style={{
            display: 'flex',
            justifyContent: isEditing ? 'space-between' : 'flex-end',
            alignItems: 'center',
            marginTop: '10px',
            paddingTop: '12px',
            borderTop: '1px solid rgba(255, 255, 255, 0.08)',
          }}>
            {isEditing && (
              <button
                type="button"
                onClick={handleDelete}
                className="btn btn-danger"
                style={{ fontSize: '0.85rem', padding: '8px 14px' }}
              >
                🗑️ Cancel Lecture
              </button>
            )}

            <div style={{ display: 'flex', gap: '10px' }}>
              <button
                type="button"
                onClick={onClose}
                className="btn btn-secondary"
                style={{ fontSize: '0.85rem' }}
              >
                Dismiss
              </button>
              <button
                type="submit"
                className="btn btn-primary"
                style={{ fontSize: '0.85rem' }}
              >
                {isEditing ? '💾 Save Schedule Change' : '➕ Confirm & Publish Slot'}
              </button>
            </div>
          </div>
        </form>
      </div>
    </div>
  );
};
