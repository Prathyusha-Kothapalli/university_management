import { Announcement } from '../types/auth';

const STORAGE_KEY = 'unisphere_announcements_data';

export const initialAnnouncements: Announcement[] = [
  {
    id: 'ann-1',
    title: 'Google & NVIDIA Campus Placement Drives 2026',
    date: 'Sep 08, 2026',
    category: 'Placement',
    content: 'Registration window is now live for all Final and Pre-Final Year students with CGPA ≥ 8.0. Test rounds commence on September 25.',
    author: 'Campus Placement Cell',
    targetRole: 'all',
  },
  {
    id: 'ann-2',
    title: 'Mid-Term Examination Schedule Released',
    date: 'Sep 06, 2026',
    category: 'Exam',
    content: 'The formal timetable for Midterm Exams (Fall 2026) has been updated. Hall ticket generation is active on your portal.',
    author: 'Office of the Controller of Examinations',
    targetRole: 'all',
  },
  {
    id: 'ann-3',
    title: 'Faculty Senate: AI & Data Science Curriculum Review',
    date: 'Sep 05, 2026',
    category: 'Faculty',
    content: 'All department professors are invited to the Academic Senate meeting on Friday at 03:00 PM in Conference Hall A to review the 2027 curriculum revisions.',
    author: 'Dean of Academics',
    targetRole: 'faculty',
  },
  {
    id: 'ann-4',
    title: 'Annual Inter-University Hackathon 2026',
    date: 'Sep 02, 2026',
    category: 'Campus',
    content: 'Registrations are open for the 48-hour AI Innovation Hackathon. Over $50,000 in prizes and direct interview opportunities with tech sponsors.',
    author: 'Student Affairs & Tech Council',
    targetRole: 'all',
  },
  {
    id: 'ann-5',
    title: '24/7 Digital Library & Study Pod Access During Exams',
    date: 'Aug 28, 2026',
    category: 'Academic',
    content: 'The Central University Library, IEEE/ACM digital terminal rooms, and collaborative study spaces will operate 24 hours daily through midterm week.',
    author: 'Head University Librarian',
    targetRole: 'all',
  },
  {
    id: 'ann-6',
    title: 'National Research Grant & Lab Equipment Proposals',
    date: 'Aug 25, 2026',
    category: 'Faculty',
    content: 'Faculty members seeking seed funding for deep learning and robotics laboratory equipment must submit their research abstracts before October 15.',
    author: 'Director of Research & Development',
    targetRole: 'faculty',
  },
];

export const getStoredAnnouncements = (): Announcement[] => {
  try {
    const data = localStorage.getItem(STORAGE_KEY);
    if (data) {
      const parsed = JSON.parse(data);
      if (Array.isArray(parsed) && parsed.length > 0) {
        return parsed;
      }
    }
  } catch (e) {
    console.error('Error reading announcements from localStorage', e);
  }
  return initialAnnouncements;
};

export const saveStoredAnnouncements = (items: Announcement[]): void => {
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(items));
    window.dispatchEvent(new CustomEvent('unisphere_announcements_updated', { detail: items }));
  } catch (e) {
    console.error('Error saving announcements to localStorage', e);
  }
};

export const addAnnouncement = (
  item: Omit<Announcement, 'id' | 'date'>
): Announcement[] => {
  const current = getStoredAnnouncements();
  const dateStr = new Date().toLocaleDateString('en-US', {
    month: 'short',
    day: '2-digit',
    year: 'numeric',
  });

  const newAnn: Announcement = {
    ...item,
    id: `ann-${Date.now()}`,
    date: dateStr,
  };

  const updated = [newAnn, ...current];
  saveStoredAnnouncements(updated);
  return updated;
};

export const deleteAnnouncement = (id: string): Announcement[] => {
  const current = getStoredAnnouncements();
  const updated = current.filter((item) => item.id !== id);
  saveStoredAnnouncements(updated);
  return updated;
};
