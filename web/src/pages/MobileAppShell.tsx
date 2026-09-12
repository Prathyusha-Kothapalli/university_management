import React, { useState, useEffect } from 'react';
import { User, ScheduleItem, Announcement } from '../types/auth';
import { AttendanceView } from './AttendanceView';
import { AssignmentsView } from './AssignmentsView';
import { ExamsView } from './ExamsView';
import { PlacementsView } from './PlacementsView';
import { AiAssistantView } from './AiAssistantView';
import { AnnouncementsView } from './AnnouncementsView';
import { NotificationsView } from './NotificationsView';
import { getStoredSchedule } from '../services/scheduleStore';
import { getStoredAnnouncements } from '../services/announcementStore';
import { getStoredNotifications, CampusNotification } from '../services/notificationStore';
import { FacultyTimetableModal } from '../components/FacultyTimetableModal';
import { MobileAuthView } from './MobileAuthView';

interface MobileAppShellProps {
  user: User | null;
  onLogin?: (user: User) => void;
  onLogout: () => void;
  onSwitchRole: () => void;
  initialTab?: string;
  onNavigate?: (view: string) => void;
  isFullscreen?: boolean;
  onToggleFullscreen?: () => void;
}

export const MobileAppShell: React.FC<MobileAppShellProps> = ({
  user,
  onLogin,
  onLogout,
  onSwitchRole,
  initialTab = 'home',
  onNavigate,
  isFullscreen = false,
  onToggleFullscreen,
}) => {
  const [activeTab, setActiveTab] = useState<'home' | 'schedule' | 'ai' | 'profile'>('home');
  const [subView, setSubView] = useState<'none' | 'attendance' | 'assignments' | 'exams' | 'placements' | 'announcements' | 'notifications'>('none');
  const [selectedDay, setSelectedDay] = useState('Monday');
  const [isOfflineMode, setIsOfflineMode] = useState(false);
  const [schedule, setSchedule] = useState<ScheduleItem[]>(() => getStoredSchedule());
  const [announcements, setAnnouncements] = useState<Announcement[]>(() => getStoredAnnouncements());
  const [notifications, setNotifications] = useState<CampusNotification[]>(() => getStoredNotifications());

  // Faculty modal state
  const [modalOpen, setModalOpen] = useState(false);
  const [editingItem, setEditingItem] = useState<ScheduleItem | null>(null);

  const isFaculty = user?.role === 'faculty';

  const reloadSchedule = () => {
    setSchedule(getStoredSchedule());
  };

  const reloadAnnouncements = () => {
    setAnnouncements(getStoredAnnouncements());
  };

  useEffect(() => {
    const handleSchedUpdated = () => reloadSchedule();
    const handleAnnUpdated = () => reloadAnnouncements();
    const handleNotifUpdated = () => setNotifications(getStoredNotifications());

    window.addEventListener('unisphere_schedule_updated', handleSchedUpdated);
    window.addEventListener('unisphere_announcements_updated', handleAnnUpdated);
    window.addEventListener('unisphere_notifications_updated', handleNotifUpdated);

    return () => {
      window.removeEventListener('unisphere_schedule_updated', handleSchedUpdated);
      window.removeEventListener('unisphere_announcements_updated', handleAnnUpdated);
      window.removeEventListener('unisphere_notifications_updated', handleNotifUpdated);
    };
  }, []);

  // Sync when initialTab / currentView changes from parent navbar
  useEffect(() => {
    if (initialTab === 'placements') {
      setActiveTab('home');
      setSubView('placements');
    } else if (initialTab === 'announcements') {
      setActiveTab('home');
      setSubView('announcements');
    } else if (initialTab === 'notifications') {
      setActiveTab('home');
      setSubView('notifications');
    } else if (initialTab === 'profile') {
      setActiveTab('profile');
      setSubView('none');
    } else if (initialTab === 'schedule') {
      setActiveTab('schedule');
      setSubView('none');
    } else if (initialTab === 'dashboard') {
      setActiveTab('home');
      setSubView('none');
    }
  }, [initialTab]);

  const days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'];
  const daySchedule = schedule.filter((s) => s.day === selectedDay);

  const navigateToSub = (view: 'attendance' | 'assignments' | 'exams' | 'placements' | 'announcements' | 'notifications') => {
    setSubView(view);
    if (onNavigate) {
      if (view === 'placements') onNavigate('placements');
      else if (view === 'announcements') onNavigate('announcements');
      else if (view === 'notifications') onNavigate('notifications');
    }
  };

  const handleTabChange = (tab: 'home' | 'schedule' | 'ai' | 'profile') => {
    setActiveTab(tab);
    setSubView('none');
    if (onNavigate) {
      if (tab === 'home') onNavigate('dashboard');
      else if (tab === 'schedule') onNavigate('schedule');
      else if (tab === 'profile') onNavigate('profile');
    }
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
    <div className={`phone-wrapper ${isFullscreen ? 'fullscreen' : ''}`}>
      <div className={`phone-shell ${isFullscreen ? 'fullscreen' : ''}`}>
        {/* Phone Top Notch Bar & Status Bar */}
        <div className="phone-notch-bar">
          <span>9:41</span>
          <div className="phone-island">
            <div className="phone-island-cam" />
          </div>
          <div style={{ display: 'flex', alignItems: 'center', gap: '6px', fontSize: '0.7rem' }}>
            <span>5G</span>
            <span>📶</span>
            <span>{isOfflineMode ? '📴' : '🔋 98%'}</span>
          </div>
        </div>

        {/* In-Phone Header */}
        <div style={{
          padding: '10px 16px',
          background: 'rgba(15, 23, 42, 0.85)',
          backdropFilter: 'blur(12px)',
          borderBottom: '1px solid rgba(255, 255, 255, 0.06)',
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          zIndex: 30,
        }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
            {subView !== 'none' ? (
              <button
                onClick={() => setSubView('none')}
                style={{
                  background: 'none',
                  border: 'none',
                  color: '#38bdf8',
                  fontSize: '1.1rem',
                  fontWeight: 800,
                  cursor: 'pointer',
                  padding: '2px 6px',
                }}
              >
                ←
              </button>
            ) : (
              <div
                onClick={() => handleTabChange('home')}
                style={{
                  width: '30px',
                  height: '30px',
                  borderRadius: '8px',
                  background: 'linear-gradient(135deg, #2563eb, #0ea5e9)',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  fontWeight: 900,
                  color: '#fff',
                  fontSize: '0.9rem',
                  cursor: 'pointer',
                }}
              >
                U
              </div>
            )}
            <div>
              <div style={{ fontSize: '0.85rem', fontWeight: 800, color: '#f8fafc', letterSpacing: '-0.3px' }}>
                {subView === 'attendance'
                  ? (isFaculty ? 'Faculty Attendance Roster' : 'Attendance Tracker')
                  : subView === 'assignments'
                  ? (isFaculty ? 'Faculty Grading Hub' : 'Active Assignments')
                  : subView === 'exams'
                  ? 'Exams & Results'
                  : subView === 'placements'
                  ? 'Campus Placements'
                  : subView === 'announcements'
                  ? 'Announcements'
                  : subView === 'notifications'
                  ? 'Notifications Center'
                  : activeTab === 'schedule'
                  ? (isFaculty ? 'Faculty Timetable' : 'Lecture Timetable')
                  : activeTab === 'ai'
                  ? 'UniSphere AI'
                  : activeTab === 'profile'
                  ? 'My Account'
                  : (isFaculty ? 'Faculty Mobile Hub' : 'UniSphere Mobile')}
              </div>
              <div style={{ fontSize: '0.65rem', color: isOfflineMode ? '#f59e0b' : '#10b981' }}>
                {isOfflineMode ? '● Offline Mode Active' : '● Connected to Python API'}
              </div>
            </div>
          </div>

          {/* Quick status badges, Notification Bell, and CLICKABLE PROFILE AVATAR */}
          <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
            {/* Notification Bell with Badge */}
            <div
              onClick={() => navigateToSub('notifications')}
              title="Campus Notifications Center"
              style={{
                position: 'relative',
                cursor: 'pointer',
                padding: '4px 6px',
                borderRadius: '8px',
                background: subView === 'notifications' ? 'rgba(56, 189, 248, 0.25)' : 'rgba(255, 255, 255, 0.08)',
                border: subView === 'notifications' ? '1px solid rgba(56, 189, 248, 0.4)' : '1px solid rgba(255, 255, 255, 0.1)',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                fontSize: '0.82rem',
                transition: 'all 0.15s ease',
              }}
            >
              🔔
              {notifications.filter((n) => !n.read).length > 0 && (
                <span
                  style={{
                    position: 'absolute',
                    top: '-3px',
                    right: '-3px',
                    background: '#ef4444',
                    color: '#fff',
                    fontSize: '0.52rem',
                    fontWeight: 900,
                    padding: '1px 3px',
                    borderRadius: '8px',
                    minWidth: '13px',
                    textAlign: 'center',
                    lineHeight: '11px',
                    boxShadow: '0 2px 5px rgba(239, 68, 68, 0.5)',
                  }}
                >
                  {notifications.filter((n) => !n.read).length}
                </span>
              )}
            </div>
            {user && (
              <span
                onClick={onSwitchRole}
                title="Switch between Student and Faculty"
                style={{
                  fontSize: '0.65rem',
                  cursor: 'pointer',
                  padding: '3px 7px',
                  borderRadius: '8px',
                  background: isFaculty ? 'rgba(99, 102, 241, 0.2)' : 'rgba(14, 165, 233, 0.2)',
                  color: isFaculty ? '#c084fc' : '#38bdf8',
                  fontWeight: 700,
                  border: isFaculty ? '1px solid rgba(99, 102, 241, 0.35)' : '1px solid rgba(14, 165, 233, 0.35)',
                }}
              >
                {isFaculty ? 'Faculty 👨‍🏫' : 'Student 🎓'}
              </span>
            )}

            {onToggleFullscreen && (
              <span
                onClick={onToggleFullscreen}
                title="Toggle between phone frame and fullscreen mobile view"
                style={{
                  fontSize: '0.65rem',
                  cursor: 'pointer',
                  padding: '3px 7px',
                  borderRadius: '8px',
                  background: 'rgba(255, 255, 255, 0.08)',
                  color: '#cbd5e1',
                  fontWeight: 700,
                  border: '1px solid rgba(255, 255, 255, 0.15)',
                }}
              >
                {isFullscreen ? '📱 Frame' : '⛶ Full'}
              </span>
            )}

            <span
              onClick={() => setIsOfflineMode(!isOfflineMode)}
              title="Click to toggle simulated Offline Mode"
              style={{
                fontSize: '0.65rem',
                cursor: 'pointer',
                padding: '3px 7px',
                borderRadius: '8px',
                background: isOfflineMode ? 'rgba(245, 158, 11, 0.2)' : 'rgba(16, 185, 129, 0.15)',
                color: isOfflineMode ? '#f59e0b' : '#10b981',
                fontWeight: 700,
              }}
            >
              {isOfflineMode ? 'Offline' : 'Online'}
            </span>

            {/* Clickable Avatar to Open Profile */}
            {user && (
              <div
                onClick={() => handleTabChange('profile')}
                title="Tap to open your profile"
                style={{
                  width: '28px',
                  height: '28px',
                  borderRadius: '50%',
                  background: activeTab === 'profile'
                    ? 'linear-gradient(135deg, #38bdf8, #2563eb)'
                    : '#334155',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  fontSize: '0.78rem',
                  fontWeight: 700,
                  color: '#ffffff',
                  cursor: 'pointer',
                  boxShadow: activeTab === 'profile' ? '0 0 8px rgba(56, 189, 248, 0.5)' : 'none',
                  border: '1.5px solid rgba(255, 255, 255, 0.2)',
                }}
              >
                {user.name.charAt(0)}
              </div>
            )}
          </div>
        </div>

        {/* Phone Scrollable Screen Content */}
        <div className="phone-screen">
          {!user ? (
            <MobileAuthView onSuccess={(u) => onLogin && onLogin(u)} />
          ) : (
            <>
              {/* 1. If inside a SubView */}
              {subView === 'attendance' && <AttendanceView user={user} isFaculty={isFaculty} />}
              {subView === 'assignments' && <AssignmentsView user={user} isFaculty={isFaculty} />}
              {subView === 'exams' && <ExamsView />}
              {subView === 'placements' && <PlacementsView />}
              {subView === 'announcements' && <AnnouncementsView user={user} />}
              {subView === 'notifications' && <NotificationsView onNavigateSub={navigateToSub} />}

          {/* 2. If at Root of Active Tab */}
          {subView === 'none' && activeTab === 'home' && (
            <div style={{ padding: '1.25rem', display: 'flex', flexDirection: 'column', gap: '14px' }}>
              {/* Greeting Banner */}
              <div
                onClick={() => handleTabChange('profile')}
                title="Tap to view your complete profile"
                style={{
                  background: isFaculty
                    ? 'linear-gradient(135deg, #1e1b4b, #4338ca)'
                    : 'linear-gradient(135deg, #1e3a8a, #0369a1)',
                  padding: '1.25rem',
                  borderRadius: '16px',
                  color: '#fff',
                  boxShadow: '0 4px 16px rgba(3, 105, 161, 0.25)',
                  cursor: 'pointer',
                  transition: 'transform 0.15s',
                }}
              >
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
                  <div>
                    <div style={{ fontSize: '0.75rem', opacity: 0.85 }}>
                      {isFaculty ? 'Faculty Instructor 👋' : 'Welcome back 👋'}
                    </div>
                    <div style={{ fontSize: '1.2rem', fontWeight: 800, marginTop: '2px' }}>
                      {user?.name || 'Alex Rivera'}
                    </div>
                    <div style={{ fontSize: '0.72rem', opacity: 0.8, marginTop: '2px' }}>
                      {isFaculty ? 'Tenured Professor' : `Roll: ${user?.id || 'CS-2023-889'}`} • Dept of CS & AI
                    </div>
                  </div>
                  <span style={{
                    fontSize: '0.7rem',
                    background: 'rgba(255,255,255,0.2)',
                    padding: '3px 8px',
                    borderRadius: '8px',
                    fontWeight: 700,
                    display: 'flex',
                    alignItems: 'center',
                    gap: '4px',
                  }}>
                    👤 Profile ›
                  </span>
                </div>
              </div>

              {/* Announcements Alert Chip on Home */}
              <div
                onClick={() => navigateToSub('announcements')}
                style={{
                  backgroundColor: 'rgba(245, 158, 11, 0.12)',
                  border: '1px solid rgba(245, 158, 11, 0.3)',
                  borderRadius: '12px',
                  padding: '10px 12px',
                  display: 'flex',
                  justifyContent: 'space-between',
                  alignItems: 'center',
                  cursor: 'pointer',
                }}
              >
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                  <span style={{ fontSize: '1.1rem' }}>📢</span>
                  <div>
                    <div style={{ fontSize: '0.78rem', fontWeight: 700, color: '#fbbf24' }}>
                      {visibleAnnouncements.length} Campus Announcements
                    </div>
                    <div style={{ fontSize: '0.68rem', color: '#cbd5e1' }}>
                      {visibleAnnouncements[0]?.title.slice(0, 36)}...
                    </div>
                  </div>
                </div>
                <span style={{ fontSize: '0.75rem', color: '#fbbf24', fontWeight: 700 }}>View →</span>
              </div>

              {/* FACULTY FEATURE: Change Timetable Direct Quick Action */}
              {isFaculty && (
                <div
                  className="glass-panel"
                  style={{
                    padding: '1rem',
                    border: '1.5px solid rgba(99, 102, 241, 0.5)',
                    background: 'rgba(30, 27, 75, 0.6)',
                  }}
                >
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '8px' }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                      <span style={{ fontSize: '1.2rem' }}>🗓️</span>
                      <span style={{ fontSize: '0.9rem', fontWeight: 800, color: '#f8fafc' }}>
                        Change Timetable
                      </span>
                    </div>
                    <button
                      onClick={handleOpenAddLecture}
                      className="btn btn-primary"
                      style={{ padding: '4px 10px', fontSize: '0.75rem', borderRadius: '8px' }}
                    >
                      ➕ Add Slot
                    </button>
                  </div>
                  <p style={{ fontSize: '0.75rem', color: '#94a3b8', marginBottom: '8px' }}>
                    Faculty can reschedule hours or add extra teaching sessions.
                  </p>
                  <button
                    onClick={() => handleTabChange('schedule')}
                    className="btn btn-secondary"
                    style={{ width: '100%', padding: '6px', fontSize: '0.78rem' }}
                  >
                    Open Weekly Timetable Editor →
                  </button>
                </div>
              )}

              {/* Quick Actions Grid (Student & Faculty Modules) */}
              <div>
                <div style={{ fontSize: '0.825rem', fontWeight: 700, color: '#94a3b8', marginBottom: '8px', textTransform: 'uppercase', letterSpacing: '0.5px' }}>
                  {isFaculty ? 'Faculty Quick Access' : 'Student Campus Modules'}
                </div>
                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(2, 1fr)', gap: '10px' }}>
                  {/* PLACEMENTS IN STUDENT MODULE */}
                  {!isFaculty && (
                    <div
                      onClick={() => navigateToSub('placements')}
                      className="glass-panel"
                      style={{
                        padding: '0.9rem',
                        cursor: 'pointer',
                        transition: 'transform 0.15s',
                        border: '1px solid rgba(16, 185, 129, 0.35)',
                      }}
                    >
                      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                        <span style={{ fontSize: '1.4rem' }}>💼</span>
                        <span style={{ fontSize: '0.7rem', color: '#34d399', fontWeight: 800 }}>Tier-1</span>
                      </div>
                      <div style={{ fontSize: '0.85rem', fontWeight: 700, color: '#f8fafc', marginTop: '6px' }}>
                        Placements
                      </div>
                      <div style={{ fontSize: '0.68rem', color: '#94a3b8' }}>Google, NVIDIA, Apple</div>
                    </div>
                  )}

                  {/* ANNOUNCEMENTS IN BOTH STUDENT AND FACULTY */}
                  <div
                    onClick={() => navigateToSub('announcements')}
                    className="glass-panel"
                    style={{
                      padding: '0.9rem',
                      cursor: 'pointer',
                      transition: 'transform 0.15s',
                      border: '1px solid rgba(245, 158, 11, 0.35)',
                    }}
                  >
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                      <span style={{ fontSize: '1.4rem' }}>📢</span>
                      <span style={{ fontSize: '0.7rem', color: '#fbbf24', fontWeight: 800 }}>
                        {visibleAnnouncements.length} New
                      </span>
                    </div>
                    <div style={{ fontSize: '0.85rem', fontWeight: 700, color: '#f8fafc', marginTop: '6px' }}>
                      Announcements
                    </div>
                    <div style={{ fontSize: '0.68rem', color: '#94a3b8' }}>
                      {isFaculty ? 'Post & View' : 'Campus circulars'}
                    </div>
                  </div>

                  {/* Timetable Card */}
                  <div
                    onClick={() => handleTabChange('schedule')}
                    className="glass-panel"
                    style={{
                      padding: '0.9rem',
                      cursor: 'pointer',
                      transition: 'transform 0.15s',
                    }}
                  >
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                      <span style={{ fontSize: '1.4rem' }}>📅</span>
                      <span style={{ fontSize: '0.7rem', color: '#a78bfa', fontWeight: 800 }}>
                        {isFaculty ? 'Change' : 'Classes'}
                      </span>
                    </div>
                    <div style={{ fontSize: '0.85rem', fontWeight: 700, color: '#f8fafc', marginTop: '6px' }}>
                      Timetable
                    </div>
                    <div style={{ fontSize: '0.68rem', color: '#94a3b8' }}>
                      {isFaculty ? 'Reschedule slots' : 'Weekly lectures'}
                    </div>
                  </div>

                  {/* Attendance Card */}
                  <div
                    onClick={() => navigateToSub('attendance')}
                    className="glass-panel"
                    style={{
                      padding: '0.9rem',
                      cursor: 'pointer',
                      transition: 'transform 0.15s',
                    }}
                  >
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                      <span style={{ fontSize: '1.4rem' }}>📊</span>
                      <span style={{ fontSize: '0.7rem', color: '#10b981', fontWeight: 800 }}>
                        {isFaculty ? 'Roster' : '89.0%'}
                      </span>
                    </div>
                    <div style={{ fontSize: '0.85rem', fontWeight: 700, color: '#f8fafc', marginTop: '6px' }}>
                      {isFaculty ? 'Attendance Roster' : 'Attendance'}
                    </div>
                    <div style={{ fontSize: '0.68rem', color: '#94a3b8' }}>
                      {isFaculty ? 'Class marking' : 'Safe status (≥75%)'}
                    </div>
                  </div>

                  {/* Assignments Card */}
                  <div
                    onClick={() => navigateToSub('assignments')}
                    className="glass-panel"
                    style={{
                      padding: '0.9rem',
                      cursor: 'pointer',
                      transition: 'transform 0.15s',
                    }}
                  >
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                      <span style={{ fontSize: '1.4rem' }}>📝</span>
                      <span style={{ fontSize: '0.7rem', color: '#f59e0b', fontWeight: 800 }}>
                        {isFaculty ? 'Grading' : '2 Due'}
                      </span>
                    </div>
                    <div style={{ fontSize: '0.85rem', fontWeight: 700, color: '#f8fafc', marginTop: '6px' }}>
                      {isFaculty ? 'Grading Hub' : 'Assignments'}
                    </div>
                    <div style={{ fontSize: '0.68rem', color: '#94a3b8' }}>
                      {isFaculty ? 'Review submissions' : 'Coursework tasks'}
                    </div>
                  </div>

                  {/* Notifications Card */}
                  <div
                    onClick={() => navigateToSub('notifications')}
                    className="glass-panel"
                    style={{
                      padding: '0.9rem',
                      cursor: 'pointer',
                      transition: 'transform 0.15s',
                      border: notifications.filter((n) => !n.read).length > 0 ? '1px solid rgba(56, 189, 248, 0.4)' : 'none',
                    }}
                  >
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                      <span style={{ fontSize: '1.4rem' }}>🔔</span>
                      <span style={{
                        fontSize: '0.7rem',
                        color: notifications.filter((n) => !n.read).length > 0 ? '#38bdf8' : '#94a3b8',
                        fontWeight: 800,
                      }}>
                        {notifications.filter((n) => !n.read).length > 0
                          ? `${notifications.filter((n) => !n.read).length} New`
                          : 'Caught up'}
                      </span>
                    </div>
                    <div style={{ fontSize: '0.85rem', fontWeight: 700, color: '#f8fafc', marginTop: '6px' }}>
                      Notifications
                    </div>
                    <div style={{ fontSize: '0.68rem', color: '#94a3b8' }}>Real-time alerts</div>
                  </div>

                  {/* Profile Card */}
                  <div
                    onClick={() => handleTabChange('profile')}
                    className="glass-panel"
                    style={{
                      padding: '0.9rem',
                      cursor: 'pointer',
                      transition: 'transform 0.15s',
                      border: '1px solid rgba(56, 189, 248, 0.3)',
                    }}
                  >
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                      <span style={{ fontSize: '1.4rem' }}>👤</span>
                      <span style={{ fontSize: '0.7rem', color: '#38bdf8', fontWeight: 800 }}>Open</span>
                    </div>
                    <div style={{ fontSize: '0.85rem', fontWeight: 700, color: '#f8fafc', marginTop: '6px' }}>
                      My Profile
                    </div>
                    <div style={{ fontSize: '0.68rem', color: '#94a3b8' }}>ID & credentials</div>
                  </div>
                </div>
              </div>

              {/* Today's Schedule Preview */}
              <div>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '8px' }}>
                  <div style={{ fontSize: '0.825rem', fontWeight: 700, color: '#94a3b8', textTransform: 'uppercase', letterSpacing: '0.5px' }}>
                    {isFaculty ? "Today's Teaching Lectures" : "Today's Schedule"}
                  </div>
                  <button
                    onClick={() => handleTabChange('schedule')}
                    style={{ background: 'none', border: 'none', color: '#38bdf8', fontSize: '0.72rem', fontWeight: 700, cursor: 'pointer' }}
                  >
                    Full Week →
                  </button>
                </div>

                <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
                  {schedule.slice(0, 2).map((item) => (
                    <div
                      key={item.id}
                      className="glass-panel"
                      style={{
                        padding: '0.85rem 1rem',
                        borderLeft: `4px solid ${item.color}`,
                        display: 'flex',
                        justifyContent: 'space-between',
                        alignItems: 'center',
                      }}
                    >
                      <div>
                        <div style={{ display: 'flex', gap: '6px', alignItems: 'center' }}>
                          <span style={{ fontSize: '0.75rem', fontWeight: 700, color: '#60a5fa' }}>
                            {item.code} • {item.time}
                          </span>
                        </div>
                        <div style={{ fontSize: '0.85rem', fontWeight: 700, color: '#f8fafc', marginTop: '2px' }}>
                          {item.title}
                        </div>
                        <div style={{ fontSize: '0.7rem', color: '#94a3b8' }}>
                          🏛️ {item.room}
                        </div>
                      </div>

                      {isFaculty && (
                        <button
                          onClick={() => handleOpenEditLecture(item)}
                          className="btn btn-secondary"
                          style={{ padding: '4px 8px', fontSize: '0.72rem' }}
                          title="Change lecture"
                        >
                          ✏️ Edit
                        </button>
                      )}
                    </div>
                  ))}
                </div>
              </div>

              {/* AI Copilot Teaser */}
              <div
                onClick={() => handleTabChange('ai')}
                style={{
                  background: 'linear-gradient(135deg, rgba(99, 102, 241, 0.2), rgba(14, 165, 233, 0.2))',
                  border: '1px solid rgba(99, 102, 241, 0.4)',
                  borderRadius: '14px',
                  padding: '0.9rem',
                  display: 'flex',
                  alignItems: 'center',
                  gap: '12px',
                  cursor: 'pointer',
                }}
              >
                <div style={{ fontSize: '1.6rem' }}>✨</div>
                <div>
                  <div style={{ fontSize: '0.85rem', fontWeight: 700, color: '#f8fafc' }}>
                    Have a question? Ask AI Copilot
                  </div>
                  <div style={{ fontSize: '0.72rem', color: '#94a3b8' }}>
                    {isFaculty ? 'Query student attendance & classroom bookings' : 'Instant answers for placements, timetable & exams'}
                  </div>
                </div>
              </div>
            </div>
          )}

          {/* Schedule Tab with Faculty Change Option */}
          {subView === 'none' && activeTab === 'schedule' && (
            <div style={{ padding: '1rem' }}>
              {/* Day selector with Add button for Faculty */}
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '10px' }}>
                <div style={{ fontSize: '0.85rem', fontWeight: 800, color: '#f8fafc' }}>
                  {selectedDay} Schedule
                </div>
                {isFaculty && (
                  <button
                    onClick={handleOpenAddLecture}
                    className="btn btn-primary"
                    style={{ padding: '4px 10px', fontSize: '0.72rem', borderRadius: '8px' }}
                  >
                    ➕ Add Slot
                  </button>
                )}
              </div>

              <div style={{ display: 'flex', gap: '6px', overflowX: 'auto', paddingBottom: '8px', marginBottom: '12px' }}>
                {days.map((d) => (
                  <button
                    key={d}
                    onClick={() => setSelectedDay(d)}
                    style={{
                      padding: '6px 12px',
                      borderRadius: '8px',
                      border: selectedDay === d ? '1.5px solid #38bdf8' : '1px solid var(--color-border)',
                      backgroundColor: selectedDay === d ? 'rgba(56, 189, 248, 0.2)' : 'rgba(28, 37, 65, 0.6)',
                      color: selectedDay === d ? '#38bdf8' : '#94a3b8',
                      fontWeight: 700,
                      fontSize: '0.75rem',
                      cursor: 'pointer',
                      whiteSpace: 'nowrap',
                    }}
                  >
                    {d.slice(0, 3)}
                  </button>
                ))}
              </div>

              <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
                {daySchedule.length > 0 ? (
                  daySchedule.map((item) => (
                    <div
                      key={item.id}
                      className="glass-panel"
                      style={{
                        padding: '0.9rem 1rem',
                        borderLeft: `4px solid ${item.color}`,
                        display: 'flex',
                        justifyContent: 'space-between',
                        alignItems: 'center',
                      }}
                    >
                      <div style={{ flex: 1 }}>
                        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '4px' }}>
                          <span style={{ fontSize: '0.72rem', fontWeight: 700, color: '#38bdf8' }}>
                            {item.code}
                          </span>
                          <span style={{ fontSize: '0.72rem', color: '#f59e0b', fontWeight: 600 }}>
                            {item.time}
                          </span>
                        </div>
                        <div style={{ fontSize: '0.875rem', fontWeight: 700, color: '#f8fafc', marginBottom: '4px' }}>
                          {item.title}
                        </div>
                        <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.72rem', color: '#94a3b8' }}>
                          <span>🏛️ {item.room}</span>
                          <span>👨‍🏫 {item.instructor}</span>
                        </div>
                      </div>

                      {isFaculty && (
                        <button
                          onClick={() => handleOpenEditLecture(item)}
                          className="btn btn-secondary"
                          style={{ padding: '6px 10px', fontSize: '0.75rem', marginLeft: '10px', whiteSpace: 'nowrap' }}
                          title="Change or reschedule this lecture"
                        >
                          ✏️ Change
                        </button>
                      )}
                    </div>
                  ))
                ) : (
                  <div className="glass-panel" style={{ padding: '2rem', textAlign: 'center', color: '#94a3b8' }}>
                    <div style={{ fontSize: '1.8rem', marginBottom: '6px' }}>☕</div>
                    <div style={{ fontWeight: 700, fontSize: '0.9rem', color: '#f8fafc' }}>
                      No lectures on {selectedDay}
                    </div>
                    {isFaculty && (
                      <button
                        onClick={handleOpenAddLecture}
                        className="btn btn-primary"
                        style={{ marginTop: '10px', padding: '6px 12px', fontSize: '0.75rem' }}
                      >
                        ➕ Add a lecture for {selectedDay}
                      </button>
                    )}
                  </div>
                )}
              </div>
            </div>
          )}

          {/* AI Assistant Tab */}
          {subView === 'none' && activeTab === 'ai' && <AiAssistantView />}

          {/* Profile Tab */}
          {subView === 'none' && activeTab === 'profile' && (
            <div style={{ padding: '1.25rem', display: 'flex', flexDirection: 'column', gap: '14px' }}>
              <div className="glass-panel" style={{ padding: '1.25rem', textAlign: 'center' }}>
                <div style={{
                  width: '64px',
                  height: '64px',
                  borderRadius: '50%',
                  background: isFaculty
                    ? 'linear-gradient(135deg, #4338ca, #6366f1)'
                    : 'linear-gradient(135deg, #2563eb, #38bdf8)',
                  margin: '0 auto 10px',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  fontSize: '1.6rem',
                  fontWeight: 800,
                  color: '#fff',
                }}>
                  {user?.name.charAt(0) || 'A'}
                </div>
                <div style={{ fontSize: '1.1rem', fontWeight: 800, color: '#f8fafc' }}>
                  {user?.name || 'Alex Rivera'}
                </div>
                <div style={{ fontSize: '0.78rem', color: '#94a3b8', marginTop: '2px' }}>
                  {user?.email || 'alex.rivera@unisphere.edu'}
                </div>
                <div style={{ marginTop: '8px' }}>
                  <span className={`badge badge-${user?.role || 'student'}`}>
                    {user?.role === 'faculty' ? 'Faculty Member' : 'Student'} • {user?.department || 'Computer Science'}
                  </span>
                </div>
              </div>

              {/* Account Options & Role Switcher */}
              <div className="glass-panel" style={{ padding: '0.5rem', display: 'flex', flexDirection: 'column' }}>
                <div
                  onClick={onSwitchRole}
                  style={{
                    padding: '12px 14px',
                    display: 'flex',
                    justifyContent: 'space-between',
                    alignItems: 'center',
                    cursor: 'pointer',
                    borderBottom: '1px solid rgba(255,255,255,0.06)',
                  }}
                >
                  <div>
                    <div style={{ fontSize: '0.875rem', fontWeight: 700, color: '#f8fafc' }}>
                      🔄 Switch to {user?.role === 'student' ? 'Faculty 👨‍🏫' : 'Student 🎓'}
                    </div>
                    <div style={{ fontSize: '0.7rem', color: '#94a3b8' }}>
                      Test both student and faculty timetable & announcements
                    </div>
                  </div>
                  <span style={{ color: '#38bdf8', fontWeight: 800 }}>›</span>
                </div>

                <div
                  onClick={() => setIsOfflineMode(!isOfflineMode)}
                  style={{
                    padding: '12px 14px',
                    display: 'flex',
                    justifyContent: 'space-between',
                    alignItems: 'center',
                    cursor: 'pointer',
                    borderBottom: '1px solid rgba(255,255,255,0.06)',
                  }}
                >
                  <div>
                    <div style={{ fontSize: '0.85rem', color: '#f8fafc', fontWeight: 600 }}>
                      💾 Offline Storage Cache
                    </div>
                    <div style={{ fontSize: '0.7rem', color: '#94a3b8' }}>
                      {isOfflineMode ? 'Running from local Hive/IndexedDB cache' : 'Live synchronizing with Python API'}
                    </div>
                  </div>
                  <span style={{ fontSize: '0.75rem', color: isOfflineMode ? '#f59e0b' : '#10b981', fontWeight: 700 }}>
                    {isOfflineMode ? 'Enabled' : 'Connected'}
                  </span>
                </div>

                <div
                  onClick={onLogout}
                  style={{
                    padding: '12px 14px',
                    display: 'flex',
                    justifyContent: 'space-between',
                    alignItems: 'center',
                    cursor: 'pointer',
                    color: '#ef4444',
                  }}
                >
                  <span style={{ fontSize: '0.85rem', fontWeight: 600 }}>
                    🚪 Sign Out
                  </span>
                  <span>›</span>
                </div>
              </div>
            </div>
          )}
            </>
          )}
        </div>

        {/* Mobile Bottom Tab Bar */}
        {user && (
          <div className="mobile-tab-bar">
            <button
              onClick={() => handleTabChange('home')}
              className={`mobile-tab-btn ${activeTab === 'home' && subView === 'none' ? 'active' : ''}`}
            >
            <span className="tab-icon">🏠</span>
            <span>Home</span>
          </button>
          <button
            onClick={() => handleTabChange('schedule')}
            className={`mobile-tab-btn ${activeTab === 'schedule' ? 'active' : ''}`}
          >
            <span className="tab-icon">📅</span>
            <span>Timetable</span>
          </button>
          <button
            onClick={() => handleTabChange('ai')}
            className={`mobile-tab-btn ${activeTab === 'ai' ? 'active' : ''}`}
          >
            <span className="tab-icon">✨</span>
            <span>AI Copilot</span>
          </button>
          <button
            onClick={() => handleTabChange('profile')}
            className={`mobile-tab-btn ${activeTab === 'profile' ? 'active' : ''}`}
          >
            <span className="tab-icon">👤</span>
            <span>Profile</span>
          </button>
        </div>
        )}

        {/* Phone Bottom Home Bar */}
        <div className="phone-home-bar">
          <div className="phone-home-pill" />
        </div>
      </div>

      {/* Faculty Timetable Edit/Add Modal in Phone view */}
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
