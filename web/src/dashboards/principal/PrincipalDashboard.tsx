import React from 'react';
import { StatCard } from '../../components/charts/StatCard';
import { Card, CardHeader, CardTitle, CardDescription, CardContent } from '../../components/ui/Card';
import { DataTable } from '../../components/tables/DataTable';
import { Badge } from '../../components/ui/Badge';
import { Award, GraduationCap, Users, CalendarCheck, BookOpen } from 'lucide-react';

const collegeAlerts = [
  { dept: 'Computer Science', alert: 'Mid-term mark entry incomplete (85%)', priority: 'HIGH' },
  { dept: 'Mechanical Engg', alert: 'Faculty leave request pending approval', priority: 'MEDIUM' },
  { dept: 'Electrical Engg', alert: 'Lab Equipment Maintenance required', priority: 'LOW' },
];

export const PrincipalDashboard: React.FC = () => {
  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold text-white tracking-tight flex items-center gap-2">
          <Award className="w-6 h-6 text-amber-400" /> Principal Academic Dashboard
        </h1>
        <p className="text-xs text-slate-400">Campus academic operations, attendance index & departmental reviews</p>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <StatCard
          title="Campus Students"
          value="4,850"
          change="12 Departments"
          changeType="neutral"
          icon={<GraduationCap className="w-5 h-5" />}
        />
        <StatCard
          title="Teaching Staff"
          value="240 Faculty"
          change="1:20 Ph.D Ratio"
          changeType="positive"
          icon={<Users className="w-5 h-5" />}
          iconBg="bg-sky-500/10 text-sky-400"
        />
        <StatCard
          title="Average Attendance"
          value="88.4%"
          change="+1.2% this week"
          changeType="positive"
          icon={<CalendarCheck className="w-5 h-5" />}
          iconBg="bg-emerald-500/10 text-emerald-400"
        />
        <StatCard
          title="Pass Percentage"
          value="94.2%"
          change="Autonomous Standard"
          changeType="positive"
          icon={<BookOpen className="w-5 h-5" />}
          iconBg="bg-purple-500/10 text-purple-400"
        />
      </div>

      <Card className="glass-card">
        <CardHeader>
          <CardTitle>Action Items & Departmental Alerts</CardTitle>
          <CardDescription>Academic compliance triggers requiring Principal intervention</CardDescription>
        </CardHeader>
        <CardContent>
          <DataTable
            data={collegeAlerts}
            columns={[
              { header: 'Department', accessorKey: 'dept' },
              { header: 'Alert Description', accessorKey: 'alert' },
              {
                header: 'Priority Level',
                accessorKey: 'priority',
                cell: (row) => (
                  <Badge variant={row.priority === 'HIGH' ? 'destructive' : 'warning'}>
                    {row.priority}
                  </Badge>
                ),
              },
            ]}
          />
        </CardContent>
      </Card>
    </div>
  );
};
