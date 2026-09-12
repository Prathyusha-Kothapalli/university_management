import React from 'react';
import { StatCard } from '../../components/charts/StatCard';
import { Users, Contact, Receipt, UserCheck } from 'lucide-react';

export const HrDashboard: React.FC = () => {
  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold text-white tracking-tight flex items-center gap-2">
          <Users className="w-6 h-6 text-purple-400" /> HR & Payroll Portal
        </h1>
        <p className="text-xs text-slate-400">Employee lifecycle, leave approvals, salary structure, and recruitment</p>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <StatCard title="Total Employees" value="620 Staff" icon={<Users className="w-5 h-5" />} />
        <StatCard title="Present Today" value="594 Staff (95.8%)" icon={<UserCheck className="w-5 h-5" />} iconBg="bg-emerald-500/10 text-emerald-400" />
        <StatCard title="Pending Leave Requests" value="12 Requests" icon={<Contact className="w-5 h-5" />} iconBg="bg-amber-500/10 text-amber-400" />
        <StatCard title="Payroll Status" value="September Processed" icon={<Receipt className="w-5 h-5" />} iconBg="bg-sky-500/10 text-sky-400" />
      </div>
    </div>
  );
};
