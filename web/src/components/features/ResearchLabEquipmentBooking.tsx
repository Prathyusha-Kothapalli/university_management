import React, { useState } from 'react';
import { Cpu, Clock, CheckCircle2 } from 'lucide-react';

interface Equipment {
  id: string;
  name: string;
  category: string;
  labLocation: string;
  availableSlot: string;
  status: 'Available' | 'Reserved';
}

export const ResearchLabEquipmentBooking: React.FC = () => {
  const [equipmentList] = useState<Equipment[]>([
    { id: 'eq-1', name: 'NVIDIA H100 GPU AI Cluster Node 4', category: 'High-Performance Computing', labLocation: 'AI Supercomputing Hub - Room 102', availableSlot: 'Today, 08:00 PM - 11:00 PM', status: 'Available' },
    { id: 'eq-2', name: 'FEI Quanta 200 Scanning Electron Microscope (SEM)', category: 'Advanced Microscopy', labLocation: 'Nanotechnology Research Center', availableSlot: 'Tomorrow, 10:00 AM - 01:00 PM', status: 'Available' },
  ]);

  const [bookedId, setBookedId] = useState<string | null>(null);

  const handleBook = (id: string) => {
    setBookedId(id);
    setTimeout(() => setBookedId(null), 2500);
  };

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-5">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-3">
          <div className="p-2.5 bg-slate-100 text-slate-800 rounded-lg">
            <Cpu className="w-5 h-5" />
          </div>
          <div>
            <h3 className="font-semibold text-gray-900">Advanced Research Lab Equipment Reservation</h3>
            <p className="text-xs text-gray-500">Reserve GPU clusters, electron microscopes & advanced instrumentation</p>
          </div>
        </div>
      </div>

      <div className="space-y-3">
        {equipmentList.map(eq => (
          <div key={eq.id} className="p-4 rounded-xl border border-gray-100 bg-gray-50/40 flex items-center justify-between">
            <div className="space-y-1">
              <div className="flex items-center gap-2">
                <span className="text-[10px] font-bold text-slate-800 bg-slate-200 px-2 py-0.5 rounded">
                  {eq.category}
                </span>
                <h4 className="font-bold text-xs text-gray-900">{eq.name}</h4>
              </div>
              <p className="text-xs text-gray-500">{eq.labLocation}</p>
              <div className="text-[11px] text-emerald-600 font-medium flex items-center gap-1">
                <Clock className="w-3.5 h-3.5" /> Next Available Slot: {eq.availableSlot}
              </div>
            </div>

            <button
              onClick={() => handleBook(eq.id)}
              className={`text-xs font-semibold px-3.5 py-2 rounded-lg flex items-center gap-1 transition-all shrink-0 ${
                bookedId === eq.id
                  ? 'bg-emerald-600 text-white'
                  : 'bg-slate-900 hover:bg-slate-800 text-white shadow-sm'
              }`}
            >
              {bookedId === eq.id ? (
                <>
                  <CheckCircle2 className="w-3.5 h-3.5" /> Slot Booked
                </>
              ) : (
                'Book Instrument Slot'
              )}
            </button>
          </div>
        ))}
      </div>
    </div>
  );
};
