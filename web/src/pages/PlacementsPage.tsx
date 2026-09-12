import React, { useState } from 'react';
import { User } from '../types/auth';

interface PlacementsPageProps {
  user: User | null;
}

interface DriveItem {
  id: string;
  company: string;
  logo: string;
  role: string;
  pkg: string;
  pkgRaw: number;
  deadline: string;
  location: string;
  eligibility: string;
  rounds: string[];
  openings: number;
}

export const PlacementsPage: React.FC<PlacementsPageProps> = ({ user }) => {
  const [tab, setTab] = useState<'all' | 'applied' | 'superDream'>('all');
  const [appliedIds, setAppliedIds] = useState<string[]>(['p3']);
  const [searchQuery, setSearchQuery] = useState('');
  const [notification, setNotification] = useState<string | null>(null);

  const drives: DriveItem[] = [
    {
      id: 'p1',
      company: 'Google',
      logo: '🌐',
      role: 'Software Engineer - AI & Core Distributed Systems',
      pkg: '₹48.5 LPA ($190,000)',
      pkgRaw: 48.5,
      deadline: 'Sep 25, 2026',
      location: 'Mountain View / Bengaluru',
      eligibility: 'CGPA ≥ 8.5 • CS/AI/ECE • No active backlogs',
      rounds: ['Online Coding Challenge (LeetCode Hard)', 'Technical Round 1 (Algorithms)', 'Technical Round 2 (System Design)', 'Googliness & Leadership'],
      openings: 12,
    },
    {
      id: 'p2',
      company: 'NVIDIA',
      logo: '⚡',
      role: 'Deep Learning Systems Engineer (CUDA/TensorRT)',
      pkg: '₹52.0 LPA ($210,000)',
      pkgRaw: 52.0,
      deadline: 'Oct 02, 2026',
      location: 'Santa Clara / Pune',
      eligibility: 'CGPA ≥ 8.8 • CS/AI/EE • CUDA/C++ preferred',
      rounds: ['GPU Architectures OA', 'CUDA & Concurrency Interview', 'Deep Learning Graph Optimization', 'Engineering Director Round'],
      openings: 8,
    },
    {
      id: 'p3',
      company: 'Microsoft',
      logo: '🪟',
      role: 'Azure Cloud Platforms Engineer',
      pkg: '₹44.0 LPA ($175,000)',
      pkgRaw: 44.0,
      deadline: 'Sep 20, 2026',
      location: 'Redmond / Hyderabad',
      eligibility: 'CGPA ≥ 8.0 • All Engineering Branches',
      rounds: ['Online Assessment', 'Data Structures & System Coding', 'Cloud Distributed Systems', 'AA Behavioral Round'],
      openings: 20,
    },
    {
      id: 'p4',
      company: 'Apple',
      logo: '🍎',
      role: 'Embedded Software Engineer - Apple Intelligence',
      pkg: '₹46.5 LPA ($185,000)',
      pkgRaw: 46.5,
      deadline: 'Oct 10, 2026',
      location: 'Cupertino / Bengaluru',
      eligibility: 'CGPA ≥ 8.5 • CS/ECE • C/C++/RTOS',
      rounds: ['Embedded Coding Assessment', 'Low-Level Systems Design', 'Kernel & Driver Architecture', 'Team Cultural Fit'],
      openings: 6,
    },
    {
      id: 'p5',
      company: 'Amazon Web Services',
      logo: '📦',
      role: 'SDE-1 Distributed High-Throughput Services',
      pkg: '₹42.0 LPA ($165,000)',
      pkgRaw: 42.0,
      deadline: 'Sep 28, 2026',
      location: 'Seattle / Hyderabad',
      eligibility: 'CGPA ≥ 8.0 • CS/IT/ECE',
      rounds: ['Amazon OA1 & OA2 (Work Simulation)', 'Technical DSA Round 1', 'Object-Oriented Design Round', 'Bar Raiser Interview'],
      openings: 25,
    },
    {
      id: 'p6',
      company: 'OpenAI',
      logo: '🔮',
      role: 'Applied AI Researcher & Systems Fellow',
      pkg: '₹58.0 LPA ($220,000)',
      pkgRaw: 58.0,
      deadline: 'Oct 15, 2026',
      location: 'San Francisco / Remote',
      eligibility: 'CGPA ≥ 9.0 • Top 5% Departmental Standing',
      rounds: ['Research Code Review', 'Transformers & Alignment Deep Dive', 'Distributed Training at Scale', 'Founding Team Chat'],
      openings: 3,
    },
  ];

  const handleApply = (drive: DriveItem) => {
    if (!appliedIds.includes(drive.id)) {
      setAppliedIds([...appliedIds, drive.id]);
      setNotification(`Application for ${drive.company} (${drive.role}) successfully submitted to Placement Cell!`);
      setTimeout(() => setNotification(null), 3500);
    }
  };

  const filteredDrives = drives.filter((d) => {
    if (tab === 'applied' && !appliedIds.includes(d.id)) return false;
    if (tab === 'superDream' && d.pkgRaw < 45) return false;
    if (searchQuery.trim()) {
      const q = searchQuery.toLowerCase();
      return (
        d.company.toLowerCase().includes(q) ||
        d.role.toLowerCase().includes(q) ||
        d.location.toLowerCase().includes(q)
      );
    }
    return true;
  });

  return (
    <div style={{ maxWidth: '1200px', margin: '0 auto', padding: '2rem 1.5rem', width: '100%' }}>
      {/* Toast Alert */}
      {notification && (
        <div style={{
          position: 'fixed',
          bottom: '24px',
          right: '24px',
          padding: '12px 20px',
          backgroundColor: '#059669',
          color: '#ffffff',
          borderRadius: '12px',
          boxShadow: 'var(--shadow-lg)',
          zIndex: 1000,
          fontWeight: 700,
          fontSize: '0.9rem',
          display: 'flex',
          alignItems: 'center',
          gap: '8px',
          border: '1px solid rgba(255, 255, 255, 0.3)',
        }}>
          <span>⚡</span>
          <span>{notification}</span>
        </div>
      )}

      {/* Hero Placement Banner */}
      <div style={{
        background: 'linear-gradient(135deg, #065f46 0%, #059669 50%, #0d9488 100%)',
        borderRadius: 'var(--radius-lg)',
        padding: '2.25rem',
        boxShadow: 'var(--shadow-md)',
        marginBottom: '2rem',
        color: '#ffffff',
      }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', flexWrap: 'wrap', gap: '1.5rem' }}>
          <div>
            <div style={{
              display: 'inline-flex',
              alignItems: 'center',
              gap: '6px',
              padding: '4px 12px',
              borderRadius: '20px',
              backgroundColor: 'rgba(255, 255, 255, 0.2)',
              fontSize: '0.75rem',
              fontWeight: 700,
              textTransform: 'uppercase',
              letterSpacing: '0.5px',
              marginBottom: '10px',
            }}>
              🎓 Student Module • University Career Placement Cell
            </div>
            <h1 style={{ fontSize: '2.2rem', fontWeight: 800, letterSpacing: '-0.5px' }}>
              Campus Placement Portal 2026
            </h1>
            <p style={{ fontSize: '1rem', opacity: 0.9, marginTop: '4px' }}>
              Connect with premier global technology recruiters, track applications, and attend on-campus interviews.
            </p>
          </div>

          {/* Student Status Card */}
          <div style={{
            backgroundColor: 'rgba(0, 0, 0, 0.25)',
            backdropFilter: 'blur(12px)',
            padding: '1rem 1.25rem',
            borderRadius: '14px',
            border: '1px solid rgba(255, 255, 255, 0.2)',
            minWidth: '240px',
          }}>
            <div style={{ fontSize: '0.78rem', opacity: 0.85 }}>Your Placement Standing</div>
            <div style={{ fontSize: '1.3rem', fontWeight: 800, color: '#34d399', marginTop: '2px' }}>
              Eligible: Super Dream Tier
            </div>
            <div style={{ fontSize: '0.75rem', opacity: 0.9, marginTop: '4px' }}>
              CGPA: <strong>{user?.gpa ? user.gpa.toFixed(2) : '9.42'}</strong> • Dept Rank: <strong>#4</strong>
            </div>
            <div style={{ fontSize: '0.72rem', color: '#6ee7b7', marginTop: '2px' }}>
              ✓ Resume Verified by Placement Officer
            </div>
          </div>
        </div>

        {/* Quick Placement Stats */}
        <div style={{
          display: 'grid',
          gridTemplateColumns: 'repeat(auto-fit, minmax(180px, 1fr))',
          gap: '1rem',
          marginTop: '1.75rem',
          paddingTop: '1.5rem',
          borderTop: '1px solid rgba(255, 255, 255, 0.2)',
        }}>
          <div>
            <div style={{ fontSize: '0.8rem', opacity: 0.85 }}>Highest Package</div>
            <div style={{ fontSize: '1.6rem', fontWeight: 800 }}>₹58.0 LPA</div>
          </div>
          <div>
            <div style={{ fontSize: '0.8rem', opacity: 0.85 }}>Average CTC</div>
            <div style={{ fontSize: '1.6rem', fontWeight: 800 }}>₹19.4 LPA</div>
          </div>
          <div>
            <div style={{ fontSize: '0.8rem', opacity: 0.85 }}>Placement Percentage</div>
            <div style={{ fontSize: '1.6rem', fontWeight: 800 }}>96.4% Placed</div>
          </div>
          <div>
            <div style={{ fontSize: '0.8rem', opacity: 0.85 }}>Active Drives</div>
            <div style={{ fontSize: '1.6rem', fontWeight: 800 }}>{drives.length} Openings</div>
          </div>
        </div>
      </div>

      {/* Filter and Search Bar */}
      <div style={{
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center',
        flexWrap: 'wrap',
        gap: '1rem',
        marginBottom: '1.75rem',
      }}>
        <div style={{ display: 'flex', gap: '8px' }}>
          <button
            onClick={() => setTab('all')}
            style={{
              padding: '8px 18px',
              borderRadius: '10px',
              border: tab === 'all' ? '1.5px solid #10b981' : '1px solid var(--color-border)',
              backgroundColor: tab === 'all' ? 'rgba(16, 185, 129, 0.2)' : 'rgba(28, 37, 65, 0.6)',
              color: tab === 'all' ? '#34d399' : '#94a3b8',
              fontWeight: 700,
              fontSize: '0.875rem',
              cursor: 'pointer',
            }}
          >
            All Campus Drives ({drives.length})
          </button>
          <button
            onClick={() => setTab('applied')}
            style={{
              padding: '8px 18px',
              borderRadius: '10px',
              border: tab === 'applied' ? '1.5px solid #10b981' : '1px solid var(--color-border)',
              backgroundColor: tab === 'applied' ? 'rgba(16, 185, 129, 0.2)' : 'rgba(28, 37, 65, 0.6)',
              color: tab === 'applied' ? '#34d399' : '#94a3b8',
              fontWeight: 700,
              fontSize: '0.875rem',
              cursor: 'pointer',
            }}
          >
            My Applications ({appliedIds.length})
          </button>
          <button
            onClick={() => setTab('superDream')}
            style={{
              padding: '8px 18px',
              borderRadius: '10px',
              border: tab === 'superDream' ? '1.5px solid #10b981' : '1px solid var(--color-border)',
              backgroundColor: tab === 'superDream' ? 'rgba(16, 185, 129, 0.2)' : 'rgba(28, 37, 65, 0.6)',
              color: tab === 'superDream' ? '#34d399' : '#94a3b8',
              fontWeight: 700,
              fontSize: '0.875rem',
              cursor: 'pointer',
            }}
          >
            Super Dream ≥ ₹45 LPA
          </button>
        </div>

        <div style={{ minWidth: '260px' }}>
          <input
            type="text"
            className="form-input"
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            placeholder="🔍 Search company or role..."
            style={{ padding: '8px 14px', fontSize: '0.875rem' }}
          />
        </div>
      </div>

      {/* Drives List */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(360px, 1fr))', gap: '1.25rem' }}>
        {filteredDrives.map((d) => {
          const isApplied = appliedIds.includes(d.id);

          return (
            <div
              key={d.id}
              className="glass-panel"
              style={{
                padding: '1.5rem',
                display: 'flex',
                flexDirection: 'column',
                justifyContent: 'space-between',
                borderTop: isApplied ? '4px solid #10b981' : '4px solid #3b82f6',
              }}
            >
              <div>
                {/* Header */}
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                    <span style={{ fontSize: '2rem' }}>{d.logo}</span>
                    <div>
                      <h3 style={{ fontSize: '1.2rem', fontWeight: 800, color: '#f8fafc' }}>
                        {d.company}
                      </h3>
                      <span style={{ fontSize: '0.78rem', color: '#94a3b8' }}>
                        📍 {d.location}
                      </span>
                    </div>
                  </div>

                  <span style={{
                    fontSize: '0.825rem',
                    fontWeight: 800,
                    color: '#34d399',
                    backgroundColor: 'rgba(52, 211, 153, 0.15)',
                    padding: '4px 10px',
                    borderRadius: '8px',
                    border: '1px solid rgba(52, 211, 153, 0.3)',
                  }}>
                    {d.pkg}
                  </span>
                </div>

                {/* Role */}
                <div style={{ fontSize: '0.975rem', fontWeight: 700, color: '#e2e8f0', marginTop: '12px' }}>
                  {d.role}
                </div>

                {/* Criteria */}
                <div style={{
                  backgroundColor: 'rgba(15, 23, 42, 0.6)',
                  padding: '10px 12px',
                  borderRadius: '10px',
                  marginTop: '10px',
                  fontSize: '0.78rem',
                  color: '#94a3b8',
                  display: 'flex',
                  flexDirection: 'column',
                  gap: '4px',
                }}>
                  <div>🎯 <strong>Eligibility:</strong> {d.eligibility}</div>
                  <div>⏳ <strong>Application Deadline:</strong> {d.deadline}</div>
                  <div>👥 <strong>Campus Quota:</strong> {d.openings} positions</div>
                </div>

                {/* Rounds */}
                <div style={{ marginTop: '12px' }}>
                  <div style={{ fontSize: '0.75rem', fontWeight: 700, color: '#64748b', textTransform: 'uppercase', marginBottom: '6px' }}>
                    Selection Process ({d.rounds.length} Rounds):
                  </div>
                  <div style={{ display: 'flex', flexWrap: 'wrap', gap: '4px' }}>
                    {d.rounds.map((r, idx) => (
                      <span
                        key={idx}
                        style={{
                          fontSize: '0.7rem',
                          padding: '2px 8px',
                          borderRadius: '6px',
                          backgroundColor: 'rgba(255, 255, 255, 0.06)',
                          color: '#cbd5e1',
                        }}
                      >
                        {idx + 1}. {r.split('(')[0]}
                      </span>
                    ))}
                  </div>
                </div>
              </div>

              {/* Action */}
              <div style={{ marginTop: '1.25rem', paddingTop: '1rem', borderTop: '1px solid rgba(255, 255, 255, 0.08)' }}>
                <button
                  onClick={() => handleApply(d)}
                  disabled={isApplied}
                  className={`btn ${isApplied ? 'btn-secondary' : 'btn-primary'}`}
                  style={{
                    width: '100%',
                    padding: '10px',
                    fontSize: '0.875rem',
                    fontWeight: 700,
                    cursor: isApplied ? 'default' : 'pointer',
                    background: isApplied ? 'rgba(16, 185, 129, 0.15)' : undefined,
                    color: isApplied ? '#34d399' : undefined,
                    borderColor: isApplied ? 'rgba(16, 185, 129, 0.4)' : undefined,
                  }}
                >
                  {isApplied ? '✓ Application Submitted (Under Review)' : '⚡ 1-Tap Campus Apply'}
                </button>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
};
