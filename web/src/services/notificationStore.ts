export interface CampusNotification {
  id: string;
  title: string;
  message: string;
  timestamp: string;
  timeAgo: string;
  category: 'exam' | 'placement' | 'fee' | 'campus' | 'academic';
  read: boolean;
  priority?: 'high' | 'normal' | 'urgent';
  icon?: string;
}

const STORAGE_KEY = 'unisphere_notifications_data';

export const initialNotifications: CampusNotification[] = [
  {
    id: 'notif-1',
    title: 'Midterm Hall Ticket Generated',
    message: 'Your Fall 2026 digital hall ticket and seat allocation are now available for viewing and export.',
    timestamp: '2026-09-12T10:00:00Z',
    timeAgo: '15m ago',
    category: 'exam',
    read: false,
    priority: 'urgent',
    icon: '📝',
  },
  {
    id: 'notif-2',
    title: 'Google & NVIDIA Shortlist Released',
    message: 'Congratulations! You have been shortlisted for the AI Engineering campus placement technical rounds.',
    timestamp: '2026-09-12T08:30:00Z',
    timeAgo: '2h ago',
    category: 'placement',
    read: false,
    priority: 'high',
    icon: '🎯',
  },
  {
    id: 'notif-3',
    title: 'Term 2 Tuition Fee Receipt',
    message: 'Electronic payment confirmation for Fall Semester ($4,250) has been processed successfully.',
    timestamp: '2026-09-11T14:20:00Z',
    timeAgo: '1d ago',
    category: 'fee',
    read: true,
    priority: 'normal',
    icon: '💳',
  },
  {
    id: 'notif-4',
    title: 'AI Innovation Hackathon 2026',
    message: 'Registrations are 80% full. Submit your 4-person team before the deadline this Friday.',
    timestamp: '2026-09-10T12:00:00Z',
    timeAgo: '2d ago',
    category: 'campus',
    read: false,
    priority: 'normal',
    icon: '🚀',
  },
  {
    id: 'notif-5',
    title: 'CS-401 Lab Relocation',
    message: 'Today’s Neural Architectures lab session has shifted to Turing Hall Advanced AI Lab 4.',
    timestamp: '2026-09-09T09:15:00Z',
    timeAgo: '3d ago',
    category: 'academic',
    read: true,
    priority: 'normal',
    icon: '🔬',
  },
];

export const getStoredNotifications = (): CampusNotification[] => {
  try {
    const data = localStorage.getItem(STORAGE_KEY);
    if (data) {
      const parsed = JSON.parse(data);
      if (Array.isArray(parsed) && parsed.length > 0) {
        return parsed;
      }
    }
  } catch (e) {
    console.error('Error reading notifications from localStorage', e);
  }
  return initialNotifications;
};

export const saveStoredNotifications = (items: CampusNotification[]): void => {
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(items));
    window.dispatchEvent(new CustomEvent('unisphere_notifications_updated', { detail: items }));
  } catch (e) {
    console.error('Error saving notifications to localStorage', e);
  }
};

export const toggleNotificationRead = (id: string): CampusNotification[] => {
  const current = getStoredNotifications();
  const updated = current.map((item) =>
    item.id === id ? { ...item, read: !item.read } : item
  );
  saveStoredNotifications(updated);
  return updated;
};

export const markAllNotificationsRead = (): CampusNotification[] => {
  const current = getStoredNotifications();
  const updated = current.map((item) => ({ ...item, read: true }));
  saveStoredNotifications(updated);
  return updated;
};

export const deleteNotification = (id: string): CampusNotification[] => {
  const current = getStoredNotifications();
  const updated = current.filter((item) => item.id !== id);
  saveStoredNotifications(updated);
  return updated;
};
