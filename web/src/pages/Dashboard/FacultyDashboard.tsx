import React, { useState } from 'react';
import { useAuth } from '../../hooks/useAuth';
import { useToast } from '../../hooks/useToast';
import { Card } from '../../components/Card';
import { DataTable, Column } from '../../components/DataTable';
import { Button } from '../../components/Button';
import { Modal } from '../../components/Modal';
import {
  GraduationCap,
  BookOpen,
  UserCheck,
  Clock,
  CheckCircle,
  RefreshCw,
  QrCode,
  Award,
} from 'lucide-react';

interface ClassSchedule {
  id: string;
  courseCode: string;
  courseTitle: string;
  time: string;
  room: string;
  enrolledStudents: number;
  attendanceStatus: 'Pending' | 'Completed';
}

interface PendingSubmission {
  id: string;
  studentName: string;
  assignmentTitle: string;
  submittedAt: string;
  score: string;
  status: 'Ungraded' | 'Graded';
}

export const FacultyDashboard: React.FC = () => {
  const { user } = useAuth();
  const { showToast } = useToast();

  const [activeTab, setActiveTab] = useState<'overview' | 'attendance' | 'grading' | 'office_hours'>('overview');
  const [isRefreshing, setIsRefreshing] = useState(false);

  // Modals state
  const [isAttendanceModalOpen, setIsAttendanceModalOpen] = useState(false);
  const [isGradeModalOpen, setIsGradeModalOpen] = useState(false);
  const [selectedSubmission, setSelectedSubmission] = useState<PendingSubmission | null>(null);
  const [gradeScore, setGradeScore] = useState('92');

  const [todayClasses] = useState<ClassSchedule[]>([
    { id: 'c-101', courseCode: 'CS-401', courseTitle: 'Advanced Artificial Intelligence', time: '09:00 AM - 10:30 AM', room: 'Hall 302', enrolledStudents: 62, attendanceStatus: 'Completed' },
    { id: 'c-102', courseCode: 'CS-402', courseTitle: 'Distributed Systems Architecture', time: '11:00 AM - 12:30 PM', room: 'Lab 104', enrolledStudents: 54, attendanceStatus: 'Pending' },
    { id: 'c-103', courseCode: 'CS-501', courseTitle: 'Neural Networks Seminar', time: '02:30 PM - 04:00 PM', room: 'Seminar Room B', enrolledStudents: 28, attendanceStatus: 'Pending' },
  ]);

  const [submissions, setSubmissions] = useState<PendingSubmission[]>([
    { id: 'sub-301', studentName: 'Alex Morgan', assignmentTitle: 'Transformer Model Implementation in PyTorch', submittedAt: '2 hours ago', score: 'Pending', status: 'Ungraded' },
    { id: 'sub-302', studentName: 'Rahul Sharma', assignmentTitle: 'Consensus Algorithms (Raft vs Paxos)', submittedAt: 'Yesterday', score: '88/100', status: 'Graded' },
    { id: 'sub-303', studentName: 'Ananya Roy', assignmentTitle: 'Distributed Cache Invalidation Strategies', submittedAt: '2 days ago', score: '95/100', status: 'Graded' },
  ]);

  const handleRefresh = () => {
    setIsRefreshing(true);
    showToast('Syncing real-time lecture & grading metrics...', 'info');
    setTimeout(() => {
      setIsRefreshing(false);
      showToast('Faculty dashboard metrics up to date!', 'success');
    }, 700);
  };

  const handleGradeSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!selectedSubmission) return;

    setSubmissions((prev) =>
      prev.map((s) => (s.id === selectedSubmission.id ? { ...s, score: `${gradeScore}/100`, status: 'Graded' } : s))
    );
    showToast(`Graded submission for ${selectedSubmission.studentName} with score ${gradeScore}/100`, 'success');
    setIsGradeModalOpen(false);
    setSelectedSubmission(null);
  };

  const classColumns: Column<ClassSchedule>[] = [
    { header: 'Course Code', accessorKey: 'courseCode', cell: (r) => <strong style={{ color: '#38bdf8' }}>{r.courseCode}</strong> },
    { header: 'Course Title', accessorKey: 'courseTitle', cell: (r) => <span style={{ color: '#f8fafc', fontWeight: 600 }}>{r.courseTitle}</span> },
    { header: 'Time Slot', accessorKey: 'time' },
    { header: 'Location / Hall', accessorKey: 'room' },
    { header: 'Enrolled', accessorKey: 'enrolledStudents', cell: (r) => <strong>{r.enrolledStudents} Students</strong> },
    {
      header: 'Attendance',
      accessorKey: 'attendanceStatus',
      cell: (r) => (
        <span
          style={{
            padding: '2px 10px',
            borderRadius: '12px',
            fontSize: '0.75rem',
            fontWeight: 700,
            background: r.attendanceStatus === 'Completed' ? 'rgba(16,185,129,0.2)' : 'rgba(245,158,11,0.2)',
            color: r.attendanceStatus === 'Completed' ? '#34d399' : '#f59e0b',
          }}
        >
          {r.attendanceStatus}
        </span>
      ),
    },
  ];

  const submissionColumns: Column<PendingSubmission>[] = [
    { header: 'Student Name', accessorKey: 'studentName', cell: (r) => <strong style={{ color: '#f8fafc' }}>{r.studentName}</strong> },
    { header: 'Assignment Title', accessorKey: 'assignmentTitle' },
    { header: 'Submitted', accessorKey: 'submittedAt', cell: (r) => <span style={{ color: '#94a3b8', fontSize: '0.8rem' }}>{r.submittedAt}</span> },
    { header: 'Score', accessorKey: 'score', cell: (r) => <strong style={{ color: r.status === 'Graded' ? '#34d399' : '#f59e0b' }}>{r.score}</strong> },
  ];

  return (
    <div style={{ padding: '1.75rem', display: 'flex', flexDirection: 'column', gap: '1.5rem', maxWidth: '1600px', margin: '0 auto' }}>
      {/* Header Banner */}
      <div
        style={{
          background: 'linear-gradient(135deg, rgba(30, 41, 59, 0.95), rgba(15, 23, 42, 0.98))',
          backdropFilter: 'blur(16px)',
          border: '1px solid rgba(56, 189, 248, 0.3)',
          borderRadius: '20px',
          padding: '1.75rem',
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          flexWrap: 'wrap',
          gap: '1.25rem',
          boxShadow: '0 8px 32px rgba(0, 0, 0, 0.35)',
        }}
      >
        <div style={{ display: 'flex', alignItems: 'center', gap: '1.25rem' }}>
          <div
            style={{
              width: '62px',
              height: '62px',
              borderRadius: '16px',
              background: 'linear-gradient(135deg, #2563eb, #1d4ed8)',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              color: '#ffffff',
              boxShadow: '0 4px 20px rgba(37, 99, 235, 0.4)',
            }}
          >
            <GraduationCap size={32} />
          </div>
          <div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
              <h1 style={{ margin: 0, fontSize: '1.6rem', fontWeight: 800, color: '#f8fafc', letterSpacing: '-0.5px' }}>
                Faculty Academic Portal & Grading Desk
              </h1>
            </div>
            <p style={{ margin: '4px 0 0 0', fontSize: '0.88rem', color: '#94a3b8' }}>
              Welcome, <strong>{user?.full_name || 'Dr. Sarah Jenkins'}</strong> &bull; Dept of Computer Science & Engineering (Senior Professor)
            </p>
          </div>
        </div>

        <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
          <Button variant="primary" icon={<QrCode size={16} />} onClick={() => setIsAttendanceModalOpen(true)}>
            QR Attendance Scanner
          </Button>
          <button
            onClick={handleRefresh}
            title="Refresh Metrics"
            style={{ padding: '9px 12px', borderRadius: '10px', border: '1px solid rgba(255, 255, 255, 0.1)', background: 'rgba(255, 255, 255, 0.05)', color: '#38bdf8', cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center' }}
          >
            <RefreshCw size={16} className={isRefreshing ? 'animate-spin' : ''} />
          </button>
        </div>
      </div>

      {/* Navigation Tabs */}
      <div style={{ display: 'flex', gap: '8px', borderBottom: '1px solid rgba(255, 255, 255, 0.08)', paddingBottom: '8px' }}>
        {[
          { id: 'overview', label: 'Teaching Overview', icon: <BookOpen size={16} /> },
          { id: 'attendance', label: 'Class Attendance Desk', icon: <UserCheck size={16} /> },
          { id: 'grading', label: 'Assignment Grading Queue', icon: <Award size={16} /> },
          { id: 'office_hours', label: 'Office Hours & Advisory', icon: <Clock size={16} /> },
        ].map((tab) => (
          <button
            key={tab.id}
            onClick={() => setActiveTab(tab.id as any)}
            style={{
              display: 'flex',
              alignItems: 'center',
              gap: '8px',
              padding: '10px 18px',
              borderRadius: '10px',
              border: activeTab === tab.id ? '1px solid rgba(56, 189, 248, 0.4)' : '1px solid transparent',
              background: activeTab === tab.id ? 'rgba(37, 99, 235, 0.2)' : 'transparent',
              color: activeTab === tab.id ? '#38bdf8' : '#94a3b8',
              fontWeight: 600,
              fontSize: '0.875rem',
              cursor: 'pointer',
            }}
          >
            {tab.icon}
            <span>{tab.label}</span>
          </button>
        ))}
      </div>

      {/* Tab 1: Overview */}
      {activeTab === 'overview' && (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(260px, 1fr))', gap: '1.25rem' }}>
            {[
              { title: 'Active Teaching Courses', value: '3 Courses', sub: '144 Enrolled Students Total', icon: <BookOpen size={22} color="#38bdf8" />, bg: 'rgba(56,189,248,0.1)' },
              { title: 'Average Attendance Rate', value: '94.2%', sub: 'High student engagement', icon: <UserCheck size={22} color="#34d399" />, bg: 'rgba(52,211,153,0.1)' },
              { title: 'Pending Submissions', value: '1 Ungraded', sub: '2 graded today', icon: <Award size={22} color="#f59e0b" />, bg: 'rgba(245,158,11,0.1)' },
              { title: 'Office Hours Booked', value: '4 Meetings', sub: 'Scheduled for this afternoon', icon: <Clock size={22} color="#c084fc" />, bg: 'rgba(192,132,252,0.1)' },
            ].map((stat, i) => (
              <div key={i} style={{ backgroundColor: 'rgba(30, 41, 59, 0.7)', backdropFilter: 'blur(16px)', border: '1px solid rgba(255, 255, 255, 0.08)', borderRadius: '16px', padding: '1.25rem', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                <div>
                  <div style={{ fontSize: '0.78rem', color: '#94a3b8', textTransform: 'uppercase', fontWeight: 600 }}>{stat.title}</div>
                  <div style={{ fontSize: '1.75rem', fontWeight: 800, color: '#f8fafc', marginTop: '4px' }}>{stat.value}</div>
                  <div style={{ fontSize: '0.72rem', color: '#64748b', marginTop: '4px' }}>{stat.sub}</div>
                </div>
                <div style={{ width: '48px', height: '48px', borderRadius: '12px', background: stat.bg, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
                  {stat.icon}
                </div>
              </div>
            ))}
          </div>

          <Card title="Today's Lecture Schedule">
            <DataTable columns={classColumns} data={todayClasses} />
          </Card>
        </div>
      )}

      {/* Tab 2: Class Attendance */}
      {activeTab === 'attendance' && (
        <Card title="Digital Attendance Management">
          <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '1rem', alignItems: 'center' }}>
            <span style={{ fontSize: '0.88rem', color: '#cbd5e1' }}>Select a class session to launch live QR attendance code or roll call sheet.</span>
            <Button variant="primary" icon={<QrCode size={16} />} onClick={() => setIsAttendanceModalOpen(true)}>
              Generate Dynamic Attendance QR
            </Button>
          </div>
          <DataTable columns={classColumns} data={todayClasses} />
        </Card>
      )}

      {/* Tab 3: Assignment Grading Queue */}
      {activeTab === 'grading' && (
        <Card title="Assignment Submission Grading Queue">
          <DataTable
            columns={submissionColumns}
            data={submissions}
            actions={(row) => (
              <Button
                variant="primary"
                size="sm"
                onClick={() => {
                  setSelectedSubmission(row);
                  setIsGradeModalOpen(true);
                }}
              >
                {row.status === 'Graded' ? 'Edit Grade' : 'Grade Submission'}
              </Button>
            )}
          />
        </Card>
      )}

      {/* Tab 4: Office Hours & Advisory */}
      {activeTab === 'office_hours' && (
        <Card title="Faculty Office Hours & Student Advising">
          <div style={{ padding: '1rem', background: 'rgba(15,23,42,0.6)', borderRadius: '12px', border: '1px solid rgba(255,255,255,0.08)' }}>
            <div style={{ fontWeight: 700, color: '#38bdf8', marginBottom: '8px' }}>Upcoming Office Appointments (Today 3:00 PM - 5:00 PM)</div>
            <ul style={{ color: '#cbd5e1', fontSize: '0.85rem', paddingLeft: '1.2rem', margin: 0 }}>
              <li>3:00 PM - Alex Morgan (Topic: Final Thesis Project Review)</li>
              <li>3:30 PM - Ananya Roy (Topic: Distributed Systems Exam Guidance)</li>
            </ul>
          </div>
        </Card>
      )}

      {/* QR Code Modal */}
      <Modal isOpen={isAttendanceModalOpen} onClose={() => setIsAttendanceModalOpen(false)} title="Live QR Attendance Code - CS-402">
        <div style={{ textAlign: 'center', display: 'flex', flexDirection: 'column', gap: '1rem', alignItems: 'center' }}>
          <div style={{ padding: '1.25rem', background: '#ffffff', borderRadius: '16px', width: 'fit-content' }}>
            <QrCode size={160} style={{ color: '#0f172a' }} />
          </div>
          <div style={{ fontSize: '0.85rem', color: '#cbd5e1' }}>Students scan via UniSphere Mobile App to confirm presence.</div>
          <Button variant="primary" onClick={() => setIsAttendanceModalOpen(false)}>Close Session</Button>
        </div>
      </Modal>

      {/* Grade Submission Modal */}
      <Modal isOpen={isGradeModalOpen} onClose={() => setIsGradeModalOpen(false)} title="Grade Student Submission">
        {selectedSubmission && (
          <form onSubmit={handleGradeSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
            <div>
              <div style={{ fontSize: '0.85rem', color: '#94a3b8' }}>Student: <strong style={{ color: '#f8fafc' }}>{selectedSubmission.studentName}</strong></div>
              <div style={{ fontSize: '0.85rem', color: '#94a3b8', marginTop: '2px' }}>Assignment: <strong style={{ color: '#38bdf8' }}>{selectedSubmission.assignmentTitle}</strong></div>
            </div>
            <div>
              <label style={{ display: 'block', fontSize: '0.8rem', color: '#cbd5e1', marginBottom: '4px' }}>Assign Score (Out of 100)</label>
              <input type="number" min="0" max="100" value={gradeScore} onChange={(e) => setGradeScore(e.target.value)} required style={{ width: '100%', padding: '8px 12px', borderRadius: '8px', background: 'rgba(15,23,42,0.8)', border: '1px solid rgba(255,255,255,0.15)', color: '#f8fafc' }} />
            </div>
            <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '8px' }}>
              <Button variant="outline" onClick={() => setIsGradeModalOpen(false)}>Cancel</Button>
              <Button variant="primary" icon={<CheckCircle size={16} />}>Submit Grade</Button>
            </div>
          </form>
        )}
      </Modal>
    </div>
  );
};

export default FacultyDashboard;
