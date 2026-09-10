import React, { useState } from 'react';
import { Video, Calendar, UserCheck, Star, CheckCircle } from 'lucide-react';

interface MockSession {
  id: string;
  interviewer: string;
  role: string;
  company: string;
  slot: string;
  type: 'Technical (DSA/System Design)' | 'Behavioral & HR' | 'System Architecture';
  rating?: number;
  status: 'Upcoming' | 'Completed';
}

export const MockInterviewScheduler: React.FC = () => {
  const [sessions, setSessions] = useState<MockSession[]>([
    {
      id: 'INT-101',
      interviewer: 'Vikramaditya Sharma (Alumnus @ Google)',
      role: 'Staff Software Engineer',
      company: 'Google',
      slot: 'Tomorrow, 06:00 PM',
      type: 'Technical (DSA/System Design)',
      status: 'Upcoming'
    },
    {
      id: 'INT-098',
      interviewer: 'Dr. Ananya Rao',
      role: 'Associate Professor',
      company: 'UniSphere AI Faculty',
      slot: 'Sep 05, 2026',
      type: 'Behavioral & HR',
      rating: 4.8,
      status: 'Completed'
    }
  ]);

  const [showModal, setShowModal] = useState(false);
  const [interviewer, setInterviewer] = useState('Senior Alumni Mentor');
  const [type, setType] = useState<MockSession['type']>('Technical (DSA/System Design)');
  const [slot, setSlot] = useState('Saturday, 04:00 PM');
  const [booked, setBooked] = useState(false);

  const handleBook = (e: React.FormEvent) => {
    e.preventDefault();
    const newSession: MockSession = {
      id: `INT-${Math.floor(100 + Math.random() * 900)}`,
      interviewer,
      role: 'Corporate Technical Lead',
      company: 'Tech Industry Partner',
      slot,
      type,
      status: 'Upcoming'
    };
    setSessions([newSession, ...sessions]);
    setBooked(true);
    setTimeout(() => {
      setBooked(false);
      setShowModal(false);
    }, 2000);
  };

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-5">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-3">
          <div className="p-2.5 bg-violet-50 text-violet-600 rounded-lg">
            <Video className="w-5 h-5" />
          </div>
          <div>
            <h3 className="font-semibold text-gray-900">Mock Interview & Peer Feedback Scheduler</h3>
            <p className="text-xs text-gray-500">Book 1-on-1 technical DSA & System Design mock interviews with faculty & alumni</p>
          </div>
        </div>
        <button
          onClick={() => setShowModal(true)}
          className="bg-violet-600 hover:bg-violet-700 text-white text-xs font-semibold px-3.5 py-2 rounded-lg flex items-center gap-1.5 transition-colors"
        >
          <Calendar className="w-4 h-4" />
          Schedule Mock Slot
        </button>
      </div>

      <div className="space-y-3">
        {sessions.map(s => (
          <div key={s.id} className="p-4 rounded-xl border border-gray-100 bg-gray-50/40 flex items-center justify-between">
            <div className="flex items-center gap-3">
              <div className="p-2.5 bg-white border border-gray-200 rounded-xl">
                <UserCheck className="w-5 h-5 text-violet-600" />
              </div>
              <div>
                <div className="flex items-center gap-2">
                  <span className="font-semibold text-xs text-gray-900">{s.interviewer}</span>
                  <span className="text-[10px] bg-violet-50 text-violet-700 px-2 py-0.5 rounded-full font-medium">
                    {s.type}
                  </span>
                </div>
                <p className="text-xs text-gray-500">{s.role} • {s.company}</p>
                <span className="text-[11px] text-gray-400">Slot: {s.slot}</span>
              </div>
            </div>

            <div className="text-right">
              {s.status === 'Upcoming' ? (
                <span className="bg-emerald-50 text-emerald-700 text-xs font-semibold px-3 py-1 rounded-full border border-emerald-100 flex items-center gap-1">
                  <Video className="w-3.5 h-3.5" /> Join Meeting
                </span>
              ) : (
                <div className="flex items-center gap-1 text-xs text-amber-500 font-bold">
                  <Star className="w-4 h-4 fill-amber-400" />
                  {s.rating} / 5.0
                </div>
              )}
            </div>
          </div>
        ))}
      </div>

      {showModal && (
        <div className="fixed inset-0 bg-black/40 backdrop-blur-sm z-50 flex items-center justify-center p-4">
          <div className="bg-white rounded-2xl p-6 w-full max-w-md space-y-4 shadow-xl border border-gray-100">
            <h3 className="font-semibold text-gray-900 text-sm">Schedule Mock Technical Interview</h3>
            
            {booked ? (
              <div className="p-4 bg-emerald-50 text-emerald-800 rounded-xl text-center space-y-1">
                <CheckCircle className="w-8 h-8 text-emerald-600 mx-auto mb-1" />
                <h4 className="font-bold text-xs">Interview Slot Confirmed!</h4>
                <p className="text-[11px]">Calendar invitation & Google Meet link dispatched to your email.</p>
              </div>
            ) : (
              <form onSubmit={handleBook} className="space-y-3">
                <div>
                  <label className="block text-xs font-medium text-gray-700 mb-1">Interview Domain</label>
                  <select
                    value={type}
                    onChange={e => setType(e.target.value as any)}
                    className="w-full text-xs border border-gray-200 rounded-lg p-2.5 bg-white focus:ring-2 focus:ring-violet-500"
                  >
                    <option value="Technical (DSA/System Design)">Technical (DSA & System Design)</option>
                    <option value="Behavioral & HR">Behavioral & HR Leadership</option>
                    <option value="System Architecture">AI & ML System Architecture</option>
                  </select>
                </div>

                <div>
                  <label className="block text-xs font-medium text-gray-700 mb-1">Preferred Interviewer Pool</label>
                  <select
                    value={interviewer}
                    onChange={e => setInterviewer(e.target.value)}
                    className="w-full text-xs border border-gray-200 rounded-lg p-2.5 bg-white focus:ring-2 focus:ring-violet-500"
                  >
                    <option value="Senior Alumni Mentor (FAANG / Unicorn)">FAANG Alumni Mentors</option>
                    <option value="UniSphere Senior Faculty Panel">UniSphere Senior Faculty Panel</option>
                    <option value="Peer Student Lead (CSE Final Year)">Peer Student Lead (CSE 4th Year)</option>
                  </select>
                </div>

                <div>
                  <label className="block text-xs font-medium text-gray-700 mb-1">Time Slot</label>
                  <input
                    type="text"
                    value={slot}
                    onChange={e => setSlot(e.target.value)}
                    className="w-full text-xs border border-gray-200 rounded-lg p-2.5 focus:ring-2 focus:ring-violet-500"
                    required
                  />
                </div>

                <div className="flex justify-end gap-2 pt-2">
                  <button
                    type="button"
                    onClick={() => setShowModal(false)}
                    className="px-4 py-2 text-xs text-gray-600 hover:bg-gray-100 rounded-lg"
                  >
                    Cancel
                  </button>
                  <button
                    type="submit"
                    className="px-4 py-2 text-xs font-medium bg-violet-600 hover:bg-violet-700 text-white rounded-lg"
                  >
                    Confirm Slot
                  </button>
                </div>
              </form>
            )}
          </div>
        </div>
      )}
    </div>
  );
};
