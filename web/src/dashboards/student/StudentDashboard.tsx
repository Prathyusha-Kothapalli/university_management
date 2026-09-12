import React from 'react';
import { StatCard } from '../../components/charts/StatCard';
import { Card, CardHeader, CardTitle, CardDescription, CardContent } from '../../components/ui/Card';
import { DataTable } from '../../components/tables/DataTable';
import { LayoutDashboard, CheckCircle2, FileText, CreditCard, Award } from 'lucide-react';
import { Button } from '../../components/ui/Button';

const upcomingExams = [
  { subject: 'CSE-301: Database Management Systems', date: 'Sep 18, 2026', time: '10:00 AM', venue: 'Exam Hall A' },
  { subject: 'CSE-302: Operating Systems & Architecture', date: 'Sep 21, 2026', time: '02:00 PM', venue: 'Exam Hall B' },
  { subject: 'CSE-303: Artificial Intelligence Basics', date: 'Sep 24, 2026', time: '10:00 AM', venue: 'Lab 3' },
];

export const StudentDashboard: React.FC = () => {
  return (
    <div className="space-y-6">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <h1 className="text-2xl font-bold text-white tracking-tight flex items-center gap-2">
            <LayoutDashboard className="w-6 h-6 text-sky-400" /> Student Portal
          </h1>
          <p className="text-xs text-slate-400">Semester 6 — B.Tech Computer Science & Engineering</p>
        </div>
        <Button size="sm" variant="glass" className="gap-2">
          <CreditCard className="w-4 h-4" /> Pay Pending Fees
        </Button>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <StatCard
          title="Overall Attendance"
          value="91.5%"
          change="Safe (>75%)"
          changeType="positive"
          icon={<CheckCircle2 className="w-5 h-5" />}
        />
        <StatCard
          title="Current CGPA"
          value="8.84 / 10"
          change="Rank #4 in Batch"
          changeType="positive"
          icon={<Award className="w-5 h-5" />}
          iconBg="bg-indigo-500/10 text-indigo-400"
        />
        <StatCard
          title="Pending Assignments"
          value="2 Due"
          change="Next due in 2 days"
          changeType="warning"
          icon={<FileText className="w-5 h-5" />}
          iconBg="bg-amber-500/10 text-amber-400"
        />
        <StatCard
          title="Fee Status"
          value="₹0 Outstanding"
          change="Paid for Sem 6"
          changeType="positive"
          icon={<CreditCard className="w-5 h-5" />}
          iconBg="bg-emerald-500/10 text-emerald-400"
        />
      </div>

      <Card className="glass-card">
        <CardHeader>
          <CardTitle>Upcoming Mid-Semester Examination Schedule</CardTitle>
          <CardDescription>Verified by Exam Cell — Hall ticket downloadable</CardDescription>
        </CardHeader>
        <CardContent>
          <DataTable
            data={upcomingExams}
            columns={[
              { header: 'Subject Course', accessorKey: 'subject' },
              { header: 'Date', accessorKey: 'date' },
              { header: 'Time Slot', accessorKey: 'time' },
              { header: 'Exam Venue', accessorKey: 'venue' },
            ]}
          />
        </CardContent>
      </Card>
    </div>
  );
};
