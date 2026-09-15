import React, { useState } from 'react';
import { HelpCircle, Sparkles, Copy, CheckCircle2 } from 'lucide-react';

interface Question {
  id: string;
  type: 'Multiple Choice' | 'Short Answer' | 'Coding Proof';
  bloomsLevel: 'Analyze' | 'Evaluate' | 'Apply' | 'Remember';
  promptText: string;
  marks: number;
}

export const AiExamQuestionGenerator: React.FC = () => {
  const [subject, setSubject] = useState('Operating Systems');
  const [difficulty, setDifficulty] = useState('Medium');
  const [questions, setQuestions] = useState<Question[]>([
    {
      id: 'q-101',
      type: 'Multiple Choice',
      bloomsLevel: 'Analyze',
      promptText: 'In a Banker\'s Algorithm execution, if Allocation = [2, 1, 0] and Need = [1, 2, 2], calculate if system is in safe state.',
      marks: 5
    },
    {
      id: 'q-102',
      type: 'Coding Proof',
      bloomsLevel: 'Evaluate',
      promptText: 'Write a C++ program implementing Producer-Consumer solution using POSIX semaphores and mutex locks.',
      marks: 10
    }
  ]);

  const [copiedId, setCopiedId] = useState<string | null>(null);

  const handleGenerate = (e: React.FormEvent) => {
    e.preventDefault();
    const newQ: Question = {
      id: `q-${Math.floor(100 + Math.random() * 900)}`,
      type: 'Short Answer',
      bloomsLevel: 'Apply',
      promptText: `Explain the memory fragmentation trade-off between Paging vs Segmentation in ${subject}.`,
      marks: 5
    };
    setQuestions([newQ, ...questions]);
  };

  const handleCopy = (id: string) => {
    setCopiedId(id);
    setTimeout(() => setCopiedId(null), 2000);
  };

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-5">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-3">
          <div className="p-2.5 bg-indigo-50 text-indigo-600 rounded-lg">
            <HelpCircle className="w-5 h-5" />
          </div>
          <div>
            <h3 className="font-semibold text-gray-900">AI Exam Question & Quiz Draft Generator</h3>
            <p className="text-xs text-gray-500">Bloom's Taxonomy-aligned exam paper question generator for faculty</p>
          </div>
        </div>
      </div>

      <form onSubmit={handleGenerate} className="grid grid-cols-1 md:grid-cols-3 gap-3 bg-gray-50 p-3.5 rounded-xl border border-gray-100 mb-4">
        <div>
          <label className="block text-xs font-medium text-gray-700 mb-1">Target Subject</label>
          <input
            type="text"
            value={subject}
            onChange={e => setSubject(e.target.value)}
            className="w-full text-xs border border-gray-200 rounded-lg p-2 bg-white focus:ring-2 focus:ring-indigo-500"
            required
          />
        </div>

        <div>
          <label className="block text-xs font-medium text-gray-700 mb-1">Difficulty Level</label>
          <select
            value={difficulty}
            onChange={e => setDifficulty(e.target.value)}
            className="w-full text-xs border border-gray-200 rounded-lg p-2 bg-white focus:ring-2 focus:ring-indigo-500"
          >
            <option value="Easy">Easy (Knowledge / Recall)</option>
            <option value="Medium">Medium (Application / Analysis)</option>
            <option value="Hard">Hard (Evaluation / Synthesis)</option>
          </select>
        </div>

        <div className="flex items-end">
          <button
            type="submit"
            className="w-full bg-indigo-600 hover:bg-indigo-700 text-white text-xs font-semibold py-2 px-3 rounded-lg flex items-center justify-center gap-1.5 transition-colors"
          >
            <Sparkles className="w-4 h-4" />
            Generate Question
          </button>
        </div>
      </form>

      <div className="space-y-3">
        {questions.map(q => (
          <div key={q.id} className="p-4 rounded-xl border border-gray-100 bg-white shadow-xs space-y-2">
            <div className="flex items-center justify-between">
              <div className="flex items-center gap-2">
                <span className="text-[10px] font-bold bg-indigo-100 text-indigo-800 px-2.5 py-0.5 rounded-full">
                  {q.type}
                </span>
                <span className="text-[10px] bg-purple-50 text-purple-700 font-semibold px-2 py-0.5 rounded-full">
                  Bloom: {q.bloomsLevel}
                </span>
                <span className="text-xs font-bold text-gray-700 font-mono">[{q.marks} Marks]</span>
              </div>

              <button
                onClick={() => handleCopy(q.id)}
                className="text-xs text-gray-500 hover:text-indigo-600 flex items-center gap-1"
              >
                {copiedId === q.id ? (
                  <span className="text-emerald-600 font-bold flex items-center gap-0.5">
                    <CheckCircle2 className="w-3.5 h-3.5" /> Copied
                  </span>
                ) : (
                  <>
                    <Copy className="w-3.5 h-3.5" /> Copy
                  </>
                )}
              </button>
            </div>

            <p className="text-xs text-gray-800 font-medium">{q.promptText}</p>
          </div>
        ))}
      </div>
    </div>
  );
};
