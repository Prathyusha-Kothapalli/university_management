import React from 'react';
import { Library } from 'lucide-react';

export const LibrarySummary: React.FC = () => {
  const books = [
    { title: 'Database System Concepts (7th Ed)', due: '14 Sep 2026', status: 'Due Soon' },
    { title: 'Clean Code: A Handbook of Agile Software Craftsmanship', due: '20 Sep 2026', status: 'Issued' },
    { title: 'Introduction to Algorithms (CLRS 4th Ed)', due: '05 Oct 2026', status: 'Issued' },
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
            Library System & Active Books
          </h3>
          <p style={{ fontSize: '0.78rem', color: '#94a3b8', margin: '2px 0 0 0' }}>
            Issued Books: <strong style={{ color: '#38bdf8' }}>3</strong> | Due Soon: <strong style={{ color: '#f59e0b' }}>1</strong> | Pending Fine: <strong style={{ color: '#f43f5e' }}>₹150</strong>
          </p>
        </div>
        <Library size={20} color="#a855f7" />
      </div>

      <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
        {books.map((b, i) => (
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
              <div style={{ fontSize: '0.85rem', fontWeight: 600, color: '#f1f5f9' }}>{b.title}</div>
              <div style={{ fontSize: '0.72rem', color: '#64748b', marginTop: '2px' }}>
                Due Date: <strong style={{ color: b.status === 'Due Soon' ? '#f59e0b' : '#cbd5e1' }}>{b.due}</strong>
              </div>
            </div>
            <span
              style={{
                padding: '2px 8px',
                borderRadius: '6px',
                fontSize: '0.72rem',
                fontWeight: 700,
                backgroundColor: b.status === 'Due Soon' ? 'rgba(245, 158, 11, 0.15)' : 'rgba(56, 189, 248, 0.15)',
                color: b.status === 'Due Soon' ? '#f59e0b' : '#38bdf8',
              }}
            >
              {b.status}
            </span>
          </div>
        ))}
      </div>
    </div>
  );
};
