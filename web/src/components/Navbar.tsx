import React from 'react';
import { useAuth } from '../features/auth/AuthContext';

interface NavbarProps {
  currentView: 'dashboard' | 'study_assistant';
  onViewChange: (view: 'dashboard' | 'study_assistant') => void;
  onToggleBot?: () => void;
  isBotOpen?: boolean;
}

export const Navbar: React.FC<NavbarProps> = ({ currentView, onViewChange, onToggleBot, isBotOpen }) => {
  const { user, tenant, logout } = useAuth();

  const getRoleBadgeStyle = (role?: string) => {
    switch (role) {
      case 'SUPER_ADMIN':
        return { bg: 'rgba(239, 68, 68, 0.15)', border: 'rgba(239, 68, 68, 0.4)', text: '#fca5a5' };
      case 'UNIVERSITY_ADMIN':
        return { bg: 'rgba(245, 158, 11, 0.15)', border: 'rgba(245, 158, 11, 0.4)', text: '#fcd34d' };
      case 'FACULTY':
        return { bg: 'rgba(59, 130, 246, 0.15)', border: 'rgba(59, 130, 246, 0.4)', text: '#93c5fd' };
      case 'STUDENT':
        return { bg: 'rgba(16, 185, 129, 0.15)', border: 'rgba(16, 185, 129, 0.4)', text: '#6ee7b7' };
      case 'STAFF':
        return { bg: 'rgba(168, 85, 247, 0.15)', border: 'rgba(168, 85, 247, 0.4)', text: '#d8b4fe' };
      default:
        return { bg: 'rgba(100, 116, 139, 0.15)', border: 'rgba(100, 116, 139, 0.4)', text: '#cbd5e1' };
    }
  };

  const getInitials = (name?: string) => {
    if (!name) return 'U';
    const parts = name.trim().split(' ');
    if (parts.length >= 2) return `${parts[0][0]}${parts[1][0]}`.toUpperCase();
    return name.slice(0, 2).toUpperCase();
  };

  const badgeStyle = getRoleBadgeStyle(user?.role);

  return (
    <header style={{
      backgroundColor: 'rgba(15, 23, 42, 0.85)',
      backdropFilter: 'blur(12px)',
      WebkitBackdropFilter: 'blur(12px)',
      borderBottom: '1px solid rgba(255, 255, 255, 0.08)',
      padding: '0.65rem 1.75rem',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'space-between',
      position: 'sticky',
      top: 0,
      zIndex: 100,
      boxShadow: '0 4px 20px -5px rgba(0, 0, 0, 0.3)'
    }}>
      {/* Brand & Campus Info */}
      <div style={{ display: 'flex', alignItems: 'center', gap: '1.75rem' }}>
        <div
          style={{ display: 'flex', alignItems: 'center', gap: '0.75rem', cursor: 'pointer' }}
          onClick={() => onViewChange('dashboard')}
        >
          <div style={{
            width: '36px',
            height: '36px',
            borderRadius: '10px',
            background: 'linear-gradient(135deg, #0284c7 0%, #6366f1 100%)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            fontWeight: 800,
            fontSize: '1.1rem',
            color: '#ffffff',
            boxShadow: '0 0 15px rgba(2, 132, 199, 0.4)'
          }}>
            U
          </div>
          <div>
            <div style={{ fontSize: '1.15rem', fontWeight: 800, letterSpacing: '-0.02em', color: '#f8fafc', lineHeight: 1.2 }}>
              UniSphere<span style={{ color: '#38bdf8' }}>.ai</span>
            </div>
            <div style={{ fontSize: '0.65rem', color: '#64748b', fontWeight: 600, letterSpacing: '0.04em', textTransform: 'uppercase' }}>
              Academic Ecosystem
            </div>
          </div>
        </div>

        {/* View Switcher Tabs */}
        <div style={{
          display: 'flex',
          backgroundColor: 'rgba(2, 6, 23, 0.6)',
          padding: '0.25rem',
          borderRadius: '10px',
          border: '1px solid rgba(255, 255, 255, 0.06)',
          alignItems: 'center',
          gap: '0.2rem'
        }}>
          <button
            onClick={() => onViewChange('dashboard')}
            style={{
              backgroundColor: currentView === 'dashboard' ? 'rgba(56, 189, 248, 0.15)' : 'transparent',
              color: currentView === 'dashboard' ? '#38bdf8' : '#94a3b8',
              border: currentView === 'dashboard' ? '1px solid rgba(56, 189, 248, 0.3)' : '1px solid transparent',
              padding: '0.45rem 0.9rem',
              borderRadius: '8px',
              fontSize: '0.82rem',
              fontWeight: 600,
              cursor: 'pointer',
              display: 'flex',
              alignItems: 'center',
              gap: '0.4rem',
              transition: 'all 0.15s ease'
            }}
          >
            <span>🏛️</span>
            <span>{user ? 'Campus Portal' : 'Sign In / Portals'}</span>
          </button>

          <button
            onClick={() => onViewChange('study_assistant')}
            style={{
              backgroundColor: currentView === 'study_assistant' ? 'rgba(56, 189, 248, 0.15)' : 'transparent',
              color: currentView === 'study_assistant' ? '#38bdf8' : '#94a3b8',
              border: currentView === 'study_assistant' ? '1px solid rgba(56, 189, 248, 0.3)' : '1px solid transparent',
              padding: '0.45rem 0.9rem',
              borderRadius: '8px',
              fontSize: '0.82rem',
              fontWeight: 600,
              cursor: 'pointer',
              display: 'flex',
              alignItems: 'center',
              gap: '0.4rem',
              transition: 'all 0.15s ease'
            }}
          >
            <span>📖</span>
            <span>Full Workspace</span>
          </button>

          {onToggleBot && (
            <button
              onClick={onToggleBot}
              title="Toggle Floating AI Study Bot"
              style={{
                backgroundColor: isBotOpen ? 'rgba(99, 102, 241, 0.25)' : 'rgba(56, 189, 248, 0.1)',
                color: isBotOpen ? '#a5b4fc' : '#38bdf8',
                border: isBotOpen ? '1px solid rgba(99, 102, 241, 0.4)' : '1px solid rgba(56, 189, 248, 0.25)',
                padding: '0.45rem 0.85rem',
                borderRadius: '8px',
                fontSize: '0.82rem',
                fontWeight: 700,
                cursor: 'pointer',
                display: 'flex',
                alignItems: 'center',
                gap: '0.35rem',
                transition: 'all 0.15s ease'
              }}
            >
              <span>✨</span>
              <span>{isBotOpen ? 'Bot Open' : 'AI Bot Widget'}</span>
            </button>
          )}
        </div>

        {/* Active Campus Tag */}
        {tenant && (
          <div style={{
            display: 'flex',
            alignItems: 'center',
            gap: '0.5rem',
            backgroundColor: 'rgba(30, 41, 59, 0.6)',
            padding: '0.35rem 0.85rem',
            borderRadius: '8px',
            border: '1px solid rgba(255, 255, 255, 0.08)',
            fontSize: '0.8rem'
          }}>
            <span style={{ width: '6px', height: '6px', borderRadius: '50%', backgroundColor: '#10b981' }} />
            <span style={{ color: '#94a3b8' }}>Campus:</span>
            <span style={{ fontWeight: 600, color: '#f8fafc' }}>{tenant.name}</span>
            <span style={{
              backgroundColor: 'rgba(2, 132, 199, 0.2)',
              color: '#38bdf8',
              border: '1px solid rgba(2, 132, 199, 0.3)',
              padding: '0.1rem 0.45rem',
              borderRadius: '4px',
              fontSize: '0.7rem',
              fontWeight: 700
            }}>
              {tenant.code}
            </span>
          </div>
        )}
      </div>

      {/* User Profile & Actions */}
      {user ? (
        <div style={{ display: 'flex', alignItems: 'center', gap: '1.25rem' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem' }}>
            <div style={{
              width: '36px',
              height: '36px',
              borderRadius: '50%',
              background: 'linear-gradient(135deg, #1e293b 0%, #334155 100%)',
              border: '2px solid rgba(56, 189, 248, 0.4)',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              fontWeight: 700,
              fontSize: '0.82rem',
              color: '#38bdf8'
            }}>
              {getInitials(user.full_name)}
            </div>

            <div style={{ textAlign: 'left' }}>
              <div style={{ fontWeight: 600, fontSize: '0.86rem', color: '#f8fafc' }}>
                {user.full_name}
              </div>
              <div style={{ display: 'flex', alignItems: 'center', gap: '0.4rem', marginTop: '0.1rem' }}>
                <span style={{
                  backgroundColor: badgeStyle.bg,
                  color: badgeStyle.text,
                  border: `1px solid ${badgeStyle.border}`,
                  fontSize: '0.65rem',
                  fontWeight: 700,
                  padding: '0.05rem 0.45rem',
                  borderRadius: '9999px',
                  letterSpacing: '0.02em'
                }}>
                  {user.role.replace('_', ' ')}
                </span>
                <span style={{ fontSize: '0.72rem', color: '#64748b' }}>{user.email}</span>
              </div>
            </div>
          </div>

          <button
            onClick={logout}
            style={{
              backgroundColor: 'rgba(239, 68, 68, 0.1)',
              color: '#fca5a5',
              border: '1px solid rgba(239, 68, 68, 0.25)',
              padding: '0.45rem 0.85rem',
              borderRadius: '8px',
              cursor: 'pointer',
              fontWeight: 600,
              fontSize: '0.8rem',
              transition: 'all 0.15s ease'
            }}
            onMouseOver={(e) => {
              e.currentTarget.style.backgroundColor = 'rgba(239, 68, 68, 0.2)';
              e.currentTarget.style.borderColor = 'rgba(239, 68, 68, 0.5)';
            }}
            onMouseOut={(e) => {
              e.currentTarget.style.backgroundColor = 'rgba(239, 68, 68, 0.1)';
              e.currentTarget.style.borderColor = 'rgba(239, 68, 68, 0.25)';
            }}
          >
            Sign Out
          </button>
        </div>
      ) : (
        <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem' }}>
          <button
            onClick={() => onViewChange('dashboard')}
            style={{
              background: 'linear-gradient(135deg, #0284c7 0%, #0369a1 100%)',
              color: '#ffffff',
              border: '1px solid rgba(56, 189, 248, 0.3)',
              padding: '0.45rem 1rem',
              borderRadius: '8px',
              cursor: 'pointer',
              fontWeight: 700,
              fontSize: '0.82rem',
              display: 'flex',
              alignItems: 'center',
              gap: '0.4rem',
              boxShadow: '0 2px 8px rgba(2, 132, 199, 0.25)'
            }}
          >
            <span>🔐</span>
            <span>Sign In / Demo Accounts</span>
          </button>
        </div>
      )}
    </header>
  );
};
