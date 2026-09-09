import React from 'react';
import { StatCard } from '../../components/charts/StatCard';
import { CheckSquare, Award, FileCheck, ShieldCheck } from 'lucide-react';

export const AccreditationDashboard: React.FC = () => {
  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold text-white tracking-tight flex items-center gap-2">
          <CheckSquare className="w-6 h-6 text-emerald-400" /> Accreditation & Quality Assurance
        </h1>
        <p className="text-xs text-slate-400">NAAC, NBA, NIRF data collection & IQAC compliance documentation</p>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <StatCard title="NAAC Institutional Grade" value="A++ (3.74 CGPA)" change="Valid till 2029" changeType="positive" icon={<Award className="w-5 h-5" />} />
        <StatCard title="NBA Accredited Programs" value="8 Programs" change="Full 6 Years" changeType="positive" icon={<CheckSquare className="w-5 h-5" />} iconBg="bg-emerald-500/10 text-emerald-400" />
        <StatCard title="AQAR Submission Readiness" value="94% Complete" icon={<FileCheck className="w-5 h-5" />} iconBg="bg-sky-500/10 text-sky-400" />
        <StatCard title="IQAC Audit Status" value="Compliant" icon={<ShieldCheck className="w-5 h-5" />} iconBg="bg-purple-500/10 text-purple-400" />
      </div>
    </div>
  );
};
