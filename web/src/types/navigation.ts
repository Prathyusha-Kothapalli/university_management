import { UserRole } from './user';

export interface NavItem {
  title: string;
  href: string;
  iconName: string;
  badge?: string;
  badgeVariant?: 'default' | 'success' | 'warning' | 'destructive' | 'info';
  requiredPermissions?: string[];
  allowedRoles?: UserRole[];
  children?: NavItem[];
}

export interface NavSection {
  sectionTitle?: string;
  items: NavItem[];
}

export type DynamicNavConfig = Record<UserRole, NavSection[]>;
