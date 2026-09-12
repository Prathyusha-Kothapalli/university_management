import React from 'react';
import { StatCard } from '../../components/charts/StatCard';
import { ShieldAlert, FileText, CheckCircle2, Clock } from 'lucide-react';

export const GrievanceDashboard: React.FC = () => {
  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold text-white tracking-tight flex items-center gap-2">
          <ShieldAlert className="w-6 h-6 text-rose-400" /> Confidential Grievance Redressal
        </h1>
        <p className="text-xs text-slate-400">Anti-ragging, internal complaints committee (ICC) & student welfare inbox</p>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <StatCard title="Active Grievances" value="2 Cases" icon={<ShieldAlert className="w-5 h-5" />} />
        <StatCard title="Under Investigation" value="1 Case" icon={<Clock className="w-5 h-5" />} iconBg="bg-amber-500/10 text-amber-400" />
        <StatCard title="Resolved Cases" value="48 Cases" icon={<CheckCircle2 className="w-5 h-5" />} iconBg="bg-emerald-500/10 text-emerald-400" />
        <StatCard title="UGC Compliance Status" value="Fully Compliant" icon={<FileText className="w-5 h-5" />} iconBg="bg-sky-500/10 text-sky-400" />
      </div>
    </div>
  );
};
