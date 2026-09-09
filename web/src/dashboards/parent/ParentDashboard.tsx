import React from 'react';
import { StatCard } from '../../components/charts/StatCard';
import { Card, CardHeader, CardTitle, CardDescription, CardContent } from '../../components/ui/Card';
import { HeartHandshake, CheckCircle2, Award, CreditCard, Bell } from 'lucide-react';
import { Badge } from '../../components/ui/Badge';

export const ParentDashboard: React.FC = () => {
  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold text-white tracking-tight flex items-center gap-2">
          <HeartHandshake className="w-6 h-6 text-rose-400" /> Parent Portal
        </h1>
        <p className="text-xs text-slate-400">Monitoring ward: Rohan Sharma (B.Tech CSE - Reg: 2024CSE091)</p>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <StatCard title="Ward Attendance" value="91.5%" change="Regular" changeType="positive" icon={<CheckCircle2 className="w-5 h-5" />} />
        <StatCard title="Ward Grade / CGPA" value="8.84 / 10" change="Distinction" changeType="positive" icon={<Award className="w-5 h-5" />} iconBg="bg-indigo-500/10 text-indigo-400" />
        <StatCard title="Tuition Fee Status" value="Cleared" change="Sem 6 Receipts Paid" changeType="positive" icon={<CreditCard className="w-5 h-5" />} iconBg="bg-emerald-500/10 text-emerald-400" />
        <StatCard title="Teacher Alerts" value="0 Alerts" change="Good Progress" changeType="positive" icon={<Bell className="w-5 h-5" />} iconBg="bg-sky-500/10 text-sky-400" />
      </div>

      <Card className="glass-card">
        <CardHeader>
          <CardTitle>Recent Attendance & Remarks from HOD</CardTitle>
          <CardDescription>Daily automated college entry log & mentor remarks</CardDescription>
        </CardHeader>
        <CardContent className="space-y-3">
          <div className="p-3.5 rounded-xl bg-slate-900/60 border border-slate-800 flex items-center justify-between text-xs">
            <div>
              <p className="font-semibold text-slate-200">Daily Campus RFID Attendance</p>
              <p className="text-slate-400">Punched in at 08:45 AM today at Gate 1</p>
            </div>
            <Badge variant="success">PRESENT</Badge>
          </div>
        </CardContent>
      </Card>
    </div>
  );
};
