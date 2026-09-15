import React, { useState } from 'react';
import { Calendar, Video, MapPin, Plus } from 'lucide-react';
import { useToast } from '../../hooks/useToast';

interface PTMBooking {
  id: string;
  facultyName: string;
  course: string;
  date: string;
  time: string;
  type: 'Virtual (Google Meet)' | 'In-Person (Faculty Office)';
  status: 'Confirmed' | 'Pending Approval' | 'Completed';
}

export const ParentPTMManager: React.FC = () => {
  const { showToast } = useToast();
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [faculty, setFaculty] = useState('Dr. Sarah Jenkins (DB Teacher & Mentor)');
  const [meetingType, setMeetingType] = useState<'Virtual (Google Meet)' | 'In-Person (Faculty Office)'>('Virtual (Google Meet)');
  const [selectedDate, setSelectedDate] = useState('2026-09-18');
  const [selectedTime, setSelectedTime] = useState('03:30 PM');

  const [bookings, setBookings] = useState<PTMBooking[]>([
    {
      id: 'PTM-01',
      facultyName: 'Dr. Sarah Jenkins',
      course: 'Database Management Systems',
      date: 'Sept 15, 2026',
      time: '04:00 PM',
      type: 'Virtual (Google Meet)',
      status: 'Confirmed',
    },
    {
      id: 'PTM-02',
      facultyName: 'Dr. Robert Rao (HOD)',
      course: 'CSE Department Administration',
      date: 'Sept 22, 2026',
      time: '02:30 PM',
      type: 'In-Person (Faculty Office)',
      status: 'Pending Approval',
    },
  ]);

  const handleBookMeeting = (e: React.FormEvent) => {
    e.preventDefault();
    const newBooking: PTMBooking = {
      id: `PTM-0${bookings.length + 1}`,
      facultyName: faculty.split(' (')[0],
      course: 'Academic & Attendance Consultation',
      date: selectedDate,
      time: selectedTime,
      type: meetingType,
      status: 'Confirmed',
    };
    setBookings([newBooking, ...bookings]);
    setIsModalOpen(false);
    showToast(`PTM meeting confirmed with ${newBooking.facultyName} for ${selectedDate} at ${selectedTime}`, 'success');
  };

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
            Parent-Teacher Meetings (PTM) & Consultations
          </h3>
          <p style={{ fontSize: '0.78rem', color: '#94a3b8', margin: '2px 0 0 0' }}>
            Book virtual or in-person 1-on-1 sessions with class faculty & HOD
          </p>
        </div>

        <button
          onClick={() => setIsModalOpen(true)}
          style={{
            backgroundColor: 'rgba(168, 85, 247, 0.2)',
            border: '1px solid rgba(168, 85, 247, 0.4)',
            color: '#c084fc',
            borderRadius: '8px',
            padding: '6px 12px',
            fontSize: '0.78rem',
            fontWeight: 700,
            cursor: 'pointer',
            display: 'flex',
            alignItems: 'center',
            gap: '4px',
          }}
        >
          <Plus size={14} /> Schedule PTM
        </button>
      </div>

      <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
        {bookings.map((b) => (
          <div
            key={b.id}
            style={{
              backgroundColor: 'rgba(15, 23, 42, 0.5)',
              border: '1px solid rgba(255, 255, 255, 0.05)',
              borderRadius: '10px',
              padding: '10px 12px',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'space-between',
              flexWrap: 'wrap',
              gap: '8px',
            }}
          >
            <div>
              <div style={{ fontSize: '0.85rem', fontWeight: 700, color: '#f1f5f9' }}>{b.facultyName}</div>
              <div style={{ fontSize: '0.75rem', color: '#64748b', marginTop: '2px', display: 'flex', gap: '12px' }}>
                <span style={{ display: 'inline-flex', alignItems: 'center', gap: '3px', color: '#38bdf8' }}>
                  <Calendar size={12} /> {b.date} • {b.time}
                </span>
                <span style={{ display: 'inline-flex', alignItems: 'center', gap: '3px' }}>
                  {b.type.includes('Virtual') ? <Video size={12} color="#a855f7" /> : <MapPin size={12} color="#f59e0b" />}
                  {b.type}
                </span>
              </div>
            </div>

            <span
              style={{
                padding: '2px 8px',
                borderRadius: '6px',
                fontSize: '0.72rem',
                fontWeight: 700,
                backgroundColor:
                  b.status === 'Confirmed'
                    ? 'rgba(52, 211, 153, 0.15)'
                    : 'rgba(245, 158, 11, 0.15)',
                color: b.status === 'Confirmed' ? '#34d399' : '#f59e0b',
              }}
            >
              {b.status}
            </span>
          </div>
        ))}
      </div>

      {/* PTM Modal */}
      {isModalOpen && (
        <div
          style={{
            position: 'fixed',
            inset: 0,
            backgroundColor: 'rgba(0, 0, 0, 0.7)',
            backdropFilter: 'blur(8px)',
            zIndex: 200,
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            padding: '1rem',
          }}
        >
          <div
            style={{
              backgroundColor: '#0f172a',
              border: '1px solid rgba(168, 85, 247, 0.4)',
              borderRadius: '16px',
              padding: '1.5rem',
              maxWidth: '480px',
              width: '100%',
              boxShadow: '0 20px 50px rgba(0,0,0,0.5)',
            }}
          >
            <h3 style={{ fontSize: '1.15rem', fontWeight: 800, color: '#f8fafc', margin: '0 0 12px 0' }}>
              Schedule Parent-Teacher Meeting (PTM)
            </h3>
            <form onSubmit={handleBookMeeting} style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
              <div>
                <label style={{ fontSize: '0.78rem', color: '#94a3b8', display: 'block', marginBottom: '4px' }}>Select Faculty / HOD</label>
                <select
                  value={faculty}
                  onChange={(e) => setFaculty(e.target.value)}
                  style={{ width: '100%', backgroundColor: 'rgba(30, 41, 59, 0.9)', border: '1px solid rgba(255,255,255,0.12)', borderRadius: '8px', color: '#f8fafc', padding: '8px 12px', fontSize: '0.825rem' }}
                >
                  <option value="Dr. Sarah Jenkins (DB Teacher & Mentor)">Dr. Sarah Jenkins (Database Systems)</option>
                  <option value="Prof. Alan Turing (OS Professor)">Prof. Alan Turing (Operating Systems)</option>
                  <option value="Dr. Robert Rao (HOD Computer Science)">Dr. Robert Rao (Head of Dept)</option>
                  <option value="Dr. Emily Vance (AI Professor)">Dr. Emily Vance (Machine Learning)</option>
                </select>
              </div>

              <div>
                <label style={{ fontSize: '0.78rem', color: '#94a3b8', display: 'block', marginBottom: '4px' }}>Meeting Mode</label>
                <select
                  value={meetingType}
                  onChange={(e) => setMeetingType(e.target.value as any)}
                  style={{ width: '100%', backgroundColor: 'rgba(30, 41, 59, 0.9)', border: '1px solid rgba(255,255,255,0.12)', borderRadius: '8px', color: '#f8fafc', padding: '8px 12px', fontSize: '0.825rem' }}
                >
                  <option value="Virtual (Google Meet)">Virtual Video Call (Google Meet)</option>
                  <option value="In-Person (Faculty Office)">In-Person (Faculty Cabin 304)</option>
                </select>
              </div>

              <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '10px' }}>
                <div>
                  <label style={{ fontSize: '0.78rem', color: '#94a3b8', display: 'block', marginBottom: '4px' }}>Date</label>
                  <input
                    type="date"
                    value={selectedDate}
                    onChange={(e) => setSelectedDate(e.target.value)}
                    style={{ width: '100%', backgroundColor: 'rgba(30, 41, 59, 0.9)', border: '1px solid rgba(255,255,255,0.12)', borderRadius: '8px', color: '#f8fafc', padding: '8px 12px', fontSize: '0.825rem' }}
                  />
                </div>
                <div>
                  <label style={{ fontSize: '0.78rem', color: '#94a3b8', display: 'block', marginBottom: '4px' }}>Time Slot</label>
                  <select
                    value={selectedTime}
                    onChange={(e) => setSelectedTime(e.target.value)}
                    style={{ width: '100%', backgroundColor: 'rgba(30, 41, 59, 0.9)', border: '1px solid rgba(255,255,255,0.12)', borderRadius: '8px', color: '#f8fafc', padding: '8px 12px', fontSize: '0.825rem' }}
                  >
                    <option value="02:30 PM">02:30 PM</option>
                    <option value="03:30 PM">03:30 PM</option>
                    <option value="04:30 PM">04:30 PM</option>
                  </select>
                </div>
              </div>

              <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '10px', marginTop: '10px' }}>
                <button
                  type="button"
                  onClick={() => setIsModalOpen(false)}
                  style={{ backgroundColor: 'rgba(255, 255, 255, 0.05)', border: '1px solid rgba(255, 255, 255, 0.1)', color: '#94a3b8', borderRadius: '8px', padding: '8px 14px', fontSize: '0.825rem', cursor: 'pointer' }}
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  style={{ backgroundColor: '#a855f7', border: 'none', color: '#ffffff', borderRadius: '8px', padding: '8px 16px', fontSize: '0.825rem', fontWeight: 700, cursor: 'pointer' }}
                >
                  Confirm Booking
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
};
