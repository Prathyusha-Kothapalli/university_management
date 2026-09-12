import React, { useState } from 'react';
import { Card } from '../../components/Card';
import { AiAttendancePredictor } from '../../components/features/AiAttendancePredictor';
import { AiExamQuestionGenerator } from '../../components/features/AiExamQuestionGenerator';
import { AiFlashcardGenerator } from '../../components/features/AiFlashcardGenerator';
import { AiLabAssistant } from '../../components/features/AiLabAssistant';
import { AiResearchPaperSummarizer } from '../../components/features/AiResearchPaperSummarizer';
import { AiCourseRecommender } from '../../components/features/AiCourseRecommender';
import { AiGPAAdviceEngine } from '../../components/features/AiGPAAdviceEngine';
import { AiVoiceAssistant } from '../../components/features/AiVoiceAssistant';

import { AlumniMentorshipScheduler } from '../../components/features/AlumniMentorshipScheduler';
import { AlumniJobBoard } from '../../components/features/AlumniJobBoard';
import { AlumniDirectory } from '../../components/features/AlumniDirectory';
import { AlumniDonationPortal } from '../../components/features/AlumniDonationPortal';
import { MockInterviewScheduler } from '../../components/features/MockInterviewScheduler';
import { CompanyReviewHub } from '../../components/features/CompanyReviewHub';
import { OfferLetterVault } from '../../components/features/OfferLetterVault';

import { CanteenMealPlanner } from '../../components/features/CanteenMealPlanner';
import { CampusHealthCenter } from '../../components/features/CampusHealthCenter';
import { CampusSecurityEscortService } from '../../components/features/CampusSecurityEscortService';
import { HostelRoommateMatcher } from '../../components/features/HostelRoommateMatcher';
import { LostAndFoundPortal } from '../../components/features/LostAndFoundPortal';
import { HostelTicketManager } from '../../components/features/HostelTicketManager';
import { FacilityReservationModal } from '../../components/features/FacilityReservationModal';

import { CertificateVerificationQR } from '../../components/features/CertificateVerificationQR';
import { ClassroomEquipmentManager } from '../../components/features/ClassroomEquipmentManager';
import { EmergencyBroadcastModal } from '../../components/features/EmergencyBroadcastModal';
import { ExpenditureRefundTracker } from '../../components/features/ExpenditureRefundTracker';
import { VisitorPassModal } from '../../components/features/VisitorPassModal';
import { AuditLogInspector } from '../../components/features/AuditLogInspector';

import { ExamHallTicketGenerator } from '../../components/features/ExamHallTicketGenerator';
import { HackathonLeaderboard } from '../../components/features/HackathonLeaderboard';
import { PeerReviewJournal } from '../../components/features/PeerReviewJournal';
import { DigitalWalletCard } from '../../components/features/DigitalWalletCard';
import { LibrarySeatBooking } from '../../components/features/LibrarySeatBooking';
import { PeerTutoringMarketplace } from '../../components/features/PeerTutoringMarketplace';
import { PlagiarismChecker } from '../../components/features/PlagiarismChecker';
import { StudyPlannerModal } from '../../components/features/StudyPlannerModal';
import { SustainabilityDashboard } from '../../components/features/SustainabilityDashboard';

import { FeeInstallmentCalculator } from '../../components/features/FeeInstallmentCalculator';
import { FeeReminderSettings } from '../../components/features/FeeReminderSettings';
import { GpaSimulator } from '../../components/features/GpaSimulator';
import { GradeDisputeModal } from '../../components/features/GradeDisputeModal';
import { GuestLectureManager } from '../../components/features/GuestLectureManager';
import { PatentFilingManager } from '../../components/features/PatentFilingManager';
import { StartupIncubatorPortal } from '../../components/features/StartupIncubatorPortal';
import { InternshipLogbook } from '../../components/features/InternshipLogbook';
import { CourseFeedbackAnalytics } from '../../components/features/CourseFeedbackAnalytics';
import { DepartmentAnalyticsHub } from '../../components/features/DepartmentAnalyticsHub';
import { DigitalLibraryEbooks } from '../../components/features/DigitalLibraryEbooks';
import { FacultyOfficeHours } from '../../components/features/FacultyOfficeHours';
import { CertificationVault } from '../../components/features/CertificationVault';
import { DataExportCenter } from '../../components/features/DataExportCenter';

import {
  Sparkles,
  Bot,
  Briefcase,
  Building2,
  Award,
  CheckCircle,
  GraduationCap,
  DollarSign,
  BarChart2,
} from 'lucide-react';

export const SmartCampusFeaturesHub: React.FC = () => {
  const [activeCategory, setActiveCategory] = useState<'ai' | 'career' | 'campus' | 'governance' | 'academics' | 'finance' | 'analytics'>('ai');

  return (
    <div style={{ padding: '1.75rem', display: 'flex', flexDirection: 'column', gap: '1.5rem', maxWidth: '1600px', margin: '0 auto' }}>
      {/* Header Banner */}
      <div
        style={{
          background: 'linear-gradient(135deg, rgba(30, 41, 59, 0.95), rgba(15, 23, 42, 0.98))',
          backdropFilter: 'blur(16px)',
          border: '1px solid rgba(168, 85, 247, 0.35)',
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
              background: 'linear-gradient(135deg, #a855f7, #6366f1)',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              color: '#ffffff',
              boxShadow: '0 4px 20px rgba(168, 85, 247, 0.4)',
            }}
          >
            <Sparkles size={32} />
          </div>
          <div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
              <h1 style={{ margin: 0, fontSize: '1.6rem', fontWeight: 800, color: '#f8fafc', letterSpacing: '-0.5px' }}>
                Smart Campus 50 Enterprise Features Suite
              </h1>
              <span
                style={{
                  fontSize: '0.72rem',
                  fontWeight: 700,
                  padding: '3px 10px',
                  borderRadius: '12px',
                  background: 'rgba(168, 85, 247, 0.2)',
                  color: '#c084fc',
                  border: '1px solid rgba(168, 85, 247, 0.3)',
                  display: 'flex',
                  alignItems: 'center',
                  gap: '4px',
                }}
              >
                <CheckCircle size={13} /> All 50 Features Active
              </span>
            </div>
            <p style={{ margin: '4px 0 0 0', fontSize: '0.88rem', color: '#94a3b8' }}>
              Complete Enterprise Smart Campus System — AI Tools, Careers, Facilities, Governance, Academics & Finance
            </p>
          </div>
        </div>
      </div>

      {/* Category Tabs */}
      <div style={{ display: 'flex', gap: '8px', borderBottom: '1px solid rgba(255, 255, 255, 0.08)', paddingBottom: '8px', overflowX: 'auto' }}>
        {[
          { id: 'ai', label: '1. AI & Voice Tools (8)', icon: <Bot size={16} /> },
          { id: 'career', label: '2. Careers & Alumni (7)', icon: <Briefcase size={16} /> },
          { id: 'campus', label: '3. Campus & Living (7)', icon: <Building2 size={16} /> },
          { id: 'governance', label: '4. Operations & Security (6)', icon: <Award size={16} /> },
          { id: 'academics', label: '5. Academics & Learning (9)', icon: <GraduationCap size={16} /> },
          { id: 'finance', label: '6. Finance & Grants (7)', icon: <DollarSign size={16} /> },
          { id: 'analytics', label: '7. Analytics & Export (6)', icon: <BarChart2 size={16} /> },
        ].map((tab) => (
          <button
            key={tab.id}
            onClick={() => setActiveCategory(tab.id as any)}
            style={{
              display: 'flex',
              alignItems: 'center',
              gap: '8px',
              padding: '10px 18px',
              borderRadius: '10px',
              border: activeCategory === tab.id ? '1px solid rgba(168, 85, 247, 0.4)' : '1px solid transparent',
              background: activeCategory === tab.id ? 'rgba(168, 85, 247, 0.2)' : 'transparent',
              color: activeCategory === tab.id ? '#c084fc' : '#94a3b8',
              fontWeight: 600,
              fontSize: '0.875rem',
              cursor: 'pointer',
              whiteSpace: 'nowrap',
            }}
          >
            {tab.icon}
            <span>{tab.label}</span>
          </button>
        ))}
      </div>

      {/* Category 1: AI & Voice Tools */}
      {activeCategory === 'ai' && (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
          <Card title="Feature #1: AI Attendance Risk Predictor"><AiAttendancePredictor /></Card>
          <Card title="Feature #2: AI Exam Question & Quiz Generator"><AiExamQuestionGenerator /></Card>
          <Card title="Feature #3: AI Flashcard Study Generator"><AiFlashcardGenerator /></Card>
          <Card title="Feature #4: AI Lab Assistant & Code Debugger"><AiLabAssistant /></Card>
          <Card title="Feature #5: AI Research Paper Summarizer"><AiResearchPaperSummarizer /></Card>
          <Card title="Feature #6: AI Elective Course Recommender"><AiCourseRecommender /></Card>
          <Card title="Feature #7: AI Target GPA Advice Engine"><AiGPAAdviceEngine /></Card>
          <Card title="Feature #8: AI Voice Assistant Dictation Console"><AiVoiceAssistant /></Card>
        </div>
      )}

      {/* Category 2: Careers & Alumni */}
      {activeCategory === 'career' && (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
          <Card title="Feature #9: Alumni Career Mentorship Scheduler"><AlumniMentorshipScheduler /></Card>
          <Card title="Feature #10: Alumni Job & Referral Board"><AlumniJobBoard /></Card>
          <Card title="Feature #11: Global Alumni Directory"><AlumniDirectory /></Card>
          <Card title="Feature #12: Alumni Endowment & Lab Donation Portal"><AlumniDonationPortal /></Card>
          <Card title="Feature #13: AI Mock Interview Simulator"><MockInterviewScheduler /></Card>
          <Card title="Feature #14: Company Review & Salary Insights"><CompanyReviewHub /></Card>
          <Card title="Feature #15: Placement Offer Letter Vault"><OfferLetterVault /></Card>
        </div>
      )}

      {/* Category 3: Campus & Living */}
      {activeCategory === 'campus' && (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
          <Card title="Feature #16: Canteen Meal Planner & Pre-Order"><CanteenMealPlanner /></Card>
          <Card title="Feature #17: Campus Health Center Tele-Clinic"><CampusHealthCenter /></Card>
          <Card title="Feature #18: Campus Security Night Escort Service"><CampusSecurityEscortService /></Card>
          <Card title="Feature #19: Hostel Roommate Matcher"><HostelRoommateMatcher /></Card>
          <Card title="Feature #20: Campus Lost & Found Desk"><LostAndFoundPortal /></Card>
          <Card title="Feature #21: Hostel Ticket & Helpdesk Manager"><HostelTicketManager /></Card>
          <Card title="Feature #22: Campus Auditorium & Facility Reservation"><FacilityReservationModal /></Card>
        </div>
      )}

      {/* Category 4: Operations & Security */}
      {activeCategory === 'governance' && (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
          <Card title="Feature #23: Blockchain Certificate Verification QR"><CertificateVerificationQR /></Card>
          <Card title="Feature #24: Classroom Equipment Manager"><ClassroomEquipmentManager /></Card>
          <Card title="Feature #25: Expenditure & Grant Refund Tracker"><ExpenditureRefundTracker /></Card>
          <Card title="Feature #26: Visitor QR Gate Pass Generator"><VisitorPassModal /></Card>
          <Card title="Feature #27: Emergency Campus Broadcast System"><EmergencyBroadcastModal /></Card>
          <Card title="Feature #28: Security & Audit Log Inspector"><AuditLogInspector /></Card>
        </div>
      )}

      {/* Category 5: Academics & Learning */}
      {activeCategory === 'academics' && (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
          <Card title="Feature #29: Exam Hall Ticket & Seating Generator"><ExamHallTicketGenerator /></Card>
          <Card title="Feature #30: University Hackathon Live Leaderboard"><HackathonLeaderboard /></Card>
          <Card title="Feature #31: Peer-Reviewed Academic Journal Hub"><PeerReviewJournal /></Card>
          <Card title="Feature #32: Campus Digital Pass & Student Wallet Card"><DigitalWalletCard /></Card>
          <Card title="Feature #33: Library Quiet Seat & Pod Booking"><LibrarySeatBooking /></Card>
          <Card title="Feature #34: Peer-to-Peer Tutoring Marketplace"><PeerTutoringMarketplace /></Card>
          <Card title="Feature #35: AI Code & Document Plagiarism Inspector"><PlagiarismChecker /></Card>
          <Card title="Feature #36: Intelligent Semester Study Planner"><StudyPlannerModal /></Card>
          <Card title="Feature #37: Campus Green Energy & Sustainability Dashboard"><SustainabilityDashboard /></Card>
        </div>
      )}

      {/* Category 6: Finance & Grants */}
      {activeCategory === 'finance' && (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
          <Card title="Feature #38: Semester Fee Installment Calculator"><FeeInstallmentCalculator /></Card>
          <Card title="Feature #39: Automated Fee Payment Reminder Settings"><FeeReminderSettings /></Card>
          <Card title="Feature #40: Graduation Honors & GPA Simulator"><GpaSimulator /></Card>
          <Card title="Feature #41: Grade Dispute & Revaluation Portal"><GradeDisputeModal /></Card>
          <Card title="Feature #42: Visiting Guest Lecture & Seminar Manager"><GuestLectureManager /></Card>
          <Card title="Feature #43: Patent & Innovation Filing Hub"><PatentFilingManager /></Card>
          <Card title="Feature #44: University Startup Incubator Portal"><StartupIncubatorPortal /></Card>
        </div>
      )}

      {/* Category 7: Analytics & System Tools */}
      {activeCategory === 'analytics' && (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
          <Card title="Feature #45: Industrial Internship Training Logbook"><InternshipLogbook /></Card>
          <Card title="Feature #46: Course Feedback Sentiment Analytics"><CourseFeedbackAnalytics /></Card>
          <Card title="Feature #47: Department KPI & Research Analytics Hub"><DepartmentAnalyticsHub /></Card>
          <Card title="Feature #48: Digital E-Book Reader & Annotator"><DigitalLibraryEbooks /></Card>
          <Card title="Feature #49: Faculty Office Hours Booking Desk"><FacultyOfficeHours /></Card>
          <Card title="Feature #50: Micro-Credentials & Skill Badge Vault"><CertificationVault /></Card>
          <Card title="Feature #51: University Data Export & Audit Center"><DataExportCenter /></Card>
        </div>
      )}
    </div>
  );
};

export default SmartCampusFeaturesHub;
