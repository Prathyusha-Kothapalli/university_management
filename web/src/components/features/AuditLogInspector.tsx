import React, { useState } from 'react';
import { Search, Terminal } from 'lucide-react';

interface AuditLog {
  id: string;
  timestamp: string;
  actor: string;
  role: string;
  action: string;
  targetEntity: string;
  ipAddress: string;
  severity: 'Info' | 'Warning' | 'Critical';
}

export const AuditLogInspector: React.FC = () => {
  const [search, setSearch] = useState('');
  const [severityFilter, setSeverityFilter] = useState<string>('All');

  const logs: AuditLog[] = [
    { id: 'LOG-9921', timestamp: '2026-09-10 16:30:12', actor: 'Dr. Ananya Sharma', role: 'HOD', action: 'Approved Syllabus Revision for CS-401', targetEntity: 'Course / CS-401', ipAddress: '10.0.4.18', severity: 'Info' },
    { id: 'LOG-9922', timestamp: '2026-09-10 15:45:00', actor: 'Admin Portal', role: 'SYSTEM', action: 'Role Privilege Elevation for HOD User', targetEntity: 'User / HOD-402', ipAddress: '10.0.0.1', severity: 'Warning' },
    { id: 'LOG-9923', timestamp: '2026-09-10 14:12:33', actor: 'Prof. Rajesh Verma', role: 'Faculty', action: 'Published Midterm Exam Grades', targetEntity: 'Exams / CS-302', ipAddress: '10.0.4.22', severity: 'Info' },
    { id: 'LOG-9924', timestamp: '2026-09-10 12:05:40', actor: 'Prathyusha (Student)', role: 'Student', action: 'Submitted Re-evaluation Appeal', targetEntity: 'GradeDispute / DISP-101', ipAddress: '103.220.14.92', severity: 'Info' },
    { id: 'LOG-9925', timestamp: '2026-09-10 09:10:15', actor: 'Unrecognized Device', role: 'UNKNOWN', action: 'Failed Admin Password Attempt (3x)', targetEntity: 'Auth / SecurityGateway', ipAddress: '185.220.101.5', severity: 'Critical' },
  ];

  const filtered = logs.filter(l => {
    const matchesSearch = l.actor.toLowerCase().includes(search.toLowerCase()) || l.action.toLowerCase().includes(search.toLowerCase());
    const matchesSeverity = severityFilter === 'All' || l.severity === severityFilter;
    return matchesSearch && matchesSeverity;
  });

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-5">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-3">
          <div className="p-2.5 bg-slate-100 text-slate-700 rounded-lg">
            <Terminal className="w-5 h-5" />
          </div>
          <div>
            <h3 className="font-semibold text-gray-900">System Audit Log & Activity Inspector</h3>
            <p className="text-xs text-gray-500">Immutable audit trail of administrative role changes, grade modifications & logins</p>
          </div>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-3 mb-4">
        <div className="md:col-span-2 relative">
          <Search className="w-4 h-4 text-gray-400 absolute left-3 top-2.5" />
          <input
            type="text"
            placeholder="Search audit trail by actor, action or IP address..."
            value={search}
            onChange={e => setSearch(e.target.value)}
            className="w-full text-xs border border-gray-200 rounded-lg pl-9 pr-3 py-2 focus:ring-2 focus:ring-slate-500 focus:outline-none"
          />
        </div>

        <select
          value={severityFilter}
          onChange={e => setSeverityFilter(e.target.value)}
          className="text-xs border border-gray-200 rounded-lg px-3 py-2 bg-white focus:ring-2 focus:ring-slate-500"
        >
          <option value="All">All Severity Levels</option>
          <option value="Info">Info</option>
          <option value="Warning">Warning</option>
          <option value="Critical">Critical Security Alerts</option>
        </select>
      </div>

      <div className="divide-y divide-gray-100 border border-gray-100 rounded-xl overflow-hidden font-mono text-xs">
        {filtered.map(l => (
          <div key={l.id} className="p-3.5 bg-white flex items-center justify-between hover:bg-gray-50/80 transition-colors">
            <div className="flex items-center gap-3">
              <span className={`text-[10px] font-bold px-2 py-0.5 rounded-full ${
                l.severity === 'Critical' ? 'bg-rose-100 text-rose-800' :
                l.severity === 'Warning' ? 'bg-amber-100 text-amber-800' :
                'bg-slate-100 text-slate-700'
              }`}>
                {l.severity}
              </span>
              <div>
                <div className="flex items-center gap-2">
                  <span className="font-semibold text-gray-900 font-sans">{l.actor}</span>
                  <span className="text-[10px] bg-gray-100 text-gray-600 px-1.5 py-0.5 rounded font-sans">{l.role}</span>
                  <span className="text-gray-400 text-[11px]">{l.timestamp}</span>
                </div>
                <p className="text-gray-600 font-sans mt-0.5">{l.action}</p>
              </div>
            </div>

            <div className="text-right shrink-0">
              <div className="text-[11px] text-gray-400">{l.targetEntity}</div>
              <div className="text-[10px] text-gray-400">IP: {l.ipAddress}</div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
