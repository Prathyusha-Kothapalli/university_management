import React, { useState } from 'react';
import { MessageSquare, Send, CheckCircle2, Clock } from 'lucide-react';

interface FeedbackItem {
  id: string;
  category: 'Curriculum' | 'Hostel Facilities' | 'Library & Wi-Fi' | 'Exam Evaluation';
  subject: string;
  submittedAt: string;
  status: 'Under Review by HOD' | 'Resolved & Action Taken';
  anonymous: boolean;
}

export const StudentFeedbackBox: React.FC = () => {
  const [items, setItems] = useState<FeedbackItem[]>([
    { id: 'FB-901', category: 'Library & Wi-Fi', subject: 'Request 24/7 Library Study Hall access during Mid-Term week', submittedAt: '2026-09-07', status: 'Resolved & Action Taken', anonymous: true },
    { id: 'FB-902', category: 'Curriculum', subject: 'Incorporate PyTorch Hands-On Labs in CS-401 Machine Learning syllabus', submittedAt: '2026-09-09', status: 'Under Review by HOD', anonymous: true },
  ]);

  const [showModal, setShowModal] = useState(false);
  const [subject, setSubject] = useState('');
  const [category, setCategory] = useState<FeedbackItem['category']>('Curriculum');
  const [anonymous, setAnonymous] = useState(true);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!subject) return;

    const newItem: FeedbackItem = {
      id: `FB-${Math.floor(100 + Math.random() * 900)}`,
      category,
      subject,
      submittedAt: new Date().toISOString().split('T')[0],
      status: 'Under Review by HOD',
      anonymous
    };

    setItems([newItem, ...items]);
    setShowModal(false);
    setSubject('');
  };

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-5">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-3">
          <div className="p-2.5 bg-indigo-50 text-indigo-600 rounded-lg">
            <MessageSquare className="w-5 h-5" />
          </div>
          <div>
            <h3 className="font-semibold text-gray-900">Anonymous Student Feedback & Suggestion Box</h3>
            <p className="text-xs text-gray-500">Direct feedback channel to HOD & Dean with status resolution tracking</p>
          </div>
        </div>

        <button
          onClick={() => setShowModal(true)}
          className="bg-indigo-600 hover:bg-indigo-700 text-white text-xs font-semibold px-3.5 py-2 rounded-lg flex items-center gap-1.5 transition-colors shadow-sm"
        >
          <Send className="w-4 h-4" />
          Submit Feedback
        </button>
      </div>

      <div className="space-y-3">
        {items.map(item => (
          <div key={item.id} className="p-4 rounded-xl border border-gray-100 bg-gray-50/40 space-y-2">
            <div className="flex items-center justify-between">
              <div className="flex items-center gap-2">
                <span className="text-[10px] font-bold text-indigo-700 bg-indigo-100 px-2.5 py-0.5 rounded-full">
                  {item.category}
                </span>
                {item.anonymous && (
                  <span className="text-[10px] text-gray-500 bg-gray-200 px-2 py-0.5 rounded font-medium">
                    🔒 Anonymous
                  </span>
                )}
              </div>

              <span className={`text-[11px] font-semibold px-2.5 py-0.5 rounded-full flex items-center gap-1 ${
                item.status === 'Resolved & Action Taken' ? 'bg-emerald-50 text-emerald-700' : 'bg-amber-50 text-amber-700'
              }`}>
                {item.status === 'Resolved & Action Taken' ? (
                  <CheckCircle2 className="w-3.5 h-3.5 text-emerald-600" />
                ) : (
                  <Clock className="w-3.5 h-3.5 text-amber-600" />
                )}
                {item.status}
              </span>
            </div>

            <p className="text-xs text-gray-800 font-medium">{item.subject}</p>
            <div className="text-[11px] text-gray-400">Submitted: {item.submittedAt}</div>
          </div>
        ))}
      </div>

      {showModal && (
        <div className="fixed inset-0 bg-black/40 backdrop-blur-sm z-50 flex items-center justify-center p-4">
          <div className="bg-white rounded-2xl p-6 w-full max-w-md space-y-4 shadow-xl border border-gray-100">
            <h3 className="font-semibold text-gray-900 text-sm">Submit Anonymous Suggestion / Grievance</h3>
            <form onSubmit={handleSubmit} className="space-y-3">
              <div>
                <label className="block text-xs font-medium text-gray-700 mb-1">Feedback Category</label>
                <select
                  value={category}
                  onChange={e => setCategory(e.target.value as any)}
                  className="w-full text-xs border border-gray-200 rounded-lg p-2.5 bg-white focus:ring-2 focus:ring-indigo-500"
                >
                  <option value="Curriculum">Academic Curriculum & Labs</option>
                  <option value="Hostel Facilities">Hostel Facilities & Mess</option>
                  <option value="Library & Wi-Fi">Library & Wi-Fi Network</option>
                  <option value="Exam Evaluation">Exam Evaluation & Grading</option>
                </select>
              </div>

              <div>
                <label className="block text-xs font-medium text-gray-700 mb-1">Feedback Detail / Suggestion</label>
                <textarea
                  rows={3}
                  value={subject}
                  onChange={e => setSubject(e.target.value)}
                  className="w-full text-xs border border-gray-200 rounded-lg p-2.5 focus:ring-2 focus:ring-indigo-500 focus:outline-none"
                  placeholder="Type your feedback or improvement suggestion..."
                  required
                />
              </div>

              <label className="flex items-center gap-2 text-xs text-gray-600 cursor-pointer">
                <input
                  type="checkbox"
                  checked={anonymous}
                  onChange={e => setAnonymous(e.target.checked)}
                  className="rounded text-indigo-600 focus:ring-indigo-500"
                />
                <span>Keep submission strictly anonymous (Identity hidden from HOD)</span>
              </label>

              <div className="flex justify-end gap-2 pt-2">
                <button
                  type="button"
                  onClick={() => setShowModal(false)}
                  className="px-4 py-2 text-xs text-gray-600 hover:bg-gray-100 rounded-lg"
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  className="px-4 py-2 text-xs font-medium bg-indigo-600 hover:bg-indigo-700 text-white rounded-lg flex items-center gap-1"
                >
                  <Send className="w-3.5 h-3.5" /> Submit to HOD
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
};
