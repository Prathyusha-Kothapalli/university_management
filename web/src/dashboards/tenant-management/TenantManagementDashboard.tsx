import React from 'react';
import { StatCard } from '../../components/charts/StatCard';
import { Building2, Globe, ShieldCheck, CreditCard } from 'lucide-react';

export const TenantManagementDashboard: React.FC = () => {
  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold text-white tracking-tight flex items-center gap-2">
          <Building2 className="w-6 h-6 text-indigo-400" /> Multi-Tenant Provisioning Hub
        </h1>
        <p className="text-xs text-slate-400">Institutional onboarding, custom domain mapping, and SaaS subscription tiers</p>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <StatCard title="Onboarded Colleges" value="14 Campuses" icon={<Building2 className="w-5 h-5" />} />
        <StatCard title="Custom Domain Mappings" value="14 Active DNS" icon={<Globe className="w-5 h-5" />} iconBg="bg-sky-500/10 text-sky-400" />
        <StatCard title="Tenant DB Isolation" value="Schema Isolated" icon={<ShieldCheck className="w-5 h-5" />} iconBg="bg-emerald-500/10 text-emerald-400" />
        <StatCard title="ARR SaaS Subscription" value="₹85 Lakhs" icon={<CreditCard className="w-5 h-5" />} iconBg="bg-purple-500/10 text-purple-400" />
      </div>
    </div>
  );
};
