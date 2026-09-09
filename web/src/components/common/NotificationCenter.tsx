import React, { useState } from 'react';
import { Bell, Check, Trash2, Calendar, AlertTriangle, Info } from 'lucide-react';
import { Badge } from '../ui/Badge';

interface Notification {
  id: string;
  title: string;
  message: string;
  timestamp: string;
  type: 'info' | 'warning' | 'urgent';
  read: boolean;
}

export const NotificationCenter: React.FC = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [notifications, setNotifications] = useState<Notification[]>([
    {
      id: '1',
      title: 'Examination Schedule Published',
      message: 'Fall Semester Final Exams schedule has been released by Exam Cell.',
      timestamp: '10m ago',
      type: 'info',
      read: false,
    },
    {
      id: '2',
      title: 'Fee Due Reminder',
      message: 'Pending tuition fees payment due date is 15th Sept.',
      timestamp: '2h ago',
      type: 'warning',
      read: false,
    },
    {
      id: '3',
      title: 'Low Attendance Alert',
      message: 'Computer Science II Section B average attendance dropped below 80%.',
      timestamp: '1d ago',
      type: 'urgent',
      read: true,
    },
  ]);

  const unreadCount = notifications.filter((n) => !n.read).length;

  const markAllRead = () => {
    setNotifications((prev) => prev.map((n) => ({ ...n, read: true })));
  };

  const clearAll = () => {
    setNotifications([]);
  };

  return (
    <div className="relative">
      <button
        onClick={() => setIsOpen(!isOpen)}
        className="relative p-2 rounded-xl text-slate-300 hover:text-white hover:bg-slate-800/80 transition-all border border-transparent hover:border-slate-700/50"
      >
        <Bell className="w-5 h-5" />
        {unreadCount > 0 && (
          <span className="absolute top-1.5 right-1.5 flex h-2.5 w-2.5">
            <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-sky-400 opacity-75"></span>
            <span className="relative inline-flex rounded-full h-2.5 w-2.5 bg-sky-500"></span>
          </span>
        )}
      </button>

      {isOpen && (
        <div className="absolute right-0 mt-3 w-80 sm:w-96 glass-panel rounded-2xl shadow-2xl border border-slate-700/60 overflow-hidden z-50 animate-in fade-in zoom-in-95 duration-150">
          <div className="p-4 border-b border-slate-800 flex items-center justify-between bg-slate-900/50">
            <div className="flex items-center gap-2">
              <h3 className="text-sm font-semibold text-slate-100">Notifications</h3>
              {unreadCount > 0 && (
                <Badge variant="info" className="text-[10px] px-1.5 py-0">
                  {unreadCount} new
                </Badge>
              )}
            </div>
            <div className="flex items-center gap-2 text-xs text-slate-400">
              <button
                onClick={markAllRead}
                className="hover:text-sky-400 flex items-center gap-1 transition-colors"
                title="Mark all as read"
              >
                <Check className="w-3.5 h-3.5" />
              </button>
              <button
                onClick={clearAll}
                className="hover:text-rose-400 flex items-center gap-1 transition-colors"
                title="Clear all"
              >
                <Trash2 className="w-3.5 h-3.5" />
              </button>
            </div>
          </div>

          <div className="max-h-80 overflow-y-auto divide-y divide-slate-800/60">
            {notifications.length > 0 ? (
              notifications.map((n) => (
                <div
                  key={n.id}
                  className={`p-4 transition-colors ${
                    n.read ? 'bg-slate-900/20 opacity-70' : 'bg-slate-800/40 hover:bg-slate-800/60'
                  }`}
                >
                  <div className="flex items-start gap-3">
                    <div className="p-2 rounded-lg bg-slate-800 text-sky-400 mt-0.5">
                      {n.type === 'urgent' ? (
                        <AlertTriangle className="w-4 h-4 text-rose-400" />
                      ) : n.type === 'warning' ? (
                        <Calendar className="w-4 h-4 text-amber-400" />
                      ) : (
                        <Info className="w-4 h-4 text-sky-400" />
                      )}
                    </div>
                    <div className="flex-1 min-w-0">
                      <div className="flex items-center justify-between">
                        <h4 className="text-xs font-semibold text-slate-200 truncate">{n.title}</h4>
                        <span className="text-[10px] text-slate-500">{n.timestamp}</span>
                      </div>
                      <p className="text-xs text-slate-400 mt-1 line-clamp-2">{n.message}</p>
                    </div>
                  </div>
                </div>
              ))
            ) : (
              <div className="p-8 text-center text-xs text-slate-500">
                No notifications right now
              </div>
            )}
          </div>

          <div className="p-2.5 bg-slate-900/80 border-t border-slate-800 text-center text-xs text-slate-400">
            <span>COLLEXA Realtime Notification Hub</span>
          </div>
        </div>
      )}
    </div>
  );
};
