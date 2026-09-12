import React from 'react';
import { Bot, Sparkles, ArrowRight } from 'lucide-react';
import { useNavigate } from 'react-router-dom';

export const ParentAICopilotCard: React.FC = () => {
  const navigate = useNavigate();

  const sampleQuestions = [
    "How is my child's attendance?",
    "What exams are coming up?",
    "Which assignments are pending?",
    "Are there any outstanding fees?",
  ];

  return (
    <div
      style={{
        background: 'linear-gradient(135deg, rgba(168, 85, 247, 0.2), rgba(37, 99, 235, 0.15))',
        backdropFilter: 'blur(16px)',
        border: '1px solid rgba(168, 85, 247, 0.3)',
        borderRadius: '20px',
        padding: '1.5rem',
        display: 'flex',
        flexDirection: 'column',
        gap: '12px',
        boxShadow: '0 8px 32px rgba(168, 85, 247, 0.1)',
      }}
    >
      <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
        <div
          style={{
            width: '42px',
            height: '42px',
            borderRadius: '12px',
            background: 'linear-gradient(135deg, #a855f7, #6366f1)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            color: '#ffffff',
          }}
        >
          <Bot size={22} />
        </div>
        <div>
          <h3 style={{ fontSize: '1.1rem', fontWeight: 800, color: '#f8fafc', margin: 0 }}>
            🤖 UniSphere AI Parent Copilot
          </h3>
          <p style={{ fontSize: '0.78rem', color: '#cbd5e1', margin: '2px 0 0 0' }}>
            Ask intelligent questions about your child's university progress & schedule
          </p>
        </div>
      </div>

      <div style={{ display: 'flex', flexDirection: 'column', gap: '6px', margin: '6px 0' }}>
        {sampleQuestions.map((q, i) => (
          <button
            key={i}
            onClick={() => navigate('/parent/ai')}
            style={{
              backgroundColor: 'rgba(15, 23, 42, 0.6)',
              border: '1px solid rgba(255, 255, 255, 0.08)',
              borderRadius: '8px',
              padding: '8px 12px',
              color: '#e2e8f0',
              fontSize: '0.8rem',
              textAlign: 'left',
              cursor: 'pointer',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'space-between',
              transition: 'all 0.15s ease',
            }}
          >
            <span>"{q}"</span>
            <Sparkles size={14} color="#a855f7" />
          </button>
        ))}
      </div>

      <button
        onClick={() => navigate('/parent/ai')}
        style={{
          backgroundColor: '#a855f7',
          border: 'none',
          color: '#ffffff',
          borderRadius: '10px',
          padding: '10px 16px',
          fontSize: '0.85rem',
          fontWeight: 700,
          cursor: 'pointer',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          gap: '8px',
          boxShadow: '0 4px 14px rgba(168, 85, 247, 0.4)',
        }}
      >
        Open AI Copilot Chat <ArrowRight size={16} />
      </button>
    </div>
  );
};
