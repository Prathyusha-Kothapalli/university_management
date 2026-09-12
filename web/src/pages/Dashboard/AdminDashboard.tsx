import React, { useState } from 'react';
import { useAuth } from '../../hooks/useAuth';
import { useToast } from '../../hooks/useToast';
import { Card } from '../../components/Card';
import { DataTable, Column } from '../../components/DataTable';
import { Button } from '../../components/Button';
import { Modal } from '../../components/Modal';
import {
  Shield,
  Building2,
  Users,
  Activity,
  Plus,
  Search,
  RefreshCw,
  Lock,
  Database,
  Server,
  ShieldCheck,
} from 'lucide-react';

interface Tenant {
  id: string;
  name: string;
  code: string;
  subdomain: string;
  studentsCount: number;
  facultyCount: number;
  status: 'Active' | 'Maintenance' | 'Suspended';
}

interface SystemUser {
  id: string;
  name: string;
  email: string;
  role: 'admin' | 'faculty' | 'student' | 'hod' | 'parent' | 'librarian';
  department: string;
  status: 'Active' | 'Locked';
  lastLogin: string;
}

interface AuditLog {
  id: string;
  timestamp: string;
  user: string;
  action: string;
  ip: string;
  severity: 'Info' | 'Warning' | 'Critical';
}

export const AdminDashboard: React.FC = () => {
  const { user } = useAuth();
  const { showToast } = useToast();

  const [activeTab, setActiveTab] = useState<'overview' | 'tenants' | 'users' | 'audit' | 'system'>('overview');
  const [isRefreshing, setIsRefreshing] = useState(false);

  // Modals state
  const [isOnboardModalOpen, setIsOnboardModalOpen] = useState(false);
  const [isCreateUserModalOpen, setIsCreateUserModalOpen] = useState(false);

  // Search filters
  const [userSearch, setUserSearch] = useState('');
  const [tenantSearch, setTenantSearch] = useState('');

  // Form states
  const [tenantName, setTenantName] = useState('');
  const [tenantCode, setTenantCode] = useState('');
  const [tenantSubdomain, setTenantSubdomain] = useState('');

  const [userName, setUserName] = useState('');
  const [userEmail, setUserEmail] = useState('');
  const [userRole, setUserRole] = useState<'admin' | 'faculty' | 'student' | 'hod' | 'parent' | 'librarian'>('faculty');

  // Mock data
  const [tenants] = useState<Tenant[]>([
    { id: 't-101', name: 'UniSphere Main Campus', code: 'UNI-MAIN', subdomain: 'main.unisphere.edu', studentsCount: 12400, facultyCount: 850, status: 'Active' },
    { id: 't-102', name: 'UniSphere Tech Park Campus', code: 'UNI-TECH', subdomain: 'tech.unisphere.edu', studentsCount: 4200, facultyCount: 310, status: 'Active' },
    { id: 't-103', name: 'UniSphere Medical & Health Center', code: 'UNI-MED', subdomain: 'med.unisphere.edu', studentsCount: 2800, facultyCount: 420, status: 'Active' },
  ]);

  const [systemUsers] = useState<SystemUser[]>([
    { id: 'u-901', name: 'Dr. Robert Rao', email: 'robert.rao@unisphere.edu', role: 'hod', department: 'Computer Science', status: 'Active', lastLogin: '10 mins ago' },
    { id: 'u-902', name: 'Dr. Sarah Jenkins', email: 'sarah.j@unisphere.edu', role: 'faculty', department: 'Computer Science', status: 'Active', lastLogin: '1 hour ago' },
    { id: 'u-903', name: 'Mrs. Eleanor Vance', email: 'eleanor.v@unisphere.edu', role: 'librarian', department: 'Central Library', status: 'Active', lastLogin: '5 mins ago' },
    { id: 'u-904', name: 'Alex Morgan', email: 'alex.morgan@unisphere.edu', role: 'student', department: 'Computer Science', status: 'Active', lastLogin: '2 mins ago' },
    { id: 'u-905', name: 'Mr. Ramesh Kumar', email: 'ramesh.k@unisphere.edu', role: 'parent', department: 'Guardian Portal', status: 'Active', lastLogin: 'Yesterday' },
  ]);

  const [auditLogs] = useState<AuditLog[]>([
    { id: 'log-801', timestamp: '2026-09-11 09:42:15', user: 'admin@unisphere.edu', action: 'Privilege Escalation granted to u-903 (Librarian)', ip: '192.168.1.104', severity: 'Info' },
    { id: 'log-802', timestamp: '2026-09-11 09:15:30', user: 'system_gateway', action: 'Failed MFA authentication attempt (3 consecutive)', ip: '203.0.113.45', severity: 'Warning' },
    { id: 'log-803', timestamp: '2026-09-11 08:30:00', user: 'database_service', action: 'Automated PostgreSQL Snapshot Backup Completed (2.4 GB)', ip: 'localhost', severity: 'Info' },
    { id: 'log-804', timestamp: '2026-09-10 22:10:45', user: 'sarah.j@unisphere.edu', action: 'Modified Exam Marksheet for CS301', ip: '192.168.1.188', severity: 'Info' },
  ]);

  const filteredUsers = systemUsers.filter(
    (u) =>
      u.name.toLowerCase().includes(userSearch.toLowerCase()) ||
      u.email.toLowerCase().includes(userSearch.toLowerCase()) ||
      u.role.toLowerCase().includes(userSearch.toLowerCase())
  );

  const filteredTenants = tenants.filter(
    (t) =>
      t.name.toLowerCase().includes(tenantSearch.toLowerCase()) ||
      t.subdomain.toLowerCase().includes(tenantSearch.toLowerCase())
  );

  const handleRefresh = () => {
    setIsRefreshing(true);
    showToast('Refreshing system governance & telemetry metrics...', 'info');
    setTimeout(() => {
      setIsRefreshing(false);
      showToast('System health telemetry updated successfully!', 'success');
    }, 700);
  };

  const handleOnboardSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!tenantName || !tenantCode || !tenantSubdomain) {
      showToast('Please fill all tenant onboarding details', 'warning');
      return;
    }
    showToast(`Campus Tenant "${tenantName}" onboarded with subdomain ${tenantSubdomain}`, 'success');
    setIsOnboardModalOpen(false);
    setTenantName('');
    setTenantCode('');
    setTenantSubdomain('');
  };

  const handleCreateUserSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!userName || !userEmail) {
      showToast('Please fill User Name and Email', 'warning');
      return;
    }
    showToast(`User ${userName} created with role ${userRole.toUpperCase()} & credentials dispatched.`, 'success');
    setIsCreateUserModalOpen(false);
    setUserName('');
    setUserEmail('');
  };

  const tenantColumns: Column<Tenant>[] = [
    { header: 'Tenant Code', accessorKey: 'code', cell: (r) => <span style={{ fontFamily: 'monospace', color: '#38bdf8' }}>{r.code}</span> },
    { header: 'Campus Name', accessorKey: 'name', cell: (r) => <strong style={{ color: '#f8fafc' }}>{r.name}</strong> },
    { header: 'Subdomain', accessorKey: 'subdomain', cell: (r) => <span style={{ color: '#94a3b8' }}>{r.subdomain}</span> },
    { header: 'Students', accessorKey: 'studentsCount', cell: (r) => <strong>{r.studentsCount.toLocaleString()}</strong> },
    { header: 'Faculty Staff', accessorKey: 'facultyCount', cell: (r) => <span>{r.facultyCount.toLocaleString()}</span> },
    {
      header: 'Status',
      accessorKey: 'status',
      cell: (r) => (
        <span style={{ padding: '2px 10px', borderRadius: '12px', background: 'rgba(16,185,129,0.2)', color: '#34d399', fontSize: '0.75rem', fontWeight: 700 }}>
          {r.status}
        </span>
      ),
    },
  ];

  const userColumns: Column<SystemUser>[] = [
    { header: 'User ID', accessorKey: 'id', cell: (r) => <span style={{ fontFamily: 'monospace', color: '#94a3b8' }}>{r.id}</span> },
    { header: 'Full Name', accessorKey: 'name', cell: (r) => <strong style={{ color: '#f8fafc' }}>{r.name}</strong> },
    { header: 'Email Address', accessorKey: 'email', cell: (r) => <span style={{ color: '#38bdf8' }}>{r.email}</span> },
    { header: 'System Role', accessorKey: 'role', cell: (r) => <span style={{ textTransform: 'uppercase', padding: '2px 8px', background: 'rgba(56,189,248,0.15)', borderRadius: '6px', fontSize: '0.72rem', fontWeight: 700, color: '#38bdf8' }}>{r.role}</span> },
    { header: 'Department', accessorKey: 'department' },
    { header: 'Last Login', accessorKey: 'lastLogin', cell: (r) => <span style={{ color: '#64748b', fontSize: '0.8rem' }}>{r.lastLogin}</span> },
  ];

  const auditColumns: Column<AuditLog>[] = [
    { header: 'Log ID', accessorKey: 'id', cell: (r) => <span style={{ fontFamily: 'monospace', color: '#94a3b8' }}>{r.id}</span> },
    { header: 'Timestamp', accessorKey: 'timestamp', cell: (r) => <span style={{ fontSize: '0.8rem', color: '#cbd5e1' }}>{r.timestamp}</span> },
    { header: 'Actor / User', accessorKey: 'user', cell: (r) => <strong style={{ color: '#38bdf8' }}>{r.user}</strong> },
    { header: 'Audit Action', accessorKey: 'action' },
    { header: 'IP Address', accessorKey: 'ip', cell: (r) => <span style={{ fontFamily: 'monospace', color: '#64748b' }}>{r.ip}</span> },
    {
      header: 'Severity',
      accessorKey: 'severity',
      cell: (r) => (
        <span
          style={{
            padding: '2px 8px',
            borderRadius: '6px',
            fontSize: '0.72rem',
            fontWeight: 700,
            background: r.severity === 'Critical' ? 'rgba(239,68,68,0.2)' : r.severity === 'Warning' ? 'rgba(245,158,11,0.2)' : 'rgba(56,189,248,0.2)',
            color: r.severity === 'Critical' ? '#f87171' : r.severity === 'Warning' ? '#f59e0b' : '#38bdf8',
          }}
        >
          {r.severity}
        </span>
      ),
    },
  ];

  return (
    <div style={{ padding: '1.75rem', display: 'flex', flexDirection: 'column', gap: '1.5rem', maxWidth: '1600px', margin: '0 auto' }}>
      {/* Executive Header Banner */}
      <div
        style={{
          background: 'linear-gradient(135deg, rgba(30, 41, 59, 0.95), rgba(15, 23, 42, 0.98))',
          backdropFilter: 'blur(16px)',
          border: '1px solid rgba(168, 85, 247, 0.3)',
          borderRadius: '20px',
          padding: '1.75rem',
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          flexWrap: 'wrap',
          gap: '1.25rem',
          boxShadow: '0 8px 32px rgba(0, 0, 0, 0.35)',
        }}
      >
        <div style={{ display: 'flex', alignItems: 'center', gap: '1.25rem' }}>
          <div
            style={{
              width: '62px',
              height: '62px',
              borderRadius: '16px',
              background: 'linear-gradient(135deg, #a855f7, #7e22ce)',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              color: '#ffffff',
              boxShadow: '0 4px 20px rgba(168, 85, 247, 0.4)',
            }}
          >
            <Shield size={32} />
          </div>
          <div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
              <h1 style={{ margin: 0, fontSize: '1.6rem', fontWeight: 800, color: '#f8fafc', letterSpacing: '-0.5px' }}>
                Multi-Tenant Superuser Governance Center
              </h1>
              <span style={{ fontSize: '0.72rem', fontWeight: 700, padding: '3px 10px', borderRadius: '12px', background: 'rgba(168, 85, 247, 0.2)', color: '#c084fc', border: '1px solid rgba(168, 85, 247, 0.3)', display: 'flex', alignItems: 'center', gap: '4px' }}>
                <ShieldCheck size={13} /> Global Superuser Active
              </span>
            </div>
            <p style={{ margin: '4px 0 0 0', fontSize: '0.88rem', color: '#94a3b8' }}>
              Logged in as <strong>{user?.full_name || 'Admin Administrator'}</strong> &bull; Managing 3 Campuses, Security Telemetry & Database Isolation
            </p>
          </div>
        </div>

        {/* Quick Action Buttons */}
        <div style={{ display: 'flex', alignItems: 'center', gap: '10px', flexWrap: 'wrap' }}>
          <Button variant="primary" icon={<Building2 size={16} />} onClick={() => setIsOnboardModalOpen(true)}>
            Onboard New Campus
          </Button>
          <Button variant="secondary" icon={<Plus size={16} />} onClick={() => setIsCreateUserModalOpen(true)}>
            Provision System User
          </Button>
          <button
            onClick={handleRefresh}
            title="Refresh System Governance Telemetry"
            style={{ padding: '9px 12px', borderRadius: '10px', border: '1px solid rgba(255, 255, 255, 0.1)', background: 'rgba(255, 255, 255, 0.05)', color: '#c084fc', cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center' }}
          >
            <RefreshCw size={16} className={isRefreshing ? 'animate-spin' : ''} />
          </button>
        </div>
      </div>

      {/* Tabs */}
      <div style={{ display: 'flex', gap: '8px', borderBottom: '1px solid rgba(255, 255, 255, 0.08)', paddingBottom: '8px', overflowX: 'auto' }}>
        {[
          { id: 'overview', label: 'System Overview', icon: <Activity size={16} /> },
          { id: 'tenants', label: 'Campus Tenants Registry', icon: <Building2 size={16} /> },
          { id: 'users', label: 'Global User Management', icon: <Users size={16} /> },
          { id: 'audit', label: 'Security & Audit Logs', icon: <Lock size={16} /> },
          { id: 'system', label: 'Infrastructure & Database', icon: <Server size={16} /> },
        ].map((tab) => (
          <button
            key={tab.id}
            onClick={() => setActiveTab(tab.id as any)}
            style={{
              display: 'flex',
              alignItems: 'center',
              gap: '8px',
              padding: '10px 18px',
              borderRadius: '10px',
              border: activeTab === tab.id ? '1px solid rgba(168, 85, 247, 0.4)' : '1px solid transparent',
              background: activeTab === tab.id ? 'rgba(168, 85, 247, 0.2)' : 'transparent',
              color: activeTab === tab.id ? '#c084fc' : '#94a3b8',
              fontWeight: 600,
              fontSize: '0.875rem',
              cursor: 'pointer',
              whiteSpace: 'nowrap',
            }}
          >
            {tab.icon}
            <span>{tab.label}</span>
          </button>
        ))}
      </div>

      {/* Tab 1: System Overview */}
      {activeTab === 'overview' && (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(260px, 1fr))', gap: '1.25rem' }}>
            {[
              { title: 'Total Enrolled Students', value: '19,400', sub: 'Across 3 active campuses', icon: <Users size={22} color="#38bdf8" />, bg: 'rgba(56,189,248,0.1)' },
              { title: 'Faculty & Administrative Staff', value: '1,580', sub: 'Active academic accounts', icon: <Shield size={22} color="#c084fc" />, bg: 'rgba(192,132,252,0.1)' },
              { title: 'Active Campus Subdomains', value: '3 Tenants', sub: '100% database isolation', icon: <Building2 size={22} color="#34d399" />, bg: 'rgba(52,211,153,0.1)' },
              { title: 'Global System Health', value: '99.98% Uptime', sub: 'FastAPI + Redis + PostgreSQL', icon: <Activity size={22} color="#f59e0b" />, bg: 'rgba(245,158,11,0.1)' },
            ].map((stat, i) => (
              <div key={i} style={{ backgroundColor: 'rgba(30, 41, 59, 0.7)', backdropFilter: 'blur(16px)', border: '1px solid rgba(255, 255, 255, 0.08)', borderRadius: '16px', padding: '1.25rem', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                <div>
                  <div style={{ fontSize: '0.78rem', color: '#94a3b8', textTransform: 'uppercase', fontWeight: 600 }}>{stat.title}</div>
                  <div style={{ fontSize: '1.75rem', fontWeight: 800, color: '#f8fafc', marginTop: '4px' }}>{stat.value}</div>
                  <div style={{ fontSize: '0.72rem', color: '#64748b', marginTop: '4px' }}>{stat.sub}</div>
                </div>
                <div style={{ width: '48px', height: '48px', borderRadius: '12px', background: stat.bg, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
                  {stat.icon}
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Tab 2: Campus Tenants Registry */}
      {activeTab === 'tenants' && (
        <Card title="Multi-Tenant Campus Registry">
          <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '1.25rem' }}>
            <div style={{ position: 'relative', width: '280px' }}>
              <Search size={16} style={{ position: 'absolute', left: '12px', top: '10px', color: '#94a3b8' }} />
              <input
                type="text"
                placeholder="Search Tenants..."
                value={tenantSearch}
                onChange={(e) => setTenantSearch(e.target.value)}
                style={{ width: '100%', padding: '8px 12px 8px 36px', borderRadius: '8px', background: 'rgba(15,23,42,0.6)', border: '1px solid rgba(255,255,255,0.1)', color: '#f8fafc', fontSize: '0.85rem' }}
              />
            </div>
            <Button variant="primary" icon={<Building2 size={16} />} onClick={() => setIsOnboardModalOpen(true)}>
              Onboard Campus Tenant
            </Button>
          </div>
          <DataTable columns={tenantColumns} data={filteredTenants} />
        </Card>
      )}

      {/* Tab 3: Global User Management */}
      {activeTab === 'users' && (
        <Card title="Global User Account Management">
          <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '1.25rem' }}>
            <div style={{ position: 'relative', width: '280px' }}>
              <Search size={16} style={{ position: 'absolute', left: '12px', top: '10px', color: '#94a3b8' }} />
              <input
                type="text"
                placeholder="Search Users by Name/Email/Role..."
                value={userSearch}
                onChange={(e) => setUserSearch(e.target.value)}
                style={{ width: '100%', padding: '8px 12px 8px 36px', borderRadius: '8px', background: 'rgba(15,23,42,0.6)', border: '1px solid rgba(255,255,255,0.1)', color: '#f8fafc', fontSize: '0.85rem' }}
              />
            </div>
            <Button variant="primary" icon={<Plus size={16} />} onClick={() => setIsCreateUserModalOpen(true)}>
              Provision System User
            </Button>
          </div>
          <DataTable columns={userColumns} data={filteredUsers} />
        </Card>
      )}

      {/* Tab 4: Security & Audit Logs */}
      {activeTab === 'audit' && (
        <Card title="Security & Governance Audit Inspector">
          <DataTable columns={auditColumns} data={auditLogs} />
        </Card>
      )}

      {/* Tab 5: Infrastructure & Database */}
      {activeTab === 'system' && (
        <Card title="Database & Infrastructure Metrics">
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: '1.25rem' }}>
            <div style={{ padding: '1.25rem', background: 'rgba(15,23,42,0.6)', borderRadius: '12px', border: '1px solid rgba(255,255,255,0.08)' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px', color: '#38bdf8', fontWeight: 700, marginBottom: '8px' }}>
                <Database size={18} /> PostgreSQL Cluster Status
              </div>
              <div style={{ fontSize: '0.85rem', color: '#cbd5e1' }}>Pool Connections: 24 / 100 active</div>
              <div style={{ fontSize: '0.85rem', color: '#cbd5e1', marginTop: '4px' }}>Latency: 1.2ms</div>
            </div>

            <div style={{ padding: '1.25rem', background: 'rgba(15,23,42,0.6)', borderRadius: '12px', border: '1px solid rgba(255,255,255,0.08)' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px', color: '#c084fc', fontWeight: 700, marginBottom: '8px' }}>
                <Server size={18} /> Redis Caching Engine
              </div>
              <div style={{ fontSize: '0.85rem', color: '#cbd5e1' }}>Cache Hit Rate: 98.4%</div>
              <div style={{ fontSize: '0.85rem', color: '#cbd5e1', marginTop: '4px' }}>Memory Consumption: 142 MB</div>
            </div>
          </div>
        </Card>
      )}

      {/* Onboard Tenant Modal */}
      <Modal isOpen={isOnboardModalOpen} onClose={() => setIsOnboardModalOpen(false)} title="Onboard New Campus Tenant">
        <form onSubmit={handleOnboardSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
          <div>
            <label style={{ display: 'block', fontSize: '0.8rem', color: '#cbd5e1', marginBottom: '4px' }}>Campus / University Name</label>
            <input type="text" placeholder="e.g. UniSphere North Campus" value={tenantName} onChange={(e) => setTenantName(e.target.value)} required style={{ width: '100%', padding: '8px 12px', borderRadius: '8px', background: 'rgba(15,23,42,0.8)', border: '1px solid rgba(255,255,255,0.15)', color: '#f8fafc' }} />
          </div>
          <div>
            <label style={{ display: 'block', fontSize: '0.8rem', color: '#cbd5e1', marginBottom: '4px' }}>Tenant Code</label>
            <input type="text" placeholder="e.g. UNI-NORTH" value={tenantCode} onChange={(e) => setTenantCode(e.target.value)} required style={{ width: '100%', padding: '8px 12px', borderRadius: '8px', background: 'rgba(15,23,42,0.8)', border: '1px solid rgba(255,255,255,0.15)', color: '#f8fafc' }} />
          </div>
          <div>
            <label style={{ display: 'block', fontSize: '0.8rem', color: '#cbd5e1', marginBottom: '4px' }}>Subdomain</label>
            <input type="text" placeholder="e.g. north.unisphere.edu" value={tenantSubdomain} onChange={(e) => setTenantSubdomain(e.target.value)} required style={{ width: '100%', padding: '8px 12px', borderRadius: '8px', background: 'rgba(15,23,42,0.8)', border: '1px solid rgba(255,255,255,0.15)', color: '#f8fafc' }} />
          </div>
          <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '8px', marginTop: '8px' }}>
            <Button variant="outline" onClick={() => setIsOnboardModalOpen(false)}>Cancel</Button>
            <Button variant="primary" icon={<Building2 size={16} />}>Confirm Onboarding</Button>
          </div>
        </form>
      </Modal>

      {/* Provision User Modal */}
      <Modal isOpen={isCreateUserModalOpen} onClose={() => setIsCreateUserModalOpen(false)} title="Provision System User Account">
        <form onSubmit={handleCreateUserSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
          <div>
            <label style={{ display: 'block', fontSize: '0.8rem', color: '#cbd5e1', marginBottom: '4px' }}>Full Name</label>
            <input type="text" placeholder="e.g. Prof. Alan Turing" value={userName} onChange={(e) => setUserName(e.target.value)} required style={{ width: '100%', padding: '8px 12px', borderRadius: '8px', background: 'rgba(15,23,42,0.8)', border: '1px solid rgba(255,255,255,0.15)', color: '#f8fafc' }} />
          </div>
          <div>
            <label style={{ display: 'block', fontSize: '0.8rem', color: '#cbd5e1', marginBottom: '4px' }}>Email Address</label>
            <input type="email" placeholder="e.g. alan.turing@unisphere.edu" value={userEmail} onChange={(e) => setUserEmail(e.target.value)} required style={{ width: '100%', padding: '8px 12px', borderRadius: '8px', background: 'rgba(15,23,42,0.8)', border: '1px solid rgba(255,255,255,0.15)', color: '#f8fafc' }} />
          </div>
          <div>
            <label style={{ display: 'block', fontSize: '0.8rem', color: '#cbd5e1', marginBottom: '4px' }}>Assigned Role</label>
            <select value={userRole} onChange={(e) => setUserRole(e.target.value as any)} style={{ width: '100%', padding: '8px 12px', borderRadius: '8px', background: 'rgba(15,23,42,0.8)', border: '1px solid rgba(255,255,255,0.15)', color: '#f8fafc' }}>
              <option value="admin">Admin / Superuser</option>
              <option value="faculty">Faculty Member</option>
              <option value="student">Student</option>
              <option value="hod">Head of Department (HOD)</option>
              <option value="librarian">Librarian</option>
              <option value="parent">Parent / Guardian</option>
            </select>
          </div>
          <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '8px', marginTop: '8px' }}>
            <Button variant="outline" onClick={() => setIsCreateUserModalOpen(false)}>Cancel</Button>
            <Button variant="primary" icon={<Plus size={16} />}>Provision User</Button>
          </div>
        </form>
      </Modal>
    </div>
  );
};

export default AdminDashboard;
