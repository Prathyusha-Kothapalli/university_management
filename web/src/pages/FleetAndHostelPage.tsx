import React, { useState } from "react";
import { FleetFuelTracker, FuelEntry } from "../components/Transport/FleetFuelTracker";

export const FleetAndHostelPage: React.FC = () => {
  const [fuelEntries] = useState<FuelEntry[]>([
    { id: "fl1", vehicle_number: "BUS-101 (Volvo 44-Seater)", fuel_liters: 85.0, cost_amount: 144.5, odometer_reading: 42150, logged_at: "2026-03-10" },
    { id: "fl2", vehicle_number: "VAN-204 (Campus Shuttle)", fuel_liters: 42.5, cost_amount: 72.25, odometer_reading: 18920, logged_at: "2026-03-11" },
  ]);

  return (
    <div className="min-h-screen bg-slate-900 text-slate-100 p-6 space-y-6">
      <div className="flex justify-between items-center border-b border-slate-800 pb-6">
        <div>
          <h1 className="text-3xl font-extrabold text-slate-100">Smart Campus Transport & Hostel Fleet</h1>
          <p className="text-slate-400 mt-1">Manage transport routes, fuel consumption, vehicle maintenance logs, and hostel tickets.</p>
        </div>
      </div>

      <FleetFuelTracker entries={fuelEntries} />
    </div>
  );
};
