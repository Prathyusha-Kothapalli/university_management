import React from "react";

export interface CoPoEntry {
  co_code: string;
  bloom_level: string;
  target_pct: number;
  mapped_pos: Array<{
    po_code: string;
    weight: number;
  }>;
}

interface CoPoMatrixTableProps {
  matrixData: CoPoEntry[];
  programOutcomes: string[]; // e.g. ["PO1", "PO2", "PO3", "PO4", "PO5"]
}

export const CoPoMatrixTable: React.FC<CoPoMatrixTableProps> = ({
  matrixData,
  programOutcomes,
}) => {
  const getMappedWeight = (co: CoPoEntry, poCode: string) => {
    const match = co.mapped_pos.find((item) => item.po_code === poCode);
    return match ? match.weight : "-";
  };

  return (
    <div className="bg-slate-800 border border-slate-700 rounded-xl p-6 shadow-xl overflow-x-auto">
      <div className="mb-6">
        <h3 className="text-xl font-bold text-slate-100">Outcome-Based Education (OBE) CO-PO Mapping Matrix</h3>
        <p className="text-sm text-slate-400">
          Direct mapping of Course Outcomes (CO) against Program Outcomes (PO) with Bloom's Taxonomy classification.
        </p>
      </div>

      <table className="w-full text-left border-collapse min-w-[700px]">
        <thead>
          <tr className="border-b border-slate-700 text-xs font-semibold text-slate-400 uppercase tracking-wider bg-slate-900/60">
            <th className="py-3 px-4">CO Code</th>
            <th className="py-3 px-4">Bloom's Taxonomy</th>
            <th className="py-3 px-4 text-center">Target Attainment</th>
            {programOutcomes.map((po) => (
              <th key={po} className="py-3 px-4 text-center font-mono text-indigo-400">
                {po}
              </th>
            ))}
          </tr>
        </thead>
        <tbody className="divide-y divide-slate-700/60 text-sm">
          {matrixData.length === 0 ? (
            <tr>
              <td colSpan={3 + programOutcomes.length} className="text-center py-6 text-slate-500">
                No course outcome mappings configured yet.
              </td>
            </tr>
          ) : (
            matrixData.map((co) => (
              <tr key={co.co_code} className="hover:bg-slate-700/30 transition-colors">
                <td className="py-3 px-4 font-bold text-slate-100 font-mono">{co.co_code}</td>
                <td className="py-3 px-4">
                  <span className="px-2 py-1 text-xs font-medium bg-slate-700 text-slate-300 rounded">
                    {co.bloom_level}
                  </span>
                </td>
                <td className="py-3 px-4 text-center font-mono text-emerald-400 font-medium">
                  {co.target_pct}%
                </td>
                {programOutcomes.map((po) => {
                  const weight = getMappedWeight(co, po);
                  return (
                    <td key={po} className="py-3 px-4 text-center font-mono font-bold">
                      {weight === 3 ? (
                        <span className="text-emerald-400">3 (High)</span>
                      ) : weight === 2 ? (
                        <span className="text-amber-400">2 (Med)</span>
                      ) : weight === 1 ? (
                        <span className="text-blue-400">1 (Low)</span>
                      ) : (
                        <span className="text-slate-600">-</span>
                      )}
                    </td>
                  );
                })}
              </tr>
            ))
          )}
        </tbody>
      </table>
    </div>
  );
};
