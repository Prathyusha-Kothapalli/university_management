import React, { useState } from 'react';
import { Card } from '../../components/Card';
import { Button } from '../../components/Button';
import { useToast } from '../../hooks/useToast';
import { Award, CheckCircle, XCircle, Award as MeritIcon, Users } from 'lucide-react';

export const AdmissionReviewPage: React.FC = () => {
  const { showToast } = useToast();
  const [applications, setApplications] = useState([
    { id: '1', name: 'Taylor Swift', email: 'taylor@gmail.com', gpa: 3.85, examScore: 92.0, composite: 91.4, status: 'SUBMITTED' },
    { id: '2', name: 'Ethan Hunt', email: 'ethan@imf.gov', gpa: 3.65, examScore: 88.0, composite: 85.7, status: 'SUBMITTED' },
  ]);

  const handleUpdateStatus = (id: string, newStatus: string) => {
    setApplications((prev) => prev.map((a) => (a.id === id ? { ...a, status: newStatus } : a)));
    showToast(`Applicant status updated to ${newStatus}`, 'success');
  };

  return (
    <div style={{ padding: '2rem', maxWidth: '1100px', margin: '0 auto' }}>
      <div style={{ marginBottom: '2rem' }}>
        <h1 style={{ fontSize: '1.8rem', fontWeight: 800, color: '#f8fafc', margin: 0 }}>
          Admission Committee Review & Merit List
        </h1>
        <p style={{ color: '#94a3b8', margin: '4px 0 0 0', fontSize: '0.9rem' }}>
          Evaluate applicant GPA, entrance exam rankings, and issue admission offer letters.
        </p>
      </div>

      <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
        {applications.map((app) => (
          <Card key={app.id} style={{ padding: '1.25rem 1.5rem', backgroundColor: 'rgba(15, 23, 42, 0.6)', border: '1px solid rgba(255, 255, 255, 0.08)', borderRadius: '16px' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <div>
                <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                  <span style={{ fontWeight: 700, color: '#f8fafc', fontSize: '1.1rem' }}>{app.name}</span>
                  <span style={{ padding: '2px 8px', borderRadius: '8px', background: 'rgba(37, 99, 235, 0.15)', color: '#38bdf8', fontSize: '0.75rem', fontWeight: 700 }}>
                    {app.status}
                  </span>
                </div>
                <p style={{ color: '#94a3b8', fontSize: '0.85rem', margin: '4px 0 0 0' }}>{app.email}</p>
                <div style={{ display: 'flex', gap: '1rem', marginTop: '8px', fontSize: '0.8rem', color: '#cbd5e1' }}>
                  <span>GPA: <strong>{app.gpa}</strong></span>
                  <span>Entrance Exam: <strong>{app.examScore}%</strong></span>
                  <span style={{ color: '#10b981' }}>Composite Merit Score: <strong>{app.composite}</strong></span>
                </div>
              </div>

              <div style={{ display: 'flex', gap: '8px' }}>
                <Button onClick={() => handleUpdateStatus(app.id, 'OFFERED')} variant="primary" size="sm">
                  Issue Offer Letter
                </Button>
                <Button onClick={() => handleUpdateStatus(app.id, 'REJECTED')} variant="outline" size="sm" style={{ color: '#ef4444', borderColor: 'rgba(239,68,68,0.3)' }}>
                  Reject Application
                </Button>
              </div>
            </div>
          </Card>
        ))}
      </div>
    </div>
  );
};
