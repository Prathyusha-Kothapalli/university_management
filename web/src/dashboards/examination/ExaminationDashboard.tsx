import React from 'react';
import { StatCard } from '../../components/charts/StatCard';
import { Card, CardHeader, CardTitle, CardDescription, CardContent } from '../../components/ui/Card';
import { FileCheck, GraduationCap, Edit3, Calendar } from 'lucide-react';

export const ExaminationDashboard: React.FC = () => {
  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold text-white tracking-tight flex items-center gap-2">
          <FileCheck className="w-6 h-6 text-indigo-400" /> Controller of Examinations Portal
        </h1>
        <p className="text-xs text-slate-400">Exam schedules, hall tickets, mark entries, and transcript generation</p>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <StatCard title="Upcoming Examinations" value="18 Subjects" icon={<Calendar className="w-5 h-5" />} />
        <StatCard title="Hall Tickets Issued" value="4,810" icon={<FileCheck className="w-5 h-5" />} iconBg="bg-sky-500/10 text-sky-400" />
        <StatCard title="Marks Evaluated" value="78%" icon={<Edit3 className="w-5 h-5" />} iconBg="bg-emerald-500/10 text-emerald-400" />
        <StatCard title="Results Published" value="4 Courses" icon={<GraduationCap className="w-5 h-5" />} iconBg="bg-purple-500/10 text-purple-400" />
      </div>

      <Card className="glass-card">
        <CardHeader>
          <CardTitle>Evaluation & Result Audit Matrix</CardTitle>
          <CardDescription>All mark entries verified with double keying by Exam Controllers</CardDescription>
        </CardHeader>
        <CardContent>
          <p className="text-xs text-slate-300">
            Fall Semester semester exam evaluation is 78% complete. Publication expected on Sept 28th.
          </p>
        </CardContent>
      </Card>
    </div>
  );
};
