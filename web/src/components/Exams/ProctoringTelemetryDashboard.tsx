import React from "react";

export interface ProctorEvent {
  id: string;
  student_name: string;
  anomaly_type: "FACE_NOT_DETECTED" | "MULTIPLE_FACES" | "NOISE_DETECTED" | "TAB_SWITCH";
  confidence_score: number;
  logged_at: string;
}

interface ProctoringTelemetryDashboardProps {
  events: ProctorEvent[];
}

export const ProctoringTelemetryDashboard: React.FC<ProctoringTelemetryDashboardProps> = ({ events }) => {
  const getBadgeStyle = (type: string) => {
    switch (type) {
      case "MULTIPLE_FACES":
        return "bg-rose-500/10 text-rose-400 border-rose-500/30";
      case "TAB_SWITCH":
        return "bg-amber-500/10 text-amber-400 border-amber-500/30";
      default:
        return "bg-blue-500/10 text-blue-400 border-blue-500/30";
    }
  };

  return (
    <div className="bg-slate-800 border border-slate-700 rounded-xl p-6 shadow-xl space-y-4">
      <div className="flex justify-between items-center">
        <div>
          <h3 className="text-xl font-bold text-slate-100">Live AI Proctoring Anomaly Telemetry</h3>
          <p className="text-sm text-slate-400">Computer vision and acoustic anomaly detections recorded in real time.</p>
        </div>
        <span className="px-3 py-1 bg-emerald-500/10 text-emerald-400 border border-emerald-500/30 rounded-full text-xs font-semibold animate-pulse">
          ● Live Proctoring Active
        </span>
      </div>

      <div className="space-y-3">
        {events.length === 0 ? (
          <div className="text-center py-6 text-slate-500">No proctoring anomaly events detected.</div>
        ) : (
          events.map((ev) => (
            <div key={ev.id} className="p-4 bg-slate-900/60 border border-slate-700/60 rounded-lg flex items-center justify-between">
              <div className="space-y-1">
                <span className="font-semibold text-slate-100">{ev.student_name}</span>
                <div className="flex items-center space-x-2">
                  <span className={`px-2.5 py-0.5 text-xs font-semibold border rounded-full ${getBadgeStyle(ev.anomaly_type)}`}>
                    {ev.anomaly_type}
                  </span>
                  <span className="text-xs text-slate-400">Confidence: {(ev.confidence_score * 100).toFixed(0)}%</span>
                </div>
              </div>
              <span className="text-xs font-mono text-slate-400">{new Date(ev.logged_at).toLocaleTimeString()}</span>
            </div>
          ))
        )}
      </div>
    </div>
  );
};
