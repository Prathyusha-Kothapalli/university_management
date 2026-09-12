import React from 'react';
import { StatCard } from '../../components/charts/StatCard';
import { Truck, Home, MapPin, Users } from 'lucide-react';

export const HostelTransportDashboard: React.FC = () => {
  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold text-white tracking-tight flex items-center gap-2">
          <Truck className="w-6 h-6 text-sky-400" /> Hostel & Transport Operations
        </h1>
        <p className="text-xs text-slate-400">Room allocations, mess schedule, bus routes, and vehicle GPS tracking</p>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <StatCard title="Hostel Occupancy" value="1,850 / 2,000" change="92.5%" changeType="positive" icon={<Home className="w-5 h-5" />} />
        <StatCard title="Mess Complaints" value="2 Pending" icon={<Users className="w-5 h-5" />} iconBg="bg-amber-500/10 text-amber-400" />
        <StatCard title="Active Transport Routes" value="28 Bus Routes" icon={<MapPin className="w-5 h-5" />} iconBg="bg-emerald-500/10 text-emerald-400" />
        <StatCard title="Bus Fleet Status" value="34 Vehicles" change="All On Schedule" changeType="positive" icon={<Truck className="w-5 h-5" />} iconBg="bg-purple-500/10 text-purple-400" />
      </div>
    </div>
  );
};
