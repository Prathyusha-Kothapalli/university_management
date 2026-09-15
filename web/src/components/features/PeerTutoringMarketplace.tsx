import React, { useState } from 'react';
import { BookOpen, Star, Calendar, CheckCircle, Award } from 'lucide-react';

interface TutorSession {
  id: string;
  tutorName: string;
  subject: string;
  rating: number;
  creditsPerHour: number;
  availableSlot: string;
}

export const PeerTutoringMarketplace: React.FC = () => {
  const [tutors] = useState<TutorSession[]>([
    { id: 'tut-1', tutorName: 'Ananya Roy (Senior CSE)', subject: 'Data Structures & Graph Algorithms', rating: 4.9, creditsPerHour: 15, availableSlot: 'Today, 05:00 PM' },
    { id: 'tut-2', tutorName: 'Sameer Sen (M.Tech AI)', subject: 'PyTorch & Neural Networks Lab', rating: 4.8, creditsPerHour: 20, availableSlot: 'Tomorrow, 04:00 PM' },
  ]);

  const [bookedId, setBookedId] = useState<string | null>(null);

  const handleBook = (id: string) => {
    setBookedId(id);
    setTimeout(() => setBookedId(null), 2500);
  };

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-5">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-3">
          <div className="p-2.5 bg-blue-50 text-blue-600 rounded-lg">
            <BookOpen className="w-5 h-5" />
          </div>
          <div>
            <h3 className="font-semibold text-gray-900">Peer-to-Peer Tutoring Exchange</h3>
            <p className="text-xs text-gray-500">Book 1-on-1 peer tutoring sessions with senior student toppers</p>
          </div>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
        {tutors.map(t => (
          <div key={t.id} className="p-4 rounded-xl border border-gray-100 bg-gray-50/40 flex items-center justify-between">
            <div className="space-y-1">
              <div className="flex items-center gap-2">
                <h4 className="font-bold text-xs text-gray-900">{t.tutorName}</h4>
                <span className="text-xs text-amber-500 font-bold flex items-center gap-0.5">
                  <Star className="w-3.5 h-3.5 fill-amber-400" /> {t.rating}
                </span>
              </div>
              <p className="text-xs text-blue-600 font-medium">{t.subject}</p>
              <div className="flex items-center gap-3 text-[11px] text-gray-400">
                <span className="flex items-center gap-1">
                  <Calendar className="w-3 h-3 text-blue-500" /> {t.availableSlot}
                </span>
                <span className="flex items-center gap-1 font-semibold text-blue-700">
                  <Award className="w-3 h-3 text-blue-500" /> {t.creditsPerHour} Credits/hr
                </span>
              </div>
            </div>

            <button
              onClick={() => handleBook(t.id)}
              className={`text-xs font-semibold px-3.5 py-2 rounded-lg flex items-center gap-1 transition-all shrink-0 ${
                bookedId === t.id
                  ? 'bg-emerald-600 text-white'
                  : 'bg-blue-600 hover:bg-blue-700 text-white shadow-sm'
              }`}
            >
              {bookedId === t.id ? (
                <>
                  <CheckCircle className="w-3.5 h-3.5" /> Booked
                </>
              ) : (
                'Book Tutoring'
              )}
            </button>
          </div>
        ))}
      </div>
    </div>
  );
};
