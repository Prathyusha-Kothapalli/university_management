import React from 'react';
import { NavLink } from 'react-router-dom';
import { useAuth } from '../../hooks/useAuth';
import { ROLE_NAVIGATION } from '../../config/navigation';
import { UserRole } from '../../types/user';
import { cn } from '../../lib/utils';
import * as LucideIcons from 'lucide-react';
import { GraduationCap, ChevronLeft, ChevronRight, LogOut } from 'lucide-react';

interface SidebarProps {
  isCollapsed: boolean;
  onToggleCollapse: () => void;
  isMobileOpen: boolean;
  onCloseMobile: () => void;
}

const DynamicIcon: React.FC<{ name: string; className?: string }> = ({ name, className = 'w-4 h-4' }) => {
  const IconComponent = (LucideIcons as any)[name] || LucideIcons.LayoutDashboard;
  return <IconComponent className={className} />;
};

export const Sidebar: React.FC<SidebarProps> = ({
  isCollapsed,
  onToggleCollapse,
  isMobileOpen,
  onCloseMobile,
}) => {
  const { user, logout } = useAuth();

  if (!user) return null;

  const role = user.role as UserRole;
  const navSections = ROLE_NAVIGATION[role] || ROLE_NAVIGATION['STUDENT'];

  return (
    <>
      {/* Mobile Backdrop Overlay */}
      {isMobileOpen && (
        <div
          onClick={onCloseMobile}
          className="fixed inset-0 z-40 bg-slate-950/80 backdrop-blur-sm lg:hidden animate-in fade-in"
        />
      )}

      {/* Sidebar Container */}
      <aside
        className={cn(
          'fixed top-0 bottom-0 left-0 z-50 flex flex-col bg-slate-950/95 border-r border-slate-800/80 backdrop-blur-2xl transition-all duration-300 ease-in-out',
          isCollapsed ? 'w-20' : 'w-64',
          isMobileOpen ? 'translate-x-0' : '-translate-x-full lg:translate-x-0'
        )}
      >
        {/* Brand Header */}
        <div className="h-16 px-4 flex items-center justify-between border-b border-slate-800/80">
          <div className="flex items-center gap-3 overflow-hidden">
            <div className="p-2 rounded-xl bg-gradient-to-tr from-sky-500 to-indigo-600 text-white shadow-lg shadow-sky-500/20 shrink-0">
              <GraduationCap className="w-5 h-5" />
            </div>
            {!isCollapsed && (
              <div className="flex flex-col">
                <span className="text-base font-bold tracking-tight text-white leading-none">
                  COLLEXA
                </span>
                <span className="text-[10px] text-sky-400 font-semibold tracking-wider uppercase mt-1">
                  Enterprise ERP
                </span>
              </div>
            )}
          </div>

          {/* Desktop Collapse Toggle */}
          <button
            onClick={onToggleCollapse}
            className="hidden lg:flex p-1.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800/80 transition-all border border-slate-800"
          >
            {isCollapsed ? <ChevronRight className="w-4 h-4" /> : <ChevronLeft className="w-4 h-4" />}
          </button>
        </div>

        {/* User Persona Card */}
        {!isCollapsed && (
          <div className="mx-3 mt-4 p-3 rounded-xl bg-slate-900/60 border border-slate-800/80 flex items-center gap-3">
            <div className="w-9 h-9 rounded-lg bg-sky-600/30 border border-sky-500/40 text-sky-400 flex items-center justify-center font-bold text-sm shrink-0">
              {user.name.charAt(0)}
            </div>
            <div className="min-w-0 flex-1">
              <p className="text-xs font-semibold text-slate-200 truncate">{user.name}</p>
              <p className="text-[10px] text-sky-400 font-mono tracking-tight uppercase truncate">
                {user.role}
              </p>
            </div>
          </div>
        )}

        {/* Dynamic Navigation Sections */}
        <div className="flex-1 overflow-y-auto px-3 py-4 space-y-6">
          {navSections.map((section, sIdx) => (
            <div key={sIdx} className="space-y-1">
              {!isCollapsed && section.sectionTitle && (
                <h4 className="px-3 text-[10px] font-semibold uppercase tracking-wider text-slate-400 mb-2">
                  {section.sectionTitle}
                </h4>
              )}
              {section.items.map((item, iIdx) => (
                <NavLink
                  key={iIdx}
                  to={item.href}
                  onClick={onCloseMobile}
                  className={({ isActive }) =>
                    cn(
                      'flex items-center gap-3 px-3 py-2.5 rounded-xl text-xs font-medium transition-all group relative',
                      isActive
                        ? 'bg-gradient-to-r from-sky-500/20 to-indigo-500/10 text-sky-400 font-semibold border border-sky-500/30 shadow-md shadow-sky-500/5'
                        : 'text-slate-400 hover:text-slate-200 hover:bg-slate-900/60'
                    )
                  }
                >
                  <DynamicIcon name={item.iconName} className="w-4 h-4 shrink-0 transition-transform group-hover:scale-110" />
                  {!isCollapsed && <span className="truncate">{item.title}</span>}

                  {/* Tooltip when collapsed */}
                  {isCollapsed && (
                    <div className="absolute left-full ml-3 px-2.5 py-1 rounded-md bg-slate-900 text-slate-100 text-xs font-medium whitespace-nowrap opacity-0 pointer-events-none group-hover:opacity-100 group-hover:pointer-events-auto transition-opacity shadow-xl border border-slate-700 z-50">
                      {item.title}
                    </div>
                  )}
                </NavLink>
              ))}
            </div>
          ))}
        </div>

        {/* Bottom Footer Actions */}
        <div className="p-3 border-t border-slate-800/80 bg-slate-950">
          <button
            onClick={logout}
            className={cn(
              'w-full flex items-center gap-3 px-3 py-2.5 rounded-xl text-xs font-medium text-rose-400 hover:bg-rose-500/10 transition-all border border-transparent hover:border-rose-500/20',
              isCollapsed && 'justify-center'
            )}
            title="Sign Out"
          >
            <LogOut className="w-4 h-4 shrink-0" />
            {!isCollapsed && <span>Sign Out</span>}
          </button>
        </div>
      </aside>
    </>
  );
};
