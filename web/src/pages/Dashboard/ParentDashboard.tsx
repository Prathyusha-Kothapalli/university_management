import React, { useState } from 'react';
import { useAuth } from '../../hooks/useAuth';
import { useToast } from '../../hooks/useToast';
import { ParentStatCards } from '../../components/dashboard/ParentStatCards';
import { StudentProfileCard } from '../../components/dashboard/StudentProfileCard';
import { AttendanceOverview } from '../../components/dashboard/AttendanceOverview';
import { AcademicPerformance } from '../../components/dashboard/AcademicPerformance';
import { CourseOverview } from '../../components/dashboard/CourseOverview';
import { AssignmentSummary } from '../../components/dashboard/AssignmentSummary';
import { UpcomingExams } from '../../components/dashboard/UpcomingExams';
import { ResultsOverview } from '../../components/dashboard/ResultsOverview';
import { FeeSummary } from '../../components/dashboard/FeeSummary';
import { LibrarySummary } from '../../components/dashboard/LibrarySummary';
import { HostelSummary } from '../../components/dashboard/HostelSummary';
import { TransportSummary } from '../../components/dashboard/TransportSummary';
import { PlacementSummary } from '../../components/dashboard/PlacementSummary';
import { NotificationSummary } from '../../components/dashboard/NotificationSummary';
import { DocumentSummary } from '../../components/dashboard/DocumentSummary';
import { ParentAICopilotCard } from '../../components/dashboard/ParentAICopilotCard';
import { ParentPTMManager } from '../../components/dashboard/ParentPTMManager';
import { ParentPaymentModal } from '../../components/dashboard/ParentPaymentModal';
import { ParentFacultyMessaging } from '../../components/dashboard/ParentFacultyMessaging';
import {
  Users,
  ShieldCheck,
  RefreshCw,
  Download,
  CreditCard,
  LayoutDashboard,
  GraduationCap,
  Calendar,
  DollarSign,
  MessageSquare,
  Building2,
} from 'lucide-react';

export const ParentDashboard: React.FC = () => {
  const { user } = useAuth();
  const { showToast } = useToast();
  const [isRefreshing, setIsRefreshing] = useState(false);
  const [isPaymentModalOpen, setIsPaymentModalOpen] = useState(false);
  const [selectedStudent, setSelectedStudent] = useState<'Rahul Kumar' | 'Ananya Kumar'>('Rahul Kumar');
  const [activeTab, setActiveTab] = useState<'overview' | 'attendance' | 'academics' | 'fees' | 'ptm' | 'services'>('overview');

  const handleStudentSwitch = (studentName: 'Rahul Kumar' | 'Ananya Kumar') => {
    setSelectedStudent(studentName);
    showToast(`Switched active student view to ${studentName}`, 'info');
  };

  const handleRefresh = () => {
    setIsRefreshing(true);
    showToast('Syncing real-time student progress & attendance records...', 'info');
    setTimeout(() => {
      setIsRefreshing(false);
      showToast('Student record updated', 'success');
    }, 800);
  };

  const handleExportPDF = () => {
    showToast(`Exporting official Academic Progress Report PDF for ${selectedStudent}...`, 'info');
    setTimeout(() => {
      showToast('Report PDF downloaded successfully!', 'success');
    }, 1200);
  };

  const studentDetails = selectedStudent === 'Rahul Kumar'
    ? { name: 'Rahul Kumar', id: 'STU-2026-001', program: 'B.Tech Computer Science', dept: 'Computer Science & Engineering', sem: 'Semester 5', standing: 'Good', gpa: 8.42, attendance: 86.4, fees: 18500 }
    : { name: 'Ananya Kumar', id: 'STU-2026-042', program: 'B.Tech AI & Data Science', dept: 'Computer Science & Engineering', sem: 'Semester 3', standing: 'Excellent', gpa: 9.15, attendance: 94.2, fees: 0 };

  return (
    <div style={{ padding: '1.75rem', display: 'flex', flexDirection: 'column', gap: '1.5rem', maxWidth: '1600px', margin: '0 auto' }}>
      {/* Top Welcome Banner */}
      <div
        style={{
          background: 'linear-gradient(135deg, rgba(30, 41, 59, 0.9), rgba(15, 23, 42, 0.95))',
          backdropFilter: 'blur(16px)',
          border: '1px solid rgba(168, 85, 247, 0.25)',
          borderRadius: '20px',
          padding: '1.75rem',
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          flexWrap: 'wrap',
          gap: '1.25rem',
          boxShadow: '0 8px 32px rgba(0, 0, 0, 0.3)',
        }}
      >
        <div style={{ display: 'flex', alignItems: 'center', gap: '1.25rem' }}>
          <div
            style={{
              width: '60px',
              height: '60px',
              borderRadius: '16px',
              background: 'linear-gradient(135deg, #a855f7, #6366f1)',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              boxShadow: '0 4px 16px rgba(168, 85, 247, 0.4)',
            }}
          >
            <Users size={30} color="#ffffff" />
          </div>
          <div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
              <span
                style={{
                  backgroundColor: 'rgba(168, 85, 247, 0.15)',
                  color: '#c084fc',
                  fontSize: '0.75rem',
                  fontWeight: 700,
                  padding: '3px 10px',
                  borderRadius: '20px',
                  border: '1px solid rgba(168, 85, 247, 0.3)',
                  display: 'inline-flex',
                  alignItems: 'center',
                  gap: '4px',
                }}
              >
                <ShieldCheck size={13} /> Parent & Guardian Portal
              </span>
              <span style={{ fontSize: '0.8rem', color: '#94a3b8' }}>Authorized Student Monitoring</span>
            </div>
            <h1 style={{ fontSize: '1.65rem', fontWeight: 800, color: '#f8fafc', margin: '6px 0 2px 0' }}>
              Good Morning, {user?.full_name || 'Mr. Ramesh Kumar'} 👋
            </h1>
            <p style={{ fontSize: '0.85rem', color: '#cbd5e1', margin: 0 }}>
              Here's an overview of <strong style={{ color: '#38bdf8' }}>{studentDetails.name}</strong>'s academic progress, attendance, and fee status.
            </p>
          </div>
        </div>

        {/* Action Controls */}
        <div style={{ display: 'flex', alignItems: 'center', gap: '10px', flexWrap: 'wrap' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '6px', backgroundColor: 'rgba(15, 23, 42, 0.8)', border: '1px solid rgba(255, 255, 255, 0.12)', borderRadius: '10px', padding: '6px 12px' }}>
            <span style={{ fontSize: '0.78rem', color: '#94a3b8' }}>Student:</span>
            <select
              value={selectedStudent}
              onChange={(e) => handleStudentSwitch(e.target.value as 'Rahul Kumar' | 'Ananya Kumar')}
              style={{
                backgroundColor: 'transparent',
                border: 'none',
                color: '#f8fafc',
                fontWeight: 700,
                fontSize: '0.825rem',
                outline: 'none',
                cursor: 'pointer',
              }}
            >
              <option value="Rahul Kumar" style={{ backgroundColor: '#0f172a' }}>Rahul Kumar (Sem 5)</option>
              <option value="Ananya Kumar" style={{ backgroundColor: '#0f172a' }}>Ananya Kumar (Sem 3)</option>
            </select>
          </div>

          <button
            onClick={handleRefresh}
            disabled={isRefreshing}
            style={{
              backgroundColor: 'rgba(255, 255, 255, 0.05)',
              border: '1px solid rgba(255, 255, 255, 0.12)',
              color: '#e2e8f0',
              borderRadius: '10px',
              padding: '8px 14px',
              fontSize: '0.825rem',
              fontWeight: 600,
              cursor: 'pointer',
              display: 'flex',
              alignItems: 'center',
              gap: '6px',
            }}
          >
            <RefreshCw size={15} /> Refresh
          </button>
          <button
            onClick={handleExportPDF}
            style={{
              backgroundColor: 'rgba(56, 189, 248, 0.15)',
              border: '1px solid rgba(56, 189, 248, 0.3)',
              color: '#38bdf8',
              borderRadius: '10px',
              padding: '8px 14px',
              fontSize: '0.825rem',
              fontWeight: 600,
              cursor: 'pointer',
              display: 'flex',
              alignItems: 'center',
              gap: '6px',
            }}
          >
            <Download size={15} /> Export Report
          </button>

          <button
            onClick={() => setIsPaymentModalOpen(true)}
            style={{
              backgroundColor: '#2563eb',
              border: 'none',
              color: '#ffffff',
              borderRadius: '10px',
              padding: '8px 14px',
              fontSize: '0.825rem',
              fontWeight: 700,
              cursor: 'pointer',
              display: 'flex',
              alignItems: 'center',
              gap: '6px',
              boxShadow: '0 4px 14px rgba(37, 99, 235, 0.4)',
            }}
          >
            <CreditCard size={15} /> Pay Fees
          </button>
        </div>
      </div>

      {/* Prominent Student Profile Card */}
      <StudentProfileCard
        studentName={studentDetails.name}
        studentId={studentDetails.id}
        program={studentDetails.program}
        department={studentDetails.dept}
        semester={studentDetails.sem}
        academicStanding={studentDetails.standing}
      />

      {/* KPI Metric Cards */}
      <ParentStatCards
        attendanceRate={studentDetails.attendance}
        cgpa={studentDetails.gpa}
        outstandingFees={studentDetails.fees}
      />

      {/* View Section Tabs */}
      <div
        style={{
          display: 'flex',
          gap: '8px',
          borderBottom: '1px solid rgba(255, 255, 255, 0.08)',
          paddingBottom: '8px',
          overflowX: 'auto',
        }}
      >
        <button
          onClick={() => setActiveTab('overview')}
          style={{
            backgroundColor: activeTab === 'overview' ? 'rgba(56, 189, 248, 0.18)' : 'transparent',
            border: activeTab === 'overview' ? '1px solid rgba(56, 189, 248, 0.3)' : '1px solid transparent',
            color: activeTab === 'overview' ? '#38bdf8' : '#94a3b8',
            borderRadius: '10px',
            padding: '8px 14px',
            fontSize: '0.85rem',
            fontWeight: 600,
            cursor: 'pointer',
            display: 'flex',
            alignItems: 'center',
            gap: '6px',
          }}
        >
          <LayoutDashboard size={16} /> Overview & Profile
        </button>
        <button
          onClick={() => setActiveTab('attendance')}
          style={{
            backgroundColor: activeTab === 'attendance' ? 'rgba(52, 211, 153, 0.18)' : 'transparent',
            border: activeTab === 'attendance' ? '1px solid rgba(52, 211, 153, 0.3)' : '1px solid transparent',
            color: activeTab === 'attendance' ? '#34d399' : '#94a3b8',
            borderRadius: '10px',
            padding: '8px 14px',
            fontSize: '0.85rem',
            fontWeight: 600,
            cursor: 'pointer',
            display: 'flex',
            alignItems: 'center',
            gap: '6px',
          }}
        >
          <Calendar size={16} /> Attendance Analytics
        </button>
        <button
          onClick={() => setActiveTab('academics')}
          style={{
            backgroundColor: activeTab === 'academics' ? 'rgba(168, 85, 247, 0.18)' : 'transparent',
            border: activeTab === 'academics' ? '1px solid rgba(168, 85, 247, 0.3)' : '1px solid transparent',
            color: activeTab === 'academics' ? '#c084fc' : '#94a3b8',
            borderRadius: '10px',
            padding: '8px 14px',
            fontSize: '0.85rem',
            fontWeight: 600,
            cursor: 'pointer',
            display: 'flex',
            alignItems: 'center',
            gap: '6px',
          }}
        >
          <GraduationCap size={16} /> Academics & Exams
        </button>
        <button
          onClick={() => setActiveTab('fees')}
          style={{
            backgroundColor: activeTab === 'fees' ? 'rgba(245, 158, 11, 0.18)' : 'transparent',
            border: activeTab === 'fees' ? '1px solid rgba(245, 158, 11, 0.3)' : '1px solid transparent',
            color: activeTab === 'fees' ? '#f59e0b' : '#94a3b8',
            borderRadius: '10px',
            padding: '8px 14px',
            fontSize: '0.85rem',
            fontWeight: 600,
            cursor: 'pointer',
            display: 'flex',
            alignItems: 'center',
            gap: '6px',
          }}
        >
          <DollarSign size={16} /> Fees & Payment Gateway
        </button>
        <button
          onClick={() => setActiveTab('ptm')}
          style={{
            backgroundColor: activeTab === 'ptm' ? 'rgba(244, 63, 94, 0.18)' : 'transparent',
            border: activeTab === 'ptm' ? '1px solid rgba(244, 63, 94, 0.3)' : '1px solid transparent',
            color: activeTab === 'ptm' ? '#f43f5e' : '#94a3b8',
            borderRadius: '10px',
            padding: '8px 14px',
            fontSize: '0.85rem',
            fontWeight: 600,
            cursor: 'pointer',
            display: 'flex',
            alignItems: 'center',
            gap: '6px',
          }}
        >
          <MessageSquare size={16} /> PTM & Faculty Chat
        </button>
        <button
          onClick={() => setActiveTab('services')}
          style={{
            backgroundColor: activeTab === 'services' ? 'rgba(14, 165, 233, 0.18)' : 'transparent',
            border: activeTab === 'services' ? '1px solid rgba(14, 165, 233, 0.3)' : '1px solid transparent',
            color: activeTab === 'services' ? '#38bdf8' : '#94a3b8',
            borderRadius: '10px',
            padding: '8px 14px',
            fontSize: '0.85rem',
            fontWeight: 600,
            cursor: 'pointer',
            display: 'flex',
            alignItems: 'center',
            gap: '6px',
          }}
        >
          <Building2 size={16} /> Campus Services & Vault
        </button>
      </div>

      {/* Tab Content */}
      {activeTab === 'overview' && (
        <div style={{ display: 'grid', gridTemplateColumns: '2fr 1fr', gap: '1.5rem' }}>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
            <AttendanceOverview />
            <AcademicPerformance />
            <CourseOverview />
            <AssignmentSummary />
            <ResultsOverview />
            <FeeSummary />
          </div>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
            <ParentAICopilotCard />
            <UpcomingExams />
            <NotificationSummary />
            <LibrarySummary />
            <HostelSummary />
            <TransportSummary />
            <PlacementSummary />
            <DocumentSummary />
          </div>
        </div>
      )}

      {activeTab === 'attendance' && (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
          <AttendanceOverview />
        </div>
      )}

      {activeTab === 'academics' && (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
          <CourseOverview />
          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1.5rem' }}>
            <AssignmentSummary />
            <UpcomingExams />
          </div>
          <ResultsOverview />
        </div>
      )}

      {activeTab === 'fees' && (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
          <FeeSummary />
        </div>
      )}

      {activeTab === 'ptm' && (
        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1.5rem' }}>
          <ParentPTMManager />
          <ParentFacultyMessaging />
        </div>
      )}

      {activeTab === 'services' && (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1.5rem' }}>
            <LibrarySummary />
            <PlacementSummary />
          </div>
          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1.5rem' }}>
            <HostelSummary />
            <TransportSummary />
          </div>
          <DocumentSummary />
        </div>
      )}

      {/* Online Fee Payment Modal */}
      <ParentPaymentModal
        isOpen={isPaymentModalOpen}
        onClose={() => setIsPaymentModalOpen(false)}
      />
    </div>
  );
};
