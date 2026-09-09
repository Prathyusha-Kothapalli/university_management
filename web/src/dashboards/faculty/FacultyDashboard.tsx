import React from 'react';
import { StatCard } from '../../components/charts/StatCard';
import { Card, CardHeader, CardTitle, CardDescription, CardContent } from '../../components/ui/Card';
import { DataTable } from '../../components/tables/DataTable';
import { Button } from '../../components/ui/Button';
import { BookOpen, Clock, CheckSquare, Edit3, UserCheck } from 'lucide-react';
import { Badge } from '../../components/ui/Badge';

const todayClasses = [
  { time: '09:00 AM - 10:00 AM', course: 'CSE-301: Database Management Systems', room: 'Lab 4', batch: 'Semester 5 Sec A', status: 'COMPLETED' },
  { time: '11:15 AM - 12:15 PM', course: 'CSE-402: Distributed Systems', room: 'Hall 201', batch: 'Semester 7 Sec B', status: 'UPCOMING' },
  { time: '02:00 PM - 04:00 PM', course: 'CSE-301: DBMS Practical Lab', room: 'Lab 2', batch: 'Semester 5 Sec B', status: 'UPCOMING' },
];

export const FacultyDashboard: React.FC = () => {
  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold text-white tracking-tight flex items-center gap-2">
          <BookOpen className="w-6 h-6 text-sky-400" /> Faculty Workspace
        </h1>
        <p className="text-xs text-slate-400">Class schedule, digital attendance logging, and assignment grading</p>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <StatCard title="Today's Classes" value="3 Lectures" icon={<Clock className="w-5 h-5" />} />
        <StatCard title="Total Enrolled Students" value="185 Students" icon={<UserCheck className="w-5 h-5" />} iconBg="bg-sky-500/10 text-sky-400" />
        <StatCard title="Pending Assignments" value="28 Submissions" icon={<CheckSquare className="w-5 h-5" />} iconBg="bg-amber-500/10 text-amber-400" />
        <StatCard title="Syllabus Completion" value="68%" icon={<Edit3 className="w-5 h-5" />} iconBg="bg-emerald-500/10 text-emerald-400" />
      </div>

      <Card className="glass-card">
        <CardHeader className="flex flex-row items-center justify-between">
          <div>
            <CardTitle>Today's Teaching Schedule</CardTitle>
            <CardDescription>Click to mark digital attendance or launch lecture notes</CardDescription>
          </div>
          <Button size="sm" className="gap-1.5">
            <UserCheck className="w-4 h-4" /> Mark Quick Attendance
          </Button>
        </CardHeader>
        <CardContent>
          <DataTable
            data={todayClasses}
            columns={[
              { header: 'Time Slot', accessorKey: 'time' },
              { header: 'Subject Course', accessorKey: 'course' },
              { header: 'Batch / Section', accessorKey: 'batch' },
              { header: 'Room / Venue', accessorKey: 'room' },
              {
                header: 'Status',
                accessorKey: 'status',
                cell: (row) => (
                  <Badge variant={row.status === 'COMPLETED' ? 'success' : 'info'}>
                    {row.status}
                  </Badge>
                ),
              },
            ]}
          />
        </CardContent>
      </Card>
    </div>
  );
};
