import React from "react";

export interface FuelEntry {
  id: string;
  vehicle_number: string;
  fuel_liters: number;
  cost_amount: number;
  odometer_reading: number;
  logged_at: string;
}

interface FleetFuelTrackerProps {
  entries: FuelEntry[];
}

export const FleetFuelTracker: React.FC<FleetFuelTrackerProps> = ({ entries }) => {
  const totalCost = entries.reduce((acc, e) => acc + e.cost_amount, 0);
  const totalLiters = entries.reduce((acc, e) => acc + e.fuel_liters, 0);

  return (
    <div className="bg-slate-800 border border-slate-700 rounded-xl p-6 shadow-xl space-y-5">
      <div className="flex justify-between items-center">
        <div>
          <h3 className="text-xl font-bold text-slate-100">Fleet Fuel & Mileage Analytics</h3>
          <p className="text-sm text-slate-400">Track fuel consumption, cost per kilometer, and refueling logs.</p>
        </div>
        <div className="text-right">
          <span className="block text-xs text-slate-400 uppercase">Total Monthly Fuel Expense</span>
          <span className="text-2xl font-extrabold font-mono text-emerald-400">${totalCost.toLocaleString()}</span>
        </div>
      </div>

      <div className="grid grid-cols-2 gap-4 bg-slate-900/60 p-4 rounded-lg border border-slate-700/60">
        <div>
          <span className="text-xs text-slate-400">Total Fuel Consumed</span>
          <span className="block text-lg font-bold font-mono text-indigo-400">{totalLiters.toFixed(1)} Liters</span>
        </div>
        <div>
          <span className="text-xs text-slate-400">Avg Cost / Liter</span>
          <span className="block text-lg font-bold font-mono text-sky-400">${totalLiters > 0 ? (totalCost / totalLiters).toFixed(2) : "0.00"}</span>
        </div>
      </div>

      <table className="w-full text-left border-collapse text-sm">
        <thead>
          <tr className="border-b border-slate-700 text-xs font-semibold text-slate-400 uppercase bg-slate-900/70">
            <th className="py-2.5 px-3">Vehicle</th>
            <th className="py-2.5 px-3 text-right">Liters</th>
            <th className="py-2.5 px-3 text-right">Cost ($)</th>
            <th className="py-2.5 px-3 text-right">Odometer (km)</th>
            <th className="py-2.5 px-3 text-right">Timestamp</th>
          </tr>
        </thead>
        <tbody className="divide-y divide-slate-700/60 font-mono text-xs">
          {entries.map((e) => (
            <tr key={e.id} className="hover:bg-slate-700/30">
              <td className="py-2.5 px-3 font-semibold text-slate-100 font-sans">{e.vehicle_number}</td>
              <td className="py-2.5 px-3 text-right text-indigo-300">{e.fuel_liters} L</td>
              <td className="py-2.5 px-3 text-right text-emerald-400 font-bold">${e.cost_amount}</td>
              <td className="py-2.5 px-3 text-right text-slate-300">{e.odometer_reading.toLocaleString()} km</td>
              <td className="py-2.5 px-3 text-right text-slate-400">{new Date(e.logged_at).toLocaleDateString()}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};
