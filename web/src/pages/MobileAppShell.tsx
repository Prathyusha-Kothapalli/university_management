import React, { useState } from 'react';
import { User } from '../types/auth';
import { AttendanceView } from './AttendanceView';
import { AssignmentsView } from './AssignmentsView';
import { ExamsView } from './ExamsView';
import { PlacementsView } from './PlacementsView';
import { AiAssistantView } from './AiAssistantView';
import { mockSchedule } from '../services/mockData';

interface MobileAppShellProps {
  user: User | null;
  onLogout: () => void;
  onSwitchRole: () => void;
}

export const MobileAppShell: React.FC<MobileAppShellProps> = ({
  user,
  onLogout,
  onSwitchRole,
}) => {
  const [activeTab, setActiveTab] = useState<'home' | 'schedule' | 'ai' | 'profile'>('home');
  const [subView, setSubView] = useState<'none' | 'attendance' | 'assignments' | 'exams' | 'placements'>('none');
  const [selectedDay, setSelectedDay] = useState('Monday');
  const [isOfflineMode, setIsOfflineMode] = useState(false);

  const days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'];
  const daySchedule = mockSchedule.filter((s) => s.day === selectedDay);

  const navigateToSub = (view: 'attendance' | 'assignments' | 'exams' | 'placements') => {
    setSubView(view);
  };

  const handleTabChange = (tab: 'home' | 'schedule' | 'ai' | 'profile') => {
    setActiveTab(tab);
    setSubView('none');
  };

  return (
    <div className="phone-wrapper">
      <div className="phone-shell">
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
              <div style={{
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
              }}>
                U
              </div>
            )}
            <div>
              <div style={{ fontSize: '0.85rem', fontWeight: 800, color: '#f8fafc', letterSpacing: '-0.3px' }}>
                {subView === 'attendance'
                  ? 'Attendance Tracker'
                  : subView === 'assignments'
                  ? 'Active Assignments'
                  : subView === 'exams'
                  ? 'Exams & Results'
                  : subView === 'placements'
                  ? 'Campus Placements'
                  : activeTab === 'schedule'
                  ? 'Weekly Timetable'
                  : activeTab === 'ai'
                  ? 'UniSphere AI'
                  : activeTab === 'profile'
                  ? 'My Account'
                  : 'UniSphere Mobile'}
              </div>
              <div style={{ fontSize: '0.65rem', color: isOfflineMode ? '#f59e0b' : '#10b981' }}>
                {isOfflineMode ? '● Offline Mode Active' : '● Connected to Python API'}
              </div>
            </div>
          </div>

          {/* Quick status badges */}
          <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
            <span
              onClick={() => setIsOfflineMode(!isOfflineMode)}
              title="Click to toggle simulated Offline Mode"
              style={{
                fontSize: '0.65rem',
                cursor: 'pointer',
                padding: '2px 8px',
                borderRadius: '8px',
                background: isOfflineMode ? 'rgba(245, 158, 11, 0.2)' : 'rgba(16, 185, 129, 0.15)',
                color: isOfflineMode ? '#f59e0b' : '#10b981',
                fontWeight: 700,
              }}
            >
              {isOfflineMode ? 'Offline' : 'Online'}
            </span>
            <div style={{
              width: '28px',
              height: '28px',
              borderRadius: '50%',
              background: '#334155',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              fontSize: '0.75rem',
              fontWeight: 700,
              color: '#38bdf8',
            }}>
              {user?.name.charAt(0) || 'U'}
            </div>
          </div>
        </div>

        {/* Phone Scrollable Screen Content */}
        <div className="phone-screen">
          {/* 1. If inside a SubView */}
          {subView === 'attendance' && <AttendanceView />}
          {subView === 'assignments' && <AssignmentsView />}
          {subView === 'exams' && <ExamsView />}
          {subView === 'placements' && <PlacementsView />}

          {/* 2. If at Root of Active Tab */}
          {subView === 'none' && activeTab === 'home' && (
            <div style={{ padding: '1.25rem', display: 'flex', flexDirection: 'column', gap: '14px' }}>
              {/* Student Greeting Banner */}
              <div style={{
                background: 'linear-gradient(135deg, #1e3a8a, #0369a1)',
                padding: '1.25rem',
                borderRadius: '16px',
                color: '#fff',
                boxShadow: '0 4px 16px rgba(3, 105, 161, 0.25)',
              }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
                  <div>
                    <div style={{ fontSize: '0.75rem', opacity: 0.85 }}>Welcome back 👋</div>
                    <div style={{ fontSize: '1.2rem', fontWeight: 800, marginTop: '2px' }}>
                      {user?.name || 'Alex Rivera'}
                    </div>
                    <div style={{ fontSize: '0.72rem', opacity: 0.8, marginTop: '2px' }}>
                      Roll: {user?.id || 'CS-2023-889'} • Dept of CS & AI
                    </div>
                  </div>
                  <span style={{
                    fontSize: '0.7rem',
                    background: 'rgba(255,255,255,0.2)',
                    padding: '2px 8px',
                    borderRadius: '8px',
                    fontWeight: 700,
                  }}>
                    Fall 2026
                  </span>
                </div>
              </div>

              {/* Quick Actions Grid (Flutter Modules) */}
              <div>
                <div style={{ fontSize: '0.825rem', fontWeight: 700, color: '#94a3b8', marginBottom: '8px', textTransform: 'uppercase', letterSpacing: '0.5px' }}>
                  Mobile Campus Modules
                </div>
                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(2, 1fr)', gap: '10px' }}>
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
                      <span style={{ fontSize: '0.7rem', color: '#10b981', fontWeight: 800 }}>89.0%</span>
                    </div>
                    <div style={{ fontSize: '0.85rem', fontWeight: 700, color: '#f8fafc', marginTop: '6px' }}>
                      Attendance
                    </div>
                    <div style={{ fontSize: '0.68rem', color: '#94a3b8' }}>All subjects safe</div>
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
                      <span style={{ fontSize: '0.7rem', color: '#f59e0b', fontWeight: 800 }}>2 Due</span>
                    </div>
                    <div style={{ fontSize: '0.85rem', fontWeight: 700, color: '#f8fafc', marginTop: '6px' }}>
                      Assignments
                    </div>
                    <div style={{ fontSize: '0.68rem', color: '#94a3b8' }}>Next: Sep 18</div>
                  </div>

                  {/* Exams & Transcripts */}
                  <div
                    onClick={() => navigateToSub('exams')}
                    className="glass-panel"
                    style={{
                      padding: '0.9rem',
                      cursor: 'pointer',
                      transition: 'transform 0.15s',
                    }}
                  >
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                      <span style={{ fontSize: '1.4rem' }}>🎯</span>
                      <span style={{ fontSize: '0.7rem', color: '#a78bfa', fontWeight: 800 }}>9.42 CGPA</span>
                    </div>
                    <div style={{ fontSize: '0.85rem', fontWeight: 700, color: '#f8fafc', marginTop: '6px' }}>
                      Exams & Grades
                    </div>
                    <div style={{ fontSize: '0.68rem', color: '#94a3b8' }}>Admit card ready</div>
                  </div>

                  {/* Placements */}
                  <div
                    onClick={() => navigateToSub('placements')}
                    className="glass-panel"
                    style={{
                      padding: '0.9rem',
                      cursor: 'pointer',
                      transition: 'transform 0.15s',
                    }}
                  >
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                      <span style={{ fontSize: '1.4rem' }}>💼</span>
                      <span style={{ fontSize: '0.7rem', color: '#34d399', fontWeight: 800 }}>4 Drives</span>
                    </div>
                    <div style={{ fontSize: '0.85rem', fontWeight: 700, color: '#f8fafc', marginTop: '6px' }}>
                      Placements
                    </div>
                    <div style={{ fontSize: '0.68rem', color: '#94a3b8' }}>Google, NVIDIA, Apple</div>
                  </div>
                </div>
              </div>

              {/* Today's Classes */}
              <div>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '8px' }}>
                  <div style={{ fontSize: '0.825rem', fontWeight: 700, color: '#94a3b8', textTransform: 'uppercase', letterSpacing: '0.5px' }}>
                    Today's Schedule
                  </div>
                  <button
                    onClick={() => handleTabChange('schedule')}
                    style={{ background: 'none', border: 'none', color: '#38bdf8', fontSize: '0.72rem', fontWeight: 700, cursor: 'pointer' }}
                  >
                    Full Week →
                  </button>
                </div>

                <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
                  <div className="glass-panel" style={{ padding: '0.85rem 1rem', borderLeft: '4px solid #3b82f6' }}>
                    <div style={{ display: 'flex', justifyContent: 'space-between' }}>
                      <span style={{ fontSize: '0.75rem', fontWeight: 700, color: '#60a5fa' }}>CS-401 • 10:00 AM</span>
                      <span style={{ fontSize: '0.7rem', color: '#94a3b8' }}>Turing B-204</span>
                    </div>
                    <div style={{ fontSize: '0.85rem', fontWeight: 700, color: '#f8fafc', marginTop: '3px' }}>
                      Deep Learning & Neural Architectures
                    </div>
                  </div>

                  <div className="glass-panel" style={{ padding: '0.85rem 1rem', borderLeft: '4px solid #10b981' }}>
                    <div style={{ display: 'flex', justifyContent: 'space-between' }}>
                      <span style={{ fontSize: '0.75rem', fontWeight: 700, color: '#34d399' }}>DS-310 • 01:30 PM</span>
                      <span style={{ fontSize: '0.7rem', color: '#94a3b8' }}>Newton N-101</span>
                    </div>
                    <div style={{ fontSize: '0.85rem', fontWeight: 700, color: '#f8fafc', marginTop: '3px' }}>
                      Big Data Distributed Systems
                    </div>
                  </div>
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
                    Have a question? Ask AI
                  </div>
                  <div style={{ fontSize: '0.72rem', color: '#94a3b8' }}>
                    Instant answers for rooms, attendance & schedules
                  </div>
                </div>
              </div>
            </div>
          )}

          {/* Schedule Tab */}
          {subView === 'none' && activeTab === 'schedule' && (
            <div style={{ padding: '1rem' }}>
              {/* Day selector */}
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
                {daySchedule.map((item) => (
                  <div
                    key={item.id}
                    className="glass-panel"
                    style={{
                      padding: '0.9rem 1rem',
                      borderLeft: `4px solid ${item.color}`,
                    }}
                  >
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
                ))}
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
                  background: 'linear-gradient(135deg, #2563eb, #38bdf8)',
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
                    {user?.role || 'Student'} • {user?.department || 'Computer Science'}
                  </span>
                </div>
              </div>

              {/* Account Options */}
              <div className="glass-panel" style={{ padding: '0.5rem', display: 'flex', flexDirection: 'column' }}>
                <div
                  onClick={onSwitchRole}
                  style={{
                    padding: '10px 12px',
                    display: 'flex',
                    justifyContent: 'space-between',
                    alignItems: 'center',
                    cursor: 'pointer',
                    borderBottom: '1px solid rgba(255,255,255,0.06)',
                  }}
                >
                  <span style={{ fontSize: '0.85rem', color: '#f8fafc' }}>
                    🔄 Switch to {user?.role === 'student' ? 'Faculty' : 'Student'} Role
                  </span>
                  <span style={{ color: '#38bdf8' }}>›</span>
                </div>

                <div
                  onClick={() => setIsOfflineMode(!isOfflineMode)}
                  style={{
                    padding: '10px 12px',
                    display: 'flex',
                    justifyContent: 'space-between',
                    alignItems: 'center',
                    cursor: 'pointer',
                    borderBottom: '1px solid rgba(255,255,255,0.06)',
                  }}
                >
                  <div>
                    <div style={{ fontSize: '0.85rem', color: '#f8fafc' }}>
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
                    padding: '10px 12px',
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
        </div>

        {/* Mobile Bottom Tab Bar */}
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

        {/* Phone Bottom Home Bar */}
        <div className="phone-home-bar">
          <div className="phone-home-pill" />
        </div>
      </div>
    </div>
  );
};
