import React, { useState } from 'react';

export const AssignmentsView: React.FC = () => {
  const [tab, setTab] = useState<'pending' | 'completed'>('pending');
  const [submittedId, setSubmittedId] = useState<string | null>(null);

  const assignments = [
    {
      id: 'a1',
      code: 'CS-401',
      title: 'Transformer Architecture Implementation',
      due: 'Sep 18, 2026',
      points: 100,
      status: 'Pending',
    },
    {
      id: 'a2',
      code: 'DS-310',
      title: 'MapReduce Distributed Log Analyzer',
      due: 'Sep 22, 2026',
      points: 100,
      status: 'Pending',
    },
    {
      id: 'a3',
      code: 'MATH-250',
      title: 'Lagrangian Dual Problem Set',
      due: 'Sep 05, 2026',
      points: 50,
      grade: '48/50',
      status: 'Completed',
    },
    {
      id: 'a4',
      code: 'ETH-102',
      title: 'Algorithmic Fairness Case Study',
      due: 'Aug 29, 2026',
      points: 50,
      grade: '46/50',
      status: 'Completed',
    },
  ];

  const filtered = assignments.filter((a) => {
    if (submittedId === a.id) return tab === 'completed';
    return tab === 'pending' ? a.status === 'Pending' : a.status === 'Completed';
  });

  return (
    <div style={{ padding: '1.25rem' }}>
      <div style={{ display: 'flex', gap: '8px', marginBottom: '1rem' }}>
        <button
          onClick={() => setTab('pending')}
          className={`btn ${tab === 'pending' ? 'btn-primary' : 'btn-secondary'}`}
          style={{ flex: 1, padding: '8px', fontSize: '0.825rem' }}
        >
          Pending
        </button>
        <button
          onClick={() => setTab('completed')}
          className={`btn ${tab === 'completed' ? 'btn-primary' : 'btn-secondary'}`}
          style={{ flex: 1, padding: '8px', fontSize: '0.825rem' }}
        >
          Completed
        </button>
      </div>

      <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
        {filtered.map((item) => (
          <div key={item.id} className="glass-panel" style={{ padding: '1rem' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <span style={{ fontSize: '0.75rem', fontWeight: 700, color: '#38bdf8' }}>{item.code}</span>
              <span style={{
                fontSize: '0.7rem',
                fontWeight: 700,
                color: item.status === 'Pending' && submittedId !== item.id ? '#f59e0b' : '#10b981',
                backgroundColor: item.status === 'Pending' && submittedId !== item.id ? 'rgba(245, 158, 11, 0.15)' : 'rgba(16, 185, 129, 0.15)',
                padding: '2px 8px',
                borderRadius: '8px',
              }}>
                {submittedId === item.id ? 'Submitted' : item.status}
              </span>
            </div>
            <div style={{ fontSize: '0.95rem', fontWeight: 700, color: '#f8fafc', marginTop: '6px' }}>
              {item.title}
            </div>
            <div style={{ fontSize: '0.75rem', color: '#94a3b8', marginTop: '4px' }}>
              Due: {item.due} • {item.points} Points Max
            </div>
            {tab === 'pending' && submittedId !== item.id && (
              <button
                onClick={() => setSubmittedId(item.id)}
                className="btn btn-primary"
                style={{ width: '100%', marginTop: '10px', padding: '8px', fontSize: '0.8rem' }}
              >
                📤 Upload & Submit
              </button>
            )}
          </div>
        ))}
      </div>
    </div>
  );
};
