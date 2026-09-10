import React, { useState } from 'react';
import { Target, CheckCircle2, XCircle, ArrowRight } from 'lucide-react';

interface Drive {
  id: string;
  company: string;
  role: string;
  ctc: string;
  minCgpa: number;
  maxBacklogs: number;
  eligibleBranches: string[];
  status: 'Eligible & Shortlisted' | 'Ineligible (CGPA Below Cutoff)' | 'Registration Open';
}

export const PlacementEligibilityMatcher: React.FC = () => {
  const [userCgpa] = useState(8.65);
  const [activeBacklogs] = useState(0);

  const drives: Drive[] = [
    {
      id: 'DRV-101',
      company: 'Microsoft',
      role: 'Software Development Engineer (SDE-1)',
      ctc: '₹44.0 LPA',
      minCgpa: 8.0,
      maxBacklogs: 0,
      eligibleBranches: ['CSE', 'ECE', 'IT'],
      status: 'Eligible & Shortlisted'
    },
    {
      id: 'DRV-102',
      company: 'Amazon AWS',
      role: 'Cloud Systems Engineer',
      ctc: '₹32.0 LPA',
      minCgpa: 7.5,
      maxBacklogs: 0,
      eligibleBranches: ['CSE', 'ECE', 'EEE', 'IT'],
      status: 'Eligible & Shortlisted'
    },
    {
      id: 'DRV-103',
      company: 'Goldman Sachs',
      role: 'Quantitative Financial Analyst',
      ctc: '₹38.0 LPA',
      minCgpa: 9.0,
      maxBacklogs: 0,
      eligibleBranches: ['CSE', 'Math & Computing'],
      status: 'Ineligible (CGPA Below Cutoff)'
    }
  ];

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-5">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-3">
          <div className="p-2.5 bg-emerald-50 text-emerald-600 rounded-lg">
            <Target className="w-5 h-5" />
          </div>
          <div>
            <h3 className="font-semibold text-gray-900">Placement Drive Eligibility Matcher</h3>
            <p className="text-xs text-gray-500">Automated qualification & cutoff match scanner across 150+ campus recruitment drives</p>
          </div>
        </div>

        <div className="flex items-center gap-2 bg-emerald-50/60 border border-emerald-100 px-3 py-1.5 rounded-lg text-xs">
          <span className="text-gray-600">Your Academic Metrics:</span>
          <span className="font-bold text-emerald-700">CGPA {userCgpa}</span>
          <span className="text-gray-300">|</span>
          <span className="font-semibold text-emerald-700">{activeBacklogs} Backlogs</span>
        </div>
      </div>

      <div className="space-y-3">
        {drives.map(drive => {
          const isEligible = userCgpa >= drive.minCgpa && activeBacklogs <= drive.maxBacklogs;

          return (
            <div
              key={drive.id}
              className={`p-4 rounded-xl border transition-all flex items-center justify-between ${
                isEligible ? 'bg-emerald-50/30 border-emerald-100' : 'bg-gray-50/50 border-gray-100'
              }`}
            >
              <div className="flex items-center gap-3.5">
                {isEligible ? (
                  <CheckCircle2 className="w-6 h-6 text-emerald-600 shrink-0" />
                ) : (
                  <XCircle className="w-6 h-6 text-rose-500 shrink-0" />
                )}

                <div>
                  <div className="flex items-center gap-2">
                    <h4 className="font-bold text-sm text-gray-900">{drive.company}</h4>
                    <span className="font-mono text-xs font-bold text-emerald-700 bg-emerald-100/60 px-2 py-0.5 rounded">
                      {drive.ctc}
                    </span>
                  </div>
                  <p className="text-xs text-gray-600 font-medium">{drive.role}</p>
                  <div className="flex items-center gap-3 text-[11px] text-gray-400 mt-1">
                    <span>Min CGPA: {drive.minCgpa}</span>
                    <span>Max Backlogs: {drive.maxBacklogs}</span>
                    <span>Branches: {drive.eligibleBranches.join(', ')}</span>
                  </div>
                </div>
              </div>

              <div>
                {isEligible ? (
                  <button className="bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-semibold px-4 py-2 rounded-lg flex items-center gap-1 transition-colors shadow-sm">
                    Apply Now <ArrowRight className="w-3.5 h-3.5" />
                  </button>
                ) : (
                  <span className="text-xs text-rose-600 bg-rose-50 font-semibold px-3 py-1 rounded-full border border-rose-100">
                    Not Eligible
                  </span>
                )}
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
};
