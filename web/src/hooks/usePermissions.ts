import { useAuth } from './useAuth';
import { UserRole } from '../types/user';

export function usePermissions() {
  const { user } = useAuth();

  const hasPermission = (requiredPermission: string): boolean => {
    if (!user) return false;
    if (user.role === 'SUPER_ADMIN' || user.role === 'SYSTEM_ADMIN') return true;
    return user.permissions?.includes(requiredPermission) || false;
  };

  const hasAnyPermission = (requiredPermissions: string[]): boolean => {
    if (!user) return false;
    if (user.role === 'SUPER_ADMIN' || user.role === 'SYSTEM_ADMIN') return true;
    return requiredPermissions.some((perm) => user.permissions?.includes(perm));
  };

  const hasAllPermissions = (requiredPermissions: string[]): boolean => {
    if (!user) return false;
    if (user.role === 'SUPER_ADMIN' || user.role === 'SYSTEM_ADMIN') return true;
    return requiredPermissions.every((perm) => user.permissions?.includes(perm));
  };

  const hasRole = (role: UserRole | UserRole[]): boolean => {
    if (!user) return false;
    if (Array.isArray(role)) {
      return role.includes(user.role);
    }
    return user.role === role;
  };

  return {
    userPermissions: user?.permissions || [],
    userRole: user?.role,
    hasPermission,
    hasAnyPermission,
    hasAllPermissions,
    hasRole,
  };
}
