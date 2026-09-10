import React, { useState } from 'react';
import { Briefcase, Sparkles } from 'lucide-react';
import { useToast } from '../../hooks/useToast';

export const ResumeAnalyzer: React.FC = () => {
  const { showToast } = useToast();
  const [matchScore, setMatchScore] = useState(88);

  const missingSkills = ['Docker Containerization', 'Kubernetes Deployment', 'System Design'];

  const handleAnalyze = () => {
    showToast('AI Career Coach: Matching resume against TechCorp Software Engineer JD...', 'info');
    setTimeout(() => {
      setMatchScore(92);
      showToast('Resume match score updated: 92% Match (Highly Recommended)', 'success');
    }, 1200);
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
          <h3 style={{ fontSize: '1.05rem', fontWeight: 700, color: '#f8fafc', margin: 0, display: 'flex', alignItems: 'center', gap: '6px' }}>
            <Sparkles size={18} color="#a855f7" /> AI Placement Resume Matcher & Skill Gap Analyzer
          </h3>
          <p style={{ fontSize: '0.78rem', color: '#94a3b8', margin: '2px 0 0 0' }}>
            Match student profile against corporate job descriptions to improve placement rates
          </p>
        </div>
        <Briefcase size={20} color="#a855f7" />
      </div>

      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', backgroundColor: 'rgba(15, 23, 42, 0.5)', padding: '12px 14px', borderRadius: '10px' }}>
        <div>
          <div style={{ fontSize: '0.85rem', fontWeight: 700, color: '#f1f5f9' }}>Target Role: TechCorp Systems - Graduate Software Engineer</div>
          <div style={{ fontSize: '0.75rem', color: '#94a3b8', marginTop: '2px' }}>
            Recommended Skill Additions: <span style={{ color: '#f59e0b' }}>{missingSkills.join(', ')}</span>
          </div>
        </div>

        <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
          <div style={{ textAlign: 'right' }}>
            <div style={{ fontSize: '1.1rem', fontWeight: 800, color: '#a855f7' }}>{matchScore}%</div>
            <div style={{ fontSize: '0.68rem', color: '#a855f7', fontWeight: 600 }}>JD Match</div>
          </div>
          <button
            onClick={handleAnalyze}
            style={{
              backgroundColor: 'rgba(168, 85, 247, 0.15)',
              border: '1px solid rgba(168, 85, 247, 0.3)',
              color: '#c084fc',
              borderRadius: '8px',
              padding: '6px 12px',
              fontSize: '0.78rem',
              fontWeight: 600,
              cursor: 'pointer',
            }}
          >
            Analyze Resume
          </button>
        </div>
      </div>
    </div>
  );
};
