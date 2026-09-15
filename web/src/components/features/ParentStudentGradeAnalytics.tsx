import React from 'react';
import { Award, TrendingUp } from 'lucide-react';

export const ParentStudentGradeAnalytics: React.FC = () => {
  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-5">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-3">
          <div className="p-2.5 bg-blue-50 text-blue-600 rounded-lg">
            <Award className="w-5 h-5" />
          </div>
          <div>
            <h3 className="font-semibold text-gray-900">Parent Student Grade & Attendance Analytics</h3>
            <p className="text-xs text-gray-500">Comprehensive academic progress breakdown for Parent/Guardian supervision</p>
          </div>
        </div>

        <span className="text-xs font-bold text-emerald-700 bg-emerald-50 px-3 py-1 rounded-full border border-emerald-200 flex items-center gap-1">
          <TrendingUp className="w-3.5 h-3.5" /> SGPA 3.84 (Top 5%)
        </span>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-3">
        <div className="p-4 rounded-xl border border-gray-100 bg-blue-50/30">
          <div className="text-xs font-semibold text-gray-500">Cumulative GPA (CGPA)</div>
          <div className="font-extrabold text-xl text-gray-900 font-mono mt-1">3.84 / 4.0</div>
          <div className="text-[11px] text-emerald-600 font-bold mt-1">A Grade Standing</div>
        </div>

        <div className="p-4 rounded-xl border border-gray-100 bg-blue-50/30">
          <div className="text-xs font-semibold text-gray-500">Semester Attendance</div>
          <div className="font-extrabold text-xl text-emerald-700 font-mono mt-1">94.5%</div>
          <div className="text-[11px] text-gray-500 mt-1">18 of 19 Classes Attended</div>
        </div>

        <div className="p-4 rounded-xl border border-gray-100 bg-blue-50/30">
          <div className="text-xs font-semibold text-gray-500">Degree Credits Earned</div>
          <div className="font-extrabold text-xl text-purple-700 font-mono mt-1">76 / 120</div>
          <div className="text-[11px] text-purple-600 font-bold mt-1">63.3% Degree Complete</div>
        </div>
      </div>
    </div>
  );
};
