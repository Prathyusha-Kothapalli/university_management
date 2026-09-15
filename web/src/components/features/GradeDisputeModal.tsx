import React, { useState } from 'react';
import { useToast } from '../../hooks/useToast';

export const GradeDisputeModal: React.FC = () => {
  const { showToast } = useToast();
  const [requests, setRequests] = useState([
    { id: 'DIS-01', subject: 'Operating Systems (Mid-Sem)', currentGrade: 'B+', reason: 'Totaling mismatch in Question 3 (Memory Page Table calculation)', status: 'Under Review' },
  ]);

  const handleCreateDispute = () => {
    const newReq = {
      id: `DIS-0${requests.length + 1}`,
      subject: 'Database Management Systems',
      currentGrade: 'A-',
      reason: 'Re-checking requested for B+ Tree balancing proof',
      status: 'Submitted',
    };
    setRequests([newReq, ...requests]);
    showToast('Submitted grade re-evaluation request to Exam Cell & HOD', 'success');
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
            Exam Paper Re-evaluation & Grade Dispute Resolution
          </h3>
          <p style={{ fontSize: '0.78rem', color: '#94a3b8', margin: '2px 0 0 0' }}>
            Submit re-checking requests for mid-term or end-semester evaluation answer scripts
          </p>
        </div>

        <button
          onClick={handleCreateDispute}
          style={{
            backgroundColor: 'rgba(245, 158, 11, 0.15)',
            border: '1px solid rgba(245, 158, 11, 0.3)',
            color: '#f59e0b',
            borderRadius: '8px',
            padding: '6px 12px',
            fontSize: '0.78rem',
            fontWeight: 700,
            cursor: 'pointer',
          }}
        >
          Request Re-evaluation
        </button>
      </div>

      <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
        {requests.map((r) => (
          <div
            key={r.id}
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
              <div style={{ fontSize: '0.85rem', fontWeight: 700, color: '#f1f5f9' }}>{r.subject}</div>
              <div style={{ fontSize: '0.75rem', color: '#94a3b8', marginTop: '2px' }}>
                Grade: <strong style={{ color: '#38bdf8' }}>{r.currentGrade}</strong> • Reason: "{r.reason}"
              </div>
            </div>

            <span
              style={{
                backgroundColor: 'rgba(245, 158, 11, 0.15)',
                color: '#f59e0b',
                fontSize: '0.72rem',
                fontWeight: 700,
                padding: '2px 8px',
                borderRadius: '6px',
              }}
            >
              {r.status}
            </span>
          </div>
        ))}
      </div>
    </div>
  );
};
