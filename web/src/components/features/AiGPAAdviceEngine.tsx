import React, { useState } from 'react';
import { Calculator, Sparkles, Award } from 'lucide-react';

export const AiGPAAdviceEngine: React.FC = () => {
  const [targetGpa, setTargetGpa] = useState<number>(3.90);
  const [calculatedTarget] = useState({
    requiredMidtermPct: 92,
    requiredFinalPct: 88,
    adviceText: 'To achieve 3.90 target CGPA, aim for minimum 92% in CS-401 Machine Learning End-Sem exam.'
  });

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-5">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-3">
          <div className="p-2.5 bg-indigo-50 text-indigo-600 rounded-lg">
            <Calculator className="w-5 h-5" />
          </div>
          <div>
            <h3 className="font-semibold text-gray-900">AI Target GPA & Assignment Score Advice Engine</h3>
            <p className="text-xs text-gray-500">Reverse-engineers required assignment & exam scores to reach target CGPA</p>
          </div>
        </div>

        <span className="text-xs font-bold text-indigo-700 bg-indigo-50 px-3 py-1 rounded-full border border-indigo-100 flex items-center gap-1">
          <Award className="w-3.5 h-3.5 text-indigo-600" /> Current CGPA 3.84
        </span>
      </div>

      <div className="p-4 rounded-xl border border-indigo-100 bg-indigo-50/30 space-y-3">
        <div className="flex items-center justify-between">
          <label className="text-xs font-semibold text-gray-800">Desired Target CGPA Goal:</label>
          <input
            type="number"
            step="0.05"
            min="3.0"
            max="4.0"
            value={targetGpa}
            onChange={e => setTargetGpa(Number(e.target.value))}
            className="text-xs border border-gray-200 rounded-lg px-3 py-1.5 font-bold font-mono text-indigo-700 bg-white focus:ring-2 focus:ring-indigo-500"
          />
        </div>

        <div className="grid grid-cols-2 gap-2 text-xs bg-white p-3 rounded-lg border border-gray-100">
          <div>
            <span className="text-gray-400">Req. Midterm Score:</span>
            <div className="font-bold text-gray-900 font-mono">{calculatedTarget.requiredMidtermPct}%</div>
          </div>
          <div>
            <span className="text-gray-400">Req. End-Sem Score:</span>
            <div className="font-bold text-emerald-700 font-mono">{calculatedTarget.requiredFinalPct}%</div>
          </div>
        </div>

        <div className="text-xs text-indigo-800 font-medium italic bg-white p-2.5 rounded-lg border border-gray-100">
          <Sparkles className="w-3.5 h-3.5 text-indigo-500 inline mr-1" />
          {calculatedTarget.adviceText}
        </div>
      </div>
    </div>
  );
};
