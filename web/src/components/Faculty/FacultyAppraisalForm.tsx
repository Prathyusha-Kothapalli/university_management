import React, { useState } from "react";

interface FacultyAppraisalFormProps {
  facultyId: string;
  academicYearId: string;
  onSubmit: (appraisalData: any) => Promise<void>;
}

export const FacultyAppraisalForm: React.FC<FacultyAppraisalFormProps> = ({
  facultyId,
  academicYearId,
  onSubmit,
}) => {
  const [teachingScore, setTeachingScore] = useState(4.5);
  const [researchScore, setResearchScore] = useState(4.0);
  const [serviceScore, setServiceScore] = useState(4.2);
  const [selfAssessment, setSelfAssessment] = useState("");
  const [reviewerComments, setReviewerComments] = useState("");
  const [submitting, setSubmitting] = useState(false);
  const [success, setSuccess] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setSubmitting(true);
    try {
      await onSubmit({
        faculty_id: facultyId,
        academic_year_id: academicYearId,
        teaching_score: teachingScore,
        research_score: researchScore,
        service_score: serviceScore,
        self_assessment: selfAssessment,
        reviewer_comments: reviewerComments,
      });
      setSuccess(true);
    } catch (err) {
      console.error(err);
    } finally {
      setSubmitting(false);
    }
  };

  const calculatedOverall = (teachingScore * 0.4 + researchScore * 0.4 + serviceScore * 0.2).toFixed(2);

  return (
    <div className="bg-slate-800 border border-slate-700 rounded-xl p-6 shadow-xl">
      <h3 className="text-xl font-bold text-slate-100 mb-2">Faculty Annual Appraisal Submission</h3>
      <p className="text-sm text-slate-400 mb-6">
        Submit performance ratings across teaching, research contributions, and institutional service.
      </p>

      {success && (
        <div className="mb-6 p-4 bg-emerald-500/10 border border-emerald-500/30 rounded-lg text-emerald-400 text-sm">
          Faculty appraisal submitted successfully! Computed Overall Score: <strong>{calculatedOverall} / 5.0</strong>
        </div>
      )}

      <form onSubmit={handleSubmit} className="space-y-5">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div>
            <label className="block text-xs font-semibold uppercase tracking-wider text-slate-300 mb-2">
              Teaching Score (40% Weight)
            </label>
            <input
              type="number"
              min="1"
              max="5"
              step="0.1"
              value={teachingScore}
              onChange={(e) => setTeachingScore(parseFloat(e.target.value))}
              className="w-full px-3 py-2 bg-slate-900 border border-slate-700 rounded-lg text-slate-100 font-mono focus:outline-none focus:border-indigo-500"
            />
          </div>

          <div>
            <label className="block text-xs font-semibold uppercase tracking-wider text-slate-300 mb-2">
              Research Score (40% Weight)
            </label>
            <input
              type="number"
              min="1"
              max="5"
              step="0.1"
              value={researchScore}
              onChange={(e) => setResearchScore(parseFloat(e.target.value))}
              className="w-full px-3 py-2 bg-slate-900 border border-slate-700 rounded-lg text-slate-100 font-mono focus:outline-none focus:border-indigo-500"
            />
          </div>

          <div>
            <label className="block text-xs font-semibold uppercase tracking-wider text-slate-300 mb-2">
              Service Score (20% Weight)
            </label>
            <input
              type="number"
              min="1"
              max="5"
              step="0.1"
              value={serviceScore}
              onChange={(e) => setServiceScore(parseFloat(e.target.value))}
              className="w-full px-3 py-2 bg-slate-900 border border-slate-700 rounded-lg text-slate-100 font-mono focus:outline-none focus:border-indigo-500"
            />
          </div>
        </div>

        <div className="p-4 bg-slate-900/60 border border-slate-700/60 rounded-lg flex justify-between items-center">
          <span className="text-sm font-medium text-slate-300">Weighted Overall Rating:</span>
          <span className="text-xl font-bold font-mono text-indigo-400">{calculatedOverall} / 5.0</span>
        </div>

        <div>
          <label className="block text-sm font-medium text-slate-300 mb-1">
            Faculty Self-Assessment Statement
          </label>
          <textarea
            rows={4}
            value={selfAssessment}
            onChange={(e) => setSelfAssessment(e.target.value)}
            placeholder="Highlight key achievements, curriculum innovations, publications, and administrative contributions..."
            className="w-full px-3 py-2 bg-slate-900 border border-slate-700 rounded-lg text-slate-100 text-sm focus:outline-none focus:border-indigo-500"
          />
        </div>

        <div>
          <label className="block text-sm font-medium text-slate-300 mb-1">
            Department Chair / Peer Reviewer Comments
          </label>
          <textarea
            rows={3}
            value={reviewerComments}
            onChange={(e) => setReviewerComments(e.target.value)}
            placeholder="Evaluator feedback and recommendations for professional development..."
            className="w-full px-3 py-2 bg-slate-900 border border-slate-700 rounded-lg text-slate-100 text-sm focus:outline-none focus:border-indigo-500"
          />
        </div>

        <div className="flex justify-end">
          <button
            type="submit"
            disabled={submitting}
            className="px-5 py-2.5 bg-indigo-600 hover:bg-indigo-500 text-white font-semibold text-sm rounded-lg shadow-md transition-colors disabled:opacity-50"
          >
            {submitting ? "Submitting Appraisal..." : "Submit Annual Appraisal"}
          </button>
        </div>
      </form>
    </div>
  );
};
