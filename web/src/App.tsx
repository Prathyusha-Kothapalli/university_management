import React, { useState, useEffect } from 'react';
import { User } from './types/auth';
import { mockStudentUser, mockFacultyUser } from './services/mockData';
import { Navbar } from './components/Navbar';
import { AuthPage } from './pages/AuthPage';
import { DashboardPage } from './pages/DashboardPage';
import { CoursesPage } from './pages/CoursesPage';
import { SchedulePage } from './pages/SchedulePage';
import { ProfilePage } from './pages/ProfilePage';

export const App: React.FC = () => {
  const [user, setUser] = useState<User | null>(() => {
    try {
      const saved = localStorage.getItem('unisphere_user');
      if (saved) return JSON.parse(saved);
    } catch (_) {}
    return mockStudentUser; // Provide instant access by default
  });

  const [currentView, setCurrentView] = useState<string>('dashboard');

  useEffect(() => {
    if (user) {
      localStorage.setItem('unisphere_user', JSON.stringify(user));
    } else {
      localStorage.removeItem('unisphere_user');
    }
  }, [user]);

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
      />

      {/* Main Content Area */}
      <main style={{ flex: 1, display: 'flex', flexDirection: 'column' }}>
        {!user || currentView === 'auth' ? (
          <AuthPage onSuccess={handleLoginSuccess} />
        ) : (
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
