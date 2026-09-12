import { UserRole } from '../types/user';
import { NavSection } from '../types/navigation';

export const ROLE_NAVIGATION: Record<UserRole, NavSection[]> = {
  SUPER_ADMIN: [
    {
      sectionTitle: 'System & Admin',
      items: [
        { title: 'System Overview', href: '/super-admin/dashboard', iconName: 'ShieldAlert' },
        { title: 'Tenant Management', href: '/tenant-management/dashboard', iconName: 'Building2' },
        { title: 'System Monitoring', href: '/monitoring/dashboard', iconName: 'Activity' },
        { title: 'Security Admin', href: '/security/dashboard', iconName: 'Lock' },
        { title: 'BI & Analytics', href: '/bi/dashboard', iconName: 'BarChart3' },
      ],
    },
    {
      sectionTitle: 'Core Operations',
      items: [
        { title: 'Management', href: '/management/dashboard', iconName: 'PieChart' },
        { title: 'Principal Portal', href: '/principal/dashboard', iconName: 'Award' },
        { title: 'Admissions', href: '/admissions/dashboard', iconName: 'UserPlus' },
        { title: 'Finance & Accounts', href: '/finance/dashboard', iconName: 'CreditCard' },
        { title: 'HR & Payroll', href: '/hr/dashboard', iconName: 'Users' },
      ],
    },
  ],

  MANAGEMENT: [
    {
      sectionTitle: 'Executive',
      items: [
        { title: 'Executive Overview', href: '/management/dashboard', iconName: 'PieChart' },
        { title: 'BI & Analytics', href: '/bi/dashboard', iconName: 'BarChart3' },
        { title: 'Accreditation', href: '/accreditation/dashboard', iconName: 'CheckSquare' },
      ],
    },
    {
      sectionTitle: 'Institutions',
      items: [
        { title: 'Finance Overview', href: '/finance/dashboard', iconName: 'CreditCard' },
        { title: 'Placements & Alumni', href: '/placement-alumni/dashboard', iconName: 'Briefcase' },
        { title: 'Research & Innovation', href: '/research/dashboard', iconName: 'FileText' },
      ],
    },
  ],

  PRINCIPAL: [
    {
      sectionTitle: 'Academic Leadership',
      items: [
        { title: 'College Dashboard', href: '/principal/dashboard', iconName: 'Award' },
        { title: 'Academic Performance', href: '/attendance-analytics/dashboard', iconName: 'LineChart' },
        { title: 'Examination Cell', href: '/examination/dashboard', iconName: 'FileCheck' },
      ],
    },
    {
      sectionTitle: 'Administration',
      items: [
        { title: 'HR & Staff', href: '/hr/dashboard', iconName: 'Users' },
        { title: 'Finance Summary', href: '/finance/dashboard', iconName: 'DollarSign' },
        { title: 'Accreditation Rank', href: '/accreditation/dashboard', iconName: 'CheckSquare' },
      ],
    },
  ],

  DEAN: [
    {
      sectionTitle: 'School Operations',
      items: [
        { title: 'School Dashboard', href: '/dean/dashboard', iconName: 'Landmark' },
        { title: 'HOD Matrix', href: '/hod/dashboard', iconName: 'Grid' },
        { title: 'Research Portal', href: '/research/dashboard', iconName: 'Microscope' },
      ],
    },
  ],

  HOD: [
    {
      sectionTitle: 'Department',
      items: [
        { title: 'Department Dashboard', href: '/hod/dashboard', iconName: 'Building' },
        { title: 'Faculty & Workload', href: '/faculty/dashboard', iconName: 'UserCheck' },
        { title: 'Attendance Analytics', href: '/attendance-analytics/dashboard', iconName: 'CheckCircle2' },
        { title: 'Examination Results', href: '/examination/dashboard', iconName: 'GraduationCap' },
      ],
    },
  ],

  FACULTY: [
    {
      sectionTitle: 'Teaching',
      items: [
        { title: 'Faculty Portal', href: '/faculty/dashboard', iconName: 'BookOpen' },
        { title: 'My LMS Courses', href: '/lms/dashboard', iconName: 'Video' },
        { title: 'Attendance Logger', href: '/attendance-analytics/dashboard', iconName: 'Calendar' },
        { title: 'Exams & Grading', href: '/examination/dashboard', iconName: 'Edit3' },
      ],
    },
  ],

  STUDENT: [
    {
      sectionTitle: 'Academic Portal',
      items: [
        { title: 'Student Dashboard', href: '/student/dashboard', iconName: 'LayoutDashboard' },
        { title: 'LMS Learning Portal', href: '/lms/dashboard', iconName: 'BookOpen' },
        { title: 'Attendance & Timetable', href: '/attendance-analytics/dashboard', iconName: 'Clock' },
        { title: 'Results & Marksheets', href: '/examination/dashboard', iconName: 'FileSpreadsheet' },
        { title: 'Fee Payments', href: '/finance/dashboard', iconName: 'CreditCard' },
        { title: 'Library Portal', href: '/library/dashboard', iconName: 'Book' },
        { title: 'Placement Drive', href: '/placement-alumni/dashboard', iconName: 'Briefcase' },
      ],
    },
  ],

  PARENT: [
    {
      sectionTitle: 'Parent Portal',
      items: [
        { title: 'Ward Dashboard', href: '/parent/dashboard', iconName: 'HeartHandshake' },
        { title: 'Attendance Record', href: '/attendance-analytics/dashboard', iconName: 'Clock' },
        { title: 'Fee Status', href: '/finance/dashboard', iconName: 'CreditCard' },
        { title: 'Academic Reports', href: '/examination/dashboard', iconName: 'FileText' },
      ],
    },
  ],

  ADMISSION_TEAM: [
    {
      sectionTitle: 'Admissions',
      items: [
        { title: 'Admissions Dashboard', href: '/admissions/dashboard', iconName: 'UserPlus' },
        { title: 'Applicant Verification', href: '/admissions/dashboard', iconName: 'FileCheck' },
      ],
    },
  ],

  EXAM_CELL: [
    {
      sectionTitle: 'Examinations',
      items: [
        { title: 'Exam Cell Dashboard', href: '/examination/dashboard', iconName: 'FileCheck' },
        { title: 'Results Management', href: '/examination/dashboard', iconName: 'GraduationCap' },
      ],
    },
  ],

  FINANCE: [
    {
      sectionTitle: 'Finance & Accounts',
      items: [
        { title: 'Finance Dashboard', href: '/finance/dashboard', iconName: 'CreditCard' },
        { title: 'Fee Collections', href: '/finance/dashboard', iconName: 'DollarSign' },
        { title: 'Payroll Integration', href: '/hr/dashboard', iconName: 'Receipt' },
      ],
    },
  ],

  HR: [
    {
      sectionTitle: 'Human Resources',
      items: [
        { title: 'HR & Payroll Dashboard', href: '/hr/dashboard', iconName: 'Users' },
        { title: 'Employee Directory', href: '/hr/dashboard', iconName: 'Contact' },
      ],
    },
  ],

  LIBRARIAN: [
    {
      sectionTitle: 'Library',
      items: [
        { title: 'Library Dashboard', href: '/library/dashboard', iconName: 'Book' },
        { title: 'Book Checkouts & Fines', href: '/library/dashboard', iconName: 'Bookmark' },
      ],
    },
  ],

  CAMPUS_OPERATIONS: [
    {
      sectionTitle: 'Campus Ops',
      items: [
        { title: 'Hostel & Transport', href: '/hostel-transport/dashboard', iconName: 'Truck' },
        { title: 'Inventory Management', href: '/inventory/dashboard', iconName: 'Package' },
      ],
    },
  ],

  PLACEMENT_TEAM: [
    {
      sectionTitle: 'Placements',
      items: [
        { title: 'Placement & Alumni', href: '/placement-alumni/dashboard', iconName: 'Briefcase' },
      ],
    },
  ],

  LMS_ADMIN: [
    {
      sectionTitle: 'Learning System',
      items: [
        { title: 'LMS Admin Portal', href: '/lms/dashboard', iconName: 'Video' },
      ],
    },
  ],

  RESEARCH_TEAM: [
    {
      sectionTitle: 'Research',
      items: [
        { title: 'Research Dashboard', href: '/research/dashboard', iconName: 'Microscope' },
      ],
    },
  ],

  INVENTORY_MANAGER: [
    {
      sectionTitle: 'Inventory',
      items: [
        { title: 'Inventory Dashboard', href: '/inventory/dashboard', iconName: 'Package' },
      ],
    },
  ],

  COMPLIANCE_OFFICER: [
    {
      sectionTitle: 'Compliance',
      items: [
        { title: 'Accreditation & Quality', href: '/accreditation/dashboard', iconName: 'CheckSquare' },
      ],
    },
  ],

  HELPDESK_AGENT: [
    {
      sectionTitle: 'Helpdesk',
      items: [
        { title: 'Help Desk Tickets', href: '/helpdesk/dashboard', iconName: 'HelpCircle' },
      ],
    },
  ],

  GRIEVANCE_OFFICER: [
    {
      sectionTitle: 'Grievance',
      items: [
        { title: 'Grievance Redressal', href: '/grievance/dashboard', iconName: 'ShieldAlert' },
      ],
    },
  ],

  SECURITY_ADMIN: [
    {
      sectionTitle: 'Security',
      items: [
        { title: 'Campus Security', href: '/security/dashboard', iconName: 'Lock' },
      ],
    },
  ],

  SYSTEM_ADMIN: [
    {
      sectionTitle: 'System Admin',
      items: [
        { title: 'System Monitoring', href: '/monitoring/dashboard', iconName: 'Activity' },
      ],
    },
  ],

  TENANT_ADMIN: [
    {
      sectionTitle: 'Tenant',
      items: [
        { title: 'Tenant Management', href: '/tenant-management/dashboard', iconName: 'Building2' },
      ],
    },
  ],

  BI_ANALYST: [
    {
      sectionTitle: 'Analytics',
      items: [
        { title: 'BI & Analytics', href: '/bi/dashboard', iconName: 'BarChart3' },
        { title: 'AI Intelligence', href: '/ai-intelligence/dashboard', iconName: 'Sparkles' },
      ],
    },
  ],
};
