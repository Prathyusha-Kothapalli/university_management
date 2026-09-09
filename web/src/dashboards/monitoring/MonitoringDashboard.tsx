import React from 'react';
import { StatCard } from '../../components/charts/StatCard';
import { Activity, Server, Cpu, Database } from 'lucide-react';

export const MonitoringDashboard: React.FC = () => {
  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold text-white tracking-tight flex items-center gap-2">
          <Activity className="w-6 h-6 text-sky-400" /> Infrastructure & System Health Monitoring
        </h1>
        <p className="text-xs text-slate-400">Node metrics, database connection pools, Redis cache status, and error logs</p>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <StatCard title="API Gateway Uptime" value="99.99%" icon={<Server className="w-5 h-5" />} />
        <StatCard title="CPU Utilization" value="34% Load" icon={<Cpu className="w-5 h-5" />} iconBg="bg-emerald-500/10 text-emerald-400" />
        <StatCard title="PostgreSQL Pool Connections" value="48 / 200" icon={<Database className="w-5 h-5" />} iconBg="bg-sky-500/10 text-sky-400" />
        <StatCard title="Redis Cache Hit Ratio" value="94.8%" icon={<Activity className="w-5 h-5" />} iconBg="bg-purple-500/10 text-purple-400" />
      </div>
    </div>
  );
};
