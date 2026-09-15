import React, { useState } from 'react';
import { Users, Calendar, CheckCircle2, UserPlus } from 'lucide-react';

interface Club {
  id: string;
  name: string;
  category: 'Tech' | 'Robotics' | 'Cultural' | 'Sports';
  membersCount: number;
  upcomingEvent: string;
  eventDate: string;
  joined: boolean;
}

export const StudentClubManager: React.FC = () => {
  const [clubs, setClubs] = useState<Club[]>([
    { id: 'clb-1', name: 'UniSphere AI & Robotics Club', category: 'Tech', membersCount: 340, upcomingEvent: 'Annual Autonomous Drone Race', eventDate: 'March 25, 2026', joined: true },
    { id: 'clb-2', name: 'CyberSec & Ethical Hacking Guild', category: 'Tech', membersCount: 210, upcomingEvent: 'Inter-College CTF 2026', eventDate: 'April 02, 2026', joined: false },
    { id: 'clb-3', name: 'Campus Music & Performing Arts', category: 'Cultural', membersCount: 180, upcomingEvent: 'Spring Fest Battle of Bands', eventDate: 'April 10, 2026', joined: false },
  ]);

  const toggleJoin = (id: string) => {
    setClubs(clubs.map(c => c.id === id ? { ...c, joined: !c.joined, membersCount: c.joined ? c.membersCount - 1 : c.membersCount + 1 } : c));
  };

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-5">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-3">
          <div className="p-2.5 bg-violet-50 text-violet-600 rounded-lg">
            <Users className="w-5 h-5" />
          </div>
          <div>
            <h3 className="font-semibold text-gray-900">Campus Student Club & Society Manager</h3>
            <p className="text-xs text-gray-500">Discover student tech societies, cultural clubs & register for campus events</p>
          </div>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-3">
        {clubs.map(club => (
          <div key={club.id} className="p-4 rounded-xl border border-gray-100 bg-gray-50/50 flex flex-col justify-between space-y-3">
            <div>
              <div className="flex items-center justify-between mb-2">
                <span className="text-[10px] font-bold text-violet-700 bg-violet-100 px-2.5 py-0.5 rounded-full">
                  {club.category}
                </span>
                <span className="text-xs text-gray-400 font-semibold">{club.membersCount} Members</span>
              </div>
              <h4 className="font-bold text-xs text-gray-900 mb-1">{club.name}</h4>
              <div className="p-2 bg-white rounded-lg border border-gray-100 text-xs text-gray-600 space-y-0.5">
                <div className="font-semibold text-violet-800 text-[11px]">Upcoming Event:</div>
                <div className="font-medium text-gray-900">{club.upcomingEvent}</div>
                <div className="text-[10px] text-gray-400 flex items-center gap-1">
                  <Calendar className="w-3 h-3 text-violet-500" /> {club.eventDate}
                </div>
              </div>
            </div>

            <button
              onClick={() => toggleJoin(club.id)}
              className={`w-full py-2 text-xs font-semibold rounded-lg flex items-center justify-center gap-1.5 transition-all ${
                club.joined
                  ? 'bg-emerald-50 text-emerald-700 border border-emerald-200'
                  : 'bg-violet-600 hover:bg-violet-700 text-white shadow-sm'
              }`}
            >
              {club.joined ? (
                <>
                  <CheckCircle2 className="w-3.5 h-3.5 text-emerald-600" /> Member (Joined)
                </>
              ) : (
                <>
                  <UserPlus className="w-3.5 h-3.5" /> Join Club
                </>
              )}
            </button>
          </div>
        ))}
      </div>
    </div>
  );
};
