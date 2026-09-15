import React from 'react';
import { Home } from 'lucide-react';

export const HostelSummary: React.FC = () => {
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
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1rem' }}>
        <div>
          <h3 style={{ fontSize: '1.05rem', fontWeight: 700, color: '#f8fafc', margin: 0 }}>
            Hostel & Accommodation Details
          </h3>
          <p style={{ fontSize: '0.78rem', color: '#94a3b8', margin: '2px 0 0 0' }}>
            Campus Housing Allocation Status
          </p>
        </div>
        <Home size={20} color="#34d399" />
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '10px' }}>
        <div style={{ backgroundColor: 'rgba(15, 23, 42, 0.5)', padding: '10px', borderRadius: '8px' }}>
          <div style={{ fontSize: '0.72rem', color: '#64748b' }}>Hostel Building</div>
          <div style={{ fontSize: '0.875rem', fontWeight: 700, color: '#f8fafc' }}>Sunrise Hostel</div>
        </div>
        <div style={{ backgroundColor: 'rgba(15, 23, 42, 0.5)', padding: '10px', borderRadius: '8px' }}>
          <div style={{ fontSize: '0.72rem', color: '#64748b' }}>Room & Block</div>
          <div style={{ fontSize: '0.875rem', fontWeight: 700, color: '#38bdf8' }}>Room B-204 (Block B)</div>
        </div>
      </div>
    </div>
  );
};
