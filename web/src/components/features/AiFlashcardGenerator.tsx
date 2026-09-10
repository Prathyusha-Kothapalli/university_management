import React, { useState } from 'react';
import { Sparkles, RotateCw, CheckCircle2, BookOpen } from 'lucide-react';

interface Flashcard {
  id: number;
  question: string;
  answer: string;
  subject: string;
}

export const AiFlashcardGenerator: React.FC = () => {
  const [cards] = useState<Flashcard[]>([
    { id: 1, question: 'What is the primary difference between a Mutex and a Semaphore in OS?', answer: 'A Mutex is a locking mechanism (only 1 thread accesses resource), whereas a Semaphore is a signaling mechanism allowing N resources.', subject: 'Operating Systems' },
    { id: 2, question: 'Define 3NF (Third Normal Form) in Database Normalization.', answer: 'A relation is in 3NF if it is in 2NF and no non-prime attribute is transitively dependent on the primary key.', subject: 'Database Systems' },
    { id: 3, question: 'What is Vanishing Gradient Problem in Deep Neural Networks?', answer: 'It occurs when gradients shrink exponentially as backpropagation propagates through early layers, preventing weight updates.', subject: 'Machine Learning' },
  ]);

  const [currentIndex, setCurrentIndex] = useState(0);
  const [showAnswer, setShowAnswer] = useState(false);

  const card = cards[currentIndex];

  const handleNext = () => {
    setShowAnswer(false);
    setCurrentIndex((currentIndex + 1) % cards.length);
  };

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-5">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-3">
          <div className="p-2.5 bg-indigo-50 text-indigo-600 rounded-lg">
            <Sparkles className="w-5 h-5" />
          </div>
          <div>
            <h3 className="font-semibold text-gray-900">AI Active Recall Flashcard Generator</h3>
            <p className="text-xs text-gray-500">Auto-generated revision flashcards from course lecture notes & exam syllabi</p>
          </div>
        </div>
        <span className="text-xs font-semibold text-indigo-700 bg-indigo-50 px-3 py-1 rounded-full border border-indigo-100 flex items-center gap-1">
          <BookOpen className="w-3.5 h-3.5" /> Card {currentIndex + 1} of {cards.length}
        </span>
      </div>

      <div
        onClick={() => setShowAnswer(!showAnswer)}
        className="p-6 rounded-2xl border border-indigo-100 bg-indigo-50/30 text-center min-h-[160px] flex flex-col justify-center items-center cursor-pointer transition-all hover:shadow-sm"
      >
        <span className="text-[10px] font-bold text-indigo-700 bg-indigo-100 px-2.5 py-0.5 rounded-full mb-2">
          {card.subject}
        </span>
        <h4 className="font-bold text-sm text-gray-900 mb-2">
          {showAnswer ? 'Answer:' : 'Question:'}
        </h4>
        <p className="text-xs text-gray-700 max-w-lg mx-auto">
          {showAnswer ? card.answer : card.question}
        </p>
        <span className="text-[11px] text-indigo-600 font-semibold mt-3 flex items-center gap-1">
          <RotateCw className="w-3.5 h-3.5" /> {showAnswer ? 'Click to see Question' : 'Click card to reveal Answer'}
        </span>
      </div>

      <div className="flex justify-end gap-2 mt-4">
        <button
          onClick={handleNext}
          className="bg-indigo-600 hover:bg-indigo-700 text-white text-xs font-semibold px-4 py-2 rounded-lg transition-colors flex items-center gap-1 shadow-sm"
        >
          <CheckCircle2 className="w-3.5 h-3.5" /> Next Flashcard
        </button>
      </div>
    </div>
  );
};
