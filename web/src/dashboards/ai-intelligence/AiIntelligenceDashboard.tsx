import React from 'react';
import { StatCard } from '../../components/charts/StatCard';
import { Sparkles, Brain, Bot, Zap } from 'lucide-react';

export const AiIntelligenceDashboard: React.FC = () => {
  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold text-white tracking-tight flex items-center gap-2">
          <Sparkles className="w-6 h-6 text-amber-400" /> AI Intelligence & Predictive Copilot
        </h1>
        <p className="text-xs text-slate-400">Dropout risk prediction, smart RAG document queries, and AI grading analytics</p>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <StatCard title="Predictive Risk Detections" value="14 Students" change="Flagged Early" changeType="warning" icon={<Brain className="w-5 h-5" />} />
        <StatCard title="AI Copilot Queries Resolved" value="14,290" change="Avg 1.2s response" changeType="positive" icon={<Bot className="w-5 h-5" />} iconBg="bg-sky-500/10 text-sky-400" />
        <StatCard title="Automated Assignment Suggestions" value="840 Papers" icon={<Zap className="w-5 h-5" />} iconBg="bg-emerald-500/10 text-emerald-400" />
        <StatCard title="RAG Knowledge Vectors" value="1.2 Million" icon={<Sparkles className="w-5 h-5" />} iconBg="bg-purple-500/10 text-purple-400" />
      </div>
    </div>
  );
};
