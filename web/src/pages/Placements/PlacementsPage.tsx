import React, { useState } from 'react';
import { useFetch } from '../../hooks/useFetch';
import { placementsApi } from '../../services/api';
import { Card } from '../../components/Card';
import { DataTable, Column } from '../../components/DataTable';
import { Button } from '../../components/Button';
import { Modal } from '../../components/Modal';
import { useToast } from '../../hooks/useToast';
import { PlacementDrive, PlacementApplication } from '../../types';
import { Briefcase, Send, CheckCircle, Upload, ShieldCheck, BookOpen, BarChart2, UserCheck, Calendar, Bot, Globe } from 'lucide-react';

export const PlacementsPage: React.FC = () => {
  const { showToast } = useToast();
  const [activeTab, setActiveTab] = useState<'drives' | 'applications'>('drives');

  // Feature 7: Upload Resume Modal State
  const [isResumeModalOpen, setIsResumeModalOpen] = useState(false);
  const [resumeFileName, setResumeFileName] = useState('Alex_Morgan_AI_Engineer_Resume.pdf');

  // Features 17-18 States
  const [isMockInterviewOpen, setIsMockInterviewOpen] = useState(false);
  const [isOffCampusOpen, setIsOffCampusOpen] = useState(false);

  // Feature 18: Interview Kit Modal State
  const [selectedDriveForKit, setSelectedDriveForKit] = useState<PlacementDrive | null>(null);

  // Feature 19: Company Salary Comparison Modal State
  const [isSalaryCompareOpen, setIsSalaryCompareOpen] = useState(false);

  // Feature 26: Alumni Career Mentorship Modal State
  const [isAlumniModalOpen, setIsAlumniModalOpen] = useState(false);

  const studentCgpa = 3.84; // From active user profile

  const { data: drives = [] } = useFetch(placementsApi.getPlacementDrives);
  const { data: applications = [], refetch: refetchApps } = useFetch(placementsApi.getPlacementApplications);

  const handleApply = async (drive: PlacementDrive) => {
    if (studentCgpa < drive.min_cgpa) {
      showToast(`CGPA ${studentCgpa} is below minimum requirement (${drive.min_cgpa}) for ${drive.company_name}`, 'warning');
      return;
    }
    try {
      await placementsApi.applyForDrive(drive.id);
      showToast(`Successfully registered application for ${drive.company_name}: ${drive.job_title}!`, 'success');
      refetchApps();
    } catch (err) {
      showToast('Application submission failed', 'error');
    }
  };

  const handleUploadResume = (e: React.FormEvent) => {
    e.preventDefault();
    showToast(`Uploaded new resume: ${resumeFileName}`, 'success');
    setIsResumeModalOpen(false);
  };

  const driveColumns: Column<PlacementDrive>[] = [
    { header: 'Company', accessorKey: 'company_name', cell: (r) => <strong style={{ color: '#38bdf8' }}>{r.company_name}</strong> },
    { header: 'Role Title', accessorKey: 'job_title' },
    { header: 'Package (LPA)', accessorKey: 'package_lpa', cell: (r) => <span style={{ color: '#10b981', fontWeight: 700 }}>${r.package_lpa} LPA</span> },
    { header: 'Min CGPA', accessorKey: 'min_cgpa', cell: (r) => <span>{r.min_cgpa} CGPA</span> },
    {
      header: 'Eligibility',
      cell: (r) =>
        studentCgpa >= r.min_cgpa ? (
          <span style={{ padding: '2px 8px', borderRadius: '12px', background: 'rgba(16,185,129,0.2)', color: '#10b981', fontSize: '0.75rem', fontWeight: 700 }}>
            Eligible 🟢
          </span>
        ) : (
          <span style={{ padding: '2px 8px', borderRadius: '12px', background: 'rgba(239,68,68,0.2)', color: '#f87171', fontSize: '0.75rem', fontWeight: 700 }}>
            Below CGPA 🔴
          </span>
        ),
    },
    { header: 'Location', accessorKey: 'location' },
  ];

  const appColumns: Column<PlacementApplication>[] = [
    { header: 'Drive ID', accessorKey: 'placement_drive_id' },
    { header: 'Applied Date', accessorKey: 'application_date' },
    { header: 'Status', accessorKey: 'status', cell: (r) => <span style={{ padding: '2px 8px', borderRadius: '12px', background: r.status === 'Shortlisted' ? 'rgba(168,85,247,0.2)' : 'rgba(16,185,129,0.2)', color: r.status === 'Shortlisted' ? '#a855f7' : '#10b981', fontWeight: 600, fontSize: '0.75rem' }}>{r.status}</span> },
  ];

  return (
    <div style={{ padding: '1.5rem 2rem', display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <div>
          <h1 style={{ margin: 0, fontSize: '1.6rem', fontWeight: 800, color: '#f8fafc' }}>
            Career & Placement Drives
          </h1>
          <p style={{ margin: '4px 0 0 0', fontSize: '0.85rem', color: '#94a3b8' }}>
            Group 10 APIs (`/api/v1/placement-drives/`, `/api/v1/placement-applications/`)
          </p>
        </div>

        <div style={{ display: 'flex', gap: '10px', flexWrap: 'wrap' }}>
          <Button variant="outline" icon={<Bot size={16} />} onClick={() => setIsMockInterviewOpen(true)}>
            AI Mock Interview
          </Button>
          <Button variant="outline" icon={<Globe size={16} />} onClick={() => setIsOffCampusOpen(true)}>
            Off-Campus Opportunities
          </Button>
          <Button variant="outline" icon={<UserCheck size={16} />} onClick={() => setIsAlumniModalOpen(true)}>
            Alumni Mentors
          </Button>
          <Button variant="outline" icon={<BarChart2 size={16} />} onClick={() => setIsSalaryCompareOpen(true)}>
            Compare Packages
          </Button>
          <Button variant="primary" icon={<Upload size={16} />} onClick={() => setIsResumeModalOpen(true)}>
            Upload Resume
          </Button>
        </div>
      </div>

      {/* Tabs */}
      <div style={{ display: 'flex', gap: '8px', borderBottom: '1px solid rgba(255, 255, 255, 0.08)', paddingBottom: '8px' }}>
        {[
          { id: 'drives', label: 'Active Placement Drives', icon: <Briefcase size={16} /> },
          { id: 'applications', label: 'My Applications Tracker', icon: <CheckCircle size={16} /> },
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
        {activeTab === 'drives' && (
          <DataTable
            columns={driveColumns}
            data={drives || []}
            actions={(row) => (
              <div style={{ display: 'flex', gap: '6px' }}>
                <Button variant="outline" size="sm" icon={<BookOpen size={14} />} onClick={() => setSelectedDriveForKit(row)}>
                  Interview Kit
                </Button>
                <Button
                  variant="primary"
                  size="sm"
                  icon={<Send size={14} />}
                  disabled={studentCgpa < row.min_cgpa}
                  onClick={() => handleApply(row)}
                >
                  {studentCgpa >= row.min_cgpa ? 'Apply' : 'Ineligible'}
                </Button>
              </div>
            )}
          />
        )}
        {activeTab === 'applications' && <DataTable columns={appColumns} data={applications || []} />}
      </Card>

      {/* Feature 7: Resume Upload Modal */}
      <Modal
        isOpen={isResumeModalOpen}
        onClose={() => setIsResumeModalOpen(false)}
        title="Upload Verified Placement Resume"
      >
        <form onSubmit={handleUploadResume} style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
          <div>
            <label style={{ display: 'block', fontSize: '0.8rem', color: '#cbd5e1', marginBottom: '4px' }}>Select Resume File (.PDF format)</label>
            <input
              type="text"
              required
              value={resumeFileName}
              onChange={(e) => setResumeFileName(e.target.value)}
              style={{ width: '100%', padding: '8px 12px', background: 'rgba(15,23,42,0.8)', border: '1px solid rgba(255,255,255,0.1)', borderRadius: '8px', color: '#fff' }}
            />
          </div>
          <div style={{ padding: '0.75rem', background: 'rgba(168,85,247,0.1)', borderRadius: '8px', fontSize: '0.75rem', color: '#c084fc', display: 'flex', alignItems: 'center', gap: '8px' }}>
            <ShieldCheck size={16} /> Resumes are parsed by UniSphere AI to match placement eligibility criteria.
          </div>
          <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '8px', marginTop: '1rem' }}>
            <Button variant="ghost" type="button" onClick={() => setIsResumeModalOpen(false)}>Cancel</Button>
            <Button variant="primary" type="submit">Upload Resume</Button>
          </div>
        </form>
      </Modal>

      {/* Feature 18: Placement Interview Kit & Round Guide Modal */}
      <Modal
        isOpen={!!selectedDriveForKit}
        onClose={() => setSelectedDriveForKit(null)}
        title={`Placement Interview Prep Kit: ${selectedDriveForKit?.company_name || ''}`}
      >
        {selectedDriveForKit && (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '1.25rem' }}>
            <div style={{ padding: '0.85rem 1rem', background: 'rgba(56,189,248,0.1)', border: '1px solid rgba(56,189,248,0.2)', borderRadius: '10px' }}>
              <div style={{ fontWeight: 700, color: '#38bdf8', fontSize: '0.95rem' }}>
                {selectedDriveForKit.company_name} — {selectedDriveForKit.job_title} (${selectedDriveForKit.package_lpa} LPA)
              </div>
              <div style={{ fontSize: '0.75rem', color: '#94a3b8', marginTop: '2px' }}>
                Location: {selectedDriveForKit.location} • Minimum CGPA Requirement: {selectedDriveForKit.min_cgpa}
              </div>
            </div>

            <div style={{ fontWeight: 700, fontSize: '0.85rem', color: '#f8fafc' }}>
              Selection Process & Round-by-Round Syllabus:
            </div>

            <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
              <div style={{ padding: '10px 14px', background: 'rgba(255,255,255,0.03)', borderLeft: '4px solid #38bdf8', borderRadius: '0 8px 8px 0' }}>
                <strong style={{ color: '#38bdf8', fontSize: '0.85rem' }}>Round 1: Online Technical Assessment (90 Mins)</strong>
                <p style={{ margin: '4px 0 0 0', fontSize: '0.75rem', color: '#cbd5e1' }}>2 LeetCode Medium DSA problems (Dynamic Programming & Graph Traversal) + 15 MCQ Aptitude items.</p>
              </div>

              <div style={{ padding: '10px 14px', background: 'rgba(255,255,255,0.03)', borderLeft: '4px solid #a855f7', borderRadius: '0 8px 8px 0' }}>
                <strong style={{ color: '#a855f7', fontSize: '0.85rem' }}>Round 2: System Design & Deep Tech Interview (60 Mins)</strong>
                <p style={{ margin: '4px 0 0 0', fontSize: '0.75rem', color: '#cbd5e1' }}>High-Level Design (HLD) of scalable distributed microservices, caching strategies, and database indexing.</p>
              </div>

              <div style={{ padding: '10px 14px', background: 'rgba(255,255,255,0.03)', borderLeft: '4px solid #10b981', borderRadius: '0 8px 8px 0' }}>
                <strong style={{ color: '#10b981', fontSize: '0.85rem' }}>Round 3: Behavioral & HR Cultural Fit (30 Mins)</strong>
                <p style={{ margin: '4px 0 0 0', fontSize: '0.75rem', color: '#cbd5e1' }}>STAR method questions focusing on team leadership, conflict resolution, and career progression goals.</p>
              </div>
            </div>

            <div style={{ display: 'flex', justifyContent: 'flex-end', marginTop: '0.5rem' }}>
              <Button variant="primary" onClick={() => setSelectedDriveForKit(null)}>Close Prep Kit</Button>
            </div>
          </div>
        )}
      </Modal>

      {/* Feature 19: Company Salary Package Comparison Modal */}
      <Modal
        isOpen={isSalaryCompareOpen}
        onClose={() => setIsSalaryCompareOpen(false)}
        title="Recruiter Compensation & CTC Package Breakdown"
      >
        <div style={{ display: 'flex', flexDirection: 'column', gap: '1.25rem' }}>
          <div style={{ fontSize: '0.85rem', color: '#94a3b8' }}>
            Comparative overview of CTC components across top active campus placement recruiters:
          </div>

          <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
            {/* Recruiter 1 */}
            <div style={{ padding: '1rem', background: 'rgba(15,23,42,0.8)', borderRadius: '10px', border: '1px solid rgba(255,255,255,0.08)' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '6px' }}>
                <strong style={{ color: '#38bdf8', fontSize: '0.9rem' }}>Google AI Lab — $165,000 CTC</strong>
                <span style={{ color: '#10b981', fontWeight: 700, fontSize: '0.8rem' }}>Tier 1 Super Dream</span>
              </div>
              <div style={{ height: '8px', width: '100%', background: 'rgba(255,255,255,0.1)', borderRadius: '4px', overflow: 'hidden', display: 'flex' }}>
                <div style={{ width: '60%', background: '#38bdf8' }} title="Base: $100k" />
                <div style={{ width: '25%', background: '#a855f7' }} title="RSU Stocks: $40k" />
                <div style={{ width: '15%', background: '#10b981' }} title="Bonus: $25k" />
              </div>
              <div style={{ display: 'flex', gap: '12px', fontSize: '0.7rem', color: '#94a3b8', marginTop: '6px' }}>
                <span style={{ color: '#38bdf8' }}>■ Base Salary: $100,000</span>
                <span style={{ color: '#a855f7' }}>■ RSUs (4 Yrs): $40,000</span>
                <span style={{ color: '#10b981' }}>■ Joining Bonus: $25,000</span>
              </div>
            </div>

            {/* Recruiter 2 */}
            <div style={{ padding: '1rem', background: 'rgba(15,23,42,0.8)', borderRadius: '10px', border: '1px solid rgba(255,255,255,0.08)' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '6px' }}>
                <strong style={{ color: '#a855f7', fontSize: '0.9rem' }}>Microsoft Azure — $140,000 CTC</strong>
                <span style={{ color: '#a855f7', fontWeight: 700, fontSize: '0.8rem' }}>Dream Offer</span>
              </div>
              <div style={{ height: '8px', width: '100%', background: 'rgba(255,255,255,0.1)', borderRadius: '4px', overflow: 'hidden', display: 'flex' }}>
                <div style={{ width: '65%', background: '#38bdf8' }} title="Base: $90k" />
                <div style={{ width: '20%', background: '#a855f7' }} title="Stocks: $30k" />
                <div style={{ width: '15%', background: '#10b981' }} title="Bonus: $20k" />
              </div>
              <div style={{ display: 'flex', gap: '12px', fontSize: '0.7rem', color: '#94a3b8', marginTop: '6px' }}>
                <span style={{ color: '#38bdf8' }}>■ Base Salary: $90,000</span>
                <span style={{ color: '#a855f7' }}>■ Stock Grants: $30,000</span>
                <span style={{ color: '#10b981' }}>■ Relocation: $20,000</span>
              </div>
            </div>
          </div>

          <div style={{ display: 'flex', justifyContent: 'flex-end', marginTop: '0.5rem' }}>
            <Button variant="primary" onClick={() => setIsSalaryCompareOpen(false)}>Close Comparison</Button>
          </div>
        </div>
      </Modal>

      {/* Feature 26: Alumni Career Mentorship & Referral Booking Modal */}
      <Modal
        isOpen={isAlumniModalOpen}
        onClose={() => setIsAlumniModalOpen(false)}
        title="Verified University Alumni Mentors & Referral Network"
      >
        <div style={{ display: 'flex', flexDirection: 'column', gap: '1.25rem' }}>
          <div style={{ fontSize: '0.85rem', color: '#94a3b8' }}>
            Connect with UniSphere graduates for 1-on-1 resume reviews, mock interviews, and internal employee referrals:
          </div>

          <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
            {/* Mentor 1 */}
            <div style={{ padding: '0.85rem 1rem', background: 'rgba(56,189,248,0.1)', border: '1px solid rgba(56,189,248,0.2)', borderRadius: '10px', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <div>
                <strong style={{ color: '#f8fafc', fontSize: '0.9rem' }}>Elena Rostova (Senior AI Staff Engineer @ Google)</strong>
                <div style={{ fontSize: '0.75rem', color: '#94a3b8' }}>Class of 2022 • Offers: Mock Coding Interview & Internal Job Referral</div>
              </div>
              <Button variant="primary" size="sm" icon={<Calendar size={14} />} onClick={() => showToast('Booked 1-on-1 mentorship session with Elena Rostova!', 'success')}>
                Book Session
              </Button>
            </div>

            {/* Mentor 2 */}
            <div style={{ padding: '0.85rem 1rem', background: 'rgba(168,85,247,0.1)', border: '1px solid rgba(168,85,247,0.2)', borderRadius: '10px', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <div>
                <strong style={{ color: '#f8fafc', fontSize: '0.9rem' }}>Kevin Zhang (Cloud Systems Lead @ Microsoft)</strong>
                <div style={{ fontSize: '0.75rem', color: '#94a3b8' }}>Class of 2021 • Offers: Resume Critique & Azure Architecture Guidance</div>
              </div>
              <Button variant="outline" size="sm" icon={<Calendar size={14} />} onClick={() => showToast('Booked 1-on-1 mentorship session with Kevin Zhang!', 'success')}>
                Book Session
              </Button>
            </div>
          </div>

          <div style={{ display: 'flex', justifyContent: 'flex-end', marginTop: '0.5rem' }}>
            <Button variant="primary" onClick={() => setIsAlumniModalOpen(false)}>Done</Button>
          </div>
        </div>
      </Modal>

      {/* Feature 17: Mock AI Interview Simulator Modal */}
      <Modal
        isOpen={isMockInterviewOpen}
        onClose={() => setIsMockInterviewOpen(false)}
        title="UniSphere AI Technical Mock Interview Simulator"
      >
        <div style={{ display: 'flex', flexDirection: 'column', gap: '1.25rem' }}>
          <div style={{ padding: '1rem', background: 'rgba(168,85,247,0.1)', borderRadius: '10px', border: '1px solid rgba(168,85,247,0.3)', display: 'flex', alignItems: 'center', gap: '10px' }}>
            <Bot size={24} style={{ color: '#c084fc' }} />
            <div style={{ fontSize: '0.85rem', color: '#cbd5e1' }}>
              <strong style={{ color: '#c084fc' }}>Interactive AI Interviewer:</strong> Practice live voice coding challenges, system design scenarios, and behavioral questions with instant feedback scoring.
            </div>
          </div>

          <Button variant="primary" onClick={() => { showToast('Launched AI Technical Interview session for System Design!', 'success'); setIsMockInterviewOpen(false); }}>
            Start 30-Min AI Coding Session
          </Button>
        </div>
      </Modal>

      {/* Feature 18: Off-Campus Vetted Jobs Portal Modal */}
      <Modal
        isOpen={isOffCampusOpen}
        onClose={() => setIsOffCampusOpen(false)}
        title="Vetted Off-Campus Tech Internships & Opportunities"
      >
        <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
          <div style={{ padding: '0.85rem 1rem', background: 'rgba(56,189,248,0.1)', border: '1px solid rgba(56,189,248,0.2)', borderRadius: '10px', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <div>
              <strong style={{ color: '#38bdf8', fontSize: '0.9rem' }}>OpenAI Summer Research Fellowship 2026</strong>
              <div style={{ fontSize: '0.75rem', color: '#94a3b8' }}>Remote / San Francisco • $12,000/mo Stipend • Deadline April 15</div>
            </div>
            <Button variant="primary" size="sm" onClick={() => { showToast('Redirecting to OpenAI Application Portal...', 'info'); setIsOffCampusOpen(false); }}>
              Apply Direct
            </Button>
          </div>
        </div>
      </Modal>
    </div>
  );
};
