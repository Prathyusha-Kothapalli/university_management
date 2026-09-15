import React, { useState } from 'react';
import { useAuth } from '../features/auth/AuthContext';

export const LoginForm: React.FC = () => {
  const { login, registerTenant, error, clearError } = useAuth();
  const [activeTab, setActiveTab] = useState<'login' | 'register-tenant'>('login');
  const [isLoading, setIsLoading] = useState(false);

  // Login state
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [tenantCode, setTenantCode] = useState('');

  // Register Tenant state
  const [tenantName, setTenantName] = useState('');
  const [regTenantCode, setRegTenantCode] = useState('');
  const [tenantDomain, setTenantDomain] = useState('');
  const [adminEmail, setAdminEmail] = useState('');
  const [adminPassword, setAdminPassword] = useState('');
  const [adminName, setAdminName] = useState('');

  const handleLoginSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsLoading(true);
    try {
      await login(email, password, tenantCode || undefined);
    } catch {
      // handled in context
    } finally {
      setIsLoading(false);
    }
  };

  const handleRegisterTenantSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsLoading(true);
    try {
      await registerTenant({
        tenant_name: tenantName,
        tenant_code: regTenantCode,
        tenant_domain: tenantDomain || undefined,
        admin_email: adminEmail,
        admin_password: adminPassword,
        admin_name: adminName,
      });
    } catch {
      // handled in context
    } finally {
      setIsLoading(false);
    }
  };

  const handleDemoQuickLogin = (demoEmail: string, demoPass: string, code?: string) => {
    clearError();
    setEmail(demoEmail);
    setPassword(demoPass);
    setTenantCode(code || '');
    login(demoEmail, demoPass, code);
  };

  return (
    <div style={{
      minHeight: 'calc(100vh - 61px)',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      padding: '3rem 1.5rem',
      position: 'relative'
    }}>
      <div style={{
        maxWidth: '540px',
        width: '100%',
        backgroundColor: 'rgba(14, 21, 38, 0.85)',
        backdropFilter: 'blur(20px)',
        WebkitBackdropFilter: 'blur(20px)',
        borderRadius: '20px',
        border: '1px solid rgba(255, 255, 255, 0.12)',
        boxShadow: '0 25px 50px -12px rgba(0, 0, 0, 0.6), 0 0 35px rgba(2, 132, 199, 0.15)',
        overflow: 'hidden'
      }}>
        {/* Top University Brand Bar */}
        <div style={{
          padding: '2rem 2rem 1.25rem 2rem',
          textAlign: 'center',
          borderBottom: '1px solid rgba(255, 255, 255, 0.08)',
          background: 'linear-gradient(180deg, rgba(2, 132, 199, 0.1) 0%, transparent 100%)'
        }}>
          <div style={{
            width: '52px',
            height: '52px',
            borderRadius: '14px',
            background: 'linear-gradient(135deg, #0284c7 0%, #6366f1 100%)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            fontWeight: 800,
            fontSize: '1.5rem',
            color: '#ffffff',
            margin: '0 auto 0.85rem auto',
            boxShadow: '0 8px 20px rgba(2, 132, 199, 0.4), 0 0 15px rgba(99, 102, 241, 0.3)'
          }}>
            🎓
          </div>
          <h1 style={{ fontSize: '1.5rem', fontWeight: 800, color: '#f8fafc', margin: '0 0 0.3rem 0', letterSpacing: '-0.02em' }}>
            UniSphere<span style={{ color: '#38bdf8' }}> Enterprise</span>
          </h1>
          <p style={{ color: '#94a3b8', fontSize: '0.86rem', margin: 0, fontWeight: 500 }}>
            Unified Academic Portal & Multi-Tenant AI Platform
          </p>
        </div>

        {/* Tab Toggle */}
        <div style={{
          display: 'flex',
          margin: '1.25rem 1.75rem 0 1.75rem',
          backgroundColor: 'rgba(2, 6, 23, 0.6)',
          padding: '0.3rem',
          borderRadius: '12px',
          border: '1px solid rgba(255, 255, 255, 0.08)'
        }}>
          <button
            type="button"
            onClick={() => { setActiveTab('login'); clearError(); }}
            style={{
              flex: 1,
              padding: '0.65rem',
              backgroundColor: activeTab === 'login' ? 'rgba(56, 189, 248, 0.18)' : 'transparent',
              color: activeTab === 'login' ? '#38bdf8' : '#94a3b8',
              fontWeight: 700,
              fontSize: '0.84rem',
              border: activeTab === 'login' ? '1px solid rgba(56, 189, 248, 0.35)' : '1px solid transparent',
              borderRadius: '8px',
              cursor: 'pointer',
              transition: 'all 0.15s ease'
            }}
          >
            Institutional Sign In
          </button>
          <button
            type="button"
            onClick={() => { setActiveTab('register-tenant'); clearError(); }}
            style={{
              flex: 1,
              padding: '0.65rem',
              backgroundColor: activeTab === 'register-tenant' ? 'rgba(56, 189, 248, 0.18)' : 'transparent',
              color: activeTab === 'register-tenant' ? '#38bdf8' : '#94a3b8',
              fontWeight: 700,
              fontSize: '0.84rem',
              border: activeTab === 'register-tenant' ? '1px solid rgba(56, 189, 248, 0.35)' : '1px solid transparent',
              borderRadius: '8px',
              cursor: 'pointer',
              transition: 'all 0.15s ease'
            }}
          >
            Onboard New Campus
          </button>
        </div>

        <div style={{ padding: '1.5rem 1.75rem 2rem 1.75rem' }}>
          {error && (
            <div style={{
              backgroundColor: 'rgba(239, 68, 68, 0.12)',
              border: '1px solid rgba(239, 68, 68, 0.4)',
              color: '#fca5a5',
              padding: '0.85rem 1rem',
              borderRadius: '10px',
              marginBottom: '1.25rem',
              fontSize: '0.84rem',
              display: 'flex',
              alignItems: 'center',
              gap: '0.5rem'
            }}>
              <span>⚠️</span>
              <span>{error}</span>
            </div>
          )}

          {activeTab === 'login' ? (
            <form onSubmit={handleLoginSubmit}>
              <div style={{ marginBottom: '1rem' }}>
                <label style={{ display: 'block', fontSize: '0.8rem', fontWeight: 600, color: '#cbd5e1', marginBottom: '0.35rem' }}>
                  Institutional Email Address
                </label>
                <input
                  type="email"
                  required
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  placeholder="name@stanford.edu or admin@unisphere.ai"
                  style={{
                    width: '100%',
                    padding: '0.75rem 0.95rem',
                    backgroundColor: 'rgba(2, 6, 23, 0.7)',
                    border: '1px solid rgba(255, 255, 255, 0.12)',
                    borderRadius: '10px',
                    color: '#f8fafc',
                    outline: 'none',
                    fontSize: '0.88rem',
                    transition: 'border-color 0.2s, box-shadow 0.2s'
                  }}
                  onFocus={(e) => {
                    e.target.style.borderColor = '#38bdf8';
                    e.target.style.boxShadow = '0 0 12px rgba(56, 189, 248, 0.2)';
                  }}
                  onBlur={(e) => {
                    e.target.style.borderColor = 'rgba(255, 255, 255, 0.12)';
                    e.target.style.boxShadow = 'none';
                  }}
                />
              </div>

              <div style={{ marginBottom: '1rem' }}>
                <label style={{ display: 'block', fontSize: '0.8rem', fontWeight: 600, color: '#cbd5e1', marginBottom: '0.35rem' }}>
                  Password
                </label>
                <input
                  type="password"
                  required
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  placeholder="••••••••••••"
                  style={{
                    width: '100%',
                    padding: '0.75rem 0.95rem',
                    backgroundColor: 'rgba(2, 6, 23, 0.7)',
                    border: '1px solid rgba(255, 255, 255, 0.12)',
                    borderRadius: '10px',
                    color: '#f8fafc',
                    outline: 'none',
                    fontSize: '0.88rem',
                    transition: 'border-color 0.2s, box-shadow 0.2s'
                  }}
                  onFocus={(e) => {
                    e.target.style.borderColor = '#38bdf8';
                    e.target.style.boxShadow = '0 0 12px rgba(56, 189, 248, 0.2)';
                  }}
                  onBlur={(e) => {
                    e.target.style.borderColor = 'rgba(255, 255, 255, 0.12)';
                    e.target.style.boxShadow = 'none';
                  }}
                />
              </div>

              <div style={{ marginBottom: '1.25rem' }}>
                <label style={{ display: 'block', fontSize: '0.8rem', fontWeight: 600, color: '#cbd5e1', marginBottom: '0.35rem' }}>
                  Campus / Tenant Code <span style={{ color: '#64748b', fontWeight: 400 }}>(e.g. STANFORD, MIT)</span>
                </label>
                <input
                  type="text"
                  value={tenantCode}
                  onChange={(e) => setTenantCode(e.target.value)}
                  placeholder="STANFORD"
                  style={{
                    width: '100%',
                    padding: '0.75rem 0.95rem',
                    backgroundColor: 'rgba(2, 6, 23, 0.7)',
                    border: '1px solid rgba(255, 255, 255, 0.12)',
                    borderRadius: '10px',
                    color: '#f8fafc',
                    outline: 'none',
                    fontSize: '0.88rem',
                    transition: 'border-color 0.2s, box-shadow 0.2s'
                  }}
                  onFocus={(e) => {
                    e.target.style.borderColor = '#38bdf8';
                    e.target.style.boxShadow = '0 0 12px rgba(56, 189, 248, 0.2)';
                  }}
                  onBlur={(e) => {
                    e.target.style.borderColor = 'rgba(255, 255, 255, 0.12)';
                    e.target.style.boxShadow = 'none';
                  }}
                />
              </div>

              <button
                type="submit"
                disabled={isLoading}
                style={{
                  width: '100%',
                  padding: '0.85rem',
                  background: 'linear-gradient(135deg, #0284c7 0%, #0369a1 100%)',
                  color: '#ffffff',
                  border: '1px solid rgba(56, 189, 248, 0.4)',
                  borderRadius: '10px',
                  fontWeight: 700,
                  fontSize: '0.92rem',
                  cursor: isLoading ? 'not-allowed' : 'pointer',
                  opacity: isLoading ? 0.6 : 1,
                  marginBottom: '1.5rem',
                  boxShadow: '0 4px 16px rgba(2, 132, 199, 0.35)',
                  transition: 'all 0.15s ease'
                }}
              >
                {isLoading ? 'Authenticating...' : 'Sign In to Campus'}
              </button>

              {/* Curated Demo Switcher */}
              <div style={{ borderTop: '1px solid rgba(255, 255, 255, 0.08)', paddingTop: '1.25rem' }}>
                <div style={{
                  fontSize: '0.72rem',
                  color: '#94a3b8',
                  textTransform: 'uppercase',
                  letterSpacing: '0.06em',
                  marginBottom: '0.75rem',
                  textAlign: 'center',
                  fontWeight: 700
                }}>
                  Instant Role Sandbox (1-Click)
                </div>

                <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '0.55rem' }}>
                  <button
                    type="button"
                    onClick={() => handleDemoQuickLogin('john.doe@stanford.edu', 'Student@123', 'STANFORD')}
                    style={{
                      padding: '0.7rem 0.8rem',
                      backgroundColor: 'rgba(16, 185, 129, 0.08)',
                      border: '1px solid rgba(16, 185, 129, 0.35)',
                      color: '#6ee7b7',
                      borderRadius: '10px',
                      fontSize: '0.78rem',
                      cursor: 'pointer',
                      fontWeight: 600,
                      textAlign: 'left',
                      transition: 'all 0.15s ease'
                    }}
                    onMouseOver={(e) => (e.currentTarget.style.backgroundColor = 'rgba(16, 185, 129, 0.16)')}
                    onMouseOut={(e) => (e.currentTarget.style.backgroundColor = 'rgba(16, 185, 129, 0.08)')}
                  >
                    <div style={{ fontWeight: 700, display: 'flex', alignItems: 'center', gap: '0.3rem' }}>
                      <span>🧑‍🎓</span>
                      <span>Student</span>
                    </div>
                    <div style={{ fontSize: '0.68rem', color: '#94a3b8', marginTop: '0.15rem' }}>Stanford CS Dept</div>
                  </button>

                  <button
                    type="button"
                    onClick={() => handleDemoQuickLogin('prof.alan@stanford.edu', 'Faculty@123', 'STANFORD')}
                    style={{
                      padding: '0.7rem 0.8rem',
                      backgroundColor: 'rgba(59, 130, 246, 0.08)',
                      border: '1px solid rgba(59, 130, 246, 0.35)',
                      color: '#93c5fd',
                      borderRadius: '10px',
                      fontSize: '0.78rem',
                      cursor: 'pointer',
                      fontWeight: 600,
                      textAlign: 'left',
                      transition: 'all 0.15s ease'
                    }}
                    onMouseOver={(e) => (e.currentTarget.style.backgroundColor = 'rgba(59, 130, 246, 0.16)')}
                    onMouseOut={(e) => (e.currentTarget.style.backgroundColor = 'rgba(59, 130, 246, 0.08)')}
                  >
                    <div style={{ fontWeight: 700, display: 'flex', alignItems: 'center', gap: '0.3rem' }}>
                      <span>👨‍🏫</span>
                      <span>Faculty</span>
                    </div>
                    <div style={{ fontSize: '0.68rem', color: '#94a3b8', marginTop: '0.15rem' }}>Prof. Alan Turing</div>
                  </button>

                  <button
                    type="button"
                    onClick={() => handleDemoQuickLogin('admin@stanford.edu', 'Admin@123', 'STANFORD')}
                    style={{
                      padding: '0.7rem 0.8rem',
                      backgroundColor: 'rgba(245, 158, 11, 0.08)',
                      border: '1px solid rgba(245, 158, 11, 0.35)',
                      color: '#fcd34d',
                      borderRadius: '10px',
                      fontSize: '0.78rem',
                      cursor: 'pointer',
                      fontWeight: 600,
                      textAlign: 'left',
                      transition: 'all 0.15s ease'
                    }}
                    onMouseOver={(e) => (e.currentTarget.style.backgroundColor = 'rgba(245, 158, 11, 0.16)')}
                    onMouseOut={(e) => (e.currentTarget.style.backgroundColor = 'rgba(245, 158, 11, 0.08)')}
                  >
                    <div style={{ fontWeight: 700, display: 'flex', alignItems: 'center', gap: '0.3rem' }}>
                      <span>🏛️</span>
                      <span>Campus Admin</span>
                    </div>
                    <div style={{ fontSize: '0.68rem', color: '#94a3b8', marginTop: '0.15rem' }}>Stanford Admin</div>
                  </button>

                  <button
                    type="button"
                    onClick={() => handleDemoQuickLogin('superadmin@unisphere.ai', 'SuperAdmin@123')}
                    style={{
                      padding: '0.7rem 0.8rem',
                      backgroundColor: 'rgba(239, 68, 68, 0.08)',
                      border: '1px solid rgba(239, 68, 68, 0.35)',
                      color: '#fca5a5',
                      borderRadius: '10px',
                      fontSize: '0.78rem',
                      cursor: 'pointer',
                      fontWeight: 600,
                      textAlign: 'left',
                      transition: 'all 0.15s ease'
                    }}
                    onMouseOver={(e) => (e.currentTarget.style.backgroundColor = 'rgba(239, 68, 68, 0.16)')}
                    onMouseOut={(e) => (e.currentTarget.style.backgroundColor = 'rgba(239, 68, 68, 0.08)')}
                  >
                    <div style={{ fontWeight: 700, display: 'flex', alignItems: 'center', gap: '0.3rem' }}>
                      <span>🌐</span>
                      <span>Super Admin</span>
                    </div>
                    <div style={{ fontSize: '0.68rem', color: '#94a3b8', marginTop: '0.15rem' }}>Global Governance</div>
                  </button>
                </div>
              </div>
            </form>
          ) : (
            <form onSubmit={handleRegisterTenantSubmit}>
              <div style={{ marginBottom: '1rem' }}>
                <label style={{ display: 'block', fontSize: '0.82rem', fontWeight: 600, color: '#cbd5e1', marginBottom: '0.35rem' }}>
                  University / Institution Name
                </label>
                <input
                  type="text"
                  required
                  value={tenantName}
                  onChange={(e) => setTenantName(e.target.value)}
                  placeholder="e.g. Cambridge Institute of Technology"
                  style={{
                    width: '100%',
                    padding: '0.7rem 0.85rem',
                    backgroundColor: 'rgba(2, 6, 23, 0.7)',
                    border: '1px solid rgba(255, 255, 255, 0.12)',
                    borderRadius: '8px',
                    color: '#f8fafc',
                    outline: 'none',
                    fontSize: '0.88rem'
                  }}
                />
              </div>

              <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '0.75rem', marginBottom: '1rem' }}>
                <div>
                  <label style={{ display: 'block', fontSize: '0.82rem', fontWeight: 600, color: '#cbd5e1', marginBottom: '0.35rem' }}>
                    Campus Code
                  </label>
                  <input
                    type="text"
                    required
                    value={regTenantCode}
                    onChange={(e) => setRegTenantCode(e.target.value)}
                    placeholder="e.g. CIT"
                    style={{
                      width: '100%',
                      padding: '0.7rem 0.85rem',
                      backgroundColor: 'rgba(2, 6, 23, 0.7)',
                      border: '1px solid rgba(255, 255, 255, 0.12)',
                      borderRadius: '8px',
                      color: '#f8fafc',
                      outline: 'none',
                      fontSize: '0.88rem'
                    }}
                  />
                </div>
                <div>
                  <label style={{ display: 'block', fontSize: '0.82rem', fontWeight: 600, color: '#cbd5e1', marginBottom: '0.35rem' }}>
                    Domain
                  </label>
                  <input
                    type="text"
                    value={tenantDomain}
                    onChange={(e) => setTenantDomain(e.target.value)}
                    placeholder="cit.edu"
                    style={{
                      width: '100%',
                      padding: '0.7rem 0.85rem',
                      backgroundColor: 'rgba(2, 6, 23, 0.7)',
                      border: '1px solid rgba(255, 255, 255, 0.12)',
                      borderRadius: '8px',
                      color: '#f8fafc',
                      outline: 'none',
                      fontSize: '0.88rem'
                    }}
                  />
                </div>
              </div>

              <div style={{
                backgroundColor: 'rgba(2, 6, 23, 0.4)',
                border: '1px solid rgba(255, 255, 255, 0.08)',
                padding: '1rem',
                borderRadius: '10px',
                marginBottom: '1.25rem'
              }}>
                <div style={{ fontSize: '0.76rem', fontWeight: 700, color: '#38bdf8', marginBottom: '0.75rem', textTransform: 'uppercase' }}>
                  Root Administrator Account
                </div>
                <div style={{ marginBottom: '0.65rem' }}>
                  <input
                    type="text"
                    required
                    value={adminName}
                    onChange={(e) => setAdminName(e.target.value)}
                    placeholder="Admin Full Name (e.g. Dr. Jane Smith)"
                    style={{ width: '100%', padding: '0.65rem', backgroundColor: '#090d16', border: '1px solid rgba(255, 255, 255, 0.1)', borderRadius: '6px', color: '#fff', fontSize: '0.85rem' }}
                  />
                </div>
                <div style={{ marginBottom: '0.65rem' }}>
                  <input
                    type="email"
                    required
                    value={adminEmail}
                    onChange={(e) => setAdminEmail(e.target.value)}
                    placeholder="Admin Email (e.g. admin@cit.edu)"
                    style={{ width: '100%', padding: '0.65rem', backgroundColor: '#090d16', border: '1px solid rgba(255, 255, 255, 0.1)', borderRadius: '6px', color: '#fff', fontSize: '0.85rem' }}
                  />
                </div>
                <div>
                  <input
                    type="password"
                    required
                    value={adminPassword}
                    onChange={(e) => setAdminPassword(e.target.value)}
                    placeholder="Password (minimum 6 characters)"
                    style={{ width: '100%', padding: '0.65rem', backgroundColor: '#090d16', border: '1px solid rgba(255, 255, 255, 0.1)', borderRadius: '6px', color: '#fff', fontSize: '0.85rem' }}
                  />
                </div>
              </div>

              <button
                type="submit"
                disabled={isLoading}
                style={{
                  width: '100%',
                  padding: '0.85rem',
                  background: 'linear-gradient(135deg, #0284c7 0%, #0369a1 100%)',
                  color: '#ffffff',
                  border: '1px solid rgba(56, 189, 248, 0.4)',
                  borderRadius: '10px',
                  fontWeight: 700,
                  fontSize: '0.92rem',
                  cursor: isLoading ? 'not-allowed' : 'pointer',
                  opacity: isLoading ? 0.6 : 1
                }}
              >
                {isLoading ? 'Creating Campus...' : 'Onboard University & Administrator'}
              </button>
            </form>
          )}
        </div>
      </div>
    </div>
  );
};
