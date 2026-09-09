import React from 'react';
import { StatCard } from '../../components/charts/StatCard';
import { Card, CardHeader, CardTitle, CardDescription, CardContent } from '../../components/ui/Card';
import { PieChart, TrendingUp, Award, DollarSign, Users } from 'lucide-react';
import { ResponsiveContainer, BarChart, Bar, XAxis, YAxis, Tooltip } from 'recharts';

const campusPerformance = [
  { campus: 'Engineering', revenue: 42, placements: 88, research: 92 },
  { campus: 'Medical & Dental', revenue: 68, placements: 94, research: 96 },
  { campus: 'Business School', revenue: 35, placements: 82, research: 78 },
  { campus: 'Arts & Sciences', revenue: 22, placements: 74, research: 81 },
];

export const ManagementDashboard: React.FC = () => {
  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold text-white tracking-tight flex items-center gap-2">
          <PieChart className="w-6 h-6 text-indigo-400" /> Executive Management Dashboard
        </h1>
        <p className="text-xs text-slate-400">Trustee & Governing Board institutional metrics and financial health</p>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <StatCard
          title="Total Group Revenue"
          value="₹148.5 Cr"
          change="+14.2% YoY"
          changeType="positive"
          icon={<DollarSign className="w-5 h-5" />}
        />
        <StatCard
          title="Enrollment Count"
          value="18,420"
          change="98% Capacity"
          changeType="positive"
          icon={<Users className="w-5 h-5" />}
          iconBg="bg-sky-500/10 text-sky-400"
        />
        <StatCard
          title="Overall Placement Rate"
          value="87.6%"
          change="+3.2%"
          changeType="positive"
          icon={<TrendingUp className="w-5 h-5" />}
          iconBg="bg-emerald-500/10 text-emerald-400"
        />
        <StatCard
          title="NIRF Institutional Rank"
          value="Top 25"
          change="A++ Grade"
          changeType="neutral"
          icon={<Award className="w-5 h-5" />}
          iconBg="bg-amber-500/10 text-amber-400"
        />
      </div>

      <Card className="glass-card">
        <CardHeader>
          <CardTitle>Campus Wise Institutional Performance Comparison</CardTitle>
          <CardDescription>Revenue (₹ Cr), Placement Percentage (%), and Research Rating (1-100)</CardDescription>
        </CardHeader>
        <CardContent>
          <div className="h-72 w-full">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={campusPerformance}>
                <XAxis dataKey="campus" stroke="#64748b" fontSize={11} />
                <YAxis stroke="#64748b" fontSize={11} />
                <Tooltip contentStyle={{ backgroundColor: '#0f172a', borderColor: '#334155', borderRadius: '8px' }} />
                <Bar dataKey="revenue" fill="#38bdf8" radius={[4, 4, 0, 0]} name="Revenue (₹ Cr)" />
                <Bar dataKey="placements" fill="#10b981" radius={[4, 4, 0, 0]} name="Placement %" />
                <Bar dataKey="research" fill="#8b5cf6" radius={[4, 4, 0, 0]} name="Research Rating" />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </CardContent>
      </Card>
    </div>
  );
};
