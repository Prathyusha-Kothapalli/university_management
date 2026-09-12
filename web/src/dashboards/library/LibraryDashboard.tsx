import React from 'react';
import { StatCard } from '../../components/charts/StatCard';
import { Book, Bookmark, Clock, CheckCircle2 } from 'lucide-react';

export const LibraryDashboard: React.FC = () => {
  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold text-white tracking-tight flex items-center gap-2">
          <Book className="w-6 h-6 text-amber-400" /> University Library System
        </h1>
        <p className="text-xs text-slate-400">Book catalog, digital IEEE/Springer subscriptions, issue returns & fines</p>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <StatCard title="Total Library Books" value="64,500 Titles" icon={<Book className="w-5 h-5" />} />
        <StatCard title="Currently Issued" value="4,120 Books" icon={<Bookmark className="w-5 h-5" />} iconBg="bg-sky-500/10 text-sky-400" />
        <StatCard title="Overdue Returns" value="84 Books" icon={<Clock className="w-5 h-5" />} iconBg="bg-amber-500/10 text-amber-400" />
        <StatCard title="E-Journal Subscriptions" value="12 Databases" icon={<CheckCircle2 className="w-5 h-5" />} iconBg="bg-emerald-500/10 text-emerald-400" />
      </div>
    </div>
  );
};
