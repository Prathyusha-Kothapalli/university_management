import React, { useState } from 'react';
import { Card } from '../../components/Card';
import { Button } from '../../components/Button';
import { useToast } from '../../hooks/useToast';
import { Award, DollarSign, CheckCircle2, XCircle, Plus, Filter } from 'lucide-react';

export const ScholarshipManagerPage: React.FC = () => {
  const { showToast } = useToast();
  const [scholarships, setScholarships] = useState([
    { id: '1', name: "Presidential Merit Excellence Grant", student: "Alex Morgan", amount: 6000, type: "MERIT", status: "APPROVED" },
    { id: '2', name: "Opportunity Need-Based Aid", student: "Jordan Lee", amount: 4500, type: "NEED_BASED", status: "PENDING" },
  ]);

  const handleApprove = (id: string) => {
    setScholarships((prev) => prev.map((s) => (s.id === id ? { ...s, status: 'APPROVED' } : s)));
    showToast('Scholarship application approved for disbursement.', 'success');
  };

  return (
    <div style={{ padding: '2rem', maxWidth: '1100px', margin: '0 auto' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '2rem' }}>
        <div>
          <h1 style={{ fontSize: '1.8rem', fontWeight: 800, color: '#f8fafc', margin: 0 }}>
            Scholarship Catalog & Financial Aid Management
          </h1>
          <p style={{ color: '#94a3b8', margin: '4px 0 0 0', fontSize: '0.9rem' }}>
            Review merit/need-based awards, disburse grants, and manage financial aid budgets.
          </p>
        </div>
        <Button variant="primary">
          <Plus size={16} style={{ marginRight: '6px' }} /> Create Scholarship Program
        </Button>
      </div>

      <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
        {scholarships.map((sch) => (
          <Card key={sch.id} style={{ padding: '1.25rem 1.5rem', backgroundColor: 'rgba(15, 23, 42, 0.6)', border: '1px solid rgba(255, 255, 255, 0.08)', borderRadius: '16px' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <div>
                <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                  <Award size={20} color="#f59e0b" />
                  <span style={{ fontWeight: 700, color: '#f8fafc', fontSize: '1.1rem' }}>{sch.name}</span>
                  <span style={{ padding: '2px 8px', borderRadius: '8px', background: sch.status === 'APPROVED' ? 'rgba(16, 185, 129, 0.15)' : 'rgba(245, 158, 11, 0.15)', color: sch.status === 'APPROVED' ? '#10b981' : '#f59e0b', fontSize: '0.75rem', fontWeight: 700 }}>
                    {sch.status}
                  </span>
                </div>
                <p style={{ color: '#94a3b8', fontSize: '0.85rem', margin: '4px 0 0 28px' }}>
                  Applicant: <strong>{sch.student}</strong> • Type: {sch.type} • Award: <strong style={{ color: '#10b981' }}>${sch.amount.toLocaleString()}</strong>
                </p>
              </div>

              {sch.status === 'PENDING' && (
                <Button onClick={() => handleApprove(sch.id)} variant="primary" size="sm">
                  Approve Award Grant
                </Button>
              )}
            </div>
          </Card>
        ))}
      </div>
    </div>
  );
};
