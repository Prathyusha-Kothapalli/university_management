import React, { useState } from 'react';
import { Sparkles } from 'lucide-react';
import { useToast } from '../../hooks/useToast';

export const StudyPlannerModal: React.FC = () => {
  const { showToast } = useToast();
  const [isGenerated, setIsGenerated] = useState(false);

  const roadmap = [
    { day: 'Monday (Sept 14)', subject: 'Operating Systems', focus: 'Process Synchronization & Semaphores', duration: '2.5 hrs' },
    { day: 'Tuesday (Sept 15)', subject: 'Database Management Systems', focus: 'B+ Tree Indexing & 3NF Normalization', duration: '3.0 hrs' },
    { day: 'Wednesday (Sept 16)', subject: 'Computer Networks', focus: 'TCP Flow Control & Subnetting', duration: '2.0 hrs' },
    { day: 'Thursday (Sept 17)', subject: 'Data Structures & Algorithms', focus: 'Graph Traversal (BFS/DFS) & Dijkstra', duration: '2.5 hrs' },
  ];

  const handleGenerate = () => {
    setIsGenerated(true);
    showToast('AI Generated 7-Day Exam Preparation Roadmap!', 'success');
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
          <h3 style={{ fontSize: '1.05rem', fontWeight: 700, color: '#f8fafc', margin: 0, display: 'flex', alignItems: 'center', gap: '6px' }}>
            <Sparkles size={18} color="#38bdf8" /> AI Study Roadmap Generator
          </h3>
          <p style={{ fontSize: '0.78rem', color: '#94a3b8', margin: '2px 0 0 0' }}>
            Smart study planner tailored to your upcoming mid-term exam schedule
          </p>
        </div>

        <button
          onClick={handleGenerate}
          style={{
            backgroundColor: isGenerated ? '#059669' : '#2563eb',
            border: 'none',
            color: '#ffffff',
            borderRadius: '8px',
            padding: '6px 12px',
            fontSize: '0.78rem',
            fontWeight: 700,
            cursor: 'pointer',
            display: 'flex',
            alignItems: 'center',
            gap: '4px',
          }}
        >
          <Sparkles size={14} /> {isGenerated ? 'Roadmap Synced' : 'Generate Roadmap'}
        </button>
      </div>

      <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
        {roadmap.map((item, i) => (
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
              <div style={{ fontSize: '0.825rem', fontWeight: 700, color: '#38bdf8' }}>{item.day}: {item.subject}</div>
              <div style={{ fontSize: '0.75rem', color: '#cbd5e1', marginTop: '2px' }}>Topic Focus: {item.focus}</div>
            </div>
            <span style={{ fontSize: '0.72rem', fontWeight: 600, color: '#34d399', backgroundColor: 'rgba(52, 211, 153, 0.12)', padding: '2px 8px', borderRadius: '4px' }}>
              {item.duration}
            </span>
          </div>
        ))}
      </div>
    </div>
  );
};
