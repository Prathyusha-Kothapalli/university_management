import React from 'react';
import { BarChart3, TrendingUp, Award, Users, BookOpen } from 'lucide-react';

export const DepartmentAnalyticsHub: React.FC = () => {
  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-5">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-3">
          <div className="p-2.5 bg-indigo-50 text-indigo-600 rounded-lg">
            <BarChart3 className="w-5 h-5" />
          </div>
          <div>
            <h3 className="font-semibold text-gray-900">HOD Executive Department Analytics Hub</h3>
            <p className="text-xs text-gray-500">Executive metrics comparing semester pass %, placement offers & research publications</p>
          </div>
        </div>

        <span className="text-xs font-bold text-indigo-700 bg-indigo-50 px-3 py-1 rounded-full border border-indigo-100 flex items-center gap-1">
          <TrendingUp className="w-3.5 h-3.5" /> Department Rank #1 (CSE)
        </span>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-3">
        <div className="p-3.5 rounded-xl border border-gray-100 bg-indigo-50/30">
          <div className="flex justify-between items-start">
            <div>
              <div className="text-[11px] text-gray-500 font-semibold">Semester Pass Rate</div>
              <div className="font-extrabold text-lg text-gray-900 font-mono mt-0.5">94.8%</div>
            </div>
            <BookOpen className="w-5 h-5 text-indigo-600" />
          </div>
          <div className="text-[10px] text-emerald-600 font-bold mt-1">+2.4% vs last year</div>
        </div>

        <div className="p-3.5 rounded-xl border border-gray-100 bg-indigo-50/30">
          <div className="flex justify-between items-start">
            <div>
              <div className="text-[11px] text-gray-500 font-semibold">Placement Rate</div>
              <div className="font-extrabold text-lg text-gray-900 font-mono mt-0.5">91.2%</div>
            </div>
            <Award className="w-5 h-5 text-emerald-600" />
          </div>
          <div className="text-[10px] text-emerald-600 font-bold mt-1">Highest CTC ₹44 LPA</div>
        </div>

        <div className="p-3.5 rounded-xl border border-gray-100 bg-indigo-50/30">
          <div className="flex justify-between items-start">
            <div>
              <div className="text-[11px] text-gray-500 font-semibold">Research Papers Published</div>
              <div className="font-extrabold text-lg text-gray-900 font-mono mt-0.5">48 Papers</div>
            </div>
            <BarChart3 className="w-5 h-5 text-purple-600" />
          </div>
          <div className="text-[10px] text-purple-600 font-bold mt-1">IEEE & Scopus Indexed</div>
        </div>

        <div className="p-3.5 rounded-xl border border-gray-100 bg-indigo-50/30">
          <div className="flex justify-between items-start">
            <div>
              <div className="text-[11px] text-gray-500 font-semibold">Faculty Cadre Uptime</div>
              <div className="font-extrabold text-lg text-gray-900 font-mono mt-0.5">98.5%</div>
            </div>
            <Users className="w-5 h-5 text-amber-600" />
          </div>
          <div className="text-[10px] text-amber-600 font-bold mt-1">42 Full-Time Faculty</div>
        </div>
      </div>
    </div>
  );
};
