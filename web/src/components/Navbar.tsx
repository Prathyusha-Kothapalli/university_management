import React from 'react';
import { User } from '../types/auth';

interface NavbarProps {
  user: User | null;
  currentView: string;
  onNavigate: (view: string) => void;
  onLogout: () => void;
  onSwitchRole: () => void;
  isMobileMode?: boolean;
  onToggleMobileMode?: (mobile: boolean) => void;
}

export const Navbar: React.FC<NavbarProps> = ({
  user,
  currentView,
  onNavigate,
  onLogout,
  onSwitchRole,
  isMobileMode = false,
  onToggleMobileMode,
}) => {
  return (
    <header style={{
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'space-between',
      padding: '0.875rem 2rem',
      backgroundColor: 'rgba(15, 23, 42, 0.85)',
      backdropFilter: 'blur(16px)',
      borderBottom: '1px solid rgba(255, 255, 255, 0.08)',
      position: 'sticky',
      top: 0,
      zIndex: 100,
    }}>
      {/* Brand */}
      <div 
        onClick={() => onNavigate('dashboard')}
        style={{
          display: 'flex',
          alignItems: 'center',
          gap: '12px',
          cursor: 'pointer',
        }}
      >
        <div style={{
          width: '38px',
          height: '38px',
          borderRadius: '10px',
          background: 'linear-gradient(135deg, #2563eb, #0ea5e9)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          color: '#ffffff',
          fontWeight: 800,
          fontSize: '1.2rem',
          boxShadow: '0 4px 12px rgba(37, 99, 235, 0.4)',
        }}>
          U
        </div>
        <div>
          <div style={{ fontWeight: 800, fontSize: '1.15rem', color: '#f8fafc', letterSpacing: '-0.3px' }}>
            UniSphere <span style={{ color: '#38bdf8' }}>AI</span>
          </div>
          <div style={{ fontSize: '0.72rem', color: '#94a3b8', letterSpacing: '0.3px' }}>
            Campus Portal
          </div>
        </div>
      </div>

      {/* Nav Navigation Links */}
      {user && (
        <nav style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
          {[
            { id: 'dashboard', label: 'Dashboard' },
            { id: 'courses', label: 'Courses' },
            { id: 'schedule', label: 'Timetable' },
            { id: 'profile', label: 'My Profile' },
          ].map((item) => (
            <button
              key={item.id}
              onClick={() => onNavigate(item.id)}
              style={{
                background: currentView === item.id ? 'rgba(37, 99, 235, 0.2)' : 'transparent',
                color: currentView === item.id ? '#38bdf8' : '#94a3b8',
                border: currentView === item.id ? '1px solid rgba(56, 189, 248, 0.3)' : '1px solid transparent',
                padding: '8px 16px',
                borderRadius: '8px',
                fontSize: '0.875rem',
                fontWeight: currentView === item.id ? 700 : 500,
                cursor: 'pointer',
                transition: 'all 0.2s',
              }}
            >
              {item.label}
            </button>
          ))}
        </nav>
      )}

      {/* User Actions */}
      {user ? (
        <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
          {/* Mobile vs Desktop View Toggle */}
          {onToggleMobileMode && (
            <div style={{
              display: 'flex',
              background: 'rgba(15, 23, 42, 0.9)',
              padding: '3px',
              borderRadius: '10px',
              border: '1px solid rgba(255, 255, 255, 0.12)',
              gap: '2px',
            }}>
              <button
                type="button"
                onClick={() => onToggleMobileMode(true)}
                style={{
                  padding: '5px 12px',
                  borderRadius: '7px',
                  border: 'none',
                  background: isMobileMode ? 'linear-gradient(135deg, #2563eb, #0ea5e9)' : 'transparent',
                  color: isMobileMode ? '#ffffff' : '#94a3b8',
                  fontSize: '0.75rem',
                  fontWeight: 700,
                  cursor: 'pointer',
                  display: 'flex',
                  alignItems: 'center',
                  gap: '4px',
                  boxShadow: isMobileMode ? '0 2px 8px rgba(37,99,235,0.4)' : 'none',
                  transition: 'all 0.15s ease',
                }}
              >
                📱 Mobile View
              </button>
              <button
                type="button"
                onClick={() => onToggleMobileMode(false)}
                style={{
                  padding: '5px 12px',
                  borderRadius: '7px',
                  border: 'none',
                  background: !isMobileMode ? 'linear-gradient(135deg, #2563eb, #0ea5e9)' : 'transparent',
                  color: !isMobileMode ? '#ffffff' : '#94a3b8',
                  fontSize: '0.75rem',
                  fontWeight: 700,
                  cursor: 'pointer',
                  display: 'flex',
                  alignItems: 'center',
                  gap: '4px',
                  boxShadow: !isMobileMode ? '0 2px 8px rgba(37,99,235,0.4)' : 'none',
                  transition: 'all 0.15s ease',
                }}
              >
                🖥️ Desktop
              </button>
            </div>
          )}

          {/* Role Switcher Pill */}
          <button
            onClick={onSwitchRole}
            title="Toggle between Student and Faculty portal view"
            style={{
              padding: '5px 12px',
              borderRadius: '20px',
              border: '1px solid #3b82f6',
              background: 'rgba(37, 99, 235, 0.15)',
              color: '#60a5fa',
              fontSize: '0.75rem',
              fontWeight: 700,
              cursor: 'pointer',
            }}
          >
            Role: {user.role === 'student' ? 'Student 🎓' : 'Faculty 👨‍🏫'}
          </button>

          {/* User Info Avatar */}
          <div 
            onClick={() => onNavigate('profile')}
            style={{
              display: 'flex',
              alignItems: 'center',
              gap: '10px',
              cursor: 'pointer',
              padding: '4px 10px',
              borderRadius: '24px',
              background: 'rgba(255, 255, 255, 0.05)',
            }}
          >
            <div style={{
              width: '32px',
              height: '32px',
              borderRadius: '50%',
              background: '#2563eb',
              color: '#ffffff',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              fontWeight: 700,
              fontSize: '0.85rem',
            }}>
              {user.name.charAt(0)}
            </div>
            <div style={{ textAlign: 'left', display: 'flex', flexDirection: 'column' }}>
              <span style={{ fontSize: '0.85rem', fontWeight: 600, color: '#f8fafc' }}>
                {user.name.split(' ')[0]}
              </span>
              <span style={{ fontSize: '0.7rem', color: '#94a3b8' }}>
                {user.studentId}
              </span>
            </div>
          </div>

          {/* Logout Button */}
          <button
            onClick={onLogout}
            className="btn btn-danger"
            style={{ padding: '6px 14px', fontSize: '0.8rem' }}
          >
            Sign Out
          </button>
        </div>
      ) : (
        <div style={{ display: 'flex', gap: '10px' }}>
          <button
            onClick={() => onNavigate('auth')}
            className="btn btn-primary"
            style={{ padding: '8px 20px', fontSize: '0.875rem' }}
          >
            Sign In
          </button>
        </div>
      )}
    </header>
  );
};
