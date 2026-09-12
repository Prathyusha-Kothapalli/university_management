import React from 'react';
import { StatCard } from '../../components/charts/StatCard';
import { Package, AlertCircle, ShoppingCart, CheckSquare } from 'lucide-react';

export const InventoryDashboard: React.FC = () => {
  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold text-white tracking-tight flex items-center gap-2">
          <Package className="w-6 h-6 text-sky-400" /> Inventory & Asset Management
        </h1>
        <p className="text-xs text-slate-400">Lab consumables, IT hardware assets, purchase requisitions, and vendor audits</p>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <StatCard title="Total Tracked Assets" value="14,800 Items" icon={<Package className="w-5 h-5" />} />
        <StatCard title="Low Stock Alerts" value="8 Items" change="Re-order Level" changeType="warning" icon={<AlertCircle className="w-5 h-5" />} iconBg="bg-amber-500/10 text-amber-400" />
        <StatCard title="Pending Purchase Orders" value="5 Approved" icon={<ShoppingCart className="w-5 h-5" />} iconBg="bg-sky-500/10 text-sky-400" />
        <StatCard title="Maintenance Work Orders" value="3 In Progress" icon={<CheckSquare className="w-5 h-5" />} iconBg="bg-emerald-500/10 text-emerald-400" />
      </div>
    </div>
  );
};
