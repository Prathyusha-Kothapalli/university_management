import React, { useState } from 'react';
import { AuthProvider, useAuth } from './features/auth/AuthContext';
import { Navbar } from './components/Navbar';
import { LoginForm } from './components/LoginForm';
import { SuperAdminDashboard } from './components/SuperAdminDashboard';
import { UniversityAdminDashboard } from './components/UniversityAdminDashboard';
import { UserPortalView } from './components/UserPortalView';
import { AIStudyAssistant } from './components/AIStudyAssistant';
import { AIBotWidget } from './components/AIBotWidget';

const MainContent: React.FC<{ currentView: 'dashboard' | 'study_assistant' }> = ({ currentView }) => {
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

  if (currentView === 'study_assistant') {
    return <AIStudyAssistant />;
  }

  if (!user) {
    return <LoginForm />;
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
  const [currentView, setCurrentView] = useState<'dashboard' | 'study_assistant'>('dashboard');
  const [isBotOpen, setIsBotOpen] = useState<boolean>(false);

  return (
    <div style={{
      minHeight: '100vh',
      backgroundColor: '#0f172a',
      color: '#f8fafc',
      fontFamily: 'system-ui, -apple-system, sans-serif',
      position: 'relative'
    }}>
      <Navbar
        currentView={currentView}
        onViewChange={setCurrentView}
        onToggleBot={() => setIsBotOpen(prev => !prev)}
        isBotOpen={isBotOpen}
      />
      <main>
        <MainContent currentView={currentView} />
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

