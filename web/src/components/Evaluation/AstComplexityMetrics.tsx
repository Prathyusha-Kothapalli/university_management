import React from "react";

interface AstComplexityMetricsProps {
  submissionId: string;
  cyclomaticComplexity: number;
  linterWarnings: number;
  similarityScore: number;
  isFlagged: boolean;
}

export const AstComplexityMetrics: React.FC<AstComplexityMetricsProps> = ({
  submissionId,
  cyclomaticComplexity,
  linterWarnings,
  similarityScore,
  isFlagged,
}) => {
  return (
    <div className="bg-slate-800 border border-slate-700 rounded-xl p-6 shadow-xl space-y-4">
      <div className="flex justify-between items-center">
        <div>
          <h3 className="text-xl font-bold text-slate-100">AST Code Evaluation & Plagiarism Report</h3>
          <p className="text-sm text-slate-400">Submission ID: <span className="font-mono text-indigo-300">{submissionId.substring(0, 8)}...</span></p>
        </div>
        <span
          className={`px-3 py-1 text-xs font-semibold rounded-full border ${
            isFlagged ? "bg-rose-500/10 text-rose-400 border-rose-500/30" : "bg-emerald-500/10 text-emerald-400 border-emerald-500/30"
          }`}
        >
          {isFlagged ? "⚠️ Plagiarism Flagged" : "✓ Clean Code Baseline"}
        </span>
      </div>

      <div className="grid grid-cols-3 gap-4 font-mono text-center">
        <div className="p-4 bg-slate-900/60 border border-slate-700/60 rounded-lg">
          <span className="text-[10px] text-slate-400 uppercase tracking-wider block font-sans">Cyclomatic Complexity</span>
          <span className="text-2xl font-bold text-indigo-400 mt-1 block">{cyclomaticComplexity}</span>
        </div>

        <div className="p-4 bg-slate-900/60 border border-slate-700/60 rounded-lg">
          <span className="text-[10px] text-slate-400 uppercase tracking-wider block font-sans">Linter Warnings</span>
          <span className="text-2xl font-bold text-amber-400 mt-1 block">{linterWarnings}</span>
        </div>

        <div className="p-4 bg-slate-900/60 border border-slate-700/60 rounded-lg">
          <span className="text-[10px] text-slate-400 uppercase tracking-wider block font-sans">AST Similarity</span>
          <span className={`text-2xl font-bold mt-1 block ${isFlagged ? "text-rose-400" : "text-emerald-400"}`}>
            {(similarityScore * 100).toFixed(1)}%
          </span>
        </div>
      </div>
    </div>
  );
};
