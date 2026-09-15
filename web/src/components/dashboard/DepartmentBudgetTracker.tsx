import React, { useState } from 'react';
import { DollarSign } from 'lucide-react';
import { useToast } from '../../hooks/useToast';

interface GrantRequest {
  id: string;
  applicant: string;
  projectTitle: string;
  amount: number;
  category: string;
  status: 'Pending' | 'Approved' | 'Rejected';
}

export const DepartmentBudgetTracker: React.FC = () => {
  const { showToast } = useToast();

  const totalBudget = 150000;
  const spent = 92400;
  const remaining = totalBudget - spent;
  const percentSpent = Math.round((spent / totalBudget) * 100);

  const categories = [
    { name: 'Lab Hardware & GPUs', allocated: 60000, spent: 42000, color: '#38bdf8' },
    { name: 'Software & Cloud Licenses', allocated: 35000, spent: 21500, color: '#a855f7' },
    { name: 'Research Seed Grants', allocated: 35000, spent: 20000, color: '#34d399' },
    { name: 'Conferences & Seminars', allocated: 20000, spent: 8900, color: '#f59e0b' },
  ];

  const [grants, setGrants] = useState<GrantRequest[]>([
    {
      id: 'GR-201',
      applicant: 'Dr. Emily Vance',
      projectTitle: 'LLM Fine-Tuning Server Upgrade',
      amount: 12500,
      category: 'Research Grant',
      status: 'Pending',
    },
    {
      id: 'GR-202',
      applicant: 'Prof. Michael Scott',
      projectTitle: 'Kubernetes Cluster Cloud Testing Credit',
      amount: 4800,
      category: 'Cloud License',
      status: 'Pending',
    },
  ]);

  const handleApproveGrant = (id: string, title: string, amount: number) => {
    setGrants((prev) =>
      prev.map((g) => (g.id === id ? { ...g, status: 'Approved' } : g))
    );
    showToast(`Approved grant "${title}" ($${amount.toLocaleString()})`, 'success');
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
            Department Budget & Research Grant Allocations
          </h3>
          <p style={{ fontSize: '0.78rem', color: '#94a3b8', margin: '2px 0 0 0' }}>
            Annual Budget: <strong style={{ color: '#34d399' }}>${totalBudget.toLocaleString()}</strong> | Spent: <strong style={{ color: '#38bdf8' }}>${spent.toLocaleString()} ({percentSpent}%)</strong> | Remaining: <strong style={{ color: '#f59e0b' }}>${remaining.toLocaleString()}</strong>
          </p>
        </div>
        <DollarSign size={20} color="#34d399" />
      </div>

      {/* Progress Bar */}
      <div style={{ marginBottom: '1.25rem' }}>
        <div style={{ height: '8px', width: '100%', backgroundColor: 'rgba(255, 255, 255, 0.08)', borderRadius: '4px', overflow: 'hidden' }}>
          <div style={{ height: '100%', width: `${percentSpent}%`, background: 'linear-gradient(90deg, #0284c7, #34d399)', borderRadius: '4px' }} />
        </div>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1rem', marginBottom: '1rem' }}>
        {/* Category Breakdown */}
        <div>
          <div style={{ fontSize: '0.8rem', fontWeight: 600, color: '#cbd5e1', marginBottom: '8px' }}>
            Budget Category Utilization
          </div>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
            {categories.map((cat) => {
              const catPercent = Math.round((cat.spent / cat.allocated) * 100);
              return (
                <div key={cat.name} style={{ fontSize: '0.78rem' }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', color: '#94a3b8', marginBottom: '3px' }}>
                    <span>{cat.name}</span>
                    <span style={{ fontWeight: 600, color: '#f8fafc' }}>
                      ${cat.spent.toLocaleString()} / ${cat.allocated.toLocaleString()} ({catPercent}%)
                    </span>
                  </div>
                  <div style={{ height: '5px', width: '100%', backgroundColor: 'rgba(255, 255, 255, 0.06)', borderRadius: '3px', overflow: 'hidden' }}>
                    <div style={{ height: '100%', width: `${catPercent}%`, backgroundColor: cat.color, borderRadius: '3px' }} />
                  </div>
                </div>
              );
            })}
          </div>
        </div>

        {/* Pending Grant Approvals */}
        <div>
          <div style={{ fontSize: '0.8rem', fontWeight: 600, color: '#cbd5e1', marginBottom: '8px' }}>
            Pending Research Grant Approvals
          </div>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
            {grants.map((g) => (
              <div
                key={g.id}
                style={{
                  backgroundColor: 'rgba(15, 23, 42, 0.5)',
                  border: '1px solid rgba(255, 255, 255, 0.05)',
                  borderRadius: '8px',
                  padding: '8px 10px',
                  display: 'flex',
                  flexDirection: 'column',
                  gap: '4px',
                }}
              >
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                  <span style={{ fontSize: '0.8rem', fontWeight: 600, color: '#f1f5f9' }}>{g.projectTitle}</span>
                  <span style={{ fontSize: '0.8rem', fontWeight: 700, color: '#34d399' }}>${g.amount.toLocaleString()}</span>
                </div>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', fontSize: '0.72rem', color: '#64748b' }}>
                  <span>{g.applicant} • {g.category}</span>
                  {g.status === 'Pending' ? (
                    <button
                      onClick={() => handleApproveGrant(g.id, g.projectTitle, g.amount)}
                      style={{
                        backgroundColor: 'rgba(52, 211, 153, 0.15)',
                        border: '1px solid rgba(52, 211, 153, 0.3)',
                        color: '#34d399',
                        borderRadius: '4px',
                        padding: '2px 8px',
                        fontSize: '0.7rem',
                        fontWeight: 600,
                        cursor: 'pointer',
                      }}
                    >
                      Approve Grant
                    </button>
                  ) : (
                    <span style={{ color: '#34d399', fontWeight: 600 }}>Approved</span>
                  )}
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};
