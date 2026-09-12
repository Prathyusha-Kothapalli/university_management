import React, { useState } from "react";

export interface ChunkInfo {
  chunk_id: str;
  document_id: str;
  section: str;
  content: str;
  word_count: number;
}

interface VectorCollectionManagerProps {
  chunks: ChunkInfo[];
  onIngestClick?: () => void;
}

export const VectorCollectionManager: React.FC<VectorCollectionManagerProps> = ({
  chunks,
  onIngestClick,
}) => {
  return (
    <div className="bg-slate-800 border border-slate-700 rounded-xl p-6 shadow-xl space-y-4">
      <div className="flex justify-between items-center">
        <div>
          <h3 className="text-xl font-bold text-slate-100">Vector Collection & Knowledge Chunks</h3>
          <p className="text-sm text-slate-400">Indexed document windows with dense vector & BM25 sparse attributes.</p>
        </div>
        {onIngestClick && (
          <button
            onClick={onIngestClick}
            className="px-4 py-2 bg-indigo-600 hover:bg-indigo-500 text-white font-medium text-sm rounded-lg transition-colors"
          >
            + Ingest Markdown Document
          </button>
        )}
      </div>

      <div className="space-y-3">
        {chunks.map((chk) => (
          <div key={chk.chunk_id} className="p-4 bg-slate-900/60 border border-slate-700/60 rounded-lg space-y-2">
            <div className="flex justify-between items-center">
              <span className="text-xs font-mono font-bold text-indigo-400">{chk.chunk_id}</span>
              <span className="text-xs px-2 py-0.5 bg-slate-800 text-slate-300 rounded font-medium">{chk.section}</span>
            </div>
            <p className="text-sm text-slate-200">{chk.content}</p>
            <div className="text-right text-xs text-slate-500 font-mono">
              Document: {chk.document_id} • Words: {chk.word_count}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
