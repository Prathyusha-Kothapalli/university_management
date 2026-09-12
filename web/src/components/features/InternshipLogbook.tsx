import React, { useState } from 'react';
import { Briefcase, CheckCircle2, Clock, PlusCircle } from 'lucide-react';

interface WeeklyLog {
  id: string;
  weekNumber: number;
  startDate: string;
  endDate: string;
  tasksCompleted: string;
  learnings: string;
  status: 'Approved by Supervisor' | 'Pending Verification' | 'Needs Revision';
  hoursLogged: number;
}

export const InternshipLogbook: React.FC = () => {
  const [companyName] = useState('Amazon Web Services (AWS) - Summer Intern');
  const [logs, setLogs] = useState<WeeklyLog[]>([
    {
      id: 'LOG-08',
      weekNumber: 8,
      startDate: '2026-08-25',
      endDate: '2026-08-31',
      tasksCompleted: 'Configured Kubernetes auto-scaling policy for microservices backend.',
      learnings: 'Hands-on Helm charts, Prometheus metrics, and Terraform deployment.',
      status: 'Approved by Supervisor',
      hoursLogged: 40
    },
    {
      id: 'LOG-09',
      weekNumber: 9,
      startDate: '2026-09-01',
      endDate: '2026-09-07',
      tasksCompleted: 'Created automated CI/CD pipeline using GitHub Actions & AWS ECR.',
      learnings: 'Docker layer caching optimization & IAM role security scoping.',
      status: 'Pending Verification',
      hoursLogged: 42
    }
  ]);

  const [showForm, setShowForm] = useState(false);
  const [tasks, setTasks] = useState('');
  const [learnings, setLearnings] = useState('');
  const [hours, setHours] = useState(40);

  const handleAddLog = (e: React.FormEvent) => {
    e.preventDefault();
    if (!tasks || !learnings) return;

    const newLog: WeeklyLog = {
      id: `LOG-0${logs.length + 8}`,
      weekNumber: logs.length + 8,
      startDate: '2026-09-08',
      endDate: '2026-09-14',
      tasksCompleted: tasks,
      learnings,
      status: 'Pending Verification',
      hoursLogged: hours
    };

    setLogs([newLog, ...logs]);
    setShowForm(false);
    setTasks('');
    setLearnings('');
  };

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-5">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-3">
          <div className="p-2.5 bg-blue-50 text-blue-600 rounded-lg">
            <Briefcase className="w-5 h-5" />
          </div>
          <div>
            <h3 className="font-semibold text-gray-900">Corporate Internship Logbook & Weekly Tracker</h3>
            <p className="text-xs text-gray-500">Submit industrial training logs, supervisor sign-offs & credit approvals</p>
          </div>
        </div>
        <button
          onClick={() => setShowForm(true)}
          className="bg-blue-600 hover:bg-blue-700 text-white text-xs font-semibold px-3 py-2 rounded-lg flex items-center gap-1.5 transition-colors"
        >
          <PlusCircle className="w-4 h-4" />
          Submit Weekly Log
        </button>
      </div>

      <div className="p-3 bg-blue-50/50 rounded-xl border border-blue-100 mb-4 flex items-center justify-between">
        <div>
          <span className="text-[10px] uppercase tracking-wider font-bold text-blue-600">Active Internship</span>
          <h4 className="font-semibold text-xs text-gray-900">{companyName}</h4>
        </div>
        <div className="text-right">
          <span className="text-xs font-bold text-blue-700 font-mono">
            {logs.reduce((a, b) => a + b.hoursLogged, 0)} Total Hours Logged
          </span>
        </div>
      </div>

      <div className="space-y-3">
        {logs.map(log => (
          <div key={log.id} className="p-4 rounded-xl border border-gray-100 bg-gray-50/40 space-y-2">
            <div className="flex items-center justify-between">
              <div className="flex items-center gap-2">
                <span className="font-bold text-xs text-blue-600 bg-blue-50 px-2.5 py-0.5 rounded-full">
                  Week {log.weekNumber}
                </span>
                <span className="text-xs font-medium text-gray-700">
                  {log.startDate} to {log.endDate}
                </span>
              </div>
              <span className={`text-[11px] font-semibold px-2.5 py-0.5 rounded-full flex items-center gap-1 ${
                log.status === 'Approved by Supervisor' ? 'bg-emerald-50 text-emerald-700' : 'bg-amber-50 text-amber-700'
              }`}>
                {log.status === 'Approved by Supervisor' ? (
                  <CheckCircle2 className="w-3.5 h-3.5 text-emerald-600" />
                ) : (
                  <Clock className="w-3.5 h-3.5 text-amber-600" />
                )}
                {log.status}
              </span>
            </div>

            <div className="text-xs text-gray-700">
              <strong className="text-gray-900">Key Deliverables: </strong> {log.tasksCompleted}
            </div>
            <div className="text-xs text-gray-500 italic">
              <strong className="text-gray-700 not-italic">Technical Learnings: </strong> {log.learnings}
            </div>
          </div>
        ))}
      </div>

      {showForm && (
        <div className="fixed inset-0 bg-black/40 backdrop-blur-sm z-50 flex items-center justify-center p-4">
          <div className="bg-white rounded-2xl p-6 w-full max-w-md space-y-4 shadow-xl border border-gray-100">
            <h3 className="font-semibold text-gray-900 text-sm">Submit Weekly Internship Report</h3>
            <form onSubmit={handleAddLog} className="space-y-3">
              <div>
                <label className="block text-xs font-medium text-gray-700 mb-1">Key Deliverables / Tasks Completed</label>
                <textarea
                  rows={2}
                  value={tasks}
                  onChange={e => setTasks(e.target.value)}
                  className="w-full text-xs border border-gray-200 rounded-lg p-2.5 focus:ring-2 focus:ring-blue-500 focus:outline-none"
                  placeholder="Describe technical work completed this week..."
                  required
                />
              </div>

              <div>
                <label className="block text-xs font-medium text-gray-700 mb-1">Technical Skills Learned</label>
                <textarea
                  rows={2}
                  value={learnings}
                  onChange={e => setLearnings(e.target.value)}
                  className="w-full text-xs border border-gray-200 rounded-lg p-2.5 focus:ring-2 focus:ring-blue-500 focus:outline-none"
                  placeholder="Key concepts, frameworks or tools used..."
                  required
                />
              </div>

              <div>
                <label className="block text-xs font-medium text-gray-700 mb-1">Total Hours Worked</label>
                <input
                  type="number"
                  value={hours}
                  onChange={e => setHours(Number(e.target.value))}
                  className="w-full text-xs border border-gray-200 rounded-lg p-2.5 font-semibold focus:ring-2 focus:ring-blue-500"
                  min="10"
                  max="60"
                  required
                />
              </div>

              <div className="flex justify-end gap-2 pt-2">
                <button
                  type="button"
                  onClick={() => setShowForm(false)}
                  className="px-4 py-2 text-xs text-gray-600 hover:bg-gray-100 rounded-lg"
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  className="px-4 py-2 text-xs font-medium bg-blue-600 hover:bg-blue-700 text-white rounded-lg"
                >
                  Submit Log
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
};
