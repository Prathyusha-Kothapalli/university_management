import React from 'react';
import { StatCard } from '../../components/charts/StatCard';
import { Microscope, FileText, Award, DollarSign } from 'lucide-react';

export const ResearchDashboard: React.FC = () => {
  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold text-white tracking-tight flex items-center gap-2">
          <Microscope className="w-6 h-6 text-purple-400" /> Research & Innovation Portal
        </h1>
        <p className="text-xs text-slate-400">Scopus/IEEE publications, funded research grants, patents & IP portfolio</p>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <StatCard title="Indexed Publications" value="384 Papers" change="Scopus / Web of Science" changeType="positive" icon={<FileText className="w-5 h-5" />} />
        <StatCard title="Active Funded Grants" value="₹4.20 Cr" icon={<DollarSign className="w-5 h-5" />} iconBg="bg-emerald-500/10 text-emerald-400" />
        <StatCard title="Patents Filed / Granted" value="28 / 6" icon={<Award className="w-5 h-5" />} iconBg="bg-sky-500/10 text-sky-400" />
        <StatCard title="Ph.D Scholars Enrolled" value="112 Scholars" icon={<Microscope className="w-5 h-5" />} iconBg="bg-indigo-500/10 text-indigo-400" />
      </div>
    </div>
  );
};
