import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../hooks/useAuth';
import { UserRole } from '../types';
import { useTheme } from '../hooks/useTheme';
import { useToast } from '../hooks/useToast';
import { Modal } from './Modal';
import { Bell, Sun, Moon, LogOut, User as UserIcon, RefreshCw, Search, Command, ArrowRight } from 'lucide-react';

export const Navbar: React.FC = () => {
  const { user, role, logout, switchRole } = useAuth();
  const { theme, toggleTheme } = useTheme();
  const { showToast } = useToast();
  const navigate = useNavigate();

  const [showNotifications, setShowNotifications] = useState(false);
  const [isCommandPaletteOpen, setIsCommandPaletteOpen] = useState(false);
  const [cmdSearchQuery, setCmdSearchQuery] = useState('');

  // Keyboard shortcut Ctrl+K / Cmd+K listener
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
        e.preventDefault();
        setIsCommandPaletteOpen((prev) => !prev);
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, []);

  const handleRoleToggle = () => {
    const nextRole: UserRole = role === 'student' ? 'faculty' : role === 'faculty' ? 'hod' : role === 'hod' ? 'parent' : role === 'parent' ? 'librarian' : role === 'librarian' ? 'admin' : 'student';
    switchRole(nextRole);
    const targetPath =
      nextRole === 'admin'
        ? '/admin/dashboard'
        : nextRole === 'faculty'
        ? '/faculty/dashboard'
        : nextRole === 'hod'
        ? '/hod/dashboard'
        : nextRole === 'parent'
        ? '/parent/dashboard'
        : nextRole === 'librarian'
        ? '/librarian/dashboard'
        : '/dashboard';
    navigate(targetPath);
    showToast(`Switched active portal view to ${nextRole.toUpperCase()}`, 'info');
  };

  const handleLogout = () => {
    logout();
    showToast('Signed out of UniSphere AI', 'info');
    navigate('/login');
  };

  const quickNavLinks = [
    { label: 'Dashboard & KPIs', path: '/dashboard', cat: 'Overview' },
    { label: 'Parent & Guardian Portal', path: '/parent/dashboard', cat: 'Parent Portal' },
    { label: 'HOD Department Portal', path: '/hod/dashboard', cat: 'Management' },
    { label: 'Librarian Operations Dashboard', path: '/librarian/dashboard', cat: 'Management' },
    { label: 'Academics & Courses', path: '/academics', cat: 'Academics' },
    { label: 'Assignments & Study Notes', path: '/learning', cat: 'Learning' },
    { label: 'Exams, Grades & Transcripts', path: '/exams', cat: 'Exams' },
    { label: 'Fee Structures & Payment Gateway', path: '/finance', cat: 'Finance' },
    { label: 'Library Catalog Search', path: '/library', cat: 'Library' },
    { label: 'Hostel & Transport Services', path: '/facilities', cat: 'Facilities' },
    { label: 'Placement Drives Directory', path: '/placements', cat: 'Careers' },
    { label: 'AI Assistant Copilot', path: '/ai', cat: 'AI Tools' },
    { label: 'User Profile & Document Vault', path: '/profile', cat: 'Profile' },
  ];

  const filteredNavLinks = quickNavLinks.filter((link) =>
    link.label.toLowerCase().includes(cmdSearchQuery.toLowerCase()) ||
    link.cat.toLowerCase().includes(cmdSearchQuery.toLowerCase())
  );

  return (
    <header
      style={{
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'space-between',
        padding: '0.75rem 1.75rem',
        backgroundColor: 'rgba(15, 23, 42, 0.95)',
        backdropFilter: 'blur(16px)',
        borderBottom: '1px solid rgba(255, 255, 255, 0.08)',
        position: 'sticky',
        top: 0,
        zIndex: 100,
        height: '65px',
      }}
    >
      {/* Brand Logo & Name */}
      <div
        onClick={() => navigate('/dashboard')}
        style={{ display: 'flex', alignItems: 'center', gap: '12px', cursor: 'pointer' }}
      >
        <img
          src="/logo.png"
          alt="UniSphere AI Logo"
          style={{
            width: '38px',
            height: '38px',
            objectFit: 'contain',
            filter: 'drop-shadow(0 4px 10px rgba(37, 99, 235, 0.5))',
          }}
        />
        <div>
          <div style={{ fontWeight: 800, fontSize: '1.15rem', color: '#f8fafc', letterSpacing: '-0.3px' }}>
            UniSphere <span style={{ color: '#38bdf8' }}>AI</span>
          </div>
          <div style={{ fontSize: '0.7rem', color: '#94a3b8', letterSpacing: '0.3px' }}>
            Smart Campus SPA Portal
          </div>
        </div>
      </div>

      {/* Center Command Palette Search Bar */}
      {user && (
        <nav style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
          {(user.role === 'faculty'
            ? [
                { id: 'dashboard', label: 'Dashboard' },
                { id: 'courses', label: 'Teaching Courses' },
                { id: 'schedule', label: 'Timetable' },
                { id: 'announcements', label: 'Announcements 📢' },
                { id: 'profile', label: 'My Profile' },
              ]
            : [
                { id: 'dashboard', label: 'Dashboard' },
                { id: 'courses', label: 'Courses' },
                { id: 'schedule', label: 'Timetable' },
                { id: 'placements', label: 'Placements 💼' },
                { id: 'announcements', label: 'Announcements 📢' },
                { id: 'profile', label: 'My Profile' },
              ]
          ).map((item) => (
            <button
              onClick={toggleTheme}
              title={`Switch to ${theme === 'dark' ? 'Light' : 'Dark'} mode`}
              style={{
                background: currentView === item.id ? 'rgba(37, 99, 235, 0.2)' : 'transparent',
                color: currentView === item.id ? '#38bdf8' : '#94a3b8',
                border: currentView === item.id ? '1px solid rgba(56, 189, 248, 0.3)' : '1px solid transparent',
                padding: '7px 14px',
                borderRadius: '8px',
                fontSize: '0.85rem',
                fontWeight: currentView === item.id ? 700 : 500,
                cursor: 'pointer',
                transition: 'all 0.2s',
                whiteSpace: 'nowrap',
              }}
            >
              {theme === 'dark' ? <Sun size={16} /> : <Moon size={16} />}
            </button>

            {/* Notifications Button */}
            <div style={{ position: 'relative' }}>
              <button
                onClick={() => setShowNotifications(!showNotifications)}
                style={{
                  background: 'rgba(255, 255, 255, 0.05)',
                  border: '1px solid rgba(255, 255, 255, 0.1)',
                  color: '#e2e8f0',
                  padding: '7px',
                  borderRadius: '8px',
                  cursor: 'pointer',
                  display: 'flex',
                  alignItems: 'center',
                  position: 'relative',
                }}
              >
                <Bell size={16} />
                <span
                  style={{
                    position: 'absolute',
                    top: '4px',
                    right: '4px',
                    width: '8px',
                    height: '8px',
                    borderRadius: '50%',
                    backgroundColor: '#ef4444',
                  }}
                />
              </button>

              {/* Notifications Dropdown */}
              {showNotifications && (
                <div
                  style={{
                    position: 'absolute',
                    top: '42px',
                    right: 0,
                    width: '300px',
                    backgroundColor: '#0f172a',
                    border: '1px solid rgba(255, 255, 255, 0.12)',
                    borderRadius: '12px',
                    boxShadow: '0 10px 30px rgba(0,0,0,0.5)',
                    padding: '12px',
                    zIndex: 200,
                  }}
                >
                  <div style={{ fontWeight: 700, fontSize: '0.85rem', color: '#f8fafc', marginBottom: '8px', borderBottom: '1px solid rgba(255,255,255,0.08)', paddingBottom: '6px' }}>
                    Notifications
                  </div>
                  <div style={{ display: 'flex', flexDirection: 'column', gap: '8px', fontSize: '0.8rem' }}>
                    <div style={{ color: '#cbd5e1', padding: '6px', borderRadius: '6px', background: 'rgba(255,255,255,0.03)' }}>
                      <strong>CS301 Assignment Posted</strong>
                      <div style={{ fontSize: '0.72rem', color: '#94a3b8' }}>Due in 5 days</div>
                    </div>
                    <div style={{ color: '#cbd5e1', padding: '6px', borderRadius: '6px', background: 'rgba(255,255,255,0.03)' }}>
                      <strong>Placement Drive Registered</strong>
                      <div style={{ fontSize: '0.72rem', color: '#94a3b8' }}>Google AI Systems Engineer</div>
                    </div>
                  </div>
                </div>
              )}
            </div>

            {/* User Profile Pill */}
            <div
              onClick={() => navigate('/profile')}
              style={{
                display: 'flex',
                alignItems: 'center',
                gap: '10px',
                cursor: 'pointer',
                padding: '4px 10px',
                borderRadius: '24px',
                background: 'rgba(255, 255, 255, 0.05)',
                border: '1px solid rgba(255, 255, 255, 0.08)',
              }}
            >
              <div
                style={{
                  width: '30px',
                  height: '30px',
                  borderRadius: '50%',
                  background: '#2563eb',
                  color: '#ffffff',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  fontWeight: 700,
                  fontSize: '0.85rem',
                }}
              >
                {user.full_name ? user.full_name.charAt(0) : <UserIcon size={16} />}
              </div>
              <div style={{ textAlign: 'left', display: 'flex', flexDirection: 'column' }}>
                <span style={{ fontSize: '0.85rem', fontWeight: 600, color: '#f8fafc' }}>
                  {user.full_name || user.name || 'User'}
                </span>
                <span style={{ fontSize: '0.68rem', color: '#94a3b8' }}>
                  {user.studentId || user.email}
                </span>
              </div>
            </div>

            {/* Logout Button */}
            <button
              onClick={handleLogout}
              title="Sign Out"
              style={{
                background: 'rgba(239, 68, 68, 0.15)',
                border: '1px solid rgba(239, 68, 68, 0.3)',
                color: '#f87171',
                padding: '7px 12px',
                borderRadius: '8px',
                cursor: 'pointer',
                display: 'flex',
                alignItems: 'center',
                gap: '6px',
                fontSize: '0.8rem',
                fontWeight: 600,
              }}
            >
              <LogOut size={15} />
              <span>Exit</span>
            </button>
          </>
        )}
      </div>

      {/* Global Command Palette Modal */}
      <Modal
        isOpen={isCommandPaletteOpen}
        onClose={() => setIsCommandPaletteOpen(false)}
        title="UniSphere Command Palette"
        maxWidth="500px"
      >
        <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
          <div style={{ position: 'relative', display: 'flex', alignItems: 'center' }}>
            <Search size={16} style={{ position: 'absolute', left: '12px', color: '#38bdf8' }} />
            <input
              type="text"
              autoFocus
              placeholder="Search page or command..."
              value={cmdSearchQuery}
              onChange={(e) => setCmdSearchQuery(e.target.value)}
              style={{
                width: '100%',
                padding: '10px 12px 10px 38px',
                backgroundColor: 'rgba(15, 23, 42, 0.9)',
                border: '1px solid rgba(56, 189, 248, 0.4)',
                borderRadius: '10px',
                color: '#f8fafc',
                fontSize: '0.9rem',
                outline: 'none',
              }}
            />
          </div>

          <div style={{ display: 'flex', flexDirection: 'column', gap: '6px', maxHeight: '300px', overflowY: 'auto' }}>
            {filteredNavLinks.map((item, idx) => (
              <button
                key={idx}
                onClick={() => {
                  setIsCommandPaletteOpen(false);
                  navigate(item.path);
                }}
                style={{
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'space-between',
                  padding: '10px 12px',
                  borderRadius: '8px',
                  border: '1px solid rgba(255, 255, 255, 0.05)',
                  backgroundColor: 'rgba(255, 255, 255, 0.02)',
                  color: '#e2e8f0',
                  fontSize: '0.85rem',
                  cursor: 'pointer',
                  textAlign: 'left',
                }}
              >
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                  <Command size={14} style={{ color: '#a855f7' }} />
                  <span>{item.label}</span>
                </div>
                <span style={{ fontSize: '0.75rem', color: '#38bdf8', display: 'flex', alignItems: 'center', gap: '4px' }}>
                  {item.cat} <ArrowRight size={12} />
                </span>
              </button>
            ))}
          </div>
        </div>
      </Modal>
    </header>
  );
};
