import React, { useState } from "react";
import { FeeInstallmentSchedule, InstallmentItem } from "../components/Finance/FeeInstallmentSchedule";

export const FinanceGatewayPage: React.FC = () => {
  const [installments] = useState<InstallmentItem[]>([
    { installment_number: 1, amount: 2500, due_date: "2026-01-15", status: "PAID", paid_date: "2026-01-12" },
    { installment_number: 2, amount: 2500, due_date: "2026-03-15", status: "PENDING" },
    { installment_number: 3, amount: 2500, due_date: "2026-05-15", status: "PENDING" },
  ]);

  return (
    <div className="min-h-screen bg-slate-900 text-slate-100 p-6 space-y-6">
      <div className="flex justify-between items-center border-b border-slate-800 pb-6">
        <div>
          <h1 className="text-3xl font-extrabold text-slate-100">Enterprise Finance & Payment Gateways</h1>
          <p className="text-slate-400 mt-1">Configure multi-tenant gateway keys, fee installment plans, and reconciliation webhooks.</p>
        </div>
      </div>

      <FeeInstallmentSchedule studentName="Jessica Taylor" totalFee={7500} installments={installments} />
    </div>
  );
};
