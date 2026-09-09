import React from 'react';
import { Button } from '../../components/ui/Button';
import { useNavigate } from 'react-router-dom';
import { Compass, Home } from 'lucide-react';

export const NotFound: React.FC = () => {
  const navigate = useNavigate();

  return (
    <div className="flex flex-col items-center justify-center min-h-[70vh] text-center space-y-4 px-4">
      <div className="p-4 rounded-2xl bg-sky-500/10 border border-sky-500/30 text-sky-400">
        <Compass className="w-16 h-16 animate-pulse" />
      </div>
      <h1 className="text-6xl font-black text-white tracking-tight">404</h1>
      <h2 className="text-xl font-bold text-slate-200">Page Not Found</h2>
      <p className="text-xs text-slate-400 max-w-sm">
        The requested ERP route or module location does not exist or has been relocated.
      </p>
      <Button onClick={() => navigate('/')} variant="primary" className="gap-2">
        <Home className="w-4 h-4" /> Return to Dashboard
      </Button>
    </div>
  );
};
