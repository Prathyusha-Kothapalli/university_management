import React from 'react';
import { Building2, Award } from 'lucide-react';

export const DepartmentOverview: React.FC = () => {
  return (
    <div style={{ padding: '1.75rem', display: 'flex', flexDirection: 'column', gap: '1.5rem', maxWidth: '1400px', margin: '0 auto' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <div>
          <h1 style={{ fontSize: '1.5rem', fontWeight: 800, color: '#f8fafc', margin: 0 }}>
            Department Overview & Accreditation
          </h1>
          <p style={{ fontSize: '0.85rem', color: '#94a3b8', margin: '4px 0 0 0' }}>
            Computer Science & Engineering • Established 2008 • NBA Accredited
          </p>
        </div>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: '1.25rem' }}>
        <div
          style={{
            backgroundColor: 'rgba(30, 41, 59, 0.7)',
            border: '1px solid rgba(255, 255, 255, 0.08)',
            borderRadius: '16px',
            padding: '1.25rem',
          }}
        >
          <div style={{ display: 'flex', alignItems: 'center', gap: '10px', marginBottom: '10px' }}>
            <Award size={20} color="#f59e0b" />
            <h3 style={{ fontSize: '1rem', fontWeight: 700, color: '#f8fafc', margin: 0 }}>Accreditation & Status</h3>
          </div>
          <ul style={{ fontSize: '0.85rem', color: '#cbd5e1', paddingLeft: '1.2rem', display: 'flex', flexDirection: 'column', gap: '6px' }}>
            <li>NBA Tier-1 Accredited (Valid till 2028)</li>
            <li>NAAC A++ Grade Certified</li>
            <li>NIRF Ranking: Top 25 Nationally</li>
            <li>Center of Excellence in AI & Data Science</li>
          </ul>
        </div>

        <div
          style={{
            backgroundColor: 'rgba(30, 41, 59, 0.7)',
            border: '1px solid rgba(255, 255, 255, 0.08)',
            borderRadius: '16px',
            padding: '1.25rem',
          }}
        >
          <div style={{ display: 'flex', alignItems: 'center', gap: '10px', marginBottom: '10px' }}>
            <Building2 size={20} color="#38bdf8" />
            <h3 style={{ fontSize: '1rem', fontWeight: 700, color: '#f8fafc', margin: 0 }}>Laboratories & Infrastructure</h3>
          </div>
          <ul style={{ fontSize: '0.85rem', color: '#cbd5e1', paddingLeft: '1.2rem', display: 'flex', flexDirection: 'column', gap: '6px' }}>
            <li>12 High-Performance Computing Labs (600 Systems)</li>
            <li>NVIDIA AI Deep Learning GPU Workstation Suite</li>
            <li>IoT & Embedded Systems Lab</li>
            <li>Cyber Security & Forensics Research Lab</li>
          </ul>
        </div>
      </div>
    </div>
  );
};
