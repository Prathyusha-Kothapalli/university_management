import React from "react";
import { SmartBuildingControlsCard } from "../components/IoT/SmartBuildingControlsCard";

export const CampusIotTelemetryPage: React.FC = () => {
  return (
    <div className="min-h-screen bg-slate-900 text-slate-100 p-6 space-y-6">
      <div className="flex justify-between items-center border-b border-slate-800 pb-6">
        <div>
          <h1 className="text-3xl font-extrabold text-slate-100">Smart Campus IoT Telemetry & Controls</h1>
          <p className="text-slate-400 mt-1">Monitor real-time sensor metrics, HVAC temperature setpoints, and occupancy sensors.</p>
        </div>
      </div>

      <div className="space-y-6">
        <SmartBuildingControlsCard roomName="Auditorium A-101" initialTemp={21.5} initialLighting={85} isOccupied={true} />
        <SmartBuildingControlsCard roomName="Computer Lab CS-204" initialTemp={22.0} initialLighting={70} isOccupied={false} />
      </div>
    </div>
  );
};
