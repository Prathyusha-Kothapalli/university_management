import React, { useState } from 'react';
import { useFetch } from '../../hooks/useFetch';
import { examsApi } from '../../services/api';
import { Card } from '../../components/Card';
import { DataTable, Column } from '../../components/DataTable';
import { Button } from '../../components/Button';
import { Modal } from '../../components/Modal';
import { useToast } from '../../hooks/useToast';
import { ExamSchedule, ExamResult } from '../../types';
import { Award, Calendar, FileText, Download, Calculator, TrendingUp, Ticket, QrCode, AlertCircle } from 'lucide-react';

export const ExamsPage: React.FC = () => {
  const { showToast } = useToast();
  const [activeTab, setActiveTab] = useState<'schedules' | 'results' | 'transcript' | 'calculator'>('schedules');

  // GPA Target Calculator State
  const [targetCgpa, setTargetCgpa] = useState<number>(3.90);

  // Feature 9: Hall Ticket Modal
  const [selectedScheduleForTicket, setSelectedScheduleForTicket] = useState<ExamSchedule | null>(null);

  // Feature 10: Re-evaluation Appeal Modal
  const [selectedResultForAppeal, setSelectedResultForAppeal] = useState<ExamResult | null>(null);
  const [appealReason, setAppealReason] = useState('');

  const { data: schedules = [] } = useFetch(examsApi.getExamSchedules);
  const { data: results = [] } = useFetch(examsApi.getExamResults);
  const { data: transcripts = [] } = useFetch(examsApi.getTranscripts);

  const handleDownloadTranscript = () => {
    showToast('Official Grade Transcript PDF generated & downloading...', 'success');
  };

  const handlePrintHallTicket = () => {
    window.print();
    showToast('Printing Exam Hall Admit Ticket...', 'info');
  };

  const handleSubmitAppeal = (e: React.FormEvent) => {
    e.preventDefault();
    showToast(`Submitted Grade Re-Evaluation Appeal for Result ${selectedResultForAppeal?.id}`, 'success');
    setSelectedResultForAppeal(null);
    setAppealReason('');
  };

  const scheduleColumns: Column<ExamSchedule>[] = [
    { header: 'Exam ID', accessorKey: 'exam_id' },
    { header: 'Exam Date', accessorKey: 'exam_date', cell: (r) => <strong style={{ color: '#38bdf8' }}>{r.exam_date}</strong> },
    { header: 'Start Time', accessorKey: 'start_time' },
    { header: 'End Time', accessorKey: 'end_time' },
  ];

  const resultColumns: Column<ExamResult>[] = [
    { header: 'Student ID', accessorKey: 'student_id' },
    { header: 'Marks Obtained', accessorKey: 'marks_obtained', cell: (r) => <strong>{r.marks_obtained} / {r.max_marks}</strong> },
    { header: 'Grade', accessorKey: 'grade', cell: (r) => <span style={{ padding: '2px 8px', borderRadius: '12px', background: 'rgba(16,185,129,0.2)', color: '#10b981', fontWeight: 700 }}>{r.grade}</span> },
    { header: 'Remarks', accessorKey: 'remarks' },
  ];

  const transcriptData = transcripts && transcripts.length > 0 ? transcripts[0] : null;

  return (
    <div style={{ padding: '1.5rem 2rem', display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <div>
          <h1 style={{ margin: 0, fontSize: '1.6rem', fontWeight: 800, color: '#f8fafc' }}>
            Examinations, Grades & Transcripts
          </h1>
          <p style={{ margin: '4px 0 0 0', fontSize: '0.85rem', color: '#94a3b8' }}>
            Group 6 APIs (`/api/v1/exams/`, `/api/v1/exam-schedules/`, `/api/v1/exam-results/`, `/api/v1/transcripts/`)
          </p>
        </div>

        <Button variant="primary" icon={<Download size={16} />} onClick={handleDownloadTranscript}>
          Generate Official Transcript
        </Button>
      </div>

      {/* Tabs */}
      <div style={{ display: 'flex', gap: '8px', borderBottom: '1px solid rgba(255, 255, 255, 0.08)', paddingBottom: '8px' }}>
        {[
          { id: 'schedules', label: 'Exam Schedules', icon: <Calendar size={16} /> },
          { id: 'results', label: 'Gradebook & Results', icon: <Award size={16} /> },
          { id: 'transcript', label: 'Academic Transcript', icon: <FileText size={16} /> },
          { id: 'calculator', label: 'GPA Predictor Tool', icon: <Calculator size={16} /> },
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
        {activeTab === 'schedules' && (
          <DataTable
            columns={scheduleColumns}
            data={schedules || []}
            actions={(row) => (
              <Button variant="primary" size="sm" icon={<Ticket size={14} />} onClick={() => setSelectedScheduleForTicket(row)}>
                Hall Admit Ticket
              </Button>
            )}
          />
        )}
        {activeTab === 'results' && (
          <DataTable
            columns={resultColumns}
            data={results || []}
            actions={(row) => (
              <Button variant="outline" size="sm" icon={<AlertCircle size={14} />} onClick={() => setSelectedResultForAppeal(row)}>
                Appeal Grade
              </Button>
            )}
          />
        )}
        {activeTab === 'transcript' && (
          <div style={{ padding: '1rem', display: 'flex', flexDirection: 'column', gap: '1rem' }}>
            <div style={{ padding: '1.25rem', background: 'rgba(37,99,235,0.1)', border: '1px solid rgba(56,189,248,0.3)', borderRadius: '12px' }}>
              <h3 style={{ margin: 0, color: '#f8fafc' }}>UniSphere Cumulative Academic Summary</h3>
              <div style={{ display: 'flex', gap: '2rem', marginTop: '1rem' }}>
                <div>
                  <div style={{ fontSize: '0.8rem', color: '#94a3b8' }}>Cumulative GPA</div>
                  <div style={{ fontSize: '1.6rem', fontWeight: 800, color: '#38bdf8' }}>{transcriptData?.cgpa ?? 3.84}</div>
                </div>
                <div>
                  <div style={{ fontSize: '0.8rem', color: '#94a3b8' }}>Total Earned Credits</div>
                  <div style={{ fontSize: '1.6rem', fontWeight: 800, color: '#10b981' }}>{transcriptData?.total_credits_earned ?? 76}</div>
                </div>
                <div>
                  <div style={{ fontSize: '0.8rem', color: '#94a3b8' }}>Standing</div>
                  <div style={{ fontSize: '1.6rem', fontWeight: 800, color: '#a855f7' }}>First Class with Distinction</div>
                </div>
              </div>
            </div>
          </div>
        )}
        {activeTab === 'calculator' && (
          <div style={{ padding: '1.25rem', display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
              <TrendingUp size={24} style={{ color: '#a855f7' }} />
              <div>
                <h3 style={{ margin: 0, color: '#f8fafc' }}>Interactive CGPA Target Predictor</h3>
                <p style={{ margin: '2px 0 0 0', fontSize: '0.85rem', color: '#94a3b8' }}>
                  Simulate required grades in upcoming courses to achieve your desired graduation honors.
                </p>
              </div>
            </div>

            <div style={{ background: 'rgba(255,255,255,0.03)', padding: '1.25rem', borderRadius: '12px', display: 'flex', flexDirection: 'column', gap: '1rem' }}>
              <div>
                <label style={{ display: 'block', fontSize: '0.85rem', fontWeight: 600, color: '#cbd5e1', marginBottom: '8px' }}>
                  Desired Graduation Target CGPA: <strong style={{ color: '#38bdf8' }}>{targetCgpa.toFixed(2)}</strong>
                </label>
                <input
                  type="range"
                  min="3.00"
                  max="4.00"
                  step="0.05"
                  value={targetCgpa}
                  onChange={(e) => setTargetCgpa(parseFloat(e.target.value))}
                  style={{ width: '100%', accentColor: '#2563eb' }}
                />
              </div>

              <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1rem', marginTop: '0.5rem' }}>
                <div style={{ padding: '1rem', background: 'rgba(16,185,129,0.1)', border: '1px solid rgba(16,185,129,0.3)', borderRadius: '10px' }}>
                  <div style={{ fontSize: '0.75rem', color: '#94a3b8' }}>Required Average SGPA (Next 4 Semesters)</div>
                  <div style={{ fontSize: '1.5rem', fontWeight: 800, color: '#10b981', marginTop: '4px' }}>
                    {targetCgpa > 3.84 ? (3.84 + (targetCgpa - 3.84) * 1.5).toFixed(2) : '3.80'} / 4.00
                  </div>
                </div>
                <div style={{ padding: '1rem', background: 'rgba(168,85,247,0.1)', border: '1px solid rgba(168,85,247,0.3)', borderRadius: '10px' }}>
                  <div style={{ fontSize: '0.75rem', color: '#94a3b8' }}>Target Grade Distribution</div>
                  <div style={{ fontSize: '1.1rem', fontWeight: 700, color: '#c084fc', marginTop: '4px' }}>
                    {targetCgpa >= 3.9 ? '80% A+ (4.0), 20% A (3.7)' : '60% A (3.7), 40% B+ (3.3)'}
                  </div>
                </div>
              </div>
            </div>
          </div>
        )}
      </Card>

      {/* Feature 9: Hall Ticket Modal */}
      <Modal
        isOpen={!!selectedScheduleForTicket}
        onClose={() => setSelectedScheduleForTicket(null)}
        title="Official End-Semester Examination Hall Admit Ticket"
      >
        {selectedScheduleForTicket && (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
            <div style={{ padding: '1rem', background: 'rgba(37,99,235,0.1)', border: '1px solid rgba(56,189,248,0.3)', borderRadius: '12px', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <div>
                <div style={{ fontSize: '0.75rem', color: '#94a3b8' }}>Candidate Roll Number</div>
                <strong style={{ fontSize: '1.1rem', color: '#38bdf8' }}>UNI-2026-8890</strong>
              </div>
              <div style={{ textAlign: 'right' }}>
                <div style={{ fontSize: '0.75rem', color: '#94a3b8' }}>Assigned Hall & Seat</div>
                <strong style={{ fontSize: '1.1rem', color: '#10b981' }}>ATH-302 (Desk #44)</strong>
              </div>
            </div>

            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1rem', fontSize: '0.85rem' }}>
              <div><span style={{ color: '#94a3b8' }}>Exam Date:</span> <strong>{selectedScheduleForTicket.exam_date}</strong></div>
              <div><span style={{ color: '#94a3b8' }}>Timing:</span> <strong>{selectedScheduleForTicket.start_time} - {selectedScheduleForTicket.end_time}</strong></div>
            </div>

            <div style={{ display: 'flex', alignItems: 'center', gap: '16px', padding: '1rem', background: 'rgba(255,255,255,0.03)', borderRadius: '10px' }}>
              <QrCode size={40} style={{ color: '#38bdf8' }} />
              <div style={{ fontSize: '0.75rem', color: '#94a3b8' }}>Admit Ticket QR Code. Present student ID at entrance door.</div>
            </div>

            <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '8px' }}>
              <Button variant="ghost" onClick={() => setSelectedScheduleForTicket(null)}>Close</Button>
              <Button variant="primary" icon={<Download size={14} />} onClick={handlePrintHallTicket}>Print Admit Card</Button>
            </div>
          </div>
        )}
      </Modal>

      {/* Feature 10: Grade Re-Evaluation Appeal Modal */}
      <Modal
        isOpen={!!selectedResultForAppeal}
        onClose={() => setSelectedResultForAppeal(null)}
        title={`Submit Grade Re-Evaluation Appeal: Result ${selectedResultForAppeal?.id || ''}`}
      >
        <form onSubmit={handleSubmitAppeal} style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
          <div style={{ fontSize: '0.85rem', color: '#cbd5e1' }}>
            Requesting formal paper re-checking for score: <strong>{selectedResultForAppeal?.marks_obtained} / {selectedResultForAppeal?.max_marks}</strong> (Grade {selectedResultForAppeal?.grade}).
          </div>
          <div>
            <label style={{ display: 'block', fontSize: '0.8rem', color: '#cbd5e1', marginBottom: '4px' }}>Reason for Re-Evaluation Appeal</label>
            <textarea
              required
              rows={3}
              placeholder="State question numbers or discrepancy details..."
              value={appealReason}
              onChange={(e) => setAppealReason(e.target.value)}
              style={{ width: '100%', padding: '8px 12px', background: 'rgba(15,23,42,0.8)', border: '1px solid rgba(255,255,255,0.1)', borderRadius: '8px', color: '#fff' }}
            />
          </div>
          <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '8px', marginTop: '1rem' }}>
            <Button variant="ghost" type="button" onClick={() => setSelectedResultForAppeal(null)}>Cancel</Button>
            <Button variant="primary" type="submit">Submit Appeal</Button>
          </div>
        </form>
      </Modal>
    </div>
  );
};
