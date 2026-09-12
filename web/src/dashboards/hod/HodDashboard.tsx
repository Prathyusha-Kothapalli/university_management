import React from 'react';
import { StatCard } from '../../components/charts/StatCard';
import { Card, CardHeader, CardTitle, CardContent } from '../../components/ui/Card';
import { DataTable } from '../../components/tables/DataTable';
import { Building, Users, Calendar, Award } from 'lucide-react';

const deptFaculty = [
  { name: 'Dr. Vikram Seth', designation: 'Professor', load: '16 hrs/wk', subjects: 'DBMS, Data Structures' },
  { name: 'Prof. Ananya Roy', designation: 'Associate Prof', load: '14 hrs/wk', subjects: 'Artificial Intelligence' },
  { name: 'Dr. Rajesh Patel', designation: 'Assistant Prof', load: '18 hrs/wk', subjects: 'Operating Systems' },
];

export const HodDashboard: React.FC = () => {
  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold text-white tracking-tight flex items-center gap-2">
          <Building className="w-6 h-6 text-purple-400" /> Head of Department (HOD) Portal
        </h1>
        <p className="text-xs text-slate-400">Department of Computer Science & Engineering management</p>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <StatCard title="Department Students" value="720 Students" icon={<Users className="w-5 h-5" />} />
        <StatCard title="Department Faculty" value="32 Staff" icon={<Building className="w-5 h-5" />} iconBg="bg-sky-500/10 text-sky-400" />
        <StatCard title="Avg Dept Attendance" value="89.1%" icon={<Calendar className="w-5 h-5" />} iconBg="bg-emerald-500/10 text-emerald-400" />
        <StatCard title="Lab Utilization" value="94%" icon={<Award className="w-5 h-5" />} iconBg="bg-purple-500/10 text-purple-400" />
      </div>

      <Card className="glass-card">
        <CardHeader>
          <CardTitle>Department Faculty Workload & Subject Allocation</CardTitle>
        </CardHeader>
        <CardContent>
          <DataTable
            data={deptFaculty}
            columns={[
              { header: 'Faculty Name', accessorKey: 'name' },
              { header: 'Designation', accessorKey: 'designation' },
              { header: 'Weekly Load', accessorKey: 'load' },
              { header: 'Assigned Subjects', accessorKey: 'subjects' },
            ]}
          />
        </CardContent>
      </Card>
    </div>
  );
};
