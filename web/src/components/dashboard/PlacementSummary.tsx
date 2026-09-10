import React from 'react';
import { Briefcase } from 'lucide-react';

export const PlacementSummary: React.FC = () => {
  const drives = [
    { company: 'TechCorp Systems', role: 'Software Engineer', status: 'Submitted', package: '₹14 LPA' },
    { company: 'InnovateLabs AI', role: 'Graduate AI Developer', status: 'Shortlisted', package: '₹18 LPA' },
    { company: 'DataDynamics', role: 'Data Engineer', status: 'Under Review', package: '₹12 LPA' },
  ];

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
            Corporate Placements & Career Drives
          </h3>
          <p style={{ fontSize: '0.78rem', color: '#94a3b8', margin: '2px 0 0 0' }}>
            Active Drives: <strong style={{ color: '#38bdf8' }}>8</strong> | Applications: <strong style={{ color: '#f8fafc' }}>3</strong> | Shortlisted: <strong style={{ color: '#34d399' }}>1</strong>
          </p>
        </div>
        <Briefcase size={20} color="#34d399" />
      </div>

      <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
        {drives.map((d, i) => (
          <div
            key={i}
            style={{
              backgroundColor: 'rgba(15, 23, 42, 0.5)',
              border: '1px solid rgba(255, 255, 255, 0.05)',
              borderRadius: '10px',
              padding: '10px 12px',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'space-between',
            }}
          >
            <div>
              <div style={{ fontSize: '0.85rem', fontWeight: 700, color: '#f1f5f9' }}>{d.company}</div>
              <div style={{ fontSize: '0.72rem', color: '#64748b', marginTop: '2px' }}>
                Role: <strong style={{ color: '#cbd5e1' }}>{d.role}</strong> ({d.package})
              </div>
            </div>
            <span
              style={{
                padding: '2px 8px',
                borderRadius: '6px',
                fontSize: '0.72rem',
                fontWeight: 700,
                backgroundColor: d.status === 'Shortlisted' ? 'rgba(52, 211, 153, 0.15)' : 'rgba(56, 189, 248, 0.15)',
                color: d.status === 'Shortlisted' ? '#34d399' : '#38bdf8',
              }}
            >
              {d.status}
            </span>
          </div>
        ))}
      </div>
    </div>
  );
};
