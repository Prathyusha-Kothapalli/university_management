import React from 'react';
import { Shield, AlertTriangle, CheckCircle, Clock } from 'lucide-react';

export interface AuditLogItem {
  id: string;
  email: string;
  eventType: string;
  status: 'SUCCESS' | 'FAILED' | 'WARNING';
  ipAddress: string;
  details?: string;
  timestamp: string;
}

interface SecurityAuditTableProps {
  logs: AuditLogItem[];
  onRefresh?: () => void;
}

export const SecurityAuditTable: React.FC<SecurityAuditTableProps> = ({ logs }) => {
  return (
    <div style={{ backgroundColor: 'rgba(15, 23, 42, 0.6)', border: '1px solid rgba(255, 255, 255, 0.1)', borderRadius: '14px', overflow: 'hidden' }}>
      <div style={{ padding: '1.25rem', borderBottom: '1px solid rgba(255, 255, 255, 0.08)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <div>
          <h3 style={{ margin: 0, fontSize: '1.1rem', color: '#f8fafc', fontWeight: 700 }}>
            Authentication & Security Audit Trail
          </h3>
          <p style={{ margin: '4px 0 0 0', fontSize: '0.8rem', color: '#94a3b8' }}>
            Real-time telemetry of system logins, password changes, MFA challenges, and access anomalies.
          </p>
        </div>
      </div>

      <div style={{ overflowX: 'auto' }}>
        <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left', fontSize: '0.85rem' }}>
          <thead>
            <tr style={{ backgroundColor: 'rgba(255, 255, 255, 0.03)', color: '#94a3b8', borderBottom: '1px solid rgba(255, 255, 255, 0.08)' }}>
              <th style={{ padding: '12px 16px' }}>Event Type</th>
              <th style={{ padding: '12px 16px' }}>User Email</th>
              <th style={{ padding: '12px 16px' }}>IP Address</th>
              <th style={{ padding: '12px 16px' }}>Status</th>
              <th style={{ padding: '12px 16px' }}>Timestamp</th>
            </tr>
          </thead>
          <tbody>
            {logs.length === 0 ? (
              <tr>
                <td colSpan={5} style={{ padding: '2rem', textAlign: 'center', color: '#64748b' }}>
                  No audit log entries recorded.
                </td>
              </tr>
            ) : (
              logs.map((log) => (
                <tr key={log.id} style={{ borderBottom: '1px solid rgba(255, 255, 255, 0.05)', color: '#e2e8f0' }}>
                  <td style={{ padding: '12px 16px', fontWeight: 600 }}>
                    <span style={{ display: 'inline-flex', alignItems: 'center', gap: '6px' }}>
                      <Shield size={14} color="#38bdf8" />
                      {log.eventType}
                    </span>
                  </td>
                  <td style={{ padding: '12px 16px' }}>{log.email}</td>
                  <td style={{ padding: '12px 16px', fontFamily: 'monospace', color: '#cbd5e1' }}>{log.ipAddress}</td>
                  <td style={{ padding: '12px 16px' }}>
                    {log.status === 'SUCCESS' ? (
                      <span style={{ display: 'inline-flex', alignItems: 'center', gap: '4px', color: '#10b981', backgroundColor: 'rgba(16, 185, 129, 0.15)', padding: '2px 8px', borderRadius: '12px', fontSize: '0.75rem' }}>
                        <CheckCircle size={12} /> SUCCESS
                      </span>
                    ) : (
                      <span style={{ display: 'inline-flex', alignItems: 'center', gap: '4px', color: '#ef4444', backgroundColor: 'rgba(239, 68, 68, 0.15)', padding: '2px 8px', borderRadius: '12px', fontSize: '0.75rem' }}>
                        <AlertTriangle size={12} /> {log.status}
                      </span>
                    )}
                  </td>
                  <td style={{ padding: '12px 16px', color: '#94a3b8' }}>
                    <span style={{ display: 'inline-flex', alignItems: 'center', gap: '4px' }}>
                      <Clock size={12} />
                      {new Date(log.timestamp).toLocaleString()}
                    </span>
                  </td>
                </tr>
              ))
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
};
