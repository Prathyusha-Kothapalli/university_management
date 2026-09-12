import React from 'react';
import { StatCard } from '../../components/charts/StatCard';
import { Card, CardHeader, CardTitle, CardContent } from '../../components/ui/Card';
import { DataTable } from '../../components/tables/DataTable';
import { CreditCard, DollarSign, TrendingUp, AlertCircle } from 'lucide-react';
import { Badge } from '../../components/ui/Badge';

const feeCollections = [
  { id: 'TXN-9012', student: 'Rohan Sharma', amount: '₹65,000', mode: 'ONLINE_UPI', date: 'Today, 10:14 AM', status: 'SUCCESS' },
  { id: 'TXN-9013', student: 'Priya Nair', amount: '₹72,000', mode: 'NET_BANKING', date: 'Today, 11:30 AM', status: 'SUCCESS' },
  { id: 'TXN-9014', student: 'Amitav Ghosh', amount: '₹45,000', mode: 'CHQ_DEPOSIT', date: 'Yesterday', status: 'PENDING_CLEARANCE' },
];

export const FinanceDashboard: React.FC = () => {
  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold text-white tracking-tight flex items-center gap-2">
          <CreditCard className="w-6 h-6 text-emerald-400" /> Finance & Accounts Portal
        </h1>
        <p className="text-xs text-slate-400">Tuition collection, outstanding dues, scholarship distribution & payouts</p>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <StatCard title="Total Sem Fee Collected" value="₹18.42 Cr" change="+8.1%" changeType="positive" icon={<DollarSign className="w-5 h-5" />} />
        <StatCard title="Pending Outstanding Dues" value="₹35.2 Lakhs" change="420 Students" changeType="warning" icon={<AlertCircle className="w-5 h-5" />} iconBg="bg-amber-500/10 text-amber-400" />
        <StatCard title="Scholarships Disbursed" value="₹1.20 Cr" change="280 Scholars" changeType="positive" icon={<TrendingUp className="w-5 h-5" />} iconBg="bg-sky-500/10 text-sky-400" />
        <StatCard title="Monthly Payroll Outflow" value="₹3.40 Cr" change="Faculty & Staff" changeType="neutral" icon={<CreditCard className="w-5 h-5" />} iconBg="bg-purple-500/10 text-purple-400" />
      </div>

      <Card className="glass-card">
        <CardHeader>
          <CardTitle>Recent Payment Receipts Stream</CardTitle>
        </CardHeader>
        <CardContent>
          <DataTable
            data={feeCollections}
            columns={[
              { header: 'Txn ID', accessorKey: 'id' },
              { header: 'Student Name', accessorKey: 'student' },
              { header: 'Amount Paid', accessorKey: 'amount' },
              { header: 'Payment Method', accessorKey: 'mode' },
              { header: 'Timestamp', accessorKey: 'date' },
              {
                header: 'Status',
                accessorKey: 'status',
                cell: (row) => (
                  <Badge variant={row.status === 'SUCCESS' ? 'success' : 'warning'}>
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
