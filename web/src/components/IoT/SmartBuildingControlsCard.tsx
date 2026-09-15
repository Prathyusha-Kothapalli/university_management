import React, { useState } from "react";

interface SmartBuildingControlsCardProps {
  roomName: string;
  initialTemp: number;
  initialLighting: number;
  isOccupied: boolean;
}

export const SmartBuildingControlsCard: React.FC<SmartBuildingControlsCardProps> = ({
  roomName,
  initialTemp,
  initialLighting,
  isOccupied,
}) => {
  const [temp, setTemp] = useState(initialTemp);
  const [lighting, setLighting] = useState(initialLighting);
  const [occupied, setOccupied] = useState(isOccupied);

  return (
    <div className="bg-slate-800 border border-slate-700 rounded-xl p-6 shadow-xl space-y-5">
      <div className="flex justify-between items-center">
        <div>
          <h3 className="text-xl font-bold text-slate-100">{roomName} Smart Environment</h3>
          <p className="text-sm text-slate-400">Classroom HVAC setpoint, ambient lighting, and motion sensor telemetry.</p>
        </div>
        <span
          className={`px-3 py-1 text-xs font-semibold rounded-full border ${
            occupied ? "bg-emerald-500/10 text-emerald-400 border-emerald-500/30" : "bg-slate-700 text-slate-400 border-slate-600"
          }`}
        >
          {occupied ? "● Occupied" : "○ Vacant"}
        </span>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div className="p-4 bg-slate-900/60 border border-slate-700/60 rounded-lg space-y-3">
          <div className="flex justify-between items-center">
            <span className="text-sm font-medium text-slate-300">HVAC Target Temperature</span>
            <span className="text-xl font-bold font-mono text-indigo-400">{temp.toFixed(1)} °C</span>
          </div>
          <input
            type="range"
            min="18"
            max="28"
            step="0.5"
            value={temp}
            onChange={(e) => setTemp(parseFloat(e.target.value))}
            className="w-full accent-indigo-500"
          />
        </div>

        <div className="p-4 bg-slate-900/60 border border-slate-700/60 rounded-lg space-y-3">
          <div className="flex justify-between items-center">
            <span className="text-sm font-medium text-slate-300">Lighting Level</span>
            <span className="text-xl font-bold font-mono text-amber-400">{lighting}%</span>
          </div>
          <input
            type="range"
            min="0"
            max="100"
            step="5"
            value={lighting}
            onChange={(e) => setLighting(parseInt(e.target.value))}
            className="w-full accent-amber-500"
          />
        </div>
      </div>
    </div>
  );
};
