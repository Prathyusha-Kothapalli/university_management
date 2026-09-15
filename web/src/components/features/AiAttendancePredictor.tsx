import React, { useState } from 'react';
import { ShieldAlert, TrendingDown } from 'lucide-react';

interface RiskStudent {
  id: string;
  name: string;
  rollNo: string;
  attendancePct: number;
  classesNeeded: number;
  riskLevel: 'High Risk (Below 75%)' | 'Moderate Risk (75%-80%)' | 'Safe (>80%)';
}

export const AiAttendancePredictor: React.FC = () => {
  const [students] = useState<RiskStudent[]>([
    { id: 'st-1', name: 'Vikram Mehta', rollNo: '22CSE104', attendancePct: 68.5, classesNeeded: 6, riskLevel: 'High Risk (Below 75%)' },
    { id: 'st-2', name: 'Sneha Kulkarni', rollNo: '22CSE118', attendancePct: 76.2, classesNeeded: 2, riskLevel: 'Moderate Risk (75%-80%)' },
    { id: 'st-3', name: 'Kavya Pillai', rollNo: '22CSE089', attendancePct: 89.0, classesNeeded: 0, riskLevel: 'Safe (>80%)' },
  ]);

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-5">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-3">
          <div className="p-2.5 bg-rose-50 text-rose-600 rounded-lg">
            <ShieldAlert className="w-5 h-5" />
          </div>
          <div>
            <h3 className="font-semibold text-gray-900">AI Attendance Shortage Risk Predictor</h3>
            <p className="text-xs text-gray-500">Predictive attendance shortage detector for academic advisor intervention</p>
          </div>
        </div>
      </div>

      <div className="space-y-3">
        {students.map(s => (
          <div key={s.id} className="p-4 rounded-xl border border-gray-100 bg-gray-50/40 flex items-center justify-between">
            <div className="flex items-center gap-3">
              <div className={`p-2 rounded-lg font-bold text-xs ${
                s.attendancePct < 75 ? 'bg-rose-100 text-rose-700' : 'bg-amber-100 text-amber-700'
              }`}>
                {s.attendancePct}%
              </div>
              <div>
                <div className="flex items-center gap-2">
                  <h4 className="font-semibold text-xs text-gray-900">{s.name}</h4>
                  <span className="font-mono text-[11px] text-gray-400">({s.rollNo})</span>
                </div>
                <p className="text-xs text-gray-500 mt-0.5">
                  {s.classesNeeded > 0
                    ? `Requires ${s.classesNeeded} consecutive lectures to reach 75% threshold.`
                    : 'Attendance status compliant for end-semester exams.'}
                </p>
              </div>
            </div>

            <div>
              <span className={`text-[11px] font-semibold px-2.5 py-1 rounded-full flex items-center gap-1 ${
                s.attendancePct < 75 ? 'bg-rose-100 text-rose-800' :
                s.attendancePct <= 80 ? 'bg-amber-100 text-amber-800' :
                'bg-emerald-100 text-emerald-800'
              }`}>
                {s.attendancePct < 75 && <TrendingDown className="w-3.5 h-3.5" />}
                {s.riskLevel}
              </span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
