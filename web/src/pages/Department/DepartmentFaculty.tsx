import React from 'react';
import { DataTable, Column } from '../../components/DataTable';

interface FacultyItem {
  id: string;
  name: string;
  designation: string;
  specialization: string;
  publications: number;
  courses: string;
  email: string;
}

export const DepartmentFaculty: React.FC = () => {
  const faculty: FacultyItem[] = [
    { id: '1', name: 'Dr. Sarah Jenkins', designation: 'Professor', specialization: 'Database Systems & Big Data', publications: 42, courses: 'CS301, CS702', email: 'sarah.j@unisphere.edu' },
    { id: '2', name: 'Prof. Alan Turing', designation: 'Professor', specialization: 'Theory of Computation & Algorithms', publications: 88, courses: 'CS302, CS501', email: 'alan.t@unisphere.edu' },
    { id: '3', name: 'Dr. Robert Rao', designation: 'HOD & Professor', specialization: 'Computer Networks & Security', publications: 64, courses: 'CS303, CS801', email: 'robert.rao@unisphere.edu' },
    { id: '4', name: 'Dr. Emily Vance', designation: 'Associate Professor', specialization: 'Deep Learning & NLP', publications: 31, courses: 'CS401, CS602', email: 'emily.v@unisphere.edu' },
    { id: '5', name: 'Prof. Michael Scott', designation: 'Assistant Professor', specialization: 'Distributed Systems & Cloud', publications: 18, courses: 'CS402, CS504', email: 'michael.s@unisphere.edu' },
    { id: '6', name: 'Dr. Grace Hopper', designation: 'Associate Professor', specialization: 'Compiler Design & Data Structures', publications: 52, courses: 'CS201, CS403', email: 'grace.h@unisphere.edu' },
  ];

  const columns: Column<FacultyItem>[] = [
    { header: 'Faculty Name', accessorKey: 'name' },
    { header: 'Designation', accessorKey: 'designation' },
    { header: 'Specialization', accessorKey: 'specialization' },
    { header: 'Assigned Courses', accessorKey: 'courses' },
    { header: 'Publications', accessorKey: 'publications' },
    { header: 'Email', accessorKey: 'email' },
  ];

  return (
    <div style={{ padding: '1.75rem', display: 'flex', flexDirection: 'column', gap: '1.25rem', maxWidth: '1400px', margin: '0 auto' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <div>
          <h1 style={{ fontSize: '1.5rem', fontWeight: 800, color: '#f8fafc', margin: 0 }}>
            Department Faculty Roster
          </h1>
          <p style={{ fontSize: '0.85rem', color: '#94a3b8', margin: '4px 0 0 0' }}>
            42 full-time professors, associate professors, and assistant professors
          </p>
        </div>
      </div>

      <DataTable data={faculty} columns={columns} />
    </div>
  );
};
