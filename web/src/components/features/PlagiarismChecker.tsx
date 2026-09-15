import React, { useState } from 'react';
import { FileCheck } from 'lucide-react';
import { useToast } from '../../hooks/useToast';

export const PlagiarismChecker: React.FC = () => {
  const { showToast } = useToast();
  const [similarityScore, setSimilarityScore] = useState<number | null>(4.2);
  const [isScanning, setIsScanning] = useState(false);

  const handleScan = () => {
    setIsScanning(true);
    showToast('AI Plagiarism Scanner: Analyzing document against IEEE/GitHub repository database...', 'info');
    setTimeout(() => {
      setIsScanning(false);
      setSimilarityScore(3.8);
      showToast('Scan complete: 3.8% Similarity Index (Original & Verified)', 'success');
    }, 1500);
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
            AI Assignment Plagiarism & Similarity Scanner
          </h3>
          <p style={{ fontSize: '0.78rem', color: '#94a3b8', margin: '2px 0 0 0' }}>
            Instant Turnitin-style plagiarism verification for student code & lab reports
          </p>
        </div>
        <FileCheck size={20} color="#34d399" />
      </div>

      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', backgroundColor: 'rgba(15, 23, 42, 0.5)', padding: '12px 14px', borderRadius: '10px' }}>
        <div>
          <div style={{ fontSize: '0.85rem', fontWeight: 700, color: '#f1f5f9' }}>Binary Search Tree Optimization Lab.pdf</div>
          <div style={{ fontSize: '0.72rem', color: '#64748b', marginTop: '2px' }}>
            Submitted: Sept 12, 2026 • 2.4 MB
          </div>
        </div>

        <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
          {similarityScore !== null && (
            <div style={{ textAlign: 'right' }}>
              <div style={{ fontSize: '1rem', fontWeight: 800, color: '#34d399' }}>{similarityScore}%</div>
              <div style={{ fontSize: '0.68rem', color: '#34d399', fontWeight: 600 }}>Original</div>
            </div>
          )}
          <button
            onClick={handleScan}
            disabled={isScanning}
            style={{
              backgroundColor: 'rgba(52, 211, 153, 0.15)',
              border: '1px solid rgba(52, 211, 153, 0.3)',
              color: '#34d399',
              borderRadius: '8px',
              padding: '6px 12px',
              fontSize: '0.78rem',
              fontWeight: 600,
              cursor: 'pointer',
            }}
          >
            {isScanning ? 'Scanning...' : 'Re-Scan Paper'}
          </button>
        </div>
      </div>
    </div>
  );
};
