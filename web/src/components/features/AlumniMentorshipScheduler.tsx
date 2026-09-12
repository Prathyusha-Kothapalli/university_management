import React, { useState } from 'react';
import { Calendar, Video, User, Clock } from 'lucide-react';

interface MentorshipSession {
  id: string;
  mentorName: string;
  companyRole: string;
  topic: string;
  slot: string;
  status: 'Confirmed' | 'Pending Confirmation';
}

export const AlumniMentorshipScheduler: React.FC = () => {
  const [sessions] = useState<MentorshipSession[]>([
    {
      id: 'mnt-101',
      mentorName: 'Aditya Srivastava',
      companyRole: 'Senior Cloud Architect @ Microsoft',
      topic: 'Transitioning from B.Tech to FAANG Cloud Roles & Resume Review',
      slot: 'Saturday, Sept 19 • 06:00 PM',
      status: 'Confirmed'
    }
  ]);

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-5">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-3">
          <div className="p-2.5 bg-blue-50 text-blue-600 rounded-lg">
            <Calendar className="w-5 h-5" />
          </div>
          <div>
            <h3 className="font-semibold text-gray-900">Alumni 1-on-1 Mentorship Session Scheduler</h3>
            <p className="text-xs text-gray-500">Schedule video consultation calls & career advice sessions with alumni leaders</p>
          </div>
        </div>
      </div>

      <div className="space-y-3">
        {sessions.map(s => (
          <div key={s.id} className="p-4 rounded-xl border border-gray-100 bg-gray-50/40 flex items-center justify-between">
            <div className="flex items-center gap-3">
              <div className="p-2.5 bg-white border border-gray-200 rounded-xl text-blue-600">
                <User className="w-5 h-5" />
              </div>
              <div>
                <h4 className="font-bold text-xs text-gray-900">{s.mentorName}</h4>
                <p className="text-xs text-blue-600 font-medium">{s.companyRole}</p>
                <div className="text-xs text-gray-700 mt-1">Agenda: {s.topic}</div>
                <div className="text-[11px] text-gray-400 flex items-center gap-1 mt-0.5">
                  <Clock className="w-3 h-3 text-blue-500" /> {s.slot}
                </div>
              </div>
            </div>

            <button className="text-xs font-semibold px-3 py-1.5 rounded-lg bg-emerald-50 text-emerald-700 border border-emerald-200 flex items-center gap-1 shrink-0">
              <Video className="w-3.5 h-3.5 text-emerald-600" /> Join Call
            </button>
          </div>
        ))}
      </div>
    </div>
  );
};
