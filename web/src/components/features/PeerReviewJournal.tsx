import React, { useState } from 'react';
import { BookOpen, CheckCircle, Clock } from 'lucide-react';

interface JournalPaper {
  id: string;
  title: string;
  author: string;
  submittedDate: string;
  reviewStatus: 'Peer Review Completed' | 'Revisions Requested' | 'Under Blind Review';
  targetConference: string;
}

export const PeerReviewJournal: React.FC = () => {
  const [papers] = useState<JournalPaper[]>([
    {
      id: 'JRN-101',
      title: 'Federated Learning for Privacy-Preserving Medical Record Analysis',
      author: 'Alex Morgan & Dr. Ananya Sharma',
      submittedDate: '2026-08-28',
      reviewStatus: 'Peer Review Completed',
      targetConference: 'IEEE Transactions on Neural Networks 2026'
    },
    {
      id: 'JRN-102',
      title: 'Zero-Knowledge Cryptography in Decoupled Blockchain Networks',
      author: 'Vikram Mehta',
      submittedDate: '2026-09-02',
      reviewStatus: 'Under Blind Review',
      targetConference: 'ACM Conference on Computer & Communications Security'
    }
  ]);

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-5">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-3">
          <div className="p-2.5 bg-indigo-50 text-indigo-600 rounded-lg">
            <BookOpen className="w-5 h-5" />
          </div>
          <div>
            <h3 className="font-semibold text-gray-900">Department Peer-Review Journal Portal</h3>
            <p className="text-xs text-gray-500">Internal peer review workflow before international conference & journal submissions</p>
          </div>
        </div>
      </div>

      <div className="space-y-3">
        {papers.map(p => (
          <div key={p.id} className="p-4 rounded-xl border border-gray-100 bg-gray-50/40 space-y-2">
            <div className="flex items-center justify-between">
              <span className="text-[10px] font-bold text-indigo-700 bg-indigo-100 px-2.5 py-0.5 rounded-full">
                {p.targetConference}
              </span>
              <span className={`text-[11px] font-semibold px-2.5 py-0.5 rounded-full flex items-center gap-1 ${
                p.reviewStatus === 'Peer Review Completed' ? 'bg-emerald-50 text-emerald-700' : 'bg-amber-50 text-amber-700'
              }`}>
                {p.reviewStatus === 'Peer Review Completed' ? <CheckCircle className="w-3.5 h-3.5 text-emerald-600" /> : <Clock className="w-3.5 h-3.5 text-amber-600" />}
                {p.reviewStatus}
              </span>
            </div>

            <h4 className="font-bold text-xs text-gray-900">{p.title}</h4>
            <div className="flex items-center justify-between text-xs text-gray-500 pt-1 border-t border-gray-100">
              <span>Author(s): <strong>{p.author}</strong></span>
              <span className="text-[11px] text-gray-400">Submitted: {p.submittedDate}</span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
