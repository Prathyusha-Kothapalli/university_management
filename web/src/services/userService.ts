import { apiRequest } from './api';
import { User } from '../types/user';

export const userService = {
  async getUsers(): Promise<User[]> {
    try {
      return await apiRequest<User[]>('/users');
    } catch {
      return [
        { id: '1', name: 'Rahul Kumar', email: 'rahul@collexa.com', role: 'STUDENT', permissions: ['attendance.view'], status: 'ACTIVE' },
        { id: '2', name: 'Dr. Anaya Verma', email: 'anaya@collexa.com', role: 'FACULTY', permissions: ['attendance.create'], status: 'ACTIVE' },
      ];
    }
  },

  async getUserById(id: string): Promise<User> {
    return await apiRequest<User>(`/users/${id}`);
  },
};
