import React, { useState } from "react";
import { FacultyAppraisalForm } from "../components/Faculty/FacultyAppraisalForm";
import { ResearchPublicationsList, PublicationItem } from "../components/Faculty/ResearchPublicationsList";

export const FacultyAppraisalPage: React.FC = () => {
  const [activeTab, setActiveTab] = useState<"appraisal" | "publications">("appraisal");

  const [publications] = useState<PublicationItem[]>([
    {
      id: "pub-01",
      title: "Deep Reinforcement Learning in Multi-Agent Campus Logistics Optimization",
      journal_conference: "IEEE Transactions on Neural Networks and Learning Systems",
      doi: "10.1109/TNNLS.2025.321890",
      publication_date: "2025-11-14",
      citation_count: 24,
      impact_factor: 10.4,
      is_peer_reviewed: true,
    },
    {
      id: "pub-02",
      title: "Outcome-Based Curriculum Alignment in Hybrid Learning Management Environments",
      journal_conference: "ACM Conference on Computer Science Education (SIGCSE)",
      doi: "10.1145/3545945.3569801",
      publication_date: "2026-01-20",
      citation_count: 8,
      impact_factor: 3.8,
      is_peer_reviewed: true,
    },
  ]);

  const handleAppraisalSubmit = async (data: any) => {
    console.log("Appraisal submitted:", data);
  };

  return (
    <div className="min-h-screen bg-slate-900 text-slate-100 p-6 space-y-6">
      <div className="flex justify-between items-center border-b border-slate-800 pb-6">
        <div>
          <h1 className="text-3xl font-extrabold text-slate-100">Faculty Workload & Appraisal Portal</h1>
          <p className="text-slate-400 mt-1">
            Track faculty qualifications, research grant allocations, appraisals, and publication metrics.
          </p>
        </div>
      </div>

      <div className="flex space-x-2 border-b border-slate-800">
        <button
          onClick={() => setActiveTab("appraisal")}
          className={`px-4 py-2.5 font-medium text-sm border-b-2 transition-colors ${
            activeTab === "appraisal"
              ? "border-indigo-500 text-indigo-400 font-semibold"
              : "border-transparent text-slate-400 hover:text-slate-200"
          }`}
        >
          Annual Performance Appraisal
        </button>
        <button
          onClick={() => setActiveTab("publications")}
          className={`px-4 py-2.5 font-medium text-sm border-b-2 transition-colors ${
            activeTab === "publications"
              ? "border-indigo-500 text-indigo-400 font-semibold"
              : "border-transparent text-slate-400 hover:text-slate-200"
          }`}
        >
          Research & Publications ({publications.length})
        </button>
      </div>

      {activeTab === "appraisal" && (
        <div className="max-w-4xl">
          <FacultyAppraisalForm
            facultyId="fac-5510"
            academicYearId="ay-2025-2026"
            onSubmit={handleAppraisalSubmit}
          />
        </div>
      )}

      {activeTab === "publications" && (
        <ResearchPublicationsList publications={publications} />
      )}
    </div>
  );
};
