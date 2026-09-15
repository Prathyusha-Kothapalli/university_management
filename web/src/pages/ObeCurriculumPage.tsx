import React, { useState } from "react";
import { CoPoMatrixTable, CoPoEntry } from "../components/Curriculum/CoPoMatrixTable";

export const ObeCurriculumPage: React.FC = () => {
  const programOutcomes = ["PO1", "PO2", "PO3", "PO4", "PO5", "PO6"];

  const [matrixData] = useState<CoPoEntry[]>([
    {
      co_code: "CO1",
      bloom_level: "Understand & Apply",
      target_pct: 75,
      mapped_pos: [
        { po_code: "PO1", weight: 3 },
        { po_code: "PO2", weight: 2 },
        { po_code: "PO3", weight: 1 },
      ],
    },
    {
      co_code: "CO2",
      bloom_level: "Analyze & Design",
      target_pct: 80,
      mapped_pos: [
        { po_code: "PO2", weight: 3 },
        { po_code: "PO3", weight: 3 },
        { po_code: "PO4", weight: 2 },
      ],
    },
    {
      co_code: "CO3",
      bloom_level: "Evaluate & Synthesize",
      target_pct: 70,
      mapped_pos: [
        { po_code: "PO1", weight: 2 },
        { po_code: "PO4", weight: 3 },
        { po_code: "PO5", weight: 3 },
        { po_code: "PO6", weight: 2 },
      ],
    },
  ]);

  return (
    <div className="min-h-screen bg-slate-900 text-slate-100 p-6 space-y-6">
      <div className="flex justify-between items-center border-b border-slate-800 pb-6">
        <div>
          <h1 className="text-3xl font-extrabold text-slate-100">Outcome-Based Education (OBE) & Curriculum Matrix</h1>
          <p className="text-slate-400 mt-1">
            Formulate Course Outcomes (COs), Program Educational Objectives (PEOs), and compliance reports for NBA/ABET accreditation.
          </p>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-6">
        <div className="bg-slate-800 border border-slate-700 rounded-xl p-5 shadow-lg">
          <span className="text-xs font-semibold uppercase tracking-wider text-slate-400">Total Program Outcomes</span>
          <p className="text-3xl font-bold font-mono text-indigo-400 mt-2">12 POs</p>
          <span className="text-xs text-slate-500 mt-1 block">Engineering & Computing Standards</span>
        </div>

        <div className="bg-slate-800 border border-slate-700 rounded-xl p-5 shadow-lg">
          <span className="text-xs font-semibold uppercase tracking-wider text-slate-400">Avg Target Attainment Threshold</span>
          <p className="text-3xl font-bold font-mono text-emerald-400 mt-2">75.0%</p>
          <span className="text-xs text-slate-500 mt-1 block">Continuous Quality Improvement (CQI)</span>
        </div>

        <div className="bg-slate-800 border border-slate-700 rounded-xl p-5 shadow-lg">
          <span className="text-xs font-semibold uppercase tracking-wider text-slate-400">Accreditation Readiness Status</span>
          <p className="text-3xl font-bold text-sky-400 mt-2">Tier-1 Compliant</p>
          <span className="text-xs text-slate-500 mt-1 block">Automated SAR Dossier Generated</span>
        </div>
      </div>

      <CoPoMatrixTable matrixData={matrixData} programOutcomes={programOutcomes} />
    </div>
  );
};
