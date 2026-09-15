import React, { useState } from "react";
import { AcademicHoldModal } from "../components/StudentLifecycle/AcademicHoldModal";
import { SupportCaseCard, SupportCaseData } from "../components/StudentLifecycle/SupportCaseCard";

export const StudentLifecyclePage: React.FC = () => {
  const [isHoldModalOpen, setIsHoldModalOpen] = useState(false);
  const [activeTab, setActiveTab] = useState<"holds" | "support" | "conduct">("holds");

  const [holds, setHolds] = useState([
    {
      id: "hold-001",
      student_id: "stud-9921",
      student_name: "Alex Mercer",
      hold_type: "FINANCIAL",
      reason: "Outstanding Spring Semester Tuition Fee ($2,450)",
      placed_at: "2026-02-15",
    },
    {
      id: "hold-002",
      student_id: "stud-8812",
      student_name: "Sophia Chen",
      hold_type: "DOCUMENT_MISSING",
      reason: "High School Final Transcript Official Copy Pending",
      placed_at: "2026-03-01",
    },
  ]);

  const [supportCases, setSupportCases] = useState<SupportCaseData[]>([
    {
      id: "case-7701-44",
      student_id: "stud-9921",
      subject: "Academic Probation Appeal & Advisory Support",
      category: "ACADEMIC_ADVISING",
      priority: "HIGH",
      status: "OPEN",
      details: "Requesting academic plan review for grade improvement in Algorithms and Data Structures.",
      created_at: "2026-03-10T10:30:00Z",
    },
    {
      id: "case-8812-99",
      student_id: "stud-8812",
      subject: "Hostel Allocation Transfer Request",
      category: "HOSTEL_ISSUE",
      priority: "MEDIUM",
      status: "IN_PROGRESS",
      details: "Student requesting quiet study block transfer due to upcoming graduate entrance exams.",
      created_at: "2026-03-08T14:15:00Z",
    },
  ]);

  const handlePlaceHold = async (studentId: string, holdType: string, reason: string) => {
    const newHold = {
      id: `hold-${Date.now().toString().slice(-4)}`,
      student_id: studentId,
      student_name: `Student (${studentId.substring(0, 6)})`,
      hold_type: holdType,
      reason: reason,
      placed_at: new Date().toISOString().split("T")[0],
    };
    setHolds([newHold, ...holds]);
  };

  const handleUpdateSupportStatus = (caseId: string, newStatus: string) => {
    setSupportCases((prev) =>
      prev.map((c) => (c.id === caseId ? { ...c, status: newStatus as any } : c))
    );
  };

  return (
    <div className="min-h-screen bg-slate-900 text-slate-100 p-6 space-y-6">
      <div className="flex flex-col md:flex-row justify-between items-start md:items-center gap-4 border-b border-slate-800 pb-6">
        <div>
          <h1 className="text-3xl font-extrabold text-slate-100">Student Lifecycle & Advising</h1>
          <p className="text-slate-400 mt-1">
            Manage academic holds, student conduct cases, advising support, and student achievements.
          </p>
        </div>
        <button
          onClick={() => setIsHoldModalOpen(true)}
          className="px-4 py-2 bg-rose-600 hover:bg-rose-500 text-white font-semibold text-sm rounded-lg shadow-lg transition-colors"
        >
          + Place Academic Hold
        </button>
      </div>

      {/* Tabs */}
      <div className="flex space-x-2 border-b border-slate-800">
        <button
          onClick={() => setActiveTab("holds")}
          className={`px-4 py-2.5 font-medium text-sm border-b-2 transition-colors ${
            activeTab === "holds"
              ? "border-indigo-500 text-indigo-400 font-semibold"
              : "border-transparent text-slate-400 hover:text-slate-200"
          }`}
        >
          Active Academic Holds ({holds.length})
        </button>
        <button
          onClick={() => setActiveTab("support")}
          className={`px-4 py-2.5 font-medium text-sm border-b-2 transition-colors ${
            activeTab === "support"
              ? "border-indigo-500 text-indigo-400 font-semibold"
              : "border-transparent text-slate-400 hover:text-slate-200"
          }`}
        >
          Advising & Support Cases ({supportCases.length})
        </button>
      </div>

      {/* Content */}
      {activeTab === "holds" && (
        <div className="bg-slate-800 border border-slate-700 rounded-xl overflow-hidden shadow-xl">
          <table className="w-full text-left border-collapse">
            <thead>
              <tr className="bg-slate-900/70 text-xs font-semibold text-slate-400 uppercase tracking-wider border-b border-slate-700">
                <th className="py-3 px-4">Student</th>
                <th className="py-3 px-4">Hold Category</th>
                <th className="py-3 px-4">Reason / Notes</th>
                <th className="py-3 px-4">Date Placed</th>
                <th className="py-3 px-4 text-right">Actions</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-700/60 text-sm">
              {holds.map((h) => (
                <tr key={h.id} className="hover:bg-slate-700/30 transition-colors">
                  <td className="py-3 px-4">
                    <span className="font-semibold text-slate-100 block">{h.student_name}</span>
                    <span className="text-xs font-mono text-slate-400">{h.student_id}</span>
                  </td>
                  <td className="py-3 px-4">
                    <span className="px-2.5 py-1 text-xs font-semibold bg-rose-500/10 text-rose-400 border border-rose-500/20 rounded-full">
                      {h.hold_type}
                    </span>
                  </td>
                  <td className="py-3 px-4 text-slate-300 max-w-xs truncate">{h.reason}</td>
                  <td className="py-3 px-4 font-mono text-xs text-slate-400">{h.placed_at}</td>
                  <td className="py-3 px-4 text-right">
                    <button
                      onClick={() => setHolds(holds.filter((item) => item.id !== h.id))}
                      className="px-3 py-1 bg-slate-700 hover:bg-emerald-600 text-xs font-medium text-slate-200 rounded transition-colors"
                    >
                      Resolve Hold
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      {activeTab === "support" && (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {supportCases.map((c) => (
            <SupportCaseCard key={c.id} caseData={c} onUpdateStatus={handleUpdateSupportStatus} />
          ))}
        </div>
      )}

      <AcademicHoldModal
        isOpen={isHoldModalOpen}
        onClose={() => setIsHoldModalOpen(false)}
        onSubmit={handlePlaceHold}
      />
    </div>
  );
};
