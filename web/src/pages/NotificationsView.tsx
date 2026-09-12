import React, { useState, useEffect } from 'react';
import {
  CampusNotification,
  getStoredNotifications,
  toggleNotificationRead,
  markAllNotificationsRead,
  deleteNotification,
} from '../services/notificationStore';

interface NotificationsViewProps {
  onNavigateSub?: (
    view: 'attendance' | 'assignments' | 'exams' | 'placements' | 'announcements' | 'notifications'
  ) => void;
}

export const NotificationsView: React.FC<NotificationsViewProps> = ({ onNavigateSub }) => {
  const [notifications, setNotifications] = useState<CampusNotification[]>(() => getStoredNotifications());
  const [activeCategory, setActiveCategory] = useState<string>('all');

  useEffect(() => {
    const handleUpdate = () => {
      setNotifications(getStoredNotifications());
    };
    window.addEventListener('unisphere_notifications_updated', handleUpdate);
    return () => window.removeEventListener('unisphere_notifications_updated', handleUpdate);
  }, []);

  const categories = [
    { id: 'all', label: 'All' },
    { id: 'exam', label: 'Exams' },
    { id: 'placement', label: 'Placements' },
    { id: 'fee', label: 'Fees' },
    { id: 'campus', label: 'Campus' },
    { id: 'academic', label: 'Academics' },
  ];

  const unreadCount = notifications.filter((n) => !n.read).length;

  const filtered = notifications.filter((n) => {
    if (activeCategory === 'all') return true;
    return n.category === activeCategory;
  });

  const handleToggleRead = (id: string, e?: React.MouseEvent) => {
    if (e) e.stopPropagation();
    const updated = toggleNotificationRead(id);
    setNotifications(updated);
  };

  const handleMarkAll = () => {
    const updated = markAllNotificationsRead();
    setNotifications(updated);
  };

  const handleDelete = (id: string, e: React.MouseEvent) => {
    e.stopPropagation();
    const updated = deleteNotification(id);
    setNotifications(updated);
  };

  return (
    <div style={{ padding: '1.25rem', display: 'flex', flexDirection: 'column', gap: '14px' }}>
      {/* Header Overview Card */}
      <div
        style={{
          background: 'linear-gradient(135deg, #1e3a8a, #0284c7)',
          padding: '1.25rem',
          borderRadius: '16px',
          color: '#fff',
          boxShadow: '0 4px 16px rgba(2, 132, 199, 0.25)',
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
        }}
      >
        <div>
          <div style={{ fontSize: '0.75rem', opacity: 0.9, fontWeight: 600 }}>
            Notifications Center
          </div>
          <div style={{ fontSize: '1.4rem', fontWeight: 800, marginTop: '2px' }}>
            {unreadCount > 0 ? `${unreadCount} Unread Alerts` : 'All Caught Up! 🎉'}
          </div>
          <div style={{ fontSize: '0.72rem', opacity: 0.85, marginTop: '2px' }}>
            Real-time university alerts, schedules & placement feeds
          </div>
        </div>
        {unreadCount > 0 && (
          <button
            onClick={handleMarkAll}
            style={{
              background: 'rgba(255, 255, 255, 0.2)',
              border: '1px solid rgba(255, 255, 255, 0.35)',
              color: '#fff',
              borderRadius: '10px',
              padding: '6px 10px',
              fontSize: '0.72rem',
              fontWeight: 700,
              cursor: 'pointer',
              whiteSpace: 'nowrap',
            }}
          >
            Mark all read ✓
          </button>
        )}
      </div>

      {/* Filter Category Chips */}
      <div
        style={{
          display: 'flex',
          gap: '8px',
          overflowX: 'auto',
          paddingBottom: '4px',
          scrollbarWidth: 'none',
        }}
      >
        {categories.map((cat) => {
          const isActive = activeCategory === cat.id;
          const count =
            cat.id === 'all'
              ? notifications.length
              : notifications.filter((n) => n.category === cat.id).length;

          return (
            <button
              key={cat.id}
              onClick={() => setActiveCategory(cat.id)}
              style={{
                flexShrink: 0,
                padding: '6px 12px',
                borderRadius: '20px',
                fontSize: '0.75rem',
                fontWeight: 700,
                cursor: 'pointer',
                border: isActive
                  ? '1px solid #38bdf8'
                  : '1px solid rgba(255, 255, 255, 0.1)',
                background: isActive
                  ? 'rgba(14, 165, 233, 0.25)'
                  : 'rgba(30, 41, 59, 0.6)',
                color: isActive ? '#38bdf8' : '#94a3b8',
                display: 'flex',
                alignItems: 'center',
                gap: '5px',
                transition: 'all 0.15s ease',
              }}
            >
              <span>{cat.label}</span>
              <span
                style={{
                  fontSize: '0.65rem',
                  padding: '1px 5px',
                  borderRadius: '10px',
                  background: isActive ? '#0284c7' : 'rgba(255, 255, 255, 0.1)',
                  color: '#fff',
                }}
              >
                {count}
              </span>
            </button>
          );
        })}
      </div>

      {/* Notifications List */}
      <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
        {filtered.length === 0 ? (
          <div
            className="glass-panel"
            style={{
              padding: '2rem 1rem',
              textAlign: 'center',
              color: '#94a3b8',
            }}
          >
            <div style={{ fontSize: '2rem', marginBottom: '8px' }}>📭</div>
            <div style={{ fontWeight: 700, fontSize: '0.9rem', color: '#f8fafc' }}>
              No notifications in this category
            </div>
            <div style={{ fontSize: '0.75rem', marginTop: '4px' }}>
              You're completely up to date.
            </div>
          </div>
        ) : (
          filtered.map((item) => {
            const isPriority = item.priority === 'urgent' || item.priority === 'high';
            return (
              <div
                key={item.id}
                onClick={() => handleToggleRead(item.id)}
                className="glass-panel"
                style={{
                  padding: '12px 14px',
                  borderRadius: '14px',
                  cursor: 'pointer',
                  borderLeft: !item.read ? '4px solid #38bdf8' : '4px solid transparent',
                  background: !item.read
                    ? 'rgba(15, 23, 42, 0.85)'
                    : 'rgba(15, 23, 42, 0.5)',
                  transition: 'background 0.2s',
                  position: 'relative',
                }}
              >
                <div style={{ display: 'flex', alignItems: 'flex-start', gap: '10px' }}>
                  {/* Category Icon */}
                  <div
                    style={{
                      width: '36px',
                      height: '36px',
                      borderRadius: '10px',
                      background:
                        item.category === 'exam'
                          ? 'rgba(239, 68, 68, 0.15)'
                          : item.category === 'placement'
                          ? 'rgba(16, 185, 129, 0.15)'
                          : item.category === 'fee'
                          ? 'rgba(245, 158, 11, 0.15)'
                          : 'rgba(56, 189, 248, 0.15)',
                      display: 'flex',
                      alignItems: 'center',
                      justifyContent: 'center',
                      fontSize: '1.2rem',
                      flexShrink: 0,
                    }}
                  >
                    {item.icon || '🔔'}
                  </div>

                  {/* Body */}
                  <div style={{ flex: 1, minWidth: 0 }}>
                    <div
                      style={{
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'space-between',
                        gap: '6px',
                      }}
                    >
                      <div
                        style={{
                          fontSize: '0.85rem',
                          fontWeight: item.read ? 600 : 800,
                          color: item.read ? '#cbd5e1' : '#f8fafc',
                          lineHeight: 1.3,
                        }}
                      >
                        {item.title}
                      </div>
                      <span
                        style={{
                          fontSize: '0.65rem',
                          color: '#64748b',
                          whiteSpace: 'nowrap',
                          flexShrink: 0,
                        }}
                      >
                        {item.timeAgo}
                      </span>
                    </div>

                    <div
                      style={{
                        fontSize: '0.74rem',
                        color: '#94a3b8',
                        marginTop: '4px',
                        lineHeight: 1.4,
                      }}
                    >
                      {item.message}
                    </div>

                    {/* Footer tags and actions */}
                    <div
                      style={{
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'space-between',
                        marginTop: '8px',
                      }}
                    >
                      <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                        <span
                          style={{
                            fontSize: '0.62rem',
                            fontWeight: 700,
                            padding: '2px 6px',
                            borderRadius: '6px',
                            textTransform: 'uppercase',
                            background: 'rgba(255, 255, 255, 0.08)',
                            color: '#94a3b8',
                          }}
                        >
                          {item.category}
                        </span>
                        {isPriority && (
                          <span
                            style={{
                              fontSize: '0.62rem',
                              fontWeight: 700,
                              padding: '2px 6px',
                              borderRadius: '6px',
                              background: 'rgba(239, 68, 68, 0.2)',
                              color: '#f87171',
                            }}
                          >
                            {item.priority === 'urgent' ? 'Urgent' : 'Important'}
                          </span>
                        )}
                        {!item.read && (
                          <span
                            style={{
                              width: '6px',
                              height: '6px',
                              borderRadius: '50%',
                              backgroundColor: '#38bdf8',
                              display: 'inline-block',
                            }}
                          />
                        )}
                        {onNavigateSub && (
                          <button
                            onClick={(e) => {
                              e.stopPropagation();
                              if (item.category === 'exam') onNavigateSub('exams');
                              else if (item.category === 'placement') onNavigateSub('placements');
                              else if (item.category === 'academic') onNavigateSub('attendance');
                              else if (item.category === 'campus') onNavigateSub('announcements');
                            }}
                            style={{
                              background: 'none',
                              border: 'none',
                              color: '#38bdf8',
                              fontSize: '0.68rem',
                              fontWeight: 700,
                              cursor: 'pointer',
                              padding: '0 4px',
                            }}
                          >
                            {item.category === 'exam'
                              ? 'Exams ›'
                              : item.category === 'placement'
                              ? 'Placements ›'
                              : item.category === 'academic'
                              ? 'Attendance ›'
                              : 'Announcements ›'}
                          </button>
                        )}
                      </div>

                      <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                        <button
                          onClick={(e) => handleToggleRead(item.id, e)}
                          title={item.read ? 'Mark as unread' : 'Mark as read'}
                          style={{
                            background: 'none',
                            border: 'none',
                            color: item.read ? '#64748b' : '#38bdf8',
                            fontSize: '0.75rem',
                            cursor: 'pointer',
                            padding: '2px',
                          }}
                        >
                          {item.read ? 'Mark unread' : '✓ Read'}
                        </button>
                        <button
                          onClick={(e) => handleDelete(item.id, e)}
                          title="Dismiss notification"
                          style={{
                            background: 'none',
                            border: 'none',
                            color: '#64748b',
                            fontSize: '0.8rem',
                            cursor: 'pointer',
                            padding: '2px',
                          }}
                        >
                          ✕
                        </button>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            );
          })
        )}
      </div>
    </div>
  );
};
