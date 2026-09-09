import React from 'react';
import { StatCard } from '../../components/charts/StatCard';
import { Card, CardHeader, CardTitle, CardContent } from '../../components/ui/Card';
import { DataTable } from '../../components/tables/DataTable';
import { UserPlus, FileCheck, CheckCircle2, Clock } from 'lucide-react';
import { Badge } from '../../components/ui/Badge';

const applications = [
  { id: 'ADM-4091', applicant: 'Aarav Mehta', course: 'B.Tech CSE', score: '94.2%', status: 'VERIFIED' },
  { id: 'ADM-4092', applicant: 'Priya Nair', course: 'B.Tech AI & ML', score: '91.8%', status: 'PENDING_DOCS' },
  { id: 'ADM-4093', applicant: 'Kabir Singh', course: 'MBA Tech', score: '88.5%', status: 'VERIFIED' },
];

export const AdmissionsDashboard: React.FC = () => {
  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold text-white tracking-tight flex items-center gap-2">
          <UserPlus className="w-6 h-6 text-sky-400" /> Admissions Cell Portal
        </h1>
        <p className="text-xs text-slate-400">Application funnel, document verification, and seat allocation matrix</p>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <StatCard title="Total Received Applications" value="3,420" icon={<UserPlus className="w-5 h-5" />} />
        <StatCard title="Documents Verified" value="2,890" icon={<FileCheck className="w-5 h-5" />} iconBg="bg-sky-500/10 text-sky-400" />
        <StatCard title="Seats Confirmed" value="1,240 / 1,500" icon={<CheckCircle2 className="w-5 h-5" />} iconBg="bg-emerald-500/10 text-emerald-400" />
        <StatCard title="Pending Review" value="530" icon={<Clock className="w-5 h-5" />} iconBg="bg-amber-500/10 text-amber-400" />
      </div>

      <Card className="glass-card">
        <CardHeader>
          <CardTitle>Recent Application Verification Queue</CardTitle>
        </CardHeader>
        <CardContent>
          <DataTable
            data={applications}
            columns={[
              { header: 'App ID', accessorKey: 'id' },
              { header: 'Applicant Name', accessorKey: 'applicant' },
              { header: 'Target Course', accessorKey: 'course' },
              { header: 'Entrance Score', accessorKey: 'score' },
              {
                header: 'Verification Status',
                accessorKey: 'status',
                cell: (row) => (
                  <Badge variant={row.status === 'VERIFIED' ? 'success' : 'warning'}>
                    {row.status}
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
