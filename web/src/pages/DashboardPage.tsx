import React, { useState } from 'react';
import { User } from '../types/auth';
import { mockSchedule, mockCourses, mockAnnouncements } from '../services/mockData';

interface DashboardPageProps {
  user: User;
  onNavigate: (view: string) => void;
}

export const DashboardPage: React.FC<DashboardPageProps> = ({ user, onNavigate }) => {
  const [notification, setNotification] = useState<string | null>(null);

  const showNotification = (text: string) => {
    setNotification(text);
    setTimeout(() => setNotification(null), 3000);
  };

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
        background: 'linear-gradient(135deg, #1e3a8a 0%, #2563eb 50%, #0ea5e9 100%)',
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
              {user.role} Portal
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

        <div style={{ display: 'flex', gap: '10px' }}>
          <button
            onClick={() => onNavigate('courses')}
            className="btn"
            style={{
              backgroundColor: '#ffffff',
              color: '#1e3a8a',
              fontWeight: 700,
              boxShadow: '0 4px 12px rgba(0, 0, 0, 0.15)',
            }}
          >
            📚 My Courses
          </button>
          <button
            onClick={() => onNavigate('profile')}
            className="btn"
            style={{
              backgroundColor: 'rgba(255, 255, 255, 0.15)',
              color: '#ffffff',
              border: '1px solid rgba(255, 255, 255, 0.3)',
            }}
          >
            👤 Profile
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
        {[
          {
            title: 'Cumulative GPA',
            value: user.gpa.toFixed(2),
            sub: 'Top 5% of Department',
            icon: '🎯',
            color: '#2563eb',
          },
          {
            title: 'Class Attendance',
            value: `${user.attendanceRate.toFixed(1)}%`,
            sub: 'Excellent standing',
            icon: '✅',
            color: '#10b981',
          },
          {
            title: 'Credits Completed',
            value: `${user.creditsEarned || 88} / ${user.totalCredits || 120}`,
            sub: 'On Track for Graduation',
            icon: '🎓',
            color: '#0ea5e9',
          },
          {
            title: 'Enrolled Courses',
            value: `${mockCourses.length}`,
            sub: 'Fall Semester 2026',
            icon: '📖',
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
        {[
          { title: 'Courses', desc: '5 Enrolled', icon: '📚', action: () => onNavigate('courses') },
          { title: 'Timetable', desc: 'Weekly Classes', icon: '📅', action: () => onNavigate('schedule') },
          { title: 'Exams & Grades', desc: 'Fall 2026 Transcripts', icon: '📊', action: () => showNotification('Opening official grades & transcript portal...') },
          { title: 'Tuition & Fees', desc: '$0.00 Balance', icon: '💳', action: () => showNotification('Fee statement: 100% paid for current semester.') },
          { title: 'Digital Library', desc: '40K+ Journals', icon: '🏛️', action: () => showNotification('Connected to University IEEE & ACM library credentials.') },
          { title: 'Campus AI Copilot', desc: 'Virtual Assistant', icon: '🤖', action: () => showNotification('UniSphere AI Concierge is active!') },
        ].map((mod, idx) => (
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

          <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
            {mockSchedule.slice(0, 3).map((item) => (
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
                  <div style={{ fontSize: '0.85rem', color: '#94a3b8', marginTop: '2px' }}>
                    {item.title}
                  </div>
                  <div style={{ fontSize: '0.75rem', color: '#64748b', marginTop: '4px' }}>
                    ⏰ {item.time} • 📍 {item.room} • 👨‍🏫 {item.instructor}
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Campus Announcements */}
        <div className="glass-panel" style={{ padding: '1.5rem' }}>
          <h3 style={{ fontSize: '1.15rem', fontWeight: 700, color: '#f8fafc', marginBottom: '1.25rem' }}>
            📢 Official Campus Notices
          </h3>

          <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
            {mockAnnouncements.map((ann) => (
              <div
                key={ann.id}
                style={{
                  padding: '12px 14px',
                  borderRadius: '12px',
                  backgroundColor: 'rgba(15, 23, 42, 0.6)',
                  border: '1px solid var(--color-border)',
                }}
              >
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                  <span style={{
                    fontSize: '0.7rem',
                    fontWeight: 700,
                    padding: '2px 8px',
                    borderRadius: '10px',
                    backgroundColor: 'rgba(99, 102, 241, 0.2)',
                    color: '#a5b4fc',
                  }}>
                    {ann.category}
                  </span>
                  <span style={{ fontSize: '0.75rem', color: '#64748b' }}>{ann.date}</span>
                </div>
                <div style={{ fontWeight: 600, fontSize: '0.9rem', color: '#f8fafc', marginTop: '6px' }}>
                  {ann.title}
                </div>
                <div style={{ fontSize: '0.8rem', color: '#94a3b8', marginTop: '4px' }}>
                  {ann.content}
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};
