import React from "react";
import { AstComplexityMetrics } from "../components/Evaluation/AstComplexityMetrics";

export const AstEvaluationGradingPage: React.FC = () => {
  return (
    <div className="min-h-screen bg-slate-900 text-slate-100 p-6 space-y-6">
      <div className="flex justify-between items-center border-b border-slate-800 pb-6">
        <div>
          <h1 className="text-3xl font-extrabold text-slate-100">AST Code Evaluation & Plagiarism Engine</h1>
          <p className="text-slate-400 mt-1">Automated AST parsing, cyclomatic complexity calculations, and pairwise plagiarism reports.</p>
        </div>
      </div>

      <div className="space-y-6">
        <AstComplexityMetrics
          submissionId="sub-9921-b44"
          cyclomaticComplexity={4}
          linterWarnings={0}
          similarityScore={0.12}
          isFlagged={false}
        />
        <AstComplexityMetrics
          submissionId="sub-8812-x11"
          cyclomaticComplexity={18}
          linterWarnings={5}
          similarityScore={0.88}
          isFlagged={true}
        />
      </div>
    </div>
  );
};
