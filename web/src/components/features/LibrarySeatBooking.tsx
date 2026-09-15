import React, { useState } from 'react';
import { Calendar, Clock, CheckCircle2 } from 'lucide-react';

interface SeatZone {
  id: string;
  zoneName: string;
  floor: string;
  availableSeats: number;
  totalSeats: number;
  type: 'Silent Individual Cubicle' | 'Group Discussion Room' | 'Digital Resource Terminal';
}

export const LibrarySeatBooking: React.FC = () => {
  const [zones] = useState<SeatZone[]>([
    { id: 'zn-1', zoneName: 'Ramanujan Silent Study Zone A', floor: '1st Floor', availableSeats: 14, totalSeats: 40, type: 'Silent Individual Cubicle' },
    { id: 'zn-2', zoneName: 'Collaborative Group Discussion Pod 3', floor: '2nd Floor', availableSeats: 2, totalSeats: 6, type: 'Group Discussion Room' },
    { id: 'zn-3', zoneName: 'IEEE & ACM Digital Journal Terminal', floor: 'Ground Floor', availableSeats: 8, totalSeats: 15, type: 'Digital Resource Terminal' },
  ]);

  const [reservedZoneId, setReservedZoneId] = useState<string | null>(null);

  const handleReserve = (id: string) => {
    setReservedZoneId(id);
    setTimeout(() => setReservedZoneId(null), 2500);
  };

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-5">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-3">
          <div className="p-2.5 bg-emerald-50 text-emerald-600 rounded-lg">
            <Calendar className="w-5 h-5" />
          </div>
          <div>
            <h3 className="font-semibold text-gray-900">Silent Study Zone & Discussion Pod Reservation</h3>
            <p className="text-xs text-gray-500">Real-time seat availability & discussion room booking in central library</p>
          </div>
        </div>
      </div>

      <div className="space-y-3">
        {zones.map(z => (
          <div key={z.id} className="p-4 rounded-xl border border-gray-100 bg-gray-50/40 flex items-center justify-between">
            <div className="space-y-1">
              <div className="flex items-center gap-2">
                <span className="text-[10px] font-bold text-emerald-700 bg-emerald-100 px-2.5 py-0.5 rounded-full">
                  {z.type}
                </span>
                <span className="text-xs text-gray-400 font-medium">• {z.floor}</span>
              </div>
              <h4 className="font-bold text-xs text-gray-900">{z.zoneName}</h4>
              <div className="text-xs text-gray-500 flex items-center gap-1">
                <Clock className="w-3.5 h-3.5 text-emerald-600" />
                <span className="font-semibold text-emerald-700">{z.availableSeats} of {z.totalSeats} seats currently available</span>
              </div>
            </div>

            <button
              onClick={() => handleReserve(z.id)}
              className={`text-xs font-semibold px-3.5 py-2 rounded-lg flex items-center gap-1 transition-all shrink-0 ${
                reservedZoneId === z.id
                  ? 'bg-emerald-600 text-white'
                  : 'bg-emerald-50 hover:bg-emerald-100 text-emerald-700 border border-emerald-200'
              }`}
            >
              {reservedZoneId === z.id ? (
                <>
                  <CheckCircle2 className="w-3.5 h-3.5" /> Seat Reserved
                </>
              ) : (
                'Reserve Seat'
              )}
            </button>
          </div>
        ))}
      </div>
    </div>
  );
};
