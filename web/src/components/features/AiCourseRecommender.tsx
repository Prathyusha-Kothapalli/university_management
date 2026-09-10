import React, { useState } from 'react';
import { Compass, Sparkles, BookOpen, CheckCircle2 } from 'lucide-react';

interface Recommendation {
  id: string;
  courseCode: string;
  courseTitle: string;
  track: 'Data Science & AI' | 'Cloud Infrastructure' | 'Cybersecurity' | 'Full-Stack Engineering';
  matchScore: number;
  reason: string;
  credits: number;
}

export const AiCourseRecommender: React.FC = () => {
  const [selectedTrack, setSelectedTrack] = useState<string>('All');
  const [enrolledIds, setEnrolledIds] = useState<string[]>([]);

  const recommendations: Recommendation[] = [
    {
      id: 'rec-1',
      courseCode: 'CS-482',
      courseTitle: 'Deep Reinforcement Learning & Autonomous Agents',
      track: 'Data Science & AI',
      matchScore: 96,
      reason: 'Aligns with your 92% score in Linear Algebra and PyTorch lab project.',
      credits: 4
    },
    {
      id: 'rec-2',
      courseCode: 'CS-465',
      courseTitle: 'Cloud-Native Microservices with Kubernetes & Istio',
      track: 'Cloud Infrastructure',
      matchScore: 91,
      reason: 'Complements your completed Docker & AWS Cloud Foundations certification.',
      credits: 3
    },
    {
      id: 'rec-3',
      courseCode: 'CS-491',
      courseTitle: 'Applied Cryptography & Zero-Knowledge Proofs',
      track: 'Cybersecurity',
      matchScore: 88,
      reason: 'Recommended based on Discrete Mathematics grade and security interest.',
      credits: 4
    }
  ];

  const filtered = recommendations.filter(r => selectedTrack === 'All' || r.track === selectedTrack);

  const handleEnroll = (id: string) => {
    setEnrolledIds([...enrolledIds, id]);
  };

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-5">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-3">
          <div className="p-2.5 bg-sky-50 text-sky-600 rounded-lg">
            <Compass className="w-5 h-5" />
          </div>
          <div>
            <h3 className="font-semibold text-gray-900">AI Elective & Career Path Recommender</h3>
            <p className="text-xs text-gray-500">Smart course recommendations tailored to target career trajectories</p>
          </div>
        </div>

        <select
          value={selectedTrack}
          onChange={e => setSelectedTrack(e.target.value)}
          className="text-xs border border-gray-200 rounded-lg px-3 py-1.5 bg-white focus:ring-2 focus:ring-sky-500"
        >
          <option value="All">All Career Tracks</option>
          <option value="Data Science & AI">Data Science & AI</option>
          <option value="Cloud Infrastructure">Cloud Infrastructure</option>
          <option value="Cybersecurity">Cybersecurity</option>
        </select>
      </div>

      <div className="space-y-3">
        {filtered.map(rec => {
          const isEnrolled = enrolledIds.includes(rec.id);

          return (
            <div key={rec.id} className="p-4 rounded-xl border border-gray-100 bg-gray-50/50 flex items-center justify-between">
              <div className="flex items-center gap-3.5">
                <div className="p-2.5 bg-white border border-gray-200 rounded-xl text-sky-600 font-mono font-bold text-xs">
                  {rec.courseCode}
                </div>
                <div>
                  <div className="flex items-center gap-2">
                    <h4 className="font-bold text-xs text-gray-900">{rec.courseTitle}</h4>
                    <span className="text-[10px] bg-sky-50 text-sky-700 font-semibold px-2 py-0.5 rounded-full">
                      {rec.track}
                    </span>
                    <span className="text-[10px] text-emerald-600 font-bold bg-emerald-50 px-2 py-0.5 rounded-full flex items-center gap-0.5">
                      <Sparkles className="w-3 h-3 text-emerald-500" /> {rec.matchScore}% Match
                    </span>
                  </div>
                  <p className="text-xs text-gray-600 mt-1">{rec.reason}</p>
                </div>
              </div>

              <div className="shrink-0 ml-3">
                {isEnrolled ? (
                  <span className="text-xs text-emerald-700 bg-emerald-50 font-semibold px-3 py-1.5 rounded-lg flex items-center gap-1 border border-emerald-100">
                    <CheckCircle2 className="w-4 h-4 text-emerald-600" /> Enrolled
                  </span>
                ) : (
                  <button
                    onClick={() => handleEnroll(rec.id)}
                    className="bg-sky-600 hover:bg-sky-700 text-white text-xs font-semibold px-3.5 py-1.5 rounded-lg transition-colors flex items-center gap-1"
                  >
                    <BookOpen className="w-3.5 h-3.5" /> Add Elective ({rec.credits} Cr)
                  </button>
                )}
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
};
