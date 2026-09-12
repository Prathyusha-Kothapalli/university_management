import React from "react";

export interface SupportCaseData {
  id: string;
  student_id: string;
  subject: string;
  category: string;
  priority: "LOW" | "MEDIUM" | "HIGH" | "URGENT";
  status: "OPEN" | "IN_PROGRESS" | "RESOLVED" | "CLOSED";
  details: string;
  created_at: string;
}

interface SupportCaseCardProps {
  caseData: SupportCaseData;
  onUpdateStatus?: (caseId: string, newStatus: string) => void;
}

export const SupportCaseCard: React.FC<SupportCaseCardProps> = ({
  caseData,
  onUpdateStatus,
}) => {
  const getPriorityBadge = (priority: string) => {
    switch (priority) {
      case "URGENT":
        return "bg-rose-500/10 text-rose-400 border-rose-500/20";
      case "HIGH":
        return "bg-amber-500/10 text-amber-400 border-amber-500/20";
      case "MEDIUM":
        return "bg-blue-500/10 text-blue-400 border-blue-500/20";
      default:
        return "bg-slate-500/10 text-slate-400 border-slate-500/20";
    }
  };

  const getStatusBadge = (status: string) => {
    switch (status) {
      case "RESOLVED":
        return "bg-emerald-500/10 text-emerald-400 border-emerald-500/20";
      case "IN_PROGRESS":
        return "bg-indigo-500/10 text-indigo-400 border-indigo-500/20";
      case "OPEN":
        return "bg-amber-500/10 text-amber-400 border-amber-500/20";
      default:
        return "bg-slate-500/10 text-slate-400 border-slate-500/20";
    }
  };

  return (
    <div className="bg-slate-800/80 border border-slate-700 rounded-xl p-5 shadow-lg hover:border-slate-600 transition-all">
      <div className="flex justify-between items-start mb-3">
        <div>
          <span className="text-xs font-mono text-slate-400">ID: {caseData.id.substring(0, 8)}...</span>
          <h4 className="text-base font-semibold text-slate-100 mt-1">{caseData.subject}</h4>
        </div>
        <div className="flex space-x-2">
          <span className={`px-2.5 py-0.5 text-xs font-medium border rounded-full ${getPriorityBadge(caseData.priority)}`}>
            {caseData.priority}
          </span>
          <span className={`px-2.5 py-0.5 text-xs font-medium border rounded-full ${getStatusBadge(caseData.status)}`}>
            {caseData.status}
          </span>
        </div>
      </div>

      <p className="text-sm text-slate-300 mb-4 line-clamp-2">{caseData.details}</p>

      <div className="flex justify-between items-center text-xs text-slate-400 pt-3 border-t border-slate-700/60">
        <span>Category: <strong className="text-slate-200 font-normal">{caseData.category}</strong></span>
        <span>{new Date(caseData.created_at).toLocaleDateString()}</span>
      </div>

      {onUpdateStatus && caseData.status !== "RESOLVED" && (
        <div className="mt-4 pt-3 border-t border-slate-700/60 flex justify-end space-x-2">
          <button
            onClick={() => onUpdateStatus(caseData.id, "IN_PROGRESS")}
            className="px-3 py-1 bg-slate-700 hover:bg-slate-600 text-xs font-medium text-slate-200 rounded-md transition-colors"
          >
            Mark In Progress
          </button>
          <button
            onClick={() => onUpdateStatus(caseData.id, "RESOLVED")}
            className="px-3 py-1 bg-emerald-600 hover:bg-emerald-500 text-xs font-medium text-white rounded-md transition-colors"
          >
            Resolve Case
          </button>
        </div>
      )}
    </div>
  );
};
