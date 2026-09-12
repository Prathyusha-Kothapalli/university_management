import React, { useState, useEffect } from 'react';
import { User } from './types/auth';
import { mockStudentUser, mockFacultyUser } from './services/mockData';
import { AuthPage } from './pages/AuthPage';
import { DashboardPage } from './pages/DashboardPage';
import { CoursesPage } from './pages/CoursesPage';
import { SchedulePage } from './pages/SchedulePage';
import { ProfilePage } from './pages/ProfilePage';
import { PlacementsPage } from './pages/PlacementsPage';
import { AnnouncementsPage } from './pages/AnnouncementsPage';
import { AiRagPlaygroundPage } from './pages/AiRagPlaygroundPage';
import { HostelManagementDashboard } from './pages/Hostel/HostelManagementDashboard';
import { MobileAppShell } from './pages/MobileAppShell';
import { SplashScreen } from './pages/SplashScreen';

export const App: React.FC = () => {
  const [user, setUser] = useState<User | null>(() => {
    try {
      const saved = localStorage.getItem('unisphere_user');
      if (saved) return JSON.parse(saved);
    } catch (_) {}
    return mockStudentUser; // Logged in by default
  });

  const [currentView, setCurrentView] = useState<string>('dashboard');
  const [isMobileMode, setIsMobileMode] = useState<boolean>(() => {
    const saved = localStorage.getItem('unisphere_mode');
    return saved === 'mobile'; // Default to desktop view
  });

  const [showSplash, setShowSplash] = useState<boolean>(() => {
    return !sessionStorage.getItem('unisphere_splash_shown');
  });

  const [isFullscreen, setIsFullscreen] = useState<boolean>(() => {
    return localStorage.getItem('unisphere_fullscreen') === 'true';
  });

  useEffect(() => {
    if (user) {
      localStorage.setItem('unisphere_user', JSON.stringify(user));
    } else {
      localStorage.removeItem('unisphere_user');
    }
  }, [user]);

  const handleFinishSplash = () => {
    sessionStorage.setItem('unisphere_splash_shown', 'true');
    setShowSplash(false);
  };

  const handleToggleMode = (mobile: boolean) => {
    setIsMobileMode(mobile);
    localStorage.setItem('unisphere_mode', mobile ? 'mobile' : 'desktop');
  };

  const handleToggleFullscreen = () => {
    setIsFullscreen((prev) => {
      const next = !prev;
      localStorage.setItem('unisphere_fullscreen', String(next));
      return next;
    });
  };

  const handleLoginSuccess = (authenticatedUser: User) => {
    setUser(authenticatedUser);
    setCurrentView('dashboard');
  };

  const handleLogout = () => {
    setUser(null);
    setCurrentView('auth');
  };

  const handleSwitchRole = () => {
    if (!user) return;
    if (user.role === 'student') {
      setUser(mockFacultyUser);
    } else {
      setUser(mockStudentUser);
    }
  };

  const handleUpdateUser = (updated: User) => {
    setUser(updated);
  };

  return (
    <div style={{ minHeight: '100vh', display: 'flex', flexDirection: 'column', backgroundColor: '#0b132b', color: '#f8fafc' }}>
      {/* Splash Screen */}
      {showSplash && <SplashScreen onFinish={handleFinishSplash} />}

      {/* Top Header / Desktop Navigation Bar */}
      <header style={{
        backgroundColor: 'rgba(15, 23, 42, 0.95)',
        backdropFilter: 'blur(16px)',
        borderBottom: '1px solid rgba(255, 255, 255, 0.08)',
        padding: '0.75rem 1.5rem',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'space-between',
        position: 'sticky',
        top: 0,
        zIndex: 100,
        flexWrap: 'wrap',
        gap: '0.75rem',
      }}>
        {/* Brand Logo & Title */}
        <div style={{ display: 'flex', alignItems: 'center', gap: '12px', cursor: 'pointer' }} onClick={() => setCurrentView('dashboard')}>
          <div style={{
            width: '36px',
            height: '36px',
            borderRadius: '10px',
            background: 'linear-gradient(135deg, #2563eb, #7c3aed)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            color: '#fff',
            fontWeight: 800,
            fontSize: '1.1rem',
            boxShadow: '0 4px 12px rgba(37, 99, 235, 0.4)',
          }}>
            U
          </div>
          <div>
            <div style={{ fontWeight: 800, fontSize: '1.1rem', letterSpacing: '-0.3px', background: 'linear-gradient(90deg, #38bdf8, #818cf8)', WebkitBackgroundClip: 'text', WebkitTextFillColor: 'transparent' }}>
              UniSphere AI
            </div>
            <div style={{ fontSize: '0.7rem', color: '#64748b', fontWeight: 600 }}>
              Enterprise Web Application Portal
            </div>
          </div>
        </div>

        {/* Web Navigation Tabs (when logged in and in desktop mode) */}
        {user && !isMobileMode && (
          <nav style={{ display: 'flex', alignItems: 'center', gap: '4px', flexWrap: 'wrap' }}>
            {[
              { id: 'dashboard', label: '📊 Dashboard' },
              { id: 'hostel', label: '🏢 Hostel Dashboard' },
              { id: 'courses', label: '📚 Courses' },
              { id: 'schedule', label: '📅 Timetable' },
              { id: 'placements', label: '💼 Placements' },
              { id: 'announcements', label: '📢 Notices' },
              { id: 'ai', label: '🤖 AI Copilot' },
              { id: 'profile', label: '👤 Profile' },
            ].map((tab) => {
              const active = currentView === tab.id;
              return (
                <button
                  key={tab.id}
                  onClick={() => setCurrentView(tab.id)}
                  style={{
                    padding: '6px 14px',
                    borderRadius: '8px',
                    fontSize: '0.85rem',
                    fontWeight: active ? 700 : 500,
                    border: 'none',
                    cursor: 'pointer',
                    backgroundColor: active ? 'rgba(37, 99, 235, 0.25)' : 'transparent',
                    color: active ? '#38bdf8' : '#94a3b8',
                    transition: 'all 0.15s ease',
                  }}
                >
                  {tab.label}
                </button>
              );
            })}
          </nav>
        )}

        {/* Right Controls & Mode Switcher */}
        <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
          {/* Mode Switcher Toggle */}
          <div style={{
            display: 'flex',
            backgroundColor: 'rgba(255, 255, 255, 0.05)',
            padding: '3px',
            borderRadius: '10px',
            border: '1px solid rgba(255, 255, 255, 0.1)',
          }}>
            <button
              onClick={() => handleToggleMode(false)}
              style={{
                padding: '4px 10px',
                borderRadius: '7px',
                fontSize: '0.78rem',
                fontWeight: !isMobileMode ? 700 : 500,
                border: 'none',
                cursor: 'pointer',
                backgroundColor: !isMobileMode ? '#2563eb' : 'transparent',
                color: !isMobileMode ? '#ffffff' : '#94a3b8',
                transition: 'all 0.15s ease',
              }}
            >
              🖥️ Web App
            </button>
            <button
              onClick={() => handleToggleMode(true)}
              style={{
                padding: '4px 10px',
                borderRadius: '7px',
                fontSize: '0.78rem',
                fontWeight: isMobileMode ? 700 : 500,
                border: 'none',
                cursor: 'pointer',
                backgroundColor: isMobileMode ? '#2563eb' : 'transparent',
                color: isMobileMode ? '#ffffff' : '#94a3b8',
                transition: 'all 0.15s ease',
              }}
            >
              📱 Mobile App
            </button>
          </div>

          {user && (
            <>
              {/* Role Switcher */}
              <button
                onClick={handleSwitchRole}
                style={{
                  padding: '4px 10px',
                  borderRadius: '8px',
                  fontSize: '0.75rem',
                  fontWeight: 600,
                  backgroundColor: 'rgba(168, 85, 247, 0.15)',
                  border: '1px solid rgba(168, 85, 247, 0.3)',
                  color: '#c084fc',
                  cursor: 'pointer',
                }}
                title="Click to toggle Student / Faculty demo user"
              >
                🔄 {user.role === 'student' ? 'Student View' : 'Faculty View'}
              </button>

              {/* Sign Out */}
              <button
                onClick={handleLogout}
                style={{
                  padding: '4px 10px',
                  borderRadius: '8px',
                  fontSize: '0.75rem',
                  fontWeight: 600,
                  backgroundColor: 'rgba(239, 68, 68, 0.12)',
                  border: '1px solid rgba(239, 68, 68, 0.25)',
                  color: '#f87171',
                  cursor: 'pointer',
                }}
              >
                Sign Out
              </button>
            </>
          )}
        </div>
      </header>

      {/* Main App Content */}
      <main style={{ flex: 1, display: 'flex', flexDirection: 'column' }}>
        {!user || currentView === 'auth' ? (
          <AuthPage onSuccess={handleLoginSuccess} />
        ) : isMobileMode ? (
          /* Mobile App Simulator View */
          <div style={{
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            justifyContent: 'center',
            padding: '1.5rem 0.5rem',
            background: 'radial-gradient(circle at 50% 20%, rgba(37, 99, 235, 0.12), transparent 70%)',
            flex: 1,
          }}>
            <div style={{
              display: 'flex',
              alignItems: 'center',
              gap: '12px',
              marginBottom: '1rem',
              color: '#94a3b8',
              fontSize: '0.85rem',
            }}>
              <span>📱 <strong>UniSphere Mobile Simulator</strong></span>
              <span>•</span>
              <span style={{ color: '#10b981' }}>Live Interactive Prototype</span>
              <span>•</span>
              <button
                onClick={() => handleToggleMode(false)}
                style={{
                  background: 'rgba(255,255,255,0.06)',
                  border: '1px solid rgba(255,255,255,0.12)',
                  color: '#38bdf8',
                  borderRadius: '6px',
                  padding: '2px 8px',
                  fontSize: '0.75rem',
                  cursor: 'pointer',
                }}
              >
                Switch to Web App ↗
              </button>
            </div>

            <MobileAppShell
              user={user}
              onLogin={handleLoginSuccess}
              onLogout={handleLogout}
              onSwitchRole={handleSwitchRole}
              isFullscreen={isFullscreen}
              onToggleFullscreen={handleToggleFullscreen}
            />
          </div>
        ) : (
          /* Desktop Web Application View */
          <div style={{ flex: 1, padding: '1rem' }}>
            {currentView === 'dashboard' && <DashboardPage user={user} onNavigate={setCurrentView} />}
            {currentView === 'hostel' && <HostelManagementDashboard user={user} />}
            {currentView === 'courses' && <CoursesPage />}
            {currentView === 'schedule' && <SchedulePage user={user} />}
            {currentView === 'placements' && <PlacementsPage user={user} />}
            {currentView === 'announcements' && <AnnouncementsPage user={user} />}
            {currentView === 'ai' && <AiRagPlaygroundPage />}
            {currentView === 'profile' && (
              <ProfilePage
                user={user}
                onUpdateUser={handleUpdateUser}
                onLogout={handleLogout}
              />
            )}
          </div>
        )}
      </main>

      {/* Modern Desktop Footer */}
      <footer style={{
        padding: '1.25rem 2rem',
        textAlign: 'center',
        borderTop: '1px solid rgba(255, 255, 255, 0.06)',
        color: '#64748b',
        fontSize: '0.8rem',
        backgroundColor: 'rgba(15, 23, 42, 0.8)',
      }}>
        <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', gap: '8px', flexWrap: 'wrap' }}>
          <span style={{
            width: '8px',
            height: '8px',
            borderRadius: '50%',
            backgroundColor: '#10b981',
            display: 'inline-block',
          }} />
          <span>UniSphere AI Enterprise Platform • Multi-Tenant Web Portal • http://localhost:3000</span>
        </div>
      </footer>
    </div>
  );
};

export default App;

