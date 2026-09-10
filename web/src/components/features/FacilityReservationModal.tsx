import React, { useState } from 'react';
import { Building2, Calendar, Clock, CheckCircle2 } from 'lucide-react';

interface Facility {
  id: string;
  name: string;
  category: 'Auditorium' | 'Sports Court' | 'AI Supercomputer Lab' | 'Seminar Hall';
  capacity: string;
  status: 'Available' | 'Booked';
  imageIcon: string;
}

export const FacilityReservationModal: React.FC = () => {
  const [selectedFacility, setSelectedFacility] = useState<string>('fac-1');
  const [date, setDate] = useState<string>('2026-09-15');
  const [timeSlot, setTimeSlot] = useState<string>('02:00 PM - 04:00 PM');
  const [purpose, setPurpose] = useState<string>('');
  const [booked, setBooked] = useState(false);

  const facilities: Facility[] = [
    { id: 'fac-1', name: 'APJ Abdul Kalam Main Auditorium', category: 'Auditorium', capacity: '800 Seats', status: 'Available', imageIcon: '🎭' },
    { id: 'fac-2', name: 'AI & GPU High-Performance Compute Lab', category: 'AI Supercomputer Lab', capacity: '40 Workstations', status: 'Available', imageIcon: '🖥️' },
    { id: 'fac-3', name: 'Indoor Badminton & Tennis Arena', category: 'Sports Court', capacity: '4 Courts', status: 'Available', imageIcon: '🎾' },
    { id: 'fac-4', name: 'Ramanujan Seminar Complex - Hall B', category: 'Seminar Hall', capacity: '150 Seats', status: 'Available', imageIcon: '🏛️' },
  ];

  const handleBooking = (e: React.FormEvent) => {
    e.preventDefault();
    if (!purpose) return;
    setBooked(true);
    setTimeout(() => {
      setBooked(false);
      setPurpose('');
    }, 3000);
  };

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-5">
      <div className="flex items-center gap-3 mb-4">
        <div className="p-2.5 bg-cyan-50 text-cyan-600 rounded-lg">
          <Building2 className="w-5 h-5" />
        </div>
        <div>
          <h3 className="font-semibold text-gray-900">Campus Facility & Sports Court Reservation</h3>
          <p className="text-xs text-gray-500">Reserve auditoriums, tennis courts, seminar halls, and high-performance AI labs</p>
        </div>
      </div>

      {booked ? (
        <div className="p-6 bg-emerald-50 border border-emerald-200 rounded-xl text-center space-y-2">
          <CheckCircle2 className="w-10 h-10 text-emerald-600 mx-auto" />
          <h4 className="font-bold text-gray-900 text-sm">Facility Reservation Requested!</h4>
          <p className="text-xs text-gray-600">Your reservation request for {facilities.find(f => f.id === selectedFacility)?.name} on {date} ({timeSlot}) has been sent for estate admin approval.</p>
        </div>
      ) : (
        <form onSubmit={handleBooking} className="space-y-4">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
            {facilities.map(fac => (
              <div
                key={fac.id}
                onClick={() => setSelectedFacility(fac.id)}
                className={`p-3.5 rounded-xl border transition-all cursor-pointer flex items-center gap-3 ${
                  selectedFacility === fac.id
                    ? 'bg-cyan-50/50 border-cyan-300 ring-2 ring-cyan-500/20'
                    : 'bg-gray-50/50 border-gray-100 hover:border-gray-200'
                }`}
              >
                <div className="text-2xl">{fac.imageIcon}</div>
                <div className="flex-1">
                  <div className="flex items-center justify-between">
                    <span className="text-[10px] font-semibold text-cyan-700 bg-cyan-100/60 px-2 py-0.5 rounded-full">
                      {fac.category}
                    </span>
                    <span className="text-[10px] text-gray-400 font-medium">{fac.capacity}</span>
                  </div>
                  <h4 className="font-semibold text-xs text-gray-900 mt-1">{fac.name}</h4>
                </div>
              </div>
            ))}
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-3 bg-gray-50 p-4 rounded-xl border border-gray-100">
            <div>
              <label className="block text-xs font-medium text-gray-700 mb-1">Reservation Date</label>
              <div className="relative">
                <Calendar className="w-4 h-4 text-gray-400 absolute left-3 top-2.5" />
                <input
                  type="date"
                  value={date}
                  onChange={e => setDate(e.target.value)}
                  className="w-full text-xs border border-gray-200 rounded-lg pl-9 pr-3 py-2 bg-white focus:ring-2 focus:ring-cyan-500 focus:outline-none"
                  required
                />
              </div>
            </div>

            <div>
              <label className="block text-xs font-medium text-gray-700 mb-1">Time Window</label>
              <div className="relative">
                <Clock className="w-4 h-4 text-gray-400 absolute left-3 top-2.5" />
                <select
                  value={timeSlot}
                  onChange={e => setTimeSlot(e.target.value)}
                  className="w-full text-xs border border-gray-200 rounded-lg pl-9 pr-3 py-2 bg-white focus:ring-2 focus:ring-cyan-500 focus:outline-none"
                >
                  <option value="09:00 AM - 11:00 AM">09:00 AM - 11:00 AM</option>
                  <option value="11:30 AM - 01:30 PM">11:30 AM - 01:30 PM</option>
                  <option value="02:00 PM - 04:00 PM">02:00 PM - 04:00 PM</option>
                  <option value="04:30 PM - 06:30 PM">04:30 PM - 06:30 PM</option>
                </select>
              </div>
            </div>

            <div>
              <label className="block text-xs font-medium text-gray-700 mb-1">Event / Purpose</label>
              <input
                type="text"
                placeholder="e.g., Hackathon Keynote, Tennis Practice"
                value={purpose}
                onChange={e => setPurpose(e.target.value)}
                className="w-full text-xs border border-gray-200 rounded-lg px-3 py-2 bg-white focus:ring-2 focus:ring-cyan-500 focus:outline-none"
                required
              />
            </div>
          </div>

          <div className="flex justify-end">
            <button
              type="submit"
              className="bg-cyan-600 hover:bg-cyan-700 text-white text-xs font-semibold px-5 py-2 rounded-lg transition-all shadow-sm"
            >
              Confirm Facility Booking Request
            </button>
          </div>
        </form>
      )}
    </div>
  );
};
