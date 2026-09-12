import React, { useState, useEffect } from 'react';
import { useToast } from '../../hooks/useToast';
import { Button } from '../../components/Button';
import { Card } from '../../components/Card';
import { Monitor, Smartphone, Globe, ShieldAlert, LogOut, Trash2, RefreshCw } from 'lucide-react';

interface SessionItem {
  session_id: string;
  user_id: string;
  email: string;
  role: string;
  ip_address: string;
  created_at: string;
}

export const SessionManagementPage: React.FC = () => {
  const { showToast } = useToast();
  const [sessions, setSessions] = useState<SessionItem[]>([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    fetchSessions();
  }, []);

  const fetchSessions = async () => {
    setLoading(true);
    try {
      const response = await fetch('http://localhost:8000/api/v1/auth/sessions');
      const data = await response.json();
      setSessions(data.active_sessions || []);
    } catch (err) {
      showToast('Error loading active sessions', 'error');
    } finally {
      setLoading(false);
    }
  };

  const handleRevokeSession = async (sessionId: string) => {
    try {
      const response = await fetch(`http://localhost:8000/api/v1/auth/sessions/${sessionId}`, {
        method: 'DELETE',
      });
      if (!response.ok) throw new Error('Revocation failed');
      showToast('Session terminated successfully.', 'success');
      fetchSessions();
    } catch (err: any) {
      showToast(err.message || 'Error revoking session', 'error');
    }
  };

  const handleLogoutAll = async () => {
    try {
      const response = await fetch('http://localhost:8000/api/v1/auth/logout-all', {
        method: 'POST',
        headers: { Authorization: 'Bearer DEMO_TOKEN' },
      });
      if (!response.ok) throw new Error('Logout all failed');
      showToast('All active sessions terminated.', 'success');
      fetchSessions();
    } catch (err: any) {
      showToast(err.message || 'Error terminating all sessions', 'error');
    }
  };

  return (
    <div style={{ padding: '2rem', maxWidth: '1000px', margin: '0 auto' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '2rem' }}>
        <div>
          <h1 style={{ fontSize: '1.8rem', fontWeight: 800, color: '#f8fafc', margin: 0 }}>
            Active Devices & Session Monitoring
          </h1>
          <p style={{ color: '#94a3b8', margin: '4px 0 0 0', fontSize: '0.9rem' }}>
            Review active logins, IP addresses, and revoke suspicious device sessions.
          </p>
        </div>
        <div style={{ display: 'flex', gap: '0.75rem' }}>
          <Button onClick={fetchSessions} variant="secondary" isLoading={loading}>
            <RefreshCw size={16} style={{ marginRight: '6px' }} /> Refresh List
          </Button>
          <Button onClick={handleLogoutAll} variant="danger">
            <LogOut size={16} style={{ marginRight: '6px' }} /> Terminate All Devices
          </Button>
        </div>
      </div>

      <div style={{ display: 'grid', gap: '1rem' }}>
        {sessions.length === 0 ? (
          <Card style={{ padding: '2rem', textAlign: 'center', color: '#94a3b8' }}>
            No active session records found or all sessions terminated.
          </Card>
        ) : (
          sessions.map((sess, idx) => (
            <Card
              key={sess.session_id || idx}
              style={{
                padding: '1.25rem 1.5rem',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'space-between',
                backgroundColor: 'rgba(15, 23, 42, 0.6)',
                border: '1px solid rgba(255, 255, 255, 0.08)',
                borderRadius: '14px',
              }}
            >
              <div style={{ display: 'flex', alignItems: 'center', gap: '1rem' }}>
                <div
                  style={{
                    width: '44px',
                    height: '44px',
                    borderRadius: '12px',
                    backgroundColor: 'rgba(37, 99, 235, 0.15)',
                    color: '#38bdf8',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                  }}
                >
                  <Monitor size={22} />
                </div>
                <div>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                    <span style={{ fontWeight: 700, color: '#f8fafc', fontSize: '1rem' }}>
                      {sess.email} ({sess.role.toUpperCase()})
                    </span>
                    {idx === 0 && (
                      <span style={{ padding: '2px 8px', borderRadius: '12px', background: 'rgba(16, 185, 129, 0.2)', color: '#10b981', fontSize: '0.75rem', fontWeight: 600 }}>
                        Current Session
                      </span>
                    )}
                  </div>
                  <div style={{ display: 'flex', gap: '1rem', marginTop: '4px', fontSize: '0.8rem', color: '#94a3b8' }}>
                    <span>IP: {sess.ip_address}</span>
                    <span>Started: {new Date(sess.created_at).toLocaleString()}</span>
                  </div>
                </div>
              </div>

              <Button
                onClick={() => handleRevokeSession(sess.session_id)}
                variant="outline"
                size="sm"
                style={{ color: '#ef4444', borderColor: 'rgba(239, 68, 68, 0.3)' }}
              >
                <Trash2 size={14} style={{ marginRight: '4px' }} /> Revoke Access
              </Button>
            </Card>
          ))
        )}
      </div>
    </div>
  );
};
