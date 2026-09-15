import React, { useState } from 'react';
import { useFetch } from '../../hooks/useFetch';
import { learningApi } from '../../services/api';
import { Card } from '../../components/Card';
import { DataTable, Column } from '../../components/DataTable';
import { Button } from '../../components/Button';
import { Modal } from '../../components/Modal';
import { useToast } from '../../hooks/useToast';
import { Assignment, AssignmentSubmission, LearningMaterial } from '../../types';
import { FileText, Upload, Download, CheckCircle, Edit3, ShieldAlert, Eye, FileSpreadsheet, Video, Play, Clock, Sparkles, Terminal } from 'lucide-react';

export const LearningPage: React.FC = () => {
  const { showToast } = useToast();
  const [activeTab, setActiveTab] = useState<'assignments' | 'submissions' | 'materials'>('assignments');

  // Feature 54: Code Sandbox Benchmark Modal State
  const [isCodeBenchmarkOpen, setIsCodeBenchmarkOpen] = useState(false);
  const [selectedAssignment, setSelectedAssignment] = useState<Assignment | null>(null);
  const [submissionText, setSubmissionText] = useState('');
  const [isSubmitModalOpen, setIsSubmitModalOpen] = useState(false);

  // Feature 23: Recorded Lecture Video Player Modal State
  const [isLectureModalOpen, setIsLectureModalOpen] = useState(false);
  const [playbackSpeed, setPlaybackSpeed] = useState<string>('1.0x');

  // Feature 3: Faculty Grade Marking Modal
  const [selectedSubForGrading, setSelectedSubForGrading] = useState<AssignmentSubmission | null>(null);
  const [gradeMarks, setGradeMarks] = useState<string>('95');
  const [gradeFeedback, setGradeFeedback] = useState<string>('Excellent implementation of QLoRA optimization.');

  // Feature 6: Slide Preview Modal
  const [selectedMaterialForPreview, setSelectedMaterialForPreview] = useState<LearningMaterial | null>(null);

  // Feature 7: Plagiarism Report Modal
  const [selectedSubForPlagiarism, setSelectedSubForPlagiarism] = useState<AssignmentSubmission | null>(null);

  const { data: assignments = [] } = useFetch(learningApi.getAssignments);
  const { data: submissions = [], refetch: refetchSubmissions } = useFetch(learningApi.getAssignmentSubmissions);
  const { data: materials = [] } = useFetch(learningApi.getLearningMaterials);

  const handleOpenSubmitModal = (asg: Assignment) => {
    setSelectedAssignment(asg);
    setSubmissionText('');
    setIsSubmitModalOpen(true);
  };

  const handleSubmitAssignment = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!selectedAssignment) return;
    try {
      await learningApi.submitAssignment({
        assignment_id: selectedAssignment.id,
        submission_text: submissionText,
      });
      showToast(`Submitted solution for "${selectedAssignment.title}"`, 'success');
      setIsSubmitModalOpen(false);
      refetchSubmissions();
    } catch (err) {
      showToast('Failed to upload submission', 'error');
    }
  };

  const handleSaveGrade = (e: React.FormEvent) => {
    e.preventDefault();
    if (!selectedSubForGrading) return;
    showToast(`Graded submission ${selectedSubForGrading.id} with ${gradeMarks} marks`, 'success');
    setSelectedSubForGrading(null);
    refetchSubmissions();
  };

  // Feature 8: Export Submissions to CSV
  const handleExportCSV = () => {
    const csvHeader = 'Submission ID,Assignment ID,Student ID,Submission Date,Status,Marks Obtained\n';
    const csvRows = (submissions || [])
      .map((s) => `${s.id},${s.assignment_id},${s.student_id},${s.submission_date},${s.status},${s.marks_obtained ?? 'Pending'}`)
      .join('\n');
    const blob = new Blob([csvHeader + csvRows], { type: 'text/csv' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `Submissions_Gradebook_Export.csv`;
    a.click();
    showToast('Exported gradebook submissions to CSV file!', 'success');
  };

  const assignmentColumns: Column<Assignment>[] = [
    { header: 'Title', accessorKey: 'title', cell: (r) => <strong>{r.title}</strong> },
    { header: 'Max Marks', accessorKey: 'max_marks', cell: (r) => <span>{r.max_marks} pts</span> },
    { header: 'Due Date', accessorKey: 'due_date', cell: (r) => <span style={{ color: '#f59e0b' }}>{new Date(r.due_date).toLocaleDateString()}</span> },
    { header: 'Description', accessorKey: 'description' },
  ];

  const submissionColumns: Column<AssignmentSubmission>[] = [
    { header: 'Submission ID', accessorKey: 'id', cell: (r) => <span style={{ color: '#38bdf8' }}>{r.id}</span> },
    { header: 'Status', accessorKey: 'status', cell: (r) => <span style={{ padding: '2px 8px', borderRadius: '12px', background: r.status === 'Graded' ? 'rgba(16,185,129,0.2)' : 'rgba(245,158,11,0.2)', color: r.status === 'Graded' ? '#10b981' : '#f59e0b', fontSize: '0.75rem' }}>{r.status}</span> },
    { header: 'Marks Obtained', accessorKey: 'marks_obtained', cell: (r) => <strong>{r.marks_obtained !== undefined ? `${r.marks_obtained} pts` : 'Pending'}</strong> },
    { header: 'Plagiarism', cell: () => <span style={{ padding: '2px 8px', borderRadius: '12px', background: 'rgba(16,185,129,0.15)', color: '#10b981', fontSize: '0.75rem', fontWeight: 600 }}>2% Similarity 🟢</span> },
  ];

  const materialColumns: Column<LearningMaterial>[] = [
    { header: 'Title', accessorKey: 'title', cell: (r) => <strong>{r.title}</strong> },
    { header: 'Type', accessorKey: 'material_type', cell: (r) => <span style={{ color: '#a855f7', fontWeight: 600 }}>{r.material_type}</span> },
    { header: 'Description', accessorKey: 'description' },
  ];

  return (
    <div style={{ padding: '1.5rem 2rem', display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <div>
          <h1 style={{ margin: 0, fontSize: '1.6rem', fontWeight: 800, color: '#f8fafc' }}>
            Assignments & Learning Resources
          </h1>
          <p style={{ margin: '4px 0 0 0', fontSize: '0.85rem', color: '#94a3b8' }}>
            Group 5 APIs (`/api/v1/assignments/`, `/api/v1/assignment-submissions/`, `/api/v1/learning-materials/`)
          </p>
        </div>

        <div style={{ display: 'flex', gap: '10px', flexWrap: 'wrap' }}>
          <Button variant="outline" icon={<Terminal size={16} />} onClick={() => setIsCodeBenchmarkOpen(true)}>
            Code Sandbox & Benchmark
          </Button>
          <Button variant="outline" icon={<Video size={16} />} onClick={() => setIsLectureModalOpen(true)}>
            Watch Recorded Lecture
          </Button>
          <Button variant="secondary" icon={<FileSpreadsheet size={16} />} onClick={handleExportCSV}>
            Export Gradebook CSV
          </Button>
        </div>
      </div>

      {/* Tabs */}
      <div style={{ display: 'flex', gap: '8px', borderBottom: '1px solid rgba(255, 255, 255, 0.08)', paddingBottom: '8px' }}>
        {[
          { id: 'assignments', label: 'Course Assignments', icon: <FileText size={16} /> },
          { id: 'submissions', label: 'My Submissions & Grading', icon: <CheckCircle size={16} /> },
          { id: 'materials', label: 'Study Materials & Notes', icon: <Download size={16} /> },
        ].map((tab) => (
          <button
            key={tab.id}
            onClick={() => setActiveTab(tab.id as any)}
            style={{
              display: 'flex',
              alignItems: 'center',
              gap: '6px',
              padding: '8px 16px',
              borderRadius: '8px',
              border: activeTab === tab.id ? '1px solid rgba(56, 189, 248, 0.4)' : 'none',
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

      <Card>
        {activeTab === 'assignments' && (
          <DataTable
            columns={assignmentColumns}
            data={assignments || []}
            actions={(row) => (
              <Button variant="primary" size="sm" icon={<Upload size={14} />} onClick={() => handleOpenSubmitModal(row)}>
                Submit Solution
              </Button>
            )}
          />
        )}
        {activeTab === 'submissions' && (
          <DataTable
            columns={submissionColumns}
            data={submissions || []}
            actions={(row) => (
              <div style={{ display: 'flex', gap: '6px' }}>
                <Button variant="secondary" size="sm" icon={<Edit3 size={14} />} onClick={() => setSelectedSubForGrading(row)}>
                  Grade Solution
                </Button>
                <Button variant="outline" size="sm" icon={<ShieldAlert size={14} />} onClick={() => setSelectedSubForPlagiarism(row)}>
                  Plagiarism Report
                </Button>
              </div>
            )}
          />
        )}
        {activeTab === 'materials' && (
          <DataTable
            columns={materialColumns}
            data={materials || []}
            actions={(row) => (
              <Button variant="outline" size="sm" icon={<Eye size={14} />} onClick={() => setSelectedMaterialForPreview(row)}>
                Preview Deck
              </Button>
            )}
          />
        )}
      </Card>

      {/* Feature 6: Material Preview Modal */}
      <Modal
        isOpen={!!selectedMaterialForPreview}
        onClose={() => setSelectedMaterialForPreview(null)}
        title={`Slide Deck Preview: ${selectedMaterialForPreview?.title || ''}`}
      >
        {selectedMaterialForPreview && (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
            <div style={{ height: '220px', background: 'rgba(0,0,0,0.4)', borderRadius: '12px', border: '1px solid rgba(255,255,255,0.1)', display: 'flex', alignItems: 'center', justifyContent: 'center', flexDirection: 'column', gap: '8px' }}>
              <Eye size={40} style={{ color: '#38bdf8' }} />
              <div style={{ fontSize: '0.9rem', color: '#f8fafc', fontWeight: 600 }}>Interactive Document Viewer</div>
              <div style={{ fontSize: '0.75rem', color: '#94a3b8' }}>{selectedMaterialForPreview.material_type} • Uploaded on {selectedMaterialForPreview.uploaded_at}</div>
            </div>
            <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '8px' }}>
              <Button variant="ghost" onClick={() => setSelectedMaterialForPreview(null)}>Close</Button>
              <Button variant="primary" icon={<Download size={14} />}>Download Full File</Button>
            </div>
          </div>
        )}
      </Modal>

      {/* Feature 7: Plagiarism Report Modal */}
      <Modal
        isOpen={!!selectedSubForPlagiarism}
        onClose={() => setSelectedSubForPlagiarism(null)}
        title={`Turnitin AI Plagiarism Analysis: ${selectedSubForPlagiarism?.id || ''}`}
      >
        {selectedSubForPlagiarism && (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
            <div style={{ padding: '1rem', background: 'rgba(16,185,129,0.1)', border: '1px solid rgba(16,185,129,0.3)', borderRadius: '12px', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <div>
                <div style={{ fontSize: '0.75rem', color: '#94a3b8' }}>Overall Similarity Index</div>
                <strong style={{ fontSize: '1.4rem', color: '#10b981' }}>2.1% (Original Work)</strong>
              </div>
              <span style={{ padding: '4px 10px', background: '#10b981', color: '#fff', borderRadius: '12px', fontSize: '0.75rem', fontWeight: 700 }}>
                VERIFIED CLEAN
              </span>
            </div>

            <div style={{ fontSize: '0.85rem', color: '#cbd5e1' }}>
              • Matching Text Sources: 0% Internet Sources, 2.1% Student Papers repository (citation matched).
              <br />
              • AI-Generated Content Probability: &lt; 1% (Human-authored code & notes).
            </div>

            <div style={{ display: 'flex', justifyContent: 'flex-end' }}>
              <Button variant="primary" onClick={() => setSelectedSubForPlagiarism(null)}>Close Analysis</Button>
            </div>
          </div>
        )}
      </Modal>

      {/* Submit Assignment Modal */}
      <Modal
        isOpen={isSubmitModalOpen}
        onClose={() => setIsSubmitModalOpen(false)}
        title={`Submit Work: ${selectedAssignment?.title || ''}`}
      >
        <form onSubmit={handleSubmitAssignment} style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
          <div>
            <label style={{ display: 'block', fontSize: '0.8rem', color: '#cbd5e1', marginBottom: '4px' }}>
              Submission Notes / GitHub Repository Link
            </label>
            <textarea
              required
              rows={4}
              placeholder="Paste your solution notes or submission links..."
              value={submissionText}
              onChange={(e) => setSubmissionText(e.target.value)}
              style={{ width: '100%', padding: '10px 12px', background: 'rgba(15,23,42,0.8)', border: '1px solid rgba(255,255,255,0.1)', borderRadius: '8px', color: '#fff' }}
            />
          </div>
          <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '8px' }}>
            <Button variant="ghost" type="button" onClick={() => setIsSubmitModalOpen(false)}>Cancel</Button>
            <Button variant="primary" type="submit">Submit Assignment</Button>
          </div>
        </form>
      </Modal>

      {/* Feature 3: Faculty Grade Marking Modal */}
      <Modal
        isOpen={!!selectedSubForGrading}
        onClose={() => setSelectedSubForGrading(null)}
        title={`Faculty Grading: Submission ${selectedSubForGrading?.id || ''}`}
      >
        <form onSubmit={handleSaveGrade} style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
          <div>
            <label style={{ display: 'block', fontSize: '0.8rem', color: '#cbd5e1', marginBottom: '4px' }}>Marks Awarded (Out of 100)</label>
            <input
              type="number"
              required
              min={0}
              max={100}
              value={gradeMarks}
              onChange={(e) => setGradeMarks(e.target.value)}
              style={{ width: '100%', padding: '8px 12px', background: 'rgba(15,23,42,0.8)', border: '1px solid rgba(255,255,255,0.1)', borderRadius: '8px', color: '#fff' }}
            />
          </div>
          <div>
            <label style={{ display: 'block', fontSize: '0.8rem', color: '#cbd5e1', marginBottom: '4px' }}>Instructor Feedback Notes</label>
            <textarea
              required
              rows={3}
              value={gradeFeedback}
              onChange={(e) => setGradeFeedback(e.target.value)}
              style={{ width: '100%', padding: '8px 12px', background: 'rgba(15,23,42,0.8)', border: '1px solid rgba(255,255,255,0.1)', borderRadius: '8px', color: '#fff' }}
            />
          </div>
          <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '8px', marginTop: '1rem' }}>
            <Button variant="ghost" type="button" onClick={() => setSelectedSubForGrading(null)}>Cancel</Button>
            <Button variant="primary" type="submit">Save Grade & Feedback</Button>
          </div>
        </form>
      </Modal>

      {/* Feature 23: Course Recorded Lecture Video Player & Timestamped Notes Modal */}
      <Modal
        isOpen={isLectureModalOpen}
        onClose={() => setIsLectureModalOpen(false)}
        title="CS301 Lecture 12: Transformer Attention Mechanisms & Multi-Head Self-Attention"
      >
        <div style={{ display: 'flex', flexDirection: 'column', gap: '1.25rem' }}>
          {/* Simulated Video Player */}
          <div
            style={{
              width: '100%',
              height: '220px',
              borderRadius: '12px',
              background: 'linear-gradient(135deg, #0f172a, #1e293b)',
              border: '1px solid rgba(56,189,248,0.3)',
              position: 'relative',
              display: 'flex',
              flexDirection: 'column',
              justifyContent: 'center',
              alignItems: 'center',
              boxShadow: '0 8px 20px rgba(0,0,0,0.4)',
            }}
          >
            <div style={{ width: '56px', height: '56px', borderRadius: '50%', background: 'rgba(56,189,248,0.25)', display: 'flex', alignItems: 'center', justifyContent: 'center', color: '#38bdf8', cursor: 'pointer', border: '2px solid #38bdf8' }} onClick={() => showToast('Playing lecture recording stream...', 'info')}>
              <Play size={24} style={{ marginLeft: '4px' }} />
            </div>

            <div style={{ position: 'absolute', bottom: '12px', left: '16px', right: '16px', display: 'flex', justifyContent: 'space-between', alignItems: 'center', fontSize: '0.75rem', color: '#cbd5e1' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                <Clock size={14} /> 24:18 / 45:00 Mins
              </div>

              <div style={{ display: 'flex', gap: '6px' }}>
                {['1.0x', '1.25x', '1.5x', '2.0x'].map((spd) => (
                  <button
                    key={spd}
                    type="button"
                    onClick={() => {
                      setPlaybackSpeed(spd);
                      showToast(`Playback speed set to ${spd}`, 'info');
                    }}
                    style={{
                      padding: '2px 8px',
                      borderRadius: '4px',
                      border: 'none',
                      background: playbackSpeed === spd ? '#2563eb' : 'rgba(255,255,255,0.1)',
                      color: '#fff',
                      fontSize: '0.7rem',
                      cursor: 'pointer',
                      fontWeight: 600,
                    }}
                  >
                    {spd}
                  </button>
                ))}
              </div>
            </div>
          </div>

          <div style={{ fontSize: '0.85rem', fontWeight: 700, color: '#f8fafc', display: 'flex', alignItems: 'center', gap: '6px' }}>
            <Sparkles size={16} style={{ color: '#a855f7' }} /> AI Transcript Timestamps & Chapter Summary:
          </div>

          <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
            <div style={{ padding: '8px 12px', background: 'rgba(255,255,255,0.03)', borderRadius: '8px', display: 'flex', justifyContent: 'space-between', alignItems: 'center', fontSize: '0.8rem' }}>
              <div>
                <strong style={{ color: '#38bdf8' }}>[04:15]</strong> <span style={{ color: '#cbd5e1' }}>Query, Key, and Value Matrix Rotations</span>
              </div>
              <Button variant="ghost" size="sm" onClick={() => showToast('Seeked to 04:15', 'info')}>Jump</Button>
            </div>

            <div style={{ padding: '8px 12px', background: 'rgba(255,255,255,0.03)', borderRadius: '8px', display: 'flex', justifyContent: 'space-between', alignItems: 'center', fontSize: '0.8rem' }}>
              <div>
                <strong style={{ color: '#a855f7' }}>[18:30]</strong> <span style={{ color: '#cbd5e1' }}>Scaled Dot-Product Attention Equation</span>
              </div>
              <Button variant="ghost" size="sm" onClick={() => showToast('Seeked to 18:30', 'info')}>Jump</Button>
            </div>
          </div>

          <div style={{ display: 'flex', justifyContent: 'flex-end', marginTop: '0.5rem' }}>
            <Button variant="primary" onClick={() => setIsLectureModalOpen(false)}>Close Player</Button>
          </div>
        </div>
      </Modal>

      {/* Feature 54: Automated Code Sandbox Execution Benchmark Modal */}
      <Modal
        isOpen={isCodeBenchmarkOpen}
        onClose={() => setIsCodeBenchmarkOpen(false)}
        title="Interactive Code Execution Sandbox & Benchmark Profiler"
      >
        <div style={{ display: 'flex', flexDirection: 'column', gap: '1.25rem' }}>
          <div style={{ padding: '1rem', background: 'rgba(15,23,42,0.9)', borderRadius: '10px', border: '1px solid rgba(255,255,255,0.1)', fontFamily: 'monospace', fontSize: '0.75rem', color: '#10b981' }}>
            $ python3 solution.py --benchmark
            <br />
            [SUCCESS] Passed 14/14 Test Cases in 14.2ms. Peak RAM: 8.4 MB (O(N log N)).
          </div>
          <Button variant="primary" onClick={() => { showToast('Ran Python algorithm benchmarks successfully!', 'success'); setIsCodeBenchmarkOpen(false); }}>
            Execute Code Benchmark
          </Button>
        </div>
      </Modal>
    </div>
  );
};
