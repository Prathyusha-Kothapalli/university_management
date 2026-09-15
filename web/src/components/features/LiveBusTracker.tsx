import React, { useState } from 'react';
import { Bus, Navigation } from 'lucide-react';
import { useToast } from '../../hooks/useToast';

export const LiveBusTracker: React.FC = () => {
  const { showToast } = useToast();
  const [eta, setEta] = useState('8 mins');

  const handleRefreshGps = () => {
    setEta('5 mins');
    showToast('GPS Location updated: Bus #14 approaching Main Junction Stop', 'info');
  };

  return (
    <div
      style={{
        backgroundColor: 'rgba(30, 41, 59, 0.7)',
        backdropFilter: 'blur(12px)',
        border: '1px solid rgba(255, 255, 255, 0.08)',
        borderRadius: '16px',
        padding: '1.25rem',
        boxShadow: '0 4px 20px rgba(0, 0, 0, 0.2)',
      }}
    >
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1rem', flexWrap: 'wrap', gap: '10px' }}>
        <div>
          <h3 style={{ fontSize: '1.05rem', fontWeight: 700, color: '#f8fafc', margin: 0, display: 'flex', alignItems: 'center', gap: '6px' }}>
            <Bus size={18} color="#f59e0b" /> Live GPS Bus Shuttle Tracker
          </h3>
          <p style={{ fontSize: '0.78rem', color: '#94a3b8', margin: '2px 0 0 0' }}>
            Real-time GPS tracking for assigned Route 7 (AP 09 CA 8890)
          </p>
        </div>

        <button
          onClick={handleRefreshGps}
          style={{
            backgroundColor: 'rgba(245, 158, 11, 0.15)',
            border: '1px solid rgba(245, 158, 11, 0.3)',
            color: '#f59e0b',
            borderRadius: '8px',
            padding: '6px 12px',
            fontSize: '0.78rem',
            fontWeight: 600,
            cursor: 'pointer',
            display: 'flex',
            alignItems: 'center',
            gap: '4px',
          }}
        >
          <Navigation size={14} /> Refresh GPS
        </button>
      </div>

      <div style={{ backgroundColor: 'rgba(15, 23, 42, 0.5)', padding: '12px 14px', borderRadius: '10px', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <div>
          <div style={{ fontSize: '0.85rem', fontWeight: 700, color: '#f1f5f9' }}>Route 7: Main Junction → Campus Gate 1</div>
          <div style={{ fontSize: '0.75rem', color: '#94a3b8', marginTop: '2px' }}>Current Location: City Flyover (Speed: 42 km/h)</div>
        </div>
        <div style={{ textAlign: 'right' }}>
          <div style={{ fontSize: '1.1rem', fontWeight: 800, color: '#f59e0b' }}>{eta}</div>
          <div style={{ fontSize: '0.68rem', color: '#94a3b8' }}>Estimated Arrival</div>
        </div>
      </div>
    </div>
  );
};
