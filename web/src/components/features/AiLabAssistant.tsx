import React, { useState } from 'react';
import { Terminal, Play } from 'lucide-react';

export const AiLabAssistant: React.FC = () => {
  const [codeSnippet, setCodeSnippet] = useState(
    `#include <iostream>\nusing namespace std;\n\nint main() {\n    int* ptr = NULL;\n    *ptr = 42; // Segmentation Fault!\n    return 0;\n}`
  );
  const [output, setOutput] = useState<string | null>(null);
  const [isDebugging, setIsDebugging] = useState(false);

  const handleDebug = () => {
    setIsDebugging(true);
    setTimeout(() => {
      setIsDebugging(false);
      setOutput(
        `🚨 AI Error Diagnosis (C++ Segmentation Fault):\n` +
        `• Line 6: Dereferencing a NULL pointer '*ptr = 42;'\n` +
        `• Fix: Allocate memory using 'ptr = new int(42);' or check 'if (ptr != NULL)' before dereferencing.`
      );
    }, 1000);
  };

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-5">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-3">
          <div className="p-2.5 bg-slate-100 text-slate-800 rounded-lg">
            <Terminal className="w-5 h-5" />
          </div>
          <div>
            <h3 className="font-semibold text-gray-900">AI Programming Lab Code Debugger</h3>
            <p className="text-xs text-gray-500">Interactive C++, Python & Java runtime exception debugger for lab work</p>
          </div>
        </div>

        <button
          onClick={handleDebug}
          disabled={isDebugging}
          className="bg-slate-900 hover:bg-slate-800 text-white text-xs font-semibold px-4 py-2 rounded-lg flex items-center gap-1.5 transition-colors shadow-sm"
        >
          <Play className={`w-3.5 h-3.5 ${isDebugging ? 'animate-spin' : ''}`} />
          Run AI Code Debugger
        </button>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
        <div>
          <label className="block text-xs font-semibold text-gray-700 mb-1">Source Code Editor (C++ / Python / Java)</label>
          <textarea
            rows={7}
            value={codeSnippet}
            onChange={e => setCodeSnippet(e.target.value)}
            className="w-full font-mono text-xs p-3 border border-gray-200 rounded-xl bg-slate-900 text-emerald-400 focus:ring-2 focus:ring-slate-700 focus:outline-none"
          />
        </div>

        <div>
          <label className="block text-xs font-semibold text-gray-700 mb-1">AI Execution Log & Error Analysis</label>
          <div className="h-44 p-3 rounded-xl border border-gray-200 bg-slate-950 font-mono text-xs text-slate-200 overflow-y-auto whitespace-pre-wrap">
            {output ? (
              <span className="text-amber-400">{output}</span>
            ) : (
              <span className="text-slate-500 italic">Click "Run AI Code Debugger" to analyze syntax, memory leaks, and stack trace errors...</span>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};
