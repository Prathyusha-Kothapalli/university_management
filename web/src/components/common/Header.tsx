import React, { useState, useEffect } from 'react';
import { Search, Menu, Sparkles, Command } from 'lucide-react';
import { GlobalSearch } from './GlobalSearch';
import { NotificationCenter } from './NotificationCenter';
import { UserMenu } from './UserMenu';
import { useAuth } from '../../hooks/useAuth';
import { Badge } from '../ui/Badge';

interface HeaderProps {
  onToggleMobileSidebar: () => void;
}

export const Header: React.FC<HeaderProps> = ({ onToggleMobileSidebar }) => {
  const { user } = useAuth();
  const [isSearchOpen, setIsSearchOpen] = useState(false);
  const [timeString, setTimeString] = useState('');

  useEffect(() => {
    const updateTime = () => {
      const now = new Date();
      setTimeString(
        now.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit', second: '2-digit' })
      );
    };
    updateTime();
    const interval = setInterval(updateTime, 1000);
    return () => clearInterval(interval);
  }, []);

  return (
    <>
      <header className="h-16 px-4 lg:px-8 border-b border-slate-800/80 bg-slate-950/70 backdrop-blur-xl sticky top-0 z-40 flex items-center justify-between gap-4">
        {/* Left section */}
        <div className="flex items-center gap-4">
          <button
            onClick={onToggleMobileSidebar}
            className="lg:hidden p-2 rounded-xl text-slate-400 hover:text-white hover:bg-slate-800 transition-all"
          >
            <Menu className="w-5 h-5" />
          </button>

          {/* Quick search button */}
          <button
            onClick={() => setIsSearchOpen(true)}
            className="flex items-center gap-3 px-3.5 py-1.5 rounded-xl bg-slate-900/80 hover:bg-slate-800/80 text-slate-400 text-xs border border-slate-800 transition-all w-48 sm:w-72"
          >
            <Search className="w-4 h-4 text-slate-400" />
            <span className="flex-1 text-left truncate">Search ERP modules...</span>
            <span className="hidden sm:flex items-center gap-0.5 text-[10px] bg-slate-800 px-1.5 py-0.5 rounded border border-slate-700 text-slate-400">
              <Command className="w-3 h-3" /> K
            </span>
          </button>
        </div>

        {/* Right section */}
        <div className="flex items-center gap-3 sm:gap-4">
          {/* Institution / Role Indicator */}
          {user && (
            <div className="hidden md:flex items-center gap-2 px-3 py-1 rounded-xl bg-slate-900/60 border border-slate-800/80 text-xs">
              <Sparkles className="w-3.5 h-3.5 text-sky-400" />
              <span className="text-slate-300 font-medium">{user.institutionName || 'COLLEXA ERP'}</span>
              <Badge variant="purple" className="text-[10px] uppercase font-bold py-0 px-1.5">
                {user.role}
              </Badge>
            </div>
          )}

          {/* Clock */}
          <div className="hidden xl:block text-xs font-mono text-slate-400 bg-slate-900/40 px-2.5 py-1 rounded-lg border border-slate-800/50">
            {timeString}
          </div>

          <NotificationCenter />
          <UserMenu />
        </div>
      </header>

      <GlobalSearch isOpen={isSearchOpen} onClose={() => setIsSearchOpen(false)} />
    </>
  );
};
