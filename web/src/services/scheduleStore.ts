import { ScheduleItem } from '../types/auth';
import { mockSchedule } from './mockData';

const STORAGE_KEY = 'unisphere_timetable_schedule';

export const getStoredSchedule = (): ScheduleItem[] => {
  try {
    const data = localStorage.getItem(STORAGE_KEY);
    if (data) {
      const parsed = JSON.parse(data);
      if (Array.isArray(parsed) && parsed.length > 0) {
        return parsed;
      }
    }
  } catch (e) {
    console.error('Error reading schedule from localStorage', e);
  }
  return mockSchedule;
};

export const saveStoredSchedule = (items: ScheduleItem[]): void => {
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(items));
    // Dispatch custom event for cross-component sync if needed
    window.dispatchEvent(new CustomEvent('unisphere_schedule_updated', { detail: items }));
  } catch (e) {
    console.error('Error saving schedule to localStorage', e);
  }
};

export const addScheduleItem = (
  item: Omit<ScheduleItem, 'id'>
): ScheduleItem[] => {
  const current = getStoredSchedule();
  const newItem: ScheduleItem = {
    ...item,
    id: `sch_${Date.now()}`,
  };
  const updated = [...current, newItem];
  saveStoredSchedule(updated);
  return updated;
};

export const updateScheduleItem = (
  id: string,
  updates: Partial<ScheduleItem>
): ScheduleItem[] => {
  const current = getStoredSchedule();
  const updated = current.map((item) =>
    item.id === id ? { ...item, ...updates } : item
  );
  saveStoredSchedule(updated);
  return updated;
};

export const deleteScheduleItem = (id: string): ScheduleItem[] => {
  const current = getStoredSchedule();
  const updated = current.filter((item) => item.id !== id);
  saveStoredSchedule(updated);
  return updated;
};

export const resetScheduleToDefault = (): ScheduleItem[] => {
  saveStoredSchedule(mockSchedule);
  return mockSchedule;
};
