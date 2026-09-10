import React, { useState } from 'react';
import { useAuth } from '../../hooks/useAuth';
import { useToast } from '../../hooks/useToast';
import { HODStatCards } from '../../components/dashboard/HODStatCards';
import { AttendanceAnalytics } from '../../components/dashboard/AttendanceAnalytics';
import { StudentPerformance } from '../../components/dashboard/StudentPerformance';
import { FacultyWorkload } from '../../components/dashboard/FacultyWorkload';
import { AtRiskStudents } from '../../components/dashboard/AtRiskStudents';
import { TodaysSchedule } from '../../components/dashboard/TodaysSchedule';
import { DepartmentNotifications } from '../../components/dashboard/DepartmentNotifications';
import { FacultyLeaveManager } from '../../components/dashboard/FacultyLeaveManager';
import { DepartmentBudgetTracker } from '../../components/dashboard/DepartmentBudgetTracker';
import { SyllabusApprovalMatrix } from '../../components/dashboard/SyllabusApprovalMatrix';
import { ParentAdvisoryManager } from '../../components/dashboard/ParentAdvisoryManager';
import { ResearchPublicationHub } from '../../components/dashboard/ResearchPublicationHub';
import {
  Building2,
  Megaphone,
  Download,
  RefreshCw,
  ShieldCheck,
  LayoutDashboard,
  UserCheck,
  DollarSign,
  Layers,
  Award,
} from 'lucide-react';

export const HODDashboard: React.FC = () => {
  const { user } = useAuth();
  const { showToast } = useToast();
  const [isRefreshing, setIsRefreshing] = useState(false);
  const [activeTab, setActiveTab] = useState<'overview' | 'faculty' | 'finance' | 'academics' | 'research'>('overview');

  const handleExportSummary = () => {
    showToast('Exporting Department Executive Report (PDF/Excel)...', 'info');
    setTimeout(() => {
      showToast('Department Report downloaded successfully!', 'success');
    }, 1200);
  };

  const handleBroadcast = () => {
    showToast('Broadcast Modal opened for Computer Science & Eng. Department', 'info');
  };

  const handleRefresh = () => {
    setIsRefreshing(true);
    showToast('Syncing real-time department metrics from server...', 'info');
    setTimeout(() => {
      setIsRefreshing(false);
      showToast('Department metrics up to date', 'success');
    }, 800);
  };

  return (
    <div style={{ padding: '1.75rem', display: 'flex', flexDirection: 'column', gap: '1.5rem', maxWidth: '1600px', margin: '0 auto' }}>
      {/* HOD Header Banner */}
      <div
        style={{
          background: 'linear-gradient(135deg, rgba(30, 41, 59, 0.9), rgba(15, 23, 42, 0.95))',
          backdropFilter: 'blur(16px)',
          border: '1px solid rgba(56, 189, 248, 0.25)',
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
              background: 'linear-gradient(135deg, #0284c7, #0369a1)',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              boxShadow: '0 4px 16px rgba(2, 132, 199, 0.4)',
            }}
          >
            <Building2 size={30} color="#ffffff" />
          </div>
          <div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
              <span
                style={{
                  backgroundColor: 'rgba(56, 189, 248, 0.15)',
                  color: '#38bdf8',
                  fontSize: '0.75rem',
                  fontWeight: 700,
                  padding: '3px 10px',
                  borderRadius: '20px',
                  border: '1px solid rgba(56, 189, 248, 0.3)',
                  display: 'inline-flex',
                  alignItems: 'center',
                  gap: '4px',
                }}
              >
                <ShieldCheck size={13} /> HOD Portal
              </span>
              <span style={{ fontSize: '0.8rem', color: '#94a3b8' }}>CSE Dept • Code: CSE-01</span>
            </div>
            <h1 style={{ fontSize: '1.65rem', fontWeight: 800, color: '#f8fafc', margin: '6px 0 2px 0' }}>
              Department of Computer Science & Engineering
            </h1>
            <p style={{ fontSize: '0.85rem', color: '#94a3b8', margin: 0 }}>
              Head of Dept: <strong style={{ color: '#f1f5f9' }}>{user?.full_name || 'Dr. Robert Rao'}</strong> | Academic Session 2025-2026 (Odd Sem)
            </p>
          </div>
        </div>

        {/* Quick Action Controls */}
        <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
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
            onClick={handleBroadcast}
            style={{
              backgroundColor: 'rgba(168, 85, 247, 0.15)',
              border: '1px solid rgba(168, 85, 247, 0.3)',
              color: '#c084fc',
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
            <Megaphone size={15} /> Dept Notice
          </button>
          <button
            onClick={handleExportSummary}
            style={{
              backgroundColor: 'rgba(37, 99, 235, 0.2)',
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
        </div>
      </div>

      {/* KPI Metric Cards */}
      <HODStatCards />

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
          <LayoutDashboard size={16} /> Operational Overview
        </button>
        <button
          onClick={() => setActiveTab('faculty')}
          style={{
            backgroundColor: activeTab === 'faculty' ? 'rgba(168, 85, 247, 0.18)' : 'transparent',
            border: activeTab === 'faculty' ? '1px solid rgba(168, 85, 247, 0.3)' : '1px solid transparent',
            color: activeTab === 'faculty' ? '#c084fc' : '#94a3b8',
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
          <UserCheck size={16} /> Faculty & Leave Substitution
        </button>
        <button
          onClick={() => setActiveTab('finance')}
          style={{
            backgroundColor: activeTab === 'finance' ? 'rgba(52, 211, 153, 0.18)' : 'transparent',
            border: activeTab === 'finance' ? '1px solid rgba(52, 211, 153, 0.3)' : '1px solid transparent',
            color: activeTab === 'finance' ? '#34d399' : '#94a3b8',
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
          <DollarSign size={16} /> Budget & Grants
        </button>
        <button
          onClick={() => setActiveTab('academics')}
          style={{
            backgroundColor: activeTab === 'academics' ? 'rgba(245, 158, 11, 0.18)' : 'transparent',
            border: activeTab === 'academics' ? '1px solid rgba(245, 158, 11, 0.3)' : '1px solid transparent',
            color: activeTab === 'academics' ? '#f59e0b' : '#94a3b8',
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
          <Layers size={16} /> Curriculum & CO-PO
        </button>
        <button
          onClick={() => setActiveTab('research')}
          style={{
            backgroundColor: activeTab === 'research' ? 'rgba(244, 63, 94, 0.18)' : 'transparent',
            border: activeTab === 'research' ? '1px solid rgba(244, 63, 94, 0.3)' : '1px solid transparent',
            color: activeTab === 'research' ? '#f43f5e' : '#94a3b8',
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
          <Award size={16} /> Research & Parent Advisory
        </button>
      </div>

      {/* Tab Content Display */}
      {activeTab === 'overview' && (
        <div style={{ display: 'grid', gridTemplateColumns: '2fr 1fr', gap: '1.5rem' }}>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
            <AttendanceAnalytics />
            <StudentPerformance />
            <FacultyWorkload />
          </div>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
            <AtRiskStudents />
            <TodaysSchedule />
            <DepartmentNotifications />
          </div>
        </div>
      )}

      {activeTab === 'faculty' && (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
          <FacultyLeaveManager />
          <FacultyWorkload />
        </div>
      )}

      {activeTab === 'finance' && (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
          <DepartmentBudgetTracker />
        </div>
      )}

      {activeTab === 'academics' && (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
          <SyllabusApprovalMatrix />
          <AttendanceAnalytics />
        </div>
      )}

      {activeTab === 'research' && (
        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1.5rem' }}>
          <ResearchPublicationHub />
          <ParentAdvisoryManager />
        </div>
      )}
    </div>
  );
};
