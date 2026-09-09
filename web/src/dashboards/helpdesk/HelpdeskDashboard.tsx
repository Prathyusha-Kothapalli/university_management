import React from 'react';
import { StatCard } from '../../components/charts/StatCard';
import { HelpCircle, Clock, CheckCircle2, AlertCircle } from 'lucide-react';

export const HelpdeskDashboard: React.FC = () => {
  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold text-white tracking-tight flex items-center gap-2">
          <HelpCircle className="w-6 h-6 text-sky-400" /> IT & Campus Help Desk
        </h1>
        <p className="text-xs text-slate-400">Student & staff support tickets, IT assistance, and SLA tracking</p>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <StatCard title="Open Support Tickets" value="18 Tickets" icon={<HelpCircle className="w-5 h-5" />} />
        <StatCard title="Avg Resolution Time" value="2.4 Hours" change="SLA 98.2%" changeType="positive" icon={<Clock className="w-5 h-5" />} iconBg="bg-sky-500/10 text-sky-400" />
        <StatCard title="Resolved Today" value="34 Tickets" icon={<CheckCircle2 className="w-5 h-5" />} iconBg="bg-emerald-500/10 text-emerald-400" />
        <StatCard title="SLA Escalations" value="1 Ticket" change="Priority High" changeType="warning" icon={<AlertCircle className="w-5 h-5" />} iconBg="bg-rose-500/10 text-rose-400" />
      </div>
    </div>
  );
};
