import React, { useState } from 'react';
import { Calendar, UserCheck, CheckCircle2, XCircle } from 'lucide-react';
import { useToast } from '../../hooks/useToast';

interface LeaveRequest {
  id: string;
  facultyName: string;
  courseAffected: string;
  date: string;
  reason: string;
  substituteAssigned: string;
  status: 'Pending' | 'Approved' | 'Rejected';
}

export const FacultyLeaveManager: React.FC = () => {
  const { showToast } = useToast();
  const [requests, setRequests] = useState<LeaveRequest[]>([
    {
      id: 'LR-101',
      facultyName: 'Dr. Sarah Jenkins',
      courseAffected: 'CS301 Database Systems',
      date: 'Sept 12 - Sept 14, 2026',
      reason: 'Attending IEEE International Data Conference',
      substituteAssigned: 'Dr. Grace Hopper',
      status: 'Pending',
    },
    {
      id: 'LR-102',
      facultyName: 'Prof. Alan Turing',
      courseAffected: 'CS302 Operating Systems',
      date: 'Sept 15, 2026',
      reason: 'Medical Leave',
      substituteAssigned: 'Unassigned',
      status: 'Pending',
    },
    {
      id: 'LR-103',
      facultyName: 'Prof. Michael Scott',
      courseAffected: 'CS402 Distributed Systems',
      date: 'Sept 08, 2026',
      reason: 'Personal Leave',
      substituteAssigned: 'Dr. Emily Vance',
      status: 'Approved',
    },
  ]);

  const handleApprove = (id: string, name: string) => {
    setRequests((prev) =>
      prev.map((req) => (req.id === id ? { ...req, status: 'Approved' } : req))
    );
    showToast(`Approved leave request for ${name} & notified substitute faculty`, 'success');
  };

  const handleReject = (id: string, name: string) => {
    setRequests((prev) =>
      prev.map((req) => (req.id === id ? { ...req, status: 'Rejected' } : req))
    );
    showToast(`Rejected leave request for ${name}`, 'info');
  };

  const handleAssignSubstitute = (id: string) => {
    const availableFaculty = ['Dr. Grace Hopper', 'Dr. Emily Vance', 'Prof. David Miller'];
    const chosen = availableFaculty[Math.floor(Math.random() * availableFaculty.length)];
    setRequests((prev) =>
      prev.map((req) => (req.id === id ? { ...req, substituteAssigned: chosen } : req))
    );
    showToast(`Assigned ${chosen} as substitute instructor`, 'info');
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
            Faculty Leave & Class Substitution Manager
          </h3>
          <p style={{ fontSize: '0.78rem', color: '#94a3b8', margin: '2px 0 0 0' }}>
            Review leave requests and ensure 100% lecture coverage with substitute teachers
          </p>
        </div>
        <UserCheck size={20} color="#a855f7" />
      </div>

      <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
        {requests.map((req) => (
          <div
            key={req.id}
            style={{
              backgroundColor: 'rgba(15, 23, 42, 0.5)',
              border: '1px solid rgba(255, 255, 255, 0.05)',
              borderRadius: '12px',
              padding: '12px 14px',
              display: 'flex',
              flexDirection: 'column',
              gap: '8px',
            }}
          >
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '8px' }}>
              <div>
                <span style={{ fontSize: '0.9rem', fontWeight: 700, color: '#f1f5f9' }}>{req.facultyName}</span>
                <span style={{ fontSize: '0.78rem', color: '#94a3b8', marginLeft: '8px' }}>({req.courseAffected})</span>
              </div>
              <span
                style={{
                  padding: '2px 8px',
                  borderRadius: '6px',
                  fontSize: '0.72rem',
                  fontWeight: 700,
                  backgroundColor:
                    req.status === 'Approved'
                      ? 'rgba(52, 211, 153, 0.15)'
                      : req.status === 'Rejected'
                      ? 'rgba(244, 63, 94, 0.15)'
                      : 'rgba(245, 158, 11, 0.15)',
                  color:
                    req.status === 'Approved'
                      ? '#34d399'
                      : req.status === 'Rejected'
                      ? '#f43f5e'
                      : '#f59e0b',
                }}
              >
                {req.status}
              </span>
            </div>

            <div style={{ fontSize: '0.78rem', color: '#cbd5e1', display: 'flex', gap: '16px', flexWrap: 'wrap' }}>
              <span style={{ display: 'inline-flex', alignItems: 'center', gap: '4px', color: '#94a3b8' }}>
                <Calendar size={13} /> {req.date}
              </span>
              <span>Reason: "{req.reason}"</span>
            </div>

            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', paddingTop: '4px', borderTop: '1px solid rgba(255,255,255,0.04)' }}>
              <div style={{ fontSize: '0.75rem', color: '#94a3b8' }}>
                Substitute Assigned:{' '}
                <strong style={{ color: req.substituteAssigned === 'Unassigned' ? '#f43f5e' : '#38bdf8' }}>
                  {req.substituteAssigned}
                </strong>
                {req.substituteAssigned === 'Unassigned' && (
                  <button
                    onClick={() => handleAssignSubstitute(req.id)}
                    style={{
                      marginLeft: '8px',
                      backgroundColor: 'rgba(56, 189, 248, 0.15)',
                      border: '1px solid rgba(56, 189, 248, 0.3)',
                      color: '#38bdf8',
                      borderRadius: '4px',
                      padding: '2px 6px',
                      fontSize: '0.7rem',
                      cursor: 'pointer',
                    }}
                  >
                    Assign Now
                  </button>
                )}
              </div>

              {req.status === 'Pending' && (
                <div style={{ display: 'flex', gap: '8px' }}>
                  <button
                    onClick={() => handleReject(req.id, req.facultyName)}
                    style={{
                      backgroundColor: 'rgba(244, 63, 94, 0.15)',
                      border: '1px solid rgba(244, 63, 94, 0.3)',
                      color: '#f43f5e',
                      borderRadius: '6px',
                      padding: '4px 10px',
                      fontSize: '0.72rem',
                      fontWeight: 600,
                      cursor: 'pointer',
                      display: 'flex',
                      alignItems: 'center',
                      gap: '4px',
                    }}
                  >
                    <XCircle size={13} /> Reject
                  </button>
                  <button
                    onClick={() => handleApprove(req.id, req.facultyName)}
                    style={{
                      backgroundColor: 'rgba(52, 211, 153, 0.15)',
                      border: '1px solid rgba(52, 211, 153, 0.3)',
                      color: '#34d399',
                      borderRadius: '6px',
                      padding: '4px 10px',
                      fontSize: '0.72rem',
                      fontWeight: 600,
                      cursor: 'pointer',
                      display: 'flex',
                      alignItems: 'center',
                      gap: '4px',
                    }}
                  >
                    <CheckCircle2 size={13} /> Approve
                  </button>
                </div>
              )}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
