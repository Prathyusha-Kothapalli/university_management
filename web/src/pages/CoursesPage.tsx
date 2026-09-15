import React from 'react';
import { mockCourses } from '../services/mockData';

export const CoursesPage: React.FC = () => {
  return (
    <div style={{ maxWidth: '1200px', margin: '0 auto', padding: '2rem 1.5rem', width: '100%' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1.5rem', flexWrap: 'wrap', gap: '1rem' }}>
        <div>
          <h1 style={{ fontSize: '1.8rem', fontWeight: 800, color: '#f8fafc', letterSpacing: '-0.5px' }}>
            Enrolled Academic Courses
          </h1>
          <p style={{ fontSize: '0.9rem', color: '#94a3b8' }}>
            Fall Semester 2026 • 16 Total Credit Hours
          </p>
        </div>
        <div style={{ display: 'flex', gap: '8px' }}>
          <button className="btn btn-secondary" style={{ fontSize: '0.85rem' }}>
            📥 Download Syllabus Pack
          </button>
        </div>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(320px, 1fr))', gap: '1.25rem' }}>
        {mockCourses.map((course) => (
          <div key={course.id} className="glass-panel" style={{ padding: '1.5rem', display: 'flex', flexDirection: 'column', justifyContent: 'space-between' }}>
            <div>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '8px' }}>
                <span style={{
                  padding: '3px 8px',
                  borderRadius: '6px',
                  backgroundColor: 'rgba(37, 99, 235, 0.2)',
                  color: '#60a5fa',
                  fontWeight: 700,
                  fontSize: '0.8rem',
                }}>
                  {course.code}
                </span>
                <span style={{
                  fontSize: '0.8rem',
                  color: '#10b981',
                  fontWeight: 700,
                  backgroundColor: 'rgba(16, 185, 129, 0.15)',
                  padding: '2px 8px',
                  borderRadius: '10px',
                }}>
                  Grade: {course.grade}
                </span>
              </div>

              <h3 style={{ fontSize: '1.15rem', fontWeight: 700, color: '#f8fafc', marginBottom: '6px' }}>
                {course.title}
              </h3>
              <p style={{ fontSize: '0.85rem', color: '#94a3b8' }}>
                Instructor: <strong style={{ color: '#cbd5e1' }}>{course.instructor}</strong>
              </p>
              <p style={{ fontSize: '0.8rem', color: '#64748b', marginTop: '2px' }}>
                Schedule: {course.schedule} • {course.credits} Credits
              </p>
            </div>

            <div style={{ marginTop: '1.5rem' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.8rem', color: '#94a3b8', marginBottom: '6px' }}>
                <span>Curriculum Progress</span>
                <span style={{ fontWeight: 700, color: '#f8fafc' }}>{course.progress}%</span>
              </div>
              <div style={{
                height: '8px',
                width: '100%',
                backgroundColor: 'rgba(15, 23, 42, 0.8)',
                borderRadius: '4px',
                overflow: 'hidden',
              }}>
                <div style={{
                  height: '100%',
                  width: `${course.progress}%`,
                  background: 'linear-gradient(90deg, #2563eb, #38bdf8)',
                  borderRadius: '4px',
                }} />
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
