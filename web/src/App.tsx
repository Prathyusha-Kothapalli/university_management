import React, { useState, useEffect } from 'react';
import { User } from './types/auth';
import { mockStudentUser, mockFacultyUser } from './services/mockData';
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

  const handleToggleFullscreen = () => {
    setIsFullscreen((prev) => {
      const next = !prev;
      localStorage.setItem('unisphere_fullscreen', String(next));
      return next;
    });
  };

  const handleLoginSuccess = (authenticatedUser: User) => {
    setUser(authenticatedUser);
  };

  const handleLogout = () => {
    setUser(null);
  };

  const handleSwitchRole = () => {
    if (!user) return;
    if (user.role === 'student') {
      setUser(mockFacultyUser);
    } else {
      setUser(mockStudentUser);
    }
  };

  return (
    <div style={{
      minHeight: '100vh',
      backgroundColor: '#0b132b',
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      justifyContent: 'center',
      overflow: 'hidden',
    }}>
      {/* Splash Screen */}
      {showSplash && <SplashScreen onFinish={handleFinishSplash} />}

      {/* Pure Mobile Application Experience */}
      <MobileAppShell
        user={user}
        onLogin={handleLoginSuccess}
        onLogout={handleLogout}
        onSwitchRole={handleSwitchRole}
        isFullscreen={isFullscreen}
        onToggleFullscreen={handleToggleFullscreen}
      />
    </div>
  );
};

export default App;
