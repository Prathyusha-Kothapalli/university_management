import React from 'react';
import { Card, CardHeader, CardTitle, CardContent } from '../../components/ui/Card';
import { DataTable } from '../../components/tables/DataTable';
import { Badge } from '../../components/ui/Badge';
import { Button } from '../../components/ui/Button';
import { UserPlus, Download } from 'lucide-react';

const studentData = [
  { id: '2024CSE001', name: 'Aarav Sharma', department: 'Computer Science', sem: 'Sem 6', cgpa: '8.92', status: 'ACTIVE' },
  { id: '2024CSE002', name: 'Bhavna Patel', department: 'Computer Science', sem: 'Sem 6', cgpa: '9.14', status: 'ACTIVE' },
  { id: '2024CSE003', name: 'Chetan Kumar', department: 'Computer Science', sem: 'Sem 6', cgpa: '8.45', status: 'ACTIVE' },
  { id: '2024ECE012', name: 'Divya Nair', department: 'Electronics', sem: 'Sem 4', cgpa: '8.78', status: 'ACTIVE' },
];

export const StudentList: React.FC = () => {
  return (
    <Card className="glass-card">
      <CardHeader className="flex flex-row items-center justify-between">
        <div>
          <CardTitle>Central Student Register</CardTitle>
        </div>
        <div className="flex gap-2">
          <Button size="sm" variant="outline" className="gap-1 text-xs">
            <Download className="w-3.5 h-3.5" /> Export Roster
          </Button>
          <Button size="sm" className="gap-1 text-xs">
            <UserPlus className="w-3.5 h-3.5" /> Add Student
          </Button>
        </div>
      </CardHeader>
      <CardContent>
        <DataTable
          data={studentData}
          columns={[
            { header: 'Student Roll ID', accessorKey: 'id' },
            { header: 'Full Name', accessorKey: 'name' },
            { header: 'Department', accessorKey: 'department' },
            { header: 'Semester', accessorKey: 'sem' },
            { header: 'CGPA', accessorKey: 'cgpa' },
            {
              header: 'Status',
              accessorKey: 'status',
              cell: (row) => <Badge variant="success">{row.status}</Badge>,
            },
          ]}
        />
      </CardContent>
    </Card>
  );
};
