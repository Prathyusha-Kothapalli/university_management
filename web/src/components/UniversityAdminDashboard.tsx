import React, { useState, useEffect } from 'react';
import { User, UserRole } from '../types/auth';
import { useAuth } from '../features/auth/AuthContext';
import { api } from '../services/api';

export const UniversityAdminDashboard: React.FC = () => {
  const { user, tenant, registerUser } = useAuth();
  const [users, setUsers] = useState<User[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [roleFilter, setRoleFilter] = useState<string>('');
  const [message, setMessage] = useState<{ text: string; type: 'success' | 'error' } | null>(null);

  // New User Form State
  const [showAddUser, setShowAddUser] = useState(false);
  const [newEmail, setNewEmail] = useState('');
  const [newPassword, setNewPassword] = useState('');
  const [newFullName, setNewFullName] = useState('');
  const [newRole, setNewRole] = useState<UserRole>('STUDENT');
  const [newDepartment, setNewDepartment] = useState('');

  const fetchUsers = async () => {
    setLoading(true);
    try {
      const data = await api.getUsers(roleFilter ? { role: roleFilter as UserRole } : undefined);
      setUsers(data);
    } catch (err: any) {
      setMessage({ text: err.message || 'Failed to fetch campus directory', type: 'error' });
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchUsers();
  }, [roleFilter]);

  const handleCreateUser = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await registerUser({
        email: newEmail,
        password: newPassword,
        full_name: newFullName,
        role: newRole,
        department: newDepartment || undefined,
        tenant_id: tenant?.id
      });
      setMessage({ text: `Account for "${newFullName}" (${newRole}) created!`, type: 'success' });
      setShowAddUser(false);
      setNewEmail('');
      setNewPassword('');
      setNewFullName('');
      setNewDepartment('');
      fetchUsers();
    } catch (err: any) {
      setMessage({ text: err.message || 'Failed to create user', type: 'error' });
    }
  };

  const handleDeleteUser = async (userId: string, userName: string) => {
    if (!confirm(`Are you sure you want to remove user "${userName}"?`)) return;
    try {
      await api.deleteUser(userId);
      setMessage({ text: `User "${userName}" removed.`, type: 'success' });
      fetchUsers();
    } catch (err: any) {
      setMessage({ text: err.message || 'Failed to remove user', type: 'error' });
    }
  };

  const facultyCount = users.filter(u => u.role === 'FACULTY').length;
  const studentCount = users.filter(u => u.role === 'STUDENT').length;
  const staffCount = users.filter(u => u.role === 'STAFF').length;

  return (
    <div style={{ maxWidth: '1240px', margin: '2rem auto', padding: '0 1.5rem' }}>
      {/* Header */}
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
              {tenant?.name || 'University Administration'}
            </h1>
            <span style={{
              backgroundColor: 'rgba(56, 189, 248, 0.12)',
              border: '1px solid rgba(56, 189, 248, 0.3)',
              color: '#38bdf8',
              fontSize: '0.75rem',
              fontWeight: 700,
              padding: '0.25rem 0.75rem',
              borderRadius: '9999px',
              fontFamily: "'JetBrains Mono', monospace"
            }}>
              TENANT: {tenant?.code}
            </span>
          </div>
          <p style={{ color: '#94a3b8', fontSize: '0.92rem', marginTop: '0.4rem', marginBottom: 0 }}>
            Campus User Administration & Multi-Tenant Directory Isolation
          </p>
        </div>

        <button
          onClick={() => setShowAddUser(true)}
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
          <span style={{ fontSize: '1.1rem' }}>+</span> Enroll Student / Faculty
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
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', gap: '1.25rem', marginBottom: '2rem' }}>
        <div style={{
          background: 'rgba(15, 23, 42, 0.7)',
          backdropFilter: 'blur(12px)',
          border: '1px solid rgba(255, 255, 255, 0.08)',
          borderRadius: '12px',
          padding: '1.4rem'
        }}>
          <div style={{ color: '#94a3b8', fontSize: '0.8rem', fontWeight: 700, textTransform: 'uppercase', letterSpacing: '0.04em' }}>Enrolled Students</div>
          <div style={{ fontSize: '2.2rem', fontWeight: 800, color: '#10b981', marginTop: '0.35rem', letterSpacing: '-0.02em' }}>{studentCount}</div>
        </div>
        <div style={{
          background: 'rgba(15, 23, 42, 0.7)',
          backdropFilter: 'blur(12px)',
          border: '1px solid rgba(255, 255, 255, 0.08)',
          borderRadius: '12px',
          padding: '1.4rem'
        }}>
          <div style={{ color: '#94a3b8', fontSize: '0.8rem', fontWeight: 700, textTransform: 'uppercase', letterSpacing: '0.04em' }}>Faculty Members</div>
          <div style={{ fontSize: '2.2rem', fontWeight: 800, color: '#38bdf8', marginTop: '0.35rem', letterSpacing: '-0.02em' }}>{facultyCount}</div>
        </div>
        <div style={{
          background: 'rgba(15, 23, 42, 0.7)',
          backdropFilter: 'blur(12px)',
          border: '1px solid rgba(255, 255, 255, 0.08)',
          borderRadius: '12px',
          padding: '1.4rem'
        }}>
          <div style={{ color: '#94a3b8', fontSize: '0.8rem', fontWeight: 700, textTransform: 'uppercase', letterSpacing: '0.04em' }}>Campus Staff</div>
          <div style={{ fontSize: '2.2rem', fontWeight: 800, color: '#a855f7', marginTop: '0.35rem', letterSpacing: '-0.02em' }}>{staffCount}</div>
        </div>
        <div style={{
          background: 'rgba(15, 23, 42, 0.7)',
          backdropFilter: 'blur(12px)',
          border: '1px solid rgba(255, 255, 255, 0.08)',
          borderRadius: '12px',
          padding: '1.4rem'
        }}>
          <div style={{ color: '#94a3b8', fontSize: '0.8rem', fontWeight: 700, textTransform: 'uppercase', letterSpacing: '0.04em' }}>Total Campus Accounts</div>
          <div style={{ fontSize: '2.2rem', fontWeight: 800, color: '#f59e0b', marginTop: '0.35rem', letterSpacing: '-0.02em' }}>{users.length}</div>
        </div>
      </div>

      {/* Campus User Directory Table */}
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
              Institutional Member Directory
            </h2>
            <p style={{ color: '#64748b', fontSize: '0.85rem', margin: '0.2rem 0 0 0' }}>
              Filtered users scoped exclusively to {tenant?.name || 'this campus'}
            </p>
          </div>
          <div style={{ display: 'flex', gap: '0.4rem', flexWrap: 'wrap' }}>
            {['', 'STUDENT', 'FACULTY', 'STAFF', 'UNIVERSITY_ADMIN'].map(role => (
              <button
                key={role}
                onClick={() => setRoleFilter(role)}
                style={{
                  backgroundColor: roleFilter === role ? 'rgba(56, 189, 248, 0.2)' : 'rgba(15, 23, 42, 0.8)',
                  color: roleFilter === role ? '#38bdf8' : '#94a3b8',
                  border: roleFilter === role ? '1px solid rgba(56, 189, 248, 0.4)' : '1px solid rgba(255, 255, 255, 0.08)',
                  padding: '0.45rem 0.85rem',
                  borderRadius: '8px',
                  fontSize: '0.78rem',
                  fontWeight: 700,
                  cursor: 'pointer',
                  transition: 'all 0.15s ease'
                }}
              >
                {role ? role.replace('_', ' ') : 'All Members'}
              </button>
            ))}
          </div>
        </div>

        {loading ? (
          <div style={{ color: '#94a3b8', textAlign: 'center', padding: '3rem', fontSize: '0.92rem' }}>
            Loading campus directory...
          </div>
        ) : (
          <div style={{ overflowX: 'auto' }}>
            <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left', fontSize: '0.88rem' }}>
              <thead>
                <tr style={{ borderBottom: '1px solid rgba(255, 255, 255, 0.08)', color: '#94a3b8' }}>
                  <th style={{ padding: '0.85rem 0.6rem', fontWeight: 700, fontSize: '0.78rem', textTransform: 'uppercase', letterSpacing: '0.04em' }}>Name</th>
                  <th style={{ padding: '0.85rem 0.6rem', fontWeight: 700, fontSize: '0.78rem', textTransform: 'uppercase', letterSpacing: '0.04em' }}>Email</th>
                  <th style={{ padding: '0.85rem 0.6rem', fontWeight: 700, fontSize: '0.78rem', textTransform: 'uppercase', letterSpacing: '0.04em' }}>Role</th>
                  <th style={{ padding: '0.85rem 0.6rem', fontWeight: 700, fontSize: '0.78rem', textTransform: 'uppercase', letterSpacing: '0.04em' }}>Department</th>
                  <th style={{ padding: '0.85rem 0.6rem', fontWeight: 700, fontSize: '0.78rem', textTransform: 'uppercase', letterSpacing: '0.04em' }}>Status</th>
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
                        backgroundColor: u.role === 'FACULTY' ? 'rgba(59, 130, 246, 0.18)' : u.role === 'STUDENT' ? 'rgba(16, 185, 129, 0.18)' : u.role === 'STAFF' ? 'rgba(168, 85, 247, 0.18)' : 'rgba(245, 158, 11, 0.18)',
                        color: u.role === 'FACULTY' ? '#93c5fd' : u.role === 'STUDENT' ? '#6ee7b7' : u.role === 'STAFF' ? '#d8b4fe' : '#fcd34d',
                        border: `1px solid ${u.role === 'FACULTY' ? 'rgba(59, 130, 246, 0.3)' : u.role === 'STUDENT' ? 'rgba(16, 185, 129, 0.3)' : u.role === 'STAFF' ? 'rgba(168, 85, 247, 0.3)' : 'rgba(245, 158, 11, 0.3)'}`,
                        padding: '0.2rem 0.55rem',
                        borderRadius: '6px',
                        fontSize: '0.72rem',
                        fontWeight: 700,
                        letterSpacing: '0.03em'
                      }}>
                        {u.role.replace('_', ' ')}
                      </span>
                    </td>
                    <td style={{ padding: '0.85rem 0.6rem', color: '#94a3b8' }}>{u.department || '—'}</td>
                    <td style={{ padding: '0.85rem 0.6rem' }}>
                      <span style={{ color: u.is_active ? '#10b981' : '#ef4444', fontSize: '0.78rem', fontWeight: 600 }}>
                        ● {u.is_active ? 'Active' : 'Deactivated'}
                      </span>
                    </td>
                    <td style={{ padding: '0.85rem 0.6rem', textAlign: 'right' }}>
                      {u.id !== user?.id && u.role !== 'UNIVERSITY_ADMIN' && (
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
                          Remove
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

      {/* Enroll User Modal */}
      {showAddUser && (
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
              Enroll Institutional Member
            </h3>
            <form onSubmit={handleCreateUser}>
              <div style={{ marginBottom: '1rem' }}>
                <label style={{ display: 'block', fontSize: '0.84rem', color: '#cbd5e1', marginBottom: '0.35rem', fontWeight: 600 }}>Full Name</label>
                <input
                  type="text"
                  required
                  value={newFullName}
                  onChange={(e) => setNewFullName(e.target.value)}
                  placeholder="e.g. Marie Curie"
                  style={{ width: '100%', padding: '0.65rem 0.85rem', backgroundColor: 'rgba(15, 23, 42, 0.8)', border: '1px solid rgba(255, 255, 255, 0.12)', borderRadius: '8px', color: '#fff', boxSizing: 'border-box', outline: 'none' }}
                />
              </div>
              <div style={{ marginBottom: '1rem' }}>
                <label style={{ display: 'block', fontSize: '0.84rem', color: '#cbd5e1', marginBottom: '0.35rem', fontWeight: 600 }}>Email Address</label>
                <input
                  type="email"
                  required
                  value={newEmail}
                  onChange={(e) => setNewEmail(e.target.value)}
                  placeholder={`name@${tenant?.domain || 'institution.edu'}`}
                  style={{ width: '100%', padding: '0.65rem 0.85rem', backgroundColor: 'rgba(15, 23, 42, 0.8)', border: '1px solid rgba(255, 255, 255, 0.12)', borderRadius: '8px', color: '#fff', boxSizing: 'border-box', outline: 'none' }}
                />
              </div>
              <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '0.75rem', marginBottom: '1rem' }}>
                <div>
                  <label style={{ display: 'block', fontSize: '0.84rem', color: '#cbd5e1', marginBottom: '0.35rem', fontWeight: 600 }}>Role</label>
                  <select
                    value={newRole}
                    onChange={(e) => setNewRole(e.target.value as UserRole)}
                    style={{ width: '100%', padding: '0.65rem 0.85rem', backgroundColor: '#0f172a', border: '1px solid rgba(255, 255, 255, 0.12)', borderRadius: '8px', color: '#fff', boxSizing: 'border-box', outline: 'none' }}
                  >
                    <option value="STUDENT">STUDENT</option>
                    <option value="FACULTY">FACULTY</option>
                    <option value="STAFF">STAFF</option>
                  </select>
                </div>
                <div>
                  <label style={{ display: 'block', fontSize: '0.84rem', color: '#cbd5e1', marginBottom: '0.35rem', fontWeight: 600 }}>Department</label>
                  <input
                    type="text"
                    value={newDepartment}
                    onChange={(e) => setNewDepartment(e.target.value)}
                    placeholder="e.g. Physics"
                    style={{ width: '100%', padding: '0.65rem 0.85rem', backgroundColor: 'rgba(15, 23, 42, 0.8)', border: '1px solid rgba(255, 255, 255, 0.12)', borderRadius: '8px', color: '#fff', boxSizing: 'border-box', outline: 'none' }}
                  />
                </div>
              </div>
              <div style={{ marginBottom: '1.5rem' }}>
                <label style={{ display: 'block', fontSize: '0.84rem', color: '#cbd5e1', marginBottom: '0.35rem', fontWeight: 600 }}>Password</label>
                <input
                  type="password"
                  required
                  value={newPassword}
                  onChange={(e) => setNewPassword(e.target.value)}
                  placeholder="Min 6 characters"
                  style={{ width: '100%', padding: '0.65rem 0.85rem', backgroundColor: 'rgba(15, 23, 42, 0.8)', border: '1px solid rgba(255, 255, 255, 0.12)', borderRadius: '8px', color: '#fff', boxSizing: 'border-box', outline: 'none' }}
                />
              </div>
              <div style={{ display: 'flex', gap: '0.75rem', justifyContent: 'flex-end' }}>
                <button
                  type="button"
                  onClick={() => setShowAddUser(false)}
                  style={{ padding: '0.65rem 1.25rem', backgroundColor: 'rgba(255, 255, 255, 0.08)', color: '#cbd5e1', border: '1px solid rgba(255, 255, 255, 0.1)', borderRadius: '8px', cursor: 'pointer', fontWeight: 600 }}
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  style={{ padding: '0.65rem 1.35rem', background: 'linear-gradient(135deg, #0284c7 0%, #0369a1 100%)', color: '#fff', border: '1px solid rgba(56, 189, 248, 0.3)', borderRadius: '8px', fontWeight: 700, cursor: 'pointer', boxShadow: '0 4px 12px rgba(2, 132, 199, 0.3)' }}
                >
                  Enroll Member
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
};

