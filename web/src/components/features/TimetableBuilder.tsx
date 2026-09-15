import React, { useState } from 'react';
import { Calendar, Clock, Plus, Trash2, CheckCircle2, UserCheck, AlertCircle } from 'lucide-react';

interface Slot {
  id: string;
  day: string;
  time: string;
  subject: string;
  faculty: string;
  room: string;
}

export const TimetableBuilder: React.FC = () => {
  const [dayFilter, setDayFilter] = useState<string>('Monday');
  const [slots, setSlots] = useState<Slot[]>([
    { id: '1', day: 'Monday', time: '09:00 - 10:00 AM', subject: 'Data Structures', faculty: 'Dr. Sharma', room: 'LH-101' },
    { id: '2', day: 'Monday', time: '10:15 - 11:15 AM', subject: 'Operating Systems', faculty: 'Prof. Verma', room: 'LH-104' },
    { id: '3', day: 'Monday', time: '11:30 - 12:30 PM', subject: 'AI & ML Lab', faculty: 'Dr. Ananya', room: 'Lab-3' },
    { id: '4', day: 'Tuesday', time: '09:00 - 10:00 AM', subject: 'Database Systems', faculty: 'Dr. Rajesh', room: 'LH-102' },
    { id: '5', day: 'Tuesday', time: '10:15 - 11:15 AM', subject: 'Computer Networks', faculty: 'Prof. Mehta', room: 'LH-103' },
  ]);

  const [newSubject, setNewSubject] = useState('');
  const [newFaculty, setNewFaculty] = useState('');
  const [newTime, setNewTime] = useState('02:00 - 03:00 PM');
  const [newRoom, setNewRoom] = useState('LH-201');
  const [showSuccess, setShowSuccess] = useState(false);

  const handleAddSlot = (e: React.FormEvent) => {
    e.preventDefault();
    if (!newSubject || !newFaculty) return;
    const newEntry: Slot = {
      id: Date.now().toString(),
      day: dayFilter,
      time: newTime,
      subject: newSubject,
      faculty: newFaculty,
      room: newRoom
    };
    setSlots([...slots, newEntry]);
    setNewSubject('');
    setNewFaculty('');
    setShowSuccess(true);
    setTimeout(() => setShowSuccess(false), 2500);
  };

  const handleDelete = (id: string) => {
    setSlots(slots.filter(s => s.id !== id));
  };

  const filteredSlots = slots.filter(s => s.day === dayFilter);

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-5">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-3">
          <div className="p-2.5 bg-blue-50 text-blue-600 rounded-lg">
            <Calendar className="w-5 h-5" />
          </div>
          <div>
            <h3 className="font-semibold text-gray-900">Interactive Timetable & Schedule Builder</h3>
            <p className="text-xs text-gray-500">Manage course lecture slots, room allocations, and faculty timetables</p>
          </div>
        </div>
        <div className="flex bg-gray-100 p-1 rounded-lg">
          {['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'].map(d => (
            <button
              key={d}
              onClick={() => setDayFilter(d)}
              className={`px-3 py-1 text-xs font-medium rounded-md transition-all ${
                dayFilter === d ? 'bg-white text-blue-600 shadow-sm' : 'text-gray-600 hover:text-gray-900'
              }`}
            >
              {d.slice(0, 3)}
            </button>
          ))}
        </div>
      </div>

      {showSuccess && (
        <div className="mb-4 p-3 bg-emerald-50 text-emerald-700 text-xs rounded-lg flex items-center gap-2 border border-emerald-100">
          <CheckCircle2 className="w-4 h-4 text-emerald-600" />
          Lecture slot added successfully and synced with department schedule!
        </div>
      )}

      {/* Slots List */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-3 mb-5">
        {filteredSlots.map(slot => (
          <div key={slot.id} className="p-3.5 rounded-xl border border-gray-100 bg-gray-50/50 hover:bg-gray-50 transition-colors relative group">
            <button
              onClick={() => handleDelete(slot.id)}
              className="absolute top-3 right-3 text-gray-400 hover:text-rose-600 opacity-0 group-hover:opacity-100 transition-opacity"
            >
              <Trash2 className="w-4 h-4" />
            </button>
            <div className="flex items-center gap-1.5 text-xs text-blue-600 font-medium mb-1">
              <Clock className="w-3.5 h-3.5" />
              {slot.time}
            </div>
            <h4 className="font-semibold text-sm text-gray-900 mb-1">{slot.subject}</h4>
            <div className="flex items-center justify-between text-xs text-gray-500">
              <span className="flex items-center gap-1">
                <UserCheck className="w-3.5 h-3.5 text-gray-400" />
                {slot.faculty}
              </span>
              <span className="bg-white border border-gray-200 px-2 py-0.5 rounded font-mono text-[11px] text-gray-700">
                {slot.room}
              </span>
            </div>
          </div>
        ))}
        {filteredSlots.length === 0 && (
          <div className="col-span-3 p-6 text-center text-gray-400 text-xs bg-gray-50 rounded-xl border border-dashed border-gray-200">
            <AlertCircle className="w-6 h-6 mx-auto mb-1 text-gray-300" />
            No lectures scheduled for {dayFilter}. Add a slot below!
          </div>
        )}
      </div>

      {/* Add Slot Form */}
      <form onSubmit={handleAddSlot} className="bg-gray-50 p-4 rounded-xl border border-gray-100 space-y-3">
        <h4 className="text-xs font-semibold text-gray-700">Add New Slot for {dayFilter}</h4>
        <div className="grid grid-cols-1 md:grid-cols-4 gap-3">
          <input
            type="text"
            placeholder="Course / Subject Name"
            value={newSubject}
            onChange={e => setNewSubject(e.target.value)}
            className="text-xs border border-gray-200 rounded-lg px-3 py-2 bg-white focus:ring-2 focus:ring-blue-500 focus:outline-none"
            required
          />
          <input
            type="text"
            placeholder="Faculty Name"
            value={newFaculty}
            onChange={e => setNewFaculty(e.target.value)}
            className="text-xs border border-gray-200 rounded-lg px-3 py-2 bg-white focus:ring-2 focus:ring-blue-500 focus:outline-none"
            required
          />
          <input
            type="text"
            placeholder="Room (e.g. LH-201)"
            value={newRoom}
            onChange={e => setNewRoom(e.target.value)}
            className="text-xs border border-gray-200 rounded-lg px-3 py-2 bg-white focus:ring-2 focus:ring-blue-500 focus:outline-none"
          />
          <input
            type="text"
            placeholder="Time (e.g. 02:00 PM)"
            value={newTime}
            onChange={e => setNewTime(e.target.value)}
            className="text-xs border border-gray-200 rounded-lg px-3 py-2 bg-white focus:ring-2 focus:ring-blue-500 focus:outline-none"
          />
          <button
            type="submit"
            className="bg-blue-600 hover:bg-blue-700 text-white text-xs font-medium px-4 py-2 rounded-lg transition-colors flex items-center justify-center gap-1.5"
          >
            <Plus className="w-4 h-4" />
            Add Slot
          </button>
        </div>
      </form>
    </div>
  );
};
