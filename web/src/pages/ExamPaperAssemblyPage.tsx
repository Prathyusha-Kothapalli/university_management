import React, { useState } from "react";
import { ProctoringTelemetryDashboard, ProctorEvent } from "../components/Exams/ProctoringTelemetryDashboard";

export const ExamPaperAssemblyPage: React.FC = () => {
  const [activeTab, setActiveTab] = useState<"assembly" | "telemetry">("assembly");

  const [questions] = useState([
    { id: "q1", text: "Explain time complexity of Quicksort worst-case vs average-case.", type: "SHORT_ANSWER", points: 5, difficulty: "MEDIUM" },
    { id: "q2", text: "Which data structure implements FIFO ordering?", type: "MCQ", points: 2, difficulty: "EASY" },
    { id: "q3", text: "Design a B-Tree node split algorithm in C++.", type: "CODING", points: 15, difficulty: "HARD" },
  ]);

  const [proctorEvents] = useState<ProctorEvent[]>([
    { id: "ev1", student_name: "Daniel Vance", anomaly_type: "TAB_SWITCH", confidence_score: 0.98, logged_at: "2026-03-12T10:14:22Z" },
    { id: "ev2", student_name: "Marcus Brody", anomaly_type: "MULTIPLE_FACES", confidence_score: 0.91, logged_at: "2026-03-12T10:18:05Z" },
  ]);

  return (
    <div className="min-h-screen bg-slate-900 text-slate-100 p-6 space-y-6">
      <div className="flex justify-between items-center border-b border-slate-800 pb-6">
        <div>
          <h1 className="text-3xl font-extrabold text-slate-100">Exam Paper Generator & Proctoring</h1>
          <p className="text-slate-400 mt-1">Assemble balanced exam papers from question banks and inspect live AI proctoring telemetry.</p>
        </div>
      </div>

      <div className="flex space-x-2 border-b border-slate-800">
        <button
          onClick={() => setActiveTab("assembly")}
          className={`px-4 py-2.5 font-medium text-sm border-b-2 transition-colors ${
            activeTab === "assembly"
              ? "border-indigo-500 text-indigo-400 font-semibold"
              : "border-transparent text-slate-400 hover:text-slate-200"
          }`}
        >
          Exam Paper Assembly ({questions.length} Questions)
        </button>
        <button
          onClick={() => setActiveTab("telemetry")}
          className={`px-4 py-2.5 font-medium text-sm border-b-2 transition-colors ${
            activeTab === "telemetry"
              ? "border-indigo-500 text-indigo-400 font-semibold"
              : "border-transparent text-slate-400 hover:text-slate-200"
          }`}
        >
          Proctoring Anomaly Log ({proctorEvents.length})
        </button>
      </div>

      {activeTab === "assembly" && (
        <div className="bg-slate-800 border border-slate-700 rounded-xl p-6 shadow-xl space-y-4">
          <div className="flex justify-between items-center">
            <h3 className="text-xl font-bold text-slate-100">Assembled Exam Paper: Data Structures Midterm</h3>
            <span className="px-3 py-1 bg-indigo-500/10 text-indigo-400 font-mono text-sm font-semibold rounded-lg">
              Total Marks: 22 / 100
            </span>
          </div>

          <div className="space-y-3">
            {questions.map((q, idx) => (
              <div key={q.id} className="p-4 bg-slate-900/60 border border-slate-700/60 rounded-lg flex items-center justify-between">
                <div>
                  <span className="text-xs font-bold text-indigo-400 mr-2 font-mono">Q{idx + 1}. [{q.type}]</span>
                  <p className="text-sm font-medium text-slate-200 mt-1">{q.text}</p>
                </div>
                <div className="text-right">
                  <span className="text-sm font-bold font-mono text-emerald-400">{q.points} Marks</span>
                  <span className="block text-[10px] text-slate-400 uppercase tracking-wider">{q.difficulty}</span>
                </div>
              </div>
            ))}
          </div>

          <div className="flex justify-end pt-4">
            <button className="px-5 py-2.5 bg-indigo-600 hover:bg-indigo-500 text-white font-semibold text-sm rounded-lg shadow-lg transition-colors">
              Publish Exam Paper
            </button>
          </div>
        </div>
      )}

      {activeTab === "telemetry" && (
        <ProctoringTelemetryDashboard events={proctorEvents} />
      )}
    </div>
  );
};
