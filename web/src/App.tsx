import React, { useState, useEffect } from 'react';
import { User } from './types/auth';
import { mockStudentUser, mockFacultyUser } from './services/mockData';
import { Navbar } from './components/Navbar';
import { AuthPage } from './pages/AuthPage';
import { DashboardPage } from './pages/DashboardPage';
import { CoursesPage } from './pages/CoursesPage';
import { SchedulePage } from './pages/SchedulePage';
import { ProfilePage } from './pages/ProfilePage';
import { MobileAppShell } from './pages/MobileAppShell';

export const App: React.FC = () => {
  const [user, setUser] = useState<User | null>(() => {
    try {
      const saved = localStorage.getItem('unisphere_user');
      if (saved) return JSON.parse(saved);
    } catch (_) {}
    return mockStudentUser; // Provide instant access by default
  });

  const [currentView, setCurrentView] = useState<string>('dashboard');
  const [isMobileMode, setIsMobileMode] = useState<boolean>(() => {
    const saved = localStorage.getItem('unisphere_mode');
    return saved !== null ? saved === 'mobile' : true; // Default to true as user requested mobile view
  });

  useEffect(() => {
    if (user) {
      localStorage.setItem('unisphere_user', JSON.stringify(user));
    } else {
      localStorage.removeItem('unisphere_user');
    }
  }, [user]);

  const handleToggleMobileMode = (mobile: boolean) => {
    setIsMobileMode(mobile);
    localStorage.setItem('unisphere_mode', mobile ? 'mobile' : 'desktop');
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
    <div style={{ minHeight: '100vh', display: 'flex', flexDirection: 'column' }}>
      {/* Top Navigation Bar */}
      <Navbar
        user={user}
        currentView={currentView}
        onNavigate={(view) => setCurrentView(view)}
        onLogout={handleLogout}
        onSwitchRole={handleSwitchRole}
        isMobileMode={isMobileMode}
        onToggleMobileMode={handleToggleMobileMode}
      />

      {/* Main Content Area */}
      <main style={{ flex: 1, display: 'flex', flexDirection: 'column' }}>
        {!user || currentView === 'auth' ? (
          <AuthPage onSuccess={handleLoginSuccess} />
        ) : isMobileMode ? (
          /* Mobile Device View (Simulated Smartphone Frame) */
          <div style={{
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            justifyContent: 'center',
            padding: '1rem 0.5rem',
            background: 'radial-gradient(circle at 50% 20%, rgba(37, 99, 235, 0.12), transparent 70%)',
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
                onClick={() => handleToggleMobileMode(false)}
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
                Switch to Full Desktop View ↗
              </button>
            </div>

            <MobileAppShell
              user={user}
              onLogout={handleLogout}
              onSwitchRole={handleSwitchRole}
            />
          </div>
        ) : (
          /* Desktop Web View */
          <>
            {currentView === 'dashboard' && (
              <DashboardPage user={user} onNavigate={setCurrentView} />
            )}
            {currentView === 'courses' && <CoursesPage />}
            {currentView === 'schedule' && <SchedulePage />}
            {currentView === 'profile' && (
              <ProfilePage
                user={user}
                onUpdateUser={handleUpdateUser}
                onLogout={handleLogout}
              />
            )}
          </>
        )}
      </main>

      {/* Modern Footer */}
      <footer style={{
        padding: '1.5rem 2rem',
        textAlign: 'center',
        borderTop: '1px solid rgba(255, 255, 255, 0.06)',
        color: '#64748b',
        fontSize: '0.8rem',
        marginTop: 'auto',
      }}>
        <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', gap: '8px' }}>
          <span style={{
            width: '8px',
            height: '8px',
            borderRadius: '50%',
            backgroundColor: '#10b981',
            display: 'inline-block',
          }} />
          <span>UniSphere AI Platform • Multi-Tenant University Management System • Fall 2026</span>
        </div>
      </footer>
    </div>
  );
};

export default App;
