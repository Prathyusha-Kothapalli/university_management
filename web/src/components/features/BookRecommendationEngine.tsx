import React, { useState } from 'react';
import { BookOpen, Sparkles, Star, Plus } from 'lucide-react';

interface RecommendedBook {
  id: string;
  title: string;
  author: string;
  courseTag: string;
  rating: number;
  reason: string;
}

export const BookRecommendationEngine: React.FC = () => {
  const [books] = useState<RecommendedBook[]>([
    {
      id: 'rb-101',
      title: 'Designing Data-Intensive Applications',
      author: 'Martin Kleppmann',
      courseTag: 'CS-402 Distributed Systems',
      rating: 4.9,
      reason: 'Highly recommended for understanding distributed consensus & transactional storage.'
    },
    {
      id: 'rb-102',
      title: 'Deep Learning (Adaptive Computation and Machine Learning series)',
      author: 'Ian Goodfellow, Yoshua Bengio, Aaron Courville',
      courseTag: 'CS-401 Artificial Intelligence',
      rating: 4.8,
      reason: 'Syllabus reference book for Neural Networks and Backpropagation math.'
    }
  ]);

  const [savedIds, setSavedIds] = useState<string[]>([]);

  const handleSave = (id: string) => {
    if (!savedIds.includes(id)) {
      setSavedIds([...savedIds, id]);
    }
  };

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-5">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-3">
          <div className="p-2.5 bg-indigo-50 text-indigo-600 rounded-lg">
            <BookOpen className="w-5 h-5" />
          </div>
          <div>
            <h3 className="font-semibold text-gray-900">Course-Curated Book Recommendation Engine</h3>
            <p className="text-xs text-gray-500">Personalized textbook & reference reading lists aligned to active semester courses</p>
          </div>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
        {books.map(b => (
          <div key={b.id} className="p-4 rounded-xl border border-gray-100 bg-gray-50/40 space-y-2 flex flex-col justify-between">
            <div>
              <div className="flex items-center justify-between mb-1">
                <span className="text-[10px] font-bold text-indigo-700 bg-indigo-100 px-2 py-0.5 rounded">
                  {b.courseTag}
                </span>
                <span className="text-xs text-amber-500 font-bold flex items-center gap-0.5">
                  <Star className="w-3.5 h-3.5 fill-amber-400" /> {b.rating}
                </span>
              </div>
              <h4 className="font-bold text-xs text-gray-900">{b.title}</h4>
              <p className="text-xs text-gray-500">{b.author}</p>
              <div className="p-2 bg-white rounded-lg border border-gray-100 text-xs text-gray-600 mt-2 italic">
                <Sparkles className="w-3 h-3 text-indigo-500 inline mr-1" />
                {b.reason}
              </div>
            </div>

            <button
              onClick={() => handleSave(b.id)}
              className={`w-full py-1.5 text-xs font-semibold rounded-lg flex items-center justify-center gap-1 transition-all mt-2 ${
                savedIds.includes(b.id)
                  ? 'bg-emerald-50 text-emerald-700 border border-emerald-200'
                  : 'bg-indigo-600 hover:bg-indigo-700 text-white shadow-sm'
              }`}
            >
              {savedIds.includes(b.id) ? 'Saved to Reading List' : <><Plus className="w-3.5 h-3.5" /> Add to Reading List</>}
            </button>
          </div>
        ))}
      </div>
    </div>
  );
};
