import React, { useState } from 'react';
import { User, UserRole } from '../types/auth';
import { mockStudentUser, mockFacultyUser } from '../services/mockData';

interface MobileAuthViewProps {
  onSuccess: (user: User) => void;
}

export const MobileAuthView: React.FC<MobileAuthViewProps> = ({ onSuccess }) => {
  const [role, setRole] = useState<UserRole>('student');
  const [email, setEmail] = useState('alex.rivera@unisphere.edu');
  const [password, setPassword] = useState('••••••••');
  const [loading, setLoading] = useState(false);

  const handleRoleSelect = (selectedRole: UserRole) => {
    setRole(selectedRole);
    if (selectedRole === 'faculty') {
      setEmail(mockFacultyUser.email);
    } else {
      setEmail(mockStudentUser.email);
    }
  };

  const handleLogin = (e?: React.FormEvent) => {
    if (e) e.preventDefault();
    setLoading(true);

    setTimeout(() => {
      setLoading(false);
      if (role === 'faculty') {
        onSuccess(mockFacultyUser);
      } else {
        onSuccess(mockStudentUser);
      }
    }, 400);
  };

  const handleQuickDemo = (demoRole: UserRole) => {
    setLoading(true);
    setTimeout(() => {
      setLoading(false);
      onSuccess(demoRole === 'faculty' ? mockFacultyUser : mockStudentUser);
    }, 250);
  };

  return (
    <div style={{
      padding: '2rem 1.5rem',
      display: 'flex',
      flexDirection: 'column',
      justifyContent: 'center',
      minHeight: '100%',
    }}>
      {/* Brand Emblem */}
      <div style={{ textAlign: 'center', marginBottom: '1.75rem' }}>
        <div style={{
          width: '64px',
          height: '64px',
          borderRadius: '18px',
          background: 'linear-gradient(135deg, #2563eb, #0ea5e9)',
          margin: '0 auto 12px',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          fontSize: '2rem',
          fontWeight: 900,
          color: '#ffffff',
          boxShadow: '0 8px 24px rgba(37, 99, 235, 0.4)',
        }}>
          U
        </div>
        <h2 style={{ fontSize: '1.6rem', fontWeight: 800, color: '#f8fafc', letterSpacing: '-0.5px' }}>
          UniSphere <span style={{ color: '#38bdf8' }}>Mobile</span>
        </h2>
        <p style={{ fontSize: '0.85rem', color: '#94a3b8', marginTop: '4px' }}>
          Sign in to access your mobile campus hub
        </p>
      </div>

      {/* Role Toggle Pills */}
      <div style={{
        display: 'flex',
        backgroundColor: 'rgba(15, 23, 42, 0.8)',
        padding: '4px',
        borderRadius: '12px',
        border: '1px solid var(--color-border)',
        marginBottom: '1.25rem',
      }}>
        <button
          type="button"
          onClick={() => handleRoleSelect('student')}
          style={{
            flex: 1,
            padding: '8px',
            border: 'none',
            borderRadius: '9px',
            backgroundColor: role === 'student' ? '#2563eb' : 'transparent',
            color: role === 'student' ? '#ffffff' : '#94a3b8',
            fontSize: '0.825rem',
            fontWeight: 700,
            cursor: 'pointer',
            transition: 'all 0.2s',
          }}
        >
          🎓 Student
        </button>
        <button
          type="button"
          onClick={() => handleRoleSelect('faculty')}
          style={{
            flex: 1,
            padding: '8px',
            border: 'none',
            borderRadius: '9px',
            backgroundColor: role === 'faculty' ? '#6366f1' : 'transparent',
            color: role === 'faculty' ? '#ffffff' : '#94a3b8',
            fontSize: '0.825rem',
            fontWeight: 700,
            cursor: 'pointer',
            transition: 'all 0.2s',
          }}
        >
          👨‍🏫 Faculty
        </button>
      </div>

      {/* Form */}
      <form onSubmit={handleLogin} style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
        <div className="form-group" style={{ marginBottom: 0 }}>
          <label className="form-label" style={{ fontSize: '0.78rem' }}>University Email</label>
          <input
            type="email"
            className="form-input"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
            style={{ padding: '10px 14px', fontSize: '0.875rem' }}
          />
        </div>

        <div className="form-group" style={{ marginBottom: 0 }}>
          <label className="form-label" style={{ fontSize: '0.78rem' }}>Password</label>
          <input
            type="password"
            className="form-input"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
            style={{ padding: '10px 14px', fontSize: '0.875rem' }}
          />
        </div>

        <button
          type="submit"
          disabled={loading}
          className="btn btn-primary"
          style={{
            width: '100%',
            padding: '11px',
            marginTop: '8px',
            fontSize: '0.925rem',
            fontWeight: 700,
            borderRadius: '12px',
          }}
        >
          {loading ? 'Authenticating...' : `Sign In as ${role === 'student' ? 'Student' : 'Faculty'}`}
        </button>
      </form>

      {/* 1-Tap Quick Demo Access */}
      <div style={{ marginTop: '1.5rem', textAlign: 'center' }}>
        <div style={{ fontSize: '0.75rem', color: '#64748b', marginBottom: '10px', textTransform: 'uppercase', letterSpacing: '0.5px' }}>
          Instant 1-Tap Demo Access
        </div>
        <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
          <button
            type="button"
            onClick={() => handleQuickDemo('student')}
            className="btn btn-secondary"
            style={{
              padding: '9px',
              fontSize: '0.8rem',
              borderRadius: '10px',
              border: '1px solid rgba(14, 165, 233, 0.4)',
              color: '#38bdf8',
            }}
          >
            ⚡ Login as Student (Alex Rivera)
          </button>
          <button
            type="button"
            onClick={() => handleQuickDemo('faculty')}
            className="btn btn-secondary"
            style={{
              padding: '9px',
              fontSize: '0.8rem',
              borderRadius: '10px',
              border: '1px solid rgba(99, 102, 241, 0.4)',
              color: '#a5b4fc',
            }}
          >
            ⚡ Login as Faculty (Prof. Vance)
          </button>
        </div>
      </div>
    </div>
  );
};
