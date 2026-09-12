import React, { useState } from 'react';
import { Layers } from 'lucide-react';
import { useToast } from '../../hooks/useToast';

interface SyllabusChangeRequest {
  id: string;
  courseCode: string;
  courseName: string;
  proposedBy: string;
  changeDescription: string;
  status: 'Pending' | 'Approved' | 'Rejected';
}

export const SyllabusApprovalMatrix: React.FC = () => {
  const { showToast } = useToast();

  const coPoAttainment = [
    { po: 'PO1: Engineering Knowledge', attainment: 88.4, target: 85.0 },
    { po: 'PO2: Problem Analysis & Design', attainment: 84.2, target: 80.0 },
    { po: 'PO3: AI & System Development', attainment: 91.5, target: 85.0 },
    { po: 'PO4: Ethics & Teamwork', attainment: 89.0, target: 85.0 },
  ];

  const [requests, setRequests] = useState<SyllabusChangeRequest[]>([
    {
      id: 'SYL-01',
      courseCode: 'CS401',
      courseName: 'Machine Learning & AI',
      proposedBy: 'Dr. Emily Vance',
      changeDescription: 'Add Transformer Models & Diffusion Architectures to Module 4',
      status: 'Pending',
    },
    {
      id: 'SYL-02',
      courseCode: 'CS301',
      courseName: 'Database Management Systems',
      proposedBy: 'Dr. Sarah Jenkins',
      changeDescription: 'Include Vector Databases & PostgreSQL pgvector lab session',
      status: 'Pending',
    },
  ]);

  const handleApproveSyllabus = (id: string, courseCode: string) => {
    setRequests((prev) =>
      prev.map((r) => (r.id === id ? { ...r, status: 'Approved' } : r))
    );
    showToast(`Approved curriculum update for ${courseCode}`, 'success');
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
            Curriculum & CO-PO Program Outcome Attainment Matrix
          </h3>
          <p style={{ fontSize: '0.78rem', color: '#94a3b8', margin: '2px 0 0 0' }}>
            National Board of Accreditation (NBA) attainment tracking & syllabus revisions
          </p>
        </div>
        <Layers size={20} color="#38bdf8" />
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1rem' }}>
        {/* CO-PO Attainment Progress */}
        <div>
          <div style={{ fontSize: '0.8rem', fontWeight: 600, color: '#cbd5e1', marginBottom: '8px' }}>
            Program Outcome (PO) Attainment (%)
          </div>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
            {coPoAttainment.map((item) => (
              <div key={item.po} style={{ fontSize: '0.78rem' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', color: '#94a3b8', marginBottom: '3px' }}>
                  <span>{item.po}</span>
                  <span style={{ fontWeight: 600, color: item.attainment >= item.target ? '#34d399' : '#f59e0b' }}>
                    {item.attainment}% (Target: {item.target}%)
                  </span>
                </div>
                <div style={{ height: '5px', width: '100%', backgroundColor: 'rgba(255, 255, 255, 0.06)', borderRadius: '3px', overflow: 'hidden' }}>
                  <div style={{ height: '100%', width: `${item.attainment}%`, backgroundColor: '#38bdf8', borderRadius: '3px' }} />
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Pending Syllabus Revision Requests */}
        <div>
          <div style={{ fontSize: '0.8rem', fontWeight: 600, color: '#cbd5e1', marginBottom: '8px' }}>
            Pending Syllabus Revision Approvals
          </div>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
            {requests.map((r) => (
              <div
                key={r.id}
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
                  <span style={{ fontSize: '0.8rem', fontWeight: 700, color: '#38bdf8' }}>
                    {r.courseCode}: {r.courseName}
                  </span>
                  <span style={{ fontSize: '0.72rem', color: '#94a3b8' }}>By {r.proposedBy}</span>
                </div>
                <div style={{ fontSize: '0.75rem', color: '#cbd5e1' }}>"{r.changeDescription}"</div>
                <div style={{ display: 'flex', justifyContent: 'flex-end', marginTop: '4px' }}>
                  {r.status === 'Pending' ? (
                    <button
                      onClick={() => handleApproveSyllabus(r.id, r.courseCode)}
                      style={{
                        backgroundColor: 'rgba(56, 189, 248, 0.15)',
                        border: '1px solid rgba(56, 189, 248, 0.3)',
                        color: '#38bdf8',
                        borderRadius: '4px',
                        padding: '2px 8px',
                        fontSize: '0.7rem',
                        fontWeight: 600,
                        cursor: 'pointer',
                      }}
                    >
                      Approve Revision
                    </button>
                  ) : (
                    <span style={{ color: '#34d399', fontSize: '0.72rem', fontWeight: 600 }}>Approved</span>
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
