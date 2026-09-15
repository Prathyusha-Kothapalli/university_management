import React, { useState, useEffect } from 'react';
import { Tenant, User } from '../types/auth';
import { api } from '../services/api';

export const SuperAdminDashboard: React.FC = () => {
  const [tenants, setTenants] = useState<Tenant[]>([]);
  const [users, setUsers] = useState<User[]>([]);
  const [selectedTenantFilter, setSelectedTenantFilter] = useState<string>('');
  const [loading, setLoading] = useState<boolean>(true);
  const [message, setMessage] = useState<{ text: string; type: 'success' | 'error' } | null>(null);

  // New Tenant Modal / Form
  const [showAddTenant, setShowAddTenant] = useState(false);
  const [newTenantName, setNewTenantName] = useState('');
  const [newTenantCode, setNewTenantCode] = useState('');
  const [newTenantDomain, setNewTenantDomain] = useState('');
  const [newTenantDesc, setNewTenantDesc] = useState('');

  const fetchData = async () => {
    setLoading(true);
    try {
      const [tenantsList, usersList] = await Promise.all([
        api.getTenants(),
        api.getUsers(selectedTenantFilter ? { tenant_id: selectedTenantFilter } : undefined)
      ]);
      setTenants(tenantsList);
      setUsers(usersList);
    } catch (err: any) {
      setMessage({ text: err.message || 'Failed to fetch global system data', type: 'error' });
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
  }, [selectedTenantFilter]);

  const handleCreateTenant = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await api.createTenant({
        name: newTenantName,
        code: newTenantCode,
        domain: newTenantDomain || undefined,
        description: newTenantDesc || undefined,
      });
      setMessage({ text: `Institution '${newTenantName}' created successfully!`, type: 'success' });
      setShowAddTenant(false);
      setNewTenantName('');
      setNewTenantCode('');
      setNewTenantDomain('');
      setNewTenantDesc('');
      fetchData();
    } catch (err: any) {
      setMessage({ text: err.message || 'Failed to create tenant', type: 'error' });
    }
  };

  const handleDeleteUser = async (userId: string, userName: string) => {
    if (!confirm(`Are you sure you want to remove user "${userName}"?`)) return;
    try {
      await api.deleteUser(userId);
      setMessage({ text: `User "${userName}" deleted.`, type: 'success' });
      fetchData();
    } catch (err: any) {
      setMessage({ text: err.message || 'Failed to delete user', type: 'error' });
    }
  };

  return (
    <div style={{ maxWidth: '1240px', margin: '2rem auto', padding: '0 1.5rem' }}>
      {/* Header & Metrics */}
      <div style={{
        background: 'linear-gradient(135deg, rgba(14, 21, 38, 0.9) 0%, rgba(22, 32, 54, 0.8) 100%)',
        backdropFilter: 'blur(16px)',
        border: '1px solid rgba(255, 255, 255, 0.1)',
        borderRadius: '16px',
        padding: '2rem 2.25rem',
        marginBottom: '2rem',
        boxShadow: '0 12px 32px -8px rgba(0, 0, 0, 0.4)',
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center',
        flexWrap: 'wrap',
        gap: '1.25rem'
      }}>
        <div>
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem', flexWrap: 'wrap' }}>
            <h1 style={{ fontSize: '1.85rem', fontWeight: 800, color: '#f8fafc', margin: 0, letterSpacing: '-0.02em' }}>
              Super Admin Control Center
            </h1>
            <span style={{
              backgroundColor: 'rgba(239, 68, 68, 0.15)',
              border: '1px solid rgba(239, 68, 68, 0.35)',
              color: '#f87171',
              fontSize: '0.75rem',
              fontWeight: 800,
              padding: '0.25rem 0.75rem',
              borderRadius: '9999px',
              fontFamily: "'JetBrains Mono', monospace",
              letterSpacing: '0.04em'
            }}>
              GLOBAL ROOT
            </span>
          </div>
          <p style={{ color: '#94a3b8', fontSize: '0.92rem', marginTop: '0.4rem', marginBottom: 0 }}>
            Cross-Tenant Governance & Global Multi-Institution Management
          </p>
        </div>
        <button
          onClick={() => setShowAddTenant(true)}
          style={{
            background: 'linear-gradient(135deg, #0284c7 0%, #0369a1 100%)',
            color: '#fff',
            border: '1px solid rgba(56, 189, 248, 0.3)',
            padding: '0.75rem 1.4rem',
            borderRadius: '10px',
            fontWeight: 700,
            cursor: 'pointer',
            fontSize: '0.9rem',
            boxShadow: '0 4px 14px rgba(2, 132, 199, 0.35)',
            display: 'flex',
            alignItems: 'center',
            gap: '0.5rem',
            transition: 'all 0.2s ease'
          }}
        >
          <span style={{ fontSize: '1.1rem' }}>+</span> Add New University
        </button>
      </div>

      {message && (
        <div style={{
          backgroundColor: message.type === 'success' ? 'rgba(16, 185, 129, 0.12)' : 'rgba(239, 68, 68, 0.12)',
          border: `1px solid ${message.type === 'success' ? 'rgba(16, 185, 129, 0.3)' : 'rgba(239, 68, 68, 0.3)'}`,
          color: message.type === 'success' ? '#6ee7b7' : '#fca5a5',
          padding: '0.85rem 1.25rem',
          borderRadius: '10px',
          marginBottom: '1.75rem',
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          backdropFilter: 'blur(8px)'
        }}>
          <span style={{ fontSize: '0.9rem', fontWeight: 600 }}>{message.text}</span>
          <button onClick={() => setMessage(null)} style={{ background: 'none', border: 'none', color: 'inherit', cursor: 'pointer', fontSize: '1rem' }}>✕</button>
        </div>
      )}

      {/* Metrics Cards */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(240px, 1fr))', gap: '1.25rem', marginBottom: '2rem' }}>
        <div style={{
          background: 'rgba(15, 23, 42, 0.7)',
          backdropFilter: 'blur(12px)',
          border: '1px solid rgba(255, 255, 255, 0.08)',
          borderRadius: '12px',
          padding: '1.4rem'
        }}>
          <div style={{ color: '#94a3b8', fontSize: '0.8rem', fontWeight: 700, textTransform: 'uppercase', letterSpacing: '0.04em' }}>Total Institutions</div>
          <div style={{ fontSize: '2.2rem', fontWeight: 800, color: '#38bdf8', marginTop: '0.35rem', letterSpacing: '-0.02em' }}>{tenants.length}</div>
        </div>
        <div style={{
          background: 'rgba(15, 23, 42, 0.7)',
          backdropFilter: 'blur(12px)',
          border: '1px solid rgba(255, 255, 255, 0.08)',
          borderRadius: '12px',
          padding: '1.4rem'
        }}>
          <div style={{ color: '#94a3b8', fontSize: '0.8rem', fontWeight: 700, textTransform: 'uppercase', letterSpacing: '0.04em' }}>Active Tenants</div>
          <div style={{ fontSize: '2.2rem', fontWeight: 800, color: '#10b981', marginTop: '0.35rem', letterSpacing: '-0.02em' }}>
            {tenants.filter(t => t.is_active).length}
          </div>
        </div>
        <div style={{
          background: 'rgba(15, 23, 42, 0.7)',
          backdropFilter: 'blur(12px)',
          border: '1px solid rgba(255, 255, 255, 0.08)',
          borderRadius: '12px',
          padding: '1.4rem'
        }}>
          <div style={{ color: '#94a3b8', fontSize: '0.8rem', fontWeight: 700, textTransform: 'uppercase', letterSpacing: '0.04em' }}>Global Users Loaded</div>
          <div style={{ fontSize: '2.2rem', fontWeight: 800, color: '#f59e0b', marginTop: '0.35rem', letterSpacing: '-0.02em' }}>{users.length}</div>
        </div>
      </div>

      {/* Tenants Grid */}
      <div style={{ marginBottom: '2.5rem' }}>
        <h2 style={{ fontSize: '1.3rem', fontWeight: 700, color: '#f8fafc', marginBottom: '1.2rem', letterSpacing: '-0.01em' }}>
          Registered Universities & Institutions
        </h2>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(340px, 1fr))', gap: '1.25rem' }}>
          {tenants.map(t => (
            <div key={t.id} style={{
              background: 'rgba(15, 23, 42, 0.75)',
              backdropFilter: 'blur(16px)',
              border: selectedTenantFilter === t.id ? '2px solid #38bdf8' : '1px solid rgba(255, 255, 255, 0.08)',
              borderRadius: '14px',
              padding: '1.5rem',
              display: 'flex',
              flexDirection: 'column',
              justifyContent: 'space-between',
              boxShadow: selectedTenantFilter === t.id ? '0 0 24px rgba(56, 189, 248, 0.2)' : '0 6px 20px rgba(0, 0, 0, 0.2)',
              transition: 'all 0.2s ease'
            }}>
              <div>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: '0.65rem' }}>
                  <h3 style={{ fontSize: '1.15rem', fontWeight: 700, color: '#f8fafc', margin: 0 }}>{t.name}</h3>
                  <span style={{
                    backgroundColor: 'rgba(56, 189, 248, 0.12)',
                    color: '#38bdf8',
                    border: '1px solid rgba(56, 189, 248, 0.3)',
                    padding: '0.2rem 0.55rem',
                    borderRadius: '6px',
                    fontSize: '0.75rem',
                    fontWeight: 700,
                    fontFamily: "'JetBrains Mono', monospace"
                  }}>
                    {t.code}
                  </span>
                </div>
                <div style={{ color: '#94a3b8', fontSize: '0.85rem', marginBottom: '0.5rem' }}>
                  Domain: <span style={{ color: '#cbd5e1', fontFamily: "'JetBrains Mono', monospace", fontSize: '0.8rem' }}>{t.domain || 'N/A'}</span>
                </div>
                {t.description && (
                  <p style={{ color: '#64748b', fontSize: '0.82rem', margin: 0, marginBottom: '0.85rem', lineHeight: 1.5 }}>
                    {t.description}
                  </p>
                )}
              </div>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderTop: '1px solid rgba(255, 255, 255, 0.08)', paddingTop: '0.85rem', marginTop: '0.75rem' }}>
                <span style={{
                  color: t.is_active ? '#10b981' : '#ef4444',
                  fontSize: '0.78rem',
                  fontWeight: 600
                }}>
                  ● {t.is_active ? 'Active' : 'Inactive'}
                </span>
                <button
                  onClick={() => setSelectedTenantFilter(selectedTenantFilter === t.id ? '' : t.id)}
                  style={{
                    backgroundColor: selectedTenantFilter === t.id ? 'rgba(56, 189, 248, 0.2)' : 'rgba(255, 255, 255, 0.08)',
                    color: selectedTenantFilter === t.id ? '#38bdf8' : '#f8fafc',
                    border: selectedTenantFilter === t.id ? '1px solid rgba(56, 189, 248, 0.4)' : '1px solid rgba(255, 255, 255, 0.08)',
                    padding: '0.45rem 0.85rem',
                    borderRadius: '8px',
                    fontSize: '0.78rem',
                    fontWeight: 700,
                    cursor: 'pointer',
                    transition: 'all 0.15s ease'
                  }}
                >
                  {selectedTenantFilter === t.id ? 'Viewing Users' : 'Filter Users'}
                </button>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* User Directory */}
      <div style={{
        background: 'rgba(15, 23, 42, 0.75)',
        backdropFilter: 'blur(16px)',
        border: '1px solid rgba(255, 255, 255, 0.08)',
        borderRadius: '14px',
        padding: '1.75rem',
        boxShadow: '0 8px 30px rgba(0, 0, 0, 0.25)'
      }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1.5rem', flexWrap: 'wrap', gap: '0.75rem' }}>
          <div>
            <h2 style={{ fontSize: '1.3rem', fontWeight: 700, color: '#f8fafc', margin: 0 }}>
              Global User Directory
            </h2>
            {selectedTenantFilter ? (
              <span style={{ fontSize: '0.82rem', color: '#38bdf8', marginTop: '0.25rem', display: 'inline-block' }}>
                Filtered by institution ID: {selectedTenantFilter} (
                <button onClick={() => setSelectedTenantFilter('')} style={{ color: '#fca5a5', background: 'none', border: 'none', cursor: 'pointer', textDecoration: 'underline', marginLeft: '0.25rem' }}>Clear filter</button>
                )
              </span>
            ) : (
              <p style={{ color: '#64748b', fontSize: '0.85rem', margin: '0.2rem 0 0 0' }}>
                Showing all registered system accounts across all educational tenants
              </p>
            )}
          </div>
        </div>

        {loading ? (
          <div style={{ color: '#94a3b8', textAlign: 'center', padding: '3rem', fontSize: '0.92rem' }}>Loading directory...</div>
        ) : (
          <div style={{ overflowX: 'auto' }}>
            <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left', fontSize: '0.88rem' }}>
              <thead>
                <tr style={{ borderBottom: '1px solid rgba(255, 255, 255, 0.08)', color: '#94a3b8' }}>
                  <th style={{ padding: '0.85rem 0.6rem', fontWeight: 700, fontSize: '0.78rem', textTransform: 'uppercase', letterSpacing: '0.04em' }}>Name</th>
                  <th style={{ padding: '0.85rem 0.6rem', fontWeight: 700, fontSize: '0.78rem', textTransform: 'uppercase', letterSpacing: '0.04em' }}>Email</th>
                  <th style={{ padding: '0.85rem 0.6rem', fontWeight: 700, fontSize: '0.78rem', textTransform: 'uppercase', letterSpacing: '0.04em' }}>Role</th>
                  <th style={{ padding: '0.85rem 0.6rem', fontWeight: 700, fontSize: '0.78rem', textTransform: 'uppercase', letterSpacing: '0.04em' }}>Department</th>
                  <th style={{ padding: '0.85rem 0.6rem', fontWeight: 700, fontSize: '0.78rem', textTransform: 'uppercase', letterSpacing: '0.04em' }}>Institution</th>
                  <th style={{ padding: '0.85rem 0.6rem', textAlign: 'right', fontWeight: 700, fontSize: '0.78rem', textTransform: 'uppercase', letterSpacing: '0.04em' }}>Actions</th>
                </tr>
              </thead>
              <tbody>
                {users.map(u => (
                  <tr key={u.id} style={{ borderBottom: '1px solid rgba(255, 255, 255, 0.04)', transition: 'background-color 0.15s' }}>
                    <td style={{ padding: '0.85rem 0.6rem', fontWeight: 600, color: '#f8fafc' }}>{u.full_name}</td>
                    <td style={{ padding: '0.85rem 0.6rem', color: '#cbd5e1', fontFamily: "'JetBrains Mono', monospace", fontSize: '0.82rem' }}>{u.email}</td>
                    <td style={{ padding: '0.85rem 0.6rem' }}>
                      <span style={{
                        backgroundColor: u.role === 'SUPER_ADMIN' ? 'rgba(239, 68, 68, 0.18)' : u.role === 'UNIVERSITY_ADMIN' ? 'rgba(245, 158, 11, 0.18)' : 'rgba(59, 130, 246, 0.18)',
                        color: u.role === 'SUPER_ADMIN' ? '#f87171' : u.role === 'UNIVERSITY_ADMIN' ? '#fcd34d' : '#93c5fd',
                        border: `1px solid ${u.role === 'SUPER_ADMIN' ? 'rgba(239, 68, 68, 0.3)' : u.role === 'UNIVERSITY_ADMIN' ? 'rgba(245, 158, 11, 0.3)' : 'rgba(59, 130, 246, 0.3)'}`,
                        padding: '0.2rem 0.55rem',
                        borderRadius: '6px',
                        fontSize: '0.72rem',
                        fontWeight: 700,
                        letterSpacing: '0.03em'
                      }}>
                        {u.role}
                      </span>
                    </td>
                    <td style={{ padding: '0.85rem 0.6rem', color: '#94a3b8' }}>{u.department || '—'}</td>
                    <td style={{ padding: '0.85rem 0.6rem', color: '#94a3b8' }}>
                      {u.tenant ? `${u.tenant.name} (${u.tenant.code})` : u.tenant_id ? u.tenant_id : 'Global'}
                    </td>
                    <td style={{ padding: '0.85rem 0.6rem', textAlign: 'right' }}>
                      {u.role !== 'SUPER_ADMIN' && (
                        <button
                          onClick={() => handleDeleteUser(u.id, u.full_name)}
                          style={{
                            backgroundColor: 'rgba(239, 68, 68, 0.1)',
                            color: '#f87171',
                            border: '1px solid rgba(239, 68, 68, 0.25)',
                            padding: '0.3rem 0.65rem',
                            borderRadius: '6px',
                            cursor: 'pointer',
                            fontSize: '0.75rem',
                            fontWeight: 600,
                            transition: 'all 0.15s ease'
                          }}
                        >
                          Delete
                        </button>
                      )}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>

      {/* Add Tenant Modal */}
      {showAddTenant && (
        <div style={{
          position: 'fixed',
          top: 0,
          left: 0,
          right: 0,
          bottom: 0,
          backgroundColor: 'rgba(0, 0, 0, 0.75)',
          backdropFilter: 'blur(8px)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          zIndex: 1000
        }}>
          <div style={{
            background: 'linear-gradient(135deg, rgba(15, 23, 42, 0.95) 0%, rgba(22, 32, 54, 0.92) 100%)',
            border: '1px solid rgba(255, 255, 255, 0.12)',
            borderRadius: '16px',
            padding: '2.25rem',
            maxWidth: '500px',
            width: '90%',
            boxShadow: '0 20px 50px rgba(0, 0, 0, 0.5)'
          }}>
            <h3 style={{ fontSize: '1.35rem', fontWeight: 800, color: '#f8fafc', marginBottom: '1.25rem', letterSpacing: '-0.02em' }}>
              Create Institution Tenant
            </h3>
            <form onSubmit={handleCreateTenant}>
              <div style={{ marginBottom: '1rem' }}>
                <label style={{ display: 'block', fontSize: '0.84rem', color: '#cbd5e1', marginBottom: '0.35rem', fontWeight: 600 }}>Institution Name</label>
                <input
                  type="text"
                  required
                  value={newTenantName}
                  onChange={(e) => setNewTenantName(e.target.value)}
                  placeholder="e.g. Oxford University"
                  style={{ width: '100%', padding: '0.65rem 0.85rem', backgroundColor: 'rgba(15, 23, 42, 0.8)', border: '1px solid rgba(255, 255, 255, 0.12)', borderRadius: '8px', color: '#fff', boxSizing: 'border-box', outline: 'none' }}
                />
              </div>
              <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '0.75rem', marginBottom: '1rem' }}>
                <div>
                  <label style={{ display: 'block', fontSize: '0.84rem', color: '#cbd5e1', marginBottom: '0.35rem', fontWeight: 600 }}>Code</label>
                  <input
                    type="text"
                    required
                    value={newTenantCode}
                    onChange={(e) => setNewTenantCode(e.target.value)}
                    placeholder="OXFORD"
                    style={{ width: '100%', padding: '0.65rem 0.85rem', backgroundColor: 'rgba(15, 23, 42, 0.8)', border: '1px solid rgba(255, 255, 255, 0.12)', borderRadius: '8px', color: '#fff', boxSizing: 'border-box', outline: 'none' }}
                  />
                </div>
                <div>
                  <label style={{ display: 'block', fontSize: '0.84rem', color: '#cbd5e1', marginBottom: '0.35rem', fontWeight: 600 }}>Domain</label>
                  <input
                    type="text"
                    value={newTenantDomain}
                    onChange={(e) => setNewTenantDomain(e.target.value)}
                    placeholder="ox.ac.uk"
                    style={{ width: '100%', padding: '0.65rem 0.85rem', backgroundColor: 'rgba(15, 23, 42, 0.8)', border: '1px solid rgba(255, 255, 255, 0.12)', borderRadius: '8px', color: '#fff', boxSizing: 'border-box', outline: 'none' }}
                  />
                </div>
              </div>
              <div style={{ marginBottom: '1.5rem' }}>
                <label style={{ display: 'block', fontSize: '0.84rem', color: '#cbd5e1', marginBottom: '0.35rem', fontWeight: 600 }}>Description</label>
                <textarea
                  value={newTenantDesc}
                  onChange={(e) => setNewTenantDesc(e.target.value)}
                  placeholder="Campus information..."
                  rows={3}
                  style={{ width: '100%', padding: '0.65rem 0.85rem', backgroundColor: 'rgba(15, 23, 42, 0.8)', border: '1px solid rgba(255, 255, 255, 0.12)', borderRadius: '8px', color: '#fff', boxSizing: 'border-box', outline: 'none', resize: 'vertical' }}
                />
              </div>
              <div style={{ display: 'flex', gap: '0.75rem', justifyContent: 'flex-end' }}>
                <button
                  type="button"
                  onClick={() => setShowAddTenant(false)}
                  style={{ padding: '0.65rem 1.25rem', backgroundColor: 'rgba(255, 255, 255, 0.08)', color: '#cbd5e1', border: '1px solid rgba(255, 255, 255, 0.1)', borderRadius: '8px', cursor: 'pointer', fontWeight: 600 }}
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  style={{ padding: '0.65rem 1.35rem', background: 'linear-gradient(135deg, #0284c7 0%, #0369a1 100%)', color: '#fff', border: '1px solid rgba(56, 189, 248, 0.3)', borderRadius: '8px', fontWeight: 700, cursor: 'pointer', boxShadow: '0 4px 12px rgba(2, 132, 199, 0.3)' }}
                >
                  Save Tenant
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
};

