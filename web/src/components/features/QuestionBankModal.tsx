import React, { useState } from 'react';
import { Search, Download } from 'lucide-react';
import { useToast } from '../../hooks/useToast';

export const QuestionBankModal: React.FC = () => {
  const { showToast } = useToast();
  const [search, setSearch] = useState('');

  const papers = [
    { title: 'Database Systems Mid-Term Question Paper 2025', code: 'CS502', year: 2025 },
    { title: 'Operating Systems End-Sem Paper 2024', code: 'CS503', year: 2024 },
    { title: 'Data Structures & Algorithms Question Bank (200+ Qs)', code: 'CS501', year: 2025 },
  ];

  const filtered = papers.filter((p) => p.title.toLowerCase().includes(search.toLowerCase()) || p.code.toLowerCase().includes(search.toLowerCase()));

  const handleDownload = (title: string) => {
    showToast(`Downloading question paper: "${title}"`, 'info');
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
          <h3 style={{ fontSize: '1.05rem', fontWeight: 700, color: '#f8fafc', margin: 0 }}>
            Digital Question Papers & Practice Quizzes Repository
          </h3>
          <p style={{ fontSize: '0.78rem', color: '#94a3b8', margin: '2px 0 0 0' }}>
            Search previous years' mid-term and end-sem question papers across 28 CSE courses
          </p>
        </div>

        <div style={{ position: 'relative' }}>
          <Search size={14} color="#94a3b8" style={{ position: 'absolute', left: '10px', top: '9px' }} />
          <input
            type="text"
            placeholder="Search paper or code..."
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            style={{
              backgroundColor: 'rgba(15, 23, 42, 0.8)',
              border: '1px solid rgba(255, 255, 255, 0.12)',
              borderRadius: '8px',
              color: '#f8fafc',
              padding: '6px 12px 6px 30px',
              fontSize: '0.78rem',
              outline: 'none',
            }}
          />
        </div>
      </div>

      <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
        {filtered.map((p, i) => (
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
              <div style={{ fontSize: '0.85rem', fontWeight: 600, color: '#f1f5f9' }}>{p.title}</div>
              <div style={{ fontSize: '0.72rem', color: '#64748b', marginTop: '2px' }}>
                Course Code: <strong style={{ color: '#38bdf8' }}>{p.code}</strong> • Session {p.year}
              </div>
            </div>
            <button
              onClick={() => handleDownload(p.title)}
              style={{
                backgroundColor: 'rgba(56, 189, 248, 0.15)',
                border: '1px solid rgba(56, 189, 248, 0.3)',
                color: '#38bdf8',
                borderRadius: '6px',
                padding: '4px 10px',
                fontSize: '0.72rem',
                fontWeight: 600,
                cursor: 'pointer',
                display: 'flex',
                alignItems: 'center',
                gap: '4px',
              }}
            >
              <Download size={13} /> PDF
            </button>
          </div>
        ))}
      </div>
    </div>
  );
};
