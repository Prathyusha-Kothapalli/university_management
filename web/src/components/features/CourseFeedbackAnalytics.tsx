import React from 'react';
import { BarChart2, Star, Smile } from 'lucide-react';

export const CourseFeedbackAnalytics: React.FC = () => {
  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-5">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-3">
          <div className="p-2.5 bg-indigo-50 text-indigo-600 rounded-lg">
            <BarChart2 className="w-5 h-5" />
          </div>
          <div>
            <h3 className="font-semibold text-gray-900">End-of-Semester Course Feedback Analytics</h3>
            <p className="text-xs text-gray-500">Student course evaluation scores & faculty teaching effectiveness matrix</p>
          </div>
        </div>

        <span className="text-xs font-bold text-indigo-700 bg-indigo-50 px-3 py-1 rounded-full border border-indigo-100 flex items-center gap-1">
          <Smile className="w-3.5 h-3.5 text-indigo-600" /> 4.85 / 5.0 Rating
        </span>
      </div>

      <div className="space-y-3">
        <div className="p-3.5 rounded-xl border border-gray-100 bg-gray-50/40 space-y-2">
          <div className="flex items-center justify-between">
            <h4 className="font-bold text-xs text-gray-900">CS-401: Advanced AI & Machine Learning</h4>
            <span className="text-xs text-amber-500 font-bold flex items-center gap-0.5">
              <Star className="w-3.5 h-3.5 fill-amber-400" /> 4.90 (140 Responses)
            </span>
          </div>

          <div className="grid grid-cols-3 gap-2 text-xs bg-white p-2.5 rounded-lg border border-gray-100">
            <div>
              <span className="text-gray-400">Pacing & Content:</span>
              <div className="font-semibold text-gray-800">4.9 / 5.0</div>
            </div>
            <div>
              <span className="text-gray-400">Lab & PyTorch Projects:</span>
              <div className="font-semibold text-emerald-700">4.95 / 5.0</div>
            </div>
            <div>
              <span className="text-gray-400">Office Hour Support:</span>
              <div className="font-semibold text-indigo-700">4.85 / 5.0</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
