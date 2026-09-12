import React from 'react';
import { StatCard } from '../../components/charts/StatCard';
import { Calendar, CheckCircle2, AlertTriangle, Users } from 'lucide-react';

export const AttendanceAnalyticsDashboard: React.FC = () => {
  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold text-white tracking-tight flex items-center gap-2">
          <Calendar className="w-6 h-6 text-emerald-400" /> Attendance Analytics Hub
        </h1>
        <p className="text-xs text-slate-400">College-wide attendance trends, defaulter lists, and automated SMS alerts</p>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <StatCard title="Today's Campus Attendance" value="88.2%" change="+0.4%" changeType="positive" icon={<CheckCircle2 className="w-5 h-5" />} />
        <StatCard title="Defaulters (<75%)" value="142 Students" change="-12 this week" changeType="positive" icon={<AlertTriangle className="w-5 h-5" />} iconBg="bg-amber-500/10 text-amber-400" />
        <StatCard title="Critical (<65%)" value="28 Students" change="Notice Generated" changeType="warning" icon={<Users className="w-5 h-5" />} iconBg="bg-rose-500/10 text-rose-400" />
        <StatCard title="Automated SMS Dispatched" value="170 Alerts" icon={<Calendar className="w-5 h-5" />} iconBg="bg-sky-500/10 text-sky-400" />
      </div>
    </div>
  );
};
