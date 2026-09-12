import React from 'react';
import { StatCard } from '../../components/charts/StatCard';
import { BarChart3, PieChart, LineChart, FileSpreadsheet } from 'lucide-react';

export const BiDashboard: React.FC = () => {
  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold text-white tracking-tight flex items-center gap-2">
          <BarChart3 className="w-6 h-6 text-indigo-400" /> Business Intelligence & Custom Reports
        </h1>
        <p className="text-xs text-slate-400">Multi-dimensional institutional analytics, custom query builder & export suite</p>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <StatCard title="Saved BI Dashboards" value="24 Reports" icon={<BarChart3 className="w-5 h-5" />} />
        <StatCard title="Monthly Export Jobs" value="1,420 CSV/PDFs" icon={<FileSpreadsheet className="w-5 h-5" />} iconBg="bg-sky-500/10 text-sky-400" />
        <StatCard title="Data Drilldowns" value="Realtime OLAP" icon={<PieChart className="w-5 h-5" />} iconBg="bg-emerald-500/10 text-emerald-400" />
        <StatCard title="Scheduled Report Emails" value="12 Active Cron" icon={<LineChart className="w-5 h-5" />} iconBg="bg-purple-500/10 text-purple-400" />
      </div>
    </div>
  );
};
