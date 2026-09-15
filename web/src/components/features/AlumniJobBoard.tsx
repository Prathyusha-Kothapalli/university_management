import React, { useState } from 'react';
import { Briefcase, Building2, Send, CheckCircle2 } from 'lucide-react';

interface AlumniJob {
  id: string;
  title: string;
  company: string;
  location: string;
  postedBy: string;
  ctcRange: string;
  applied: boolean;
}

export const AlumniJobBoard: React.FC = () => {
  const [jobs, setJobs] = useState<AlumniJob[]>([
    { id: 'job-1', title: 'Senior AI System Engineer', company: 'Google Brain / DeepMind', location: 'Bengaluru / Hybrid', postedBy: 'Pooja Sundaram (Meta AI Alumna)', ctcRange: '₹38.0 - ₹45.0 LPA', applied: false },
    { id: 'job-2', title: 'Cloud DevOps Engineer II', company: 'Microsoft', location: 'Hyderabad', postedBy: 'Aditya Srivastava (Sr. Architect)', ctcRange: '₹28.0 - ₹34.0 LPA', applied: true },
  ]);

  const toggleApply = (id: string) => {
    setJobs(jobs.map(j => j.id === id ? { ...j, applied: true } : j));
  };

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-5">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-3">
          <div className="p-2.5 bg-teal-50 text-teal-600 rounded-lg">
            <Briefcase className="w-5 h-5" />
          </div>
          <div>
            <h3 className="font-semibold text-gray-900">Exclusive Alumni Job & Employee Referral Board</h3>
            <p className="text-xs text-gray-500">Corporate job openings & internal referral opportunities posted by alumni</p>
          </div>
        </div>
      </div>

      <div className="space-y-3">
        {jobs.map(j => (
          <div key={j.id} className="p-4 rounded-xl border border-gray-100 bg-gray-50/40 flex items-center justify-between">
            <div className="space-y-1">
              <div className="flex items-center gap-2">
                <span className="text-[10px] font-bold text-teal-800 bg-teal-100 px-2 py-0.5 rounded flex items-center gap-0.5">
                  <Building2 className="w-3 h-3 text-teal-600" /> {j.company}
                </span>
                <span className="font-mono text-xs font-bold text-emerald-700">{j.ctcRange}</span>
              </div>
              <h4 className="font-bold text-xs text-gray-900">{j.title}</h4>
              <div className="text-xs text-gray-500">
                Posted by: <strong>{j.postedBy}</strong> • Location: {j.location}
              </div>
            </div>

            <button
              onClick={() => toggleApply(j.id)}
              className={`text-xs font-semibold px-3.5 py-2 rounded-lg flex items-center gap-1 transition-all shrink-0 ${
                j.applied
                  ? 'bg-emerald-50 text-emerald-700 border border-emerald-200'
                  : 'bg-teal-600 hover:bg-teal-700 text-white shadow-sm'
              }`}
            >
              {j.applied ? (
                <>
                  <CheckCircle2 className="w-3.5 h-3.5 text-emerald-600" /> Referral Requested
                </>
              ) : (
                <>
                  <Send className="w-3.5 h-3.5" /> Request Referral
                </>
              )}
            </button>
          </div>
        ))}
      </div>
    </div>
  );
};
