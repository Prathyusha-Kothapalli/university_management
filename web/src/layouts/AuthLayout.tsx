import React from 'react';
import { Outlet } from 'react-router-dom';
import { GraduationCap } from 'lucide-react';

export const AuthLayout: React.FC = () => {
  return (
    <div className="min-h-screen bg-slate-950 flex flex-col justify-center items-center p-4 relative overflow-hidden font-sans">
      {/* Dynamic Background Glows */}
      <div className="absolute top-1/4 left-1/4 w-96 h-96 bg-sky-600/20 rounded-full blur-3xl pointer-events-none" />
      <div className="absolute bottom-1/4 right-1/4 w-96 h-96 bg-indigo-600/20 rounded-full blur-3xl pointer-events-none" />

      {/* Header Branding */}
      <div className="mb-6 text-center flex flex-col items-center gap-2 z-10">
        <div className="p-3 rounded-2xl bg-gradient-to-tr from-sky-500 to-indigo-600 text-white shadow-xl shadow-sky-500/20">
          <GraduationCap className="w-8 h-8" />
        </div>
        <h1 className="text-3xl font-extrabold tracking-tight text-white">COLLEXA</h1>
        <p className="text-xs text-sky-400 font-semibold tracking-wider uppercase">
          Enterprise College ERP Platform
        </p>
      </div>

      {/* Auth Card Container */}
      <div className="w-full max-w-md z-10">
        <Outlet />
      </div>

      {/* Footer copyright */}
      <footer className="mt-8 text-center text-xs text-slate-500 z-10">
        &copy; {new Date().getFullYear()} COLLEXA Enterprise. All rights reserved.
      </footer>
    </div>
  );
};
