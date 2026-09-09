import React from 'react';
import { StatCard } from '../../components/charts/StatCard';
import { Lock, Eye, UserCheck, Shield } from 'lucide-react';

export const SecurityDashboard: React.FC = () => {
  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold text-white tracking-tight flex items-center gap-2">
          <Lock className="w-6 h-6 text-emerald-400" /> Campus Security & Gate Pass Management
        </h1>
        <p className="text-xs text-slate-400">Visitor logs, student hostel gate passes, and CCTV surveillance integration</p>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <StatCard title="Daily Visitors Logged" value="142 Visitors" icon={<UserCheck className="w-5 h-5" />} />
        <StatCard title="Hostel Out-Pass Active" value="68 Students" icon={<Eye className="w-5 h-5" />} iconBg="bg-sky-500/10 text-sky-400" />
        <StatCard title="Active CCTV Feeds" value="128 / 128 Online" icon={<Shield className="w-5 h-5" />} iconBg="bg-emerald-500/10 text-emerald-400" />
        <StatCard title="Security Incidents" value="0 Alerts" icon={<Lock className="w-5 h-5" />} iconBg="bg-purple-500/10 text-purple-400" />
      </div>
    </div>
  );
};
