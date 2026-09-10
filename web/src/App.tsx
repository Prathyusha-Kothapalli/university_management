import React from 'react';
import { HashRouter as Router, Routes, Route, Navigate, Outlet } from 'react-router-dom';
import { AuthProvider } from './context/AuthContext';
import { ThemeProvider } from './context/ThemeContext';
import { ToastProvider } from './context/ToastContext';
import { useAuth } from './hooks/useAuth';
import { Navbar } from './components/Navbar';
import { Sidebar } from './components/Sidebar';
import { ToastContainer } from './components/ToastContainer';

// Page Views
import { LoginPage } from './pages/Auth/LoginPage';
import { DashboardPage } from './pages/Dashboard/DashboardPage';
import { AcademicsPage } from './pages/Academics/AcademicsPage';
import { LearningPage } from './pages/Learning/LearningPage';
import { ExamsPage } from './pages/Exams/ExamsPage';
import { FinancePage } from './pages/Finance/FinancePage';
import { LibraryPage } from './pages/Library/LibraryPage';
import { FacilitiesPage } from './pages/Facilities/FacilitiesPage';
import { PlacementsPage } from './pages/Placements/PlacementsPage';
import { AiAssistantPage } from './pages/AI/AiAssistantPage';
import { ProfilePage } from './pages/Profile/ProfilePage';

import { HODDashboard } from './pages/Dashboard/HODDashboard';
import { ParentDashboard } from './pages/Dashboard/ParentDashboard';
import { ParentAcademicsView } from './pages/Parent/ParentAcademicsView';
import { ParentAttendanceView } from './pages/Parent/ParentAttendanceView';
import { ParentFinanceView } from './pages/Parent/ParentFinanceView';
import { ParentServicesView } from './pages/Parent/ParentServicesView';
import { DepartmentOverview } from './pages/Department/DepartmentOverview';
import { DepartmentStudents } from './pages/Department/DepartmentStudents';
import { DepartmentFaculty } from './pages/Department/DepartmentFaculty';
import { DepartmentCourses } from './pages/Department/DepartmentCourses';

// Protected App Layout
const ProtectedLayout: React.FC = () => {
  const { isAuthenticated } = useAuth();

  if (!isAuthenticated) {
    return <Navigate to="/login" replace />;
  }

  return (
    <div style={{ minHeight: '100vh', display: 'flex', flexDirection: 'column', backgroundColor: '#090d16', color: '#f8fafc' }}>
      <Navbar />
      <div style={{ display: 'flex', flex: 1 }}>
        <Sidebar />
        <main style={{ flex: 1, minWidth: 0, overflowX: 'hidden' }}>
          <Outlet />
        </main>
      </div>
      <ToastContainer />
    </div>
  );
};

export const App: React.FC = () => {
  return (
    <AuthProvider>
      <ThemeProvider>
        <ToastProvider>
          <Router>
            <Routes>
              {/* Public Routes */}
              <Route path="/login" element={<LoginPage />} />

              {/* Protected SPA Routes */}
              <Route element={<ProtectedLayout />}>
                <Route path="/dashboard" element={<DashboardPage />} />
                <Route path="/parent/dashboard" element={<ParentDashboard />} />
                <Route path="/parent/student" element={<ParentDashboard />} />
                <Route path="/parent/academics" element={<ParentAcademicsView />} />
                <Route path="/parent/courses" element={<ParentAcademicsView />} />
                <Route path="/parent/attendance" element={<ParentAttendanceView />} />
                <Route path="/parent/assignments" element={<ParentAcademicsView />} />
                <Route path="/parent/exams" element={<ParentAcademicsView />} />
                <Route path="/parent/results" element={<ParentAcademicsView />} />
                <Route path="/parent/transcript" element={<ParentAcademicsView />} />
                <Route path="/parent/fees" element={<ParentFinanceView />} />
                <Route path="/parent/payments" element={<ParentFinanceView />} />
                <Route path="/parent/library" element={<ParentServicesView />} />
                <Route path="/parent/hostel" element={<ParentServicesView />} />
                <Route path="/parent/transport" element={<ParentServicesView />} />
                <Route path="/parent/placements" element={<ParentServicesView />} />
                <Route path="/parent/documents" element={<ParentServicesView />} />
                <Route path="/parent/notifications" element={<ParentDashboard />} />
                <Route path="/parent/ai" element={<AiAssistantPage />} />
                <Route path="/parent/profile" element={<ProfilePage />} />
                <Route path="/hod/dashboard" element={<HODDashboard />} />
                <Route path="/hod/department" element={<DepartmentOverview />} />
                <Route path="/hod/students" element={<DepartmentStudents />} />
                <Route path="/hod/faculty" element={<DepartmentFaculty />} />
                <Route path="/hod/courses" element={<DepartmentCourses />} />
                <Route path="/academics" element={<AcademicsPage />} />
                <Route path="/learning" element={<LearningPage />} />
                <Route path="/exams" element={<ExamsPage />} />
                <Route path="/finance" element={<FinancePage />} />
                <Route path="/library" element={<LibraryPage />} />
                <Route path="/facilities" element={<FacilitiesPage />} />
                <Route path="/placements" element={<PlacementsPage />} />
                <Route path="/ai" element={<AiAssistantPage />} />
                <Route path="/profile" element={<ProfilePage />} />
              </Route>

              {/* Default Fallback Redirect */}
              <Route path="*" element={<Navigate to="/dashboard" replace />} />
            </Routes>
          </Router>
        </ToastProvider>
      </ThemeProvider>
    </AuthProvider>
  );
};

export default App;
