import React, { useState } from 'react';
import { Calendar, Clock, Video, CheckCircle, User } from 'lucide-react';

interface OfficeHourSlot {
  id: string;
  facultyName: string;
  designation: string;
  dayTime: string;
  venue: string;
  booked: boolean;
}

export const FacultyOfficeHours: React.FC = () => {
  const [slots, setSlots] = useState<OfficeHourSlot[]>([
    { id: 'oh-1', facultyName: 'Dr. Ananya Sharma', designation: 'HOD & Professor (AI)', dayTime: 'Wednesdays 03:00 - 04:30 PM', venue: 'Faculty Cabin HOD-101 / Google Meet', booked: false },
    { id: 'oh-2', facultyName: 'Prof. Rajesh Verma', designation: 'Associate Professor (Systems)', dayTime: 'Thursdays 02:00 - 03:30 PM', venue: 'Cabin CSE-204', booked: true },
  ]);

  const toggleBook = (id: string) => {
    setSlots(slots.map(s => s.id === id ? { ...s, booked: !s.booked } : s));
  };

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-5">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-3">
          <div className="p-2.5 bg-blue-50 text-blue-600 rounded-lg">
            <Calendar className="w-5 h-5" />
          </div>
          <div>
            <h3 className="font-semibold text-gray-900">Virtual Faculty Office Hours & Queue Manager</h3>
            <p className="text-xs text-gray-500">Book 1-on-1 consultation & project guidance slots with department professors</p>
          </div>
        </div>
      </div>

      <div className="space-y-3">
        {slots.map(s => (
          <div key={s.id} className="p-4 rounded-xl border border-gray-100 bg-gray-50/40 flex items-center justify-between">
            <div className="flex items-center gap-3">
              <div className="p-2.5 bg-white border border-gray-200 rounded-xl text-blue-600">
                <User className="w-5 h-5" />
              </div>
              <div>
                <h4 className="font-bold text-xs text-gray-900">{s.facultyName}</h4>
                <p className="text-xs text-gray-500">{s.designation}</p>
                <div className="flex items-center gap-3 text-[11px] text-gray-400 mt-1">
                  <span className="flex items-center gap-1">
                    <Clock className="w-3 h-3 text-blue-500" /> {s.dayTime}
                  </span>
                  <span className="flex items-center gap-1">
                    <Video className="w-3 h-3 text-blue-500" /> {s.venue}
                  </span>
                </div>
              </div>
            </div>

            <button
              onClick={() => toggleBook(s.id)}
              className={`text-xs font-semibold px-3.5 py-2 rounded-lg flex items-center gap-1 transition-all ${
                s.booked
                  ? 'bg-emerald-600 text-white'
                  : 'bg-blue-600 hover:bg-blue-700 text-white shadow-sm'
              }`}
            >
              {s.booked ? (
                <>
                  <CheckCircle className="w-3.5 h-3.5" /> Slot Confirmed
                </>
              ) : (
                'Book Office Hour'
              )}
            </button>
          </div>
        ))}
      </div>
    </div>
  );
};
