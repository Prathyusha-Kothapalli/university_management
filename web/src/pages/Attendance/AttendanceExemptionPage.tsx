import React, { useState } from 'react';
import { Card } from '../../components/Card';
import { Button } from '../../components/Button';
import { useToast } from '../../hooks/useToast';
import { Calendar, FileCheck, Upload, CheckCircle, Clock, AlertTriangle, Plus } from 'lucide-react';

export const AttendanceExemptionPage: React.FC = () => {
  const { showToast } = useToast();
  const [exemptions, setExemptions] = useState([
    { id: '1', student: 'Alex Morgan', course: 'CS305 Operating Systems', type: 'MEDICAL', startDate: '2026-09-02', endDate: '2026-09-05', reason: 'Hospitalization for acute bronchitis', status: 'APPROVED' },
    { id: '2', name: 'Jordan Lee', course: 'MATH202 Linear Algebra', type: 'SPORTS', startDate: '2026-09-10', endDate: '2026-09-12', reason: 'Inter-university Track & Field Championship', status: 'PENDING' },
  ]);

  const handleApprove = (id: string) => {
    setExemptions((prev) => prev.map((e) => (e.id === id ? { ...e, status: 'APPROVED' } : e)));
    showToast('Attendance exemption request approved.', 'success');
  };

  return (
    <div style={{ padding: '2rem', maxWidth: '1100px', margin: '0 auto' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '2rem' }}>
        <div>
          <h1 style={{ fontSize: '1.8rem', fontWeight: 800, color: '#f8fafc', margin: 0 }}>
            Attendance Exemption Approvals
          </h1>
          <p style={{ color: '#94a3b8', margin: '4px 0 0 0', fontSize: '0.9rem' }}>
            Review medical, sports, and official duty absence excusal requests.
          </p>
        </div>
        <Button variant="primary">
          <Plus size={16} style={{ marginRight: '6px' }} /> Submit Exemption Request
        </Button>
      </div>

      <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
        {exemptions.map((ex) => (
          <Card key={ex.id} style={{ padding: '1.25rem 1.5rem', backgroundColor: 'rgba(15, 23, 42, 0.6)', border: '1px solid rgba(255, 255, 255, 0.08)', borderRadius: '16px' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
              <div>
                <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                  <span style={{ fontWeight: 700, color: '#f8fafc', fontSize: '1rem' }}>{ex.student || ex.name}</span>
                  <span style={{ padding: '2px 8px', borderRadius: '8px', background: 'rgba(37, 99, 235, 0.15)', color: '#38bdf8', fontSize: '0.75rem', fontWeight: 700 }}>
                    {ex.type}
                  </span>
                  <span style={{ padding: '2px 8px', borderRadius: '8px', background: ex.status === 'APPROVED' ? 'rgba(16, 185, 129, 0.15)' : 'rgba(245, 158, 11, 0.15)', color: ex.status === 'APPROVED' ? '#10b981' : '#f59e0b', fontSize: '0.75rem', fontWeight: 700 }}>
                    {ex.status}
                  </span>
                </div>
                <p style={{ color: '#cbd5e1', fontSize: '0.85rem', margin: '6px 0 0 0' }}>{ex.course} • Dates: {ex.startDate} to {ex.endDate}</p>
                <p style={{ color: '#94a3b8', fontSize: '0.8rem', margin: '4px 0 0 0' }}>Reason: "{ex.reason}"</p>
              </div>

              {ex.status === 'PENDING' && (
                <Button onClick={() => handleApprove(ex.id)} variant="primary" size="sm">
                  Approve Exemption
                </Button>
              )}
            </div>
          </Card>
        ))}
      </div>
    </div>
  );
};
