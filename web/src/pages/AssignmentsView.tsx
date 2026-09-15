import React, { useState } from 'react';
import { User } from '../types/auth';

interface AssignmentsViewProps {
  user?: User | null;
  isFaculty?: boolean;
}

interface AssignmentItem {
  id: string;
  code: string;
  title: string;
  due: string;
  points: number;
  grade?: string;
  status: 'Pending' | 'Completed';
  submissionsCount?: number;
  totalStudents?: number;
}

interface StudentSubmission {
  id: string;
  assignmentId: string;
  studentName: string;
  rollNo: string;
  submittedAt: string;
  file: string;
  score: number | null;
  maxScore: number;
  feedback: string;
  status: 'Graded' | 'Pending Review';
}

export const AssignmentsView: React.FC<AssignmentsViewProps> = ({ user, isFaculty = false }) => {
  const facultyMode = isFaculty || user?.role === 'faculty';

  // --- STUDENT MODE STATE ---
  const [studentTab, setStudentTab] = useState<'pending' | 'completed'>('pending');
  const [submittedIds, setSubmittedIds] = useState<string[]>([]);

  // Initial student assignments
  const [studentAssignments] = useState<AssignmentItem[]>([
    {
      id: 'a1',
      code: 'CS-401',
      title: 'Transformer Architecture Implementation',
      due: 'Sep 18, 2026',
      points: 100,
      status: 'Pending',
    },
    {
      id: 'a2',
      code: 'DS-310',
      title: 'MapReduce Distributed Log Analyzer',
      due: 'Sep 22, 2026',
      points: 100,
      status: 'Pending',
    },
    {
      id: 'a3',
      code: 'MATH-250',
      title: 'Lagrangian Dual Problem Set',
      due: 'Sep 05, 2026',
      points: 50,
      grade: '48/50',
      status: 'Completed',
    },
    {
      id: 'a4',
      code: 'ETH-102',
      title: 'Algorithmic Fairness Case Study',
      due: 'Aug 29, 2026',
      points: 50,
      grade: '46/50',
      status: 'Completed',
    },
  ]);

  // --- FACULTY MODE STATE ---
  const [facultyTab, setFacultyTab] = useState<'grading' | 'assignments'>('grading');
  const [showCreateModal, setShowCreateModal] = useState(false);

  // New assignment form state
  const [newTitle, setNewTitle] = useState('');
  const [newCode, setNewCode] = useState('CS-401');
  const [newDue, setNewDue] = useState('Sep 28, 2026');
  const [newPoints, setNewPoints] = useState(100);

  // Faculty assignments list
  const [facultyAssignments, setFacultyAssignments] = useState<AssignmentItem[]>([
    {
      id: 'fa-1',
      code: 'CS-401',
      title: 'Transformer Architecture Implementation',
      due: 'Sep 18, 2026',
      points: 100,
      status: 'Pending',
      submissionsCount: 28,
      totalStudents: 32,
    },
    {
      id: 'fa-2',
      code: 'CS-401',
      title: 'Attention Mechanism & Multi-Head Self Attention',
      due: 'Oct 02, 2026',
      points: 80,
      status: 'Pending',
      submissionsCount: 4,
      totalStudents: 32,
    },
    {
      id: 'fa-3',
      code: 'AI-480',
      title: 'Visual SLAM & LiDAR Odometry Pipeline',
      due: 'Sep 10, 2026',
      points: 100,
      status: 'Completed',
      submissionsCount: 26,
      totalStudents: 26,
    },
  ]);

  // Student submissions to grade
  const [submissions, setSubmissions] = useState<StudentSubmission[]>([
    {
      id: 'sub-1',
      assignmentId: 'fa-1',
      studentName: 'Alex Rivera',
      rollNo: 'CS-2023-889',
      submittedAt: 'Today at 08:30 AM',
      file: 'transformer_attention_impl.py',
      score: null,
      maxScore: 100,
      feedback: '',
      status: 'Pending Review',
    },
    {
      id: 'sub-2',
      assignmentId: 'fa-1',
      studentName: 'Elena Rostova',
      rollNo: 'CS-2023-901',
      submittedAt: 'Yesterday at 11:15 PM',
      file: 'model_weights_eval.ipynb',
      score: 96,
      maxScore: 100,
      feedback: 'Excellent clean PyTorch modular structure and tensor dimension checks.',
      status: 'Graded',
    },
    {
      id: 'sub-3',
      assignmentId: 'fa-1',
      studentName: 'Marcus Chen',
      rollNo: 'CS-2023-912',
      submittedAt: 'Sep 11 at 04:45 PM',
      file: 'chen_m_transformer.zip',
      score: null,
      maxScore: 100,
      feedback: '',
      status: 'Pending Review',
    },
    {
      id: 'sub-4',
      assignmentId: 'fa-1',
      studentName: 'Sarah Jenkins',
      rollNo: 'CS-2023-924',
      submittedAt: 'Sep 10 at 09:20 PM',
      file: 'pos_encoding_benchmark.py',
      score: 92,
      maxScore: 100,
      feedback: 'Good implementation of sinusoidal positional encodings.',
      status: 'Graded',
    },
  ]);

  const [activeGradingSubId, setActiveGradingSubId] = useState<string | null>(null);
  const [tempScore, setTempScore] = useState<string>('');
  const [tempFeedback, setTempFeedback] = useState<string>('');

  const handleOpenGradeDrawer = (sub: StudentSubmission) => {
    setActiveGradingSubId(sub.id);
    setTempScore(sub.score !== null ? sub.score.toString() : '');
    setTempFeedback(sub.feedback || '');
  };

  const handleSaveGrade = (subId: string) => {
    const numScore = parseFloat(tempScore);
    setSubmissions((prev) =>
      prev.map((s) =>
        s.id === subId
          ? {
              ...s,
              score: isNaN(numScore) ? s.score : numScore,
              feedback: tempFeedback,
              status: 'Graded',
            }
          : s
      )
    );
    setActiveGradingSubId(null);
  };

  const handleCreateAssignment = (e: React.FormEvent) => {
    e.preventDefault();
    if (!newTitle.trim()) return;

    const created: AssignmentItem = {
      id: `fa-${Date.now()}`,
      code: newCode,
      title: newTitle.trim(),
      due: newDue,
      points: Number(newPoints) || 100,
      status: 'Pending',
      submissionsCount: 0,
      totalStudents: 32,
    };

    setFacultyAssignments([created, ...facultyAssignments]);
    setNewTitle('');
    setShowCreateModal(false);
  };

  // Student upload action
  const handleStudentSubmit = (id: string) => {
    setSubmittedIds((prev) => [...prev, id]);
  };

  // --- RENDER FACULTY VIEW ---
  if (facultyMode) {
    const pendingReviewCount = submissions.filter((s) => s.status === 'Pending Review').length;

    return (
      <div style={{ padding: '1.25rem', display: 'flex', flexDirection: 'column', gap: '14px' }}>
        {/* Faculty Header */}
        <div
          style={{
            background: 'linear-gradient(135deg, #312e81, #6366f1)',
            padding: '1.25rem',
            borderRadius: '16px',
            color: '#fff',
            boxShadow: '0 4px 16px rgba(99, 102, 241, 0.25)',
            display: 'flex',
            justifyContent: 'space-between',
            alignItems: 'center',
          }}
        >
          <div>
            <div style={{ fontSize: '0.75rem', opacity: 0.9, fontWeight: 600 }}>
              Faculty Assignment Hub
            </div>
            <div style={{ fontSize: '1.25rem', fontWeight: 800, marginTop: '2px' }}>
              Submissions & Grading
            </div>
            <div style={{ fontSize: '0.72rem', opacity: 0.85, marginTop: '2px' }}>
              {pendingReviewCount} student submissions awaiting your evaluation
            </div>
          </div>
          <button
            onClick={() => setShowCreateModal(true)}
            style={{
              background: 'rgba(255, 255, 255, 0.2)',
              border: '1px solid rgba(255, 255, 255, 0.35)',
              color: '#fff',
              borderRadius: '10px',
              padding: '6px 12px',
              fontSize: '0.75rem',
              fontWeight: 700,
              cursor: 'pointer',
              whiteSpace: 'nowrap',
            }}
          >
            + Create
          </button>
        </div>

        {/* Modal: Create Assignment */}
        {showCreateModal && (
          <div
            style={{
              background: 'rgba(15, 23, 42, 0.95)',
              border: '1px solid rgba(99, 102, 241, 0.4)',
              borderRadius: '14px',
              padding: '1rem',
              boxShadow: '0 8px 32px rgba(0, 0, 0, 0.4)',
            }}
          >
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '10px' }}>
              <div style={{ fontSize: '0.9rem', fontWeight: 800, color: '#f8fafc' }}>
                New Course Assignment
              </div>
              <button
                onClick={() => setShowCreateModal(false)}
                style={{ background: 'none', border: 'none', color: '#94a3b8', fontSize: '1rem', cursor: 'pointer' }}
              >
                ✕
              </button>
            </div>
            <form onSubmit={handleCreateAssignment} style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
              <div>
                <label style={{ fontSize: '0.7rem', color: '#94a3b8' }}>Title</label>
                <input
                  type="text"
                  placeholder="e.g. Diffusion Models & Latent Spaces"
                  value={newTitle}
                  onChange={(e) => setNewTitle(e.target.value)}
                  style={{
                    width: '100%',
                    padding: '6px 8px',
                    borderRadius: '8px',
                    border: '1px solid rgba(255, 255, 255, 0.15)',
                    background: 'rgba(30, 41, 59, 0.8)',
                    color: '#fff',
                    fontSize: '0.8rem',
                  }}
                  required
                />
              </div>
              <div style={{ display: 'flex', gap: '8px' }}>
                <div style={{ flex: 1 }}>
                  <label style={{ fontSize: '0.7rem', color: '#94a3b8' }}>Course Code</label>
                  <select
                    value={newCode}
                    onChange={(e) => setNewCode(e.target.value)}
                    style={{
                      width: '100%',
                      padding: '6px 8px',
                      borderRadius: '8px',
                      border: '1px solid rgba(255, 255, 255, 0.15)',
                      background: 'rgba(30, 41, 59, 0.8)',
                      color: '#fff',
                      fontSize: '0.8rem',
                    }}
                  >
                    <option value="CS-401">CS-401</option>
                    <option value="AI-480">AI-480</option>
                    <option value="DS-310">DS-310</option>
                  </select>
                </div>
                <div style={{ flex: 1 }}>
                  <label style={{ fontSize: '0.7rem', color: '#94a3b8' }}>Max Points</label>
                  <input
                    type="number"
                    value={newPoints}
                    onChange={(e) => setNewPoints(Number(e.target.value))}
                    style={{
                      width: '100%',
                      padding: '6px 8px',
                      borderRadius: '8px',
                      border: '1px solid rgba(255, 255, 255, 0.15)',
                      background: 'rgba(30, 41, 59, 0.8)',
                      color: '#fff',
                      fontSize: '0.8rem',
                    }}
                  />
                </div>
              </div>
              <div>
                <label style={{ fontSize: '0.7rem', color: '#94a3b8' }}>Due Date</label>
                <input
                  type="text"
                  placeholder="e.g. Oct 15, 2026"
                  value={newDue}
                  onChange={(e) => setNewDue(e.target.value)}
                  style={{
                    width: '100%',
                    padding: '6px 8px',
                    borderRadius: '8px',
                    border: '1px solid rgba(255, 255, 255, 0.15)',
                    background: 'rgba(30, 41, 59, 0.8)',
                    color: '#fff',
                    fontSize: '0.8rem',
                  }}
                />
              </div>
              <button
                type="submit"
                className="btn btn-primary"
                style={{ marginTop: '6px', padding: '8px', fontSize: '0.8rem', background: '#6366f1' }}
              >
                Publish Assignment
              </button>
            </form>
          </div>
        )}

        {/* Tab Switcher */}
        <div style={{ display: 'flex', gap: '8px' }}>
          <button
            onClick={() => setFacultyTab('grading')}
            className={`btn ${facultyTab === 'grading' ? 'btn-primary' : 'btn-secondary'}`}
            style={{ flex: 1, padding: '8px', fontSize: '0.825rem' }}
          >
            Submissions ({submissions.length})
          </button>
          <button
            onClick={() => setFacultyTab('assignments')}
            className={`btn ${facultyTab === 'assignments' ? 'btn-primary' : 'btn-secondary'}`}
            style={{ flex: 1, padding: '8px', fontSize: '0.825rem' }}
          >
            Active Tasks ({facultyAssignments.length})
          </button>
        </div>

        {/* 1. Grading Tab */}
        {facultyTab === 'grading' && (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
            {submissions.map((sub) => {
              const isGraded = sub.status === 'Graded';
              const isEditing = activeGradingSubId === sub.id;

              return (
                <div key={sub.id} className="glass-panel" style={{ padding: '1rem' }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
                    <div>
                      <div style={{ fontSize: '0.9rem', fontWeight: 800, color: '#f8fafc' }}>
                        {sub.studentName}
                      </div>
                      <div style={{ fontSize: '0.72rem', color: '#94a3b8' }}>
                        {sub.rollNo} • {sub.submittedAt}
                      </div>
                    </div>
                    <span
                      style={{
                        fontSize: '0.7rem',
                        fontWeight: 700,
                        padding: '2px 8px',
                        borderRadius: '8px',
                        color: isGraded ? '#10b981' : '#f59e0b',
                        background: isGraded ? 'rgba(16, 185, 129, 0.15)' : 'rgba(245, 158, 11, 0.15)',
                      }}
                    >
                      {isGraded ? `${sub.score}/${sub.maxScore} pts` : 'Pending'}
                    </span>
                  </div>

                  {/* Submission artifact file */}
                  <div
                    style={{
                      background: 'rgba(255, 255, 255, 0.05)',
                      padding: '6px 10px',
                      borderRadius: '8px',
                      marginTop: '8px',
                      fontSize: '0.75rem',
                      display: 'flex',
                      alignItems: 'center',
                      gap: '6px',
                      color: '#38bdf8',
                    }}
                  >
                    <span>📎</span>
                    <span style={{ fontFamily: 'monospace' }}>{sub.file}</span>
                  </div>

                  {/* Feedback display if graded */}
                  {isGraded && sub.feedback && !isEditing && (
                    <div
                      style={{
                        fontSize: '0.74rem',
                        color: '#cbd5e1',
                        marginTop: '8px',
                        padding: '6px 10px',
                        background: 'rgba(16, 185, 129, 0.08)',
                        borderRadius: '6px',
                        borderLeft: '2px solid #10b981',
                      }}
                    >
                      <strong>Feedback:</strong> {sub.feedback}
                    </div>
                  )}

                  {/* Grading Controls */}
                  {isEditing ? (
                    <div style={{ marginTop: '10px', display: 'flex', flexDirection: 'column', gap: '6px' }}>
                      <div style={{ display: 'flex', gap: '8px', alignItems: 'center' }}>
                        <label style={{ fontSize: '0.75rem', color: '#94a3b8' }}>Score:</label>
                        <input
                          type="number"
                          value={tempScore}
                          onChange={(e) => setTempScore(e.target.value)}
                          placeholder="e.g. 95"
                          style={{
                            width: '80px',
                            padding: '4px 8px',
                            borderRadius: '6px',
                            border: '1px solid rgba(255,255,255,0.2)',
                            background: 'rgba(30, 41, 59, 0.8)',
                            color: '#fff',
                            fontSize: '0.8rem',
                          }}
                        />
                        <span style={{ fontSize: '0.75rem', color: '#94a3b8' }}>/ {sub.maxScore}</span>
                      </div>
                      <textarea
                        value={tempFeedback}
                        onChange={(e) => setTempFeedback(e.target.value)}
                        placeholder="Add constructive comments & feedback..."
                        rows={2}
                        style={{
                          width: '100%',
                          padding: '6px 8px',
                          borderRadius: '6px',
                          border: '1px solid rgba(255,255,255,0.2)',
                          background: 'rgba(30, 41, 59, 0.8)',
                          color: '#fff',
                          fontSize: '0.75rem',
                          resize: 'none',
                        }}
                      />
                      <div style={{ display: 'flex', gap: '6px', marginTop: '2px' }}>
                        <button
                          onClick={() => handleSaveGrade(sub.id)}
                          className="btn btn-primary"
                          style={{ flex: 1, padding: '6px', fontSize: '0.75rem' }}
                        >
                          Save Grade ✓
                        </button>
                        <button
                          onClick={() => setActiveGradingSubId(null)}
                          className="btn btn-secondary"
                          style={{ padding: '6px 10px', fontSize: '0.75rem' }}
                        >
                          Cancel
                        </button>
                      </div>
                    </div>
                  ) : (
                    <button
                      onClick={() => handleOpenGradeDrawer(sub)}
                      style={{
                        marginTop: '8px',
                        background: 'rgba(99, 102, 241, 0.15)',
                        border: '1px solid rgba(99, 102, 241, 0.3)',
                        color: '#a5b4fc',
                        borderRadius: '8px',
                        padding: '6px 10px',
                        fontSize: '0.75rem',
                        fontWeight: 700,
                        cursor: 'pointer',
                        width: '100%',
                      }}
                    >
                      {isGraded ? '✎ Edit Grade & Feedback' : '📝 Grade Submission'}
                    </button>
                  )}
                </div>
              );
            })}
          </div>
        )}

        {/* 2. Faculty Assignments List Tab */}
        {facultyTab === 'assignments' && (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
            {facultyAssignments.map((item) => (
              <div key={item.id} className="glass-panel" style={{ padding: '1rem' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                  <span style={{ fontSize: '0.75rem', fontWeight: 700, color: '#38bdf8' }}>{item.code}</span>
                  <span
                    style={{
                      fontSize: '0.7rem',
                      fontWeight: 700,
                      color: '#4ade80',
                      backgroundColor: 'rgba(74, 222, 128, 0.15)',
                      padding: '2px 8px',
                      borderRadius: '8px',
                    }}
                  >
                    Active
                  </span>
                </div>
                <div style={{ fontSize: '0.95rem', fontWeight: 700, color: '#f8fafc', marginTop: '6px' }}>
                  {item.title}
                </div>
                <div style={{ fontSize: '0.75rem', color: '#94a3b8', marginTop: '4px' }}>
                  Due: {item.due} • {item.points} Points Max
                </div>
                <div
                  style={{
                    display: 'flex',
                    justifyContent: 'space-between',
                    marginTop: '8px',
                    fontSize: '0.72rem',
                    color: '#cbd5e1',
                    background: 'rgba(255,255,255,0.05)',
                    padding: '6px 10px',
                    borderRadius: '6px',
                  }}
                >
                  <span>Submissions:</span>
                  <strong>{item.submissionsCount} / {item.totalStudents} Turn-ins</strong>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    );
  }

  // --- RENDER STUDENT VIEW (Default) ---
  const filtered = studentAssignments.filter((a) => {
    const isSubmitted = submittedIds.includes(a.id);
    if (isSubmitted) return studentTab === 'completed';
    return studentTab === 'pending' ? a.status === 'Pending' : a.status === 'Completed';
  });

  return (
    <div style={{ padding: '1.25rem' }}>
      <div style={{ display: 'flex', gap: '8px', marginBottom: '1rem' }}>
        <button
          onClick={() => setStudentTab('pending')}
          className={`btn ${studentTab === 'pending' ? 'btn-primary' : 'btn-secondary'}`}
          style={{ flex: 1, padding: '8px', fontSize: '0.825rem' }}
        >
          Pending
        </button>
        <button
          onClick={() => setStudentTab('completed')}
          className={`btn ${studentTab === 'completed' ? 'btn-primary' : 'btn-secondary'}`}
          style={{ flex: 1, padding: '8px', fontSize: '0.825rem' }}
        >
          Completed
        </button>
      </div>

      <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
        {filtered.map((item) => {
          const isSubmitted = submittedIds.includes(item.id);
          return (
            <div key={item.id} className="glass-panel" style={{ padding: '1rem' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                <span style={{ fontSize: '0.75rem', fontWeight: 700, color: '#38bdf8' }}>{item.code}</span>
                <span
                  style={{
                    fontSize: '0.7rem',
                    fontWeight: 700,
                    color: item.status === 'Pending' && !isSubmitted ? '#f59e0b' : '#10b981',
                    backgroundColor:
                      item.status === 'Pending' && !isSubmitted
                        ? 'rgba(245, 158, 11, 0.15)'
                        : 'rgba(16, 185, 129, 0.15)',
                    padding: '2px 8px',
                    borderRadius: '8px',
                  }}
                >
                  {isSubmitted ? 'Submitted' : item.grade ? `Grade: ${item.grade}` : item.status}
                </span>
              </div>
              <div style={{ fontSize: '0.95rem', fontWeight: 700, color: '#f8fafc', marginTop: '6px' }}>
                {item.title}
              </div>
              <div style={{ fontSize: '0.75rem', color: '#94a3b8', marginTop: '4px' }}>
                Due: {item.due} • {item.points} Points Max
              </div>
              {studentTab === 'pending' && !isSubmitted && (
                <button
                  onClick={() => handleStudentSubmit(item.id)}
                  className="btn btn-primary"
                  style={{ width: '100%', marginTop: '10px', padding: '8px', fontSize: '0.8rem' }}
                >
                  📤 Upload & Submit
                </button>
              )}
            </div>
          );
        })}
      </div>
    </div>
  );
};
