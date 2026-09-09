import React from 'react';
import { useAuth } from '../../hooks/useAuth';
import { Card, CardHeader, CardTitle, CardContent } from '../../components/ui/Card';
import { Badge } from '../../components/ui/Badge';
import { Shield, Building, CheckCircle2 } from 'lucide-react';

export const Profile: React.FC = () => {
  const { user } = useAuth();

  if (!user) return null;

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold text-white tracking-tight">User Profile</h1>
          <p className="text-xs text-slate-400">Account overview and assigned security credentials</p>
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Profile Card */}
        <Card className="glass-card">
          <CardContent className="p-6 text-center space-y-4">
            <div className="w-24 h-24 mx-auto rounded-2xl bg-gradient-to-tr from-sky-500 to-indigo-600 flex items-center justify-center text-4xl font-extrabold text-white shadow-xl shadow-sky-500/20">
              {user.name.charAt(0)}
            </div>
            <div>
              <h2 className="text-xl font-bold text-white">{user.name}</h2>
              <p className="text-xs text-slate-400 mt-1">{user.email}</p>
            </div>
            <div className="flex items-center justify-center gap-2">
              <Badge variant="purple" className="uppercase font-bold">
                {user.role}
              </Badge>
              <Badge variant="success" className="gap-1">
                <CheckCircle2 className="w-3 h-3" /> Active
              </Badge>
            </div>
          </CardContent>
        </Card>

        {/* Details Card */}
        <Card className="glass-card lg:col-span-2">
          <CardHeader>
            <CardTitle>Professional Details</CardTitle>
          </CardHeader>
          <CardContent className="space-y-4">
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 text-xs">
              <div className="p-3.5 rounded-xl bg-slate-900/60 border border-slate-800 space-y-1">
                <span className="text-slate-500 flex items-center gap-1.5 font-medium">
                  <Building className="w-3.5 h-3.5 text-sky-400" /> Institution / Department
                </span>
                <p className="text-slate-200 font-semibold">{user.institutionName || 'Apex University'}</p>
                <p className="text-slate-400">{user.department}</p>
              </div>

              <div className="p-3.5 rounded-xl bg-slate-900/60 border border-slate-800 space-y-1">
                <span className="text-slate-500 flex items-center gap-1.5 font-medium">
                  <Shield className="w-3.5 h-3.5 text-emerald-400" /> Security Role Code
                </span>
                <p className="text-slate-200 font-mono font-semibold">{user.role}</p>
                <p className="text-slate-400">User ID: {user.id}</p>
              </div>
            </div>

            <div className="pt-4 border-t border-slate-800 space-y-3">
              <h4 className="text-xs font-semibold text-slate-300 uppercase tracking-wider">
                Assigned RBAC Permissions
              </h4>
              <div className="flex flex-wrap gap-1.5">
                {user.permissions?.map((perm, idx) => (
                  <Badge key={idx} variant="outline" className="font-mono text-[11px]">
                    {perm}
                  </Badge>
                ))}
              </div>
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  );
};
