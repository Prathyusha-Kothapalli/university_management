import React, { useState } from 'react';
import { Search } from 'lucide-react';
import { DataTable, Column } from '../../components/DataTable';

interface StudentItem {
  id: string;
  roll: string;
  name: string;
  semester: string;
  gpa: number;
  attendance: number;
  email: string;
  status: string;
}

export const DepartmentStudents: React.FC = () => {
  const [search, setSearch] = useState('');
  const [semester, setSemester] = useState('all');

  const students: StudentItem[] = [
    { id: '1', roll: 'CS2023001', name: 'Siddharth Varma', semester: 'Sem 7', gpa: 9.92, attendance: 96.5, email: 'siddharth.v@unisphere.edu', status: 'Active' },
    { id: '2', roll: 'CS2023042', name: 'Priya Sundaram', semester: 'Sem 7', gpa: 9.88, attendance: 95.0, email: 'priya.s@unisphere.edu', status: 'Active' },
    { id: '3', roll: 'CS2024018', name: 'Rohan Mehta', semester: 'Sem 5', gpa: 9.85, attendance: 92.4, email: 'rohan.m@unisphere.edu', status: 'Active' },
    { id: '4', roll: 'CS2024045', name: 'Vikram Patel', semester: 'Sem 5', gpa: 5.80, attendance: 68.4, email: 'vikram.p@unisphere.edu', status: 'At-Risk' },
    { id: '5', roll: 'CS2025005', name: 'Ananya Sharma', semester: 'Sem 3', gpa: 9.80, attendance: 94.2, email: 'ananya.s@unisphere.edu', status: 'Active' },
    { id: '6', roll: 'CS2025012', name: 'Devendra Singh', semester: 'Sem 3', gpa: 5.40, attendance: 82.5, email: 'devendra.s@unisphere.edu', status: 'At-Risk' },
  ];

  const filtered = students.filter((s) => {
    const matchesSearch = s.name.toLowerCase().includes(search.toLowerCase()) || s.roll.toLowerCase().includes(search.toLowerCase());
    const matchesSem = semester === 'all' || s.semester.toLowerCase() === semester.toLowerCase();
    return matchesSearch && matchesSem;
  });

  const columns: Column<StudentItem>[] = [
    { header: 'Roll Number', accessorKey: 'roll' },
    { header: 'Student Name', accessorKey: 'name' },
    { header: 'Semester', accessorKey: 'semester' },
    { header: 'CGPA', accessorKey: 'gpa' },
    { header: 'Attendance (%)', accessorKey: 'attendance' },
    { header: 'Email', accessorKey: 'email' },
    {
      header: 'Status',
      accessorKey: 'status',
      cell: (row) => (
        <span
          style={{
            padding: '2px 8px',
            borderRadius: '6px',
            fontSize: '0.72rem',
            fontWeight: 700,
            backgroundColor: row.status === 'At-Risk' ? 'rgba(244, 63, 94, 0.15)' : 'rgba(52, 211, 153, 0.15)',
            color: row.status === 'At-Risk' ? '#f43f5e' : '#34d399',
          }}
        >
          {row.status}
        </span>
      ),
    },
  ];

  return (
    <div style={{ padding: '1.75rem', display: 'flex', flexDirection: 'column', gap: '1.25rem', maxWidth: '1400px', margin: '0 auto' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '10px' }}>
        <div>
          <h1 style={{ fontSize: '1.5rem', fontWeight: 800, color: '#f8fafc', margin: 0 }}>
            Department Students Directory
          </h1>
          <p style={{ fontSize: '0.85rem', color: '#94a3b8', margin: '4px 0 0 0' }}>
            Total 1,248 enrolled students in Computer Science & Engineering
          </p>
        </div>

        <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
          <div style={{ position: 'relative' }}>
            <Search size={15} color="#94a3b8" style={{ position: 'absolute', left: '10px', top: '10px' }} />
            <input
              type="text"
              placeholder="Search student..."
              value={search}
              onChange={(e) => setSearch(e.target.value)}
              style={{
                backgroundColor: 'rgba(15, 23, 42, 0.8)',
                border: '1px solid rgba(255, 255, 255, 0.12)',
                borderRadius: '8px',
                color: '#f8fafc',
                padding: '6px 12px 6px 32px',
                fontSize: '0.825rem',
                outline: 'none',
              }}
            />
          </div>

          <select
            value={semester}
            onChange={(e) => setSemester(e.target.value)}
            style={{
              backgroundColor: 'rgba(15, 23, 42, 0.8)',
              border: '1px solid rgba(255, 255, 255, 0.12)',
              borderRadius: '8px',
              color: '#f8fafc',
              padding: '6px 12px',
              fontSize: '0.825rem',
              outline: 'none',
              cursor: 'pointer',
            }}
          >
            <option value="all">All Semesters</option>
            <option value="sem 3">Sem 3</option>
            <option value="sem 5">Sem 5</option>
            <option value="sem 7">Sem 7</option>
          </select>
        </div>
      </div>

      <DataTable data={filtered} columns={columns} />
    </div>
  );
};
