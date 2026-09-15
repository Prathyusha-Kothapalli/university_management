import React from 'react';
import { FileText, Download } from 'lucide-react';
import { useToast } from '../../hooks/useToast';

export const DocumentSummary: React.FC = () => {
  const { showToast } = useToast();

  const documents = [
    { title: 'Student Identity Card', file: 'STU-2026-001_ID.pdf', size: '1.2 MB' },
    { title: 'Academic Grade Transcript (Sem 1-4)', file: 'Official_Transcript_STU001.pdf', size: '2.4 MB' },
    { title: 'Fee Payment Receipt (Inst. 2)', file: 'Fee_Receipt_Aug2026.pdf', size: '650 KB' },
    { title: 'University Admission Confirmation Letter', file: 'Admission_Confirmation.pdf', size: '890 KB' },
  ];

  const handleDownloadDoc = (title: string) => {
    showToast(`Downloading authorized document: "${title}"`, 'info');
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
            Student Document Vault & Certificates
          </h3>
          <p style={{ fontSize: '0.78rem', color: '#94a3b8', margin: '2px 0 0 0' }}>
            Official student records, transcripts, and payment receipts
          </p>
        </div>
        <FileText size={20} color="#38bdf8" />
      </div>

      <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
        {documents.map((d, i) => (
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
              <div style={{ fontSize: '0.85rem', fontWeight: 600, color: '#f1f5f9' }}>{d.title}</div>
              <div style={{ fontSize: '0.72rem', color: '#64748b', marginTop: '2px' }}>{d.file} ({d.size})</div>
            </div>
            <button
              onClick={() => handleDownloadDoc(d.title)}
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
              <Download size={13} /> Download
            </button>
          </div>
        ))}
      </div>
    </div>
  );
};
