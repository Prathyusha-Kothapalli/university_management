import React from 'react';
import { Button } from '../../components/ui/Button';
import { useNavigate } from 'react-router-dom';
import { ShieldAlert, ArrowLeft } from 'lucide-react';

export const Unauthorized: React.FC = () => {
  const navigate = useNavigate();

  return (
    <div className="flex flex-col items-center justify-center min-h-[70vh] text-center space-y-4 px-4">
      <div className="p-4 rounded-2xl bg-rose-500/10 border border-rose-500/30 text-rose-400">
        <ShieldAlert className="w-16 h-16" />
      </div>
      <h1 className="text-6xl font-black text-white tracking-tight">403</h1>
      <h2 className="text-xl font-bold text-slate-200">Access Restricted</h2>
      <p className="text-xs text-slate-400 max-w-sm">
        You do not possess the required RBAC permissions to view this ERP module. Contact your System Administrator if you believe this is an error.
      </p>
      <Button onClick={() => navigate('/')} variant="outline" className="gap-2">
        <ArrowLeft className="w-4 h-4" /> Back to Safety
      </Button>
    </div>
  );
};
