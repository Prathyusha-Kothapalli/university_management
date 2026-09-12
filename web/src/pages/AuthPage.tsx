import React, { useState } from 'react';
import { User, UserRole } from '../types/auth';
import { mockStudentUser, mockFacultyUser } from '../services/mockData';

interface AuthPageProps {
  onSuccess?: (user?: any) => void;
}

export const AuthPage: React.FC<AuthPageProps> = ({ onSuccess = () => {} }) => {
  const [isLogin, setIsLogin] = useState(true);
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [name, setName] = useState('');
  const [phone, setPhone] = useState('');
  const [role, setRole] = useState<UserRole>('student');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  const handleLogin = (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);

    if (!email || !password) {
      setError('Please provide both your university email and password.');
      return;
    }

    setLoading(true);
    setTimeout(() => {
      setLoading(false);
      // Determine role based on email or credentials
      if (email.toLowerCase().includes('faculty') || role === 'faculty') {
        onSuccess(mockFacultyUser);
      } else {
        onSuccess({
          ...mockStudentUser,
          email,
          name: email.split('@')[0].replace('.', ' '),
        });
      }
    }, 600);
  };

  const handleRegister = (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);

    if (!name || !email || !password) {
      setError('Please fill out all required fields.');
      return;
    }

    if (password !== confirmPassword) {
      setError('Passwords do not match. Please verify and try again.');
      return;
    }

    if (password.length < 6) {
      setError('Password must be at least 6 characters.');
      return;
    }

    setLoading(true);
    setTimeout(() => {
      setLoading(false);
      const newUser: User = {
        id: `usr_${Date.now()}`,
        name,
        email,
        phone: phone || '+1 (555) 000-0000',
        role,
        department: role === 'student' ? 'Artificial Intelligence & Computer Science' : 'Department of Information Systems',
        studentId: role === 'student' ? `US-2026-${Math.floor(Math.random() * 900) + 100}` : `FAC-ENG-${Math.floor(Math.random() * 90) + 10}`,
        gpa: 3.90,
        attendanceRate: 96.0,
        creditsEarned: 30,
        totalCredits: 120,
      };
      onSuccess(newUser);
    }, 700);
  };

  const autofillDemo = (demoType: 'student' | 'faculty') => {
    if (demoType === 'student') {
      setEmail(mockStudentUser.email);
      setPassword('Password123!');
      setRole('student');
    } else {
      setEmail(mockFacultyUser.email);
      setPassword('ProfPass2026!');
      setRole('faculty');
    }
    setError(null);
  };

  return (
    <div style={{
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      minHeight: 'calc(100vh - 80px)',
      padding: '2rem',
    }}>
      <div className="glass-panel animate-fade-in" style={{
        width: '100%',
        maxWidth: '480px',
        padding: '2.5rem',
        boxShadow: 'var(--shadow-lg)',
      }}>
        {/* Emblem Header */}
        <div style={{ textAlign: 'center', marginBottom: '1.75rem' }}>
          <img
            src="/logo.png"
            alt="UniSphere AI Logo"
            style={{
              width: '72px',
              height: '72px',
              objectFit: 'contain',
              margin: '0 auto 12px',
              filter: 'drop-shadow(0 8px 20px rgba(37, 99, 235, 0.4))',
            }}
          />
          <h2 style={{ fontSize: '1.75rem', fontWeight: 800, color: '#f8fafc', letterSpacing: '-0.5px' }}>
            {isLogin ? 'Welcome Back' : 'Create an Account'}
          </h2>
          <p style={{ fontSize: '0.9rem', color: '#94a3b8', marginTop: '4px' }}>
            {isLogin ? 'Sign in to your UniSphere AI portal' : 'Register for access to campus services & courses'}
          </p>
        </div>

        {/* Auth Tabs */}
        <div style={{
          display: 'flex',
          backgroundColor: 'rgba(15, 23, 42, 0.6)',
          padding: '4px',
          borderRadius: '12px',
          marginBottom: '1.5rem',
          border: '1px solid var(--color-border)',
        }}>
          <button
            type="button"
            onClick={() => { setIsLogin(true); setError(null); }}
            style={{
              flex: 1,
              padding: '8px',
              borderRadius: '8px',
              border: 'none',
              background: isLogin ? 'var(--color-primary)' : 'transparent',
              color: isLogin ? '#fff' : '#94a3b8',
              fontWeight: 600,
              fontSize: '0.875rem',
              cursor: 'pointer',
              transition: 'all 0.2s',
            }}
          >
            Sign In
          </button>
          <button
            type="button"
            onClick={() => { setIsLogin(false); setError(null); }}
            style={{
              flex: 1,
              padding: '8px',
              borderRadius: '8px',
              border: 'none',
              background: !isLogin ? 'var(--color-primary)' : 'transparent',
              color: !isLogin ? '#fff' : '#94a3b8',
              fontWeight: 600,
              fontSize: '0.875rem',
              cursor: 'pointer',
              transition: 'all 0.2s',
            }}
          >
            Register
          </button>
        </div>

        {/* Error Notification */}
        {error && (
          <div style={{
            padding: '10px 14px',
            backgroundColor: 'var(--color-error-bg)',
            border: '1px solid rgba(239, 68, 68, 0.3)',
            borderRadius: '10px',
            color: '#fca5a5',
            fontSize: '0.85rem',
            marginBottom: '1.25rem',
            display: 'flex',
            alignItems: 'center',
            gap: '8px',
          }}>
            <span>⚠️</span>
            <span>{error}</span>
          </div>
        )}

        {/* Login / Register Form */}
        <form onSubmit={isLogin ? handleLogin : handleRegister}>
          {!isLogin && (
            <>
              <div className="form-group">
                <label className="form-label">Account Role</label>
                <div style={{ display: 'flex', gap: '8px' }}>
                  {(['student', 'faculty'] as UserRole[]).map((r) => (
                    <button
                      key={r}
                      type="button"
                      onClick={() => setRole(r)}
                      style={{
                        flex: 1,
                        padding: '8px',
                        borderRadius: '8px',
                        border: role === r ? '1.5px solid #38bdf8' : '1px solid var(--color-border)',
                        background: role === r ? 'rgba(56, 189, 248, 0.15)' : 'rgba(15, 23, 42, 0.5)',
                        color: role === r ? '#38bdf8' : '#94a3b8',
                        fontWeight: 600,
                        fontSize: '0.85rem',
                        cursor: 'pointer',
                        textTransform: 'capitalize',
                      }}
                    >
                      {r === 'student' ? 'Student 🎓' : 'Faculty 👨‍🏫'}
                    </button>
                  ))}
                </div>
              </div>

              <div className="form-group">
                <label className="form-label">Full Name</label>
                <input
                  type="text"
                  className="form-input"
                  placeholder="e.g. Jordan Miller"
                  value={name}
                  onChange={(e) => setName(e.target.value)}
                  required
                />
              </div>

              <div className="form-group">
                <label className="form-label">Phone Number</label>
                <input
                  type="tel"
                  className="form-input"
                  placeholder="+1 (555) 012-3456"
                  value={phone}
                  onChange={(e) => setPhone(e.target.value)}
                />
              </div>
            </>
          )}

          <div className="form-group">
            <label className="form-label">University Email</label>
            <input
              type="email"
              className="form-input"
              placeholder="username@university.edu"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
          </div>

          <div className="form-group">
            <label className="form-label">Password</label>
            <input
              type="password"
              className="form-input"
              placeholder="••••••••"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </div>

          {!isLogin && (
            <div className="form-group">
              <label className="form-label">Confirm Password</label>
              <input
                type="password"
                className="form-input"
                placeholder="Re-enter your password"
                value={confirmPassword}
                onChange={(e) => setConfirmPassword(e.target.value)}
                required
              />
            </div>
          )}

          <button
            type="submit"
            className="btn btn-primary"
            disabled={loading}
            style={{ width: '100%', marginTop: '0.5rem', padding: '12px' }}
          >
            {loading ? 'Authenticating...' : isLogin ? 'Sign In to Portal' : 'Create Account'}
          </button>
        </form>

        {/* Quick Demo Autofill Section */}
        <div style={{
          marginTop: '1.75rem',
          padding: '12px',
          borderRadius: '12px',
          backgroundColor: 'rgba(15, 23, 42, 0.4)',
          border: '1px solid var(--color-border-subtle)',
          textAlign: 'center',
        }}>
          <div style={{ fontSize: '0.78rem', color: '#94a3b8', fontWeight: 600, marginBottom: '8px' }}>
            ⚡ Quick 1-Click Demo Login
          </div>
          <div style={{ display: 'flex', gap: '8px' }}>
            <button
              type="button"
              onClick={() => {
                autofillDemo('student');
                onSuccess(mockStudentUser);
              }}
              className="btn btn-secondary"
              style={{ flex: 1, padding: '6px 10px', fontSize: '0.78rem' }}
            >
              🎓 Student Demo
            </button>
            <button
              type="button"
              onClick={() => {
                autofillDemo('faculty');
                onSuccess(mockFacultyUser);
              }}
              className="btn btn-secondary"
              style={{ flex: 1, padding: '6px 10px', fontSize: '0.78rem' }}
            >
              👨‍🏫 Faculty Demo
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};
