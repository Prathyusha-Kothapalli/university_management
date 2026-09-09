import React from 'react';
import { StatCard } from '../../components/charts/StatCard';
import { Card, CardHeader, CardTitle, CardDescription, CardContent } from '../../components/ui/Card';
import { Landmark, FileSpreadsheet, Users, Microscope } from 'lucide-react';

export const DeanDashboard: React.FC = () => {
  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold text-white tracking-tight flex items-center gap-2">
          <Landmark className="w-6 h-6 text-sky-400" /> Dean of Faculty & School Portal
        </h1>
        <p className="text-xs text-slate-400">School curriculum execution, faculty research, and program performance</p>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <StatCard title="Departments Managed" value="5 Departments" icon={<Landmark className="w-5 h-5" />} />
        <StatCard title="Active Programs" value="14 UG / PG" icon={<FileSpreadsheet className="w-5 h-5" />} iconBg="bg-sky-500/10 text-sky-400" />
        <StatCard title="Faculty Workload" value="92% Allocated" icon={<Users className="w-5 h-5" />} iconBg="bg-emerald-500/10 text-emerald-400" />
        <StatCard title="Active Research Grants" value="₹1.85 Cr" icon={<Microscope className="w-5 h-5" />} iconBg="bg-purple-500/10 text-purple-400" />
      </div>

      <Card className="glass-card">
        <CardHeader>
          <CardTitle>School Academic Directives</CardTitle>
          <CardDescription>Curriculum revision status & NBA accreditation progress</CardDescription>
        </CardHeader>
        <CardContent>
          <p className="text-xs text-slate-300">
            All 5 school departments are operating within curriculum targets. Board of Studies meeting scheduled for next Thursday.
          </p>
        </CardContent>
      </Card>
    </div>
  );
};
