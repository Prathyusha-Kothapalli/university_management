import React from 'react';
import { StatCard } from '../../components/charts/StatCard';
import { Briefcase, Building, DollarSign, Users } from 'lucide-react';

export const PlacementAlumniDashboard: React.FC = () => {
  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold text-white tracking-tight flex items-center gap-2">
          <Briefcase className="w-6 h-6 text-emerald-400" /> Placements & Alumni Portal
        </h1>
        <p className="text-xs text-slate-400">Corporate recruitment drives, student shortlisted matrix, and alumni network</p>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <StatCard title="Placement Percentage" value="88.4%" change="+4.1%" changeType="positive" icon={<Briefcase className="w-5 h-5" />} />
        <StatCard title="Visiting Recruiters" value="142 Companies" icon={<Building className="w-5 h-5" />} iconBg="bg-sky-500/10 text-sky-400" />
        <StatCard title="Highest Package" value="₹44.5 LPA" change="Microsoft India" changeType="positive" icon={<DollarSign className="w-5 h-5" />} iconBg="bg-amber-500/10 text-amber-400" />
        <StatCard title="Average CTC" value="₹8.6 LPA" change="Autonomous Tier 1" changeType="positive" icon={<Users className="w-5 h-5" />} iconBg="bg-purple-500/10 text-purple-400" />
      </div>
    </div>
  );
};
