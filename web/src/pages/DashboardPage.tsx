import React, { useState, useEffect } from 'react';
import { User, ScheduleItem, Announcement } from '../types/auth';
import { getStoredSchedule } from '../services/scheduleStore';
import { getStoredAnnouncements } from '../services/announcementStore';
import { FacultyTimetableModal } from '../components/FacultyTimetableModal';
import { PostAnnouncementModal } from '../components/PostAnnouncementModal';

interface DashboardPageProps {
  user: User;
  onNavigate: (view: string) => void;
}

export const DashboardPage: React.FC<DashboardPageProps> = ({ user, onNavigate }) => {
  const [notification, setNotification] = useState<string | null>(null);
  const [schedule, setSchedule] = useState<ScheduleItem[]>(() => getStoredSchedule());
  const [announcements, setAnnouncements] = useState<Announcement[]>(() => getStoredAnnouncements());
  const [modalOpen, setModalOpen] = useState(false);
  const [editingItem, setEditingItem] = useState<ScheduleItem | null>(null);
  const [postAnnModalOpen, setPostAnnModalOpen] = useState(false);

  const isFaculty = user.role === 'faculty';

  const reloadSchedule = () => {
    setSchedule(getStoredSchedule());
  };

  const reloadAnnouncements = () => {
    setAnnouncements(getStoredAnnouncements());
  };

  useEffect(() => {
    const handleSchedUpdated = () => reloadSchedule();
    const handleAnnUpdated = () => reloadAnnouncements();

    window.addEventListener('unisphere_schedule_updated', handleSchedUpdated);
    window.addEventListener('unisphere_announcements_updated', handleAnnUpdated);

    return () => {
      window.removeEventListener('unisphere_schedule_updated', handleSchedUpdated);
      window.removeEventListener('unisphere_announcements_updated', handleAnnUpdated);
    };
  }, []);

  const showNotification = (text: string) => {
    setNotification(text);
    setTimeout(() => setNotification(null), 3000);
  };

  const handleOpenAddLecture = () => {
    setEditingItem(null);
    setModalOpen(true);
  };

  const handleOpenEditLecture = (item: ScheduleItem) => {
    setEditingItem(item);
    setModalOpen(true);
  };

  const visibleAnnouncements = announcements.filter(
    (a) => isFaculty || a.targetRole !== 'faculty'
  );

  return (
    <div style={{ maxWidth: '1200px', margin: '0 auto', padding: '2rem 1.5rem', width: '100%' }}>
      {/* Dynamic Toast Notification */}
      {notification && (
        <div style={{
          position: 'fixed',
          bottom: '24px',
          right: '24px',
          padding: '12px 20px',
          backgroundColor: '#1e40af',
          color: '#ffffff',
          borderRadius: '12px',
          boxShadow: 'var(--shadow-lg)',
          zIndex: 1000,
          fontWeight: 600,
          fontSize: '0.9rem',
          display: 'flex',
          alignItems: 'center',
          gap: '8px',
          border: '1px solid rgba(255, 255, 255, 0.2)',
        }}>
          <span>✨</span>
          <span>{notification}</span>
        </div>
      )}

      {/* Hero Welcome Banner */}
      <div style={{
        background: isFaculty
          ? 'linear-gradient(135deg, #1e1b4b 0%, #4338ca 50%, #6366f1 100%)'
          : 'linear-gradient(135deg, #1e3a8a 0%, #2563eb 50%, #0ea5e9 100%)',
        borderRadius: 'var(--radius-lg)',
        padding: '2.25rem',
        boxShadow: 'var(--shadow-md)',
        marginBottom: '2rem',
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center',
        flexWrap: 'wrap',
        gap: '1.5rem',
        position: 'relative',
        overflow: 'hidden',
      }}>
        <div>
          <div style={{ display: 'flex', alignItems: 'center', gap: '10px', marginBottom: '8px' }}>
            <span style={{
              padding: '4px 12px',
              borderRadius: '20px',
              backgroundColor: 'rgba(255, 255, 255, 0.2)',
              color: '#ffffff',
              fontSize: '0.75rem',
              fontWeight: 700,
              textTransform: 'uppercase',
              letterSpacing: '0.5px',
            }}>
              {isFaculty ? 'Faculty & Academic Staff Portal' : 'Student Portal'}
            </span>
            <span style={{ color: 'rgba(255, 255, 255, 0.8)', fontSize: '0.85rem' }}>
              ID: {user.studentId}
            </span>
          </div>

          <h1 style={{ fontSize: '2.2rem', fontWeight: 800, color: '#ffffff', letterSpacing: '-0.5px' }}>
            Welcome back, {user.name}!
          </h1>
          <p style={{ color: 'rgba(255, 255, 255, 0.85)', fontSize: '1rem', marginTop: '4px' }}>
            {user.department} • {user.enrolledYear || 'Academic Year 2026'}
          </p>
        </div>

        <div style={{ display: 'flex', gap: '10px', flexWrap: 'wrap' }}>
          {isFaculty ? (
            <>
              <button
                onClick={handleOpenAddLecture}
                className="btn btn-primary"
                style={{
                  backgroundColor: '#ffffff',
                  color: '#4338ca',
                  fontWeight: 700,
                  boxShadow: '0 4px 12px rgba(0, 0, 0, 0.15)',
                }}
              >
                ➕ Add / Change Timetable
              </button>
              <button
                onClick={() => setPostAnnModalOpen(true)}
                className="btn"
                style={{
                  backgroundColor: 'rgba(255, 255, 255, 0.2)',
                  color: '#ffffff',
                  fontWeight: 700,
                  border: '1px solid rgba(255, 255, 255, 0.3)',
                }}
              >
                📢 Post Notice
              </button>
            </>
          ) : (
            <button
              onClick={() => onNavigate('placements')}
              className="btn btn-primary"
              style={{
                backgroundColor: '#ffffff',
                color: '#065f46',
                fontWeight: 700,
                boxShadow: '0 4px 12px rgba(0, 0, 0, 0.15)',
              }}
            >
              💼 Placements (48 Drives)
            </button>
          )}

          <button
            onClick={() => onNavigate('courses')}
            className="btn"
            style={{
              backgroundColor: 'rgba(255, 255, 255, 0.2)',
              color: '#ffffff',
              fontWeight: 700,
              border: '1px solid rgba(255, 255, 255, 0.3)',
            }}
          >
            📚 {isFaculty ? 'Teaching Courses' : 'My Courses'}
          </button>

          <button
            id="home-dashboard-profile-btn"
            onClick={() => onNavigate('profile')}
            className="btn"
            style={{
              backgroundColor: 'rgba(255, 255, 255, 0.25)',
              color: '#ffffff',
              fontWeight: 700,
              border: '1px solid rgba(255, 255, 255, 0.4)',
              cursor: 'pointer',
            }}
          >
            👤 Open Profile
          </button>
        </div>
      </div>

      {/* 4 Academic KPI Stat Cards */}
      <div style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(auto-fit, minmax(240px, 1fr))',
        gap: '1.25rem',
        marginBottom: '2.5rem',
      }}>
        {isFaculty ? [
          {
            title: 'Assigned Courses',
            value: '3 Courses',
            sub: 'Fall Semester 2026',
            icon: '📖',
            color: '#6366f1',
          },
          {
            title: 'Enrolled Students',
            value: '142 Students',
            sub: 'CS, AI & Data Science',
            icon: '🎓',
            color: '#0ea5e9',
          },
          {
            title: 'Weekly Teaching Hours',
            value: '14 Hours / Wk',
            sub: 'On Schedule',
            icon: '⏰',
            color: '#10b981',
          },
          {
            title: 'Campus Bulletins',
            value: `${announcements.length} Notices`,
            sub: 'Published Active',
            icon: '📢',
            color: '#8b5cf6',
          },
        ].map((stat, idx) => (
          <div key={idx} className="glass-panel" style={{ padding: '1.5rem', position: 'relative' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
              <span style={{ fontSize: '0.85rem', fontWeight: 600, color: 'var(--color-text-secondary)' }}>
                {stat.title}
              </span>
              <span style={{ fontSize: '1.4rem' }}>{stat.icon}</span>
            </div>
            <div style={{ fontSize: '1.85rem', fontWeight: 800, color: '#f8fafc', marginTop: '10px', letterSpacing: '-0.5px' }}>
              {stat.value}
            </div>
            <div style={{ fontSize: '0.78rem', color: stat.color, marginTop: '4px', fontWeight: 600 }}>
              {stat.sub}
            </div>
          </div>
        )) : [
          {
            title: 'Cumulative GPA',
            value: user.gpa.toFixed(2),
            sub: 'Rank #4 in Department',
            icon: '🎯',
            color: '#2563eb',
          },
          {
            title: 'Placement Standing',
            value: 'Super Dream',
            sub: 'Eligible for ≥ ₹20 LPA Tier-1',
            icon: '💼',
            color: '#10b981',
          },
          {
            title: 'Class Attendance',
            value: `${user.attendanceRate.toFixed(1)}%`,
            sub: 'Safe Standing (≥75%)',
            icon: '✅',
            color: '#0ea5e9',
          },
          {
            title: 'Active Bulletins',
            value: `${visibleAnnouncements.length} Notices`,
            sub: 'Exams, Placements, Events',
            icon: '📢',
            color: '#6366f1',
          },
        ].map((stat, idx) => (
          <div key={idx} className="glass-panel" style={{ padding: '1.5rem', position: 'relative' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
              <span style={{ fontSize: '0.85rem', fontWeight: 600, color: 'var(--color-text-secondary)' }}>
                {stat.title}
              </span>
              <span style={{ fontSize: '1.4rem' }}>{stat.icon}</span>
            </div>
            <div style={{ fontSize: '1.85rem', fontWeight: 800, color: '#f8fafc', marginTop: '10px', letterSpacing: '-0.5px' }}>
              {stat.value}
            </div>
            <div style={{ fontSize: '0.78rem', color: stat.color, marginTop: '4px', fontWeight: 600 }}>
              {stat.sub}
            </div>
          </div>
        ))}
      </div>

      {/* FACULTY SPECIFIC: Timetable Management Section */}
      {isFaculty && (
        <div className="glass-panel" style={{ padding: '1.75rem', marginBottom: '2.5rem', border: '1.5px solid rgba(99, 102, 241, 0.4)' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1rem', flexWrap: 'wrap', gap: '1rem' }}>
            <div>
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                <span style={{ fontSize: '1.5rem' }}>🗓️</span>
                <h2 style={{ fontSize: '1.35rem', fontWeight: 800, color: '#f8fafc' }}>
                  Faculty Timetable Management
                </h2>
              </div>
              <p style={{ fontSize: '0.85rem', color: '#94a3b8', marginTop: '4px' }}>
                Reschedule lecture timings, reassign lecture halls, or add extra classroom sessions.
              </p>
            </div>
            <button
              onClick={handleOpenAddLecture}
              className="btn btn-primary"
              style={{ display: 'flex', alignItems: 'center', gap: '8px' }}
            >
              <span>➕</span>
              <span>Add Lecture Slot</span>
            </button>
          </div>

          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(320px, 1fr))', gap: '12px' }}>
            {schedule.slice(0, 6).map((item) => (
              <div
                key={item.id}
                style={{
                  backgroundColor: 'rgba(15, 23, 42, 0.75)',
                  border: '1px solid var(--color-border)',
                  borderLeft: `5px solid ${item.color}`,
                  borderRadius: '12px',
                  padding: '1rem',
                  display: 'flex',
                  justifyContent: 'space-between',
                  alignItems: 'center',
                }}
              >
                <div>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                    <span style={{ fontWeight: 800, color: '#38bdf8', fontSize: '0.85rem' }}>
                      {item.code}
                    </span>
                    <span style={{
                      fontSize: '0.7rem',
                      color: '#a5b4fc',
                      background: 'rgba(99, 102, 241, 0.15)',
                      padding: '2px 6px',
                      borderRadius: '4px',
                      fontWeight: 600,
                    }}>
                      {item.day}
                    </span>
                  </div>
                  <div style={{ fontSize: '0.92rem', fontWeight: 700, color: '#f8fafc', marginTop: '4px' }}>
                    {item.title}
                  </div>
                  <div style={{ fontSize: '0.78rem', color: '#94a3b8', marginTop: '4px' }}>
                    ⏰ {item.time} • 🏛️ {item.room}
                  </div>
                </div>

                <button
                  onClick={() => handleOpenEditLecture(item)}
                  className="btn btn-secondary"
                  style={{
                    padding: '6px 12px',
                    fontSize: '0.78rem',
                    whiteSpace: 'nowrap',
                  }}
                  title="Reschedule this slot"
                >
                  ✏️ Change
                </button>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Main Campus Services / Modules Grid */}
      <h2 style={{ fontSize: '1.3rem', fontWeight: 700, color: '#f8fafc', marginBottom: '1rem' }}>
        Campus Modules & Services
      </h2>
      <div style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(auto-fit, minmax(180px, 1fr))',
        gap: '1rem',
        marginBottom: '2.5rem',
      }}>
        {(isFaculty ? [
          { title: 'Teaching Classes', desc: '3 Active Courses', icon: '📚', action: () => onNavigate('courses') },
          { title: 'Manage Timetable', desc: 'Change & Reschedule', icon: '📅', action: () => onNavigate('schedule') },
          { title: 'Campus Bulletins', desc: 'Broadcast Notices', icon: '📢', action: () => onNavigate('announcements') },
          { title: 'My Profile & ID', desc: 'Account & Settings', icon: '👤', action: () => onNavigate('profile') },
          { title: 'Digital Library', desc: '40K+ Journals', icon: '🏛️', action: () => showNotification('Connected to University IEEE & ACM library credentials.') },
          { title: 'Campus AI Copilot', desc: 'Virtual Assistant', icon: '🤖', action: () => showNotification('UniSphere AI Concierge is ready to help!') },
        ] : [
          { title: 'Courses', desc: '5 Enrolled', icon: '📚', action: () => onNavigate('courses') },
          { title: 'Timetable', desc: 'Weekly Classes', icon: '📅', action: () => onNavigate('schedule') },
          { title: 'Placements Cell', desc: 'Google, NVIDIA Drives', icon: '💼', action: () => onNavigate('placements') },
          { title: 'Campus Bulletins', desc: 'Official Notices', icon: '📢', action: () => onNavigate('announcements') },
          { title: 'My Profile & ID', desc: 'Account & Credentials', icon: '👤', action: () => onNavigate('profile') },
          { title: 'Campus AI Copilot', desc: 'Virtual Assistant', icon: '🤖', action: () => showNotification('UniSphere AI Concierge is ready to help!') },
        ]).map((mod, idx) => (
          <div
            key={idx}
            onClick={mod.action}
            className="glass-panel"
            style={{
              padding: '1.25rem',
              cursor: 'pointer',
              transition: 'all 0.2s',
              textAlign: 'center',
            }}
            onMouseEnter={(e) => {
              e.currentTarget.style.transform = 'translateY(-3px)';
              e.currentTarget.style.borderColor = 'var(--color-secondary)';
            }}
            onMouseLeave={(e) => {
              e.currentTarget.style.transform = 'translateY(0)';
              e.currentTarget.style.borderColor = 'var(--color-border-subtle)';
            }}
          >
            <div style={{ fontSize: '2rem', marginBottom: '8px' }}>{mod.icon}</div>
            <div style={{ fontSize: '0.95rem', fontWeight: 700, color: '#f8fafc' }}>{mod.title}</div>
            <div style={{ fontSize: '0.78rem', color: '#94a3b8', marginTop: '2px' }}>{mod.desc}</div>
          </div>
        ))}
      </div>

      {/* Two Column Layout: Schedule and Announcements */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(320px, 1fr))', gap: '1.5rem' }}>
        {/* Today's Schedule Card */}
        <div className="glass-panel" style={{ padding: '1.5rem' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1.25rem' }}>
            <h3 style={{ fontSize: '1.15rem', fontWeight: 700, color: '#f8fafc' }}>
              🗓️ Today's Lectures
            </h3>
            <div style={{ display: 'flex', gap: '8px', alignItems: 'center' }}>
              {isFaculty && (
                <button
                  onClick={handleOpenAddLecture}
                  style={{
                    background: 'none',
                    border: 'none',
                    color: '#a5b4fc',
                    fontSize: '0.8rem',
                    fontWeight: 700,
                    cursor: 'pointer',
                  }}
                >
                  + Add Slot
                </button>
              )}
              <button
                onClick={() => onNavigate('schedule')}
                style={{
                  background: 'transparent',
                  border: 'none',
                  color: '#38bdf8',
                  fontSize: '0.85rem',
                  fontWeight: 600,
                  cursor: 'pointer',
                }}
              >
                View Full Week →
              </button>
            </div>
          </div>

          <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
            {schedule.slice(0, 3).map((item) => (
              <div
                key={item.id}
                style={{
                  display: 'flex',
                  alignItems: 'center',
                  padding: '12px 14px',
                  borderRadius: '12px',
                  backgroundColor: 'rgba(15, 23, 42, 0.6)',
                  border: '1px solid var(--color-border)',
                  borderLeft: `4px solid ${item.color}`,
                  justifyContent: 'space-between',
                }}
              >
                <div style={{ flex: 1 }}>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                    <span style={{ fontWeight: 700, fontSize: '0.92rem', color: '#f8fafc' }}>
                      {item.code}
                    </span>
                    <span style={{
                      fontSize: '0.7rem',
                      padding: '2px 8px',
                      borderRadius: '12px',
                      backgroundColor: item.status === 'Ongoing' ? 'rgba(16, 185, 129, 0.2)' : 'rgba(14, 165, 233, 0.15)',
                      color: item.status === 'Ongoing' ? '#34d399' : '#38bdf8',
                      fontWeight: 700,
                    }}>
                      {item.status}
                    </span>
                  </div>
                  <div style={{ fontSize: '0.875rem', color: '#cbd5e1', marginTop: '2px' }}>
                    {item.title}
                  </div>
                  <div style={{ fontSize: '0.75rem', color: '#94a3b8', marginTop: '2px' }}>
                    📍 {item.room} • ⏰ {item.time}
                  </div>
                </div>

                {isFaculty && (
                  <button
                    onClick={() => handleOpenEditLecture(item)}
                    className="btn btn-secondary"
                    style={{ padding: '4px 10px', fontSize: '0.75rem', marginLeft: '10px' }}
                    title="Reschedule lecture"
                  >
                    ✏️
                  </button>
                )}
              </div>
            ))}
          </div>
        </div>

        {/* Official Announcements Card (with View All and Post Actions!) */}
        <div className="glass-panel" style={{ padding: '1.5rem' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1.25rem', flexWrap: 'wrap', gap: '8px' }}>
            <h3 style={{ fontSize: '1.15rem', fontWeight: 700, color: '#f8fafc' }}>
              📢 Campus Bulletins
            </h3>
            <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
              {isFaculty && (
                <button
                  onClick={() => setPostAnnModalOpen(true)}
                  style={{
                    background: 'none',
                    border: 'none',
                    color: '#a5b4fc',
                    fontSize: '0.8rem',
                    fontWeight: 700,
                    cursor: 'pointer',
                  }}
                >
                  + Post Notice
                </button>
              )}
              <button
                onClick={() => onNavigate('announcements')}
                style={{
                  background: 'none',
                  border: 'none',
                  color: '#38bdf8',
                  fontSize: '0.825rem',
                  fontWeight: 700,
                  cursor: 'pointer',
                }}
              >
                View All ({visibleAnnouncements.length}) →
              </button>
            </div>
          </div>

          <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
            {visibleAnnouncements.slice(0, 3).map((ann) => (
              <div
                key={ann.id}
                onClick={() => onNavigate('announcements')}
                style={{
                  padding: '12px',
                  borderRadius: '12px',
                  backgroundColor: 'rgba(15, 23, 42, 0.4)',
                  border: '1px solid var(--color-border-subtle)',
                  cursor: 'pointer',
                  transition: 'border-color 0.15s',
                }}
                onMouseEnter={(e) => (e.currentTarget.style.borderColor = 'rgba(56, 189, 248, 0.4)')}
                onMouseLeave={(e) => (e.currentTarget.style.borderColor = 'var(--color-border-subtle)')}
              >
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '4px' }}>
                  <span style={{
                    fontSize: '0.7rem',
                    fontWeight: 700,
                    color: ann.category === 'Placement' ? '#34d399' : ann.category === 'Exam' ? '#fbbf24' : '#38bdf8',
                    textTransform: 'uppercase',
                  }}>
                    {ann.category}
                  </span>
                  <span style={{ fontSize: '0.72rem', color: '#64748b' }}>
                    {ann.date}
                  </span>
                </div>
                <div style={{ fontSize: '0.875rem', fontWeight: 600, color: '#f8fafc' }}>
                  {ann.title}
                </div>
                <div style={{ fontSize: '0.78rem', color: '#94a3b8', marginTop: '3px', lineHeight: 1.4 }}>
                  {ann.content.length > 95 ? `${ann.content.substring(0, 95)}...` : ann.content}
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* Faculty Timetable Edit/Add Modal */}
      {isFaculty && (
        <FacultyTimetableModal
          isOpen={modalOpen}
          onClose={() => setModalOpen(false)}
          onScheduleUpdated={reloadSchedule}
          initialItem={editingItem}
          instructorName={user.name}
        />
      )}

      {/* Faculty Announcement Post Modal */}
      {isFaculty && (
        <PostAnnouncementModal
          isOpen={postAnnModalOpen}
          onClose={() => setPostAnnModalOpen(false)}
          onAnnouncementCreated={reloadAnnouncements}
          authorName={user.name}
        />
      )}
    </div>
  );
};
