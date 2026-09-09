import React from 'react';
import { StatCard } from '../../components/charts/StatCard';
import { Card, CardHeader, CardTitle, CardDescription, CardContent } from '../../components/ui/Card';
import { DataTable } from '../../components/tables/DataTable';
import { Badge } from '../../components/ui/Badge';
import { ShieldAlert, Building2, Users, Server, Activity, Cpu } from 'lucide-react';
import { ResponsiveContainer, AreaChart, Area, XAxis, YAxis, Tooltip } from 'recharts';

const systemTrends = [
  { month: 'Jan', requests: 45000, latency: 42 },
  { month: 'Feb', requests: 52000, latency: 38 },
  { month: 'Mar', requests: 61000, latency: 35 },
  { month: 'Apr', requests: 58000, latency: 39 },
  { month: 'May', requests: 75000, latency: 32 },
  { month: 'Jun', requests: 89000, latency: 29 },
];

const auditLogs = [
  { id: 'LOG-891', action: 'TENANT_PROVISIONED', user: 'super.admin@collexa.com', target: 'Apex Tech University', time: '12m ago', status: 'SUCCESS' },
  { id: 'LOG-890', action: 'RBAC_PERMISSION_UPDATED', user: 'system.admin@collexa.com', target: 'HOD Role Matrix', time: '1h ago', status: 'SUCCESS' },
  { id: 'LOG-889', action: 'SECURITY_SCAN_TRIGGERED', user: 'system.cron', target: 'PostgreSQL Core DB', time: '3h ago', status: 'SUCCESS' },
  { id: 'LOG-888', action: 'FAILED_API_AUTHENTICATION', user: 'IP 192.168.1.104', target: '/api/v1/auth/login', time: '5h ago', status: 'WARNING' },
];

export const SuperAdminDashboard: React.FC = () => {
  return (
    <div className="space-y-6">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <h1 className="text-2xl font-bold text-white tracking-tight flex items-center gap-2">
            <ShieldAlert className="w-6 h-6 text-sky-400" /> Super Admin Control Hub
          </h1>
          <p className="text-xs text-slate-400">Global ERP infrastructure, tenant isolation & audit logs</p>
        </div>
        <div className="flex items-center gap-2">
          <Badge variant="success" className="gap-1 px-3 py-1">
            <Activity className="w-3.5 h-3.5" /> All Services Operational
          </Badge>
        </div>
      </div>

      {/* KPI Grid */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <StatCard
          title="Active Tenants"
          value="14 Campuses"
          change="+2 new"
          changeType="positive"
          icon={<Building2 className="w-5 h-5" />}
        />
        <StatCard
          title="Total Managed Users"
          value="48,250"
          change="+12.4%"
          changeType="positive"
          icon={<Users className="w-5 h-5" />}
          iconBg="bg-indigo-500/10 text-indigo-400"
        />
        <StatCard
          title="API Load & Throughput"
          value="89k req/min"
          change="-4ms latency"
          changeType="positive"
          icon={<Cpu className="w-5 h-5" />}
          iconBg="bg-emerald-500/10 text-emerald-400"
        />
        <StatCard
          title="Database Cluster Health"
          value="99.98%"
          change="Optimal"
          changeType="neutral"
          icon={<Server className="w-5 h-5" />}
          iconBg="bg-purple-500/10 text-purple-400"
        />
      </div>

      {/* Analytics & Audit Grid */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <Card className="glass-card lg:col-span-2">
          <CardHeader>
            <CardTitle>System API Workload & Latency (ms)</CardTitle>
            <CardDescription>Real-time cluster telemetry across multi-tenant API gateways</CardDescription>
          </CardHeader>
          <CardContent>
            <div className="h-64 w-full">
              <ResponsiveContainer width="100%" height="100%">
                <AreaChart data={systemTrends}>
                  <defs>
                    <linearGradient id="colorRequests" x1="0" y1="0" x2="0" y2="1">
                      <stop offset="5%" stopColor="#0284c7" stopOpacity={0.4} />
                      <stop offset="95%" stopColor="#0284c7" stopOpacity={0} />
                    </linearGradient>
                  </defs>
                  <XAxis dataKey="month" stroke="#64748b" fontSize={11} />
                  <YAxis stroke="#64748b" fontSize={11} />
                  <Tooltip
                    contentStyle={{ backgroundColor: '#0f172a', borderColor: '#334155', borderRadius: '8px' }}
                  />
                  <Area type="monotone" dataKey="requests" stroke="#38bdf8" fillOpacity={1} fill="url(#colorRequests)" />
                </AreaChart>
              </ResponsiveContainer>
            </div>
          </CardContent>
        </Card>

        {/* Audit Log Table */}
        <Card className="glass-card">
          <CardHeader>
            <CardTitle>Audit Stream</CardTitle>
            <CardDescription>Recent privileged administrator activities</CardDescription>
          </CardHeader>
          <CardContent>
            <DataTable
              data={auditLogs}
              columns={[
                {
                  header: 'Action',
                  accessorKey: 'action',
                  cell: (row) => (
                    <div>
                      <p className="font-semibold text-slate-200 text-xs">{row.action}</p>
                      <p className="text-[10px] text-slate-500">{row.target}</p>
                    </div>
                  ),
                },
                {
                  header: 'Status',
                  accessorKey: 'status',
                  cell: (row) => (
                    <Badge variant={row.status === 'SUCCESS' ? 'success' : 'warning'} className="text-[10px]">
                      {row.status}
                    </Badge>
                  ),
                },
              ]}
              pageSize={4}
            />
          </CardContent>
        </Card>
      </div>
    </div>
  );
};
