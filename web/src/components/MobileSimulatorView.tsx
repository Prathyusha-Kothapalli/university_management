import React, { useState } from 'react';
import { useAuth } from '../features/auth/AuthContext';

export const MobileSimulatorView: React.FC = () => {
  const { user } = useAuth();
  const [device, setDevice] = useState<'iphone' | 'android'>('iphone');
  const [activeTab, setActiveTab] = useState<'home' | 'academics' | 'hostel' | 'transport' | 'profile'>('home');
  const [isDarkMode, setIsDarkMode] = useState<boolean>(true);

  return (
    <div style={{
      minHeight: '85vh',
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      justifyContent: 'center',
      padding: '2rem 1rem',
      backgroundColor: '#090d16'
    }}>
      {/* Simulator Control Header */}
      <div style={{
        display: 'flex',
        alignItems: 'center',
        gap: '1.5rem',
        marginBottom: '1.5rem',
        backgroundColor: 'rgba(15, 23, 42, 0.8)',
        padding: '0.75rem 1.5rem',
        borderRadius: '16px',
        border: '1px solid rgba(255, 255, 255, 0.1)',
        backdropFilter: 'blur(10px)'
      }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
          <span style={{ fontSize: '0.85rem', color: '#94a3b8', fontWeight: 600 }}>Device Frame:</span>
          <button
            onClick={() => setDevice('iphone')}
            style={{
              padding: '0.4rem 0.8rem',
              borderRadius: '8px',
              border: 'none',
              backgroundColor: device === 'iphone' ? '#6366f1' : 'rgba(255,255,255,0.05)',
              color: '#ffffff',
              fontSize: '0.8rem',
              fontWeight: 600,
              cursor: 'pointer'
            }}
          >
            📱 iPhone 15 Pro
          </button>
          <button
            onClick={() => setDevice('android')}
            style={{
              padding: '0.4rem 0.8rem',
              borderRadius: '8px',
              border: 'none',
              backgroundColor: device === 'android' ? '#6366f1' : 'rgba(255,255,255,0.05)',
              color: '#ffffff',
              fontSize: '0.8rem',
              fontWeight: 600,
              cursor: 'pointer'
            }}
          >
            🤖 Pixel 8 Pro
          </button>
        </div>

        <div style={{ height: '20px', width: '1px', backgroundColor: 'rgba(255,255,255,0.1)' }} />

        <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
          <span style={{ fontSize: '0.85rem', color: '#94a3b8', fontWeight: 600 }}>Theme:</span>
          <button
            onClick={() => setIsDarkMode(!isDarkMode)}
            style={{
              padding: '0.4rem 0.8rem',
              borderRadius: '8px',
              border: 'none',
              backgroundColor: 'rgba(255,255,255,0.05)',
              color: '#38bdf8',
              fontSize: '0.8rem',
              fontWeight: 600,
              cursor: 'pointer'
            }}
          >
            {isDarkMode ? '🌙 Dark Mode' : '☀️ Light Mode'}
          </button>
        </div>
      </div>

      {/* Mobile Device Frame */}
      <div style={{
        width: device === 'iphone' ? '380px' : '390px',
        height: device === 'iphone' ? '740px' : '750px',
        borderRadius: device === 'iphone' ? '48px' : '36px',
        border: device === 'iphone' ? '12px solid #1e293b' : '10px solid #0f172a',
        boxShadow: '0 25px 50px -12px rgba(0, 0, 0, 0.7), 0 0 40px rgba(99, 102, 241, 0.25)',
        backgroundColor: isDarkMode ? '#0f172a' : '#ffffff',
        color: isDarkMode ? '#f8fafc' : '#0f172a',
        display: 'flex',
        flexDirection: 'column',
        position: 'relative',
        overflow: 'hidden'
      }}>
        {/* Notch / Dynamic Island */}
        <div style={{
          position: 'absolute',
          top: '12px',
          left: '50%',
          transform: 'translateX(-50%)',
          width: device === 'iphone' ? '120px' : '80px',
          height: device === 'iphone' ? '28px' : '20px',
          backgroundColor: '#000000',
          borderRadius: '20px',
          zIndex: 50,
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center'
        }}>
          <div style={{ width: '10px', height: '10px', borderRadius: '50%', backgroundColor: '#0f172a', border: '2px solid #1e293b' }} />
        </div>

        {/* Mobile Status Bar */}
        <div style={{
          padding: '16px 24px 8px 24px',
          display: 'flex',
          justify: 'space-between',
          alignItems: 'center',
          fontSize: '0.75rem',
          fontWeight: 700,
          zIndex: 40
        }}>
          <span>9:41</span>
          <div style={{ display: 'flex', gap: '6px', alignItems: 'center' }}>
            <span>5G</span>
            <span>📶</span>
            <span>🔋 100%</span>
          </div>
        </div>

        {/* Flutter Mobile Header Bar */}
        <div style={{
          padding: '0.75rem 1.25rem',
          backgroundColor: isDarkMode ? 'rgba(30, 41, 59, 0.9)' : 'rgba(241, 245, 249, 0.9)',
          borderBottom: isDarkMode ? '1px solid rgba(255,255,255,0.08)' : '1px solid rgba(0,0,0,0.08)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'space-between'
        }}>
          <div>
            <span style={{ fontSize: '0.65rem', color: '#6366f1', fontWeight: 800, textTransform: 'uppercase', letterSpacing: '0.05em' }}>
              UniSphere Mobile (Flutter v3.44)
            </span>
            <h3 style={{ fontSize: '1.05rem', fontWeight: 800, margin: 0 }}>
              {activeTab === 'home' && 'Student Hub'}
              {activeTab === 'academics' && 'Academics & Courses'}
              {activeTab === 'hostel' && 'Hostel Pass'}
              {activeTab === 'transport' && 'Bus GPS Pass'}
              {activeTab === 'profile' && 'My Profile'}
            </h3>
          </div>
          <div style={{
            width: '32px',
            height: '32px',
            borderRadius: '50%',
            backgroundColor: '#6366f1',
            color: '#fff',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            fontWeight: 700,
            fontSize: '0.85rem'
          }}>
            {user?.name ? user.name.slice(0, 2).toUpperCase() : 'US'}
          </div>
        </div>

        {/* Flutter Mobile Content View */}
        <div style={{
          flex: 1,
          overflowY: 'auto',
          padding: '1rem',
          display: 'flex',
          flexDirection: 'column',
          gap: '1rem'
        }}>
          {activeTab === 'home' && (
            <>
              {/* Announcement Banner */}
              <div style={{
                background: 'linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%)',
                padding: '1.25rem',
                borderRadius: '16px',
                color: '#ffffff'
              }}>
                <span style={{ fontSize: '0.65rem', backgroundColor: 'rgba(255,255,255,0.2)', padding: '0.2rem 0.5rem', borderRadius: '4px', fontWeight: 700 }}>
                  FALL 2026 ADVISORY
                </span>
                <h4 style={{ fontSize: '1.1rem', fontWeight: 800, marginTop: '0.5rem', marginBottom: '0.25rem' }}>
                  Welcome Back, {user?.name || 'Student'}!
                </h4>
                <p style={{ fontSize: '0.75rem', opacity: 0.9 }}>
                  Mid-term examination schedule released. Check your registered timetable.
                </p>
              </div>

              {/* Quick Actions Grid */}
              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(2, 1fr)', gap: '0.75rem' }}>
                <div onClick={() => setActiveTab('academics')} style={{ padding: '1rem', backgroundColor: isDarkMode ? '#1e293b' : '#f1f5f9', borderRadius: '12px', cursor: 'pointer' }}>
                  <span style={{ fontSize: '1.25rem' }}>📚</span>
                  <div style={{ fontWeight: 700, fontSize: '0.85rem', marginTop: '0.5rem' }}>My Courses</div>
                  <div style={{ fontSize: '0.65rem', color: '#94a3b8' }}>6 Enrolled</div>
                </div>

                <div onClick={() => setActiveTab('hostel')} style={{ padding: '1rem', backgroundColor: isDarkMode ? '#1e293b' : '#f1f5f9', borderRadius: '12px', cursor: 'pointer' }}>
                  <span style={{ fontSize: '1.25rem' }}>🏢</span>
                  <div style={{ fontWeight: 700, fontSize: '0.85rem', marginTop: '0.5rem' }}>Hostel Gate Pass</div>
                  <div style={{ fontSize: '0.65rem', color: '#10b981' }}>Active Pass</div>
                </div>

                <div onClick={() => setActiveTab('transport')} style={{ padding: '1rem', backgroundColor: isDarkMode ? '#1e293b' : '#f1f5f9', borderRadius: '12px', cursor: 'pointer' }}>
                  <span style={{ fontSize: '1.25rem' }}>🚌</span>
                  <div style={{ fontWeight: 700, fontSize: '0.85rem', marginTop: '0.5rem' }}>Bus Route #14</div>
                  <div style={{ fontSize: '0.65rem', color: '#f59e0b' }}>Arriving in 8 mins</div>
                </div>

                <div onClick={() => setActiveTab('profile')} style={{ padding: '1rem', backgroundColor: isDarkMode ? '#1e293b' : '#f1f5f9', borderRadius: '12px', cursor: 'pointer' }}>
                  <span style={{ fontSize: '1.25rem' }}>🆔</span>
                  <div style={{ fontWeight: 700, fontSize: '0.85rem', marginTop: '0.5rem' }}>Digital ID</div>
                  <div style={{ fontSize: '0.65rem', color: '#6366f1' }}>Verified</div>
                </div>
              </div>

              {/* Attendance Widget */}
              <div style={{ padding: '1rem', backgroundColor: isDarkMode ? '#1e293b' : '#f1f5f9', borderRadius: '14px' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '0.5rem' }}>
                  <span style={{ fontSize: '0.85rem', fontWeight: 700 }}>Overall Attendance</span>
                  <span style={{ fontSize: '0.85rem', fontWeight: 800, color: '#10b981' }}>94.2%</span>
                </div>
                <div style={{ height: '8px', backgroundColor: isDarkMode ? '#334155' : '#cbd5e1', borderRadius: '4px', overflow: 'hidden' }}>
                  <div style={{ width: '94.2%', height: '100%', backgroundColor: '#10b981' }} />
                </div>
              </div>
            </>
          )}

          {activeTab === 'academics' && (
            <div style={{ display: 'flex', flexDirection: 'column', gap: '0.75rem' }}>
              {['CS101 - Artificial Intelligence', 'CS204 - Database Systems', 'MATH301 - Discrete Mathematics', 'ENG102 - Technical Writing'].map((course, idx) => (
                <div key={idx} style={{ padding: '1rem', backgroundColor: isDarkMode ? '#1e293b' : '#f1f5f9', borderRadius: '12px' }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                    <span style={{ fontWeight: 700, fontSize: '0.85rem' }}>{course}</span>
                    <span style={{ fontSize: '0.7rem', color: '#6366f1', fontWeight: 700 }}>Grade A</span>
                  </div>
                  <p style={{ fontSize: '0.7rem', color: '#94a3b8', marginTop: '0.25rem' }}>Credits: 4.0 • Mon/Wed 10:00 AM</p>
                </div>
              ))}
            </div>
          )}

          {activeTab === 'hostel' && (
            <div style={{ padding: '1.25rem', backgroundColor: isDarkMode ? '#1e293b' : '#f1f5f9', borderRadius: '16px' }}>
              <div style={{ fontSize: '2.5rem', marginBottom: '0.5rem', textAlign: 'center' }}>🎫</div>
              <h4 style={{ textAlign: 'center', margin: '0 0 0.25rem 0', fontSize: '1rem' }}>Digital Hostel Gate Pass</h4>
              <p style={{ textAlign: 'center', fontSize: '0.75rem', color: '#94a3b8', margin: 0 }}>Valid for Outing & Night Curfew Entry</p>
              <div style={{ margin: '1.5rem auto', width: '140px', height: '140px', backgroundColor: '#ffffff', padding: '10px', borderRadius: '12px' }}>
                <div style={{ width: '100%', height: '100%', background: 'repeating-conic-gradient(#000 0% 25%, #fff 0% 50%) 50% / 20px 20px' }} />
              </div>
              <span style={{ display: 'block', textAlign: 'center', color: '#10b981', fontWeight: 700, fontSize: '0.8rem' }}>● PASS STATUS: ACTIVE</span>
            </div>
          )}

          {activeTab === 'transport' && (
            <div style={{ display: 'flex', flexDirection: 'column', gap: '0.75rem' }}>
              <div style={{ padding: '1rem', backgroundColor: isDarkMode ? '#1e293b' : '#f1f5f9', borderRadius: '12px' }}>
                <span style={{ fontSize: '0.7rem', color: '#f59e0b', fontWeight: 800 }}>LIVE GPS TELEMETRY</span>
                <h4 style={{ margin: '0.25rem 0 0.5rem 0', fontSize: '1rem' }}>Campus Express Bus #14</h4>
                <p style={{ fontSize: '0.75rem', color: '#94a3b8', margin: 0 }}>Driver: Robert Hayes • Driver Contact: +1 555-0192</p>
                <div style={{ marginTop: '0.75rem', padding: '0.5rem', backgroundColor: isDarkMode ? '#0f172a' : '#e2e8f0', borderRadius: '8px', fontSize: '0.75rem' }}>
                  Next Stop: Central Library Gate (Est. 3 mins)
                </div>
              </div>
            </div>
          )}

          {activeTab === 'profile' && (
            <div style={{ padding: '1rem', backgroundColor: isDarkMode ? '#1e293b' : '#f1f5f9', borderRadius: '12px' }}>
              <div style={{ textAlign: 'center', marginBottom: '1rem' }}>
                <div style={{ width: '64px', height: '64px', borderRadius: '50%', backgroundColor: '#6366f1', color: '#fff', display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: '1.5rem', margin: '0 auto 0.5rem auto', fontWeight: 800 }}>
                  {user?.name ? user.name.slice(0, 2).toUpperCase() : 'US'}
                </div>
                <h3 style={{ margin: 0, fontSize: '1.1rem' }}>{user?.name || 'Student Account'}</h3>
                <span style={{ fontSize: '0.75rem', color: '#94a3b8' }}>ID: US-2026-8891</span>
              </div>
              <div style={{ fontSize: '0.75rem', display: 'flex', flexDirection: 'column', gap: '0.5rem' }}>
                <div><strong>Email:</strong> {user?.email || 'student@university.edu'}</div>
                <div><strong>Role:</strong> {user?.role || 'STUDENT'}</div>
                <div><strong>Department:</strong> Computer Science</div>
              </div>
            </div>
          )}
        </div>

        {/* Flutter Bottom Navigation Bar */}
        <div style={{
          display: 'flex',
          justifyContent: 'space-around',
          alignItems: 'center',
          padding: '0.5rem 0 1rem 0',
          backgroundColor: isDarkMode ? '#1e293b' : '#f1f5f9',
          borderTop: isDarkMode ? '1px solid rgba(255,255,255,0.08)' : '1px solid rgba(0,0,0,0.08)'
        }}>
          {[
            { id: 'home', icon: '🏠', label: 'Home' },
            { id: 'academics', icon: '📖', label: 'Academics' },
            { id: 'hostel', icon: '🏢', label: 'Hostel' },
            { id: 'transport', icon: '🚌', label: 'Bus Pass' },
            { id: 'profile', icon: '👤', label: 'Profile' }
          ].map(tab => (
            <button
              key={tab.id}
              onClick={() => setActiveTab(tab.id as any)}
              style={{
                background: 'none',
                border: 'none',
                display: 'flex',
                flexDirection: 'column',
                alignItems: 'center',
                color: activeTab === tab.id ? '#6366f1' : (isDarkMode ? '#64748b' : '#94a3b8'),
                fontSize: '0.7rem',
                fontWeight: activeTab === tab.id ? 700 : 500,
                cursor: 'pointer'
              }}
            >
              <span style={{ fontSize: '1.1rem' }}>{tab.icon}</span>
              {tab.label}
            </button>
          ))}
        </div>
      </div>
    </div>
  );
};

export default MobileSimulatorView;
