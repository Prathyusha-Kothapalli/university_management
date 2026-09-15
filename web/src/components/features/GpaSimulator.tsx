import React, { useState } from 'react';
import { Calculator, Award } from 'lucide-react';

export const GpaSimulator: React.FC = () => {
  const [currentGpa] = useState(8.42);
  const [targetGpa, setTargetGpa] = useState(8.80);

  const calculateRequiredGrade = () => {
    // Current credits 76, 18 credits this sem
    const requiredGradePoints = (targetGpa * 94 - currentGpa * 76) / 18;
    return Math.min(10.0, Math.max(6.0, requiredGradePoints)).toFixed(2);
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
            <Calculator size={18} color="#34d399" /> GPA & CGPA Target Calculator Simulator
          </h3>
          <p style={{ fontSize: '0.78rem', color: '#94a3b8', margin: '2px 0 0 0' }}>
            Model "What-If" grade scenarios for Semester 5 course offerings
          </p>
        </div>
        <Award size={20} color="#34d399" />
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr 1fr', gap: '10px' }}>
        <div style={{ backgroundColor: 'rgba(15, 23, 42, 0.5)', padding: '10px', borderRadius: '8px' }}>
          <div style={{ fontSize: '0.72rem', color: '#64748b' }}>Current CGPA</div>
          <div style={{ fontSize: '1.1rem', fontWeight: 800, color: '#f8fafc' }}>{currentGpa.toFixed(2)}</div>
        </div>
        <div style={{ backgroundColor: 'rgba(15, 23, 42, 0.5)', padding: '10px', borderRadius: '8px' }}>
          <div style={{ fontSize: '0.72rem', color: '#64748b' }}>Desired Target CGPA</div>
          <input
            type="number"
            step="0.05"
            max="10.0"
            value={targetGpa}
            onChange={(e) => setTargetGpa(Number(e.target.value))}
            style={{ backgroundColor: 'transparent', border: 'none', color: '#34d399', fontSize: '1.1rem', fontWeight: 800, outline: 'none', width: '100%' }}
          />
        </div>
        <div style={{ backgroundColor: 'rgba(15, 23, 42, 0.5)', padding: '10px', borderRadius: '8px' }}>
          <div style={{ fontSize: '0.72rem', color: '#64748b' }}>Required Sem 5 GPA</div>
          <div style={{ fontSize: '1.1rem', fontWeight: 800, color: '#38bdf8' }}>{calculateRequiredGrade()} GPA</div>
        </div>
      </div>
    </div>
  );
};
