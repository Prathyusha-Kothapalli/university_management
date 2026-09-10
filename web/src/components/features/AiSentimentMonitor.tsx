import React, { useState } from 'react';
import { Brain, TrendingUp, Smile, Frown, Meh, RefreshCw } from 'lucide-react';

interface SentimentData {
  department: string;
  course: string;
  engagementScore: number;
  sentiment: 'Positive' | 'Neutral' | 'At Risk';
  positivePct: number;
  neutralPct: number;
  negativePct: number;
  aiInsights: string[];
}

export const AiSentimentMonitor: React.FC = () => {
  const [selectedDept, setSelectedDept] = useState<string>('CSE');
  const [analyzing, setAnalyzing] = useState(false);

  const mockData: SentimentData[] = [
    {
      department: 'CSE',
      course: 'CS-401 Advanced AI & Deep Learning',
      engagementScore: 92,
      sentiment: 'Positive',
      positivePct: 78,
      neutralPct: 17,
      negativePct: 5,
      aiInsights: [
        'High interactive lab participation (94% completion rate).',
        'Students praised hands-on PyTorch assignments.',
        'Minor difficulty reported in GPU allocation timing.'
      ]
    },
    {
      department: 'CSE',
      course: 'CS-302 Data Structures & Algorithms',
      engagementScore: 74,
      sentiment: 'Neutral',
      positivePct: 55,
      neutralPct: 30,
      negativePct: 15,
      aiInsights: [
        'Midterm exam stress detected in recent feedback.',
        'Graph algorithms module required 2 additional tutorial hours.',
        'Attendance dropped 4% during Week 8 revision.'
      ]
    },
    {
      department: 'ECE',
      course: 'EC-204 VLSI Circuit Design',
      engagementScore: 58,
      sentiment: 'At Risk',
      positivePct: 35,
      neutralPct: 32,
      negativePct: 33,
      aiInsights: [
        'PSpice lab simulation software setup issues reported by 28 students.',
        'Requires immediate TA intervention and office hour expansion.',
        'Average assignment score down 12% compared to last semester.'
      ]
    }
  ];

  const filtered = mockData.filter(d => selectedDept === 'All' || d.department === selectedDept);

  const handleRefresh = () => {
    setAnalyzing(true);
    setTimeout(() => {
      setAnalyzing(false);
    }, 800);
  };

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-5">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-3">
          <div className="p-2.5 bg-indigo-50 text-indigo-600 rounded-lg">
            <Brain className="w-5 h-5" />
          </div>
          <div>
            <h3 className="font-semibold text-gray-900">AI Sentiment & Engagement Monitor</h3>
            <p className="text-xs text-gray-500">Real-time NLP sentiment analysis across course feedback & attendance</p>
          </div>
        </div>
        <div className="flex items-center gap-2">
          <select
            value={selectedDept}
            onChange={(e) => setSelectedDept(e.target.value)}
            className="text-xs border border-gray-200 rounded-lg px-2.5 py-1.5 focus:outline-none focus:ring-2 focus:ring-indigo-500"
          >
            <option value="All">All Departments</option>
            <option value="CSE">CSE</option>
            <option value="ECE">ECE</option>
          </select>
          <button
            onClick={handleRefresh}
            disabled={analyzing}
            className="p-1.5 text-gray-400 hover:text-indigo-600 rounded-lg hover:bg-gray-50 transition-colors"
          >
            <RefreshCw className={`w-4 h-4 ${analyzing ? 'animate-spin text-indigo-600' : ''}`} />
          </button>
        </div>
      </div>

      <div className="space-y-4">
        {filtered.map((item, idx) => (
          <div key={idx} className="p-4 rounded-xl border border-gray-100 bg-gray-50/50 space-y-3">
            <div className="flex items-center justify-between">
              <div>
                <span className="text-xs font-semibold text-indigo-600 bg-indigo-50 px-2 py-0.5 rounded-full mr-2">
                  {item.department}
                </span>
                <span className="font-medium text-sm text-gray-900">{item.course}</span>
              </div>
              <div className="flex items-center gap-2">
                <span className={`text-xs font-medium px-2.5 py-1 rounded-full flex items-center gap-1 ${
                  item.sentiment === 'Positive' ? 'bg-emerald-50 text-emerald-700' :
                  item.sentiment === 'Neutral' ? 'bg-amber-50 text-amber-700' :
                  'bg-rose-50 text-rose-700'
                }`}>
                  {item.sentiment === 'Positive' && <Smile className="w-3.5 h-3.5" />}
                  {item.sentiment === 'Neutral' && <Meh className="w-3.5 h-3.5" />}
                  {item.sentiment === 'At Risk' && <Frown className="w-3.5 h-3.5" />}
                  {item.sentiment}
                </span>
                <span className="text-xs font-bold text-gray-700">{item.engagementScore}% Engagement</span>
              </div>
            </div>

            {/* Sentiment Breakdown Bar */}
            <div className="space-y-1">
              <div className="flex justify-between text-[11px] text-gray-500">
                <span>Positive ({item.positivePct}%)</span>
                <span>Neutral ({item.neutralPct}%)</span>
                <span>Negative ({item.negativePct}%)</span>
              </div>
              <div className="h-2 w-full bg-gray-200 rounded-full overflow-hidden flex">
                <div style={{ width: `${item.positivePct}%` }} className="bg-emerald-500 h-full" />
                <div style={{ width: `${item.neutralPct}%` }} className="bg-amber-400 h-full" />
                <div style={{ width: `${item.negativePct}%` }} className="bg-rose-500 h-full" />
              </div>
            </div>

            {/* AI Insights */}
            <div className="bg-white p-3 rounded-lg border border-gray-100 space-y-1">
              <div className="flex items-center gap-1.5 text-xs font-semibold text-indigo-700 mb-1">
                <TrendingUp className="w-3.5 h-3.5" />
                AI Observations & Recommendations
              </div>
              <ul className="space-y-1">
                {item.aiInsights.map((insight, iIdx) => (
                  <li key={iIdx} className="text-xs text-gray-600 flex items-start gap-1.5">
                    <span className="text-indigo-400 font-bold">•</span>
                    {insight}
                  </li>
                ))}
              </ul>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
