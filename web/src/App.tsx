import React, { useState } from 'react';
import { AuthProvider, useAuth } from './features/auth/AuthContext';
import { Navbar } from './components/Navbar';
import { LoginForm } from './components/LoginForm';
import { SuperAdminDashboard } from './components/SuperAdminDashboard';
import { UniversityAdminDashboard } from './components/UniversityAdminDashboard';
import { UserPortalView } from './components/UserPortalView';
import { AIStudyAssistant } from './components/AIStudyAssistant';
import { AIBotWidget } from './components/AIBotWidget';
import { MobileSimulatorView } from './components/MobileSimulatorView';
import { MobileNativePortalView } from './components/MobileNativePortalView';
import { useIsMobile } from './hooks/useIsMobile';

const MainContent: React.FC<{
  currentView: 'dashboard' | 'study_assistant' | 'mobile_simulator';
  onViewChange: (view: 'dashboard' | 'study_assistant' | 'mobile_simulator') => void;
  isMobile: boolean;
  onOpenBot: () => void;
}> = ({ currentView, onViewChange, isMobile, onOpenBot }) => {
  const { user, isLoading } = useAuth();

  if (isLoading) {
    return (
      <div style={{
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        minHeight: '80vh',
        color: '#94a3b8',
        fontSize: '1.1rem'
      }}>
        Loading UniSphere AI secure session...
      </div>
    );
  }

  // If in mobile viewport (e.g. Inspect -> Device Mode or mobile screen)
  if (isMobile) {
    if (currentView === 'study_assistant') {
      return <AIStudyAssistant />;
    }
    if (!user && currentView !== 'mobile_simulator') {
      return (
        <div style={{ padding: '1rem 0' }}>
          <LoginForm onOpenMobileView={() => onViewChange('mobile_simulator')} />
        </div>
      );
    }
    // Render full-screen mobile app layout natively
    return (
      <MobileNativePortalView
        onSwitchToDesktop={() => onViewChange('dashboard')}
        onOpenBot={onOpenBot}
      />
    );
  }

  // Desktop viewport
  if (currentView === 'mobile_simulator') {
    return <MobileSimulatorView />;
  }

  if (currentView === 'study_assistant') {
    return <AIStudyAssistant />;
  }

  if (!user) {
    return <LoginForm onOpenMobileView={() => onViewChange('mobile_simulator')} />;
  }

  // Role-based dashboard views
  switch (user.role) {
    case 'SUPER_ADMIN':
      return <SuperAdminDashboard />;
    case 'UNIVERSITY_ADMIN':
      return <UniversityAdminDashboard />;
    case 'FACULTY':
    case 'STUDENT':
    case 'STAFF':
    default:
      return <UserPortalView />;
  }
};

const AppContent: React.FC = () => {
  const isMobile = useIsMobile(768);
  const [currentView, setCurrentView] = useState<'dashboard' | 'study_assistant' | 'mobile_simulator'>(() => {
    if (typeof window !== 'undefined' && window.location.hash.includes('mobile')) {
      return 'mobile_simulator';
    }
    return 'dashboard';
  });
  const [isBotOpen, setIsBotOpen] = useState<boolean>(false);

  const handleViewChange = (view: 'dashboard' | 'study_assistant' | 'mobile_simulator') => {
    setCurrentView(view);
    if (typeof window !== 'undefined') {
      if (view === 'mobile_simulator') {
        window.location.hash = '#mobile';
      } else {
        history.replaceState(null, '', window.location.pathname);
      }
    }
  };

  return (
    <div style={{
      minHeight: '100vh',
      backgroundColor: '#0f172a',
      color: '#f8fafc',
      fontFamily: 'system-ui, -apple-system, sans-serif',
      position: 'relative',
      overflowX: 'hidden'
    }}>
      {/* Show full navbar on desktop, or when user is on dashboard in desktop view */}
      {!isMobile && (
        <Navbar
          currentView={currentView}
          onViewChange={handleViewChange}
          onToggleBot={() => setIsBotOpen(prev => !prev)}
          isBotOpen={isBotOpen}
        />
      )}

      <main>
        <MainContent
          currentView={currentView}
          onViewChange={handleViewChange}
          isMobile={isMobile}
          onOpenBot={() => setIsBotOpen(true)}
        />
      </main>

      {/* Floating AI Bot Assistant Feature across the whole site */}
      <AIBotWidget
        isOpen={isBotOpen}
        onToggle={() => setIsBotOpen(prev => !prev)}
      />
    </div>
  );
};

export const App: React.FC = () => {
  return (
    <AuthProvider>
      <AppContent />
    </AuthProvider>
  );
};

export default App;

