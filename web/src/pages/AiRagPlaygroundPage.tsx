import React, { useState } from "react";
import { VectorCollectionManager, ChunkInfo } from "../components/AI/VectorCollectionManager";

export const AiRagPlaygroundPage: React.FC = () => {
  const [chunks] = useState<ChunkInfo[]>([
    {
      chunk_id: "doc_policy_01_chk_0",
      document_id: "doc_academic_regulations_2026",
      section: "Attendance Policy",
      content: "Students must maintain a minimum of 75% attendance in all enrolled courses to be eligible for end-semester examinations. Exemptions require HOD approval.",
      word_count: 24,
    },
    {
      chunk_id: "doc_obe_01_chk_1",
      document_id: "doc_obe_accreditation_guide",
      section: "CO-PO Attainment",
      content: "Course Outcomes (COs) are mapped directly to Program Outcomes (POs) with weights 1 (Low), 2 (Medium), and 3 (High) under NBA/ABET standards.",
      word_count: 26,
    },
  ]);

  const [query, setQuery] = useState("");
  const [results, setResults] = useState<any[]>([]);

  const handleSearch = (e: React.FormEvent) => {
    e.preventDefault();
    setResults([
      {
        chunk_id: "doc_policy_01_chk_0",
        content: "Students must maintain a minimum of 75% attendance in all enrolled courses...",
        score: 0.94,
        dense: 0.92,
        sparse: 0.98,
      },
    ]);
  };

  return (
    <div className="min-h-screen bg-slate-900 text-slate-100 p-6 space-y-6">
      <div className="flex justify-between items-center border-b border-slate-800 pb-6">
        <div>
          <h1 className="text-3xl font-extrabold text-slate-100">AI RAG & Hybrid Vector Playground</h1>
          <p className="text-slate-400 mt-1">Test hybrid dense/sparse vector search, similarity reranking, and document chunking.</p>
        </div>
      </div>

      <form onSubmit={handleSearch} className="bg-slate-800 p-6 rounded-xl border border-slate-700 shadow-xl space-y-4">
        <div>
          <label className="block text-sm font-semibold text-slate-300 mb-2">Query Knowledge Base</label>
          <div className="flex gap-3">
            <input
              type="text"
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              placeholder="e.g. What is the minimum attendance requirement for final exams?"
              className="flex-1 px-4 py-2.5 bg-slate-900 border border-slate-700 rounded-lg text-slate-100 focus:outline-none focus:border-indigo-500"
            />
            <button
              type="submit"
              className="px-6 py-2.5 bg-indigo-600 hover:bg-indigo-500 text-white font-semibold text-sm rounded-lg transition-colors shadow-md"
            >
              Hybrid Search
            </button>
          </div>
        </div>
      </form>

      {results.length > 0 && (
        <div className="bg-slate-800 border border-slate-700 rounded-xl p-6 shadow-xl space-y-3">
          <h3 className="text-lg font-bold text-slate-100">Top Hybrid Retrieval Match</h3>
          {results.map((r) => (
            <div key={r.chunk_id} className="p-4 bg-slate-900/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
              <div>
                <span className="text-xs font-mono text-indigo-400 font-bold">{r.chunk_id}</span>
                <p className="text-sm text-slate-200 mt-1">{r.content}</p>
              </div>
              <div className="text-right font-mono">
                <span className="text-lg font-bold text-emerald-400">{r.score}</span>
                <span className="block text-[10px] text-slate-400">Dense: {r.dense} | Sparse: {r.sparse}</span>
              </div>
            </div>
          ))}
        </div>
      )}

      <VectorCollectionManager chunks={chunks} />
    </div>
  );
};
