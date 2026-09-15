import React, { useState } from 'react';
import { Home, Sparkles, CheckCircle2, User } from 'lucide-react';

interface MatchCandidate {
  id: string;
  name: string;
  branch: string;
  matchPct: number;
  habits: string[];
  bedPreference: 'Window Bed' | 'Door Side';
}

export const HostelRoommateMatcher: React.FC = () => {
  const [candidates] = useState<MatchCandidate[]>([
    {
      id: 'rm-1',
      name: 'Rohan Deshmukh',
      branch: 'CSE (Year 3)',
      matchPct: 94,
      habits: ['Night Owl', 'Quiet Study', 'Non-Smoker'],
      bedPreference: 'Window Bed'
    },
    {
      id: 'rm-2',
      name: 'Karthik Raja',
      branch: 'ECE (Year 3)',
      matchPct: 87,
      habits: ['Early Riser', 'Light Sleeper', 'Clean & Organized'],
      bedPreference: 'Door Side'
    }
  ]);

  const [requestedId, setRequestedId] = useState<string | null>(null);

  const handleRequest = (id: string) => {
    setRequestedId(id);
    setTimeout(() => setRequestedId(null), 2500);
  };

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-5">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-3">
          <div className="p-2.5 bg-emerald-50 text-emerald-600 rounded-lg">
            <Home className="w-5 h-5" />
          </div>
          <div>
            <h3 className="font-semibold text-gray-900">AI Hostel Roommate Compatibility Matcher</h3>
            <p className="text-xs text-gray-500">Compatibility survey matching study habits, sleep schedules & lifestyle preferences</p>
          </div>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
        {candidates.map(c => (
          <div key={c.id} className="p-4 rounded-xl border border-gray-100 bg-gray-50/40 flex items-center justify-between">
            <div className="flex items-center gap-3">
              <div className="p-2.5 bg-white border border-gray-200 rounded-xl text-gray-600">
                <User className="w-5 h-5 text-emerald-600" />
              </div>
              <div>
                <div className="flex items-center gap-2">
                  <h4 className="font-bold text-xs text-gray-900">{c.name}</h4>
                  <span className="text-[10px] bg-emerald-100 text-emerald-800 font-bold px-2 py-0.5 rounded-full flex items-center gap-0.5">
                    <Sparkles className="w-3 h-3 text-emerald-600" /> {c.matchPct}% Match
                  </span>
                </div>
                <p className="text-xs text-gray-500">{c.branch}</p>
                <div className="flex gap-1 mt-1">
                  {c.habits.map((h, i) => (
                    <span key={i} className="text-[10px] bg-white border border-gray-200 text-gray-600 px-1.5 py-0.5 rounded">
                      {h}
                    </span>
                  ))}
                </div>
              </div>
            </div>

            <button
              onClick={() => handleRequest(c.id)}
              className={`text-xs font-semibold px-3 py-1.5 rounded-lg flex items-center gap-1 transition-all shrink-0 ${
                requestedId === c.id
                  ? 'bg-emerald-600 text-white'
                  : 'bg-emerald-50 hover:bg-emerald-100 text-emerald-700 border border-emerald-200'
              }`}
            >
              {requestedId === c.id ? (
                <>
                  <CheckCircle2 className="w-3.5 h-3.5" /> Request Sent
                </>
              ) : (
                'Send Roommate Request'
              )}
            </button>
          </div>
        ))}
      </div>
    </div>
  );
};
