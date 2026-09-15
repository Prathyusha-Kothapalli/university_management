import React, { useState, useEffect } from 'react';
import { User } from '../types/auth';
import { useAuth } from '../features/auth/AuthContext';
import { api } from '../services/api';

export const UserPortalView: React.FC = () => {
  const { user, tenant } = useAuth();
  const [peers, setPeers] = useState<User[]>([]);
  const [searchTerm, setSearchTerm] = useState<string>('');
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchDirectory = async () => {
      try {
        const data = await api.getUsers();
        setPeers(data);
      } catch (err) {
        console.error('Failed to load campus directory', err);
      } finally {
        setLoading(false);
      }
    };
    fetchDirectory();
  }, []);

  const filteredPeers = peers.filter(p =>
    p.full_name.toLowerCase().includes(searchTerm.toLowerCase()) ||
    p.email.toLowerCase().includes(searchTerm.toLowerCase()) ||
    (p.department && p.department.toLowerCase().includes(searchTerm.toLowerCase()))
  );

  return (
    <div style={{ maxWidth: '1100px', margin: '2rem auto', padding: '0 1.5rem' }}>
      {/* Welcome Hero Card */}
      <div style={{
        background: 'linear-gradient(135deg, rgba(14, 21, 38, 0.9) 0%, rgba(22, 32, 54, 0.8) 100%)',
        backdropFilter: 'blur(16px)',
        border: '1px solid rgba(255, 255, 255, 0.1)',
        borderRadius: '16px',
        padding: '2rem 2.25rem',
        marginBottom: '2rem',
        boxShadow: '0 12px 32px -8px rgba(0, 0, 0, 0.4)'
      }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', flexWrap: 'wrap', gap: '1.25rem' }}>
          <div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '0.6rem', marginBottom: '0.6rem' }}>
              <span style={{
                backgroundColor: user?.role === 'FACULTY' ? 'rgba(59, 130, 246, 0.2)' : 'rgba(16, 185, 129, 0.2)',
                color: user?.role === 'FACULTY' ? '#93c5fd' : '#6ee7b7',
                border: `1px solid ${user?.role === 'FACULTY' ? 'rgba(59, 130, 246, 0.4)' : 'rgba(16, 185, 129, 0.4)'}`,
                fontSize: '0.74rem',
                fontWeight: 800,
                padding: '0.2rem 0.65rem',
                borderRadius: '9999px',
                letterSpacing: '0.04em'
              }}>
                {user?.role} PORTAL
              </span>
              <span style={{
                backgroundColor: 'rgba(2, 132, 199, 0.15)',
                color: '#38bdf8',
                border: '1px solid rgba(2, 132, 199, 0.35)',
                fontSize: '0.74rem',
                fontWeight: 700,
                padding: '0.2rem 0.65rem',
                borderRadius: '9999px'
              }}>
                {tenant?.code || 'INSTITUTION'}
              </span>
            </div>

            <h1 style={{ fontSize: '1.9rem', fontWeight: 800, color: '#f8fafc', margin: '0 0 0.35rem 0', letterSpacing: '-0.02em' }}>
              Welcome back, {user?.full_name}
            </h1>
            <p style={{ color: '#94a3b8', fontSize: '0.92rem', margin: 0, fontWeight: 500 }}>
              {tenant?.name} • {user?.department || 'Department of Computer Science'}
            </p>
          </div>

          <div style={{
            backgroundColor: 'rgba(2, 6, 23, 0.6)',
            border: '1px solid rgba(255, 255, 255, 0.08)',
            padding: '0.85rem 1.25rem',
            borderRadius: '12px',
            textAlign: 'right'
          }}>
            <div style={{ fontSize: '0.72rem', color: '#94a3b8', textTransform: 'uppercase', letterSpacing: '0.04em', fontWeight: 700 }}>
              Security Context
            </div>
            <div style={{ fontSize: '0.88rem', fontWeight: 700, color: '#34d399', marginTop: '0.25rem', display: 'flex', alignItems: 'center', gap: '0.35rem', justifyContent: 'flex-end' }}>
              <span style={{ width: '8px', height: '8px', borderRadius: '50%', backgroundColor: '#10b981' }} />
              <span>Multi-Tenant Isolated</span>
            </div>
          </div>
        </div>
      </div>

      {/* Grid of Profile & Permissions */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(320px, 1fr))', gap: '1.5rem', marginBottom: '2rem' }}>
        <div style={{
          backgroundColor: 'rgba(14, 21, 38, 0.75)',
          backdropFilter: 'blur(12px)',
          border: '1px solid rgba(255, 255, 255, 0.08)',
          borderRadius: '14px',
          padding: '1.5rem',
          boxShadow: '0 4px 20px -5px rgba(0, 0, 0, 0.3)'
        }}>
          <h3 style={{ fontSize: '1.05rem', fontWeight: 700, color: '#f8fafc', margin: '0 0 1rem 0', borderBottom: '1px solid rgba(255, 255, 255, 0.08)', paddingBottom: '0.65rem' }}>
            Academic Profile
          </h3>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '0.85rem', fontSize: '0.86rem' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between' }}>
              <span style={{ color: '#94a3b8' }}>Account Email</span>
              <span style={{ color: '#f8fafc', fontWeight: 600 }}>{user?.email}</span>
            </div>
            <div style={{ display: 'flex', justifyContent: 'space-between' }}>
              <span style={{ color: '#94a3b8' }}>Assigned Department</span>
              <span style={{ color: '#f8fafc', fontWeight: 600 }}>{user?.department || 'General Academics'}</span>
            </div>
            <div style={{ display: 'flex', justifyContent: 'space-between' }}>
              <span style={{ color: '#94a3b8' }}>Campus Identification</span>
              <span style={{ color: '#38bdf8', fontWeight: 700 }}>{tenant?.code} ({tenant?.name})</span>
            </div>
            <div style={{ display: 'flex', justifyContent: 'space-between' }}>
              <span style={{ color: '#94a3b8' }}>Institutional Domain</span>
              <span style={{ color: '#f8fafc', fontWeight: 600 }}>{tenant?.domain || 'stanford.edu'}</span>
            </div>
          </div>
        </div>

        <div style={{
          backgroundColor: 'rgba(14, 21, 38, 0.75)',
          backdropFilter: 'blur(12px)',
          border: '1px solid rgba(255, 255, 255, 0.08)',
          borderRadius: '14px',
          padding: '1.5rem',
          boxShadow: '0 4px 20px -5px rgba(0, 0, 0, 0.3)'
        }}>
          <h3 style={{ fontSize: '1.05rem', fontWeight: 700, color: '#f8fafc', margin: '0 0 1rem 0', borderBottom: '1px solid rgba(255, 255, 255, 0.08)', paddingBottom: '0.65rem' }}>
            Privileges & Tools
          </h3>
          <ul style={{ listStyle: 'none', padding: 0, margin: 0, fontSize: '0.86rem', color: '#cbd5e1', display: 'flex', flexDirection: 'column', gap: '0.65rem' }}>
            <li style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
              <span style={{ color: '#10b981', fontWeight: 800 }}>✓</span> Access verified syllabus notes & course materials
            </li>
            <li style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
              <span style={{ color: '#10b981', fontWeight: 800 }}>✓</span> Query UniSphere AI Study Copilot with RAG grounding
            </li>
            <li style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
              <span style={{ color: '#10b981', fontWeight: 800 }}>✓</span> Institutional campus member directory search
            </li>
            <li style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
              <span style={{ color: '#64748b' }}>✕</span> Tenant configuration & administrative controls (Restricted)
            </li>
          </ul>
        </div>
      </div>

      {/* Campus Directory Table */}
      <div style={{
        backgroundColor: 'rgba(14, 21, 38, 0.85)',
        backdropFilter: 'blur(16px)',
        border: '1px solid rgba(255, 255, 255, 0.08)',
        borderRadius: '16px',
        padding: '1.75rem',
        boxShadow: '0 8px 30px rgba(0, 0, 0, 0.4)'
      }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1.25rem', flexWrap: 'wrap', gap: '0.75rem' }}>
          <div>
            <h3 style={{ fontSize: '1.15rem', fontWeight: 700, color: '#f8fafc', margin: 0 }}>
              {tenant?.name} Member Directory
            </h3>
            <p style={{ color: '#94a3b8', fontSize: '0.8rem', margin: '0.2rem 0 0 0' }}>
              Verified faculty, staff, and enrolled scholars in your tenant
            </p>
          </div>

          <input
            type="text"
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            placeholder="Search by name, email, or dept..."
            style={{
              padding: '0.55rem 0.95rem',
              backgroundColor: 'rgba(2, 6, 23, 0.6)',
              border: '1px solid rgba(255, 255, 255, 0.12)',
              borderRadius: '8px',
              color: '#f8fafc',
              fontSize: '0.82rem',
              outline: 'none',
              minWidth: '240px'
            }}
          />
        </div>

        {loading ? (
          <div style={{ color: '#94a3b8', textAlign: 'center', padding: '2rem' }}>Loading verified campus directory...</div>
        ) : (
          <div style={{ overflowX: 'auto' }}>
            <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left', fontSize: '0.86rem' }}>
              <thead>
                <tr style={{ borderBottom: '1px solid rgba(255, 255, 255, 0.1)', color: '#94a3b8' }}>
                  <th style={{ padding: '0.75rem 0.6rem', fontWeight: 600 }}>Member Name</th>
                  <th style={{ padding: '0.75rem 0.6rem', fontWeight: 600 }}>Email Address</th>
                  <th style={{ padding: '0.75rem 0.6rem', fontWeight: 600 }}>Role</th>
                  <th style={{ padding: '0.75rem 0.6rem', fontWeight: 600 }}>Department</th>
                </tr>
              </thead>
              <tbody>
                {filteredPeers.map(p => (
                  <tr key={p.id} style={{ borderBottom: '1px solid rgba(255, 255, 255, 0.05)', transition: 'background 0.15s' }}>
                    <td style={{ padding: '0.75rem 0.6rem', fontWeight: 600, color: '#f8fafc' }}>{p.full_name}</td>
                    <td style={{ padding: '0.75rem 0.6rem', color: '#cbd5e1' }}>{p.email}</td>
                    <td style={{ padding: '0.75rem 0.6rem' }}>
                      <span style={{
                        backgroundColor: p.role === 'FACULTY' ? 'rgba(59, 130, 246, 0.15)' : 'rgba(16, 185, 129, 0.15)',
                        color: p.role === 'FACULTY' ? '#93c5fd' : '#6ee7b7',
                        border: `1px solid ${p.role === 'FACULTY' ? 'rgba(59, 130, 246, 0.35)' : 'rgba(16, 185, 129, 0.35)'}`,
                        padding: '0.15rem 0.5rem',
                        borderRadius: '6px',
                        fontSize: '0.72rem',
                        fontWeight: 700
                      }}>
                        {p.role}
                      </span>
                    </td>
                    <td style={{ padding: '0.75rem 0.6rem', color: '#94a3b8' }}>{p.department || '—'}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>
    </div>
  );
};

