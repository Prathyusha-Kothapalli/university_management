import React from 'react';
import { HardDrive, Server, FileText, AlertCircle } from 'lucide-react';

interface StorageUsageChartProps {
  usedBytes: number;
  quotaBytes: number;
  documentCount: number;
}

export const StorageUsageChart: React.FC<StorageUsageChartProps> = ({
  usedBytes,
  quotaBytes,
  documentCount,
}) => {
  const usedGB = (usedBytes / (1024 * 1024 * 1024)).toFixed(2);
  const quotaGB = (quotaBytes / (1024 * 1024 * 1024)).toFixed(0);
  const percentage = Math.min(Math.round((usedBytes / quotaBytes) * 100), 100);

  const getProgressColor = () => {
    if (percentage > 90) return '#ef4444';
    if (percentage > 75) return '#f59e0b';
    return '#10b981';
  };

  return (
    <div
      style={{
        backgroundColor: 'rgba(15, 23, 42, 0.6)',
        border: '1px solid rgba(255, 255, 255, 0.1)',
        borderRadius: '16px',
        padding: '1.5rem',
        color: '#f8fafc',
      }}
    >
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1rem' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
          <HardDrive size={20} color="#38bdf8" />
          <h4 style={{ margin: 0, fontSize: '1.05rem', fontWeight: 700 }}>
            Tenant Storage Quota & Monitoring
          </h4>
        </div>
        <span style={{ fontSize: '0.8rem', color: '#94a3b8', display: 'flex', alignItems: 'center', gap: '4px' }}>
          <Server size={14} /> Cloud Storage
        </span>
      </div>

      <div style={{ marginBottom: '1rem' }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.85rem', marginBottom: '6px', color: '#cbd5e1' }}>
          <span>Used: <strong>{usedGB} GB</strong> of {quotaGB} GB</span>
          <strong style={{ color: getProgressColor() }}>{percentage}%</strong>
        </div>
        <div
          style={{
            width: '100%',
            height: '10px',
            backgroundColor: 'rgba(255, 255, 255, 0.08)',
            borderRadius: '5px',
            overflow: 'hidden',
          }}
        >
          <div
            style={{
              width: `${percentage}%`,
              height: '100%',
              backgroundColor: getProgressColor(),
              transition: 'width 0.5s ease',
              borderRadius: '5px',
            }}
          />
        </div>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(2, 1fr)', gap: '12px', marginTop: '1rem' }}>
        <div style={{ backgroundColor: 'rgba(255,255,255,0.03)', padding: '10px 14px', borderRadius: '10px', display: 'flex', alignItems: 'center', gap: '10px' }}>
          <FileText size={18} color="#38bdf8" />
          <div>
            <div style={{ fontSize: '0.75rem', color: '#94a3b8' }}>Total Documents</div>
            <div style={{ fontSize: '1.1rem', fontWeight: 700, color: '#f1f5f9' }}>{documentCount.toLocaleString()}</div>
          </div>
        </div>

        <div style={{ backgroundColor: 'rgba(255,255,255,0.03)', padding: '10px 14px', borderRadius: '10px', display: 'flex', alignItems: 'center', gap: '10px' }}>
          <AlertCircle size={18} color={percentage > 80 ? '#ef4444' : '#10b981'} />
          <div>
            <div style={{ fontSize: '0.75rem', color: '#94a3b8' }}>Storage Status</div>
            <div style={{ fontSize: '0.9rem', fontWeight: 700, color: percentage > 80 ? '#ef4444' : '#10b981' }}>
              {percentage > 80 ? 'High Storage Usage' : 'Healthy Quota'}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
