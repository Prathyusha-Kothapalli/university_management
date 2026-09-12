import React from 'react';
import { AttendanceOverview } from '../../components/dashboard/AttendanceOverview';

export const ParentAttendanceView: React.FC = () => {
  return (
    <div style={{ padding: '1.75rem', display: 'flex', flexDirection: 'column', gap: '1.5rem', maxWidth: '1400px', margin: '0 auto' }}>
      <div>
        <h1 style={{ fontSize: '1.5rem', fontWeight: 800, color: '#f8fafc', margin: 0 }}>
          Student Attendance & Session Logs
        </h1>
        <p style={{ fontSize: '0.85rem', color: '#94a3b8', margin: '4px 0 0 0' }}>
          Course-wise real-time attendance tracking and session statistics
        </p>
      </div>

      <AttendanceOverview />
    </div>
  );
};
