import React, { useState } from 'react';
import { Award, CheckCircle2 } from 'lucide-react';

interface Grant {
  id: string;
  title: string;
  agency: string;
  sanctionedAmount: number;
  utilizedAmount: number;
  piName: string;
  status: 'Approved & Active' | 'Milestone 2 Review' | 'Completed';
}

export const ResearchGrantTracker: React.FC = () => {
  const [grants] = useState<Grant[]>([
    {
      id: 'GNT-401',
      title: 'DST-SERB: Generative AI Models for Healthcare Diagnostics',
      agency: 'DST - Science & Engineering Research Board',
      sanctionedAmount: 4500000,
      utilizedAmount: 2800000,
      piName: 'Dr. Ananya Sharma (HOD CSE)',
      status: 'Approved & Active'
    },
    {
      id: 'GNT-402',
      title: 'DRDO: Autonomous Drone Swarm Navigation in GPS-Denied Environments',
      agency: 'DRDO Research Grant Scheme',
      sanctionedAmount: 6200000,
      utilizedAmount: 4100000,
      piName: 'Dr. Rajesh Verma',
      status: 'Milestone 2 Review'
    }
  ]);

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-5">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-3">
          <div className="p-2.5 bg-emerald-50 text-emerald-600 rounded-lg">
            <Award className="w-5 h-5" />
          </div>
          <div>
            <h3 className="font-semibold text-gray-900">Faculty Research Grant & Funding Tracker</h3>
            <p className="text-xs text-gray-500">Track DST, SERB, DRDO research grant proposals, budget utilization & sponsor milestones</p>
          </div>
        </div>
      </div>

      <div className="space-y-3">
        {grants.map(grant => {
          const utilPct = Math.round((grant.utilizedAmount / grant.sanctionedAmount) * 100);

          return (
            <div key={grant.id} className="p-4 rounded-xl border border-gray-100 bg-gray-50/40 space-y-3">
              <div className="flex items-center justify-between">
                <div>
                  <span className="text-[10px] font-bold text-emerald-700 bg-emerald-100 px-2.5 py-0.5 rounded-full mr-2">
                    {grant.agency}
                  </span>
                  <span className="font-bold text-xs text-gray-900">{grant.title}</span>
                </div>
                <span className="text-xs font-semibold text-emerald-700 bg-emerald-50 px-2.5 py-1 rounded-full border border-emerald-100 flex items-center gap-1">
                  <CheckCircle2 className="w-3.5 h-3.5 text-emerald-600" /> {grant.status}
                </span>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-3 gap-2 text-xs text-gray-600 bg-white p-3 rounded-lg border border-gray-100">
                <div>
                  <span className="text-gray-400">Principal Investigator:</span>
                  <div className="font-semibold text-gray-800">{grant.piName}</div>
                </div>
                <div>
                  <span className="text-gray-400">Sanctioned Budget:</span>
                  <div className="font-bold text-gray-900 font-mono">₹{grant.sanctionedAmount.toLocaleString('en-IN')}</div>
                </div>
                <div>
                  <span className="text-gray-400">Funds Utilized:</span>
                  <div className="font-bold text-emerald-700 font-mono">₹{grant.utilizedAmount.toLocaleString('en-IN')} ({utilPct}%)</div>
                </div>
              </div>

              <div className="space-y-1">
                <div className="flex justify-between text-[11px] text-gray-500">
                  <span>Budget Utilization Progress</span>
                  <span>{utilPct}% Utilized</span>
                </div>
                <div className="h-2 w-full bg-gray-200 rounded-full overflow-hidden">
                  <div style={{ width: `${utilPct}%` }} className="bg-emerald-500 h-full rounded-full" />
                </div>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
};
