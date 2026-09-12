import React, { useState } from 'react';
import { User } from '../types/auth';

interface AttendanceViewProps {
  user?: User | null;
  isFaculty?: boolean;
}

interface StudentAttendanceRecord {
  id: string;
  name: string;
  rollNo: string;
  status: 'present' | 'absent' | 'late';
  avatarColor: string;
}

export const AttendanceView: React.FC<AttendanceViewProps> = ({ user, isFaculty = false }) => {
  // Check if role is faculty
  const facultyMode = isFaculty || user?.role === 'faculty';

  // --- STUDENT MODE DATA ---
  const studentRecords = [
    { code: 'CS-401', name: 'Deep Learning & Neural Architectures', attended: 38, total: 40, instructor: 'Prof. A. Vance' },
    { code: 'DS-310', name: 'Big Data Distributed Systems', attended: 32, total: 35, instructor: 'Dr. S. Mitchell' },
    { code: 'MATH-250', name: 'Stochastic Calculus & Optimization', attended: 28, total: 30, instructor: 'Dr. K. Rao' },
    { code: 'AI-480', name: 'Autonomous Robotics & Vision', attended: 26, total: 30, instructor: 'Dr. E. Thorne' },
    { code: 'ETH-102', name: 'AI Safety & Tech Ethics', attended: 19, total: 20, instructor: 'Prof. L. Chen' },
  ];

  const totalAttended = studentRecords.reduce((s, r) => s + r.attended, 0);
  const totalHours = studentRecords.reduce((s, r) => s + r.total, 0);
  const overallPct = ((totalAttended / totalHours) * 100).toFixed(1);

  // --- FACULTY MODE STATE & DATA ---
  const facultyCourses = [
    { id: 'CS-401', name: 'CS-401: Deep Learning (Sec A)', studentsCount: 8 },
    { id: 'AI-480', name: 'AI-480: Autonomous Robotics (Sec B)', studentsCount: 6 },
    { id: 'DS-310', name: 'DS-310: Big Data Systems (Sec A)', studentsCount: 7 },
  ];

  const [selectedCourse, setSelectedCourse] = useState('CS-401');
  const [sessionDate] = useState('Today, Sep 12, 2026');
  const [isSubmitted, setIsSubmitted] = useState(false);

  const [roster, setRoster] = useState<StudentAttendanceRecord[]>([
    { id: 's1', name: 'Alex Rivera', rollNo: 'CS-2023-889', status: 'present', avatarColor: '#38bdf8' },
    { id: 's2', name: 'Elena Rostova', rollNo: 'CS-2023-901', status: 'present', avatarColor: '#ec4899' },
    { id: 's3', name: 'Marcus Chen', rollNo: 'CS-2023-912', status: 'late', avatarColor: '#f59e0b' },
    { id: 's4', name: 'Sarah Jenkins', rollNo: 'CS-2023-924', status: 'absent', avatarColor: '#ef4444' },
    { id: 's5', name: 'David Kim', rollNo: 'CS-2023-933', status: 'present', avatarColor: '#8b5cf6' },
    { id: 's6', name: 'Priya Sharma', rollNo: 'CS-2023-945', status: 'present', avatarColor: '#10b981' },
    { id: 's7', name: 'Liam Wilson', rollNo: 'CS-2023-958', status: 'present', avatarColor: '#06b6d4' },
    { id: 's8', name: 'Zara Al-Mansoor', rollNo: 'CS-2023-970', status: 'present', avatarColor: '#a855f7' },
  ]);

  const updateStudentStatus = (id: string, status: 'present' | 'absent' | 'late') => {
    setRoster((prev) =>
      prev.map((s) => (s.id === id ? { ...s, status } : s))
    );
    setIsSubmitted(false);
  };

  const markAllPresent = () => {
    setRoster((prev) => prev.map((s) => ({ ...s, status: 'present' })));
    setIsSubmitted(false);
  };

  const handleSubmitRoster = () => {
    setIsSubmitted(true);
  };

  const presentCount = roster.filter((s) => s.status === 'present').length;
  const absentCount = roster.filter((s) => s.status === 'absent').length;
  const lateCount = roster.filter((s) => s.status === 'late').length;

  if (facultyMode) {
    return (
      <div style={{ padding: '1.25rem', display: 'flex', flexDirection: 'column', gap: '14px' }}>
        {/* Faculty Header */}
        <div
          style={{
            background: 'linear-gradient(135deg, #312e81, #4f46e5)',
            padding: '1.25rem',
            borderRadius: '16px',
            color: '#fff',
            boxShadow: '0 4px 16px rgba(79, 70, 229, 0.25)',
          }}
        >
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <span style={{ fontSize: '0.75rem', fontWeight: 600, opacity: 0.9 }}>
              Faculty Roster Attendance
            </span>
            <span
              style={{
                fontSize: '0.68rem',
                padding: '2px 8px',
                borderRadius: '8px',
                background: 'rgba(255, 255, 255, 0.2)',
                fontWeight: 700,
              }}
            >
              {sessionDate}
            </span>
          </div>

          <div style={{ marginTop: '10px' }}>
            <label style={{ fontSize: '0.7rem', opacity: 0.8, display: 'block', marginBottom: '4px' }}>
              Select Teaching Course & Cohort:
            </label>
            <select
              value={selectedCourse}
              onChange={(e) => {
                setSelectedCourse(e.target.value);
                setIsSubmitted(false);
              }}
              style={{
                width: '100%',
                padding: '8px 10px',
                borderRadius: '10px',
                border: '1px solid rgba(255, 255, 255, 0.25)',
                background: 'rgba(15, 23, 42, 0.7)',
                color: '#fff',
                fontSize: '0.82rem',
                fontWeight: 600,
                outline: 'none',
              }}
            >
              {facultyCourses.map((c) => (
                <option key={c.id} value={c.id} style={{ background: '#1e1b4b' }}>
                  {c.name}
                </option>
              ))}
            </select>
          </div>

          {/* Quick Metrics Bar */}
          <div
            style={{
              display: 'flex',
              justifyContent: 'space-between',
              alignItems: 'center',
              marginTop: '12px',
              paddingTop: '10px',
              borderTop: '1px solid rgba(255, 255, 255, 0.15)',
              fontSize: '0.78rem',
            }}
          >
            <span>
              <strong style={{ color: '#4ade80' }}>{presentCount}</strong> Present
            </span>
            <span>
              <strong style={{ color: '#fb7185' }}>{absentCount}</strong> Absent
            </span>
            <span>
              <strong style={{ color: '#fde047' }}>{lateCount}</strong> Late
            </span>
            <button
              onClick={markAllPresent}
              style={{
                background: 'rgba(255, 255, 255, 0.2)',
                border: 'none',
                color: '#fff',
                padding: '3px 8px',
                borderRadius: '6px',
                fontSize: '0.68rem',
                fontWeight: 700,
                cursor: 'pointer',
              }}
            >
              Mark All P ✓
            </button>
          </div>
        </div>

        {/* Success Confirmation Toast */}
        {isSubmitted && (
          <div
            style={{
              background: 'rgba(16, 185, 129, 0.2)',
              border: '1px solid rgba(16, 185, 129, 0.4)',
              color: '#34d399',
              padding: '10px 12px',
              borderRadius: '12px',
              fontSize: '0.78rem',
              display: 'flex',
              alignItems: 'center',
              gap: '8px',
              animation: 'fadeIn 0.3s ease',
            }}
          >
            <span style={{ fontSize: '1rem' }}>✅</span>
            <div>
              <strong>Roster Submitted Successfully!</strong>
              <div style={{ fontSize: '0.7rem', opacity: 0.9 }}>
                {presentCount} Present, {absentCount} Absent recorded for {selectedCourse}.
              </div>
            </div>
          </div>
        )}

        {/* Student Roster Cards */}
        <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
          <div style={{ fontSize: '0.85rem', fontWeight: 700, color: '#f8fafc' }}>
            Class Roster ({roster.length} Students)
          </div>

          {roster.map((student) => (
            <div
              key={student.id}
              className="glass-panel"
              style={{
                padding: '10px 12px',
                display: 'flex',
                justifyContent: 'space-between',
                alignItems: 'center',
                borderRadius: '12px',
              }}
            >
              <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                <div
                  style={{
                    width: '32px',
                    height: '32px',
                    borderRadius: '8px',
                    background: student.avatarColor,
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    fontWeight: 800,
                    color: '#fff',
                    fontSize: '0.8rem',
                  }}
                >
                  {student.name.charAt(0)}
                </div>
                <div>
                  <div style={{ fontSize: '0.82rem', fontWeight: 700, color: '#f8fafc' }}>
                    {student.name}
                  </div>
                  <div style={{ fontSize: '0.68rem', color: '#94a3b8' }}>
                    {student.rollNo}
                  </div>
                </div>
              </div>

              {/* Status Selector Buttons */}
              <div style={{ display: 'flex', gap: '4px' }}>
                <button
                  onClick={() => updateStudentStatus(student.id, 'present')}
                  style={{
                    width: '28px',
                    height: '28px',
                    borderRadius: '8px',
                    border: 'none',
                    fontWeight: 800,
                    fontSize: '0.72rem',
                    cursor: 'pointer',
                    background:
                      student.status === 'present'
                        ? '#10b981'
                        : 'rgba(255, 255, 255, 0.08)',
                    color: student.status === 'present' ? '#fff' : '#64748b',
                    transition: 'all 0.15s ease',
                  }}
                  title="Present"
                >
                  P
                </button>
                <button
                  onClick={() => updateStudentStatus(student.id, 'late')}
                  style={{
                    width: '28px',
                    height: '28px',
                    borderRadius: '8px',
                    border: 'none',
                    fontWeight: 800,
                    fontSize: '0.72rem',
                    cursor: 'pointer',
                    background:
                      student.status === 'late'
                        ? '#f59e0b'
                        : 'rgba(255, 255, 255, 0.08)',
                    color: student.status === 'late' ? '#fff' : '#64748b',
                    transition: 'all 0.15s ease',
                  }}
                  title="Late"
                >
                  L
                </button>
                <button
                  onClick={() => updateStudentStatus(student.id, 'absent')}
                  style={{
                    width: '28px',
                    height: '28px',
                    borderRadius: '8px',
                    border: 'none',
                    fontWeight: 800,
                    fontSize: '0.72rem',
                    cursor: 'pointer',
                    background:
                      student.status === 'absent'
                        ? '#ef4444'
                        : 'rgba(255, 255, 255, 0.08)',
                    color: student.status === 'absent' ? '#fff' : '#64748b',
                    transition: 'all 0.15s ease',
                  }}
                  title="Absent"
                >
                  A
                </button>
              </div>
            </div>
          ))}
        </div>

        {/* Submit Button */}
        <button
          onClick={handleSubmitRoster}
          className="btn btn-primary"
          style={{
            width: '100%',
            padding: '10px',
            fontSize: '0.85rem',
            fontWeight: 700,
            marginTop: '6px',
            background: 'linear-gradient(135deg, #4f46e5, #6366f1)',
          }}
        >
          {isSubmitted ? '✓ Re-Submit Attendance' : '📤 Save & Submit Roster'}
        </button>
      </div>
    );
  }

  // --- STUDENT VIEW (Default) ---
  return (
    <div style={{ padding: '1.25rem' }}>
      <div
        style={{
          background: 'linear-gradient(135deg, #1e40af, #0284c7)',
          padding: '1.5rem',
          borderRadius: '16px',
          color: '#fff',
          marginBottom: '1.25rem',
          boxShadow: '0 4px 16px rgba(2, 132, 199, 0.25)',
        }}
      >
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <span style={{ fontSize: '0.8rem', fontWeight: 600, opacity: 0.9 }}>Overall Attendance</span>
          <span
            style={{
              fontSize: '0.7rem',
              padding: '2px 8px',
              borderRadius: '10px',
              backgroundColor: 'rgba(255,255,255,0.2)',
              fontWeight: 700,
            }}
          >
            Safe (≥75%)
          </span>
        </div>
        <div style={{ fontSize: '2rem', fontWeight: 800, marginTop: '6px' }}>{overallPct}%</div>
        <div style={{ fontSize: '0.8rem', opacity: 0.85, marginTop: '2px' }}>
          {totalAttended} of {totalHours} Academic Hours Attended
        </div>
      </div>

      <h3 style={{ fontSize: '1.05rem', fontWeight: 700, color: '#f8fafc', marginBottom: '0.75rem' }}>
        Subject Breakdown
      </h3>

      <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
        {studentRecords.map((r, idx) => {
          const pct = ((r.attended / r.total) * 100).toFixed(1);
          const isSafe = parseFloat(pct) >= 75;

          return (
            <div key={idx} className="glass-panel" style={{ padding: '1rem' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                <span
                  style={{
                    fontSize: '0.75rem',
                    fontWeight: 700,
                    color: '#38bdf8',
                    padding: '2px 6px',
                    borderRadius: '6px',
                    backgroundColor: 'rgba(56, 189, 248, 0.15)',
                  }}
                >
                  {r.code}
                </span>
                <span
                  style={{
                    fontSize: '0.9rem',
                    fontWeight: 800,
                    color: isSafe ? '#10b981' : '#ef4444',
                  }}
                >
                  {pct}%
                </span>
              </div>
              <div style={{ fontSize: '0.95rem', fontWeight: 700, color: '#f8fafc', marginTop: '6px' }}>
                {r.name}
              </div>
              <div style={{ fontSize: '0.75rem', color: '#94a3b8', marginTop: '2px' }}>
                {r.instructor} • {r.attended}/{r.total} Hours
              </div>
              <div
                style={{
                  height: '6px',
                  width: '100%',
                  backgroundColor: 'rgba(15, 23, 42, 0.8)',
                  borderRadius: '3px',
                  marginTop: '8px',
                  overflow: 'hidden',
                }}
              >
                <div
                  style={{
                    height: '100%',
                    width: `${pct}%`,
                    backgroundColor: isSafe ? '#10b981' : '#ef4444',
                    borderRadius: '3px',
                  }}
                />
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
};
