import React, { useState } from 'react';

export const PlacementsView: React.FC = () => {
  const [appliedIds, setAppliedIds] = useState<string[]>(['p3']);

  const drives = [
    {
      id: 'p1',
      company: 'Google',
      role: 'Software Engineer - AI & Core Systems',
      pkg: '$190,000 / ₹48.5 LPA',
      deadline: 'Sep 25, 2026',
      eligibility: 'CGPA ≥ 8.5 • CS/AI/ECE',
      location: 'Mountain View / Bengaluru',
      logo: '🌐',
    },
    {
      id: 'p2',
      company: 'NVIDIA',
      role: 'Deep Learning Systems Engineer (CUDA/TensorRT)',
      pkg: '$210,000 / ₹52.0 LPA',
      deadline: 'Oct 02, 2026',
      eligibility: 'CGPA ≥ 8.8 • CS/AI/EE',
      location: 'Santa Clara / Pune',
      logo: '⚡',
    },
    {
      id: 'p3',
      company: 'Microsoft',
      role: 'Azure Cloud Platforms Engineer',
      pkg: '$175,000 / ₹44.0 LPA',
      deadline: 'Sep 20, 2026',
      eligibility: 'CGPA ≥ 8.0 • All Engineering',
      location: 'Redmond / Hyderabad',
      logo: '🪟',
    },
    {
      id: 'p4',
      company: 'Apple',
      role: 'Embedded Software Engineer',
      pkg: '$185,000 / ₹46.5 LPA',
      deadline: 'Oct 10, 2026',
      eligibility: 'CGPA ≥ 8.5 • CS/ECE',
      location: 'Cupertino / Bengaluru',
      logo: '🍎',
    },
  ];

  const handleApply = (id: string) => {
    if (!appliedIds.includes(id)) {
      setAppliedIds([...appliedIds, id]);
    }
  };

  return (
    <div style={{ padding: '1.25rem' }}>
      {/* Placement Stats Header */}
      <div style={{
        background: 'linear-gradient(135deg, #059669, #0d9488)',
        padding: '1.25rem',
        borderRadius: '16px',
        color: '#fff',
        marginBottom: '1rem',
      }}>
        <div style={{ fontSize: '0.8rem', fontWeight: 600, opacity: 0.9 }}>
          Campus Career & Placements 2026
        </div>
        <div style={{ fontSize: '1.8rem', fontWeight: 800, marginTop: '4px' }}>
          96.4% Placed
        </div>
        <div style={{ display: 'flex', gap: '16px', marginTop: '8px', fontSize: '0.78rem' }}>
          <div>Top Offer: <strong>₹58 LPA</strong></div>
          <div>•</div>
          <div>Avg CTC: <strong>₹19.4 LPA</strong></div>
        </div>
      </div>

      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '0.75rem' }}>
        <h3 style={{ fontSize: '1rem', fontWeight: 700, color: '#f8fafc' }}>
          Active Corporate Drives
        </h3>
        <span style={{ fontSize: '0.75rem', color: '#38bdf8' }}>{drives.length} openings</span>
      </div>

      <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
        {drives.map((d) => {
          const isApplied = appliedIds.includes(d.id);

          return (
            <div key={d.id} className="glass-panel" style={{ padding: '1rem' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: '6px' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                  <span style={{ fontSize: '1.4rem' }}>{d.logo}</span>
                  <div>
                    <div style={{ fontSize: '0.925rem', fontWeight: 700, color: '#f8fafc' }}>
                      {d.company}
                    </div>
                    <div style={{ fontSize: '0.75rem', color: '#94a3b8' }}>
                      📍 {d.location}
                    </div>
                  </div>
                </div>
                <span style={{
                  fontSize: '0.75rem',
                  fontWeight: 700,
                  color: '#34d399',
                  background: 'rgba(52, 211, 153, 0.15)',
                  padding: '2px 8px',
                  borderRadius: '6px',
                }}>
                  {d.pkg}
                </span>
              </div>

              <div style={{ fontSize: '0.85rem', fontWeight: 600, color: '#e2e8f0', margin: '6px 0' }}>
                {d.role}
              </div>

              <div style={{ fontSize: '0.75rem', color: '#94a3b8', marginBottom: '10px' }}>
                <div>🎯 <strong>Criteria:</strong> {d.eligibility}</div>
                <div>⏳ <strong>Deadline:</strong> {d.deadline}</div>
              </div>

              <button
                onClick={() => handleApply(d.id)}
                disabled={isApplied}
                className={`btn ${isApplied ? 'btn-secondary' : 'btn-primary'}`}
                style={{
                  width: '100%',
                  padding: '8px',
                  fontSize: '0.825rem',
                  cursor: isApplied ? 'default' : 'pointer',
                }}
              >
                {isApplied ? '✓ Application Submitted' : '⚡ 1-Tap Campus Apply'}
              </button>
            </div>
          );
        })}
      </div>
    </div>
  );
};
