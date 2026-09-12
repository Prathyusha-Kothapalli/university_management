import React from "react";

export interface InstallmentItem {
  installment_number: number;
  amount: number;
  due_date: string;
  status: "PENDING" | "PAID" | "OVERDUE";
  paid_date?: string;
}

interface FeeInstallmentScheduleProps {
  studentName: string;
  totalFee: number;
  installments: InstallmentItem[];
}

export const FeeInstallmentSchedule: React.FC<FeeInstallmentScheduleProps> = ({
  studentName,
  totalFee,
  installments,
}) => {
  return (
    <div className="bg-slate-800 border border-slate-700 rounded-xl p-6 shadow-xl space-y-4">
      <div className="flex justify-between items-center border-b border-slate-700 pb-4">
        <div>
          <h3 className="text-xl font-bold text-slate-100">Fee Payment Installment Schedule</h3>
          <p className="text-sm text-slate-400">Student: <strong className="text-slate-200">{studentName}</strong></p>
        </div>
        <div className="text-right">
          <span className="text-xs text-slate-400 block uppercase">Total Academic Fee</span>
          <span className="text-2xl font-extrabold font-mono text-indigo-400">${totalFee.toLocaleString()}</span>
        </div>
      </div>

      <div className="space-y-3">
        {installments.map((inst) => (
          <div
            key={inst.installment_number}
            className="p-4 bg-slate-900/60 border border-slate-700/60 rounded-lg flex items-center justify-between"
          >
            <div className="flex items-center space-x-4">
              <div className="w-10 h-10 rounded-full bg-slate-800 border border-slate-700 flex items-center justify-center font-bold text-indigo-400 font-mono">
                #{inst.installment_number}
              </div>
              <div>
                <span className="text-base font-semibold text-slate-100">${inst.amount.toLocaleString()}</span>
                <span className="block text-xs text-slate-400">Due Date: {new Date(inst.due_date).toLocaleDateString()}</span>
              </div>
            </div>

            <div>
              {inst.status === "PAID" ? (
                <span className="px-3 py-1 text-xs font-semibold bg-emerald-500/10 text-emerald-400 border border-emerald-500/30 rounded-full">
                  Paid on {inst.paid_date ? new Date(inst.paid_date).toLocaleDateString() : "Time"}
                </span>
              ) : inst.status === "OVERDUE" ? (
                <span className="px-3 py-1 text-xs font-semibold bg-rose-500/10 text-rose-400 border border-rose-500/30 rounded-full">
                  Overdue
                </span>
              ) : (
                <button className="px-3 py-1 text-xs font-semibold bg-indigo-600 hover:bg-indigo-500 text-white rounded-lg transition-colors">
                  Pay Now
                </button>
              )}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
