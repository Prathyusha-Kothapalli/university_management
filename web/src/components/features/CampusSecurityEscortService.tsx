import React, { useState } from 'react';
import { Shield, PhoneCall, MapPin, CheckCircle2, AlertOctagon } from 'lucide-react';

export const CampusSecurityEscortService: React.FC = () => {
  const [pickupLoc, setPickupLoc] = useState('Central Library Gate');
  const [requested, setRequested] = useState(false);

  const handleRequestEscort = (e: React.FormEvent) => {
    e.preventDefault();
    setRequested(true);
    setTimeout(() => setRequested(false), 3000);
  };

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-5">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-3">
          <div className="p-2.5 bg-rose-50 text-rose-600 rounded-lg">
            <Shield className="w-5 h-5" />
          </div>
          <div>
            <h3 className="font-semibold text-gray-900">Campus Security Night Escort & Panic Alert</h3>
            <p className="text-xs text-gray-500">24/7 security escort dispatch & rapid emergency response button</p>
          </div>
        </div>

        <button className="bg-rose-600 hover:bg-rose-700 text-white text-xs font-bold px-3 py-1.5 rounded-lg flex items-center gap-1 transition-colors shadow-sm">
          <AlertOctagon className="w-4 h-4" /> SOS Panic Alert
        </button>
      </div>

      {requested ? (
        <div className="p-4 bg-emerald-50 border border-emerald-200 rounded-xl text-center space-y-1">
          <CheckCircle2 className="w-8 h-8 text-emerald-600 mx-auto" />
          <h4 className="font-bold text-xs text-gray-900">Security Escort Patrol Dispatched!</h4>
          <p className="text-[11px] text-gray-600">Officer Ramesh Chandra is en route to {pickupLoc} (ETA: 4 mins).</p>
        </div>
      ) : (
        <form onSubmit={handleRequestEscort} className="flex gap-2">
          <div className="relative flex-1">
            <MapPin className="w-4 h-4 text-gray-400 absolute left-3 top-2.5" />
            <input
              type="text"
              placeholder="Enter pickup location (e.g. Library, Computer Center)..."
              value={pickupLoc}
              onChange={e => setPickupLoc(e.target.value)}
              className="w-full text-xs border border-gray-200 rounded-lg pl-9 pr-3 py-2 focus:ring-2 focus:ring-rose-500 focus:outline-none"
              required
            />
          </div>
          <button
            type="submit"
            className="bg-slate-900 hover:bg-slate-800 text-white text-xs font-semibold px-4 py-2 rounded-lg flex items-center gap-1.5 transition-colors shadow-sm shrink-0"
          >
            <PhoneCall className="w-3.5 h-3.5" /> Request Security Escort
          </button>
        </form>
      )}
    </div>
  );
};
