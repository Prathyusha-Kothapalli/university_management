import React from 'react';
import { CourseOverview } from '../../components/dashboard/CourseOverview';
import { AssignmentSummary } from '../../components/dashboard/AssignmentSummary';
import { UpcomingExams } from '../../components/dashboard/UpcomingExams';
import { ResultsOverview } from '../../components/dashboard/ResultsOverview';

export const ParentAcademicsView: React.FC = () => {
  return (
    <div style={{ padding: '1.75rem', display: 'flex', flexDirection: 'column', gap: '1.5rem', maxWidth: '1400px', margin: '0 auto' }}>
      <div>
        <h1 style={{ fontSize: '1.5rem', fontWeight: 800, color: '#f8fafc', margin: 0 }}>
          Child Academics, Courses & Examinations
        </h1>
        <p style={{ fontSize: '0.85rem', color: '#94a3b8', margin: '4px 0 0 0' }}>
          Detailed curriculum progress, assignment submissions, exam schedules, and transcripts
        </p>
      </div>

      <CourseOverview />
      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1.5rem' }}>
        <AssignmentSummary />
        <UpcomingExams />
      </div>
      <ResultsOverview />
    </div>
  );
};
