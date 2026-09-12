import React, { useState } from 'react';
import { Card } from '../../components/Card';
import { Button } from '../../components/Button';
import { Clock, BookOpen, FlaskConical, Users, CheckCircle, AlertTriangle } from 'lucide-react';

export const FacultyWorkloadPage: React.FC = () => {
  const [facultyWorkloads] = useState([
    { id: '1', name: 'Dr. Sarah Jenkins', dept: 'Computer Science', teachingHours: 14, researchHours: 8, adminHours: 4, totalLoad: 26, status: 'BALANCED' },
    { id: '2', name: 'Prof. Marcus Vance', dept: 'Electrical Engineering', teachingHours: 18, researchHours: 6, adminHours: 6, totalLoad: 30, status: 'OVERLOADED' },
    { id: '3', name: 'Dr. Elena Rostova', dept: 'Mathematics', teachingHours: 10, researchHours: 12, adminHours: 2, totalLoad: 24, status: 'BALANCED' },
  ]);

  return (
    <div style={{ padding: '2rem', maxWidth: '1100px', margin: '0 auto' }}>
      <div style={{ marginBottom: '2rem' }}>
        <h1 style={{ fontSize: '1.8rem', fontWeight: 800, color: '#f8fafc', margin: 0 }}>
          Faculty Workload & Credit Allocation
        </h1>
        <p style={{ color: '#94a3b8', margin: '4px 0 0 0', fontSize: '0.9rem' }}>
          Monitor teaching credit hours, research commitments, and department administrative load.
        </p>
      </div>

      <div style={{ display: 'grid', gap: '1rem' }}>
        {facultyWorkloads.map((fac) => (
          <Card key={fac.id} style={{ padding: '1.5rem', backgroundColor: 'rgba(15, 23, 42, 0.6)', border: '1px solid rgba(255, 255, 255, 0.08)', borderRadius: '16px' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1rem' }}>
              <div>
                <h3 style={{ margin: 0, fontSize: '1.1rem', color: '#f8fafc', fontWeight: 700 }}>{fac.name}</h3>
                <span style={{ fontSize: '0.8rem', color: '#94a3b8' }}>{fac.dept}</span>
              </div>
              <span style={{ padding: '4px 12px', borderRadius: '12px', background: fac.status === 'OVERLOADED' ? 'rgba(239, 68, 68, 0.15)' : 'rgba(16, 185, 129, 0.15)', color: fac.status === 'OVERLOADED' ? '#ef4444' : '#10b981', fontWeight: 700, fontSize: '0.8rem' }}>
                {fac.status} ({fac.totalLoad} Credit Hours)
              </span>
            </div>

            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr 1fr', gap: '1rem' }}>
              <div style={{ padding: '10px', background: 'rgba(255,255,255,0.03)', borderRadius: '8px', display: 'flex', alignItems: 'center', gap: '10px' }}>
                <BookOpen size={18} color="#38bdf8" />
                <div>
                  <div style={{ fontSize: '0.75rem', color: '#94a3b8' }}>Teaching Load</div>
                  <div style={{ fontSize: '1rem', fontWeight: 700, color: '#fff' }}>{fac.teachingHours} hrs/wk</div>
                </div>
              </div>

              <div style={{ padding: '10px', background: 'rgba(255,255,255,0.03)', borderRadius: '8px', display: 'flex', alignItems: 'center', gap: '10px' }}>
                <FlaskConical size={18} color="#a855f7" />
                <div>
                  <div style={{ fontSize: '0.75rem', color: '#94a3b8' }}>Research Hours</div>
                  <div style={{ fontSize: '1rem', fontWeight: 700, color: '#fff' }}>{fac.researchHours} hrs/wk</div>
                </div>
              </div>

              <div style={{ padding: '10px', background: 'rgba(255,255,255,0.03)', borderRadius: '8px', display: 'flex', alignItems: 'center', gap: '10px' }}>
                <Clock size={18} color="#f59e0b" />
                <div>
                  <div style={{ fontSize: '0.75rem', color: '#94a3b8' }}>Admin Duty</div>
                  <div style={{ fontSize: '1rem', fontWeight: 700, color: '#fff' }}>{fac.adminHours} hrs/wk</div>
                </div>
              </div>
            </div>
          </Card>
        ))}
      </div>
    </div>
  );
};
