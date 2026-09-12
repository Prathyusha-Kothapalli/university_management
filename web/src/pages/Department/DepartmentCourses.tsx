import React from 'react';
import { DataTable, Column } from '../../components/DataTable';

interface CourseItem {
  id: string;
  code: string;
  name: string;
  semester: string;
  credits: number;
  lead: string;
  syllabusStatus: string;
}

export const DepartmentCourses: React.FC = () => {
  const courses: CourseItem[] = [
    { id: '1', code: 'CS201', name: 'Data Structures & Algorithms', semester: 'Semester 3', credits: 4, lead: 'Dr. Grace Hopper', syllabusStatus: '100% Complete' },
    { id: '2', code: 'CS202', name: 'Discrete Mathematics', semester: 'Semester 3', credits: 3, lead: 'Prof. David Miller', syllabusStatus: '85% In-Progress' },
    { id: '3', code: 'CS301', name: 'Database Management Systems', semester: 'Semester 5', credits: 4, lead: 'Dr. Sarah Jenkins', syllabusStatus: '90% In-Progress' },
    { id: '4', code: 'CS302', name: 'Operating Systems', semester: 'Semester 5', credits: 4, lead: 'Prof. Alan Turing', syllabusStatus: '88% In-Progress' },
    { id: '5', code: 'CS303', name: 'Computer Networks', semester: 'Semester 5', credits: 3, lead: 'Dr. Robert Rao', syllabusStatus: '92% In-Progress' },
    { id: '6', code: 'CS401', name: 'Machine Learning & AI', semester: 'Semester 7', credits: 4, lead: 'Dr. Emily Vance', syllabusStatus: '95% In-Progress' },
    { id: '7', code: 'CS402', name: 'Distributed Systems', semester: 'Semester 7', credits: 4, lead: 'Prof. Michael Scott', syllabusStatus: '78% In-Progress' },
  ];

  const columns: Column<CourseItem>[] = [
    { header: 'Course Code', accessorKey: 'code' },
    { header: 'Course Title', accessorKey: 'name' },
    { header: 'Semester', accessorKey: 'semester' },
    { header: 'Credits', accessorKey: 'credits' },
    { header: 'Lead Instructor', accessorKey: 'lead' },
    { header: 'Syllabus Progress', accessorKey: 'syllabusStatus' },
  ];

  return (
    <div style={{ padding: '1.75rem', display: 'flex', flexDirection: 'column', gap: '1.25rem', maxWidth: '1400px', margin: '0 auto' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <div>
          <h1 style={{ fontSize: '1.5rem', fontWeight: 800, color: '#f8fafc', margin: 0 }}>
            Department Course Curriculum
          </h1>
          <p style={{ fontSize: '0.85rem', color: '#94a3b8', margin: '4px 0 0 0' }}>
            28 active course offerings across 8 semesters
          </p>
        </div>
      </div>

      <DataTable data={courses} columns={columns} />
    </div>
  );
};
