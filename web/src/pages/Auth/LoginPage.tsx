import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../../hooks/useAuth';
import { useToast } from '../../hooks/useToast';
import { Button } from '../../components/Button';
import { UserRole } from '../../types';
import { Lock, Mail, ShieldCheck, UserCheck, GraduationCap } from 'lucide-react';

export const LoginPage: React.FC = () => {
  const { login, switchRole } = useAuth();
  const { showToast } = useToast();
  const navigate = useNavigate();

  const [email, setEmail] = useState('alex.morgan@unisphere.edu');
  const [password, setPassword] = useState('password123');
  const [selectedRole, setSelectedRole] = useState<UserRole>('student');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    try {
      await login(email, password);
      switchRole(selectedRole);
      showToast(`Welcome back! Logged in as ${selectedRole.toUpperCase()}.`, 'success');
      navigate('/dashboard');
    } catch (err) {
      showToast('Authentication failed. Please check your credentials.', 'error');
    } finally {
      setLoading(false);
    }
  };

  const handleDemoFill = (role: UserRole) => {
    setSelectedRole(role);
    if (role === 'student') {
      setEmail('alex.morgan@unisphere.edu');
    } else if (role === 'faculty') {
      setEmail('sarah.jenkins@unisphere.edu');
    } else {
      setEmail('admin@unisphere.edu');
    }
  };

  return (
    <div
      style={{
        minHeight: '100vh',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        background: 'radial-gradient(circle at 50% 30%, rgba(37, 99, 235, 0.15), rgba(15, 23, 42, 1) 70%)',
        padding: '1.5rem',
      }}
    >
      <div
        style={{
          width: '100%',
          maxWidth: '440px',
          backgroundColor: 'rgba(15, 23, 42, 0.85)',
          backdropFilter: 'blur(20px)',
          border: '1px solid rgba(255, 255, 255, 0.12)',
          borderRadius: '20px',
          padding: '2.5rem 2rem',
          boxShadow: '0 25px 60px rgba(0, 0, 0, 0.6)',
        }}
      >
        {/* Header */}
        <div style={{ textAlign: 'center', marginBottom: '2rem' }}>
          <img
            src="/logo.png"
            alt="UniSphere AI Logo"
            style={{
              width: '72px',
              height: '72px',
              objectFit: 'contain',
              margin: '0 auto 12px auto',
              filter: 'drop-shadow(0 8px 20px rgba(37, 99, 235, 0.5))',
            }}
          />
          <h2 style={{ margin: 0, fontSize: '1.6rem', fontWeight: 800, color: '#f8fafc' }}>
            UniSphere <span style={{ color: '#38bdf8' }}>AI</span>
          </h2>
          <p style={{ margin: '6px 0 0 0', fontSize: '0.85rem', color: '#94a3b8' }}>
            Enterprise Multi-Tenant Campus Management System
          </p>
        </div>

        {/* Role Selection Tabs */}
        <div
          style={{
            display: 'flex',
            backgroundColor: 'rgba(255, 255, 255, 0.04)',
            padding: '4px',
            borderRadius: '12px',
            marginBottom: '1.5rem',
            border: '1px solid rgba(255, 255, 255, 0.08)',
          }}
        >
          {[
            { id: 'student', label: 'Student', icon: <GraduationCap size={15} /> },
            { id: 'faculty', label: 'Faculty', icon: <UserCheck size={15} /> },
            { id: 'admin', label: 'Admin', icon: <ShieldCheck size={15} /> },
          ].map((item) => (
            <button
              key={item.id}
              type="button"
              onClick={() => handleDemoFill(item.id as UserRole)}
              style={{
                flex: 1,
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                gap: '6px',
                padding: '8px 10px',
                borderRadius: '8px',
                border: 'none',
                backgroundColor: selectedRole === item.id ? '#2563eb' : 'transparent',
                color: selectedRole === item.id ? '#ffffff' : '#94a3b8',
                fontSize: '0.8rem',
                fontWeight: 600,
                cursor: 'pointer',
                transition: 'all 0.15s ease',
              }}
            >
              {item.icon}
              <span>{item.label}</span>
            </button>
          ))}
        </div>

        {/* Form */}
        <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '1.25rem' }}>
          <div>
            <label style={{ display: 'block', fontSize: '0.8rem', fontWeight: 600, color: '#cbd5e1', marginBottom: '6px' }}>
              University Email / Username
            </label>
            <div style={{ position: 'relative', display: 'flex', alignItems: 'center' }}>
              <Mail size={16} style={{ position: 'absolute', left: '12px', color: '#64748b' }} />
              <input
                type="email"
                required
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                style={{
                  width: '100%',
                  padding: '10px 12px 10px 38px',
                  backgroundColor: 'rgba(15, 23, 42, 0.7)',
                  border: '1px solid rgba(255, 255, 255, 0.12)',
                  borderRadius: '10px',
                  color: '#f8fafc',
                  fontSize: '0.9rem',
                  outline: 'none',
                }}
              />
            </div>
          </div>

          <div>
            <label style={{ display: 'block', fontSize: '0.8rem', fontWeight: 600, color: '#cbd5e1', marginBottom: '6px' }}>
              Password
            </label>
            <div style={{ position: 'relative', display: 'flex', alignItems: 'center' }}>
              <Lock size={16} style={{ position: 'absolute', left: '12px', color: '#64748b' }} />
              <input
                type="password"
                required
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                style={{
                  width: '100%',
                  padding: '10px 12px 10px 38px',
                  backgroundColor: 'rgba(15, 23, 42, 0.7)',
                  border: '1px solid rgba(255, 255, 255, 0.12)',
                  borderRadius: '10px',
                  color: '#f8fafc',
                  fontSize: '0.9rem',
                  outline: 'none',
                }}
              />
            </div>
          </div>

          <Button type="submit" variant="primary" size="lg" isLoading={loading} style={{ marginTop: '0.5rem', width: '100%' }}>
            Sign In to Campus Portal
          </Button>
        </form>

        <div style={{ textAlign: 'center', marginTop: '1.5rem', fontSize: '0.75rem', color: '#64748b' }}>
          Connects to FastAPI Backend at <code style={{ color: '#38bdf8' }}>http://localhost:8000/api/v1</code>
        </div>
      </div>
    </div>
  );
};
