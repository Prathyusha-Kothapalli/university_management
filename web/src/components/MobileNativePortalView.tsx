import React, { useState } from 'react';
import { useAuth } from '../features/auth/AuthContext';

interface MobileNativePortalViewProps {
  onSwitchToDesktop?: () => void;
  onOpenBot?: () => void;
}

export const MobileNativePortalView: React.FC<MobileNativePortalViewProps> = ({
  onSwitchToDesktop,
  onOpenBot
}) => {
  const { user, tenant, logout } = useAuth();
  const [activeTab, setActiveTab] = useState<'home' | 'academics' | 'hostel' | 'transport' | 'profile'>('home');
  const [isDarkMode, setIsDarkMode] = useState<boolean>(true);

  const getInitials = (name?: string) => {
    if (!name) return 'US';
    const parts = name.trim().split(' ');
    if (parts.length >= 2) return `${parts[0][0]}${parts[1][0]}`.toUpperCase();
    return name.slice(0, 2).toUpperCase();
  };

  return (
    <div style={{
      width: '100%',
      minHeight: '100vh',
      backgroundColor: isDarkMode ? '#090d16' : '#f8fafc',
      color: isDarkMode ? '#f8fafc' : '#0f172a',
      display: 'flex',
      flexDirection: 'column',
      position: 'relative',
      overflowX: 'hidden'
    }}>
      {/* Mobile App Header */}
      <header style={{
        position: 'sticky',
        top: 0,
        zIndex: 50,
        backgroundColor: isDarkMode ? 'rgba(15, 23, 42, 0.95)' : 'rgba(255, 255, 255, 0.95)',
        backdropFilter: 'blur(16px)',
        WebkitBackdropFilter: 'blur(16px)',
        borderBottom: isDarkMode ? '1px solid rgba(255, 255, 255, 0.08)' : '1px solid rgba(0, 0, 0, 0.08)',
        padding: '0.75rem 1rem',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'space-between',
        boxShadow: '0 2px 10px rgba(0, 0, 0, 0.2)'
      }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '0.65rem' }}>
          <div style={{
            width: '32px',
            height: '32px',
            borderRadius: '9px',
            background: 'linear-gradient(135deg, #0284c7 0%, #6366f1 100%)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            fontWeight: 800,
            fontSize: '1rem',
            color: '#ffffff'
          }}>
            U
          </div>
          <div>
            <div style={{ fontSize: '0.95rem', fontWeight: 800, lineHeight: 1.1 }}>
              UniSphere<span style={{ color: '#38bdf8' }}> Mobile</span>
            </div>
            <div style={{ fontSize: '0.62rem', color: '#64748b', fontWeight: 600 }}>
              {tenant?.code || 'CAMPUS'} • {user ? (user.role.replace('_', ' ')) : 'GUEST'}
            </div>
          </div>
        </div>

        <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
          {/* Theme toggle */}
          <button
            onClick={() => setIsDarkMode(!isDarkMode)}
            style={{
              background: 'none',
              border: isDarkMode ? '1px solid rgba(255,255,255,0.12)' : '1px solid rgba(0,0,0,0.12)',
              borderRadius: '8px',
              padding: '0.35rem 0.55rem',
              color: isDarkMode ? '#f8fafc' : '#0f172a',
              cursor: 'pointer',
              fontSize: '0.8rem'
            }}
            title="Toggle theme"
          >
            {isDarkMode ? '🌙' : '☀️'}
          </button>

          {/* Desktop switch if requested */}
          {onSwitchToDesktop && (
            <button
              onClick={onSwitchToDesktop}
              style={{
                backgroundColor: 'rgba(99, 102, 241, 0.15)',
                color: '#818cf8',
                border: '1px solid rgba(99, 102, 241, 0.35)',
                borderRadius: '8px',
                padding: '0.35rem 0.6rem',
                fontSize: '0.72rem',
                fontWeight: 700,
                cursor: 'pointer'
              }}
            >
              💻 Web View
            </button>
          )}

          {/* User Avatar */}
          <div style={{
            width: '32px',
            height: '32px',
            borderRadius: '50%',
            backgroundColor: '#6366f1',
            color: '#fff',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            fontWeight: 800,
            fontSize: '0.78rem'
          }}>
            {getInitials(user?.full_name)}
          </div>
        </div>
      </header>

      {/* Scrollable Mobile Body Content */}
      <main style={{
        flex: 1,
        padding: '1rem 1rem 5.5rem 1rem',
        maxWidth: '600px',
        margin: '0 auto',
        width: '100%',
        display: 'flex',
        flexDirection: 'column',
        gap: '1rem'
      }}>
        {activeTab === 'home' && (
          <>
            {/* Announcement / Welcome Card */}
            <div style={{
              background: 'linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%)',
              padding: '1.25rem',
              borderRadius: '16px',
              color: '#ffffff',
              boxShadow: '0 8px 25px rgba(79, 70, 229, 0.3)'
            }}>
              <span style={{ fontSize: '0.65rem', backgroundColor: 'rgba(255,255,255,0.2)', padding: '0.2rem 0.5rem', borderRadius: '4px', fontWeight: 700 }}>
                ACADEMIC YEAR 2026-2027
              </span>
              <h2 style={{ fontSize: '1.2rem', fontWeight: 800, marginTop: '0.6rem', marginBottom: '0.25rem' }}>
                Welcome, {user?.full_name || 'Student'}!
              </h2>
              <p style={{ fontSize: '0.78rem', opacity: 0.9, margin: 0, lineHeight: 1.4 }}>
                Mid-term schedule & room allocations published. Verify exam hall tickets in the Academics tab.
              </p>
            </div>

            {/* Quick Actions 2x2 Grid */}
            <div>
              <h3 style={{ fontSize: '0.85rem', fontWeight: 700, color: isDarkMode ? '#94a3b8' : '#64748b', textTransform: 'uppercase', letterSpacing: '0.05em', marginBottom: '0.65rem' }}>
                Quick Services
              </h3>
              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(2, 1fr)', gap: '0.75rem' }}>
                <div
                  onClick={() => setActiveTab('academics')}
                  style={{
                    padding: '1rem',
                    backgroundColor: isDarkMode ? '#141e33' : '#ffffff',
                    border: isDarkMode ? '1px solid rgba(255,255,255,0.08)' : '1px solid rgba(0,0,0,0.08)',
                    borderRadius: '14px',
                    cursor: 'pointer',
                    boxShadow: '0 2px 8px rgba(0,0,0,0.1)'
                  }}
                >
                  <span style={{ fontSize: '1.5rem' }}>📚</span>
                  <div style={{ fontWeight: 800, fontSize: '0.9rem', marginTop: '0.5rem' }}>My Courses</div>
                  <div style={{ fontSize: '0.7rem', color: '#94a3b8' }}>5 Active Modules</div>
                </div>

                <div
                  onClick={() => setActiveTab('hostel')}
                  style={{
                    padding: '1rem',
                    backgroundColor: isDarkMode ? '#141e33' : '#ffffff',
                    border: isDarkMode ? '1px solid rgba(255,255,255,0.08)' : '1px solid rgba(0,0,0,0.08)',
                    borderRadius: '14px',
                    cursor: 'pointer',
                    boxShadow: '0 2px 8px rgba(0,0,0,0.1)'
                  }}
                >
                  <span style={{ fontSize: '1.5rem' }}>🏢</span>
                  <div style={{ fontWeight: 800, fontSize: '0.9rem', marginTop: '0.5rem' }}>Hostel Gate Pass</div>
                  <div style={{ fontSize: '0.7rem', color: '#10b981', fontWeight: 700 }}>● Active Pass</div>
                </div>

                <div
                  onClick={() => setActiveTab('transport')}
                  style={{
                    padding: '1rem',
                    backgroundColor: isDarkMode ? '#141e33' : '#ffffff',
                    border: isDarkMode ? '1px solid rgba(255,255,255,0.08)' : '1px solid rgba(0,0,0,0.08)',
                    borderRadius: '14px',
                    cursor: 'pointer',
                    boxShadow: '0 2px 8px rgba(0,0,0,0.1)'
                  }}
                >
                  <span style={{ fontSize: '1.5rem' }}>🚌</span>
                  <div style={{ fontWeight: 800, fontSize: '0.9rem', marginTop: '0.5rem' }}>Bus Route #14</div>
                  <div style={{ fontSize: '0.7rem', color: '#f59e0b', fontWeight: 700 }}>Arriving in 6m</div>
                </div>

                <div
                  onClick={() => setActiveTab('profile')}
                  style={{
                    padding: '1rem',
                    backgroundColor: isDarkMode ? '#141e33' : '#ffffff',
                    border: isDarkMode ? '1px solid rgba(255,255,255,0.08)' : '1px solid rgba(0,0,0,0.08)',
                    borderRadius: '14px',
                    cursor: 'pointer',
                    boxShadow: '0 2px 8px rgba(0,0,0,0.1)'
                  }}
                >
                  <span style={{ fontSize: '1.5rem' }}>🆔</span>
                  <div style={{ fontWeight: 800, fontSize: '0.9rem', marginTop: '0.5rem' }}>Digital ID</div>
                  <div style={{ fontSize: '0.7rem', color: '#38bdf8', fontWeight: 700 }}>Verified</div>
                </div>
              </div>
            </div>

            {/* Attendance Progress Card */}
            <div style={{
              padding: '1.15rem',
              backgroundColor: isDarkMode ? '#141e33' : '#ffffff',
              border: isDarkMode ? '1px solid rgba(255,255,255,0.08)' : '1px solid rgba(0,0,0,0.08)',
              borderRadius: '16px',
              boxShadow: '0 2px 8px rgba(0,0,0,0.1)'
            }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '0.6rem' }}>
                <span style={{ fontSize: '0.88rem', fontWeight: 700 }}>Semester Attendance Target</span>
                <span style={{ fontSize: '0.95rem', fontWeight: 800, color: '#10b981' }}>94.2%</span>
              </div>
              <div style={{ height: '8px', backgroundColor: isDarkMode ? '#1e293b' : '#e2e8f0', borderRadius: '4px', overflow: 'hidden' }}>
                <div style={{ width: '94.2%', height: '100%', backgroundColor: '#10b981' }} />
              </div>
              <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.7rem', color: '#94a3b8', marginTop: '0.4rem' }}>
                <span>Min Required: 75%</span>
                <span style={{ color: '#10b981', fontWeight: 700 }}>Eligible for Finals</span>
              </div>
            </div>

            {/* AI Assistant Quick Prompt */}
            {onOpenBot && (
              <div
                onClick={onOpenBot}
                style={{
                  padding: '1rem',
                  borderRadius: '14px',
                  background: 'linear-gradient(135deg, rgba(56, 189, 248, 0.15) 0%, rgba(99, 102, 241, 0.15) 100%)',
                  border: '1px solid rgba(56, 189, 248, 0.35)',
                  cursor: 'pointer',
                  display: 'flex',
                  alignItems: 'center',
                  gap: '0.85rem'
                }}
              >
                <div style={{ fontSize: '1.5rem' }}>✨</div>
                <div style={{ flex: 1 }}>
                  <div style={{ fontWeight: 800, fontSize: '0.88rem', color: '#38bdf8' }}>AI Study Copilot Ready</div>
                  <div style={{ fontSize: '0.72rem', color: '#94a3b8' }}>Ask questions about AVL trees, OS, or calculus</div>
                </div>
                <span style={{ fontSize: '1.2rem', color: '#38bdf8' }}>➜</span>
              </div>
            )}
          </>
        )}

        {activeTab === 'academics' && (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '0.85rem' }}>
            <h3 style={{ fontSize: '1.1rem', fontWeight: 800, margin: '0 0 0.25rem 0' }}>Enrolled Modules (Spring 2026)</h3>
            {[
              { code: 'CS101', name: 'Data Structures & Algorithms', prof: 'Dr. Alan Turing', grade: 'Grade A', credits: '4.0', time: 'Mon/Wed 10:00 AM' },
              { code: 'CS202', name: 'Operating Systems & Architecture', prof: 'Dr. Dennis Ritchie', grade: 'Grade A-', credits: '4.0', time: 'Tue/Thu 02:00 PM' },
              { code: 'MATH301', name: 'Linear Algebra & Matrix Theory', prof: 'Dr. Katherine Johnson', grade: 'Grade A', credits: '3.0', time: 'Fri 09:00 AM' },
              { code: 'AI401', name: 'Machine Learning & Neural Networks', prof: 'Dr. Geoffrey Hinton', grade: 'Grade A+', credits: '4.0', time: 'Mon/Wed 03:30 PM' }
            ].map((course, idx) => (
              <div
                key={idx}
                style={{
                  padding: '1.15rem',
                  backgroundColor: isDarkMode ? '#141e33' : '#ffffff',
                  border: isDarkMode ? '1px solid rgba(255,255,255,0.08)' : '1px solid rgba(0,0,0,0.08)',
                  borderRadius: '14px',
                  boxShadow: '0 2px 8px rgba(0,0,0,0.1)'
                }}
              >
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
                  <div>
                    <span style={{ fontSize: '0.7rem', color: '#6366f1', fontWeight: 800 }}>{course.code}</span>
                    <h4 style={{ margin: '0.2rem 0 0.4rem 0', fontSize: '0.95rem', fontWeight: 700 }}>{course.name}</h4>
                    <p style={{ margin: 0, fontSize: '0.75rem', color: '#94a3b8' }}>Instructor: {course.prof}</p>
                  </div>
                  <span style={{
                    backgroundColor: 'rgba(99, 102, 241, 0.15)',
                    color: '#818cf8',
                    border: '1px solid rgba(99, 102, 241, 0.3)',
                    padding: '0.2rem 0.55rem',
                    borderRadius: '6px',
                    fontSize: '0.75rem',
                    fontWeight: 800
                  }}>
                    {course.grade}
                  </span>
                </div>
                <div style={{ marginTop: '0.75rem', paddingTop: '0.65rem', borderTop: isDarkMode ? '1px solid rgba(255,255,255,0.06)' : '1px solid rgba(0,0,0,0.06)', display: 'flex', justifyContent: 'space-between', fontSize: '0.72rem', color: '#94a3b8' }}>
                  <span>Credits: {course.credits}</span>
                  <span>{course.time}</span>
                </div>
              </div>
            ))}
          </div>
        )}

        {activeTab === 'hostel' && (
          <div style={{
            padding: '1.5rem',
            backgroundColor: isDarkMode ? '#141e33' : '#ffffff',
            border: isDarkMode ? '1px solid rgba(255,255,255,0.08)' : '1px solid rgba(0,0,0,0.08)',
            borderRadius: '20px',
            textAlign: 'center',
            boxShadow: '0 4px 15px rgba(0,0,0,0.15)'
          }}>
            <div style={{ fontSize: '3rem', marginBottom: '0.5rem' }}>🎫</div>
            <h3 style={{ margin: '0 0 0.25rem 0', fontSize: '1.2rem', fontWeight: 800 }}>Digital Hostel Gate Pass</h3>
            <p style={{ fontSize: '0.8rem', color: '#94a3b8', margin: 0 }}>Valid for Outing & Night Curfew Entry</p>

            {/* Generated QR Pass simulation */}
            <div style={{
              margin: '1.5rem auto',
              width: '160px',
              height: '160px',
              backgroundColor: '#ffffff',
              padding: '12px',
              borderRadius: '16px',
              boxShadow: '0 4px 15px rgba(0,0,0,0.2)'
            }}>
              <div style={{
                width: '100%',
                height: '100%',
                background: 'repeating-conic-gradient(#000 0% 25%, #fff 0% 50%) 50% / 20px 20px',
                borderRadius: '8px'
              }} />
            </div>

            <div style={{
              display: 'inline-block',
              backgroundColor: 'rgba(16, 185, 129, 0.15)',
              color: '#10b981',
              border: '1px solid rgba(16, 185, 129, 0.35)',
              padding: '0.4rem 1rem',
              borderRadius: '9999px',
              fontWeight: 800,
              fontSize: '0.82rem'
            }}>
              ● PASS STATUS: ACTIVE & VERIFIED
            </div>

            <div style={{ marginTop: '1.25rem', textAlign: 'left', fontSize: '0.78rem', color: '#94a3b8', display: 'flex', flexDirection: 'column', gap: '0.4rem' }}>
              <div><strong>Pass Holder:</strong> {user?.full_name || 'Registered Student'}</div>
              <div><strong>Hostel Block:</strong> Block B, Room 304</div>
              <div><strong>Valid Until:</strong> Today, 10:30 PM Curfew</div>
            </div>
          </div>
        )}

        {activeTab === 'transport' && (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '0.85rem' }}>
            <h3 style={{ fontSize: '1.1rem', fontWeight: 800, margin: '0 0 0.25rem 0' }}>Campus Bus Telemetry</h3>
            <div style={{
              padding: '1.25rem',
              backgroundColor: isDarkMode ? '#141e33' : '#ffffff',
              border: isDarkMode ? '1px solid rgba(255,255,255,0.08)' : '1px solid rgba(0,0,0,0.08)',
              borderRadius: '16px',
              boxShadow: '0 2px 8px rgba(0,0,0,0.1)'
            }}>
              <span style={{ fontSize: '0.7rem', color: '#f59e0b', fontWeight: 800, textTransform: 'uppercase' }}>
                ● LIVE GPS TELEMETRY
              </span>
              <h4 style={{ margin: '0.35rem 0 0.5rem 0', fontSize: '1.05rem', fontWeight: 800 }}>Campus Express Bus #14</h4>
              <p style={{ fontSize: '0.78rem', color: '#94a3b8', margin: 0 }}>Driver: Robert Hayes • Contact: +1 555-0192</p>

              <div style={{
                marginTop: '1rem',
                padding: '0.85rem',
                backgroundColor: isDarkMode ? '#0a0f1d' : '#f1f5f9',
                borderRadius: '10px',
                fontSize: '0.8rem'
              }}>
                <div style={{ fontWeight: 700, color: '#38bdf8', marginBottom: '0.2rem' }}>Next Stop: Central Library Gate</div>
                <div style={{ color: '#94a3b8', fontSize: '0.72rem' }}>Estimated Arrival: 4 mins • Speed: 28 km/h</div>
              </div>
            </div>
          </div>
        )}

        {activeTab === 'profile' && (
          <div style={{
            padding: '1.5rem',
            backgroundColor: isDarkMode ? '#141e33' : '#ffffff',
            border: isDarkMode ? '1px solid rgba(255,255,255,0.08)' : '1px solid rgba(0,0,0,0.08)',
            borderRadius: '20px',
            boxShadow: '0 4px 15px rgba(0,0,0,0.15)'
          }}>
            <div style={{ textAlign: 'center', marginBottom: '1.25rem' }}>
              <div style={{
                width: '72px',
                height: '72px',
                borderRadius: '50%',
                background: 'linear-gradient(135deg, #0284c7 0%, #6366f1 100%)',
                color: '#fff',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                fontSize: '1.75rem',
                margin: '0 auto 0.75rem auto',
                fontWeight: 800,
                boxShadow: '0 8px 20px rgba(99, 102, 241, 0.35)'
              }}>
                {getInitials(user?.full_name)}
              </div>
              <h3 style={{ margin: 0, fontSize: '1.25rem', fontWeight: 800 }}>{user?.full_name || 'Guest User'}</h3>
              <span style={{ fontSize: '0.78rem', color: '#38bdf8', fontWeight: 700 }}>ID: US-2026-8891</span>
            </div>

            <div style={{ fontSize: '0.82rem', display: 'flex', flexDirection: 'column', gap: '0.65rem' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', padding: '0.5rem 0', borderBottom: isDarkMode ? '1px solid rgba(255,255,255,0.06)' : '1px solid rgba(0,0,0,0.06)' }}>
                <span style={{ color: '#94a3b8' }}>Email:</span>
                <span style={{ fontWeight: 600 }}>{user?.email || 'student@university.edu'}</span>
              </div>
              <div style={{ display: 'flex', justifyContent: 'space-between', padding: '0.5rem 0', borderBottom: isDarkMode ? '1px solid rgba(255,255,255,0.06)' : '1px solid rgba(0,0,0,0.06)' }}>
                <span style={{ color: '#94a3b8' }}>Role:</span>
                <span style={{ fontWeight: 700, color: '#818cf8' }}>{user?.role || 'STUDENT'}</span>
              </div>
              <div style={{ display: 'flex', justifyContent: 'space-between', padding: '0.5rem 0', borderBottom: isDarkMode ? '1px solid rgba(255,255,255,0.06)' : '1px solid rgba(0,0,0,0.06)' }}>
                <span style={{ color: '#94a3b8' }}>Campus Tenant:</span>
                <span style={{ fontWeight: 600 }}>{tenant?.name || 'Default Campus'}</span>
              </div>
              <div style={{ display: 'flex', justifyContent: 'space-between', padding: '0.5rem 0' }}>
                <span style={{ color: '#94a3b8' }}>Department:</span>
                <span style={{ fontWeight: 600 }}>Computer Science & Eng.</span>
              </div>
            </div>

            {user && (
              <button
                onClick={logout}
                style={{
                  width: '100%',
                  marginTop: '1.5rem',
                  padding: '0.75rem',
                  backgroundColor: 'rgba(239, 68, 68, 0.15)',
                  color: '#fca5a5',
                  border: '1px solid rgba(239, 68, 68, 0.35)',
                  borderRadius: '12px',
                  fontWeight: 700,
                  fontSize: '0.85rem',
                  cursor: 'pointer'
                }}
              >
                Sign Out of Account
              </button>
            )}
          </div>
        )}
      </main>

      {/* Fixed Mobile Bottom Navigation Bar */}
      <nav style={{
        position: 'fixed',
        bottom: 0,
        left: 0,
        right: 0,
        zIndex: 50,
        backgroundColor: isDarkMode ? 'rgba(15, 23, 42, 0.96)' : 'rgba(255, 255, 255, 0.96)',
        backdropFilter: 'blur(20px)',
        WebkitBackdropFilter: 'blur(20px)',
        borderTop: isDarkMode ? '1px solid rgba(255, 255, 255, 0.1)' : '1px solid rgba(0, 0, 0, 0.1)',
        display: 'flex',
        justifyContent: 'space-around',
        alignItems: 'center',
        padding: '0.5rem 0 0.75rem 0',
        boxShadow: '0 -4px 20px rgba(0, 0, 0, 0.25)'
      }}>
        {[
          { id: 'home', icon: '🏠', label: 'Hub' },
          { id: 'academics', icon: '📖', label: 'Academics' },
          { id: 'hostel', icon: '🎫', label: 'Hostel' },
          { id: 'transport', icon: '🚌', label: 'Bus Pass' },
          { id: 'profile', icon: '👤', label: 'Profile' }
        ].map(tab => {
          const isSelected = activeTab === tab.id;
          return (
            <button
              key={tab.id}
              onClick={() => setActiveTab(tab.id as any)}
              style={{
                background: 'none',
                border: 'none',
                display: 'flex',
                flexDirection: 'column',
                alignItems: 'center',
                gap: '0.2rem',
                color: isSelected ? '#38bdf8' : (isDarkMode ? '#64748b' : '#94a3b8'),
                fontSize: '0.68rem',
                fontWeight: isSelected ? 800 : 500,
                cursor: 'pointer',
                padding: '0.25rem 0.5rem',
                transition: 'all 0.15s ease'
              }}
            >
              <span style={{ fontSize: '1.25rem', transform: isSelected ? 'scale(1.15)' : 'scale(1)', transition: 'transform 0.15s ease' }}>
                {tab.icon}
              </span>
              <span>{tab.label}</span>
            </button>
          );
        })}
      </nav>
    </div>
  );
};

export default MobileNativePortalView;
