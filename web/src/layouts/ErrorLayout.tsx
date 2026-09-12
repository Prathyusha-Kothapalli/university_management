import React from 'react';
import { Outlet } from 'react-router-dom';

export const ErrorLayout: React.FC = () => {
  return (
    <div className="min-h-screen bg-slate-950 flex items-center justify-center p-4">
      <div className="max-w-md w-full text-center">
        <Outlet />
      </div>
    </div>
  );
};
