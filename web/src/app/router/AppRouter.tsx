import React from 'react';
import { Routes, Route, Navigate } from 'react-router-dom';
import { ProtectedRoute } from './ProtectedRoute';
import { RoleRoute } from './RoleRoute';

// Layouts
import { AuthLayout } from '../../layouts/AuthLayout';
import { DashboardLayout } from '../../layouts/DashboardLayout';
import { ErrorLayout } from '../../layouts/ErrorLayout';

// Auth Pages
import { Login } from '../../pages/auth/Login';
import { ForgotPassword } from '../../pages/auth/ForgotPassword';
import { ResetPassword } from '../../pages/auth/ResetPassword';

// Error & Profile Pages
import { NotFound } from '../../pages/errors/NotFound';
import { Unauthorized } from '../../pages/errors/Unauthorized';
import { Profile } from '../../pages/profile/Profile';

// Dashboards (27 Roles)
import { SuperAdminDashboard } from '../../dashboards/super-admin/SuperAdminDashboard';
import { ManagementDashboard } from '../../dashboards/management/ManagementDashboard';
import { PrincipalDashboard } from '../../dashboards/principal/PrincipalDashboard';
import { DeanDashboard } from '../../dashboards/dean/DeanDashboard';
import { HodDashboard } from '../../dashboards/hod/HodDashboard';
import { FacultyDashboard } from '../../dashboards/faculty/FacultyDashboard';
import { StudentDashboard } from '../../dashboards/student/StudentDashboard';
import { ParentDashboard } from '../../dashboards/parent/ParentDashboard';
import { AdmissionsDashboard } from '../../dashboards/admissions/AdmissionsDashboard';
import { ExaminationDashboard } from '../../dashboards/examination/ExaminationDashboard';
import { FinanceDashboard } from '../../dashboards/finance/FinanceDashboard';
import { HrDashboard } from '../../dashboards/hr/HrDashboard';
import { LibraryDashboard } from '../../dashboards/library/LibraryDashboard';
import { HostelTransportDashboard } from '../../dashboards/hostel-transport/HostelTransportDashboard';
import { PlacementAlumniDashboard } from '../../dashboards/placement-alumni/PlacementAlumniDashboard';
import { LmsDashboard } from '../../dashboards/lms/LmsDashboard';
import { AttendanceAnalyticsDashboard } from '../../dashboards/attendance-analytics/AttendanceAnalyticsDashboard';
import { AiIntelligenceDashboard } from '../../dashboards/ai-intelligence/AiIntelligenceDashboard';
import { ResearchDashboard } from '../../dashboards/research/ResearchDashboard';
import { InventoryDashboard } from '../../dashboards/inventory/InventoryDashboard';
import { AccreditationDashboard } from '../../dashboards/accreditation/AccreditationDashboard';
import { HelpdeskDashboard } from '../../dashboards/helpdesk/HelpdeskDashboard';
import { GrievanceDashboard } from '../../dashboards/grievance/GrievanceDashboard';
import { SecurityDashboard } from '../../dashboards/security/SecurityDashboard';
import { MonitoringDashboard } from '../../dashboards/monitoring/MonitoringDashboard';
import { TenantManagementDashboard } from '../../dashboards/tenant-management/TenantManagementDashboard';
import { BiDashboard } from '../../dashboards/bi/BiDashboard';

export const AppRouter: React.FC = () => {
  return (
    <Routes>
      {/* Public Auth Routes */}
      <Route element={<AuthLayout />}>
        <Route path="/login" element={<Login />} />
        <Route path="/forgot-password" element={<ForgotPassword />} />
        <Route path="/reset-password" element={<ResetPassword />} />
      </Route>

      {/* Protected Dashboard Routes */}
      <Route
        element={
          <ProtectedRoute>
            <DashboardLayout />
          </ProtectedRoute>
        }
      >
        {/* Default Landing Redirect */}
        <Route path="/" element={<Navigate to="/student/dashboard" replace />} />
        <Route path="/dashboard" element={<Navigate to="/student/dashboard" replace />} />
        <Route path="/profile" element={<Profile />} />

        {/* 27 Role Dashboard Routes with RBAC protection */}
        <Route
          path="/super-admin/dashboard"
          element={
            <RoleRoute allowedRoles={['SUPER_ADMIN']}>
              <SuperAdminDashboard />
            </RoleRoute>
          }
        />
        <Route
          path="/management/dashboard"
          element={
            <RoleRoute allowedRoles={['SUPER_ADMIN', 'MANAGEMENT']}>
              <ManagementDashboard />
            </RoleRoute>
          }
        />
        <Route
          path="/principal/dashboard"
          element={
            <RoleRoute allowedRoles={['SUPER_ADMIN', 'PRINCIPAL']}>
              <PrincipalDashboard />
            </RoleRoute>
          }
        />
        <Route
          path="/dean/dashboard"
          element={
            <RoleRoute allowedRoles={['SUPER_ADMIN', 'DEAN']}>
              <DeanDashboard />
            </RoleRoute>
          }
        />
        <Route
          path="/hod/dashboard"
          element={
            <RoleRoute allowedRoles={['SUPER_ADMIN', 'HOD']}>
              <HodDashboard />
            </RoleRoute>
          }
        />
        <Route
          path="/faculty/dashboard"
          element={
            <RoleRoute allowedRoles={['SUPER_ADMIN', 'FACULTY', 'HOD']}>
              <FacultyDashboard />
            </RoleRoute>
          }
        />
        <Route
          path="/student/dashboard"
          element={
            <RoleRoute allowedRoles={['SUPER_ADMIN', 'STUDENT']}>
              <StudentDashboard />
            </RoleRoute>
          }
        />
        <Route
          path="/parent/dashboard"
          element={
            <RoleRoute allowedRoles={['SUPER_ADMIN', 'PARENT']}>
              <ParentDashboard />
            </RoleRoute>
          }
        />
        <Route
          path="/admissions/dashboard"
          element={
            <RoleRoute allowedRoles={['SUPER_ADMIN', 'ADMISSION_TEAM']}>
              <AdmissionsDashboard />
            </RoleRoute>
          }
        />
        <Route
          path="/examination/dashboard"
          element={
            <RoleRoute allowedRoles={['SUPER_ADMIN', 'EXAM_CELL', 'PRINCIPAL', 'HOD', 'FACULTY', 'STUDENT', 'PARENT']}>
              <ExaminationDashboard />
            </RoleRoute>
          }
        />
        <Route
          path="/finance/dashboard"
          element={
            <RoleRoute allowedRoles={['SUPER_ADMIN', 'FINANCE', 'MANAGEMENT', 'PRINCIPAL', 'STUDENT', 'PARENT']}>
              <FinanceDashboard />
            </RoleRoute>
          }
        />
        <Route
          path="/hr/dashboard"
          element={
            <RoleRoute allowedRoles={['SUPER_ADMIN', 'HR', 'PRINCIPAL']}>
              <HrDashboard />
            </RoleRoute>
          }
        />
        <Route
          path="/library/dashboard"
          element={
            <RoleRoute allowedRoles={['SUPER_ADMIN', 'LIBRARIAN', 'STUDENT', 'FACULTY']}>
              <LibraryDashboard />
            </RoleRoute>
          }
        />
        <Route
          path="/hostel-transport/dashboard"
          element={
            <RoleRoute allowedRoles={['SUPER_ADMIN', 'CAMPUS_OPERATIONS', 'STUDENT']}>
              <HostelTransportDashboard />
            </RoleRoute>
          }
        />
        <Route
          path="/placement-alumni/dashboard"
          element={
            <RoleRoute allowedRoles={['SUPER_ADMIN', 'PLACEMENT_TEAM', 'STUDENT', 'MANAGEMENT']}>
              <PlacementAlumniDashboard />
            </RoleRoute>
          }
        />
        <Route
          path="/lms/dashboard"
          element={
            <RoleRoute allowedRoles={['SUPER_ADMIN', 'LMS_ADMIN', 'FACULTY', 'STUDENT']}>
              <LmsDashboard />
            </RoleRoute>
          }
        />
        <Route
          path="/attendance-analytics/dashboard"
          element={
            <RoleRoute allowedRoles={['SUPER_ADMIN', 'PRINCIPAL', 'HOD', 'FACULTY', 'STUDENT', 'PARENT']}>
              <AttendanceAnalyticsDashboard />
            </RoleRoute>
          }
        />
        <Route
          path="/ai-intelligence/dashboard"
          element={
            <RoleRoute allowedRoles={['SUPER_ADMIN', 'BI_ANALYST', 'FACULTY', 'STUDENT']}>
              <AiIntelligenceDashboard />
            </RoleRoute>
          }
        />
        <Route
          path="/research/dashboard"
          element={
            <RoleRoute allowedRoles={['SUPER_ADMIN', 'RESEARCH_TEAM', 'DEAN', 'MANAGEMENT']}>
              <ResearchDashboard />
            </RoleRoute>
          }
        />
        <Route
          path="/inventory/dashboard"
          element={
            <RoleRoute allowedRoles={['SUPER_ADMIN', 'INVENTORY_MANAGER', 'CAMPUS_OPERATIONS']}>
              <InventoryDashboard />
            </RoleRoute>
          }
        />
        <Route
          path="/accreditation/dashboard"
          element={
            <RoleRoute allowedRoles={['SUPER_ADMIN', 'COMPLIANCE_OFFICER', 'PRINCIPAL', 'MANAGEMENT']}>
              <AccreditationDashboard />
            </RoleRoute>
          }
        />
        <Route
          path="/helpdesk/dashboard"
          element={
            <RoleRoute allowedRoles={['SUPER_ADMIN', 'HELPDESK_AGENT', 'STUDENT', 'FACULTY']}>
              <HelpdeskDashboard />
            </RoleRoute>
          }
        />
        <Route
          path="/grievance/dashboard"
          element={
            <RoleRoute allowedRoles={['SUPER_ADMIN', 'GRIEVANCE_OFFICER']}>
              <GrievanceDashboard />
            </RoleRoute>
          }
        />
        <Route
          path="/security/dashboard"
          element={
            <RoleRoute allowedRoles={['SUPER_ADMIN', 'SECURITY_ADMIN']}>
              <SecurityDashboard />
            </RoleRoute>
          }
        />
        <Route
          path="/monitoring/dashboard"
          element={
            <RoleRoute allowedRoles={['SUPER_ADMIN', 'SYSTEM_ADMIN']}>
              <MonitoringDashboard />
            </RoleRoute>
          }
        />
        <Route
          path="/tenant-management/dashboard"
          element={
            <RoleRoute allowedRoles={['SUPER_ADMIN', 'TENANT_ADMIN']}>
              <TenantManagementDashboard />
            </RoleRoute>
          }
        />
        <Route
          path="/bi/dashboard"
          element={
            <RoleRoute allowedRoles={['SUPER_ADMIN', 'BI_ANALYST', 'MANAGEMENT']}>
              <BiDashboard />
            </RoleRoute>
          }
        />
      </Route>

      {/* Error & Catch-all Routes */}
      <Route element={<ErrorLayout />}>
        <Route path="/errors/403" element={<Unauthorized />} />
        <Route path="/errors/404" element={<NotFound />} />
        <Route path="*" element={<NotFound />} />
      </Route>
    </Routes>
  );
};
