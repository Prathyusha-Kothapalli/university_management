import React, { useState } from 'react';
import { Plus } from 'lucide-react';
import { useToast } from '../../hooks/useToast';

export const ScholarshipPortal: React.FC = () => {
  const { showToast } = useToast();
  const [scholarships, setScholarships] = useState([
    { title: 'Merit Academic Excellence Scholarship', amount: '₹25,000 / Semester', eligibility: 'CGPA > 8.50', status: 'Awarded' },
    { title: 'National Science & AI Talent Grant', amount: '₹15,000 / Year', eligibility: 'Published AI Paper', status: 'Applied' },
  ]);

  const handleApply = (title: string) => {
    setScholarships(prev => [...prev, { title, amount: '₹20,000 / Year', eligibility: 'Submitted', status: 'Applied' }]);
    showToast(`Submitted scholarship application for "${title}"`, 'success');
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
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1rem' }}>
        <div>
          <h3 style={{ fontSize: '1.05rem', fontWeight: 700, color: '#f8fafc', margin: 0 }}>
            Scholarship & Financial Aid Application Portal
          </h3>
          <p style={{ fontSize: '0.78rem', color: '#94a3b8', margin: '2px 0 0 0' }}>
            Merit-based scholarships, tuition fee concessions, and research fellowship aid
          </p>
        </div>
        <button
          onClick={() => handleApply('Special Research Aid Grant')}
          style={{
            display: 'flex',
            alignItems: 'center',
            gap: '4px',
            background: 'rgba(245, 158, 11, 0.2)',
            border: '1px solid rgba(245, 158, 11, 0.4)',
            color: '#f59e0b',
            padding: '4px 10px',
            borderRadius: '8px',
            fontSize: '0.75rem',
            fontWeight: 700,
            cursor: 'pointer'
          }}
        >
          <Plus size={14} /> Apply Aid
        </button>
      </div>

      <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
        {scholarships.map((s, i) => (
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
              <div style={{ fontSize: '0.85rem', fontWeight: 700, color: '#f1f5f9' }}>{s.title}</div>
              <div style={{ fontSize: '0.75rem', color: '#64748b', marginTop: '2px' }}>
                Concession Amount: <strong style={{ color: '#34d399' }}>{s.amount}</strong> ({s.eligibility})
              </div>
            </div>

            <span
              style={{
                padding: '2px 8px',
                borderRadius: '6px',
                fontSize: '0.72rem',
                fontWeight: 700,
                backgroundColor: s.status === 'Awarded' ? 'rgba(52, 211, 153, 0.15)' : 'rgba(56, 189, 248, 0.15)',
                color: s.status === 'Awarded' ? '#34d399' : '#38bdf8',
              }}
            >
              {s.status}
            </span>
          </div>
        ))}
      </div>
    </div>
  );
};
