import React, { useState } from 'react';
import { Briefcase, Star, Search, ThumbsUp } from 'lucide-react';

interface CompanyReview {
  id: string;
  company: string;
  role: string;
  ctcOffered: string;
  difficulty: 'Easy' | 'Medium' | 'Hard' | 'Very Hard';
  rating: number;
  testTopics: string;
  interviewAdvice: string;
  upvotes: number;
}

export const CompanyReviewHub: React.FC = () => {
  const [search, setSearch] = useState('');
  const [reviews, setReviews] = useState<CompanyReview[]>([
    {
      id: 'rev-1',
      company: 'Microsoft',
      role: 'Software Development Engineer (SDE-1)',
      ctcOffered: '₹44.0 LPA',
      difficulty: 'Hard',
      rating: 4.9,
      testTopics: 'Graph Algorithms, Dynamic Programming (2D DP), System Design (TinyURL)',
      interviewAdvice: 'Focus on clean O(N) space complexity & edge cases in binary tree traversal.',
      upvotes: 42
    },
    {
      id: 'rev-2',
      company: 'Amazon AWS',
      role: 'Cloud Systems Engineer',
      ctcOffered: '₹32.0 LPA',
      difficulty: 'Medium',
      rating: 4.7,
      testTopics: 'Linux Internals, Docker Networking, AWS IAM Scoping & Leadership Principles',
      interviewAdvice: 'Prepare 2 STAR format stories for every Amazon Leadership Principle.',
      upvotes: 28
    }
  ]);

  const handleUpvote = (id: string) => {
    setReviews(reviews.map(r => r.id === id ? { ...r, upvotes: r.upvotes + 1 } : r));
  };

  const filtered = reviews.filter(r => r.company.toLowerCase().includes(search.toLowerCase()) || r.role.toLowerCase().includes(search.toLowerCase()));

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-5">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-3">
          <div className="p-2.5 bg-teal-50 text-teal-600 rounded-lg">
            <Briefcase className="w-5 h-5" />
          </div>
          <div>
            <h3 className="font-semibold text-gray-900">Company Placement Review & Interview Experience Hub</h3>
            <p className="text-xs text-gray-500">Peer-contributed online test patterns, interview questions & compensation breakdowns</p>
          </div>
        </div>
      </div>

      <div className="relative mb-4">
        <Search className="w-4 h-4 text-gray-400 absolute left-3 top-2.5" />
        <input
          type="text"
          placeholder="Search placement reviews by company (e.g., Microsoft, Amazon)..."
          value={search}
          onChange={e => setSearch(e.target.value)}
          className="w-full text-xs border border-gray-200 rounded-lg pl-9 pr-3 py-2 focus:ring-2 focus:ring-teal-500 focus:outline-none"
        />
      </div>

      <div className="space-y-3">
        {filtered.map(r => (
          <div key={r.id} className="p-4 rounded-xl border border-gray-100 bg-gray-50/40 space-y-2">
            <div className="flex items-center justify-between">
              <div className="flex items-center gap-2">
                <h4 className="font-bold text-xs text-gray-900">{r.company}</h4>
                <span className="font-mono text-xs font-bold text-emerald-700 bg-emerald-100 px-2 py-0.5 rounded">
                  {r.ctcOffered}
                </span>
                <span className="text-[10px] bg-rose-100 text-rose-800 font-semibold px-2 py-0.5 rounded-full">
                  Difficulty: {r.difficulty}
                </span>
              </div>

              <div className="flex items-center gap-2">
                <span className="text-xs text-amber-500 font-bold flex items-center gap-0.5">
                  <Star className="w-3.5 h-3.5 fill-amber-400" /> {r.rating}
                </span>
                <button
                  onClick={() => handleUpvote(r.id)}
                  className="text-xs text-gray-500 hover:text-teal-600 bg-white border border-gray-200 px-2.5 py-1 rounded-lg flex items-center gap-1"
                >
                  <ThumbsUp className="w-3 h-3 text-teal-600" /> {r.upvotes}
                </button>
              </div>
            </div>

            <div className="text-xs text-gray-800 font-semibold">{r.role}</div>

            <div className="p-2.5 bg-white rounded-lg border border-gray-100 space-y-1 text-xs text-gray-600">
              <div><strong>Online Test Topics:</strong> {r.testTopics}</div>
              <div className="text-teal-800"><strong>Pro-Tip / Advice:</strong> {r.interviewAdvice}</div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
