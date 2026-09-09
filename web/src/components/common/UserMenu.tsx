import React, { useState } from 'react';
import { useAuth } from '../../hooks/useAuth';
import { User, LogOut, Shield, ChevronDown, Sparkles } from 'lucide-react';
import { useNavigate } from 'react-router-dom';
import { Badge } from '../ui/Badge';

export const UserMenu: React.FC = () => {
  const { user, logout } = useAuth();
  const [isOpen, setIsOpen] = useState(false);
  const navigate = useNavigate();

  if (!user) return null;

  const handleLogout = async () => {
    await logout();
    navigate('/login');
  };

  return (
    <div className="relative">
      <button
        onClick={() => setIsOpen(!isOpen)}
        className="flex items-center gap-3 p-1.5 rounded-xl hover:bg-slate-800/80 transition-all border border-transparent hover:border-slate-700/60"
      >
        <div className="w-8 h-8 rounded-lg bg-gradient-to-tr from-sky-600 to-indigo-600 flex items-center justify-center font-bold text-white text-sm shadow-md">
          {user.name ? user.name.charAt(0).toUpperCase() : 'U'}
        </div>
        <div className="hidden sm:flex flex-col text-left">
          <span className="text-xs font-semibold text-slate-200 leading-tight">{user.name}</span>
          <span className="text-[10px] text-sky-400 font-medium tracking-wide uppercase">
            {user.role.replace('_', ' ')}
          </span>
        </div>
        <ChevronDown className="w-4 h-4 text-slate-400 hidden sm:block" />
      </button>

      {isOpen && (
        <div className="absolute right-0 mt-3 w-64 glass-panel rounded-2xl shadow-2xl border border-slate-700/60 overflow-hidden z-50 animate-in fade-in zoom-in-95 duration-150">
          <div className="p-4 border-b border-slate-800 bg-slate-900/60">
            <p className="text-xs font-semibold text-slate-100">{user.name}</p>
            <p className="text-xs text-slate-400 truncate">{user.email}</p>
            <div className="mt-2 flex items-center gap-2">
              <Badge variant="purple" className="text-[10px] uppercase">
                {user.role}
              </Badge>
              <span className="text-[10px] text-slate-400">{user.department}</span>
            </div>
          </div>

          <div className="p-2 space-y-1">
            <button
              onClick={() => {
                navigate('/profile');
                setIsOpen(false);
              }}
              className="w-full flex items-center gap-2.5 px-3 py-2 rounded-xl text-xs text-slate-300 hover:text-white hover:bg-slate-800 transition-all"
            >
              <User className="w-4 h-4 text-sky-400" />
              <span>User Profile</span>
            </button>

            <button
              onClick={() => {
                navigate('/ai-intelligence/dashboard');
                setIsOpen(false);
              }}
              className="w-full flex items-center gap-2.5 px-3 py-2 rounded-xl text-xs text-slate-300 hover:text-white hover:bg-slate-800 transition-all"
            >
              <Sparkles className="w-4 h-4 text-amber-400" />
              <span>AI Assistant</span>
            </button>

            <button
              onClick={() => {
                navigate('/security/dashboard');
                setIsOpen(false);
              }}
              className="w-full flex items-center gap-2.5 px-3 py-2 rounded-xl text-xs text-slate-300 hover:text-white hover:bg-slate-800 transition-all"
            >
              <Shield className="w-4 h-4 text-emerald-400" />
              <span>Security & Roles</span>
            </button>
          </div>

          <div className="p-2 border-t border-slate-800/80 bg-slate-900/40">
            <button
              onClick={handleLogout}
              className="w-full flex items-center gap-2.5 px-3 py-2 rounded-xl text-xs font-medium text-rose-400 hover:bg-rose-500/10 transition-all"
            >
              <LogOut className="w-4 h-4" />
              <span>Sign Out</span>
            </button>
          </div>
        </div>
      )}
    </div>
  );
};
