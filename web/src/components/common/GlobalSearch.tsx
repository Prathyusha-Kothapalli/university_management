import React, { useState, useEffect } from 'react';
import { Search, X, Command, BookOpen, Users, FileText, Settings, ArrowRight } from 'lucide-react';
import { useNavigate } from 'react-router-dom';

interface GlobalSearchProps {
  isOpen: boolean;
  onClose: () => void;
}

export const GlobalSearch: React.FC<GlobalSearchProps> = ({ isOpen, onClose }) => {
  const [query, setQuery] = useState('');
  const navigate = useNavigate();

  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
        e.preventDefault();
        if (isOpen) onClose();
        else setQuery('');
      }
      if (e.key === 'Escape' && isOpen) {
        onClose();
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [isOpen, onClose]);

  if (!isOpen) return null;

  const quickLinks = [
    { title: 'Student Enrollment List', type: 'Students', icon: Users, path: '/student/dashboard' },
    { title: 'Faculty Workload & Timetable', type: 'Faculty', icon: BookOpen, path: '/faculty/dashboard' },
    { title: 'Semester Examination Schedule', type: 'Exams', icon: FileText, path: '/examination/dashboard' },
    { title: 'Fee Collection Reports', type: 'Finance', icon: Settings, path: '/finance/dashboard' },
  ];

  const handleNavigate = (path: string) => {
    navigate(path);
    onClose();
  };

  return (
    <div className="fixed inset-0 z-50 flex items-start justify-center pt-20 bg-slate-950/80 backdrop-blur-md animate-in fade-in duration-200 px-4">
      <div className="relative w-full max-w-2xl glass-panel rounded-2xl shadow-2xl border border-slate-700/60 overflow-hidden">
        {/* Search Input */}
        <div className="flex items-center px-4 py-3 border-b border-slate-800">
          <Search className="w-5 h-5 text-slate-400 mr-3" />
          <input
            type="text"
            placeholder="Search students, faculty, courses, modules, or press Esc to exit..."
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            autoFocus
            className="w-full bg-transparent text-slate-100 placeholder:text-slate-500 text-sm focus:outline-none"
          />
          <button
            onClick={onClose}
            className="p-1 rounded-lg hover:bg-slate-800 text-slate-400 hover:text-white transition-all"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Results / Quick Links */}
        <div className="p-4 max-h-96 overflow-y-auto space-y-3">
          <div className="text-[11px] font-semibold tracking-wider uppercase text-slate-400 px-2 flex items-center justify-between">
            <span>Quick Navigation</span>
            <span className="flex items-center gap-1 text-slate-500">
              <Command className="w-3 h-3" /> K
            </span>
          </div>

          <div className="space-y-1">
            {quickLinks.map((item, idx) => {
              const Icon = item.icon;
              return (
                <button
                  key={idx}
                  onClick={() => handleNavigate(item.path)}
                  className="w-full flex items-center justify-between p-3 rounded-xl hover:bg-slate-800/70 transition-all text-left group border border-transparent hover:border-slate-700/50"
                >
                  <div className="flex items-center gap-3">
                    <div className="p-2 rounded-lg bg-slate-800 text-sky-400 group-hover:bg-sky-500/20 transition-all">
                      <Icon className="w-4 h-4" />
                    </div>
                    <div>
                      <h4 className="text-xs font-semibold text-slate-200 group-hover:text-white">
                        {item.title}
                      </h4>
                      <span className="text-[10px] text-slate-400">{item.type}</span>
                    </div>
                  </div>
                  <ArrowRight className="w-4 h-4 text-slate-600 group-hover:text-sky-400 group-hover:translate-x-1 transition-all" />
                </button>
              );
            })}
          </div>
        </div>

        {/* Footer */}
        <div className="px-4 py-2.5 bg-slate-900/90 border-t border-slate-800/80 text-[11px] text-slate-400 flex items-center justify-between">
          <span>Search COLLEXA Enterprise Database</span>
          <span className="text-sky-400 font-medium">v1.0.0 Global Search</span>
        </div>
      </div>
    </div>
  );
};
