import React from 'react';
import { Award } from 'lucide-react';
import { useToast } from '../../hooks/useToast';

interface Paper {
  id: string;
  title: string;
  authors: string;
  journal: string;
  indexing: string;
  citations: number;
  year: number;
}

export const ResearchPublicationHub: React.FC = () => {
  const { showToast } = useToast();

  const papers: Paper[] = [
    {
      id: 'PUB-01',
      title: 'Scalable Distributed Vector Indexing for Real-Time LLM Retrieval',
      authors: 'Dr. Sarah Jenkins, Dr. Robert Rao, Siddharth Varma',
      journal: 'IEEE Transactions on Knowledge & Data Engineering',
      indexing: 'IEEE / Scopus Q1',
      citations: 28,
      year: 2026,
    },
    {
      id: 'PUB-02',
      title: 'Zero-Shot Multi-Modal Sentiment Analysis in Clinical Diagnostics',
      authors: 'Dr. Emily Vance, Priya Sundaram',
      journal: 'ACM Transactions on Intelligent Systems & Technology',
      indexing: 'ACM Digital Library',
      citations: 42,
      year: 2025,
    },
    {
      id: 'PUB-03',
      title: 'Fault-Tolerant Consensus Protocols for Edge-Cloud Microservices',
      authors: 'Prof. Michael Scott, Prof. Alan Turing',
      journal: 'Elsevier Journal of Parallel & Distributed Computing',
      indexing: 'Scopus Q1',
      citations: 19,
      year: 2025,
    },
  ];

  const handleDownloadBibTeX = (title: string) => {
    showToast(`Downloaded BibTeX citation for "${title}"`, 'info');
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
            Department Research & IEEE Publication Hub
          </h3>
          <p style={{ fontSize: '0.78rem', color: '#94a3b8', margin: '2px 0 0 0' }}>
            245 Total Indexed Papers | <strong style={{ color: '#38bdf8' }}>1,840 Total Citations</strong> | h-index: <strong style={{ color: '#34d399' }}>22</strong>
          </p>
        </div>
        <Award size={20} color="#38bdf8" />
      </div>

      <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
        {papers.map((p) => (
          <div
            key={p.id}
            style={{
              backgroundColor: 'rgba(15, 23, 42, 0.5)',
              border: '1px solid rgba(255, 255, 255, 0.05)',
              borderRadius: '10px',
              padding: '10px 12px',
              display: 'flex',
              flexDirection: 'column',
              gap: '4px',
            }}
          >
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <span style={{ fontSize: '0.85rem', fontWeight: 700, color: '#f1f5f9' }}>{p.title}</span>
              <span
                style={{
                  backgroundColor: 'rgba(56, 189, 248, 0.15)',
                  color: '#38bdf8',
                  fontSize: '0.7rem',
                  fontWeight: 700,
                  padding: '2px 6px',
                  borderRadius: '4px',
                }}
              >
                {p.indexing}
              </span>
            </div>

            <div style={{ fontSize: '0.75rem', color: '#94a3b8' }}>
              Authors: <strong style={{ color: '#cbd5e1' }}>{p.authors}</strong>
            </div>

            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', fontSize: '0.72rem', color: '#64748b', marginTop: '2px' }}>
              <span>{p.journal} ({p.year})</span>
              <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
                <span style={{ color: '#34d399', fontWeight: 600 }}>{p.citations} Citations</span>
                <button
                  onClick={() => handleDownloadBibTeX(p.title)}
                  style={{
                    backgroundColor: 'transparent',
                    border: 'none',
                    color: '#38bdf8',
                    cursor: 'pointer',
                    fontSize: '0.72rem',
                    textDecoration: 'underline',
                  }}
                >
                  Export BibTeX
                </button>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
