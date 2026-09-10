import React, { useState } from 'react';
import { Search, Download, GraduationCap } from 'lucide-react';

interface Thesis {
  id: string;
  title: string;
  student: string;
  advisor: string;
  year: number;
  degree: 'B.Tech Capstone' | 'M.Tech Thesis' | 'Ph.D. Dissertation';
  downloads: number;
}

export const ResearchPaperRepository: React.FC = () => {
  const [search, setSearch] = useState('');
  const [theses] = useState<Thesis[]>([
    { id: 'ths-01', title: 'Deep Reinforcement Learning for Autonomous Drone Swarm Path Planning', student: 'Alex Morgan', advisor: 'Dr. Ananya Sharma', year: 2026, degree: 'B.Tech Capstone', downloads: 142 },
    { id: 'ths-02', title: 'Privacy-Preserving Federated Learning over Decoupled Edge Mesh Networks', student: 'Sameer Sen', advisor: 'Dr. Rajesh Verma', year: 2025, degree: 'M.Tech Thesis', downloads: 289 },
  ]);

  const filtered = theses.filter(t => t.title.toLowerCase().includes(search.toLowerCase()) || t.student.toLowerCase().includes(search.toLowerCase()));

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-5">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-3">
          <div className="p-2.5 bg-indigo-50 text-indigo-600 rounded-lg">
            <GraduationCap className="w-5 h-5" />
          </div>
          <div>
            <h3 className="font-semibold text-gray-900">Institutional Open-Access Thesis & Capstone Repository</h3>
            <p className="text-xs text-gray-500">Archived B.Tech/M.Tech capstone thesis projects & doctoral dissertations</p>
          </div>
        </div>
      </div>

      <div className="relative mb-4">
        <Search className="w-4 h-4 text-gray-400 absolute left-3 top-2.5" />
        <input
          type="text"
          placeholder="Search institutional repository by title, student or advisor..."
          value={search}
          onChange={e => setSearch(e.target.value)}
          className="w-full text-xs border border-gray-200 rounded-lg pl-9 pr-3 py-2 focus:ring-2 focus:ring-indigo-500 focus:outline-none"
        />
      </div>

      <div className="space-y-3">
        {filtered.map(t => (
          <div key={t.id} className="p-4 rounded-xl border border-gray-100 bg-gray-50/40 flex items-center justify-between">
            <div className="space-y-1">
              <div className="flex items-center gap-2">
                <span className="text-[10px] font-bold text-indigo-700 bg-indigo-100 px-2.5 py-0.5 rounded-full">
                  {t.degree}
                </span>
                <span className="text-[11px] text-gray-400 font-medium">Class of {t.year}</span>
              </div>
              <h4 className="font-bold text-xs text-gray-900">{t.title}</h4>
              <div className="text-xs text-gray-500">
                Author: <strong>{t.student}</strong> • Advisor: {t.advisor}
              </div>
            </div>

            <button className="text-xs font-semibold px-3 py-1.5 rounded-lg bg-indigo-600 hover:bg-indigo-700 text-white flex items-center gap-1 transition-colors shadow-sm shrink-0">
              <Download className="w-3.5 h-3.5" /> PDF ({t.downloads})
            </button>
          </div>
        ))}
      </div>
    </div>
  );
};
