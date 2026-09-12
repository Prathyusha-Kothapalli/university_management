import React, { useState } from 'react';
import { Card } from '../../components/Card';
import { Button } from '../../components/Button';
import { User, ShieldAlert, Award, FileText, CheckCircle2, AlertOctagon, GraduationCap, Plus } from 'lucide-react';

export const StudentDetailPage: React.FC = () => {
  const [activeTab, setActiveTab] = useState<'profile' | 'holds' | 'history'>('profile');
  const [holds, setHolds] = useState([
    { id: '1', type: 'FINANCIAL', reason: 'Unpaid Library Overdue Fee ($45.00)', placedBy: 'Bursar Office', date: '2026-09-01' },
  ]);

  return (
    <div style={{ padding: '2rem', maxWidth: '1100px', margin: '0 auto' }}>
      {/* Student Overview Header */}
      <Card style={{ padding: '1.5rem', backgroundColor: 'rgba(15, 23, 42, 0.6)', border: '1px solid rgba(255, 255, 255, 0.08)', borderRadius: '16px', marginBottom: '1.5rem' }}>
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '1.25rem' }}>
            <div style={{ width: '64px', height: '64px', borderRadius: '18px', background: 'linear-gradient(135deg, #2563eb, #38bdf8)', display: 'flex', alignItems: 'center', justifyContent: 'center', color: '#fff', fontSize: '1.8rem', fontWeight: 800 }}>
              AM
            </div>
            <div>
              <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                <h1 style={{ margin: 0, fontSize: '1.5rem', fontWeight: 800, color: '#f8fafc' }}>Alex Morgan</h1>
                <span style={{ padding: '2px 10px', borderRadius: '12px', background: 'rgba(16, 185, 129, 0.15)', color: '#10b981', fontSize: '0.75rem', fontWeight: 600 }}>
                  Active Enrolled
                </span>
              </div>
              <p style={{ margin: '4px 0 0 0', color: '#94a3b8', fontSize: '0.85rem' }}>
                B.S. Computer Science & Artificial Intelligence • Roll #: STU20260481 • Year 3 (Sem 6)
              </p>
            </div>
          </div>
          <div style={{ textAlign: 'right' }}>
            <div style={{ fontSize: '1.6rem', fontWeight: 800, color: '#38bdf8' }}>3.88 CGPA</div>
            <span style={{ fontSize: '0.75rem', color: '#10b981', fontWeight: 600 }}>Dean's High Honors</span>
          </div>
        </div>

        {/* Tab Navigation */}
        <div style={{ display: 'flex', gap: '1rem', borderTop: '1px solid rgba(255,255,255,0.08)', marginTop: '1.5rem', paddingTop: '1rem' }}>
          <button
            onClick={() => setActiveTab('profile')}
            style={{ padding: '8px 16px', borderRadius: '8px', border: 'none', background: activeTab === 'profile' ? '#2563eb' : 'transparent', color: activeTab === 'profile' ? '#fff' : '#94a3b8', cursor: 'pointer', fontWeight: 600 }}
          >
            360 Profile Summary
          </button>
          <button
            onClick={() => setActiveTab('holds')}
            style={{ padding: '8px 16px', borderRadius: '8px', border: 'none', background: activeTab === 'holds' ? '#2563eb' : 'transparent', color: activeTab === 'holds' ? '#fff' : '#94a3b8', cursor: 'pointer', fontWeight: 600, display: 'flex', alignItems: 'center', gap: '6px' }}
          >
            <ShieldAlert size={16} /> Holds & Blocks ({holds.length})
          </button>
        </div>
      </Card>

      {/* Tab Contents */}
      {activeTab === 'profile' ? (
        <div style={{ display: 'grid', gridTemplateColumns: '2fr 1fr', gap: '1.5rem' }}>
          <Card style={{ padding: '1.5rem', backgroundColor: 'rgba(15, 23, 42, 0.6)', border: '1px solid rgba(255, 255, 255, 0.08)' }}>
            <h3 style={{ color: '#f8fafc', marginTop: 0 }}>Academic History & Credit Progress</h3>
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr 1fr', gap: '1rem', margin: '1rem 0' }}>
              <div style={{ padding: '12px', background: 'rgba(255,255,255,0.03)', borderRadius: '10px' }}>
                <span style={{ fontSize: '0.75rem', color: '#94a3b8' }}>Total Earned Credits</span>
                <div style={{ fontSize: '1.2rem', fontWeight: 700, color: '#fff', marginTop: '4px' }}>96 / 120</div>
              </div>
              <div style={{ padding: '12px', background: 'rgba(255,255,255,0.03)', borderRadius: '10px' }}>
                <span style={{ fontSize: '0.75rem', color: '#94a3b8' }}>Major GPA</span>
                <div style={{ fontSize: '1.2rem', fontWeight: 700, color: '#38bdf8', marginTop: '4px' }}>3.92</div>
              </div>
              <div style={{ padding: '12px', background: 'rgba(255,255,255,0.03)', borderRadius: '10px' }}>
                <span style={{ fontSize: '0.75rem', color: '#94a3b8' }}>Attendance Rate</span>
                <div style={{ fontSize: '1.2rem', fontWeight: 700, color: '#10b981', marginTop: '4px' }}>94.2%</div>
              </div>
            </div>
          </Card>

          <Card style={{ padding: '1.5rem', backgroundColor: 'rgba(15, 23, 42, 0.6)', border: '1px solid rgba(255, 255, 255, 0.08)' }}>
            <h3 style={{ color: '#f8fafc', marginTop: 0 }}>Academic Advisor</h3>
            <p style={{ color: '#cbd5e1', fontSize: '0.9rem', margin: '4px 0' }}>Dr. Sarah Jenkins</p>
            <span style={{ fontSize: '0.8rem', color: '#94a3b8' }}>Dept of Computer Science</span>
            <Button variant="outline" size="sm" style={{ width: '100%', marginTop: '1rem' }}>
              Schedule Advisory Session
            </Button>
          </Card>
        </div>
      ) : (
        <Card style={{ padding: '1.5rem', backgroundColor: 'rgba(15, 23, 42, 0.6)', border: '1px solid rgba(255, 255, 255, 0.08)' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1rem' }}>
            <h3 style={{ color: '#f8fafc', margin: 0 }}>Active Registration & Transcript Holds</h3>
            <Button variant="primary" size="sm">
              <Plus size={14} style={{ marginRight: '4px' }} /> Place Administrative Hold
            </Button>
          </div>

          {holds.map((hold) => (
            <div key={hold.id} style={{ padding: '1rem', background: 'rgba(239, 68, 68, 0.08)', border: '1px solid rgba(239, 68, 68, 0.2)', borderRadius: '12px', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <div>
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                  <AlertOctagon size={18} color="#ef4444" />
                  <span style={{ fontWeight: 700, color: '#ef4444', fontSize: '0.9rem' }}>{hold.type} HOLD</span>
                  <span style={{ color: '#94a3b8', fontSize: '0.75rem' }}>Placed by {hold.placedBy} on {hold.date}</span>
                </div>
                <p style={{ margin: '4px 0 0 26px', color: '#f8fafc', fontSize: '0.85rem' }}>{hold.reason}</p>
              </div>
              <Button variant="outline" size="sm" style={{ borderColor: 'rgba(16, 185, 129, 0.4)', color: '#10b981' }}>
                Resolve & Lift Hold
              </Button>
            </div>
          ))}
        </Card>
      )}
    </div>
  );
};
